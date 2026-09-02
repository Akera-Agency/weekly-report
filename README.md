# Weekly Report Builder

An AI agent skill for building **client-facing** weekly product reports, one
project at a time, with auto-drafting from GitHub (merged PRs in a date window)
and ClickUp (tasks by status).

This is a client deliverable — it tells the client what shipped, what's in
progress, and what's coming next. It is **not** an internal ops plan: no team
members, no task splits, no blockers.

## What It Does

- **One project per report** — Focused, client-readable weekly updates
- **Auto-pulls data** — GitHub (merged PRs in the window), ClickUp (tasks by
  status), Fathom (optional call context)
- **Matched house style** — Follows the exact format already live in ClickUp's
  Weekly Reports list
- **Publishes to ClickUp** — Creates the report in the Weekly Reports list with
  status `live`

## Installation

### For Clawdbot

```bash
cp -r weekly-report ~/.clawdbot/skills/
# or symlink
ln -s /path/to/weekly-report ~/.clawdbot/skills/weekly-report
```

### For Claude Code / Other Agents

Copy `SKILL.md` and the `references/` folder to your agent's skill directory.

## Configuration

Edit `config/projects.json`:

```json
{
  "clickup": {
    "weeklyReportsListId": "901215259440",
    "publishStatus": "live"
  },
  "projects": [
    {
      "name": "The Key",
      "client": "Abdulrahman Albeiroti & Asem Alhomaidi",
      "githubRepo": "https://github.com/Thekey-sa/moodle-monorepo",
      "clickupSpaceId": "90125411087",
      "fathomSearch": "key"
    }
  ]
}
```

## Usage

```
# Start a report for one project + date window
weekly-report start "The Key" "W03 APR 2026" --from 2026-04-13 --to 2026-04-19

# Auto-draft all sections from GitHub + ClickUp
weekly-report draft

# Review and tweak
weekly-report show
weekly-report edit overview

# Add meetings manually
weekly-report meeting "Monday, April 20 @ 4:30 PM – The Key Standup" "Weekly alignment."

# Publish to ClickUp Weekly Reports list, status "live"
weekly-report finalize
```

## Requirements

- **GitHub access** — For merged PR history (`gh` CLI or API)
- **ClickUp API** — For reading tasks and publishing the report
- **Fathom** — Optional, for Overview call context

## File Structure

```
weekly-report/
├── SKILL.md                      # Main skill instructions
├── config/
│   └── projects.json             # Projects + ClickUp Weekly Reports list
└── references/
    ├── format-reference.md       # Markdown format template
    └── example-report.md         # Full worked example (The Key)
```

## License

MIT
