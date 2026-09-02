# Example Weekly Report - Munitron (W2 AUG 2026)

This is a real, worked example of the output format, auto-drafted from live
GitHub (merged PRs) and ClickUp (tasks by status) data. It is the gold standard
for **value-first writing**: every bullet leads with the client outcome, not the
internal ticket title. Use it as the reference for tone, structure, and depth.

---

# **Munitron - W2 AUG 2026 Weekly Update**

# **Overview**

This week centered on a major expansion of the platform's **voice (vishing)
capabilities** and a significant build-out of **employee risk intelligence** in
the tenant dashboard. The dominant execution pattern paired new feature surface
area (voice campaign controls, dialect-aware AI generation, and employee-level
risk views) with steady correctness work across campaigns, awareness, and
threat-intelligence flows.

Compared to the prior cycle, the focus shifted from foundational campaign
plumbing toward richer, customer-facing intelligence: security teams can now see
how risk is distributed across their people, and voice-based simulations gained
the realism controls needed for credible training scenarios.

* * *

# **Recent Delivery Highlights**

### **Voice (vishing) campaigns now sound real and localized**

Voice-based phishing simulations are far more convincing and easier to tailor to
your workforce.

*   **Match the accent to your people:** an optional dialect and accent selector
    generates AI voices that sound local, so a simulated call to a Gulf-based
    team lands as a Gulf-accented voice, not a generic one.
*   **Pick the right language with confidence:** a complete language matrix with
    voice previews lets you hear each option before you launch, so no campaign
    goes out with the wrong tone.
*   **Watch calls as they happen:** live call-status polling shows outbound call
    progress in real time, so you can track a campaign as it runs instead of
    waiting for a final report.

**Why this matters:** realistic, localized voice delivery is what makes vishing
training believable. Employees only build real resilience when the simulation
feels like a genuine call.

*   [\[Tenant-Admin{Voice Scenarios}\] Optional AI voice dialect/accent selector](https://app.clickup.com/t/869egxt94)
*   [\[Tenant-Admin{Voice Library}\] Language + gender UX for create/edit voices](https://app.clickup.com/t/869ehawbr)

### **See exactly where your human risk lives**

The dashboard now shows risk at the level of individual people and teams, not
just an organization-wide score.

*   **Spot your most vulnerable people:** an Employee Resilience Map shows how
    each person is doing, so you know who needs attention first.
*   **Understand how risk spreads:** a Risk Network view reveals risk
    relationships across employees, helping you find weak clusters, not just
    weak individuals.
*   **Target training where it counts:** clearer program coverage with group
    filters lets you confirm the right teams are actually enrolled.

**Why this matters:** turning one big risk number into a per-person, per-team
picture lets your security leads direct training and follow-up exactly where the
exposure is greatest.

*   [\[Tenant-Admin{Dashboard}\] Add employee Resilience Map](https://app.clickup.com/t/869edzr0v)
*   [\[Tenant-Admin{Employees}\] Add Risk Network tab](https://app.clickup.com/t/869edzqz7)

* * *

# **Key Improvements**

### **Campaign correctness and trustworthy reporting**

*   **One place for every campaign:** phishing and voice simulations are now a
    single unified campaign type, so you build and track both from one flow
    instead of juggling two.
    [\[Tenant-Admin{Campaigns}\] Merge phishing + vishing into one type](https://app.clickup.com/t/869egxt7g)
*   **Consistent tactics across everything:** the same psychological-tactic
    labels (urgency, authority, and the rest) now apply across phishing, vishing,
    and training, so your reporting compares like for like.
    [\[Tenant-Admin{Scenarios / Tactic Mastery}\] Unify psychological tactics](https://app.clickup.com/t/869ehcpm7)
*   **Numbers you can trust:** exported campaign metrics now match the in-app
    view exactly, and campaigns close themselves when their scheduled window
    ends, so you get clean final numbers without manual cleanup.

### **A complete experience in every language**

*   **Full right-to-left and translation coverage:** awareness graphs, OSINT
    pages, and partner-license flows now display correctly in every supported
    language, giving non-English teams a native experience with no broken labels.
    [\[Tenant-Admin{Threat Intelligence - Daily Digest}\] "Processing" digest handling](https://app.clickup.com/t/869egx4cj)
*   **Reliable threat briefings:** the daily threat-intelligence digest no longer
    gets stuck "processing," so your briefings arrive on schedule.

### **A faster, more stable platform**

*   **20 improvements shipped to production this week:** a steady stream of
    behind-the-scenes reliability work, including hardened media handling and
    smoother, more predictable interface behavior, keeps the platform fast and
    dependable as your usage grows.
    [View the merged work in GitHub](https://github.com/Akera-Agency/munitron/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-08-11..2026-08-17)

* * *

# **In-Progress Features**

### **Gamification System**

*   **What you will get:** a reward-based layer that keeps employees coming back
    to training, so awareness becomes a habit rather than a one-time event.
*   **Status:** in prototyping; finalizing the design before implementation.
*   [\[FEATURE\] Gamification System](https://app.clickup.com/t/869eapk22)

### **Mixed-Channel Phishing Scenarios**

*   **What you will get:** simulations that combine email, voice, and other
    channels in one coordinated attack, mirroring how real attackers actually
    operate for far more realistic testing.
*   **Status:** in development and testing.
*   [\[FEATURE{Dev}\] Mixed-Channel Phishing Scenarios](https://app.clickup.com/t/869egxt6r)

### **Spanish (ES) language support**

*   **What you will get:** full Spanish localization across the platform, opening
    it up to Spanish-speaking teams and regions.
*   **Status:** in progress.
*   [\[i18n\] Add Spanish (ES) locale support](https://app.clickup.com/t/869egxt8b)

* * *

# **Expected Deliveries This Week**

### **Predictive phishing-domain detection**

*   **What you will get:** the platform will flag lookalike and phishing domains
    before attackers use them against your people, moving protection from
    reactive to proactive.
*   **Current status:** in testing.
*   [\[FEATURE{Dev}\] Research predictive phishing domain detection](https://app.clickup.com/t/869egxt8x)

### **One-click phishing reporting in Outlook and Gmail**

*   **What you will get:** employees can report suspicious email straight from
    their inbox with a native add-in, making it effortless for staff to flag real
    threats and feed your reporting.
*   **Current status:** in code review.
*   [\[FEATURE{Dev}\] Outlook + Gmail Phishing Report Add-ins](https://app.clickup.com/t/869egxt65)

### **Guided Google Workspace onboarding**

*   **What you will get:** a step-by-step setup after connecting Google Workspace,
    so new tenants get up and running quickly with less support.
*   **Current status:** in testing.
*   [Add Google Workspace setup onboarding after connect](https://app.clickup.com/t/869em6u4c)

* * *

## **Meetings This Week**

*(Manual - to be filled in.)*
