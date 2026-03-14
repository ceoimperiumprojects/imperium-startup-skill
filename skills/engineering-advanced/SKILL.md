---
name: engineering-advanced
description: 'Advanced engineering patterns for AI-native products. Use when the user mentions agent design, RAG architecture, AI pipelines, MCP servers, API design best practices, CI/CD pipeline architecture, system design interviews, observability, infrastructure as code, or advanced engineering topics. Also triggers on: agent, RAG, retrieval augmented generation, MCP, API design, REST, GraphQL, CI/CD, GitHub Actions, Docker, Kubernetes, microservices architecture, event-driven, message queues, caching strategies, database design, system design.'
user-invocable: false
---

# Engineering Advanced

Advanced engineering patterns for AI-native startups building agents, RAG systems, APIs, and scalable infrastructure.

## Keywords

Agent design, RAG, retrieval augmented generation, MCP, API design, REST, GraphQL, CI/CD, GitHub Actions, Docker, Kubernetes, microservices, event-driven, message queues, caching, database design, system design, observability, infrastructure as code, AI pipeline

## Core Domains

### 1. Agent Design

**Agent architecture patterns:**

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| Single agent + tools | Simple tasks, clear workflow | Low |
| Agent with sub-agents | Complex tasks, domain separation | Medium |
| Agent team (orchestrator) | Multi-domain, parallel work | High |
| Agent swarm | Autonomous exploration, research | Very High |

**Agent design principles:**
- Give agents clear, specific instructions (not vague goals)
- Define tool boundaries (what the agent CAN and CANNOT do)
- Implement guardrails (content filters, action limits, human-in-the-loop)
- Design for failure (retry logic, fallback paths, error handling)
- Observe everything (log prompts, responses, tool calls, latency)

**Agent evaluation:**
- Task completion rate
- Average tokens per task
- Tool call efficiency (fewer calls = better)
- Error rate and recovery success
- User satisfaction / output quality

### 2. RAG Architecture

**RAG pipeline components:**

```
Documents → Chunking → Embedding → Vector Store → Retrieval → Generation
```

**Chunking strategies:**

| Strategy | Best For | Chunk Size |
|----------|----------|------------|
| Fixed-size | Simple docs, consistent structure | 256-512 tokens |
| Semantic | Complex docs, mixed content | Variable |
| Recursive | Hierarchical content | Parent + child |
| Document-level | Short docs, complete context needed | Full document |

**Retrieval optimization:**
- Hybrid search: Vector similarity + keyword (BM25)
- Re-ranking: Cross-encoder after initial retrieval
- Metadata filtering: Pre-filter by date, source, category
- Query expansion: Generate multiple query variations
- Contextual compression: Summarize retrieved chunks

**Vector databases:**

| Database | Self-hosted | Cloud | Best For |
|----------|------------|-------|----------|
| pgvector | Yes | Supabase, Neon | Already using PostgreSQL |
| Pinecone | No | Yes | Managed, serverless |
| Weaviate | Yes | Yes | Multi-modal, hybrid search |
| Qdrant | Yes | Yes | Performance, filtering |
| ChromaDB | Yes | No | Prototyping, local dev |

**RAG quality metrics:**
- Retrieval precision: % of retrieved chunks that are relevant
- Retrieval recall: % of relevant chunks that are retrieved
- Faithfulness: Does the answer match the retrieved context?
- Answer relevancy: Does the answer address the question?

### 3. API Design

**REST API design rules:**
- Use nouns for resources (`/users`, not `/getUsers`)
- HTTP methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE
- Consistent naming: `snake_case` for JSON, plural nouns for collections
- Pagination: Cursor-based for real-time data, offset for static
- Versioning: URL path (`/v1/`) preferred over headers
- Error responses: Consistent format with error code, message, details

**API response format:**
```json
{
  "data": { ... },
  "meta": { "page": 1, "total": 100 },
  "errors": null
}
```

**Error response format:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [{ "field": "email", "issue": "missing" }]
  }
}
```

**Rate limiting:**
- Return `429 Too Many Requests` with `Retry-After` header
- Implement per-user and per-IP limits
- Use sliding window algorithm
- Document limits clearly in API docs

### 4. CI/CD Pipeline Architecture

**Pipeline stages:**
```
Push → Lint → Test → Build → Security Scan → Deploy (Staging) → Deploy (Production)
```

**GitHub Actions best practices:**
- Cache dependencies (node_modules, pip cache)
- Run tests in parallel where possible
- Use matrix builds for multiple environments
- Pin action versions (don't use `@latest`)
- Store secrets in GitHub Secrets, not in code
- Keep workflows DRY with reusable workflows

**Deployment strategies:**

| Strategy | Risk | Complexity | Best For |
|----------|------|------------|----------|
| Direct deploy | High | Low | Internal tools, early stage |
| Blue/Green | Low | Medium | Zero-downtime deploys |
| Canary | Low | High | High-traffic production |
| Feature flags | Very Low | Medium | Gradual rollout |

### 5. MCP Server Building

**MCP (Model Context Protocol) server structure:**
- Define tools with clear names and descriptions
- Input schemas using JSON Schema
- Handle errors gracefully with informative messages
- Implement authentication if accessing external services
- Test with Claude Code or Claude Desktop

**MCP tool design principles:**
- One tool, one job (Single Responsibility)
- Clear parameter names and descriptions
- Return structured data (JSON), not prose
- Include examples in tool descriptions
- Handle edge cases (empty results, timeout, rate limits)

### 6. Observability

**Three pillars:**
1. **Logs:** Structured (JSON), with correlation IDs, appropriate levels
2. **Metrics:** Business metrics (conversions, revenue), technical metrics (latency, error rate)
3. **Traces:** Distributed tracing across services (OpenTelemetry)

**Essential alerts:**
- Error rate > X% for Y minutes
- P99 latency > Xms
- CPU/Memory > 80% sustained
- Queue depth growing
- 5xx responses from dependencies

**Tool recommendations:**
- Logging: Structured logging → Datadog, Grafana Loki, CloudWatch
- Metrics: Prometheus + Grafana, Datadog
- Tracing: OpenTelemetry → Jaeger, Datadog
- Error tracking: Sentry
- Uptime: Betteruptime, Checkly

## Reference Files

- `references/agent-design.md` — Agent architecture, evaluation, prompt engineering
- `references/rag-architecture.md` — RAG pipeline design, chunking, retrieval optimization
- `references/api-design.md` — REST/GraphQL patterns, versioning, error handling
- `references/cicd.md` — Pipeline architecture, deployment strategies, GitHub Actions
- `references/mcp-builder.md` — MCP server development, tool design, testing
