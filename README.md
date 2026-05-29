<div align="center">

# 🧠 imperium-brain

### The Ultimate Startup OS for Claude Code.

**18 Skills** · **80+ References** · **20 Slash Commands** · **8 Sub-Agents** · **87 Evals** · **Intelligent Routing**

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-blueviolet?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMkw0IDdWMTdMMTIgMjJMMjAgMTdWN0wxMiAyWiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+)](https://github.com/ceoimperiumprojects/imperium-brain)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-18-orange?style=for-the-badge)]()

> Startup ops + competitive research + content creation — all in one plugin. From pitch deck to LinkedIn viral post, from competitor analysis to brand identity. Built from **7 repos**, **10 books**, and **121K+ impressions** of proven content.

</div>

---

## Quick Start

```bash
# Install
claude plugin marketplace add ceoimperiumprojects/imperium-brain
claude plugin install imperium-brain
```

All 18 skills activate automatically. No configuration needed.

**Try it:**
```
You: "Validate my startup idea: AI-powered vocal coaching"
You: "Research all competitors in the project management space"
You: "Write a viral LinkedIn post about our first 10 customers"
You: "Create a pitch deck carousel for our Series A"
You: "Build our brand identity — colors, fonts, and voice"

# Intelligent routing — it figures out what you ACTUALLY need:
You: "Write a data-driven LinkedIn post about our market"
  → Detects implicit research need, runs research first, then writes the post

You: "Create an on-brand carousel about competitors"
  → Detects brand + research prerequisites, chains: brand → research → carousel
```

---

## Architecture

```
imperium-brain/
│
├── SKILL.md                          # Hub router — routes to 18 skills
│
├── brand/                            # Shared brand system
│   ├── brand.json                    # Colors, fonts (user-generated)
│   ├── tone-of-voice.md             # Writing voice rules
│   └── templates/                    # 5 pre-built voice templates
│
├── skills/
│   ├── STARTUP OPS (9 skills, unchanged)
│   │   ├── ceo-advisor/             # Strategy, fundraising, board
│   │   ├── cto-advisor/             # Architecture, stack, scaling
│   │   ├── product-manager/         # PRDs, roadmap, RICE
│   │   ├── marketing/               # SEO, CRO, copy, email, growth
│   │   ├── sales-gtm/              # Cold email, 137 triggers, GTM
│   │   ├── finance/                 # SaaS metrics, runway, modeling
│   │   ├── founder/                 # Validation, interviews, mindset
│   │   ├── legal/                   # Contracts, entity, compliance
│   │   └── engineering-advanced/    # Agents, RAG, MCP, CI/CD
│   │
│   ├── RESEARCH & INTELLIGENCE (2 new)
│   │   ├── research/               # 9-phase competitive intelligence
│   │   └── api-discovery/          # Hidden API detection
│   │
│   └── CONTENT CREATION (7 new)
│       ├── brand-voice/            # Brand identity + tone
│       ├── linkedin/               # Viral posts, 12 types, 55+ hooks
│       ├── carousel/               # PPTX decks, 21 layouts
│       ├── visual-media/           # Image/video sourcing + AI review
│       ├── video/                  # Bridge to Remotion
│       ├── slides/                 # HTML presentations, 12 presets
│       └── sop/                    # SOPs, runbooks, playbooks
│
├── agents/                          # 8 sub-agents
├── commands/                        # 20 slash commands
├── evals/                           # 87 eval scenarios
│   ├── evals.json                   # Eval definitions
│   ├── eval-runner.py               # Automated eval runner
│   ├── metrics.md                   # Measurable metrics (4 tiers)
│   └── results/                     # Timestamped reports
├── templates/                       # 6 reusable templates
├── assets/                          # Frameworks + checklists
└── hooks/                           # Session start automation
```

---

## Intelligent Routing

The hub router doesn't just match keywords — it **understands intent**. A 5-step Prompt Analysis Protocol detects when your request implicitly needs multiple skills, even if you only asked for one.

**How it works:**

| Step | What it does |
|------|-------------|
| **1. Extract Explicit** | Direct keyword match against 18 skills. Single match + no signals = instant route (fast path) |
| **2. Detect Implicit** | Scans for data signals ("data-driven", "how we stack up"), brand signals ("on-brand", "our voice"), strategy signals ("should we", "moat"), temporal ("then", "after that"), and parallel ("across all channels") |
| **3. Check State** | Looks at filesystem — `brand/brand.json` exists? Research files present? Skips prerequisites you already have |
| **4. Resolve Deps** | Builds execution order: research → content, brand → content, research → strategy. Parallelizes where safe |
| **5. Confirm** | 1 skill = go. Explicit combo = brief plan. Inferred combo = asks you first. Ambiguous = clarifies |

**Examples:**

| You say | It detects | It does |
|---------|-----------|---------|
| "Write a LinkedIn post about AI" | linkedin (explicit) | Routes immediately — no extras needed |
| "Write a data-driven post about our market" | linkedin + research (implicit) | "I noticed you want data-driven content — should I research first?" |
| "Position ourselves uniquely" | ceo-advisor + research (implicit) | Runs research → feeds into strategic positioning |
| "Create content across all channels" | linkedin + carousel + slides (parallel) | Runs all three in parallel |

---

## Skills

### Startup Ops (9 skills)

| Domain | What It Does |
|--------|-------------|
| **CEO Advisor** | Strategy, fundraising, board management, stakeholder alignment |
| **CTO Advisor** | Architecture evaluation, stack selection, tech debt, build vs buy |
| **Product Manager** | PRDs, roadmap planning, RICE prioritization, discovery |
| **Marketing** | SEO, CRO, copywriting, email sequences, growth hacking |
| **Sales & GTM** | 34 cold email templates, 137 triggers, 11 GTM plays |
| **Finance** | SaaS metrics, financial modeling, runway analysis |
| **Founder** | Idea validation, competitor analysis, user interviews |
| **Legal** | Contracts, entity structure, compliance, IP |
| **Engineering** | Agent design, RAG, API design, CI/CD, MCP servers |

### Research & Intelligence (2 skills)

| Domain | What It Does |
|--------|-------------|
| **Research** | 9-phase competitive intelligence. Maps entire ecosystems, builds feature matrices, mines user sentiment, benchmarks pricing. Optional imperium-crawl integration for bulk scraping, YouTube/Reddit mining |
| **API Discovery** | Hidden API detection for SPAs. Discovers internal endpoints, authentication patterns, WebSocket connections. For competitive intelligence and integration research |

### Content Creation (7 skills)

| Domain | What It Does |
|--------|-------------|
| **Brand Voice** | Brand identity wizard — colors, fonts, visual system, tone-of-voice. Generates 4 brand files used by all content skills |
| **LinkedIn** | Viral post generator. 12 post types, 55+ hooks, algorithm 2025 rules, engagement psychology. Based on 121K+ impressions |
| **Carousel** | PPTX/PowerPoint creator. 6 carousel types, 21 Python layout scripts. LinkedIn carousels, pitch decks, reports |
| **Visual Media** | Image/video sourcing with AI-powered visual review. Searches free sources, downloads candidates, evaluates with Claude's multimodal vision |
| **Video** | Bridge to Remotion. 5 startup video templates (pitch, demo, social clip, investor update, hiring). Brand-integrated |
| **Slides** | HTML presentations. Self-contained file, zero dependencies, 12 style presets, keyboard navigation |
| **SOP** | Process document generator. SOPs, runbooks, playbooks, checklists, process maps with Mermaid diagrams |

---

## Slash Commands

### Startup Ops
| Command | What It Does |
|---------|-------------|
| `/imperium:validate-idea` | Comprehensive idea validation with scorecard |
| `/imperium:pitch-deck` | Complete pitch deck generation |
| `/imperium:fundraise-prep` | Full fundraising preparation |
| `/imperium:cold-email` | Personalized cold email campaigns |
| `/imperium:competitor-matrix` | Competitive analysis matrix |
| `/imperium:pricing-strategy` | Pricing strategy with tiers |
| `/imperium:gtm-plan` | Go-to-market plan |
| `/imperium:metrics-dashboard` | SaaS metrics calculation |
| `/imperium:founder-kb` | Semantic search over 2,019 knowledge chunks |

### Research & Intelligence
| Command | What It Does |
|---------|-------------|
| `/imperium:deep-research` | Full 9-phase competitive research |
| `/imperium:discover-apis` | Hidden API discovery for any website |
| `/imperium:crawl-check` | Check imperium-crawl installation |

### Content Creation
| Command | What It Does |
|---------|-------------|
| `/imperium:create-brand` | Brand identity wizard |
| `/imperium:linkedin-post` | LinkedIn viral post generator |
| `/imperium:carousel` | PPTX carousel/deck creation |
| `/imperium:create-video` | Video content (Remotion bridge) |
| `/imperium:create-slides` | HTML presentation slides |
| `/imperium:create-sop` | SOP/runbook/playbook generator |
| `/imperium:find-images` | Image/video sourcing with visual AI review |

### Eval & Quality
| Command | What It Does |
|---------|-------------|
| `/imperium:eval-loop` | Automated structural checks and quality analysis |

---

## Sub-Agents

| Agent | Role |
|-------|------|
| `ceo-strategist` | Strategic decisions, fundraising, board prep |
| `cto-architect` | Architecture, tech stack, scaling |
| `growth-marketer` | Marketing campaigns, SEO, content |
| `sales-hunter` | Outbound sales, pipeline, GTM |
| `product-analyst` | PRD reviews, prioritization, research |
| `market-researcher` | Deep competitive intelligence, ecosystem mapping |
| `content-creator` | LinkedIn, carousels, slides, SOPs, video |
| `brand-architect` | Brand identity creation, voice definition |

---

## Brand System

Create once, apply everywhere. Run `/imperium:create-brand` to generate:

- `brand/brand.json` — 10 colors, 3 fonts, asset paths
- `brand/config.json` — Output settings
- `brand/brand-system.md` — Design philosophy
- `brand/tone-of-voice.md` — Voice rules per platform

All content skills (LinkedIn, carousel, slides, SOP, video) automatically detect and apply your brand. No brand? Sensible defaults + suggestion to create one.

**5 pre-built templates:** tech-startup, enterprise-saas, consumer-app, developer-tools, creative-agency.

---

## External Tool Integration

### imperium-crawl (optional)

For deep research with bulk scraping, AI extraction, and YouTube/Reddit mining.

```bash
npm install -g imperium-crawl
```

The research skill uses a two-tier approach:
- **Tier 1 (always):** WebSearch + WebFetch for quick lookups
- **Tier 2 (if installed):** imperium-crawl for systematic, parallel research

Falls back gracefully if not installed.

### Remotion (optional)

For MP4 video creation. The video skill bridges to Remotion.

```bash
npx create-video@latest
```

Falls back to HTML slides or carousel if not available.

---

## Knowledge Base

10 startup books distilled into actionable frameworks:

- **Strategy** — Contrarian thinking, monopoly building, power law dynamics
- **Sales** — Tactical empathy, mirroring, calibrated questions
- **Offers** — Value equation, Grand Slam offers, guarantee stacking
- **Growth** — 19 traction channels, Bullseye framework
- **Positioning** — 5-step methodology, competitive alternatives
- **Lead Gen** — Warm/cold outreach, content-based, paid acquisition
- **Engagement** — Hook Model, habit zones, variable rewards
- **Validation** — Build-Measure-Learn, MVP archetypes, pivot criteria
- **Founder** — Grit, imposter syndrome, productivity systems

<details>
<summary><strong>Optional: Semantic Search (founder-kb CLI)</strong></summary>

```bash
bash skills/founder/scripts/setup_founder_kb.sh
founder-kb search "product-market fit frameworks"
```

Requires Python 3.10+ and ~2GB disk. The plugin works fully without this.

</details>

---

## Eval Coverage

**87 eval scenarios** across all 18 domains + negative tests + cross-domain workflows:

```
Startup Ops:     CEO (4) · CTO (4) · Product (4) · Marketing (3) · Sales (4)
                 Finance (4) · Founder (4) · Legal (3) · Engineering (3)

Research:        Ecosystem (1) · Deep (1) · Video Discovery (1) · Sentiment (1)
                 API Discovery SPA (1) · API Discovery GraphQL (1)

Content:         Brand Create (1) · Brand Voice (1) · Brand Update (1)
                 LinkedIn Story (1) · LinkedIn Contrarian (1) · LinkedIn Listicle (1)
                 LinkedIn Bilingual (1) · LinkedIn No Brand (1) · LinkedIn + Image (1)
                 Carousel LinkedIn (1) · Carousel Pitch (1) · Carousel No PPTX (1)
                 Carousel + Images (1)
                 Visual Media Standalone (1) · Visual Media + Carousel (1)
                 Visual Media + LinkedIn (1) · Visual Media Video (1)
                 Visual Media Brand Fit (1) · Visual Media Rejection (1)
                 Video Pitch (1) · Video Social (1) · Video No Remotion (1)
                 Video Investor (1)
                 Slides HTML (1) · Slides Branded (1) · Slides Dark (1)
                 SOP Onboarding (1) · SOP Runbook (1) · SOP Playbook (1)
                 SOP HTML (1)

Cross-Domain:    Research→LinkedIn (1) · Brand→Carousel (1) · Research→Carousel (1)
                 Brand→LinkedIn (1) · Research→Strategy (1) · Research→GTM (1)
                 Implicit Data (1) · Implicit Brand (1) · Full Pipeline (1)
                 Parallel Content (1)

Negative Tests:  Weather (1) · React (1) · Math (1) · Recipe (1)
                 Too Broad (1) · Git (1) · Python Debug (1) · Personal (1)
```

### Automated Eval Runner

```bash
python3 evals/eval-runner.py
```

Runs 17 structural checks across 2 tiers, generates a timestamped report in `evals/results/`. See `evals/metrics.md` for full metric definitions.

---

## Source Repositories

| Repository | Contribution |
|-----------|-------------|
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 180+ foundational skills |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 20+ marketing skills |
| [sachacoldiq/ColdIQ-s-GTM-Skills](https://github.com/sachacoldiq/ColdIQ-s-GTM-Skills) | Sales triggers & email templates |
| [emotixco/claude-skills-founder](https://github.com/emotixco/claude-skills-founder) | Founder workflows |
| [Digidai/product-manager-skills](https://github.com/Digidai/product-manager-skills) | PM frameworks |
| [alirezarezvani/claude-cto-team](https://github.com/alirezarezvani/claude-cto-team) | CTO skill suite |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | PM skills |

---

<div align="center">

## License

MIT — use it, fork it, build on it.

---

**Built by [Imperium Tech](https://github.com/ceoimperiumprojects) / Pavle Anđelković**

*Your AI co-founder is one install away.*

</div>
