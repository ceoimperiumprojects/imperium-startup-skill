---
name: linkedin
description: 'LinkedIn viral post generator with proven frameworks (121K+ impressions). Produces posts optimized for the LinkedIn algorithm using 12 post types, 50+ hooks, engagement psychology, and brand voice integration. Use when the user wants to write LinkedIn posts, build thought leadership, grow their personal brand on LinkedIn, or create viral content. Triggers on: LinkedIn, LinkedIn post, viral post, hook, engagement, thought leadership, personal brand, LinkedIn algorithm, LinkedIn content, post ideas, LinkedIn strategy.'
user-invocable: false
---

# LinkedIn Viral Post Creation

Create LinkedIn posts engineered for virality using proven frameworks, algorithm mechanics, and engagement psychology. Built from analysis of posts that generated 121K+ impressions.

## Keywords

LinkedIn, LinkedIn post, viral post, hook, engagement, thought leadership, personal brand, LinkedIn algorithm, LinkedIn content, post ideas, LinkedIn strategy, LinkedIn growth, LinkedIn writing, content creation, professional brand, social selling, LinkedIn reach, impressions, LinkedIn comments, LinkedIn engagement, scroll-stopper, post format, carousel, content calendar

## Philosophy

- Every post must deliver genuine value — virality without substance is noise
- Authenticity beats polish. Real stories outperform manufactured content
- The hook is everything — 80% of your effort should go into the first 2 lines
- One idea per post, executed with precision
- Write for the person scrolling at 11 PM, tired, deciding whether to keep reading
- Short sentences. One thought = one line. Max 10-15 words per sentence
- Your audience doesn't care about you. They care about themselves through the lens of your story

---

## Configuration

Before writing, establish these preferences. If not specified, use defaults.

### Language Preference
- **Auto-detect:** If `brand/brand.json` exists, check for `language` field and use it
- **Ask if unclear:** "What language should this post be in?"
- **Default:** English
- **Bilingual markets:** Some audiences respond better to native language (emotional connection) vs English (wider reach). When the user's brand targets a non-English-speaking market, suggest writing the hook + CTA in their native language for emotional punch, with body in English — or vice versa. Test both approaches
- **Rule of thumb:** Educational/framework posts perform better in English (wider reach). Story/vulnerability posts perform better in the author's native language (deeper emotional resonance)

### Post Length Preference
- **Short (700-1,000 chars):** Quick insights, strong opinion, single idea. Best for busy audiences
- **Medium (1,000-1,400 chars):** The sweet spot. Enough depth without losing attention. DEFAULT
- **Long (1,400-1,800 chars):** Deep stories, case studies, detailed frameworks. Only when content demands it
- **Warning:** Under 700 chars = too thin for algorithm. Over 1,800 chars = reader drop-off spikes

### Industry Context
Adjusts terminology, examples, and hashtag recommendations:
- **Tech/SaaS** — MRR, ARR, churn, product-led, API, DevOps
- **Agency/Consulting** — clients, retainers, case studies, proposals, deliverables
- **E-commerce/DTC** — ROAS, AOV, LTV, supply chain, fulfillment
- **Creative/Design** — portfolio, brand, visual identity, UX, typography
- **Finance/Fintech** — compliance, regulation, risk, returns, portfolio
- **Healthcare/Biotech** — patients, outcomes, clinical, regulatory, trials
- **Education/EdTech** — learners, curriculum, outcomes, engagement, retention
- **General startup** — product-market fit, fundraising, scaling, hiring

### Target Audience
Who is reading this post:
- **Founders/CEOs** — strategic, big-picture, investor-aware
- **Developers/Engineers** — technical, skeptical of buzzwords, values precision
- **Marketers** — trend-aware, metrics-driven, creative
- **Sales professionals** — results-oriented, competitive, practical
- **Executives/VPs** — leadership-focused, ROI-driven, time-constrained
- **Job seekers/Career changers** — aspirational, skill-building, relatable
- **General professional** — broad appeal, universal themes

### Personal Brand Archetype
How the author presents themselves:
- **Thought Leader** — bold opinions, industry predictions, frameworks
- **Practitioner** — "in the trenches" stories, tactical advice, real metrics
- **Storyteller** — narrative-driven, emotional, journey-focused
- **Data-Driven** — numbers first, analysis, research-backed claims
- **Mentor** — teaching focus, career advice, nurturing tone
- **Contrarian** — challenges status quo, provocative, evidence-backed rebellion

---

## Brand Integration

Before writing any post, check if `brand/brand.json` exists in the project.

