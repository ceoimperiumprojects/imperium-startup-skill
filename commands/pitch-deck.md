---
name: imperium:pitch-deck
description: Generate a complete pitch deck outline with slide-by-slide content, speaker notes, and investor-ready narrative. Customized to your startup's stage and target investors.
user-invocable: true
---

# Pitch Deck Generator

You are building a pitch deck using the Imperium Startup framework. Create a compelling investor narrative.

## Information Gathering

Ask the user for (skip any they've already provided):
1. Company name and one-line description
2. Problem you're solving (and for whom)
3. Your solution (how it works)
4. Current traction (users, revenue, LOIs, pilots — anything)
5. Business model (how you make money)
6. Amount raising and use of funds
7. Team background (relevant experience)
8. Key competitors

## Deck Creation

Reference the template at `templates/pitch-deck-template.json` for structure.

For each of the 12 slides, generate:

### Slide Content
- **Headline**: Bold, memorable statement (not just the slide name)
- **Key points**: 3-5 bullet points max
- **Visual suggestion**: What graphic/chart/image would work here
- **Speaker notes**: What to say (30-60 seconds per slide)

### Narrative Arc

Build the story in this order:
1. **Hook** (Problem): Make them feel the pain
2. **Relief** (Solution): Show the way out
3. **Proof** (Traction): Show it's working
4. **Scale** (Market): Show the opportunity is big
5. **Edge** (Moat): Show why you win
6. **Team** (People): Show you can execute
7. **Ask** (Investment): Show the path forward

## Stage-Specific Adjustments

### Pre-Seed / Seed
- Lead with problem and team
- Traction can be pre-revenue (waitlist, interviews, LOIs)
- Financial projections less important than market insight
- Show velocity of learning

### Series A
- Lead with traction and metrics
- Show product-market fit evidence
- Clear unit economics
- Detailed go-to-market

### Series B+
- Lead with metrics and growth
- Show scalability and efficiency
- Market expansion plan
- Path to profitability

## Output Format

Deliver as a structured markdown document with:
1. Deck overview (target audience, stage, ask)
2. Slide-by-slide content with headlines, bullets, visuals, and notes
3. Appendix slide suggestions
4. Common Q&A preparation (top 10 investor questions with answers)
5. Tips for delivery
