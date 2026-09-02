# Weekly Report Builder - Setup Guide

A step-by-step guide to set up this skill for your OCPlatform agent.

---

## What This Skill Does

Builds Akera's **client-facing** weekly product reports, one project per report.
It:
- Auto-pulls merged PRs from GitHub for a date window
- Pulls ClickUp tasks by status (done / in progress / review)
- Drafts every section in the house style
- Publishes the report to the ClickUp Weekly Reports list with status `live`

It does **not** include team members, task splits, or internal blockers.

---

## Step 1: Clone the Skill

```bash
cd ~/.clawdbot/skills
git clone https://github.com/Akera-Agency/internal-weekly-plan.git weekly-report
```

---

## Step 2: Configure API Access

### ClickUp API
Add your ClickUp personal token to the agent environment (or 1Password):
```
CLICKUP_TOKEN=pk_XXXXX   # from ClickUp Settings > Apps
```
Weekly Reports list ID is already set in `config/projects.json`
(`901215259440`).

### GitHub Access
```bash
gh auth login   # or provide a PAT to the agent environment
```

### Fathom (optional)
```bash
mkdir -p ~/.config/fathom
echo "FATHOM_API_KEY=your_api_key" > ~/.config/fathom/credentials
```

---

## Step 3: Configure Projects

Edit `config/projects.json`. Fill in each project's `clickupSpaceId` as you
learn it (The Key is already set):

```json
{
  "clickup": { "weeklyReportsListId": "901215259440", "publishStatus": "live" },
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

---

## Step 4: Test the Skill

Ask your agent:
```
Start a weekly report for The Key, W03 APR 2026, from 2026-04-13 to 2026-04-19
```

The agent should:
1. Initialize the report
2. Pull merged PRs + ClickUp tasks for the window
3. Draft all sections
4. Let you tweak, then publish to the Weekly Reports list

---

## Usage Commands

| Command | What It Does |
|---------|--------------|
| `start "<Project>" "<Label>" --from <ISO> --to <ISO>` | Initialize a report |
| `draft` | Auto-pull GitHub + ClickUp, draft all sections |
| `show` | Show the current draft |
| `edit <section>` | Tweak a section |
| `meeting "<title>" "<purpose>"` | Add a meeting (manual) |
| `finalize` | Publish to Weekly Reports list, status `live` |

---

## Workflow

1. **Start** → Pick one project + date window
2. **Draft** → Auto-draft from GitHub + ClickUp
3. **Review / edit** → Tweak sections as needed
4. **Meetings** → Add manually (for now)
5. **Finalize** → Publish to ClickUp

---

## Troubleshooting

**"No GitHub data"**
→ Verify `gh auth status` is logged in and the repo/date window are correct.

**"ClickUp publish failed"**
→ Check `CLICKUP_TOKEN` has write access to list `901215259440`.

**"Fathom search empty"**
→ Optional. Meetings are manual; Fathom only adds Overview context.

**"Wrong ClickUp tickets"**
→ Fill in the project's `clickupSpaceId` in `config/projects.json`.

---

## Questions?

Repo: https://github.com/Akera-Agency/internal-weekly-plan
