---
name: imperium:deep-research
description: Launch a full 9-phase competitive intelligence research project. Maps competitors, features, pricing, user sentiment, and generates 10 deliverable documents.
user-invocable: true
---

# Deep Research — Full Competitive Intelligence

You are launching a comprehensive 9-phase competitive intelligence research project using the Imperium research framework.

## Step 1: Scope the Research

Ask the user these 5 scoping questions (do not skip any):

1. **WHAT** are we researching?
   - A specific product category (e.g., "AI vocal coach apps")
   - An open-source ecosystem (e.g., "OpenClaw forks and platforms")
   - A market segment (e.g., "team productivity tools with AI")

2. **WHO** is our target customer?
   - Consumer (B2C) or Business (B2B)?
   - What size? (individual, small team, enterprise)
   - What geography? (global, US, EU, specific country)

3. **WHAT** is our proposed USP?
   - What do we think makes us different?
   - (This will be validated or invalidated by the research)

4. **HOW DEEP** should we go?
   - Quick scan: Top 10 competitors, high-level (1-2 hours)
   - Standard: Top 20, with UI/video analysis (multi-session)
   - Deep dive: Full ecosystem, sentiment, pricing (comprehensive)

5. **WHAT TYPE** of market is this?
   - Open-source ecosystem (core project with forks/platforms)
   - SaaS market (competing cloud products)
   - App market (mobile apps on App Store / Play Store)
   - Mixed (combination of the above)

## Step 2: Check Tool Availability

Run this check before starting research:

```bash
command -v imperium-crawl >/dev/null 2>&1 && echo "TIER_2_AVAILABLE" || echo "TIER_1_ONLY"
```

Report to the user:
- **If Tier 2 available**: "imperium-crawl is installed — using deep research mode with bulk scraping, YouTube transcripts, Reddit mining, and parallel data collection."
- **If Tier 1 only**: "Using WebSearch + WebFetch. For deeper research with bulk scraping, YouTube transcripts, and Reddit mining, install imperium-crawl: `npm install -g imperium-crawl`"

## Step 3: Execute the 9 Phases

Reference the research skill for full phase details: `skills/research/SKILL.md`

### Phase 1: Ecosystem Mapping (P0)
Map ALL competitors using the 12 search strategies.
Reference: `skills/research/references/search-strategies.md`

### Phase 2: Top 20 Deep Dive (P1)
Score and select top 20, then audit UI/UX and collect demo videos.
Reference: `skills/research/references/video-search.md`
Validation: `skills/research/references/validation.md`

### Phase 3: Feature Comparison Matrix (P0)
Build the feature matrix and run gap analysis.
Reference: `skills/research/references/deliverables.md` (matrix format + gap template)

### Phase 4: User Sentiment Analysis (P1)
Mine reviews from G2, Capterra, Reddit, App Store, GitHub Issues.
With imperium-crawl: `imperium-crawl reddit --action search --query "[competitor] review"`

### Phase 5: Adjacent Competitors (P2)
Map indirect competitors and substitutes.

### Phase 6: Technical Architecture (P2)
Research how competitors solved hard technical problems.

### Phase 7: Pricing & Business Model (P1)
Collect full pricing benchmarks.
With imperium-crawl: `imperium-crawl batch-scrape --urls "comp1.com/pricing,comp2.com/pricing" --extraction-schema "extract pricing tiers"`

### Phase 8: Naming & Branding (P2)
Check domain, social handle, and trademark availability.

### Phase 9: Synthesis & Deliverables
Generate all 10 deliverables.
Reference: `skills/research/references/deliverables.md`

## Step 4: Generate Deliverables

Create all 10 deliverables in a `research/` directory:

1. `ecosystem-map.md` — Every competitor categorized
2. `top-20-profiles.md` — Deep profile for each top competitor
3. `feature-matrix.md` — All features x competitors
4. `video-library.md` — All videos indexed and prioritized
5. `ui-patterns.md` — Best/worst UI patterns
6. `gap-analysis.md` — Opportunities and table stakes
7. `user-sentiment.md` — What users love, hate, want
8. `pricing-benchmark.md` — All prices + recommendation
9. `naming-decision.md` — Name + domains + handles
10. `updated-vision.md` — Vision refined by research

## Execution Notes

- Save progress after each phase — research is iterative
- For quick scan depth: focus on Phases 1, 3, 7 only
- For standard depth: all phases except 6 and 8
- For deep dive: all 9 phases with maximum coverage
- Always validate data quality using `skills/research/references/validation.md`