### If brand files exist:
1. Read `brand/brand.json` for core identity
2. Read `brand/tone-of-voice.md` and adapt the writing style
3. Apply the brand's voice spectrums:
   - **Formal ←→ Casual** (where does this brand sit?)
   - **Technical ←→ Simple** (jargon level)
   - **Bold ←→ Diplomatic** (how strong are opinions stated?)
   - **Serious ←→ Playful** (humor and energy level)
   - **Personal ←→ Institutional** (first person vs company voice)
4. Use the brand's vocabulary patterns and terminology
5. Respect platform adaptation rules (LinkedIn = professional context)
6. Maintain brand personality while following LinkedIn best practices
7. Check for brand-specific topics to emphasize or avoid

### If no brand files exist:
Use a professional but conversational default voice:
- Confident, direct, specific — not corporate or stiff
- First-person perspective, sharing from experience
- Warm but authoritative tone
- Suggest running `/imperium:create-brand` for consistency across posts

### Voice Calibration Table

| Brand Spectrum | LinkedIn Adjustment |
|----------------|-------------------|
| Very formal | Slightly relax — LinkedIn rewards conversational tone even from formal brands |
| Very casual | Slightly tighten — LinkedIn audience expects professional baseline |
| Very technical | Add "translation" lines for broader reach while keeping credibility |
| Very simple | Add 1-2 specific data points to build authority |
| Very bold | Ensure bold claims have backing — LinkedIn audiences fact-check |
| Very diplomatic | Add at least one clear position — fence-sitting kills engagement |

---

## Core Writing Rules

### The 80/20 of LinkedIn Posts
The hook (first 140-210 characters before "see more") determines 80% of your post's success. Everything else is secondary.

### Formatting Rules
- Line break after every 1-2 sentences
- Use white space aggressively — dense text kills engagement
- One thought per line. Max 10-15 words per sentence
- Short paragraphs: 1-2 sentences maximum
- Never put links in the post body (kills reach 25-50%) — use first comment
- Use unicode characters sparingly for visual breaks (→ ↓ • ― /)
- Numbers are more compelling than words ("3x" not "triple", "$12K MRR" not "significant revenue")
- 70% of LinkedIn users are on mobile — format for small screens

### Voice Rules
- Use "you" more than "I" — make it about the reader
- Be specific: not "I grew my business" but "I went from $0 to $12K MRR in 9 months"
- Authentic > polished — imperfect but real beats perfect but sterile
- Vulnerability builds connection — share failures, not just wins
- Confident assertions, not hedging ("This works" not "I think this might work")
- Specificity = credibility. Precise numbers signal authenticity over vague claims

### Value Rules
- Every post must pass the "so what?" test
- Always add value — never just flex
- Teach something, share something, or make someone feel seen
- The reader should be able to DO something after reading your post
- If you can't articulate the takeaway in one sentence, the post isn't focused enough

### Anti-Patterns (Never Do These)
- "Excited to announce..." / "I'm humbled..." / "Big news!" — dead hooks
- Wall of text without empty lines
- Link IN the post body (put in first comment!)
- More than 5 hashtags (triggers spam filter)
- Question at the beginning instead of at the end
- Post and ghost (not responding to comments)
- Obvious AI-generated content (-30% reach, -55% engagement)
- Engagement bait ("Like if...", "Comment YES for...")
- Generic hooks that could be written by anyone
- Starting with "I" (posts starting with "You" or a number get 23% more engagement)

---

## Post Structure Formula

Every high-performing LinkedIn post follows this architecture:

```
HOOK (1-2 lines — must stop the scroll, 140-210 chars max)
↓
CONTEXT (2-3 lines — set the scene, make it relatable)
↓
BODY (5-10 lines — the meat, the insight, the story)
↓
LESSON/INSIGHT (2-3 lines — the takeaway they'll remember)
↓
CTA (1-2 lines — question at END, never beginning)
```

