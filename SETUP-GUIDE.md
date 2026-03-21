# Internal Weekly Plan Builder - Setup Guide

A step-by-step guide to set up this skill for your OpenClaw agent.

---

## What This Skill Does

Builds Akera's weekly plan documents conversationally, project-by-project. It:
- Auto-pulls data from GitHub, Fathom, ClickUp, and Jarvis
- Drafts sections based on recent activity
- Tracks Ops Tasks (blockers) and creates ClickUp tickets
- Outputs properly formatted markdown for ClickUp

---

## Step 1: Clone the Skill

```bash
cd ~/.clawdbot/skills
git clone https://github.com/Akera-Agency/internal-weekly-plan.git
```

Or if using Claude Code / other agent:
```bash
cd /path/to/your/skills
git clone https://github.com/Akera-Agency/internal-weekly-plan.git
```

---

## Step 2: Configure API Access

The skill needs access to these services:

### Jarvis API (Team Members)
```bash
# Create config file
mkdir -p ~/.config/jarvis-meetings
cat > ~/.config/jarvis-meetings/config.json << 'EOF'
{
  "jarvis_api_url": "https://internal-jarvis-production.up.railway.app/api",
  "jarvis_api_key": "YOUR_JARVIS_API_KEY",
  "timezone": "Your/Timezone"
}
EOF
```

### ClickUp API
Add to your agent's TOOLS.md or environment:
```
ClickUp API Token: pk_XXXXX (get from ClickUp Settings > Apps)
Ops Tasks List ID: 901214308228
```

### Fathom CLI
```bash
# Install fathom CLI and configure
mkdir -p ~/.config/fathom
echo "FATHOM_API_KEY=your_api_key" > ~/.config/fathom/credentials
```

### GitHub Access
```bash
# Authenticate with gh CLI
gh auth login
```

---

## Step 3: Configure Projects

Edit `config/projects.json` with your projects:

```json
{
  "projects": [
    {
      "name": "Project Name",
      "client": "Client Name", 
      "github_url": "https://github.com/org/repo",
      "clickup_space_id": "your_space_id",
      "fathom_search": "project name"
    }
  ]
}
```

---

## Step 4: Test the Skill

Ask your agent:
```
Start a weekly plan for Mar 22 → Mar 28
```

The agent should:
1. Initialize the plan
2. Ask which project to start with (or follow the configured order)
3. Pull data and draft sections
4. Let you tweak and approve each section

---

## Usage Commands

| Command | What It Does |
|---------|--------------|
| `start "Date Range"` | Initialize new weekly plan |
| `project "Name"` | Focus on a project, auto-draft |
| `next` | Move to next project |
| `opstasks` | Review identified Ops Tasks |
| `finalize` | Generate final doc, upload to ClickUp |

---

## Workflow

1. **Start** → Initialize with date range
2. **Project** → Auto-draft from data, tweak as needed
3. **Next** → Repeat for each project
4. **Ops Tasks** → Review blockers, approve ticket creation
5. **Finalize** → Upload to ClickUp ticket

---

## Project Order (Default)

1. The Key
2. Miqyas Al Dhad
3. MHP Pros
4. OpenClaw Onboard
5. Manarway
6. Munitron
7. Alifbee Exams

Edit `config/projects.json` to change the order.

---

## Troubleshooting

**"Can't find team members"**
→ Check Jarvis API key and URL in config

**"No GitHub data"**
→ Verify `gh auth status` is logged in

**"Fathom search empty"**
→ Check Fathom credentials and search terms

**"ClickUp upload failed"**
→ Verify API token has write access

---

## Questions?

Repo: https://github.com/Akera-Agency/internal-weekly-plan
