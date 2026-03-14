# Engineering Team Scaling

## Team Structure by Stage

| Stage | Size | Structure | Key Hires |
|-------|------|-----------|-----------|
| Pre-seed | 1-3 | Everyone does everything | Co-founder/CTO + 1-2 generalists |
| Seed | 3-8 | Full-stack generalists + specialist | First DevOps, first designer |
| Series A | 8-20 | 2-3 squads, tech lead per squad | Engineering manager, senior ICs |
| Series B | 20-50 | EM layer, platform team | VP Eng, principal engineers |
| Growth | 50+ | Multiple orgs, architecture team | Directors, staff engineers |

## Hiring Process

### Interview Pipeline
1. **Resume screen** (5 min): Does background match?
2. **Phone screen** (30 min): Culture fit, communication, high-level technical
3. **Technical interview** (60 min): Coding + system design (relevant to actual work)
4. **Team interview** (45 min): Collaboration, culture, working style
5. **Reference check** (2 calls): Always call references

### What to Optimize For

| Stage | Optimize For |
|-------|-------------|
| Early (1-10) | Speed, versatility, ownership mentality |
| Growth (10-30) | Depth of expertise, mentorship ability |
| Scale (30+) | Process, leadership, specialization |

### Red Flags in Candidates
- Can't explain past work simply
- Blames others for failures
- Only wants to work on "interesting" problems
- No questions about the product/business
- Wants to rewrite everything from scratch

## Engineering Culture

### Non-Negotiables
- **PR review < 24 hours** (better: same day)
- **Deploy to production daily** (or faster)
- **Blameless post-mortems** (learn, don't blame)
- **Document decisions** (ADRs for significant choices)
- **Knowledge sharing** (tech talks, pair programming, documentation)

### Meeting Hygiene
- No-meeting days (at least 2 per week)
- Standup < 15 min (async is even better)
- Every meeting has an agenda and clear outcome
- Default to 25-min or 50-min meetings

### On-Call
- Rotate fairly across the team
- Compensate on-call (time off or pay)
- Runbooks for common issues
- Post-incident review for every page
- Reduce noise: if it pages but doesn't need action, fix the alert

## Scaling Challenges & Solutions

### Bus Factor
**Problem:** Only one person understands a critical system
**Solution:** Pair programming, documentation, code reviews, rotation

### Communication Overhead
**Problem:** As team grows, coordination cost grows quadratically
**Solution:** Squad model, clear ownership, async communication, RFCs

### Quality at Speed
**Problem:** Moving fast without breaking things
**Solution:** CI/CD, automated testing, feature flags, canary deploys

### Hiring Pipeline
**Problem:** Not enough qualified candidates
**Solution:** Build employer brand, contribute to open source, speak at meetups, referral bonuses
