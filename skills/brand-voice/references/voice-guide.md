# Brand Voice Reference Guide

A practical guide to understanding different brand voices, with real examples showing how the same message transforms depending on voice settings. Use this as a reference when crafting content or calibrating your brand's tone.

---

## The Five Voice Archetypes

### 1. Professional Voice

**Best for:** Enterprise SaaS, fintech, legal tech, healthcare platforms
**Spectrum settings:** Formal 3 | Technical 4 | Serious 3 | Reserved 4
**Archetype pairing:** Sage, Ruler, Caregiver

**Characteristics:**
- Third person or inclusive "we" — rarely "I"
- Complete sentences, proper grammar, no contractions
- Data-driven claims with sources
- Measured confidence — states facts, avoids superlatives
- Industry terminology used appropriately

**Sample copy:**

> **Tagline:** Enterprise-grade security your team can trust.
>
> **Landing page hero:** Reduce compliance risk by 73% with automated policy enforcement. Our platform monitors, flags, and resolves security gaps before they become incidents.
>
> **Email subject:** Your Q3 compliance report is ready
>
> **Tweet:** Organizations using automated compliance monitoring report 73% fewer security incidents. Manual processes can't keep up with modern threat landscapes.
>
> **Error message:** We were unable to process your request. Our team has been notified and is investigating. Please try again in a few minutes, or contact support for immediate assistance.

---

### 2. Startup-Casual Voice

**Best for:** B2B SaaS startups, productivity tools, team collaboration
**Spectrum settings:** Formal 7 | Technical 5 | Serious 6 | Reserved 7
**Archetype pairing:** Innovator, Explorer, Creator

**Characteristics:**
- First person plural "we" and direct "you"
- Contractions are the default
- Short paragraphs, white space, scannable
- Confident claims backed by specifics
- Occasional personality — a metaphor here, a dash of humor there

**Sample copy:**

