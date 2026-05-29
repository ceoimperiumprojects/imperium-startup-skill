---
name: imperium:eval-loop
description: Run automated eval checks on the imperium-brain plugin. Reports pass/fail/warn with fix suggestions.
user-invocable: true
---

# Eval Loop — Automated Quality Checks

Run structural and routing checks on the imperium-brain plugin. Reports pass/fail/warn for every check, suggests prioritized fixes.

---

## Flow

### Step 1: Run the eval runner

```bash
python3 evals/eval-runner.py
```

This generates a timestamped report in `evals/results/`.

### Step 2: Read the latest results

Read the most recent file in `evals/results/` (sorted by filename = sorted by time).

### Step 3: Present structured summary

Format the results as:

```
## Eval Results — [timestamp]

### Summary: X PASS | Y FAIL | Z WARN

### Failures (fix first)
- [CHECK_NAME]: description of failure + suggested fix

### Warnings (fix next)
- [CHECK_NAME]: description of warning + suggested fix

### All Passing
- [CHECK_NAME]: OK (collapsed list)
```

### Step 4: Loop mode (when used with /loop)

When running in a recurring loop (e.g., `/loop 1h /imperium:eval-loop`):

1. Read the **previous** results file (second most recent)
2. Diff with current results
3. Report only **CHANGES** since last run:
   - New failures (was PASS, now FAIL)
   - Fixed issues (was FAIL, now PASS)
   - Unchanged failures (still FAIL — escalate priority)
4. If no changes: "All stable — no changes since last run."

### Step 5: Suggest prioritized fixes

Order fix suggestions by severity:
1. **FAIL** — Must fix before release
2. **WARN** — Should fix, but not blocking
3. **Enhancement** — Could improve but working fine

For each fix, provide:
- What's wrong
- Which file(s) to change
- Specific fix action (not vague guidance)

### Step 6: Offer to fix (with permission)

For FAIL items, offer to auto-fix:
- "I found 3 failures. Want me to fix them? (y/n)"
- Only fix with explicit user permission
- After fixing, re-run eval-runner.py to verify

---

## Usage Examples

```
# One-time check
/imperium:eval-loop

# Hourly recurring check
/loop 1h /imperium:eval-loop

# After making changes
/imperium:eval-loop
```

---

## What Gets Checked

The eval runner validates 17 structural checks across 2 tiers:

**Tier 1 — Structural Integrity:**
- Skill files exist (18 SKILL.md files)
- Frontmatter valid (YAML fields)
- References exist (non-empty files)
- Cross-references resolve (file paths in SKILL.md body)
- plugin.json sync (skills array vs directories)
- Command frontmatter (name, user-invocable)
- Hooks command count (correct number)
- Eval coverage (>= 2 per domain)
- Brand integration (7 content skills mention brand)
- Marketplace sync (counts, version)
- Agent files exist (8 agent .md files)
- Cookbook completeness (21 layouts + __init__.py)
- Counts consistency (all files agree)

**Tier 2 — Routing Accuracy:**
- Eval references exist (expected_references resolve)
- Eval skills in routing (expected_skills map to routing table)
- Eval assertion quality (>= 2 assertions each)
- Routing table completeness (every skill dir in table)

Full metric definitions: `evals/metrics.md`
