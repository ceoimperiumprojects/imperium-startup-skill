---
name: imperium-brain
description: 'The Ultimate Startup OS for Claude Code. Routes to 18 domain skills across startup ops, competitive research, and content creation. Use when the user mentions anything related to: startups, strategy, fundraising, marketing, sales, product, finance, legal, engineering, competitive research, ecosystem mapping, LinkedIn posts, carousels, presentations, slides, brand identity, tone of voice, SOPs, runbooks, video creation, API discovery, images, visual media, stock photos, or any business/startup/content topic.'
user-invocable: false
---

# Imperium Brain — Startup Operating System

18 skills, 8 agents, 19 commands. Complete startup intelligence + content creation.

---

## ROUTING TABLE

Read the user prompt. Match keywords to ONE skill (max 2 if cross-domain). Load ONLY the matched skill — never load all skills at once.

### STARTUP OPS (9 skills — unchanged)

| Keywords | Skill |
|----------|-------|
| CEO, strategy, vision, board, pivot, stakeholder, fundraising, pitch deck, investor, raise, round, valuation, term sheet | `skills/ceo-advisor` |
| CTO, architecture, tech stack, build vs buy, tech debt, scaling, infrastructure, system design | `skills/cto-advisor` |
| product, PRD, roadmap, prioritize, RICE, ICE, feature, backlog, user story, MVP, discovery | `skills/product-manager` |
| marketing, SEO, content strategy, copywriting, landing page, email sequence, social media, growth, CRO, positioning, ads | `skills/marketing` |
| sales, cold email, outbound, pipeline, leads, GTM, go-to-market, negotiation, B2B, prospecting, triggers | `skills/sales-gtm` |
| finance, metrics, MRR, ARR, CAC, LTV, churn, runway, burn rate, financial model, unit economics | `skills/finance` |
| founder, validate idea, Mom Test, interviews, competitor analysis, persona, imposter, mindset, knowledge base | `skills/founder` |
| legal, entity, LLC, incorporation, contracts, NDA, compliance, IP, trademark | `skills/legal` |
| engineering, agent design, RAG, MCP, API design, CI/CD, advanced architecture | `skills/engineering-advanced` |

### RESEARCH & INTELLIGENCE (2 skills — new)

| Keywords | Skill |
|----------|-------|
| research, competitors, competitive analysis, ecosystem, gap analysis, market map, landscape, alternatives, who else, sentiment, demo videos, feature matrix, pricing benchmark | `skills/research` |
| hidden API, discover APIs, endpoint, SPA, intercept, XHR, fetch requests, websocket, internal API, reverse engineer API | `skills/api-discovery` |

### CONTENT CREATION (6 skills — new)

**Rule:** Before generating ANY content, check if `brand/brand.json` exists. If yes, read `brand/brand.json` + `brand/tone-of-voice.md` and apply brand colors, fonts, and voice. If no, use sensible defaults and suggest running `/imperium:create-brand`.

| Keywords | Skill |
|----------|-------|
| brand, brand identity, voice, tone of voice, colors, fonts, visual identity, brand guide, brand system | `skills/brand-voice` |
| LinkedIn, LinkedIn post, viral post, hook, engagement, thought leadership, personal brand, LinkedIn algorithm | `skills/linkedin` |
| carousel, PPTX, PowerPoint, deck, pitch deck design, slide deck, presentation slides | `skills/carousel` |
| video, MP4, Remotion, demo video, explainer, social clip, video content, animation | `skills/video` |
| HTML slides, web presentation, reveal.js, browser slides, keynote alternative | `skills/slides` |
| SOP, runbook, playbook, checklist, process document, standard operating procedure, workflow doc | `skills/sop` |
| image, images, photo, find images, find visuals, stock photo, stock video, b-roll, visual media, pictures | `skills/visual-media` |

---

## ROUTING RULES

