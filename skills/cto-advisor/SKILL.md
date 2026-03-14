---
name: cto-advisor
description: 'Technical leadership for startup CTOs. Use when the user mentions architecture decisions, tech stack selection, build vs buy, tech debt management, team scaling, system design, infrastructure, security architecture, engineering process, code review standards, or any CTO-level technical decision. Also triggers on: CTO, technical architecture, microservices, monolith, database selection, API design, scaling, DevOps, CI/CD, engineering hiring, tech debt, code quality, system reliability, SRE, incident response.'
user-invocable: false
---

# CTO Advisor

Technical leadership frameworks for startup CTOs. Balance engineering excellence with business reality. Simple > clever. Boring technology wins.

## Keywords

CTO, chief technology officer, architecture, tech stack, build vs buy, tech debt, team scaling, system design, microservices, monolith, database, API design, scaling, DevOps, CI/CD, engineering hiring, infrastructure, security, code quality, SRE, incident response, performance, reliability

## Core Responsibilities

### 1. Architecture & System Design

**Architecture decision process:**
1. Define constraints (team size, budget, timeline, scale requirements)
2. List realistic options (what can this team actually build and maintain?)
3. Evaluate tradeoffs (performance, cost, complexity, hiring, vendor lock-in)
4. Document the decision (ADR — Architecture Decision Record)
5. Plan migration path (if changing existing system)

**Monolith vs Microservices decision tree:**
- Team < 10 engineers? → Monolith
- Single product? → Monolith
- Need independent deployment of components? → Consider microservices
- Can you afford the operational overhead? → If no, monolith
- Clear bounded contexts with different scaling needs? → Microservices make sense

**Database selection:**

| Need | Recommendation |
|------|----------------|
| General purpose, relational data | PostgreSQL |
| Document store, flexible schema | MongoDB |
| High-speed caching | Redis |
| Full-text search | Elasticsearch / Meilisearch |
| Time-series data | TimescaleDB / InfluxDB |
| Graph relationships | Neo4j |
| Simple key-value at scale | DynamoDB |
| Analytics/OLAP | ClickHouse / BigQuery |

**The default stack for startups:**
- Backend: Node.js/TypeScript or Python/FastAPI
- Frontend: React/Next.js or Vue/Nuxt
- Database: PostgreSQL + Redis
- Infrastructure: Railway, Render, or Vercel (avoid AWS complexity early)
- CI/CD: GitHub Actions
- Monitoring: Sentry + basic metrics

### 2. Tech Stack Selection

**Evaluation criteria:**

| Factor | Weight | Questions |
|--------|--------|-----------|
| Team capability | 30% | Can the team build and maintain this? |
| Hiring pool | 20% | Can we hire for this technology? |
| Maturity | 15% | Is this battle-tested or bleeding edge? |
| Performance | 15% | Does it meet our scale requirements? |
| Cost | 10% | Total cost of ownership? |
| Lock-in risk | 10% | How hard is it to switch later? |

**The "boring technology" rule:** Choose technology that's proven, well-documented, and has a large community. Save your innovation tokens for your product, not your infrastructure.

### 3. Build vs Buy Analysis

**Decision framework:**

| Factor | Build | Buy |
|--------|-------|-----|
| Core to your product? | Build if core differentiator | Buy if commodity |
| Team expertise? | Build if you have the skills | Buy if it's outside your domain |
| Time to market? | Build if no time pressure | Buy if speed matters |
| Customization needs? | Build if highly custom | Buy if standard works |
| Long-term cost? | Build if high volume makes it cheaper | Buy if low volume |
| Maintenance burden? | Build only if you can maintain it | Buy to offload maintenance |

**Rule of thumb:** If it's not your core product and someone else does it well, buy it. Your engineering time is your most expensive resource.

### 4. Tech Debt Management

**Tech debt categories:**
- **Deliberate-prudent:** "We know this is a shortcut, and we know how to fix it later"
- **Deliberate-reckless:** "We don't have time for good design" (danger zone)
- **Inadvertent-prudent:** "Now we know how we should have built it"
- **Inadvertent-reckless:** "What's architecture?" (fire the dev lead)

**Tech debt prioritization matrix:**

| Impact | High Frequency | Low Frequency |
|--------|---------------|---------------|
| **High Impact** | Fix NOW | Fix this quarter |
| **Low Impact** | Fix when touching that code | Probably never |

**The 20% rule:** Allocate 20% of engineering capacity to tech debt reduction. Non-negotiable. It compounds.

### 5. Team Scaling

**Engineering team structure (by stage):**

| Stage | Team Size | Structure |
|-------|-----------|-----------|
| Pre-seed | 1-3 | Everyone does everything |
| Seed | 3-8 | Full-stack generalists + 1 specialist |
| Series A | 8-20 | 2-3 squads, tech lead per squad |
| Series B | 20-50 | Engineering manager layer, platform team |
| Growth | 50+ | Multiple orgs, principal engineers, architects |

**Hiring priorities by stage:**
- **First 5:** Generalists who can ship fast
- **5-15:** First specialists (DevOps, security, data)
- **15-30:** First engineering managers, senior ICs
- **30+:** Platform team, architecture review board

**Engineering culture essentials:**
- PR review within 24 hours
- Deploy to production daily (or faster)
- Blameless post-mortems
- Document decisions (ADRs)
- Knowledge sharing (tech talks, pairing)

### 6. Security Architecture

**Security by stage:**

| Stage | Must Have | Nice to Have |
|-------|----------|-------------|
| Pre-seed | HTTPS, auth, input validation | Pen test |
| Seed | + secrets management, RBAC, backups | SOC 2 prep |
| Series A | + SOC 2, dependency scanning, incident response | Bug bounty |
| Series B+ | + SIEM, WAF, security team | ISO 27001 |

## CTO Metrics Dashboard

| Category | Metric | Target | Frequency |
|----------|--------|--------|-----------|
| Velocity | Deployment frequency | Daily+ | Weekly |
| Velocity | Lead time for changes | <1 day | Weekly |
| Quality | Change failure rate | <5% | Weekly |
| Quality | Mean time to recovery | <1 hour | Per incident |
| Health | Tech debt ratio | <20% of sprint | Monthly |
| Health | Test coverage | >80% critical paths | Monthly |
| Team | Engineering satisfaction | >7/10 | Quarterly |
| Cost | Infrastructure cost / ARR | <15% | Monthly |

## Red Flags

- Deployment takes more than 30 minutes
- No one understands a critical system (bus factor = 1)
- "We'll fix it later" is the most common phrase
- Engineers spend >30% of time on toil (manual processes)
- No monitoring/alerting on critical paths
- Production incidents happening weekly
- Tech stack chosen by resume-driven development

## Reference Files

- `references/architecture.md` — System design patterns, ADRs, scaling strategies
- `references/tech-debt.md` — Tech debt categorization, prioritization, reduction strategies
- `references/team-scaling.md` — Hiring, team structure, engineering culture
- `references/stack-selection.md` — Technology evaluation frameworks, default stacks
