# imperium-startup

Your entire C-suite, marketing team, sales force, and product org in one Claude Code plugin.

## What is this?

A unified Claude Code plugin combining **250+ skills** from **7 open-source repositories** into **9 domain skills**, **5 sub-agents**, **9 slash commands**, and a **10-book knowledge base**. Built for startup founders who need an AI co-founder, CMO, CTO, CFO, and sales team.

## Install

```bash
claude plugin install imperium-startup
```

Or clone and install locally:
```bash
git clone https://github.com/imperium-tech/imperium-startup-skill.git
cd imperium-startup-skill
claude plugin install .
```

## What's Included

### 9 Domain Skills (auto-triggered)

| Domain | What It Does |
|--------|-------------|
| **CEO Advisor** | Strategy, fundraising, board management, stakeholder alignment |
| **CTO Advisor** | Architecture, stack selection, tech debt, team scaling |
| **Product Manager** | PRDs, roadmap, prioritization, discovery, user stories |
| **Marketing** | SEO, CRO, copywriting, email, social, growth hacking |
| **Sales & GTM** | Cold email (34 templates), 137 sales triggers, 11 GTM plays |
| **Finance** | SaaS metrics, financial modeling, investor reporting |
| **Founder** | Idea validation, competitor analysis, user interviews, MVP |
| **Legal** | Contracts, entity structure, compliance, IP protection |
| **Engineering** | Agent design, RAG architecture, API design, CI/CD, MCP |

### 8 Slash Commands

| Command | Description |
|---------|-------------|
| `/imperium:validate-idea` | Run comprehensive idea validation |
| `/imperium:pitch-deck` | Generate a complete pitch deck |
| `/imperium:fundraise-prep` | Full fundraising preparation |
| `/imperium:cold-email` | Create personalized cold email campaigns |
| `/imperium:competitor-matrix` | Build competitive analysis |
| `/imperium:pricing-strategy` | Design pricing strategy and tiers |
| `/imperium:gtm-plan` | Create go-to-market plan |
| `/imperium:metrics-dashboard` | Calculate and analyze startup metrics |
| `/imperium:founder-kb` | Semantic search over 10 startup books (2,019 chunks) |

### 5 Sub-Agents

| Agent | Role |
|-------|------|
| `ceo-strategist` | Strategic decision-making and analysis |
| `cto-architect` | Technical architecture and design |
| `growth-marketer` | Marketing campaigns and optimization |
| `sales-hunter` | Outbound sales and pipeline building |
| `product-analyst` | Product analysis and management |

### Templates & Frameworks

- Pitch deck template
- Investor update template
- PRD template
- GTM plan template
- Competitive matrix template
- Board deck outline
- Lean Canvas, Mom Test, JTBD, Value Proposition Canvas
- Launch, fundraising, and SEO checklists

### Python Scripts (stdlib only)

- `saas_metrics_calculator.py` — Calculate all SaaS metrics from input data
- `financial_model.py` — Generate 18-month projections with bear/base/bull scenarios
- `rice_prioritizer.py` — Score and rank features using RICE framework

## Knowledge Base (10 Books)

Distilled insights from 10 startup books are embedded as reference files across all relevant skills. Key takeaways, frameworks, and actionable advice — no external dependencies needed.

| Book | Author | Key Contribution |
|------|--------|-----------------|
| The Lean Startup | Eric Ries | Build-Measure-Learn, validated learning, MVP types |
| The Startup Owner's Manual | Steve Blank | Customer development 4-step model, earlyvangelists |
| Never Split the Difference | Chris Voss | Tactical empathy, calibrated questions, negotiation |
| $100M Offers | Alex Hormozi | Value equation, Grand Slam offers, pricing psychology |
| $100M Leads | Alex Hormozi | 4 core lead gen methods, warm/cold frameworks |
| Zero to One | Peter Thiel | Contrarian thinking, monopoly strategy, power law |
| Hooked | Nir Eyal | Hook Model, variable rewards, habit-forming products |
| Traction | Weinberg & Mares | Bullseye framework, 19 traction channels |
| Obviously Awesome | April Dunford | 5-step positioning, competitive alternatives |
| Founder's Guide | Custom | Mindset, mental health, productivity, resilience |

### Optional: Full Semantic Search

For deep search over all 2,019 chunks with semantic matching:

```bash
# One-time setup
bash skills/founder/scripts/setup_founder_kb.sh

# Search
founder-kb search "how to validate a startup idea"
founder-kb search "pricing strategy" --source 100m-offers
founder-kb compare "customer interviews" --source1 lean-startup --source2 startup-owners-manual
```

Requires Python 3.10+ and ~2GB disk for embedding models. Plugin works fully without this — reference files contain all key insights.

## Source Repositories

This plugin synthesizes content from:

1. [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) — 180+ skills
2. [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) — 20+ marketing skills
3. [sachacoldiq/ColdIQ-s-GTM-Skills](https://github.com/sachacoldiq/ColdIQ-s-GTM-Skills) — Sales triggers & templates
4. [emotixco/claude-skills-founder](https://github.com/emotixco/claude-skills-founder) — Founder workflows
5. [Digidai/product-manager-skills](https://github.com/Digidai/product-manager-skills) — PM frameworks
6. [alirezarezvani/claude-cto-team](https://github.com/alirezarezvani/claude-cto-team) — CTO skill suite
7. [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) — PM skills

## License

MIT

## Author

Imperium Tech / Pavle Anđelković
