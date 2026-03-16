---
name: research
description: 'Comprehensive competitive intelligence and ecosystem research. 9-phase framework for mapping ANY technology market from zero to complete competitive intelligence. Supports 2-tier search: WebSearch for quick lookups, imperium-crawl (optional npm) for deep/systematic research with bulk scraping, AI extraction, YouTube/Reddit mining. Use when the user mentions: research, competitors, competitive analysis, ecosystem, gap analysis, market map, landscape, alternatives, sentiment, demo videos, feature matrix, pricing benchmark, who else exists, map the market.'
user-invocable: false
---

# Research Skill

## Overview

A systematic 9-phase framework for mapping ANY technology market from zero to complete competitive intelligence. Works for open-source ecosystems, SaaS products, mobile apps, consumer tech, B2B platforms — anything.

**Output:** 10 deliverable documents covering ecosystem map, competitor profiles, feature matrices, demo video library, UI patterns, gap analysis, user sentiment, pricing benchmarks, and technical architecture.
See `references/deliverables.md` for full schemas and templates.

---

## Tool Selection

Before starting research, check available tools:

### Tier 1: Quick Research (always available)
- Use WebSearch for simple queries (1-5 searches)
- Use WebFetch to read specific URLs
- Good for: "who are competitors?", quick lookups, 1-5 sources
- No external dependencies, no API keys needed

### Tier 2: Deep Research (if imperium-crawl installed)
Check availability: `command -v imperium-crawl >/dev/null 2>&1`

If available, use imperium-crawl for:
- **Bulk search** across 12+ query strategies (`imperium-crawl search --query "..." --count 20`)
- **Parallel scraping** of 20+ sites (`imperium-crawl batch-scrape --urls "url1,url2" --extraction-schema "..."`)
- **AI-powered extraction** (`imperium-crawl ai-extract --url URL --schema '{...}'`)
- **YouTube analysis** — NO API key needed (`imperium-crawl youtube --action search/video/transcript/channel`)
- **Reddit mining** — NO API key needed (`imperium-crawl reddit --action search/posts/comments`)
- **Screenshots** (`imperium-crawl screenshot --url URL --full-page`)
- **Pricing extraction** (`imperium-crawl batch-scrape` with pricing schema)

If NOT available:
- Suggest: `npm install -g imperium-crawl`
- Fall back to WebSearch + WebFetch for all phases
- Note limitations: no parallelism, no transcripts, no screenshots

### CLI Syntax Gotchas
- Boolean flags — NO value after flag: `--full-page` ✅ `--full-page true` ❌
- JSON params — SINGLE QUOTES: `--schema '{"key":"value"}'` ✅
- Batch URLs — COMMA-SEPARATED IN QUOTES: `--urls "url1,url2"` ✅
- Freshness codes: pd=day, pw=week, pm=month, py=year

### Tier 2 Usage Per Research Phase

**Phase 1 (Ecosystem Mapping):**
imperium-crawl search --query "[category] software" --count 20
imperium-crawl search --query "[known competitor] alternatives" --count 20
imperium-crawl batch-scrape --urls "comp1.com,comp2.com" --extraction-schema "extract company name, tagline, pricing, features"

**Phase 2C (Video Discovery):**
imperium-crawl youtube --action search --query "[competitor] demo"
imperium-crawl youtube --action transcript --url "youtube.com/watch?v=..."
imperium-crawl youtube --action channel --channel-url "youtube.com/@competitor"

**Phase 4 (User Sentiment):**
imperium-crawl reddit --action search --query "[competitor] review"
imperium-crawl reddit --action posts --subreddit "startups" --sort top --time month

**Phase 7 (Pricing):**
imperium-crawl batch-scrape --urls "comp1.com/pricing,comp2.com/pricing" --extraction-schema "extract pricing tiers with name, price, features"

### Graceful Degradation Table

| imperium-crawl tool | Tier 1 Fallback | Limitation |
|---|---|---|
| search | WebSearch | Same quality, no JSON output |
| batch_scrape | WebFetch (sequential) | 10x slower, no parallelism |
| ai_extract | WebFetch + Claude analysis | Works but uses more tokens |
| youtube | WebSearch "site:youtube.com" | No transcript/chapters |
| reddit | WebSearch "site:reddit.com" | No comment threads |
| screenshot | No fallback | Suggest manual screenshots |

