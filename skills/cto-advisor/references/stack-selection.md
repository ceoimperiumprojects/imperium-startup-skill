# Tech Stack Selection

## Evaluation Framework

| Factor | Weight | Questions |
|--------|--------|-----------|
| Team capability | 30% | Can we build and maintain this? |
| Hiring pool | 20% | Can we hire for this technology? |
| Maturity | 15% | Is it battle-tested? Good docs? Active community? |
| Performance | 15% | Does it meet our scaling needs? |
| Cost | 10% | Total cost of ownership (licenses, hosting, maintenance)? |
| Lock-in risk | 10% | How hard is it to switch later? |

## Default Stacks (Recommended)

### The "Ship Fast" Stack (Pre-seed to Seed)
- **Backend:** Node.js + TypeScript (or Python + FastAPI)
- **Frontend:** Next.js (React) or Nuxt (Vue)
- **Database:** PostgreSQL + Redis
- **Auth:** Clerk, Auth0, or Supabase Auth
- **Hosting:** Vercel (frontend) + Railway/Render (backend)
- **CI/CD:** GitHub Actions
- **Monitoring:** Sentry + Vercel Analytics

### The "Scale" Stack (Series A+)
- **Backend:** Node.js/TypeScript or Go (high-perf services)
- **Frontend:** Next.js + React
- **Database:** PostgreSQL + Redis + Elasticsearch (search)
- **Queue:** BullMQ (Redis-based) or RabbitMQ
- **Hosting:** AWS (ECS or EKS) or GCP (Cloud Run)
- **CI/CD:** GitHub Actions + ArgoCD
- **Monitoring:** Datadog or Grafana Cloud
- **Feature Flags:** LaunchDarkly or Unleash

### The "AI-Native" Stack
- **LLM:** Claude API (Anthropic) or OpenAI
- **Vector DB:** pgvector (if using PG), Pinecone, or Qdrant
- **Embedding:** Voyage AI or OpenAI embeddings
- **Orchestration:** LangChain, LlamaIndex, or direct API calls
- **Agent Framework:** Claude Agent SDK or CrewAI
- **MCP:** Claude Code MCP servers

## Build vs Buy Decision Matrix

| Factor | Build | Buy |
|--------|-------|-----|
| Core to product? | Build | Buy |
| Team expertise? | Build | Buy |
| Time pressure? | Buy | Buy |
| Custom needs? | Build | Buy |
| Long-term cost? | Build (at scale) | Buy (at low scale) |
| Maintenance? | Build (if team can sustain) | Buy (offload) |

**Rule of thumb:** Build your core product. Buy everything else.

## Technology Radar

### Adopt (Safe to Use)
PostgreSQL, Redis, TypeScript, React, Next.js, Docker, GitHub Actions, Sentry

### Trial (Worth Experimenting)
Bun, Drizzle ORM, tRPC, Turborepo, Claude Agent SDK, Playwright

### Assess (Watch But Don't Commit)
Deno 2, HTMX, Effect-TS, Tauri

### Hold (Avoid for New Projects)
jQuery, Express (use Fastify/Hono), Webpack (use Vite), Heroku (use Railway/Render)
