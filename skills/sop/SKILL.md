---
name: sop
description: 'SOP, runbook, and playbook generator. Creates structured process documents with checklists, decision trees, and role assignments. Use for documenting repeatable processes, incident response, onboarding workflows, or any standardized procedure. Triggers on: SOP, runbook, playbook, checklist, process document, standard operating procedure, workflow doc, procedure, operations manual, how-to guide, step-by-step process.'
user-invocable: false
---

# SOP, Runbook & Playbook Generator

Create structured process documents that teams can actually follow. Every step is actionable, every decision has clear criteria, every role is assigned.

## Keywords

SOP, runbook, playbook, checklist, process document, standard operating procedure, workflow doc, procedure, operations manual, how-to guide, step-by-step process, process map, incident response, onboarding, offboarding, deployment, launch checklist, sprint review, escalation, decision tree, workflow, process documentation

## Philosophy

- A process document nobody follows is worse than no document at all
- Every step must start with a verb — it's an instruction, not a description
- Ambiguity is the enemy: "as appropriate" and "as needed" are banned phrases
- If a step requires a decision, the criteria must be explicit
- Time estimates keep teams honest about effort
- Documents must be reviewed regularly — stale SOPs create false confidence
- The best process doc is the shortest one that covers all edge cases

## Document Types

### 1. SOP (Standard Operating Procedure)

**Purpose:** Document repeatable business processes so anyone can execute them consistently.

**Best for:** Customer onboarding, content publishing, hiring workflows, expense approvals, release processes, support ticket handling.

**Structure:**

```markdown
# {SOP Title}

## Document Info
| Field | Value |
|-------|-------|
| Owner | {Name, Role} |
| Last Updated | {Date} |
| Review Schedule | {Quarterly / Monthly / After incidents} |
| Version | {X.Y} |
| Approved By | {Name, Role} |

## Purpose
{One paragraph: Why does this SOP exist? What problem does it prevent?}

## Scope
{Who does this apply to? When is it used? What does it NOT cover?}

## Roles & Responsibilities
| Role | Responsibility | Person/Team |
|------|---------------|-------------|
| {Role} | {What they do in this process} | {Name or team} |

## Prerequisites
- [ ] {What must be true/ready before starting}
- [ ] {Access, permissions, tools needed}
- [ ] {Dependencies on other processes}

## Procedure

### Step 1: {Action Verb + Object}
**Owner:** {Role}
**Time estimate:** {X minutes}
**Details:**
{Detailed instructions. Be specific — include exact button names, menu paths, commands.}

**Checkpoint:** {How to verify this step is done correctly}

### Step 2: {Action Verb + Object}
...

## Exceptions & Edge Cases
| Scenario | Action |
|----------|--------|
| {What if X happens?} | {Do Y instead} |
| {What if Z is missing?} | {Escalate to / Wait for / Skip to step N} |

## Escalation Path
1. First: {Contact person/channel}
2. If unresolved in {time}: {Escalate to}
3. If critical: {Emergency contact}

## Success Criteria
- [ ] {How do you know the process completed successfully?}
- [ ] {What output/artifact should exist?}

## Revision History
| Date | Version | Change | Author |
|------|---------|--------|--------|
| {Date} | {X.Y} | {What changed} | {Name} |
```

### 2. Runbook

**Purpose:** Technical operations guide for executing or responding to specific technical scenarios. Emphasis on commands, rollback procedures, and escalation.

**Best for:** Database failover, deployment rollback, incident response, server maintenance, monitoring alert response, security incident handling.

**Structure:**

```markdown
# {Runbook Title}

## Overview
| Field | Value |
|-------|-------|
| System/Service | {What system this covers} |
| Owner | {Team or individual} |
| Severity | {P1-Critical / P2-High / P3-Medium / P4-Low} |
| Last Tested | {Date of last drill/dry-run} |
| Last Updated | {Date} |

## When to Use This Runbook
{Specific triggers — alert names, symptoms, error messages, or scenarios that should activate this runbook.}

**Trigger conditions:**
- {Alert: "alert-name" fires in monitoring}
- {Error: "specific error message" appears in logs}
- {Symptom: Users report X behavior}
- {Scheduled: During maintenance window on {schedule}}

## Prerequisites
- [ ] {Access/permissions required — list specific IAM roles, VPN, SSH keys}
- [ ] {Tools required — list CLI tools, dashboards, access}
- [ ] {Communication — who to notify before starting}

## Procedure

### Step 1: {Assess the Situation}
**Time estimate:** {X minutes}

Check current state:
```bash
# Command to check status
{command}
```

Expected output: `{what you should see}`
If output shows `{bad state}` → proceed to Step 2
If output shows `{good state}` → this runbook may not apply, verify the trigger

### Step 2: {Take Action}
**Time estimate:** {X minutes}

```bash
# Command to execute
{command}
```

**Verify:**
```bash
# Command to verify the action worked
{command}
```

Expected: `{successful output}`

### Step 3: {Confirm Resolution}
...

## Rollback Procedure

If any step fails or makes things worse, follow rollback:

### Rollback Step 1: {Undo Last Action}
```bash
# Rollback command
{command}
```

### Rollback Step 2: {Restore Previous State}
```bash
# Restore command
{command}
```

## Escalation

| Condition | Escalate To | Contact |
|-----------|-------------|---------|
| Step fails after retry | {Senior engineer} | {Slack/phone} |
| Data loss suspected | {Engineering lead + CTO} | {Phone immediately} |
| Customer impact > {N} minutes | {On-call manager} | {PagerDuty} |

## Post-Incident

After resolving:
1. Update the incident channel/ticket with resolution summary
2. Schedule a post-mortem within 48 hours
3. Document any deviations from this runbook
4. Update this runbook if steps were unclear or incorrect
5. File follow-up tickets for permanent fixes

## Related Runbooks
- {Link to related runbook 1}
- {Link to related runbook 2}
```

