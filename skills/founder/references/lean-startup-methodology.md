# Lean Startup Methodology

Build-Measure-Learn framework, validated learning, MVP types, and pivot signals. Distilled from Eric Ries' "The Lean Startup" and Steve Blank's customer development methodology.

## Core Philosophy

The fundamental activity of a startup is to turn ideas into products, measure customer response, and learn whether to pivot or persevere. Everything else is waste.

**Key insight:** The goal is NOT to build a product. It's to learn what product to build — the product customers will pay for.

## The Build-Measure-Learn Loop

```
        IDEAS
       ↗      ↘
   LEARN      BUILD
       ↖      ↙
      MEASURE
```

**Counter-intuitive:** Plan the loop BACKWARDS:
1. What do we need to LEARN? (hypothesis)
2. What do we need to MEASURE to learn it? (metric)
3. What's the minimum we need to BUILD to get that measurement? (MVP)

## Validated Learning

Not "we think" — "we tested and know."

**Validation levels (weakest to strongest):**

| Level | Evidence | Confidence |
|-------|----------|------------|
| Opinion | "I think customers want X" | Very Low |
| Survey | "60% said they'd use X" | Low |
| Landing page | "5% clicked 'Buy Now'" | Medium |
| Letter of Intent | "3 companies signed LOI" | Medium-High |
| Pre-sale | "12 people paid $49 before it existed" | High |
| Retention | "40% came back in week 2" | Very High |

**Rule:** Behavior > words. What people DO matters more than what they SAY.

## MVP Types

Choose the lightest MVP that tests your riskiest assumption:

| MVP Type | Time | Cost | Best For | Tests |
|----------|------|------|----------|-------|
| **Landing page** | 1 day | $0-100 | Value prop clarity | "Do people want this?" |
| **Explainer video** | 1-3 days | $0-500 | Complex products | "Do people understand this?" |
| **Concierge** | 1-2 weeks | $0 | Service businesses | "Can we deliver value?" |
| **Wizard of Oz** | 2-4 weeks | Low | Automation plays | "Would people use this if automated?" |
| **Pre-sales** | 1-2 weeks | $0 | B2B, high-ticket | "Will people pay for this?" |
| **Smoke test ads** | 3-5 days | $50-200 | Consumer apps | "Is there demand?" |
| **Fake door** | 1 day | $0 | Feature validation | "Do people click on this?" |
| **Single feature** | 2-6 weeks | Variable | Technical products | "Does the core mechanic work?" |
| **Piecemeal** | 1-2 weeks | Low | Marketplaces, tools | "Can we assemble this from existing tools?" |

**The right MVP = tests the riskiest assumption with the least effort.**

## Innovation Accounting

Traditional metrics (revenue, profit) are useless at early stage. Use innovation accounting instead:

**Step 1: Establish baseline**
- Build MVP, measure current state of key metrics
- Conversion rate, engagement, retention at day 0

**Step 2: Tune the engine**
- Run experiments to improve metrics toward the ideal
- Each experiment = a validated learning

**Step 3: Pivot or persevere**
- If experiments improve metrics → persevere, scale
- If metrics plateau despite experiments → pivot

**Actionable metrics vs vanity metrics:**

| Vanity (Ignore) | Actionable (Track) |
|------------------|--------------------|
| Total signups | Weekly active users |
| Page views | Activation rate |
| Downloads | Day 7 retention |
| "Registered users" | Paying customers |
| Social followers | Referral rate |

## Pivot Types

A pivot is a structured course correction to test a new hypothesis.

| Pivot Type | What Changes | Example |
|------------|-------------|---------|
| **Zoom-in** | Feature becomes the product | Flickr: game → photo sharing |
| **Zoom-out** | Product becomes a feature | Slack: game tool → comms platform |
| **Customer segment** | Different audience | YouTube: dating → all video |
| **Customer need** | Same customer, different problem | Starbucks: beans → café experience |
| **Platform** | App → platform or vice versa | — |
| **Business architecture** | B2C → B2B or vice versa | — |
| **Value capture** | Revenue model changes | Freemium → enterprise |
| **Engine of growth** | Viral → paid → sticky | — |
| **Channel** | Distribution method changes | Direct → retail |
| **Technology** | Same solution, new tech | — |

## Pivot Signals — When to Consider

**Red flags (consider pivoting):**
- Experiments consistently fail to move key metrics
- Customer conversations reveal a different, stronger problem
- Growth has flatlined despite 3+ months of effort
- You can articulate the problem but not who has it badly enough to pay
- Retention curve declines to zero (no one comes back)

**Green flags (keep going):**
- Each experiment teaches something actionable
- Retention curve flattens (some people stick)
- Organic growth emerging (word of mouth)
- Customers requesting features (they care enough to ask)
- LTV:CAC ratio improving

## Minimum Viable Experiment Template

```
Hypothesis: We believe [target customer] will [behavior]
            because [reason/insight].

Experiment: [What we'll build/do to test this]

Metric:     [What we'll measure]

Success:    [Specific threshold that validates hypothesis]
            e.g., ">5% conversion" or "3/10 interviewees mention X"

Duration:   [Maximum time: usually 1-2 weeks]

Cost:       [Maximum spend: usually <$200]

Decision:   If success → [next step]
            If failure → [pivot/kill/retest]
```

## The Five Whys (Root Cause Analysis)

When something goes wrong, ask "why" five times:

1. Why did the deploy break? → A test was missing
2. Why was the test missing? → Developer didn't write one
3. Why didn't they write one? → Rushing to meet deadline
4. Why were they rushing? → Scope wasn't cut
5. Why wasn't scope cut? → No clear MVP definition

**Root cause:** Process problem, not people problem. Fix the system.

## Lean Startup Anti-Patterns

- **"Stealth mode"** — Building in secret for months. You're not protecting an idea; you're avoiding feedback.
- **"Just one more feature"** — Infinite scope creep before any market contact.
- **"Our customers told us"** — Treating feature requests as strategy. Customers describe problems; you design solutions.
- **"We need more data"** — Analysis paralysis. The 70% rule: decide with 70% of desired info.
- **"Success theater"** — Celebrating vanity metrics (signups, downloads) while ignoring actionable ones (retention, revenue).
