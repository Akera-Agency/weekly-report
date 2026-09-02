---
name: weekly-report
description: Build client-facing weekly product reports for one project at a time, auto-drafting from GitHub (merged PRs in a date window) and ClickUp (tasks by status). Publishes to the ClickUp Weekly Reports list. No team members, no internal task splits.
version: 2.0.0
---

# Weekly Report Builder

Build Akera's **client-facing** weekly product reports, one project per report.

This is a client deliverable, not an internal ops plan. It tells the client what
shipped, what's in progress, and what's coming next in a specific time window.
**Never** include team member names, task assignments, or internal work splits.

## Quick Start

```bash
# Start a report for one project + date window
weekly-report start "The Key" "W03 APR 2026" --from 2026-04-13 --to 2026-04-19

# Auto-draft all sections from GitHub + ClickUp (+ Fathom if available)
weekly-report draft

# Review the draft
weekly-report show

# Tweak a section
weekly-report edit overview

# Add manual meetings (Meetings are manual for now)
weekly-report meeting "Monday, April 20 @ 4:30 PM – The Key Standup" "Weekly plan alignment and release review."

# Publish to ClickUp Weekly Reports list, status "live"
weekly-report finalize
```

## Workflow

1. **Start** — Pick one project and a date window (`--from`/`--to`, ISO dates).
2. **Draft** — Auto-pull data and draft every section:
   - **GitHub:** merged PRs where `merged:<from>..<to>`. Count them, cluster by
     title/theme, and build the delivery + improvements narrative.
   - **ClickUp:** tasks in the project space, bucketed by status:
     - `done` / `closed` in window → Recent Delivery Highlights
     - `in progress` → In-Progress Features
     - `review` / `testing` → Expected Deliveries This Week
   - **Fathom (optional):** call transcripts matching the project → Overview
     context. Do NOT auto-fill Meetings from Fathom yet (manual for now).
3. **Review & edit** — User tweaks any section. Don't ask section-by-section;
   draft it all, user corrects.
4. **Meetings** — User adds meetings manually (`weekly-report meeting`).
5. **Finalize** — Generate final markdown, create a task in the Weekly Reports
   list, set status to `live`, return the task URL.

**Key rule:** Auto-draft everything from data first. The user edits, never fills
from scratch.

## Commands

| Command | Description |
|---------|-------------|
| `weekly-report start "<Project>" "<Label>" --from <ISO> --to <ISO>` | Initialize a report |
| `weekly-report draft` | Auto-pull GitHub + ClickUp (+Fathom), draft all sections |
| `weekly-report show` | Show the current draft |
| `weekly-report edit <section>` | Edit a section (`overview`, `highlights`, `improvements`, `inprogress`, `expected`, `meetings`) |
| `weekly-report meeting "<title>" "<purpose>"` | Add a meeting (manual) |
| `weekly-report status` | Show what data was pulled and which sections are drafted |
| `weekly-report finalize` | Publish to Weekly Reports list, status `live`, return URL |

## Report Sections (in order)

1. **Overview** — 2-3 short paragraphs. What the week centered on. Compare to the
   prior week when possible.
2. **Recent Delivery Highlights** — Themed groups of shipped work. Per group:
   what users can now do, why it matters, linked ClickUp tickets.
3. **Key Improvements** — Enhancements + fixes, grouped by theme. Always include
   an **Infrastructure and release hygiene** group with the merged-PR count line
   and the GitHub PR-query link.
4. **In-Progress Features** — Per feature: Status, Current focus, Current ticket,
   Next milestone.
5. **Expected Deliveries This Week** — Per theme: Expected state, Current status
   (in code review / testing), ticket links.
6. **Meetings This Week** *(optional, manual)* — Per meeting: title with day/time,
   one-line purpose.

## Data Sources

| Source | What | Used for |
|--------|------|----------|
| **GitHub** | Merged PRs in `merged:<from>..<to>` | Highlights, improvements, "N merged PRs" line + link |
| **ClickUp** | Tasks by status in project space | Ticket links, in-progress + expected sections |
| **Fathom** | Calls matching project name | Overview narrative (optional) |

