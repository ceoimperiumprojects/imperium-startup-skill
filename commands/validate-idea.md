---
name: imperium:validate-idea
description: Run a comprehensive startup idea validation. Analyzes problem-solution fit, market size, competition, and creates a validation plan with Mom Test interview questions.
user-invocable: true
---

# Idea Validation Workflow

You are running the Imperium Startup idea validation framework. Guide the user through a structured validation process.

## Step 1: Capture the Idea

Ask the user to describe their startup idea. If they haven't provided details, ask:
- What problem are you solving?
- Who has this problem?
- How do they solve it today?

## Step 2: Problem Validation Assessment

Evaluate the idea across these dimensions:

### Problem Score (1-10)
- **Frequency**: How often does the target user face this problem?
- **Intensity**: How painful is this problem?
- **Willingness to pay**: Are people already spending money on alternatives?
- **Growing market**: Is this problem getting worse/more common?

### Solution Score (1-10)
- **10x better**: Is this meaningfully better than alternatives?
- **Feasibility**: Can this be built with available resources?
- **Defensibility**: Can competitors easily copy this?
- **Scalability**: Can this grow without proportional cost increase?

### Founder-Market Fit (1-10)
- **Domain expertise**: Does the founder understand this market?
- **Network**: Does the founder have access to target customers?
- **Passion**: Will the founder persist through the hard times?
- **Unfair advantage**: What does the founder have that others don't?

## Step 3: Market Sizing

Calculate TAM/SAM/SOM using bottom-up methodology:
- **TAM**: Total number of potential users × average revenue per user
- **SAM**: Subset you can realistically serve (geography, segment)
- **SOM**: What you can capture in Year 1 (be conservative)

## Step 4: Competitive Landscape

Identify:
- Direct competitors (solving the same problem)
- Indirect competitors (different solution to same problem)
- Potential future competitors (big companies that could enter)
- Your differentiation (why you win)

## Step 5: Validation Plan

Create a concrete 2-week validation plan:

### Week 1: Customer Discovery
Generate 10 Mom Test interview questions specific to this idea.
Reference: `assets/frameworks/mom-test-cheatsheet.md`

### Week 2: Market Validation
- [ ] Talk to 10 potential customers
- [ ] Identify 3 common pain points
- [ ] Test willingness to pay
- [ ] Build a landing page to test demand
- [ ] Run a small ad test ($50-100)

## Step 6: Go/No-Go Recommendation

Based on the scores, provide a clear recommendation:
- **GREEN LIGHT** (Score > 7 average): Strong idea, proceed to MVP
- **YELLOW LIGHT** (Score 5-7): Promising but needs more validation
- **RED LIGHT** (Score < 5): Fundamental concerns, pivot or pass

## Output Format

Present results as a structured report with:
1. Idea summary (1 paragraph)
2. Scores table with commentary
3. Market size estimates
4. Competitive landscape map
5. Top 3 risks and mitigations
6. 10 Mom Test questions
7. 2-week validation plan
8. Clear go/no-go recommendation