### 3. Playbook

**Purpose:** Strategic/tactical guide with decision points. Unlike SOPs (which are linear), playbooks branch based on scenarios.

**Best for:** Sales objection handling, crisis communication, competitive response, customer escalation, negotiation, marketing campaign execution.

**Structure:**

```markdown
# {Playbook Title}

## Objective
{What winning looks like. One sentence.}

## Context
{Background: Why does this playbook exist? What situation does it address? What's at stake?}

## Decision Framework

When {situation occurs}, evaluate:

```
{Situation/Input}
    │
    ├── If {Condition A} → Run Play 1
    ├── If {Condition B} → Run Play 2
    ├── If {Condition C} → Run Play 3
    └── If unclear → {Default action / Escalation}
```

## Play 1: {Scenario Name}

**Trigger:** {When to run this play}
**Goal:** {What success looks like for this scenario}
**Owner:** {Who leads}

### Steps:
1. **{Action}** — {Details, talking points, or instructions}
2. **{Action}** — {Details}
3. **{Action}** — {Details}

### Key Messages:
- {What to say / key talking point}
- {What to say / key talking point}

### What NOT to Do:
- {Common mistake to avoid}
- {Common mistake to avoid}

### Measure Success:
- {Metric or outcome that shows this play worked}

## Play 2: {Scenario Name}
...

## Play 3: {Scenario Name}
...

## Escalation Matrix
| Severity | Who Decides | Response Time |
|----------|-------------|---------------|
| Low | {Role} | {Timeframe} |
| Medium | {Role} | {Timeframe} |
| High | {Role} | {Timeframe} |
| Critical | {Role} | {Timeframe} |

## Metrics & Iteration
| Metric | Target | Current | Review Frequency |
|--------|--------|---------|-----------------|
| {Metric} | {Target} | {Current or TBD} | {Weekly/Monthly} |

Review this playbook: {frequency}
Last reviewed: {date}
```

### 4. Checklist

**Purpose:** Pre/post verification list. Simple, fast, no ambiguity.

**Best for:** Launch checklists, hiring checklists, sprint review prep, deployment verification, onboarding day-1, event planning, security audit.

**Structure:**

```markdown
# {Checklist Title}

## When to Use
{One sentence: what event or process triggers this checklist}

## Owner
{Who is responsible for completing this checklist}

## Checklist

### {Category 1}
- [ ] {Action item — specific, verifiable}
- [ ] {Action item — specific, verifiable}
- [ ] {Action item — specific, verifiable}

### {Category 2}
- [ ] {Action item}
- [ ] {Action item}
- [ ] {Action item}

### {Category 3 (if applicable)}
- [ ] {Action item}
- [ ] {Action item}

## Sign-Off
| Role | Name | Date | Signature |
|------|------|------|-----------|
| {Executor} | | | |
| {Reviewer} | | | |

## Notes
{Space for context, exceptions, or issues encountered during execution}
```

### 5. Process Map

**Purpose:** Visual workflow documentation with decision points. Shows the flow, not just the steps.

**Best for:** Customer support escalation, feature request pipeline, hiring pipeline, bug triage, content approval workflow, sales pipeline stages.

**Structure:**

```markdown
# {Process Map Title}

## Overview
{One paragraph: What process does this map? Who are the actors? What are the possible outcomes?}

## Process Diagram

```mermaid
flowchart TD
    A[{Trigger Event}] --> B{{{Decision Point 1}}}
    B -->|{Condition}| C[{Action}]
    B -->|{Condition}| D[{Action}]
    C --> E{{{Decision Point 2}}}
    E -->|{Condition}| F[{Outcome 1}]
    E -->|{Condition}| G[{Outcome 2}]
    D --> H[{Outcome 3}]

    style A fill:#3b82f6,color:#fff
    style F fill:#22c55e,color:#fff
    style G fill:#22c55e,color:#fff
    style H fill:#eab308,color:#000
