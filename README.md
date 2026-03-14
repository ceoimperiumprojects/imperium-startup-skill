<div align="center">

# 🏛️ imperium-startup

### Your entire C-suite in one Claude Code plugin.

**9 Domain Skills** · **58 References** · **9 Slash Commands** · **5 Sub-Agents** · **10 Books Distilled**

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-blueviolet?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMkw0IDdWMTdMMTIgMjJMMjAgMTdWN0wxMiAyWiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+)](https://github.com/ceoimperiumprojects/imperium-startup-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-250+-orange?style=for-the-badge)]()

> CEO advisor, CTO architect, CMO, CFO, sales team, product manager, and legal counsel — all running inside your terminal. Built from **7 open-source repositories** and **10 distilled startup books** into one unified plugin.

</div>

---

## 🚀 Quick Start

```bash
# Install directly from GitHub
claude mcp add imperium-startup -- npx -y github:ceoimperiumprojects/imperium-startup-skill

# Or clone and install locally
git clone https://github.com/ceoimperiumprojects/imperium-startup-skill.git
cd imperium-startup-skill
claude plugin install .
```

That's it. All 9 skills activate automatically based on your prompts — no configuration needed.

**Try it instantly:**
```
You: "Validate my startup idea: AI-powered vocal coaching for amateur singers"
You: "Write a cold email to enterprise prospects for my SaaS product"
You: "Calculate our runway with €200K funding at €3K/month burn rate"
```

---

## ⚡ What You Get

<table>
<tr>
<td align="center"><strong>🧠 9</strong><br/>Domain Skills</td>
<td align="center"><strong>📎 58</strong><br/>Reference Files</td>
<td align="center"><strong>💬 9</strong><br/>Slash Commands</td>
<td align="center"><strong>🤖 5</strong><br/>Sub-Agents</td>
<td align="center"><strong>📚 10</strong><br/>Books Distilled</td>
<td align="center"><strong>🧪 23</strong><br/>Eval Scenarios</td>
</tr>
</table>

> **12,000+ lines** of startup knowledge, frameworks, templates, and actionable playbooks — zero external dependencies.

---

## 🧠 Domain Skills

Skills activate automatically when your prompt matches their domain. No prefixes, no setup.

| | Domain | What It Does |
|---|--------|-------------|
| 👔 | **CEO Advisor** | Strategy, fundraising, board management, stakeholder alignment, decision frameworks |
| 🔧 | **CTO Advisor** | Architecture evaluation, stack selection, tech debt management, build vs. buy analysis |
| 📋 | **Product Manager** | PRDs, roadmap planning, RICE prioritization, discovery, user stories |
| 📣 | **Marketing** | SEO, CRO, copywriting, email sequences, social media, growth hacking |
| 🎯 | **Sales & GTM** | 34 cold email templates, 137 sales triggers, 11 GTM plays, pipeline building |
| 💰 | **Finance** | SaaS metrics, financial modeling, runway analysis, investor reporting |
| 🧭 | **Founder** | Idea validation, competitor analysis, user interviews, MVP planning |
| ⚖️ | **Legal** | Contracts, entity structure, compliance, IP protection |
| ⚙️ | **Engineering** | Agent design, RAG architecture, API design, CI/CD, MCP servers |

---

## 💬 Slash Commands

| Command | What It Does |
|---------|-------------|
| `/imperium:validate-idea` | Run comprehensive idea validation with scorecard |
| `/imperium:pitch-deck` | Generate a complete pitch deck with all key slides |
| `/imperium:fundraise-prep` | Full fundraising preparation — terms, valuation, materials |
| `/imperium:cold-email` | Create personalized cold email campaigns |
| `/imperium:competitor-matrix` | Build detailed competitive analysis matrix |
| `/imperium:pricing-strategy` | Design pricing strategy with tiers and psychology |
| `/imperium:gtm-plan` | Create complete go-to-market plan |
| `/imperium:metrics-dashboard` | Calculate and analyze all key startup metrics |
| `/imperium:founder-kb` | Semantic search over 2,019 knowledge chunks |

---

## 🤖 Sub-Agents

Specialized agents you can invoke for focused, deep-dive work:

| Agent | Role | Best For |
|-------|------|----------|
| `ceo-strategist` | Strategic decision-making | Board prep, fundraising strategy, pivots |
| `cto-architect` | Technical architecture | System design, stack evaluation, scaling |
| `growth-marketer` | Marketing & growth | Campaigns, funnels, content strategy |
| `sales-hunter` | Outbound sales | Prospecting, pipeline, email sequences |
| `product-analyst` | Product analysis | PRD reviews, prioritization, user research |

---

## 📚 Knowledge Base

Distilled insights from 10 startup books, organized by domain. Every framework, tactic, and mental model — embedded directly into skills as reference files. **No book titles exposed, just pure actionable knowledge.**

### 🎯 Strategy & Monopoly Thinking
> Contrarian thinking, competition vs. monopoly, power law dynamics, secrets, definite optimism, 0-to-1 innovation frameworks

### 💰 Sales & Negotiation Tactics
> Tactical empathy, calibrated questions, mirroring & labeling, accusation audits, "no"-oriented questions, negotiation playbooks for founders

### 🔥 Offers & Pricing Psychology
> Value equation (Dream Outcome × Perceived Likelihood ÷ Time × Effort), Grand Slam offer creation, guarantee stacking, pricing psychology, bonus structures

### 📈 Growth & Traction Channels
> 19 traction channels, Bullseye framework for channel selection, traction testing methodology, scaling strategies per channel

### 🎯 Competitive Positioning
> 5-step positioning methodology, competitive alternatives analysis, best-fit customer identification, market category selection, positioning as strategy

### 🧲 Lead Generation Systems
> 4 core lead generation methods, warm outreach frameworks, cold outreach playbooks, content-based lead gen, paid acquisition strategies

### 🪝 Product Engagement & Habits
> Hook Model (Trigger → Action → Variable Reward → Investment), habit zone mapping, variable reward design, user engagement loops

### 🧪 Validation & Lean Methodology
> Build-Measure-Learn loops, validated learning, MVP archetypes, customer development 4-step model, earlyvangelists, pivot criteria

### 🧠 Founder Psychology & Resilience
> Grit and perseverance frameworks, imposter syndrome management, founder mental health, productivity systems, decision fatigue prevention

---

<details>
<summary>🔍 <strong>Optional: Semantic Search (founder-kb CLI)</strong></summary>

For deep search over all **2,019 chunks** with semantic matching:

```bash
# One-time setup
bash skills/founder/scripts/setup_founder_kb.sh

# Search
founder-kb search "how to validate a startup idea"
founder-kb search "pricing strategy" --source 100m-offers
founder-kb compare "customer interviews" --source1 lean-startup --source2 startup-owners-manual
```

Requires Python 3.10+ and ~2GB disk for embedding models. The plugin works fully without this — all key insights are already embedded as reference files.

</details>

---

## 🏗️ Architecture

```
imperium-startup/
├── 📄 .claude-plugin/plugin.json    # Plugin manifest
├── 🧠 skills/                       # 9 domain skills
│   ├── ceo-advisor/                 #   ├── skill.md + 7 references
│   ├── cto-advisor/                 #   ├── skill.md + 4 references
│   ├── product-manager/             #   ├── skill.md + 7 references
│   ├── marketing/                   #   ├── skill.md + 10 references
│   ├── sales-gtm/                   #   ├── skill.md + 9 references
│   ├── finance/                     #   ├── skill.md + 3 references
│   ├── founder/                     #   ├── skill.md + 10 references + KB scripts
│   ├── legal/                       #   ├── skill.md + 3 references
│   └── engineering-advanced/        #   └── skill.md + 5 references
├── 💬 commands/                     # 9 slash commands
├── 🤖 agents/                      # 5 sub-agents
├── 📝 templates/                   # 6 reusable templates
├── 📦 assets/                      # Frameworks + checklists
│   ├── frameworks/                  #   Lean Canvas, JTBD, Value Prop Canvas, Mom Test
│   └── checklists/                  #   Launch, fundraising, SEO checklists
├── 🧪 evals/                       # 23 eval scenarios
└── 🪝 hooks/                       # Session start automation
```

---

## 📦 Templates & Scripts

### Templates
| Template | Format | Purpose |
|----------|--------|---------|
| Pitch Deck | JSON | Complete slide-by-slide pitch deck structure |
| Investor Update | MD | Monthly investor communication template |
| PRD | MD | Product Requirements Document framework |
| GTM Plan | MD | Go-to-market strategy template |
| Competitive Matrix | MD | Side-by-side competitor analysis |
| Board Deck | MD | Board meeting presentation outline |

### Frameworks & Checklists
Lean Canvas, Mom Test Interview Guide, JTBD Framework, Value Proposition Canvas, Launch Checklist, Fundraising Checklist, SEO Checklist

### Python Scripts (stdlib only — no pip install needed)
| Script | What It Does |
|--------|-------------|
| `saas_metrics_calculator.py` | Calculate MRR, churn, LTV, CAC, and all key SaaS metrics |
| `financial_model.py` | Generate 18-month projections with bear/base/bull scenarios |
| `rice_prioritizer.py` | Score and rank features using the RICE framework |

---

## 🧪 Eval Coverage

The plugin includes **23 eval scenarios** covering all 9 domains with assertion-based testing:

```
✅ CEO Advisor     — fundraising, strategy, board prep
✅ CTO Advisor     — architecture evaluation, build vs buy
✅ Product Manager — PRD critique, RICE prioritization
✅ Marketing       — landing pages, SEO strategy, email sequences
✅ Sales & GTM     — cold email, pipeline building, negotiation, offers
✅ Finance         — SaaS metrics, runway modeling
✅ Founder         — idea validation, user interviews, mindset, KB search
✅ Legal           — entity structure
✅ Engineering     — agent architecture design
```

> Each scenario tests skill activation, reference file loading, and output quality assertions.

---

## 🙏 Source Repositories

This plugin synthesizes and builds upon content from these open-source projects:

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

## 📄 License

MIT — use it, fork it, build on it.

---

**Built by [Imperium Tech](https://github.com/ceoimperiumprojects) / Pavle Anđelković**

*Your AI co-founder is one install away.* 🚀

</div>
