---
name: sales-gtm
description: 'B2B sales and go-to-market execution. Use when the user mentions cold email, outbound sales, lead generation, sales triggers, prospecting, pipeline building, SDR, BDR, sales enablement, objection handling, demo scripts, battlecards, GTM strategy, sales sequences, email deliverability, or any B2B sales topic. Also triggers on: sales, outbound, inbound, cold call, follow-up, lead qualification, BANT, MEDDIC, ICP, buying signals, sales process, CRM, deal flow, quota, territory, account-based marketing, ABM, Clay, Apollo, sales automation, negotiation, tactical empathy, mirroring, labeling, calibrated questions, Never Split the Difference, offer creation, Grand Slam Offer, value equation, pricing psychology, guarantee stacking, $100M Offers, $100M Leads, warm outreach, cold outreach, lead magnets, content-led leads.'
user-invocable: false
---

# Sales & GTM

Complete B2B sales and go-to-market execution framework. From identifying triggers to closing deals. Includes 137 sales triggers, 34 cold email templates, and 11 GTM plays.

## Keywords

Sales, GTM, go-to-market, cold email, outbound, prospecting, pipeline, SDR, BDR, lead generation, sales triggers, buying signals, lead qualification, BANT, MEDDIC, objection handling, battlecards, demo scripts, sales sequences, email deliverability, CRM, deal flow, quota, ABM, Clay, Apollo, sales automation, ICP, cold call, follow-up

## Core Domains

### 1. Sales Triggers & Buying Signals

Sales triggers are events that create a window of opportunity. Don't cold email random people — target people experiencing a trigger that makes your solution relevant NOW.

**Trigger categories (137 total in reference file):**

| Category | Examples | Signal Strength |
|----------|----------|----------------|
| **Leadership changes** | New CXO, new VP, reorg | Very High |
| **Funding events** | Raised round, IPO filing, acquisition | Very High |
| **Hiring signals** | Job postings for roles your product replaces | High |
| **Tech stack changes** | Adopted/dropped competitor, new tools | High |
| **Growth signals** | Office expansion, new market entry, partnerships | Medium-High |
| **Pain signals** | Bad reviews, security incidents, layoffs | Medium |
| **Industry events** | Regulation changes, market shifts | Medium |
| **Content signals** | Blog posts about your problem space, conference talks | Medium |
| **Engagement signals** | Website visits, content downloads, social interactions | Variable |

See `references/sales-triggers.md` for the complete list of 137 triggers with response templates.

### 2. Cold Email

**The anatomy of a great cold email:**
1. **Subject line:** 3-5 words, lowercase, curiosity-driven
2. **Opening:** Personalized hook tied to a trigger (1 sentence)
3. **Problem:** Acknowledge their specific pain (1-2 sentences)
4. **Bridge:** How you help (1 sentence, not a feature dump)
5. **CTA:** One clear, low-friction ask (1 sentence)
6. **Total:** Under 100 words

**The 4-email sequence:**

| Email | Timing | Approach | Length |
|-------|--------|----------|--------|
| Initial outreach | Day 1 | Trigger + problem + CTA | <100 words |
| Follow-up | Day 3-4 | New angle + social proof | <80 words |
| Value-add | Day 7-8 | Share useful content + soft CTA | <80 words |
| Break-up | Day 14 | Direct close or graceful exit | <50 words |

**Key principles:**
- Personalization > templates (but templates are a starting point)
- Sell the meeting, not the product
- One CTA per email
- No attachments (kills deliverability)
- Don't start with "I" — start with them
- No buzzwords (leverage, synergy, innovative)
- Would YOU reply to this?

See `references/cold-email.md` for all 34 templates (23 first-touch, 4 follow-up, 4 re-engagement, 3 special).

### 3. GTM Plays

11 proven go-to-market plays for different scenarios.

| Play | When to Use | Key Metric |
|------|-------------|------------|
| **The New Exec** | Target within first 90 days | 8-12% reply rate |
| **The Funding Round** | Company just raised | 6-10% reply |
| **The Competitor Swap** | Using a competitor you can beat | 5-8% reply |
| **The Industry Event** | Around conferences/events | 4-7% reply |
| **The Content Engage** | Engaged with your content | 8-12% reply |
| **The Referral Play** | Warm intro available | 15-25% reply |
| **The Case Study Drop** | Similar company success story | 5-8% reply |
| **The ROI Calculator** | Quantifiable value prop | 4-7% reply |
| **The Free Audit** | Can diagnose their problem | 6-10% reply |
| **The Mutual Connection** | Shared network/background | 8-15% reply |
| **The Breaking News** | Industry/company news hook | 5-8% reply |

