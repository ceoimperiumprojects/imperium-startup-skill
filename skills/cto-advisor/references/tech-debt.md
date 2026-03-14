# Tech Debt Management

## Tech Debt Quadrant

| | Reckless | Prudent |
|---|---------|---------|
| **Deliberate** | "We don't have time for design" | "We know this is a shortcut, and we know how to fix it" |
| **Inadvertent** | "What's architecture?" | "Now we know how we should have built it" |

**Only deliberate-prudent debt is acceptable.** Track it, schedule it, pay it down.

## Tech Debt Prioritization

### Priority Matrix

| | High Frequency (touched often) | Low Frequency (rarely touched) |
|---|-------------------------------|-------------------------------|
| **High Impact (causes bugs/slowdown)** | Fix NOW (Sprint 0) | Fix this quarter |
| **Low Impact (cosmetic/minor)** | Fix when touching that code | Probably never |

### The 20% Rule
Allocate 20% of every sprint to tech debt. Non-negotiable.

**Rationale:** Tech debt compounds. Ignoring it leads to:
- Slower feature development (2-5x over 2 years)
- Higher bug rate
- Team frustration and attrition
- Harder to hire (nobody wants to work on a mess)

## Tech Debt Tracking

### Debt Registry Template
| ID | Description | Category | Impact | Effort | Priority | Owner |
|----|-------------|----------|--------|--------|----------|-------|
| TD-001 | | Code / Architecture / Test / Infra / Docs | H/M/L | S/M/L | P1-P4 | |

### Categories
- **Code debt:** Duplicated code, complex functions, poor naming
- **Architecture debt:** Wrong patterns, tight coupling, scaling limits
- **Test debt:** Missing tests, flaky tests, slow test suite
- **Infrastructure debt:** Manual deployments, no monitoring, outdated dependencies
- **Documentation debt:** Missing docs, outdated docs, tribal knowledge

## Refactoring Strategies

### The Strangler Fig Pattern
1. Build new functionality alongside the old
2. Route traffic gradually to the new
3. Remove the old when migration is complete
4. Never do a "big rewrite" — it always takes 3x longer

### Boy Scout Rule
"Leave the code better than you found it."
- Touching a file? Fix one small thing while you're there.
- Don't scope-creep into a refactor, but clean as you go.

### Refactoring Budget Justification
Frame debt paydown in business terms:
- "This refactor will cut deploy time from 45 min to 5 min = 10 hours/week saved"
- "Fixing this coupling will let us ship the next 3 features 2x faster"
- "This test improvement will reduce production bugs by ~40%"
