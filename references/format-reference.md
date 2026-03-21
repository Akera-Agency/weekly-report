# Weekly Plan Reference Format

This is the EXACT markdown format Aziz uses for weekly plans. Follow this structure precisely.

## Key Formatting Rules

- Standard markdown headers: `#`, `##`, `###`, `####`
- Horizontal rules: `---`
- Bullet points: `-`
- Tables: Standard markdown tables for metadata, quick links, HEADS-UP, and work splits
- Italics for ownership notes: `*(Owned by Head of Engineering)*`
- Bold for emphasis: `**Purpose:**`

## Template Structure

```markdown
# [OPS{Weekly Plan}] [Date Range] Plan Direction

## [Date Range] — Direction & Early Signals

---

## 000 — Report Metadata

| Field | Value |
|-------|-------|
| **Owner** | Mohamed Aziz Hadj Hassen |
| **Week** | [Start Date] → [End Date] |

---

## Client: [Client Name]

### Project: [Project Name]

#### 🔗 Project Quick Links

| Resource | Link |
|----------|------|
| 📁 Documentation Folder | — |
| 🎫 Project Tickets | — |
| 💻 GitHub Repository | [URL or —] |
| 🎨 Figma Project | — |

### 1️⃣ OPS DIRECTION

#### URGENT — Action Required This Week

Concrete priorities that must move forward this week.

- [Item 1]
- [Item 2]

#### HEADS-UP — Upcoming Feature Work (Design / Engineering)

| Feature / Area Name | Design | Engineering |
|---------------------|--------|-------------|
| [Feature] | [✓ or blank] | [✓ or blank] |

#### NOTES / CONTEXT

- [Context item]

### 2️⃣ PRODUCT DESIGN PLAN (if needed)

*(Owned by Head of Design)*

**Purpose:** Translate the Ops Direction into design intent, scope, and delivery expectations for the week.

#### 2.1 — Design Work Scope (High-Level)

- [Design work item]

#### 2.2 — Design Work Split

| Product Designer Name | Tasks | Potential Blockers |
|-----------------------|-------|-------------------|
| [Name] | [Tasks] | [Blockers or None] |

#### 2.3 — Design Demo Recommendations

- [Demo item] → [When ready]

#### 2.4 — High-Level Design Blockers & Needs

- [Blocker]

#### 2.5 — Additional Design Notes

None

### 3️⃣ PRODUCT ENGINEERING PLAN

*(Owned by Head of Engineering)*

**Purpose:** Convert direction and design into engineering execution clarity.

#### 3.1 — Engineering Work Scope (High-Level)

- [Engineering work item]

#### 3.2 — Engineering Work Split

| Product Engineer Name | Tasks | Potential Blockers |
|-----------------------|-------|-------------------|
| [Name] | [Tasks] | [Blockers or None] |

#### 3.3 — Engineering Demo Recommendations

- [Demo item] → [When ready]

#### 3.4 — High-Level Engineering Blockers & Needs

- [Blocker]

#### 3.5 — Additional Engineering Notes

[Notes or None]

---

[Repeat for each project]
```

## ClickUp API Notes

When extracting markdown from ClickUp:
```bash
curl -s "https://api.clickup.com/api/v2/task/TASK_ID?include_markdown_description=true" \
  -H "Authorization: API_KEY" | jq -r '.markdown_description'
```

The `.description` field returns plain text (stripped). Use `.markdown_description` for raw markdown.