```

## Step Details

### {Trigger}: {Trigger Event}
**Description:** {What initiates this process}
**Owner:** {Role}
**Input:** {What information/artifact arrives}

### {Decision}: {Decision Point 1}
**Criteria:**
| Condition | Route | Rationale |
|-----------|-------|-----------|
| {If X} | {Go to Action A} | {Why} |
| {If Y} | {Go to Action B} | {Why} |

### {Action}: {Step Name}
**Owner:** {Role}
**Time:** {Estimate}
**Details:** {What to do}
**Output:** {What this step produces}

## Owner Matrix
| Step | Owner | Backup | SLA |
|------|-------|--------|-----|
| {Step} | {Person/Role} | {Backup person} | {Time target} |

## Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| End-to-end time | Total process duration | {Target} |
| Bottleneck step | Slowest step | {Target time} |
| Completion rate | % of processes completed successfully | {Target %} |
```

## Output Formats

### Markdown (Default)
- Works everywhere: GitHub, Notion, Confluence, VS Code, any text editor
- Supports checkboxes for checklists (`- [ ]` syntax)
- Mermaid diagrams render in GitHub, GitLab, Notion, and many editors
- Recommended for most use cases

### HTML (Styled, Printable)
When the user requests HTML output or wants a printable version:
- Generate a self-contained HTML file with inline CSS
- Use brand colors if available, otherwise professional defaults
- Include print styles (`@media print`) for clean PDF output
- Add interactive checkboxes (JavaScript) for checklists
- Include a "Print" button in the header

### Mermaid Diagrams
For process maps, always include a Mermaid flowchart:
- Use `flowchart TD` (top-down) for sequential processes
- Use `flowchart LR` (left-right) for pipelines
- Color-code: blue for triggers, green for success outcomes, yellow for warnings, red for failures
- Keep diagrams under 15 nodes — split into sub-diagrams if larger
- Include the diagram in both Markdown and HTML outputs

## Brand Integration

Before generating any document, check if `brand/brand.json` exists.

**If brand files exist:**
- Read `brand/tone-of-voice.md` and adapt writing style:
  - Formal brand → formal document language
  - Casual brand → approachable but still clear instructions
  - Technical brand → include more technical detail by default
- Apply brand colors to HTML output:
  - Primary color → headings, table headers
  - Accent color → checkboxes, highlights
  - Background → page background
- Use brand terminology and vocabulary patterns
- Match the company's preferred naming conventions

**If no brand files exist:**
- Use clear, professional language
- Default tone: direct, specific, no jargon unless technical context requires it
- Use standard formatting without custom colors

## Quality Standards

Every document generated must pass this quality checklist:

### Content Quality
- [ ] Every step starts with an action verb (Configure, Deploy, Review, Send, Create, etc.)
- [ ] No ambiguous language — no "appropriately", "as needed", "if necessary" without criteria
- [ ] Decision points have explicit, measurable criteria
- [ ] Roles are assigned to every step and decision
- [ ] Time estimates are provided for each step
- [ ] Prerequisites are listed completely
- [ ] Failure/exception scenarios are handled
- [ ] Success criteria are defined and measurable

### Structure Quality
- [ ] Document info section is complete (owner, date, version, review schedule)
- [ ] Logical flow — steps build on each other correctly
- [ ] No circular references — process has clear start and end
- [ ] Escalation path is defined with contacts
- [ ] Revision history is initialized

### Usability Quality
- [ ] A new team member could follow this document without additional guidance
- [ ] Critical steps are clearly marked
- [ ] Rollback/recovery is documented for risky steps
- [ ] Related documents are linked
- [ ] Review schedule is set (documents must not go stale)

## Writing Guidelines

### Action Verbs for Steps
Use these to start every step:

| Category | Verbs |
|----------|-------|
| Create | Create, Generate, Build, Draft, Set up, Initialize |
| Review | Review, Verify, Validate, Confirm, Check, Inspect, Audit |
| Update | Update, Edit, Modify, Change, Adjust, Revise |
| Communicate | Send, Notify, Escalate, Report, Share, Announce, Inform |
| Execute | Run, Execute, Deploy, Launch, Trigger, Activate, Start |
| Decide | Evaluate, Assess, Determine, Decide, Classify, Triage |
| Complete | Close, Archive, Complete, Finalize, Sign off, Resolve |

### Banned Phrases
Replace these vague phrases with specific instructions:

| Instead of | Write |
|-----------|-------|
| "Handle appropriately" | "If severity is P1, call on-call. If P2+, create Jira ticket." |
| "As needed" | "If the build fails more than 2 times, restart the CI runner." |
| "Follow best practices" | List the specific practices to follow |
| "Ensure quality" | "Verify all unit tests pass and coverage is above 80%." |
| "In a timely manner" | "Within 2 business hours" |
| "Coordinate with the team" | "Send a message to #team-channel with the status update" |
| "Use judgment" | Provide the decision criteria |

### Time Estimate Guidelines
| Step Complexity | Typical Estimate |
|----------------|-----------------|
| Simple action (click, send, check) | 2-5 minutes |
| Review/verification | 10-15 minutes |
| Configuration change | 15-30 minutes |
| Full deployment | 30-60 minutes |
| Investigation/diagnosis | 30-60 minutes |
| End-to-end process | Sum of steps + 20% buffer |
