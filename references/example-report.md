# Example Weekly Report — The Key (W03 APR 2026)

This is a real, worked example of the output format. It is adapted from a live
edition in the ClickUp Weekly Reports list. Use it as the gold standard for tone,
structure, and depth.

---

# **The Key – W03 APR 2026 Weekly Update**

# **Overview**

This week centered on high-impact scheduling and assignment reliability work,
with a strong stabilization push across exam booking, gradebook integrity, and
learning-flow continuity. The dominant execution pattern was clear: close
production bugs fast while advancing larger scheduling UX and operations
enhancements through code review and testing.

Compared to W02, this cycle shifted from broad quality cleanup to more
operationally consequential improvements for coordinators and instructors,
especially around lab/interval scheduling controls, exportability, and safer
attempt handling in SEB-linked flows.

* * *

# **Recent Delivery Highlights**

### **Exam scheduling reliability and student booking safeguards**

A concentrated release stream resolved multiple booking integrity issues and
improved trust in scheduling outcomes.

*   **What users can now do more reliably:**
    *   Book and manage exam slots with fewer invalid-state edge cases (past-time
        booking, completed-exam rebooking, missed-exam reset behavior)
    *   View cleaner scheduling metadata in student-facing flows (including
        rendering fixes for lab labels)
    *   Operate daily scheduling flows with fewer support escalations
*   **Why this matters:** Scheduling integrity is core to exam operations; these
    fixes reduce operational noise and prevent invalid student states before they
    become support incidents.

*   [\[BUG: Exam scheduling - Student\] Missed exam incorrectly resets to "Book Now"](https://app.clickup.com/t/869cuxu59)
*   [\[Admin\] Attempts: In-Progress Attempts Page Not Loading](https://app.clickup.com/t/869ct9ya6)
*   [\[BUG: Manual Booking (Super Admin)\] Unable to scan exam for manually created bookings](https://app.clickup.com/t/869crmgnq)

* * *

# **Key Improvements**

### **Gradebook and attempt-flow correctness**

*   [\[ENHANCEMENT\] Exam Scheduling - Lab & Interval Management Improvements](https://app.clickup.com/t/869cz025n)
*   [\[BUG: Assignments + SEB\] Lockdown mode assignment status + error handling fix](https://app.clickup.com/t/869ctbaxz)
*   [\[BUG: Gradebook\] Unable to set grade weight to 0 for GetTheKey](https://app.clickup.com/t/869cw0k33)

### **Operational controls for coordinators and instructors**

*   [\[ENHANCEMENT\] Schedule Slot - Export Booked Students (CSV or PDF)](https://app.clickup.com/t/869cwefwc)
*   [\[ENHANCEMENT\] Exam Scheduling Calendar - Quick Add Interval via Plus Action](https://app.clickup.com/t/869cwdtk4)
*   [\[UX\] Exam Scheduling - Assign Labs nested dropdown](https://app.clickup.com/t/869cvx4p4)

### **Infrastructure and release hygiene**

*   [Merged backend/infrastructure stream in GitHub (37 merged PRs this week)](https://github.com/Thekey-sa/moodle-monorepo/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-13..2026-04-19)
*   CI, migration, and scheduling-related backend updates continued to reduce
    release friction and regression risk.

* * *

# **In-Progress Features**

### **Exam Scheduling – Calendar UX Redesign**

*   **Status:** In Progress
*   **Current focus:** improving calendar navigation and readability for
    high-volume scheduling operations.
*   **Current ticket:** [\[ENHANCEMENT\] Exam Scheduling – Calendar UX Redesign](https://app.clickup.com/t/869cwe74r)
*   **Next milestone:** complete implementation pass and move into structured QA.

### **Student Copilot and assignment-control enhancements**

*   **Status:** In Progress
*   **Current focus:** advancing Copilot and attempt-management experiences while
    keeping core assignment flows stable.
*   **Next milestone:** merge in-progress scope and prepare demo-ready branch.

* * *

# **Expected Deliveries This Week**

### **Lab & interval scheduling management improvements**

*   **Expected state:** stronger validation, clearer naming, and smoother
    scheduling control for coordinators.
*   **Current status:** in code review.
*   **Primary ticket:** [\[ENHANCEMENT\] Lab & Interval Management Improvements](https://app.clickup.com/t/869cz025n)

### **Scheduling exports and quick interval actions**

*   **Expected state:** easier operational execution through export and faster
    interval actioning.
*   **Current status:** in code review.

* * *

## **Meetings This Week**

### **Monday, April 20 @ 4:30 PM – The Key Standup & Progress Call**

Weekly plan alignment, release review, and confirmation of priorities for
scheduling and assignment reliability streams.

### **Thursday, April 23 @ 4:30 PM – The Key Standup & Progress Call**

Mid-week progress checkpoint, demo-readiness review, and blocker triage for
in-review and in-testing items.
