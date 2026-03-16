# LinkedIn Algorithm 2025 — Deep Dive

Comprehensive breakdown of how the LinkedIn algorithm evaluates, scores, and distributes content. Based on public statements from LinkedIn Engineering, creator program data, and analysis of high-performing content patterns.

---

## Four-Phase Distribution System

### Phase 1: Classification (0-60 minutes)

Immediately after posting, LinkedIn's AI classifier scans your post.

**What it checks:**
- Is this spam? (link farms, engagement bait, copied content)
- Is this low-quality? (very short, all caps, excessive hashtags, external links)
- Does it violate community guidelines?
- Is this obviously AI-generated? (pattern detection for generic AI outputs)

**Classification outcomes:**
| Classification | Result |
|---------------|--------|
| **Spam** | Post suppressed, may trigger account review |
| **Low quality** | Minimal distribution, shown to <5% of connections |
| **Clear** | Enters Phase 2 for test distribution |

**How to ensure "clear" classification:**
- Original content (not copy-pasted from other platforms)
- No more than 5 hashtags
- No external links in the post body
- No engagement bait phrases ("Like if you agree", "Comment YES for...")
- Proper formatting (line breaks, readable structure)
- Personal, specific language (not generic corporate-speak)
- Do NOT edit the post within the first hour (resets the algorithm)

### Phase 2: Golden Hour — Test Distribution (60-120 minutes)

Your post is shown to a small sample of your network (~8-12% of connections).

**What the algorithm measures:**

| Signal | Weight | What It Means |
|--------|--------|---------------|
| Dwell time | Very High | How long people pause on your post. #1 ranking factor |
| "See more" click rate | Very High | Proves the hook works — people want to read more |
| Comment rate | High | Especially comments with 15+ words |
| Engagement velocity | High | How FAST engagement comes in this window |
| Reaction rate | Medium | Likes, celebrates, etc. |

**Critical window:** The first 60-90 minutes determine ~70% of your post's total reach. If you get strong engagement in this window, the algorithm expands distribution aggressively.

**Your job during Golden Hour:**
- Be online and responsive
- Reply to EVERY comment within 15 minutes
- Each reply you write counts as a new engagement signal
- Your reply + their reply = a comment thread = highest-value engagement

### Phase 3: Extended Distribution (2-24 hours)

If Phase 2 signals are strong, the post enters extended distribution:
- Shown to 2nd-degree connections (friends of people who engaged)
- Appears in hashtag feeds
- May enter the "trending" content pool
- Gets pushed into LinkedIn notifications ("X commented on this post")

**What triggers extended distribution:**
- High dwell time ratio (people spending 10+ seconds on your post)
- Comment threads (back-and-forth conversations, not just single comments)
- Engagement from people with large networks (amplifier effect)
- Saves/bookmarks (strongest signal — someone bookmarked your post for later)

### Phase 4: Viral / Long-Tail Distribution (24 hours - 2+ weeks)

Posts that exceed algorithm thresholds can continue getting reach for up to 2-3 weeks.

**Viral signals:**
- Engagement from outside your network (2nd and 3rd degree connections)
- High share rate (people redistributing to their followers)
- Cross-industry engagement (post resonates beyond your niche)
- Multi-day engagement (people finding it days later and still engaging)
- High save-to-impression ratio

---

## Engagement Signal Weights

| Signal | Weight | Value vs. Like | Notes |
|--------|--------|---------------|-------|
| **Save/Bookmark** | Very High | 5x | Highest-intent action. Signals "I need to come back to this" |
| **Meaningful comment** (15+ words) | Very High | 15x | Signals conversation-worthy content |
| **Comment thread** (reply chain) | Very High | 20x+ | Back-and-forth = genuine discussion |
| **Share with comment** | High | 8x | Redistributes to new network with endorsement |
| **"See more" click** | High | 3x | Proves hook effectiveness |
| **Engagement velocity** (first 90 min) | High | — | Speed of engagement matters as much as volume |
| **Profile visit from post** | Medium | 2x | Content drove curiosity about the author |
| **Share (no comment)** | Medium | 2x | Redistributes but lower intent than share-with-comment |
| **Reaction (Like, Celebrate, etc.)** | Low-Medium | 1x | Easy action, baseline signal |
| **Follower gain from post** | Medium | 3x | Content was strong enough to earn a follow |

