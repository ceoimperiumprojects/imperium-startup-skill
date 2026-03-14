# CI/CD Pipeline Architecture

## Pipeline Stages
```
Push → Lint → Test → Build → Security Scan → Deploy (Staging) → Deploy (Production)
```

## GitHub Actions Best Practices

### Workflow Structure
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm test

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run build

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - run: # deploy commands
```

### Key Practices
- Cache dependencies (saves 30-60% build time)
- Run independent jobs in parallel (lint + test)
- Pin action versions (`@v4`, not `@latest`)
- Use GitHub Secrets for credentials
- Reusable workflows for shared logic
- Matrix builds for multiple Node/Python versions

## Deployment Strategies

| Strategy | Downtime | Risk | Complexity | Best For |
|----------|----------|------|------------|----------|
| Direct | Possible | High | Low | Internal tools |
| Blue/Green | None | Low | Medium | Production APIs |
| Canary | None | Very Low | High | High-traffic apps |
| Feature Flags | None | Very Low | Medium | Gradual rollout |
| Rolling | None | Medium | Medium | Containerized apps |

### Blue/Green
- Two identical environments (blue = current, green = new)
- Deploy to green, test, switch traffic
- Rollback: Switch back to blue

### Canary
- Deploy to small % of traffic (5-10%)
- Monitor metrics (error rate, latency)
- Gradually increase if healthy
- Rollback: Route all traffic back to stable

### Feature Flags
- Deploy code to all users, but feature behind a flag
- Enable for internal → beta → 10% → 50% → 100%
- Rollback: Flip the flag

## Monitoring After Deploy

### What to Watch (First 30 minutes)
- Error rate (should not increase)
- Response time (P50, P95, P99)
- HTTP 5xx rate
- Memory/CPU usage
- Queue depth (if applicable)
- Key business metrics (signups, purchases)

### Rollback Triggers
- Error rate >2x normal
- P99 latency >3x normal
- Any critical functionality broken
- Data integrity issues