1. **Max 2 skills per request.** If a query spans 3+ domains, ask the user to narrow focus.
2. **Brand context is lightweight.** When loading for content skills, brand.json adds ~150 tokens. Always load it.
3. **Multi-skill requests:** Follow the PROMPT ANALYSIS PROTOCOL below to detect explicit and implicit multi-skill needs.
4. **Startup ops routing is unchanged.** All 9 existing skills work exactly as before.
5. **Never load skill body until routing is decided.** Read the frontmatter/description first.

---

## PROMPT ANALYSIS PROTOCOL

5-step protocol for detecting explicit AND implicit multi-skill needs. Replaces static keyword matching with intelligent intent analysis.

### Step 1: Extract Explicit Intents

Scan the user prompt for direct keyword matches against the ROUTING TABLE above.

- Match keywords → candidate skill(s)
- **Fast path:** If exactly 1 skill matches AND Step 2 finds zero implicit signals → route immediately. No further analysis needed. This handles ~90% of requests.

### Step 2: Detect Implicit Intents

Even when the user names only one deliverable, certain language signals reveal hidden prerequisites. Scan for these patterns:

**Data signals** → research prerequisite needed:
- "data-driven", "backed by data", "with stats", "with numbers"
- "based on market", "based on competitors", "how we stack up"
- "gaps in the market", "whitespace", "underserved"
- "differentiator", "unique angle", "what makes us different"
- "landscape", "who else is doing this", "market overview"

**Brand signals** → brand prerequisite needed:
- "on-brand", "in our voice", "our tone", "brand-consistent"
- "our colors", "matching our identity", "our style"
- "brand guidelines", "visual identity"

**Strategy signals** → ceo-advisor prerequisite needed:
- "should we", "what direction", "how to position ourselves"
- "moat", "defensibility", "strategic advantage"
- "where to play", "how to win", "our positioning"

**Temporal signals** → sequential execution:
- "then", "after that", "based on findings", "once we have", "from the results"

**Parallel signals** → concurrent execution:
- "and also", "plus create", "across all channels", "simultaneously"

**Visual signals** → visual-media prerequisite needed:
- "with images", "add photos", "find images for", "include visuals"
- "with screenshots", "product images", "stock photos"
- Content request + carousel plan includes image layouts

### Step 3: Check Existing State

Before adding prerequisite skills, check what already exists in the filesystem:

1. **Brand check:** Does `brand/brand.json` exist?
   - YES → use existing brand, do NOT add brand-voice as prerequisite
   - NO + brand signals detected → inform user, suggest `/imperium:create-brand` as prerequisite

2. **Research check:** Do research output files exist in cwd? (`ecosystem-map.md`, `gap-analysis.md`, `competitive-*.md`, `market-*.md`)
   - YES → use existing research files as input, do NOT re-run research
   - NO + data signals detected → inform user, add research as prerequisite

3. **Neither exists + signals detected:** Tell the user what prerequisite is needed and why, then suggest the execution plan.

### Step 4: Resolve Dependencies

When multiple skills are identified, resolve execution order using the dependency graph:

**Dependencies (must run sequentially):**
- `research` → `content` (any content skill needs research data first)
- `brand-voice` → `content` (brand must exist before content applies it)
- `research` → `ceo-advisor` (strategy needs market data)
- `research` → `sales-gtm` / `marketing` (GTM needs market intelligence)

**Parallel-safe combinations (same dependency level):**
- `linkedin` + `carousel` (both consume same research/brand inputs)
- `sales-gtm` + `marketing` (both consume same research inputs)
- `slides` + `sop` (independent content outputs)

**Execution order:** Prerequisites first → then primary skill(s), parallel where safe.

### Step 5: Confirm if Multi-Step

Choose the right confirmation level based on what was detected:

| Scenario | Action |
|----------|--------|
| 1 skill, no implicit signals | Route immediately — no confirmation needed |
| 2 skills, both explicitly stated | Brief plan statement ("I'll research first, then create the post"), then execute |
| 2+ skills, any were inferred from implicit signals | Ask user to confirm before executing ("I noticed you want data-driven content — should I run research first?") |
| Ambiguous — could be 1 or 2 skills | Ask user to clarify intent |

### Quick Reference: Common Implicit Patterns

