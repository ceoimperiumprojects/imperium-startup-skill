---
name: imperium:create-sop
description: Generate a SOP, runbook, playbook, or checklist. Creates structured process documents with clear steps, roles, and decision points.
user-invocable: true
---

# Create SOP / Runbook / Playbook

You are creating a structured process document using the Imperium SOP framework. Generate production-quality documents that teams can follow immediately.

## Step 1: Determine Document Type

Ask the user which type of document they need:

```
What type of process document do you need?

1. SOP (Standard Operating Procedure)
   → For repeatable business processes (onboarding, publishing, approvals)

2. Runbook
   → For technical operations and incident response (failover, deployment, alerts)

3. Playbook
   → For strategic situations with multiple responses (sales objections, crisis comms)

4. Checklist
   → For pre/post verification lists (launch, hiring, sprint review)

5. Process Map
   → For visual workflows with decision branches (escalation, pipeline, triage)
```

If the user's request makes the type obvious, skip this question and proceed.

**Decision shortcuts:**
- Mentions "incident", "deploy", "server", "database", commands → Runbook
- Mentions "objection", "response", "scenario", "if/then" → Playbook
- Mentions "launch", "verify", "before we", "make sure" → Checklist
- Mentions "flow", "diagram", "pipeline", "escalation path" → Process Map
- Everything else → SOP

## Step 2: Gather Information

Based on the document type, ask for relevant information.

### For SOP:
1. What process are you documenting?
2. Who are the roles involved? (and who owns the process?)
3. What triggers this process? (when does it start?)
4. Are there known exceptions or edge cases?
5. How often should this be reviewed?

### For Runbook:
1. What system/service does this cover?
2. What triggers this runbook? (alert name, error, symptom)
3. What severity level? (P1-Critical through P4-Low)
4. What tools/access are needed?
5. Who is the escalation path?

### For Playbook:
1. What situation does this playbook address?
2. What are the different scenarios/responses needed?
3. Who leads each response?
4. What does success look like?
5. How do you measure effectiveness?

### For Checklist:
1. What event/process triggers this checklist?
2. What are the main categories of items to check?
3. Who is responsible for completing it?
4. Who signs off?

### For Process Map:
1. What process/workflow are you mapping?
2. What triggers the process?
3. What are the main decision points?
4. What are the possible outcomes?
5. Who owns each step?

Skip any questions the user has already answered. If they've provided enough context, proceed directly to generation.

## Step 3: Load Brand

Check if `brand/brand.json` exists.

**If found:**
- Read `brand/tone-of-voice.md` and adapt writing style
- Formal brand → formal document language
- Casual brand → approachable but clear
- Use brand terminology and vocabulary

**If not found:**
- Use clear, professional language
- Direct, specific, no unnecessary jargon

## Step 4: Generate the Document

Load the appropriate template from `skills/sop/SKILL.md` and the full examples from `skills/sop/references/document-types.md`.

### Content Quality Rules

Every generated document must follow these rules:

1. **Every step starts with an action verb**
   - Good: "Send the welcome email to the customer"
   - Bad: "The welcome email should be sent"

2. **No ambiguous language**
   - Good: "If the build fails more than 2 times, restart the CI runner"
   - Bad: "Handle build failures appropriately"

3. **Decision points have explicit criteria**
   - Good: "If response time exceeds 500ms for 5 minutes, escalate to L2"
   - Bad: "If performance is bad, escalate"

4. **Roles assigned to every step**
   - Good: "**Owner:** CSM — Send follow-up email within 24 hours"
   - Bad: "Follow up with the customer"

5. **Time estimates on every step**
   - Good: "**Time estimate:** 15 minutes"
   - Bad: (no estimate)

6. **Prerequisites listed completely**
   - Include access, tools, permissions, dependencies

7. **Exception handling defined**
   - What if a step fails? What if conditions are unusual?

8. **Success criteria are measurable**
   - Good: "Customer activates within 7 days"
   - Bad: "Customer is successfully onboarded"

### Output Format

**Default: Markdown**
Generate the document in Markdown format. This works in GitHub, Notion, Confluence, VS Code, and any text editor.

**If user requests HTML:**
Generate a self-contained HTML file with:
- Inline CSS for professional styling
- Brand colors applied (if available)
- Interactive checkboxes (JavaScript)
- Print styles for PDF export
- A "Print" button in the header

**If Process Map:**
Always include a Mermaid flowchart diagram in addition to step details:
- Use `flowchart TD` for sequential processes
- Use `flowchart LR` for pipelines
- Color-code: blue (#3b82f6) for triggers, green (#22c55e) for success, yellow (#f59e0b) for warnings, red (#ef4444) for failures
- Keep under 15 nodes — split into sub-diagrams if larger

## Step 5: Deliver and Offer Next Steps

After generating the document:

1. **Save the file** to the current directory or specified path
   - Default filename: `{process-name}-{type}.md` (e.g., `customer-onboarding-sop.md`)

2. **Run the quality checklist** internally — verify all rules are met before delivering

3. **Offer enhancements:**
   - "Want me to add more exception handling for edge cases?"
   - "Should I create a process map diagram for this workflow?"
   - "Need an HTML version for printing or sharing?"
   - "Want me to create related documents? (e.g., a checklist that pairs with this SOP)"
   - "Should I add a training guide based on this SOP?"

4. **Suggest maintenance:**
   - "Set a calendar reminder to review this document on {suggested date based on review schedule}"
   - "Consider running a dry-run of this process with the team before going live"

## Reference

Load the SOP skill from `skills/sop/SKILL.md` for document structures, quality standards, and writing guidelines.

Load full examples from `skills/sop/references/document-types.md` for complete templates and the decision guide.
