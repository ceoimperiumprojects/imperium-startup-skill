# Agent Design Patterns

## Architecture Patterns

### Single Agent + Tools
- One agent with access to multiple tools
- Simple, predictable, easy to debug
- Best for: Focused tasks with clear workflow
- Example: Code review agent with file read + lint + test tools

### Agent with Sub-Agents
- Main agent delegates to specialized sub-agents
- Each sub-agent has its own tools and context
- Best for: Complex tasks requiring domain expertise
- Example: Research agent spawning search + analysis sub-agents

### Agent Team (Orchestrator)
- Orchestrator agent manages multiple parallel agents
- Agents work independently, results aggregated
- Best for: Multi-domain analysis, parallel work
- Example: Startup advisor with CEO, CTO, CFO agents working together

### Agent Swarm
- Autonomous agents that discover and create work
- Self-organizing, emergent behavior
- Best for: Open-ended exploration, research
- Highest complexity, hardest to control

## Agent Design Principles

### Prompt Design
- Clear role definition ("You are a...")
- Specific capabilities and limitations
- Structured output format
- Examples of good outputs
- Error handling instructions

### Tool Design
- One tool, one job (Single Responsibility)
- Clear input/output schemas
- Descriptive names and descriptions
- Handle errors gracefully
- Return structured data, not prose

### Guardrails
- Content filters (prevent harmful outputs)
- Action limits (max API calls, max file changes)
- Human-in-the-loop for destructive actions
- Budget limits (token/cost caps)
- Timeout handling

## Evaluation Framework

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| Task completion rate | Does it finish the job? | >90% |
| Output quality | Is the result good? | Human eval score >4/5 |
| Token efficiency | How many tokens per task? | Decreasing over iterations |
| Tool call efficiency | Unnecessary tool calls? | Minimal wasted calls |
| Error recovery rate | Does it handle errors well? | >80% self-recovery |
| Latency | How long per task? | Acceptable for use case |

## Common Pitfalls
- Agent loops (calling the same tool repeatedly)
- Context window overflow (too much data loaded)
- Tool misuse (using wrong tool for the task)
- Hallucination in tool parameters
- Missing error handling for API failures
- Over-reliance on single LLM call (no verification)
