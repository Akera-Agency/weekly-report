#!/usr/bin/env python3
"""
lint-report.py — Pre-finalize lint gate for weekly reports.

Runs on the report markdown BEFORE it is published to ClickUp. Blocks finalize
if any error-level rule fails. Warnings are reported but do not block.

Usage:
    python3 scripts/lint-report.py <report.md>
    python3 scripts/lint-report.py <report.md> --fix    # auto-fix safe rules

Exit codes:
    0 = clean (or only warnings)
    1 = one or more errors (finalize should be blocked)
    2 = usage / file error
"""

import sys
import re
import argparse

# ---------------------------------------------------------------------------
# Rules
# ---------------------------------------------------------------------------
# Each rule: id, level ("error"|"warn"), a scan function returning a list of
# (line_no, col, message), and an optional fixer(text) -> text.

EM_DASH = "\u2014"   # —
EN_DASH = "\u2013"   # –

def _find_char(lines, ch, msg):
    hits = []
    for i, line in enumerate(lines, 1):
        start = 0
        while True:
            idx = line.find(ch, start)
            if idx == -1:
                break
            hits.append((i, idx + 1, msg))
            start = idx + 1
    return hits


def rule_no_em_dash(lines):
    # Em dashes are banned. Replace with " - " (spaced hyphen) or reword.
    return _find_char(lines, EM_DASH,
                      "Em dash (\u2014) is banned. Use ' - ' or reword.")


def fix_em_dash(text):
    # " word — word " -> " word - word "; tighten stray spaces.
    text = re.sub(r'\s*' + EM_DASH + r'\s*', ' - ', text)
    return text


def rule_value_first_bullet(lines):
    """Flag bullets that are a raw ticket-title link with NO nearby value statement.

    A client-facing bullet must lead with a plain-language benefit, not a bare
    ticket title. A link-only bullet is acceptable as a *reference* when the
    value was already stated: either the bullet directly above it carries prose
    (a benefit line), or the current section already opened with a value bullet
    such as "What you will get". It is flagged only when it stands alone with no
    value context, i.e. a raw changelog line.

    Only top-level bullets (no leading indentation) are checked.
    """
    # link-only bullet, tolerating escaped brackets: "[\[FEATURE{...}\] title](url)"
    link_only = re.compile(r'^[-*]\s+\\?\[.+\]\([^)]+\)\s*$')
    is_bullet = re.compile(r'^[-*]\s')
    value_cue = re.compile(r'\*\*.+?\*\*|What you will get', re.I)
    header = re.compile(r'^#{1,4}\s')

    hits = []
    for i, line in enumerate(lines, 1):
        if not is_bullet.match(line) or not link_only.match(line.strip()):
            continue
        # look back for value context within this section (until a header or rule)
        has_value = False
        j = i - 2  # zero-based index of the line above (i is 1-based)
        while j >= 0:
            prev = lines[j]
            if header.match(prev) or prev.strip() == '* * *':
                break
            if value_cue.search(prev):
                has_value = True
                break
            j -= 1
        if not has_value:
            hits.append((i, 1,
                         "Raw ticket link with no value statement nearby. Lead "
                         "with a bold client benefit, then keep the link as a "
                         "reference below it."))
    return hits


def rule_no_en_dash_in_prose(lines):
    # En dashes are allowed in date ranges (e.g. "Aug 11 – Aug 17") but flagged
    # elsewhere as a warning to keep punctuation consistent.
    hits = []
    for i, line in enumerate(lines, 1):
        for m in re.finditer(EN_DASH, line):
            # allow if surrounded by digits/months (rough date-range heuristic)
            ctx = line[max(0, m.start() - 4): m.end() + 4]
            if re.search(r'\d', ctx):
                continue
            hits.append((i, m.start() + 1,
                         "En dash (\u2013) in prose. Prefer '-' unless a date range."))
    return hits


ERROR_RULES = [
    ("no-em-dash", rule_no_em_dash, fix_em_dash),
]
WARN_RULES = [
    ("value-first-bullet", rule_value_first_bullet, None),
    ("no-en-dash-in-prose", rule_no_en_dash_in_prose, None),
]


def run(path, do_fix=False):
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"lint: cannot read {path}: {e}", file=sys.stderr)
        return 2

    if do_fix:
        fixed = text
        for _id, _scan, fixer in ERROR_RULES:
            if fixer:
                fixed = fixer(fixed)
        if fixed != text:
            open(path, "w", encoding="utf-8").write(fixed)
            print(f"lint: auto-fixed {path}")
            text = fixed

    lines = text.split("\n")
    errors, warns = [], []
    for _id, scan, _fix in ERROR_RULES:
        for ln, col, msg in scan(lines):
            errors.append((_id, ln, col, msg))
    for _id, scan, _fix in WARN_RULES:
        for ln, col, msg in scan(lines):
            warns.append((_id, ln, col, msg))

    for _id, ln, col, msg in warns:
        print(f"  WARN  {_id}  {path}:{ln}:{col}  {msg}")
    for _id, ln, col, msg in errors:
        print(f"  ERROR {_id}  {path}:{ln}:{col}  {msg}")

    if errors:
        print(f"\nlint: FAILED — {len(errors)} error(s), {len(warns)} warning(s). "
              f"Fix before finalizing (or run with --fix).")
        return 1
    print(f"lint: PASSED — 0 errors, {len(warns)} warning(s).")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Lint a weekly report before finalize.")
    ap.add_argument("path", help="Path to the report markdown file")
    ap.add_argument("--fix", action="store_true",
                    help="Auto-fix safe error rules in place (e.g. em dashes)")
    args = ap.parse_args()
    sys.exit(run(args.path, do_fix=args.fix))


if __name__ == "__main__":
    main()
