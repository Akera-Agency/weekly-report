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

## Template Structure

```markdown
# **<Project> – <Label> Weekly Update**

# **Overview**

<Paragraph 1: what this week centered on — the dominant theme and execution pattern.>

<Paragraph 2: how it compares to the prior week; the shift in focus.>

* * *

# **Recent Delivery Highlights**

### **<Themed feature group>**

<One-line framing of the release stream.>

*   **What users can now do more reliably:**
    *   <capability 1>
    *   <capability 2>
*   **Why this matters:** <value statement>

*   [<Ticket title>](https://app.clickup.com/t/<id>)
*   [<Ticket title>](https://app.clickup.com/t/<id>)

* * *

# **Key Improvements**

### **<Theme, e.g. Gradebook and attempt-flow correctness>**

*   [<Ticket title>](https://app.clickup.com/t/<id>)
*   [<Ticket title>](https://app.clickup.com/t/<id>)

### **Infrastructure and release hygiene**

*   [Merged backend/infrastructure stream in GitHub (<N> merged PRs this week)](https://github.com/<owner>/<repo>/pulls?q=is%3Apr+is%3Amerged+merged%3A<from>..<to>)
*   <One line on CI / migration / backend risk reduction.>

* * *

# **In-Progress Features**

### **<Feature name>**

*   **Status:** In Progress
*   **Current focus:** <what is being worked on>
*   **Current ticket:** [<Ticket title>](https://app.clickup.com/t/<id>)
*   **Next milestone:** <what completes this>

* * *

# **Expected Deliveries This Week**

### **<Theme>**

*   **Expected state:** <what will be true when delivered>
*   **Current status:** in code review | in testing | mixed review/testing
*   **Primary ticket:** [<Ticket title>](https://app.clickup.com/t/<id>)

* * *

## **Meetings This Week**

### **<Day, Date @ Time – Call name>**

<One-line purpose.>
```

## Section Guidance

| Section | Source | Notes |
|---------|--------|-------|
| Overview | Week themes (+ Fathom) | 2-3 short paragraphs, compare to prior week |
| Recent Delivery Highlights | `done` tickets + merged PRs | Group by theme, lead with user value |
| Key Improvements | enhancements/fixes + PR count | Always end with "Infrastructure and release hygiene" |
| In-Progress Features | `in progress` tickets | Status / focus / ticket / next milestone |
| Expected Deliveries | `review` / `testing` tickets | State + current status + ticket |
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