See `references/gtm-plays.md` for full playbook with templates and execution guides.

### 4. Lead Qualification

**BANT Framework:**
- **B**udget: Can they afford it?
- **A**uthority: Are they the decision maker?
- **N**eed: Do they have the problem?
- **T**imeline: When do they need a solution?

**MEDDIC Framework (for enterprise):**
- **M**etrics: What quantifiable goals are they trying to achieve?
- **E**conomic Buyer: Who controls the budget?
- **D**ecision Criteria: What are they evaluating on?
- **D**ecision Process: How do they buy?
- **I**dentify Pain: What hurts?
- **C**hampion: Who internally advocates for you?

**Lead scoring signals:**
- Visited pricing page (High intent)
- Downloaded content (Medium intent)
- Multiple visits in a week (High intent)
- Matches ICP firmographics (Baseline fit)
- Engaged with competitor content (Medium intent)

### 5. Sales Enablement

**Battlecard template:**
- When prospect mentions [Competitor]:
  - **Acknowledge:** What they're good at
  - **Differentiate:** Where you're different/better
  - **Prove:** Data, case studies, customer quotes
  - **Landmine:** Question that exposes competitor weakness

**Demo script structure:**
1. Discovery recap (2 min): Confirm their pain points
2. Vision (1 min): Paint the "after" picture
3. Demo (10-15 min): Show solution to their specific problems
4. Social proof (2 min): Similar customer success story
5. Next steps (2 min): Clear CTA with timeline

**Objection handling (LAER):**
- **L**isten: Let them finish, don't interrupt
- **A**cknowledge: Show you understand the concern
- **E**xplore: Ask questions to understand the root cause
- **R**espond: Address with evidence and confidence

### 6. Outbound Infrastructure

**Email deliverability checklist:**
- [ ] SPF, DKIM, DMARC records configured
- [ ] Dedicated sending domain (not your main domain)
- [ ] Domain warmed up (2-4 weeks, gradual volume increase)
- [ ] Email validation on all addresses before sending
- [ ] Sending limit: 50-100/day per mailbox
- [ ] Bounce rate <3%, spam complaint rate <0.1%

**Tech stack recommendations:**
- Prospecting: Apollo, LinkedIn Sales Navigator, Clay
- Sequencing: Instantly, Smartlead, Lemlist
- Enrichment: Clay, Clearbit, Apollo
- CRM: HubSpot (free tier), Pipedrive, Salesforce

## Sales Metrics

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| Reply rate | Replies / Emails sent | 5-15% (cold) |
| Positive reply rate | Positive / Total replies | 30-50% |
| Meeting booking rate | Meetings / Prospects contacted | 2-5% |
| Show rate | Attended / Booked | 70-85% |
| Demo → Close | Closed / Demos given | 15-30% |
| Sales cycle length | Days from first touch to close | Track by segment |
| Pipeline velocity | Pipeline $ × Win rate / Sales cycle | Increasing |

## Reference Files

- `references/cold-email.md` — 34 cold email templates with use cases
- `references/sales-triggers.md` — 137 sales triggers organized by category
- `references/gtm-plays.md` — 11 go-to-market plays with execution guides
- `references/lead-qualification.md` — BANT, MEDDIC, and scoring frameworks
- `references/sales-enablement.md` — Battlecards, demo scripts, objection handling
- `references/outbound-infrastructure.md` — Deliverability, tech stack, domain setup
- `references/negotiation-tactics.md` — Tactical empathy, calibrated questions, mirroring, labeling, Ackerman model (Source: Never Split the Difference)
- `references/offer-creation.md` — Value equation, Grand Slam offers, pricing psychology, guarantee stacking (Source: $100M Offers)
- `references/lead-generation-advanced.md` — 4 core lead gen methods, warm/cold frameworks, content-led leads, lead magnets (Source: $100M Leads)