---

## Before You Start: Define the Research Scope

Every research project starts by answering these 5 questions:

1. **WHAT** are we researching? — Product category, open-source ecosystem, or market segment
2. **WHO** is our target customer? — B2C/B2B, size, geography
3. **WHAT** is our proposed USP? — What makes us different (to be validated)
4. **HOW DEEP** should we go? — Quick scan (10 competitors) / Standard (top 20) / Deep dive (full ecosystem)
5. **WHAT TYPE** of market? — Open-source / SaaS / App / Mixed

---

## THE 9-PHASE RESEARCH FRAMEWORK

---

### PHASE 1: ECOSYSTEM MAPPING
**Goal:** Build a complete inventory of everything that exists in this space.
**Priority:** P0 — Nothing else works without this.

#### 1A: Identify the Market Center

**For open-source ecosystems:** Find the core repository (GitHub URL, stars, forks, contributors, license), creator/maintainer status, Wikipedia page, governance structure, security incidents.

**For SaaS / App markets:** Find market leader(s), category definition on review sites, total market size estimates, key industry events, relevant communities (subreddits, forums).

#### 1B: Map ALL Competitors

Use all 12 search strategies — cast the widest net first, filter later.
Full strategy matrix: `references/search-strategies.md`

For EACH competitor, collect structured data using the competitor data schema.
Schema: `references/deliverables.md`

#### 1C: Map Ecosystem Tools & Infrastructure

For open-source ecosystems: hosting/managed platforms, plugin/skill marketplaces, monitoring/dashboard tools, memory/storage extensions, security tools, community resources.

#### 1D: Map Regional Variants

Search for region-specific competitors: China, India, Europe (GDPR), Southeast Asia, Latin America.

---

### PHASE 2: TOP 20 DEEP DIVE — UI, UX & DEMO VIDEOS
**Goal:** Pick top 20 competitors and study them in extreme detail.
**Priority:** P1

#### 2A: Selection Criteria

Score each competitor on: Relevance (1-5), Traction (1-5), Quality (1-5), Recency (1-5), Threat level (1-5). Take top 20 by total score.
Scoring details: `references/deliverables.md`

#### 2B: UI/UX Audit (for each of top 20)

Screenshot and document every screen category:
- **Onboarding:** Landing page, signup flow, first-time UX, onboarding wizard, time to first value
- **Core Product:** Main dashboard, primary interaction, secondary features, settings, search/nav
- **Team & Collaboration:** Invite flow, permissions, shared resources, activity feed
- **Business:** Pricing page, billing/upgrade flow, contact/support
- **Visual Identity:** Color scheme, typography, dark mode, mobile/responsive, empty/error/loading states

Validate all images before adding to library: `references/validation.md`

**Visual verification (REQUIRED):** After downloading screenshots, use the Read tool on EACH image file to visually confirm it passes validation. Claude's multimodal capability can detect:
- Wrong product (similar name, different UI)
- Generic logos/stock photos mistakenly captured
- Blurry, cropped, or outdated screenshots
- Marketing mockups vs actual product UI

Do NOT skip this step. Text-based URL analysis alone misses ~40% of irrelevant images.

#### 2C: Demo Video & Walkthrough Collection

A 5-minute demo video reveals more than an hour reading docs. Use all 8 search strategies.
Full strategies with imperium-crawl commands: `references/video-search.md`
Video validation rules: `references/validation.md`

**For video thumbnails:** If imperium-crawl captured video thumbnails, use the Read tool to verify the thumbnail actually shows the product — clickbait titles frequently mislead.
Video documentation schema: `references/deliverables.md`

#### 2D: Build UI Pattern Library

From screenshots and videos, extract: best patterns (steal these), worst patterns (avoid these), unique ideas worth adapting. Document which competitor does each thing best/worst and why.

---

### PHASE 3: FEATURE COMPARISON MATRIX
**Goal:** Know exactly who has what. Find the gaps.
**Priority:** P0

#### 3A: Define Feature Categories

Adapt to market type:
- **SaaS/Web:** Platform, core features (10-20), team/collaboration, integrations, security, pricing
- **Mobile Apps:** Platform, core features, social/community, personalization/AI, content library, monetization
- **Open-Source:** Core capabilities, plugin system, supported backends, deployment, community, docs, enterprise

