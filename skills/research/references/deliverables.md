# Research Deliverables

## The 10 Deliverables

Every completed research project produces these 10 documents:

| # | Deliverable | Format | Description |
|---|-------------|--------|-------------|
| 1 | Ecosystem Map | JSON + diagram | Every competitor categorized by type, tier, and market segment |
| 2 | Top 20 Profiles | Markdown | 1-2 page deep profile for each of the top 20 competitors |
| 3 | Feature Matrix | CSV/Markdown table | All features x competitors with status indicators |
| 4 | Demo Video Library | JSON index | All videos indexed, validated, and prioritized |
| 5 | UI/UX Pattern Library | Screenshots + notes | Best/worst patterns with analysis |
| 6 | Gap Analysis | Markdown | Opportunities, table stakes, and USP validation |
| 7 | User Sentiment | Markdown | What users love, hate, and want across all competitors |
| 8 | Pricing Benchmark | Table + Markdown | All pricing tiers + pricing recommendation |
| 9 | Naming Decision | Markdown | Final name + domain/handle availability |
| 10 | Updated Vision | Markdown | Original vision refined by research evidence |

---

## Competitor Data Schema

For EACH competitor discovered in Phase 1, collect this structured data:

```json
{
  "company": {
    "name": "",
    "url": "",
    "founded": "",
    "hq_location": "",
    "team_size": "",
    "funding_total": "",
    "funding_stage": "bootstrap | seed | series_a | series_b | public",
    "investors": [],
    "revenue_estimate": "",
    "parent_company": ""
  },
  "product": {
    "name": "",
    "tagline": "",
    "description": "",
    "launch_date": "",
    "platforms": ["web", "ios", "android", "desktop", "cli"],
    "pricing_model": "freemium | subscription | one_time | usage | open_source",
    "free_tier": "",
    "cheapest_paid": "",
    "most_expensive": "",
    "target_audience": "",
    "unique_selling_point": ""
  },
  "traction": {
    "users_estimate": "",
    "app_store_rating": "",
    "app_store_reviews": 0,
    "g2_rating": "",
    "github_stars": 0,
    "social_followers": "",
    "alexa_rank": ""
  },
  "strengths": [],
  "weaknesses": [],
  "missing_features": [],
  "notes": ""
}
```

---

## Video Documentation Schema

For each validated video, document with this structure:

```json
{
  "competitor_product": "",
  "competitor_company": "",
  "video_title": "",
  "url": "",
  "source": "youtube | twitter | producthunt | tiktok | instagram | company_site | blog | conference | podcast",
  "duration_minutes": 0,
  "date_published": "",
  "views": 0,
  "likes": 0,
  "creator_type": "official | influencer | user | media | educational | investor",
  "creator_name": "",
  "video_type": "official_demo | setup_tutorial | feature_walkthrough | honest_review | comparison | conference_talk | pitch | podcast_interview | ad | user_testimonial",
  "production_quality": "low | medium | high | professional",
  "language": "",
  "features_demonstrated": [],
  "ui_moments_to_screenshot": [
    {"timestamp": "", "description": ""}
  ],
  "onboarding_shown": false,
  "team_features_shown": false,
  "pricing_discussed": false,
  "mobile_shown": false,
  "integrations_shown": [],
  "what_impressed": "",
  "what_was_weak": "",
  "key_quotes": [],
  "user_comments_sentiment": "positive | mixed | negative",
  "top_user_comments": [],
  "watch_priority": "must_watch | recommended | optional | skip"
}
```

---

## Top 20 Selection Criteria

Score each competitor on these 5 dimensions (1-5 each):

| Dimension | What to evaluate | Weight |
|-----------|-----------------|--------|
| Relevance | How close to our target market? | High |
| Traction | How many users/revenue? | High |
| Quality | How polished is the product? | Medium |
| Recency | How recently updated? | Medium |
| Threat level | How directly does it compete with our USP? | High |

Take the top 20 by total score for deep-dive analysis.

---

## Feature Matrix Format

```markdown
| Feature | Comp A | Comp B | Comp C | Our Plan |
|---------|--------|--------|--------|----------|
| Feature 1 | Yes | No | Partial | Yes |
| Feature 2 | No | Yes | Yes | Yes |
```

Values: Yes | No | Partial | Unknown

Categorize each feature as:
- **Table stakes** — Everyone has it, we must too
- **Differentiator** — Only some have it, competitive advantage
- **Unique** — Only one competitor has it, potential opportunity

---

## Gap Analysis Template

```markdown
# Gap Analysis: [Market Category]

## 1. What does NOBODY have?
(Your biggest opportunity)

## 2. What does EVERYONE have?
(Your table stakes — must build these)

## 3. Is our USP confirmed?
(Did research validate our differentiation?)

## 4. Top 3 competitor weaknesses?
(Your potential strengths)

## 5. What surprised us?
(Adjust vision accordingly)
```

---

## Research Tracker Template

```markdown
# [Market] Research Tracker — Started [date]

## Phase 1: Ecosystem Map
- Direct Competitors: ___ / 15+
- Indirect Competitors: ___ / 10+
- Regional Variants: ___ / 3+

## Phase 2: Deep Dive
- Top 20 Selected: [ ]
- UI Screenshots: ___
- Demo Videos Found: ___ / 50+
- Videos Watched: ___ / ___

## Phase 3: Feature Matrix
- Features Tracked: ___
- Gaps Found: ___
- USP Confirmed: [ ] Yes [ ] No [ ] Adjusted

## Phase 4: Sentiment — Reviews Analyzed: ___
## Phase 5: Adjacent — Products Analyzed: ___
## Phase 6: Architecture — Decisions Made: ___
## Phase 7: Pricing — Benchmarked: ___ — Our Price: ___
## Phase 8: Naming — Checked: ___ — Final: ___
## Phase 9: Deliverables — Complete: ___ / 10
```
