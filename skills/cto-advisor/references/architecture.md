# Architecture Patterns

## Architecture Decision Records (ADRs)

### ADR Template
```
# ADR-[NUMBER]: [Title]

## Status
Proposed / Accepted / Deprecated / Superseded

## Context
What is the issue? What forces are at play?

## Decision
What is the change being proposed?

## Consequences
What becomes easier? What becomes harder?
What are the risks? What's the migration path?
```

### When to Write an ADR
- Choosing a new technology or framework
- Changing database or storage approach
- Redesigning a major component
- Adding a new service or splitting a monolith
- Any decision that's hard to reverse

## Scaling Strategies

### Vertical Scaling (Scale Up)
- Bigger machine (more CPU, RAM)
- Simpler to implement
- Has a ceiling
- Best for: Early stage, databases, simple apps

### Horizontal Scaling (Scale Out)
- More machines
- Requires stateless design
- Theoretically unlimited
- Best for: Web servers, microservices, read-heavy workloads

### Scaling Playbook by Stage

| Users | Strategy | Focus |
|-------|----------|-------|
| 0-1K | Single server, vertical scale | Ship fast, don't over-engineer |
| 1K-10K | Add caching (Redis), CDN, optimize queries | Performance basics |
| 10K-100K | Read replicas, load balancer, async jobs | Separate read/write paths |
| 100K-1M | Service extraction, message queues, search index | Bounded contexts |
| 1M+ | Full microservices, global CDN, data pipeline | Organizational scaling |

## Common Architecture Patterns

### Monolith (Start Here)
- Single deployable unit
- Shared database
- Simple to develop, test, deploy
- Best for: Teams < 10, single product, early stage

### Modular Monolith
- Single deployment, but code organized into modules
- Clear boundaries between modules
- Can extract to microservices later
- Best for: Growing teams, pre-extraction

### Microservices
- Independent services, own databases
- Independent deployment and scaling
- High operational overhead
- Best for: Large teams, multiple products, different scaling needs

### Event-Driven
- Services communicate via events (not direct calls)
- Loose coupling, high resilience
- Eventually consistent
- Best for: Complex workflows, audit requirements, multi-step processes

## Database Patterns

### CQRS (Command Query Responsibility Segregation)
- Separate read and write models
- Optimize each independently
- Adds complexity but improves performance at scale

### Event Sourcing
- Store events, not state
- Rebuild state by replaying events
- Perfect audit trail
- Complex but powerful for financial/compliance systems

### Sharding
- Split data across multiple databases
- Choose shard key carefully (hard to change)
- Common: by tenant, by geography, by ID range