| User says | They need | Why |
|-----------|-----------|-----|
| "write a data-driven LinkedIn post about our market" | research → linkedin | "data-driven" + "our market" = data signals |
| "create an on-brand carousel about competitors" | brand-voice → research → carousel | "on-brand" = brand signal, "competitors" = data signal |
| "position ourselves uniquely in the market" | research → ceo-advisor | "position" + "market" = strategy + data signals |
| "write a post about what makes us different" | research → linkedin | "what makes us different" = data signal (differentiator) |
| "create content across all channels" | linkedin + carousel + slides (parallel) | "across all channels" = parallel signal |
| "should we pivot based on competitor moves" | research → ceo-advisor | "should we" = strategy signal, "competitor" = data signal |

---

## AGENT COMPOSITION

### When to use single vs multi-agent
- **Single agent**: User request maps cleanly to one domain (e.g., "write a LinkedIn post", "research competitors")
- **Multi-agent**: User request spans two domains with clear dependency (e.g., "research competitors then create content from findings")
- **Max 2 agents per request** — same as max 2 skills. If 3+ agents needed, break into sequential requests.

### Sequential execution rule
1. First agent runs to completion, saves output to working directory
2. Second agent starts, reads output files from first agent
3. Each agent focuses on its domain — no scope creep across boundaries

### Output convention
- Agents write deliverables to the working directory (markdown, JSON, PPTX, etc.)
- File names follow skill conventions (e.g., `ecosystem-map.md`, `gap-analysis.md`, `top-20-profiles.md`)
- Next agent reads these files as input — no need for explicit "handoff" mechanism
- If an agent produces structured data (JSON, tables), downstream agents should parse and reference it directly

### Brand as shared state
- Brand is NOT an agent-to-agent handoff — it's shared context available to ALL content agents
- `brand/brand.json` + `brand/tone-of-voice.md` are always checked before content creation
- Brand architect creates these files once; all content agents consume them automatically

---

## CROSS-DOMAIN WORKFLOWS

Six common multi-agent workflows. Each specifies trigger, order, handoff, and example prompt.

### 1. Research → LinkedIn Post
- **Trigger**: "research" + "post" / "LinkedIn" / "write about findings"
- **Order**: market-researcher → content-creator (linkedin)
- **Handoff**: Research outputs `ecosystem-map.md`, `gap-analysis.md`, `top-20-profiles.md` → LinkedIn skill reads findings as source material instead of doing own WebSearch
- **Example**: "Research the AI coding assistant market then write a LinkedIn post about the top insights"

### 2. Research → Pitch Deck / Carousel
- **Trigger**: "research" + "deck" / "carousel" / "presentation" / "slides"
- **Order**: market-researcher → content-creator (carousel/slides)
- **Handoff**: Research outputs competitor data, feature matrix, pricing benchmarks → carousel builds positioning deck using real data
- **Example**: "Analyze our competitors then create a pitch deck showing our positioning"

### 3. Brand → Any Content
- **Trigger**: "brand" + any content keyword (post, carousel, slides, SOP)
- **Order**: brand-architect → content-creator
- **Handoff**: Brand generates `brand/brand.json` + `brand/tone-of-voice.md` → all content skills auto-detect and apply brand colors, fonts, voice
- **Example**: "Create our brand identity then make a LinkedIn carousel introducing the company"

### 4. Research → CEO Strategy
- **Trigger**: "research" + "strategy" / "positioning" / "where we stand"
- **Order**: market-researcher → ceo-strategist
- **Handoff**: Research outputs ecosystem map, pricing benchmarks, market gaps → CEO advisor uses for strategic positioning and decision-making
- **Example**: "Map the competitive landscape for project management tools then help me decide our strategic positioning"

### 5. Research → GTM Plan
- **Trigger**: "research" + "GTM" / "go-to-market" / "launch strategy"
- **Order**: market-researcher → sales-hunter + growth-marketer
- **Handoff**: Research outputs market map, ICP signals, competitor weaknesses → sales builds outbound strategy, marketing builds inbound strategy
- **Example**: "Research the developer tools market then build our go-to-market plan"

