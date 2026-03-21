---
name: internal-weekly-plan
description: Build internal weekly plan documents project-by-project with auto-drafting from GitHub, Fathom, and ClickUp. Pulls team members from internal Jarvis API.
version: 1.0.0
---

# Internal Weekly Plan Builder

Build Akera's weekly plan documents conversationally, project-by-project.

## Quick Start

```bash
# Start a new weekly plan
internal-weekly-plan start "Mar 19 → Mar 28"

# Work on a specific project
internal-weekly-plan project "The Key"

# Move to next project
internal-weekly-plan next

# Generate final document
internal-weekly-plan finalize
```

## Workflow

1. **Start** — Initialize plan with date range
2. **Project** — For each project:
   - Auto-pull data from GitHub, Fathom, ClickUp (last week's data informs this week's plan)
   - Get team members (from Jarvis, filter out leads)
   - **AUTO-DRAFT everything** — URGENT, HEADS-UP, engineering split based on gathered data
   - User tweaks only what needs changing
3. **Next** — Move to next project in template order
4. **Ops Tasks** — After all projects done, draft a list of Ops Tasks identified during planning (blockers, design tasks, prep work). User approves before tickets are created.
5. **Finalize** — Generate final markdown, upload to ClickUp ticket, create approved Ops Tasks

**Key rule:** Don't ask for every section — draft it based on context, user corrects as needed.

## Commands

| Command | Description |
|---------|-------------|
| `internal-weekly-plan start "<date range>"` | Initialize new plan |
| `internal-weekly-plan project "<name>"` | Focus on a project, auto-draft |
| `internal-weekly-plan team` | Show team members for current project |
| `internal-weekly-plan assign "<person>" "<task>" [blockers]` | Add engineering task assignment |
| `internal-weekly-plan urgent "<item>"` | Add to URGENT section |
| `internal-weekly-plan headsup "<feature>" [design\|eng]` | Add to HEADS-UP table |
| `internal-weekly-plan note "<text>"` | Add to NOTES/CONTEXT |
| `internal-weekly-plan demo "<item>" "<when>"` | Add demo recommendation |
| `internal-weekly-plan blocker "<item>"` | Add to blockers section |
| `internal-weekly-plan design` | Enable design section for current project |
| `internal-weekly-plan show` | Show current project draft |
| `internal-weekly-plan next` | Move to next project |
| `internal-weekly-plan status` | Show progress (which projects done) |
| `internal-weekly-plan opstasks` | Draft Ops Tasks identified during planning |
| `internal-weekly-plan finalize` | Generate final doc, ask for ClickUp link |

## Data Sources

For each project, the skill pulls:

| Source | What |
|--------|------|
| **Jarvis** | Team members (developers, designers) |
| **GitHub** | Commits & PRs from the week (by repo URL) |
| **Fathom** | Calls matching project name |
| **ClickUp** | Tickets, action items in project space |

## Working File

As you build the plan, append each project to a working file to preserve context:
```
reports/internal-weekly-plan-[date-range].md
```

Example: `reports/internal-weekly-plan-mar22-28.md`

This file accumulates all project sections. If context fills up, resume from this file.

## State File

Progress is saved to `memory/weekly-plan-state.json`:

```json
{
  "week": "Mar 19 → Mar 28",
  "currentProject": "The Key",
  "projectOrder": ["The Key", "Alifbee Exams", ...],
  "projects": {
    "The Key": {
      "status": "in_progress",
      "includeDesign": false,
      "urgent": ["AWS DNS switch needs to happen"],
      "headsup": [{"feature": "Gamification", "design": false, "eng": true}],
      "engineering": {
        "scope": ["Gamification", "AI Copilot"],
        "split": [{"name": "Ramez", "tasks": "AWS migration", "blockers": "None"}],
        "demos": ["Interval scheduling ready by Wednesday"],
        "blockers": ["Notification hub docs"]
      },
      "design": null,
      "notes": []
    }
  },
  "opsTasksDraft": [
    {"task": "Certificate design for Alifbee", "project": "Alifbee Exams", "blocker_for": "Download unit certificate feature"},
    {"task": "Review landing page copy", "project": "MHP Pros", "blocker_for": null}
  ]
}
```

## Project Order (from template)

1. The Key
2. Miqyas Al Dhad
3. MHP Pros
4. OpenClaw Onboard
5. Manarway
6. Munitron
7. Alifbee Exams

## Markdown Format

**CRITICAL:** Follow the exact format in `references/format-reference.md`

Key rules:
- Standard markdown: `#` headers, `---` rules, `-` bullets
- Tables for: metadata, quick links, HEADS-UP, work splits
- `*(Owned by Head of Engineering)*` for ownership
- `**Purpose:**` for section intros

When extracting from ClickUp for reference:
```bash
curl -s "https://api.clickup.com/api/v2/task/TASK_ID?include_markdown_description=true" \
  -H "Authorization: $API_KEY" | jq -r '.markdown_description'
```

## Integration Notes

- **Team from Jarvis**: `GET /api/projects` returns `team_members` array with first_name, last_name, role
- **Filter out leads**: Don't show Product Lead, Executive Director, Design Lead, Tech Lead in team lists (Aziz, Ramez, Tracy, Rayen)
- **GitHub repos**: Stored in project's `github_repository_url` field
- **ClickUp spaces**: Project has `clickup_space_id`, `clickup_tickets_list_id`, etc.
- **Design section**: Only included when Aziz explicitly says design is needed

## Ops Tasks Workflow

After all projects are done:
1. Draft list of Ops Tasks identified (blockers, design work, prep tasks)
2. Show to Aziz for approval
3. Create tickets in Ops Tasks list (ID: `901214308228`) with format `[PROJECTNAME] Task title`
4. Assign to Aziz and set status to "now"