> **Tagline:** Ship faster. Sleep better.
>
> **Landing page hero:** Your deploy pipeline shouldn't feel like defusing a bomb. We built the deployment platform we wished existed — zero-downtime releases, automatic rollbacks, and logs that actually make sense. Start deploying in 5 minutes.
>
> **Email subject:** You just saved 3 hours this week
>
> **Tweet:** We just shipped instant rollbacks. Push bad code on Friday at 5pm? (Don't.) But if you do, you're covered. One click, you're back. No sweat.
>
> **Error message:** Something went sideways. We're on it — usually fixed in under 2 minutes. Grab some coffee and try again shortly.

---

### 3. Technical Voice

**Best for:** Developer tools, APIs, infrastructure, open-source projects
**Spectrum settings:** Formal 5 | Technical 2 | Serious 4 | Reserved 5
**Archetype pairing:** Sage, Creator, Innovator

**Characteristics:**
- Assumes technical knowledge — no hand-holding
- Code examples over prose when possible
- Direct, concise — respects the reader's time
- No marketing fluff — substance over sizzle
- Precise terminology — "latency" not "speed," "throughput" not "performance"

**Sample copy:**

> **Tagline:** The database for developers who read the docs.
>
> **Landing page hero:** Sub-millisecond reads. Automatic sharding. Native TypeScript SDK. Built on a log-structured merge-tree with MVCC, so your reads never block your writes. `npm install @acme/db` and query in 30 seconds.
>
> **Email subject:** v2.4: Streaming queries + 40% faster cold starts
>
> **Tweet:** Just shipped streaming queries. Subscribe to a query, get real-time updates over WebSocket. No polling. No webhooks. Just `db.subscribe(query, callback)`. Docs: [link]
>
> **Error message:** `ConnectionError: Unable to reach cluster endpoint us-east-1.db.acme.io:5432`. Check your network configuration and ensure the cluster is running. [Troubleshooting guide →]

---

### 4. Friendly Voice

**Best for:** Consumer apps, edtech, wellness, community platforms
**Spectrum settings:** Formal 8 | Technical 8 | Serious 7 | Reserved 6
**Archetype pairing:** Caregiver, Everyman, Jester

**Characteristics:**
- Warm, encouraging, supportive
- Simple language — 6th to 8th grade reading level
- Uses "you" constantly — it's about the user
- Celebrates user achievements
- Gentle with errors — never blames the user
- Emojis and casual punctuation acceptable

**Sample copy:**

> **Tagline:** Learning that fits your life.
>
> **Landing page hero:** You've got 15 minutes between meetings? That's enough to learn something new. Bite-sized lessons, zero homework, and a streak system that actually makes you want to come back. Join 2M+ people who learn a little every day.
>
> **Email subject:** You're on a 7-day streak — keep it going!
>
> **Tweet:** POV: You just finished your morning lesson in the time it took your coffee to brew. That's 7 days in a row. You're kind of amazing.
>
> **Error message:** Oops, that didn't work! No worries — your progress is saved. Let's try that again.

---

### 5. Authoritative Voice

**Best for:** Research platforms, consulting, financial services, B2B enterprise
**Spectrum settings:** Formal 2 | Technical 3 | Serious 2 | Reserved 3
**Archetype pairing:** Ruler, Sage, Hero

**Characteristics:**
- Speaks from a position of deep expertise
- Makes definitive statements — not "we think" but "the data shows"
- Uses research, frameworks, and data as evidence
- Longer-form content with structured arguments
- Avoids hedging — confident without being arrogant
- Formal but not stiff — authority with warmth

**Sample copy:**

> **Tagline:** The intelligence platform for strategic decisions.
>
> **Landing page hero:** Market-moving decisions require market-moving data. Our platform synthesizes 40,000+ data sources into actionable intelligence, delivering the insights that Fortune 500 strategy teams depend on. Because in competitive markets, the best-informed team wins.
>
> **Email subject:** Market Intelligence Brief: Q3 Sector Analysis
>
> **Tweet:** Companies that adopt data-driven decision frameworks outperform peers by 2.3x on average (McKinsey, 2024). The question isn't whether to invest in intelligence infrastructure — it's how quickly you can operationalize it.
>
> **Error message:** We encountered an issue processing your analysis. Your data remains secure and your previous results are available. Our engineering team has been alerted and will resolve this promptly.

---

## Before / After Transformations

These examples show how the same raw message transforms when filtered through different brand voices. Use these as calibration references.

### Message: Announcing a new feature

**Raw message:** We added a dashboard that shows your metrics in real time.

| Voice | Transformed |
|-------|-------------|
| **Professional** | We are pleased to introduce our new real-time analytics dashboard, providing stakeholders with instant visibility into key performance metrics. |
| **Startup-Casual** | Your metrics, live. We just shipped a real-time dashboard so you can see exactly what's happening — right now, not yesterday. |
| **Technical** | New: Real-time metrics dashboard. WebSocket-powered, <100ms latency, supports custom queries. `GET /api/v2/metrics/stream` |
| **Friendly** | Guess what? You can now see all your stats updating in real time! No more refreshing. Just open your dashboard and watch the magic happen. |
| **Authoritative** | Our new real-time analytics dashboard eliminates the 24-hour data lag that compromises decision-making in fast-moving markets. Teams using real-time data make 34% faster strategic adjustments. |

### Message: Service outage notification

**Raw message:** Our servers are down and we're fixing it.

| Voice | Transformed |
|-------|-------------|
| **Professional** | We are currently experiencing a service disruption. Our engineering team is actively working to restore full functionality. We will provide updates every 30 minutes. We apologize for the inconvenience. |
| **Startup-Casual** | We're down right now — we know, and we're on it. The team is actively fixing the issue. We'll post updates every 15 minutes on our status page. Sorry about this. |
| **Technical** | Status: Degraded. Root cause: Database connection pool exhaustion on us-east-1 primary. Mitigation in progress. ETA: ~30 min. Follow status.acme.dev for updates. |
| **Friendly** | We hit a bump — the app is temporarily unavailable. Our team jumped on it immediately and we're working to get you back up and running. Hang tight, and thank you for your patience! |
| **Authoritative** | We have identified a service disruption affecting our platform. Our Site Reliability Engineering team has isolated the root cause and is executing our recovery protocol. Service restoration is expected within 30 minutes. Full incident report will follow. |

### Message: Asking for user feedback

**Raw message:** We want your feedback on the product.

| Voice | Transformed |
|-------|-------------|
| **Professional** | Your insights are invaluable to our product development process. We invite you to share your feedback through our quarterly survey. Your responses directly inform our roadmap priorities. |
| **Startup-Casual** | We build this for you, so we need to hear from you. Got 2 minutes? Tell us what's working, what's broken, and what you wish existed. Every response gets read by a real human on our team. |
| **Technical** | Feedback request: We're evaluating our API ergonomics and CLI workflow. If you've hit friction points or have feature requests, open an issue or fill out our 5-question survey: [link]. |
| **Friendly** | We'd love to hear from you! What do you like? What bugs you? What would make your day? Take our quick 2-minute survey and help us make things even better for you. |
| **Authoritative** | As we plan our next development phase, we are seeking structured input from our user base. Your operational experience with our platform provides critical data points that quantitative metrics alone cannot capture. Please contribute to our product direction survey. |

### Message: Pricing change announcement

**Raw message:** We're raising prices next month.

| Voice | Transformed |
|-------|-------------|
| **Professional** | Effective April 1, we will be adjusting our pricing structure to reflect the significant platform improvements delivered over the past year. Current subscribers will receive a 60-day grace period at existing rates. Full pricing details are available on our website. |
| **Startup-Casual** | Heads up — we're updating our pricing on April 1. Here's the honest reason: we've shipped 40+ features this year and our costs have grown. Existing customers keep their current price for 60 more days. New pricing is on our site — no surprises. |
| **Technical** | Pricing update effective 2025-04-01. See the migration guide for tier mapping. Existing API keys retain current rate limits through May 31. Changelog: [link]. |
| **Friendly** | We have some pricing news to share. Starting April 1, our plans will look a little different. We've added a ton of new features (you asked, we built!) and we're adjusting prices to keep improving. You've got 60 days at your current rate — no rush. |
| **Authoritative** | After a comprehensive review of our value delivery and market positioning, we are implementing a pricing adjustment effective April 1. This change reflects $2.4M in platform investment over the past 12 months, including 40+ feature releases. Current enterprise contracts will be honored through their term. |

---

## Voice Calibration Checklist

When writing brand content, run through this checklist:

- [ ] Does this sound like our brand, or could any company have written it?
- [ ] Is the formality level consistent with our spectrum setting?
- [ ] Are we using preferred vocabulary and avoiding banned words?
- [ ] Is the technical depth appropriate for the audience?
- [ ] Does the tone match the platform we're publishing on?
- [ ] Would our target customer feel spoken to, not spoken at?
- [ ] Is there a clear action or takeaway?
- [ ] Read it aloud — does it sound natural or forced?

## Building Your Voice Over Time

Brand voice is not static. It evolves as your company grows:

- **Pre-seed to Seed:** Voice is often the founder's natural voice. Authentic but inconsistent.
- **Seed to Series A:** Codify the voice. Write the guidelines. Train the team.
- **Series A to B:** Voice matures. More nuance, more platform adaptation, more consistency.
- **Growth stage:** Voice is institutional. Style guides, editorial reviews, brand police.

The goal is not to sound corporate. The goal is to sound unmistakably like you — at every touchpoint, at every scale.