**Comment quality breakdown:**
| Comment Type | Algorithm Value |
|-------------|----------------|
| "Great post!" / emoji only | 1x (nearly worthless) |
| 5-15 word relevant comment | 5x |
| 15+ word thoughtful comment | 15x |
| Comment that sparks a reply chain | 20x+ |
| Comment from someone with 10K+ followers | Additional amplifier boost |

---

## Penalties Table — What Kills Reach

| Anti-Pattern | Reach Penalty | Notes |
|-------------|---------------|-------|
| External link in post body | -25% to -50% | Always use first comment for links |
| Editing post within first hour | Resets algorithm | Get it right before publishing |
| More than 5 hashtags | Spam filter trigger | 3-5 is optimal, fewer is fine |
| Engagement bait ("Like = agree") | Spam classification | Algorithm actively detects and penalizes |
| Posting 2+ times per day | Second post cannibalizes first | Wait at least 18-24 hours between posts |
| Deleting and reposting | Direct penalty | If a post flops, leave it |
| Tagging people who don't engage back | Low-quality signal | Only tag people who will respond |
| Cross-posting identical content | -20% to -30% | LinkedIn detects same text on Twitter/X |
| Excessive emojis (4+) | Correlation with lower reach | 1-2 emojis max, or zero |
| Obviously AI-generated content | -30% reach, -55% engagement | LinkedIn is actively building detection |
| Post and ghost (no replies) | Reduced distribution | Reply to comments in first 2 hours minimum |
| Selling in every post | Reduced over time | Algorithm detects promotional patterns |

---

## Content Format Performance

| Format | Reach Multiplier | Best For | Key Advantage |
|--------|-----------------|----------|---------------|
| **Carousel/Document** | 2-3x (278% more engagement than video, 596% more than text) | Tutorials, listicles, frameworks | Each swipe = engagement signal |
| **Text + Image (you in photo)** | 1.5-2x | Stories, opinions, behind-the-scenes | +60% reach when photo includes you |
| **Text + Image (graphic)** | 1.2-1.5x | Data viz, quotes, infographics | Stops the scroll visually |
| **Text only** | 1x (baseline) | Stories, opinions, confessions | Highest dwell time potential |
| **Polls** | 2-5x | Market research, sparking debate | Easy engagement, but use sparingly |
| **Video** | 0.8-1.5x (variable) | Personal stories, tutorials | Risky — bad video gets penalized hard |
| **Newsletter/Article** | 0.5x feed distribution | Deep expertise, SEO, evergreen | Subscribers get notified |

### Image Best Practices
- **Format:** 1080x1350px portrait (maximum feed real estate on mobile)
- **Photos of YOU** outperform everything else (+60% reach)
- **Split images** (before/after, comparison) drive curiosity
- **Text overlays** on images boost "see more" clicks
- **Never:** Generic stock photos, AI-generated art that looks obviously artificial

### Carousel Best Practices
- 8-12 slides optimal
- Slide 1 = hook (must stop the scroll on its own)
- One clear point per slide
- Last slide = CTA + summary
- Each swipe counts as an engagement signal
- Design for mobile (large text, simple visuals)

---

## Optimal Posting Times

| Day | Optimal Time | Relative Performance |
|-----|-------------|---------------------|
| **Tuesday** | 8:00-9:30 AM | Highest activity day |
| **Wednesday** | 8:00-10:00 AM | Strong mid-week engagement |
| **Thursday** | 8:00-9:30 AM | Second-highest activity day |
| Monday | 10:00-11:00 AM | OK — people settling in |
| Friday | 8:00-9:00 AM | Lower — people winding down |
| **Weekend** | Avoid | 60-70% less reach |

**Times are relative to your TARGET AUDIENCE's timezone.** If your audience is US-based, post at 8 AM ET. If European, 8 AM CET.