#### 3B: Build the Matrix

Competitors as columns, features as rows. Values: Yes | No | Partial | Unknown
Matrix format: `references/deliverables.md`

#### 3C: Gap Analysis — THE MOST IMPORTANT OUTPUT

Answer these 5 questions:
1. **WHAT DOES NOBODY HAVE?** — Your biggest opportunity
2. **WHAT DOES EVERYONE HAVE?** — Your table stakes (must build)
3. **IS YOUR USP CONFIRMED?** — Did research validate your differentiation?
4. **TOP 3 COMPETITOR WEAKNESSES?** — Your potential strengths
5. **WHAT SURPRISED YOU?** — Adjust your vision accordingly

---

### PHASE 4: USER SENTIMENT ANALYSIS
**Goal:** What real users think — not what marketing says.
**Priority:** P1

**Sources by market type:**
- SaaS/B2B: G2, Capterra, TrustRadius, Reddit, Hacker News
- Consumer Apps: App Store, Play Store, Reddit, TikTok, YouTube
- Open-Source: GitHub Issues, Discord/Slack, Reddit, HN, Stack Overflow

**Extract:**
1. Top 10 LOVED features
2. Top 10 HATED problems
3. Top 10 REQUESTED features
4. #1 reason people choose the market leader
5. #1 reason people LEAVE the market leader
6. What people say about pricing
7. Security/privacy concerns
8. Most common "I wish it could..." statements
9. Most common competitor people switch FROM
10. Most common competitor people switch TO

---

### PHASE 5: ADJACENT COMPETITORS
**Goal:** Who else fights for the same budget?
**Priority:** P2

From the customer's perspective: "If I DON'T buy this, what do I do instead?"

Check: direct competitors, indirect competitors, DIY alternatives, big tech solutions, vertical-specific tools, "good enough" free options.

---

### PHASE 6: TECHNICAL ARCHITECTURE
**Goal:** How did others solve the hard problems?
**Priority:** P2

Research: infrastructure/scaling approach, core tech stack, security model, performance characteristics, migration path from prototype to production.

---

### PHASE 7: PRICING & BUSINESS MODEL
**Goal:** Data-driven pricing.
**Priority:** P1

Collect: full pricing benchmark table for all competitors, cost structure per user, market size (TAM/SAM/SOM), pricing psychology for the category.

---

### PHASE 8: NAMING & BRANDING
**Goal:** Available name that communicates positioning.
**Priority:** P2

For each candidate check: domains (.com, .ai, .io, .app), social handles (Twitter, Instagram, LinkedIn, TikTok), tech (GitHub, npm, App Store, Play Store), legal (USPTO, EUIPO, Google).

**RULE: Check availability BEFORE getting attached.**

---

### PHASE 9: SYNTHESIS & DELIVERABLES
**Goal:** 10 actionable documents.

Generate all 10 deliverables. Full list with schemas and templates: `references/deliverables.md`

---

## Execution Guide

### Task Distribution

**AI agents (bulk, parallelizable):** Phase 1 (find competitors), Phase 2C (find videos), Phase 4 (scrape reviews), Phase 7 (collect pricing)

**Human judgment:** Phase 2B (watch videos, evaluate UI), Phase 3C (gap analysis strategy), Phase 8 (name selection)

**Senior AI (complex analysis):** Phase 3B (feature matrix synthesis), Phase 6 (technical architecture), Phase 9 (full synthesis)

### Timeline

- **Week 1 (P0):** Phase 1 (ecosystem map) + Phase 2C (video collection) + Phase 3 (matrix + gaps)
- **Week 2 (P1):** Phase 2B (UI deep dive) + Phase 4 (sentiment) + Phase 7 (pricing)
- **Week 3 (P2):** Phase 5 (adjacent) + Phase 6 (tech) + Phase 8 (naming) + Phase 9 (synthesis)

---

## Anti-Patterns

- Building before finishing Phase 1 + 3
- Only analyzing top 3-5 competitors
- Skipping demo videos — they reveal more than docs
- Ignoring regional variants
- Trusting marketing over real user reviews
- Pricing by gut feel instead of benchmarks
- Getting attached to a name before checking availability
- Assuming your idea is unique without evidence
- 4 weeks researching, 0 weeks building — find the balance
- Unstructured notes instead of JSON — structure enables automation
