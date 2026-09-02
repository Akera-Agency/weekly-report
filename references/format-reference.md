# Weekly Report Reference Format

This is the EXACT markdown format Akera uses for **client-facing** weekly product
reports. It is anchored to the current live house style (The Key, APR 2026
editions in the ClickUp Weekly Reports list). Follow this structure precisely.

See `example-report.md` for a full worked example.

## Key Formatting Rules

- Bold top-level headers: `# **Overview**`, `# **Recent Delivery Highlights**`
- Bold subsection headers: `### **Themed group name**`
- Horizontal rules between top-level sections: `* * *`
- Bullet points: `-` or `*`
- Link ClickUp tickets inline: `[<ticket title>](https://app.clickup.com/t/<id>)`
- Client-readable: describe outcomes and value; no internal names or task splits

## Value-First Writing (the #1 rule)

**The client does not care what changed. They care what they can now do.**

Never list a raw ticket title as a bullet and stop. Every bullet must lead with
the **client outcome in bold**, then explain why it matters to them. The ticket
link is a demoted reference underneath, not the headline.

**Bad (engineer-speak changelog):**
```markdown
*   [\[Tenant-Admin{Scenarios / Tactic Mastery}\] Unify psychological tactics](https://app.clickup.com/t/869ehcpm7)
```

**Good (value-first):**
```markdown
*   **Consistent tactics across everything:** the same psychological-tactic
    labels now apply across phishing, vishing, and training, so your reporting
    compares like for like.
    [\[Tenant-Admin{Scenarios / Tactic Mastery}\] Unify psychological tactics](https://app.clickup.com/t/869ehcpm7)
```

Rules of thumb:

- **Section headers state outcomes**, not internal feature names.
  “See exactly where your human risk lives”, not “Employee risk intelligence”.
- **Lead each bullet with a bold benefit phrase**, then the plain-language payoff.
- **Answer “so what?” on every line.** If a bullet does not say what the client
  gains, rewrite it.
- **Use concrete examples** where they add clarity (e.g. “a call to a Gulf-based
  team lands as a Gulf-accented voice”).
- **In-Progress and Expected sections** open each item with a **What you will
  get** line — the outcome framed as a promise.
- **Reframe raw metrics as value.** “20 merged PRs” becomes “20 improvements
  shipped to production this week” + why it matters.
- **Translate jargon.** Strip ticket prefixes like `[Tenant-Admin{...}]` from the
  reader-facing sentence; keep them only inside the reference link.
- **No em dashes** (the linter enforces this). Use ‘ - ’ or reword.

## Template Structure

```markdown
# **<Project> – <Label> Weekly Update**

# **Overview**

<Paragraph 1: what this week centered on — the dominant theme and execution pattern.>

<Paragraph 2: how it compares to the prior week; the shift in focus.>

* * *

# **Recent Delivery Highlights**

### **<Outcome-focused header, e.g. "See exactly where your human risk lives">**

<One-line framing of what the client can now do.>

*   **<Bold benefit phrase>:** <plain-language payoff for the client, with a
    concrete example where helpful>
*   **<Bold benefit phrase>:** <plain-language payoff>

**Why this matters:** <the bigger-picture value to the client>

*   [<Ticket title>](https://app.clickup.com/t/<id>)
*   [<Ticket title>](https://app.clickup.com/t/<id>)

* * *

# **Key Improvements**

### **<Outcome-focused theme, e.g. "Numbers you can trust">**

*   **<Bold benefit phrase>:** <what the client gains, in plain language>
    [<Ticket title>](https://app.clickup.com/t/<id>)
*   **<Bold benefit phrase>:** <what the client gains>
    [<Ticket title>](https://app.clickup.com/t/<id>)

### **Infrastructure and release hygiene**

*   [Merged backend/infrastructure stream in GitHub (<N> merged PRs this week)](https://github.com/<owner>/<repo>/pulls?q=is%3Apr+is%3Amerged+merged%3A<from>..<to>)
*   <One line on CI / migration / backend risk reduction.>

* * *

# **In-Progress Features**

### **<Feature name>**

*   **What you will get:** <the client outcome, framed as a promise>
*   **Status:** <in progress / in prototyping / in testing> - <short focus note>
*   [<Ticket title>](https://app.clickup.com/t/<id>)

* * *

# **Expected Deliveries This Week**

### **<Outcome-focused theme>**

*   **What you will get:** <the client outcome, framed as a promise>
*   **Current status:** in code review | in testing | mixed review/testing
*   [<Ticket title>](https://app.clickup.com/t/<id>)

* * *

## **Meetings This Week**

### **<Day, Date @ Time – Call name>**

<One-line purpose.>
```

## Section Guidance

| Section | Source | Notes |
|---------|--------|-------|
| Overview | Week themes (+ Fathom) | 2-3 short paragraphs, compare to prior week |
| Recent Delivery Highlights | `done` tickets + merged PRs | Outcome header; value-first bullets; "Why this matters" |
| Key Improvements | enhancements/fixes + PR count | Value-first bullets; end with a "faster/more stable platform" group carrying the PR-count line |
| In-Progress Features | `in progress` tickets | Open each with "What you will get" |
| Expected Deliveries | `review` / `testing` tickets | Open each with "What you will get" + current status |
| Meetings This Week | Manual | Optional; manual entry for now |

## ClickUp API Notes

Read a task's markdown for reference:
```bash
curl -s "https://api.clickup.com/api/v2/task/<task_id>?include_markdown_description=true" \
  -H "Authorization: $CLICKUP_TOKEN" | jq -r '.markdown_description'
```

Publish a report to the Weekly Reports list (status `live`):
```bash
curl -s -X POST "https://api.clickup.com/api/v2/list/901215259440/task" \
  -H "Authorization: $CLICKUP_TOKEN" -H "Content-Type: application/json" \
  -d '{"name":"THEKEY - W03 APR 2026 Weekly Report","markdown_content":"...","status":"live"}'
```

- Use `markdown_content` when creating (renders markdown in ClickUp).
- `.markdown_description` returns raw markdown when reading; `.description` is stripped plain text.