Max 2 CTAs per post. Question goes at the END (not the beginning — LinkedIn's algorithm measures comments after scroll-through, and a question at the top gets dismissed before context is established).

---

## The 12 Post Types — Quick Reference

| # | Type | Best For | Viral Potential | Key Element |
|---|------|----------|----------------|-------------|
| 1 | Personal Story | Emotional resonance, relatability | Very High | Transformation arc |
| 2 | Product Launch | New product/feature awareness | Medium | Start with THEIR pain |
| 3 | Hiring Post | Team building, employer brand | Medium | "I don't have X" > "We're hiring X" |
| 4 | Thought Leadership | Authority, bold positioning | High | Controversial but defensible |
| 5 | Tech/Industry News | Timeliness, relevance | Medium-High | YOUR filter on news |
| 6 | Milestone | Social proof, journey sharing | Medium | Journey + numbers |
| 7 | Educational/How-To | Authority, saves | High | Numbered steps, actionable |
| 8 | Case Study | Credibility, lead generation | High | Specific metrics, before/after |
| 9 | Behind the Scenes | Authenticity, connection | High | Authenticity > polish |
| 10 | Question/Poll | Comment driving, discussion | Medium | Specific, not generic |
| 11 | Listicle | Saves, shares, easy consumption | High | Your commentary adds value |
| 12 | Contrarian/Myth-Busting | Debate, thought leadership | Very High | Evidence-backed alternative |

Full templates, formulas, and 2-3 examples per type: `references/post-types.md`

---

## Hooks — Top 10 Quick Reference

The 10 highest-performing hook structures:

1. **Transformation:** "[Time] ago I was [humble situation]. Today I [impressive outcome]."
2. **Challenge:** "Stop doing [common practice]. Do this instead."
3. **Stat shock:** "[Specific number]% of [group] fail at [thing]. Here's why."
4. **Before/After:** "[Time] ago I was [situation]. Today [outcome]. Here's what changed."
5. **Unpopular opinion:** "Unpopular opinion: [bold statement]"
6. **Authority:** "I've [credibility marker]. Here's what I know for sure."
7. **Myth-bust:** "Most people think [X]. They're wrong."
8. **Mistake:** "The #1 mistake [professionals] make (and how to fix it)"
9. **Insider:** "I asked [impressive person/number] one question. Their answer surprised me."
10. **Reframe:** "You don't need [thing everyone says you need]. You need [alternative]."

Complete library of 50+ hooks with templates and examples: `references/hooks.md`

---

## LinkedIn Algorithm 2025 — Key Rules

### Content Scoring (in order of weight):
1. **Dwell time** — how long people stop scrolling to read (#1 factor)
2. **Comments** — meaningful comments (15+ words) = 15x more valuable than likes
3. **Engagement velocity** — how fast engagement arrives in first 90 minutes
4. **Saves** — 1 save = 5x the reach value of 1 like
5. **Shares** — redistributing to new networks
6. **Reactions** — likes and other reactions (lowest weight)

### Critical Numbers:
- External links in post body: **-25% to -40% reach**
- 5+ hashtags: **spam filter trigger**
- Golden Hour (first 60-90 min): determines **70% of total reach**
- Respond to every comment in first **15 minutes**
- Best timing: **Tuesday-Thursday, 8:00-10:00 AM** (target audience timezone)
- Obvious AI content: **-30% reach, -55% engagement**
- Carousel posts: **278% more engagement** than video, **596% more** than text-only
- Post without image: **50% less reach** (use 1080x1350px portrait format)
- Photos with YOU in them: **+60% reach** vs stock photos

### Four-Phase Distribution:
1. **Classification (0-60 min)** — AI scans for spam signals
2. **Golden Hour (1-2 hours)** — Small sample, measures comments/dwell/clicks
3. **Extended Distribution (2-24 hours)** — Strong engagement = expansion
4. **Long-tail (24+ hours)** — Can resurface 2-3 weeks later

Full algorithm deep-dive: `references/algorithm-2025.md`

---

## Engagement Psychology — Quick Reference

Why people engage — and how to trigger each behavior ethically:

| Principle | What It Does | How to Use |
|-----------|-------------|-----------|
| Pattern Interrupt | 1.7 seconds to stop the thumb | Unexpected first line, broken expectations |
| Curiosity Gap | 927% more clicks when loop is opened | Show result, hide method in hook |
| Zeigarnik Effect | Incomplete tasks remembered 90% better | Leave a loop in hook, close in body |
| Mirror Neurons | Stories remembered 22x better than facts | Vivid sensory details in narratives |
| Loss Aversion | Pain of loss ~2x stronger than joy of gain | "Don't make this mistake" > "Do this instead" |
| Specificity Bias | Precise numbers signal credibility | "$47,832" > "almost $50K" |
| Social Proof | People follow what others validate | Include metrics, client results, follower counts |
| Identity Signaling | People share what reflects well on them | Write posts people are PROUD to share |
| Underdog Effect | People root for the disadvantaged fighter | Humble beginnings → impressive outcome |
| Reciprocity | People engage back when you engage first | 15-20 min engaging before your post |
| Mere Exposure | Familiarity breeds trust (7-11 touchpoints) | Post consistently, 3-5x per week |
| Cognitive Load | 70% mobile users = limited attention | Short sentences, white space, scannable format |

Full psychology guide: `references/psychology.md`

---

## Advanced Tactics — Quick Reference

- **Golden Hour Strategy:** Pre-post engagement → Publish → Reply within 15 min → Monitor 60-90 min
- **Commenting Strategy:** 15-20 min engaging before posting, 10 quality comments daily on others' posts
- **Content Calendar:** Weekly themes, batch 5-10 posts in one session
- **Content Repurposing (3-5x Rule):** One idea → text post, carousel, thread, newsletter, video
- **Monetization Pipeline:** 70% educational → 20% problem-solution → 10% promotional
- **A/B Testing:** Same topic, different hooks. Same hook, different post types. Track everything
- **Inner Circle:** Build 10-15 creator relationships for mutual amplification
- **AI Best Practices:** Use AI for structure, never for voice. Edit heavily. Add personal details AI can't know

Full tactics guide: `references/tactics.md`

---

## Quality Score (/80)

Rate every post across 8 dimensions, each scored 0-10. Target: 60+ for publish, 70+ for high-confidence viral.

| # | Dimension | 0-3 (Weak) | 4-6 (Decent) | 7-10 (Strong) |
|---|-----------|-----------|--------------|---------------|
| 1 | **Hook Power** | Generic, skippable, starts with "I" | Interesting but not scroll-stopping | Impossible to not click "see more" |
| 2 | **Specificity** | Vague, no numbers, generic claims | Some data but still fuzzy | Exact numbers, names, dates, metrics |
| 3 | **Value Density** | Filler, obvious advice, nothing new | Useful but available elsewhere | Actionable insight reader can't get elsewhere |
| 4 | **Emotional Resonance** | Flat, corporate, no feeling | Mildly engaging, some personality | Makes reader feel something — seen, inspired, challenged |
| 5 | **Formatting** | Wall of text, no breaks | Some formatting but dense sections | Perfect white space, 1-2 sentence paragraphs, mobile-optimized |
| 6 | **Readability** | Complex sentences, jargon, 12+ grade | Mixed clarity, some jargon | 8th grade level or below, every sentence crystal clear |
| 7 | **CTA Strength** | No CTA or weak generic question | Question present but uninspiring | Specific question reader is COMPELLED to answer |
| 8 | **Brand Alignment** | Off-brand or no voice consistency | Partially aligned | Voice, vocabulary, and personality perfectly calibrated |

**Readability target:** Flesch-Kincaid 8th grade level or below. Short words, short sentences, active voice. If a 14-year-old can't understand it, simplify.

**Scoring guide:**
- 60-69: Publishable with minor polish
- 70-79: Strong post, likely to perform well
- 80: Perfect score — rare, aim for 70+

---

## Pre-Post Checklist

Before publishing any post, verify:

- [ ] **Hook test:** Would YOU click "see more"? Read it as a stranger
- [ ] **One idea test:** Can you state the core message in one sentence?
- [ ] **Specificity test:** Are there numbers, names, timeframes — not vague claims?
- [ ] **Value test:** Does the reader learn something or feel something?
- [ ] **Format test:** Line breaks, short paragraphs, 1,000-1,500 chars, mobile-friendly?
- [ ] **Link test:** No external links in body? (Move to first comment)
- [ ] **CTA test:** Question or invitation to engage at the END?
- [ ] **Hashtag test:** 3-5 relevant hashtags, mix of broad + niche?
- [ ] **Voice test:** Reads naturally out loud? No corporate jargon?
- [ ] **Brand test:** Aligned with brand voice (if brand files exist)?
- [ ] **AI test:** Does NOT sound AI-generated? Personal details present? Imperfections kept?
- [ ] **Image test:** Do you have an image? Photo of YOU > illustration > no image
- [ ] **First comment test:** Is your first comment ready? (link, resource, or bonus insight)

---

## Image Strategy

- Post without image = 50% less reach
- **Best:** Photos with YOU in them (+60% reach over stock)
- **Good:** Split images (before/after, comparison), custom graphics
- **Acceptable:** Relevant screenshots, data visualizations
- **Format:** 1080x1350px portrait (takes up maximum feed space on mobile)
- **Carousel:** 8-12 slides, each slide = one clear point, first slide = hook, last slide = CTA
- **Never:** Stock photos that feel generic, AI-generated art that looks artificial

---

## Reference Files

| File | Content |
|------|---------|
| `references/post-types.md` | All 12 post types with formulas, 2-3 full examples each, common mistakes |
| `references/hooks.md` | 50+ hooks organized by 9 categories, templates + filled examples, performance tiers |
| `references/algorithm-2025.md` | Four-phase distribution, engagement weights, penalties, timing, format performance, SSI |
| `references/psychology.md` | 12 psychological principles, sharing triggers, controversy calibration, parasocial relationships |
| `references/tactics.md` | Golden Hour strategy, commenting, content calendar, repurposing, metrics, A/B testing, DMs |
