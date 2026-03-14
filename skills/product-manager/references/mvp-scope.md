# MVP Scoping

## MVP Definition
- **Minimum:** Smallest thing that tests your hypothesis
- **Viable:** Actually solves the problem (even if ugly)
- **Product:** Usable by real people (not a prototype or mockup)

## Scope Cutting Exercise

For each proposed feature, ask:
1. Can we launch without this? → Yes? Cut it.
2. Can we do a simpler version? → Yes? Simplify.
3. Must have or nice to have? → Nice to have? Cut it.
4. Can this be manual instead of automated? → Yes? Do it manually first.
5. Does this test our core hypothesis? → No? Cut it.

## MVP Types

| Type | What It Is | Time | Cost | Best For |
|------|-----------|------|------|----------|
| Landing page | Value prop + signup | 1 day | $0-100 | Testing demand |
| Concierge | Deliver service manually | 1-2 weeks | $0 | Testing value |
| Wizard of Oz | Looks automated, actually manual | 2-4 weeks | Low | Testing UX |
| Piecemeal | Built from existing tools | 1-2 weeks | $50-500 | Testing workflow |
| Single feature | One core feature, polished | 2-6 weeks | Dev time | Testing core value |

## Launch Criteria

### Before Launch
- [ ] Core value proposition works (users can achieve the main job)
- [ ] Critical bugs fixed (no data loss, no security holes)
- [ ] Basic error handling (graceful failures, not crashes)
- [ ] One complete user flow (start to finish, no dead ends)
- [ ] Basic analytics (you can measure success metrics)

### NOT Required for Launch
- Perfect UI/UX (functional > beautiful for MVP)
- Edge case handling (cover 80% of cases)
- Admin panel (do it manually)
- Multi-language support
- Advanced features
- Perfect documentation

## Post-MVP Decision Framework

After launching MVP, measure for 2-4 weeks, then decide:

| Signal | Action |
|--------|--------|
| Users keep coming back (retention) | Double down, add features |
| Users sign up but don't return | Fix activation/onboarding |
| Users return but won't pay | Test pricing, find willingness to pay |
| Nobody signs up | Revisit problem/audience/distribution |
| Users request different features | Pivot the solution (keep the problem) |
| Users describe a different problem | Pivot the problem (start over on discovery) |