**No Jarvis. No team members. No task-split tables.**

### GitHub — merged PRs in window

```bash
# Count + list merged PRs (repo from config githubRepo)
gh pr list --repo Thekey-sa/moodle-monorepo --state merged \
  --search "merged:2026-04-13..2026-04-19" --limit 200 \
  --json number,title,url
```

The client-facing PR-query link for the "release hygiene" bullet:
```
https://github.com/<owner>/<repo>/pulls?q=is%3Apr+is%3Amerged+merged%3A<from>..<to>
```

### ClickUp — tasks by status

```bash
# Tasks in the project's space, then bucket by status
curl -s "https://api.clickup.com/api/v2/team/<team_id>/task?space_ids[]=<space_id>&subtasks=true" \
  -H "Authorization: $CLICKUP_TOKEN"
```

Read a specific task's markdown for reference:
```bash
curl -s "https://api.clickup.com/api/v2/task/<task_id>?include_markdown_description=true" \
  -H "Authorization: $CLICKUP_TOKEN" | jq -r '.markdown_description'
```

## Working File

Append the report to a working file as you build it, so context is preserved:
```
reports/weekly-report-<project-slug>-<label-slug>.md
```
Example: `reports/weekly-report-the-key-w03-apr-2026.md`

## State File

Progress is saved to `memory/weekly-report-state.json`:

```json
{
  "project": "The Key",
  "label": "W03 APR 2026",
  "from": "2026-04-13",
  "to": "2026-04-19",
  "githubRepo": "https://github.com/Thekey-sa/moodle-monorepo",
  "clickupSpaceId": "90125411087",
  "data": {
    "mergedPrCount": 37,
    "prQueryUrl": "https://github.com/Thekey-sa/moodle-monorepo/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-13..2026-04-19",
    "done": [{"id": "869cuxu59", "name": "...", "url": "..."}],
    "inProgress": [],
    "review": []
  },
  "sections": {
    "overview": "...",
    "highlights": [],
    "improvements": [],
    "inProgress": [],
    "expected": [],
    "meetings": []
  },
  "published": {"taskId": null, "url": null}
}
```

## Markdown Format

**CRITICAL:** Follow the exact format in `references/format-reference.md`, and use
`references/example-report.md` as a full worked example (real The Key report).

Key rules:
- Bold section headers: `# **Overview**`, `# **Recent Delivery Highlights**`, etc.
- `### **Themed group name**` for subsections
- `* * *` horizontal rules between top-level sections
- Link ClickUp tickets inline: `[<ticket title>](https://app.clickup.com/t/<id>)`
- Keep it client-readable: outcomes and value, not internal jargon or names

## Publishing to ClickUp

After the user approves the draft:

1. Create a task in the Weekly Reports list (`config → clickup.weeklyReportsListId`
   = `901215259440`):
   ```bash
   curl -s -X POST "https://api.clickup.com/api/v2/list/901215259440/task" \
     -H "Authorization: $CLICKUP_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "THEKEY - W03 APR 2026 Weekly Report", "markdown_content": "<report md>", "status": "live"}'
   ```
2. Set status to `live` (`config → clickup.publishStatus`).
3. Return the created task URL to the user.

**Naming convention:** `<PROJECT SHORT> - <LABEL> Weekly Report`
(e.g. `THEKEY - W03 APR 2026 Weekly Report`).

## Integration Notes

- **GitHub repos**: from `config/projects.json → projects[].githubRepo`.
- **ClickUp spaces**: from `projects[].clickupSpaceId`. Fill these in as you learn
  them (only The Key is known so far: `90125411087`).
- **Fathom**: optional context only. Meetings are manual until a better source
  exists.
- **Credentials**: `CLICKUP_TOKEN` and GitHub auth come from the agent
  environment / 1Password — never commit them.

## What This Skill Does NOT Do

- No team member lists (Jarvis removed).
- No engineering/design work-split tables.
- No internal blockers or ops-task ticket creation.
- No multi-project documents — **one project per report**.
