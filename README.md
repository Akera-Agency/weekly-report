# Internal Weekly Plan Builder

An AI agent skill for building structured weekly plan documents project-by-project, with auto-drafting from GitHub, Fathom, and ClickUp data.

## What It Does

- **Conversational workflow** — Build plans project-by-project with AI drafting
- **Auto-pulls data** — Fetches from GitHub (commits/PRs), Fathom (call transcripts), ClickUp (tickets), Jarvis (team members)
- **Ops Tasks tracking** — Identifies blockers and creates ClickUp tickets
- **Consistent formatting** — Follows exact markdown structure for ClickUp

## Installation

### For Clawdbot

```bash
# Copy to your skills directory
cp -r internal-weekly-plan ~/.clawdbot/skills/

# Or symlink
ln -s /path/to/internal-weekly-plan ~/.clawdbot/skills/internal-weekly-plan
```

### For Claude Code / Other Agents

Copy the `SKILL.md` and `references/` folder to your agent's skill directory.

## Configuration

Edit `config/projects.json` to set your projects and their data sources:

```json
{
  "projects": [
    {
      "name": "Project Name",
      "client": "Client Name",
      "github_url": "https://github.com/org/repo",
      "clickup_space_id": "...",
      "fathom_search": "project name"
    }
  ]
}
```

## Usage

```
# Start a new weekly plan
internal-weekly-plan start "Mar 22 → Mar 28"

# Work on a project (auto-drafts from data)
internal-weekly-plan project "The Key"

# Tweak as needed, then move on
internal-weekly-plan next

# After all projects, review ops tasks
internal-weekly-plan opstasks

# Finalize and upload to ClickUp
internal-weekly-plan finalize
```

## Requirements

- **Jarvis API** — For team member data
- **GitHub access** — For commit/PR history
- **Fathom CLI** — For meeting transcripts
- **ClickUp API** — For ticket creation

## File Structure

```
internal-weekly-plan/
├── SKILL.md              # Main skill instructions
├── config/
│   └── projects.json     # Project configuration
└── references/
    └── format-reference.md   # Markdown format template
```

## License

MIT