**Critical rules:**
- Never post twice in the same day (posts cannibalize each other)
- Wait at least 18-24 hours between posts
- Tuesday-Thursday, 8-10 AM is the proven sweet spot
- Worst times: weekends, after 5 PM on any day, Friday afternoon

---

## Posting Frequency

| Frequency | Outcome |
|-----------|---------|
| 1x/week | Minimum to maintain visibility. Slow growth |
| **3x/week** | Minimum effective dose for growth. Recommended starting point |
| **4-5x/week** | Optimal for aggressive growth |
| 2x/day | Diminishing returns — posts cannibalize each other |
| Daily for 6 weeks then stop | Worse than 3x/week consistently for 6 months |

**Key insight:** Consistency > volume. 3x/week for 6 months will always outperform 7x/week for 6 weeks.

---

## Pre-Post Engagement Ritual

Do this 15-30 minutes BEFORE publishing your post:

1. **Comment meaningfully on 10-15 posts** in your feed (not "great post!" — real thoughts)
2. **Reply to any pending comments** on your previous posts
3. **Visit 3-5 profiles** of target connections (triggers "viewed your profile" notifications)
4. **Engage with content from people** who regularly engage with you (reciprocity)

**Why this works:** LinkedIn's algorithm gives a distribution boost to "active members." Being active before posting signals that you're a real, engaged user — not a post-and-ghost bot.

---

## Hashtag Strategy 2025

### Rules
- Use 3-5 hashtags maximum (more than 5 can trigger spam filters)
- Mix: 1 broad + 2 medium + 1-2 niche
- Place at the bottom of the post, not inline
- Follow your own hashtags to monitor those feeds
- 3 hashtags is the statistically optimal number

### Hashtag Tiers

| Tier | Follower Count | Use | Purpose |
|------|---------------|-----|---------|
| **Broad** | 1M+ followers | 1 max | Gets you into a large feed, high competition |
| **Medium** | 10K-1M followers | 2 | Balanced reach and relevance |
| **Niche** | <10K followers | 1-2 | Smaller audience, higher engagement rate |

### Hashtag Examples by Industry

| Industry | Hashtag Mix |
|----------|------------|
| **SaaS/Tech** | #saas #startuplife #productled #b2bmarketing #techfounders |
| **Sales** | #salesstrategy #b2bsales #coldoutreach #revenue #closingdeals |
| **Marketing** | #contentmarketing #seo #growthmarketing #brandstrategy #digitalmarketing |
| **Leadership** | #leadership #management #teambuilding #ceo #executiveleadership |
| **Career** | #careeradvice #jobsearch #personalgrowth #professionaldevelopment #hiring |
| **AI/ML** | #artificialintelligence #machinelearning #genai #aitools #llm |
| **Design** | #uxdesign #productdesign #designthinking #userexperience #webdesign |
| **Fintech** | #fintech #banking #payments #finance #blockchain |

---

## SSI (Social Selling Index) Optimization

LinkedIn's SSI score (0-100) affects your content distribution. Higher SSI = more organic reach.

### The 4 SSI Pillars

| Pillar | Max Score | How to Improve |
|--------|----------|----------------|
| **Establish professional brand** | 25 | Complete profile, publish regularly, get endorsements |
| **Find the right people** | 25 | Connect with relevant professionals, use search effectively |
| **Engage with insights** | 25 | Share/comment on content, join relevant groups |
| **Build relationships** | 25 | Personalized connection requests, nurture through engagement |

**Targets:**
- 70+ = top 10% of your industry
- 80+ = top 1%
- **Check yours:** linkedin.com/sales/ssi

---

## Profile Optimization for Content Creators

When people see your post, they check your profile. Your profile is your landing page.

**Headline formula:** `[What you do] | [Who you help] | [Proof/credibility]`
- Example: "Helping B2B SaaS founders grow from $0 to $1M ARR | 3x founder | Built & sold 2 companies"

**About section:** Write it as a story, not a resume. First 2 lines must hook (same principle as posts).

**Featured section:** Pin your 3 best-performing posts. Social proof.

**Banner image:** Communicate your value proposition or current project.

**Activity section:** Keep it active. A dormant profile with a viral post creates distrust.