### 6. Full Content Pipeline
- **Trigger**: "brand" + "research" + content keywords (or explicit "full pipeline")
- **Order**: brand-architect → market-researcher → content-creator (parallel: linkedin + carousel + slides)
- **Handoff**: Brand first (creates visual/voice system) → research second (creates data/insights) → content last (uses both brand + research as inputs)
- **Example**: "We're launching next month — create our brand, research the market, then generate launch content across all channels"

### 7. Visual Media → Content
- **Trigger**: "find images" + content keyword, OR image layouts in carousel plan with no images provided
- **Order**: visual-media → content-creator (carousel/linkedin)
- **Handoff**: Visual-media saves images to `media/images/[topic-slug]/` → carousel uses paths in image layouts, linkedin recommends for post
- **Example**: "Find relevant images about AI coaching and create a carousel with them"

---

## AVAILABLE COMMANDS

### Startup Ops (existing)
- `/imperium:validate-idea` — Startup idea validation
- `/imperium:pitch-deck` — Pitch deck creation
- `/imperium:fundraise-prep` — Fundraising preparation
- `/imperium:cold-email` — Cold email campaigns
- `/imperium:competitor-matrix` — Competitive matrix
- `/imperium:pricing-strategy` — Pricing strategy
- `/imperium:gtm-plan` — Go-to-market plan
- `/imperium:metrics-dashboard` — SaaS metrics dashboard
- `/imperium:founder-kb` — Knowledge base search

### Research & Intelligence (new)
- `/imperium:deep-research` — Full 9-phase competitive intelligence
- `/imperium:discover-apis` — Hidden API discovery for any website
- `/imperium:crawl-check` — Check imperium-crawl installation & capabilities

### Content Creation (new)
- `/imperium:create-brand` — Brand identity wizard (colors, fonts, voice)
- `/imperium:linkedin-post` — LinkedIn viral post generator
- `/imperium:carousel` — PPTX carousel/deck creation
- `/imperium:create-video` — Video content (bridge to Remotion)
- `/imperium:create-slides` — HTML presentation slides
- `/imperium:create-sop` — SOP/runbook/playbook generator
- `/imperium:find-images` — Image/video sourcing with visual AI review

---

## AVAILABLE AGENTS

### Startup Ops (existing)
- **ceo-strategist** — Strategic decisions, fundraising, board prep
- **cto-architect** — Architecture, tech stack, scaling
- **growth-marketer** — Marketing campaigns, SEO, content
- **sales-hunter** — Outbound sales, pipeline, GTM
- **product-analyst** — PRD, roadmap, prioritization

### Research & Content (new)
- **market-researcher** — Deep competitive intelligence, ecosystem mapping
- **content-creator** — LinkedIn posts, carousels, slides, SOPs, video
- **brand-architect** — Brand identity creation, voice definition

---

## BRAND SYSTEM

Shared resource at `brand/` — generated by `/imperium:create-brand`.

**Files:**
- `brand/brand.json` — 10 colors, 3 fonts, asset paths
- `brand/config.json` — Output settings (format, naming)
- `brand/brand-system.md` — Design philosophy, visual rules
- `brand/tone-of-voice.md` — Voice character, vocabulary, platform adaptations
- `brand/templates/` — 5 pre-built voice templates

**Usage:** Content skills auto-detect and apply brand. No brand = defaults + suggestion to create one.

---

## EXTERNAL TOOL INTEGRATION

### imperium-crawl (optional, npm)
Deep research uses imperium-crawl for bulk scraping, AI extraction, YouTube/Reddit mining.
- Check: `command -v imperium-crawl`
- Install: `npm install -g imperium-crawl`
- Falls back to WebSearch + WebFetch if not installed.

### Remotion (optional, npm)
Video skill bridges to Remotion for MP4/animation creation.
- Check: look for `remotion.config.*` or `package.json` with remotion dependency
- Install: `npx create-video@latest`
- Falls back to HTML slides or carousel if not available.
