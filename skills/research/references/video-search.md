# Video Search Strategies

A 5-minute demo video reveals more about a competitor than an hour reading their docs. Videos show real interaction flow, loading times, friction points, and how intuitive the product actually is.

## 8 Search Strategies

For EACH competitor, run ALL of these. Replace `[product]`, `[company]`, and `[founder]` with actual names.

### Strategy 1 — Product Name (primary)

**WebSearch queries:**
```
"[product name] demo" site:youtube.com
"[product name] walkthrough" site:youtube.com
"[product name] tutorial" site:youtube.com
"[product name] review" site:youtube.com
"[product name] how to use" site:youtube.com
"[product name] setup guide" site:youtube.com
"[product name] features" site:youtube.com
"[product name] [current year]" site:youtube.com
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "[product name] demo"
imperium-crawl youtube --action search --query "[product name] walkthrough"
imperium-crawl youtube --action search --query "[product name] tutorial"
imperium-crawl youtube --action search --query "[product name] review"
```

### Strategy 2 — Company Name

**WebSearch queries:**
```
"[company name] demo" site:youtube.com
"[company name] product" site:youtube.com
"[company name] launch" site:youtube.com
"[company name]" site:youtube.com (find their channel)
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "[company name] demo"
imperium-crawl youtube --action channel --channel-url "youtube.com/@[company]"
```

### Strategy 3 — Combined (product + company + founder)

**WebSearch queries:**
```
"[product name] [company name]" site:youtube.com
"[product name] by [company name]" site:youtube.com
"[founder name] [product name]" site:youtube.com
"[founder name] [company name]" site:youtube.com
"[founder name]" site:youtube.com + "demo|launch|pitch"
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "[product name] [company name]"
imperium-crawl youtube --action search --query "[founder name] [product name]"
```

### Strategy 4 — Comparison & Category

**WebSearch queries:**
```
"best [category] apps [year]" site:youtube.com
"[product name] vs [known competitor]" site:youtube.com
"[product name] vs" site:youtube.com
"[category] comparison [year]" site:youtube.com
"[category] review [year]" site:youtube.com
"top [category] tools" site:youtube.com
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "best [category] apps 2025"
imperium-crawl youtube --action search --query "[product name] vs"
imperium-crawl youtube --action search --query "[category] comparison 2025"
```

### Strategy 5 — Platform-Specific

**Manual search locations:**
```
Product Hunt: search "[product name]" on producthunt.com — launch pages have videos
Twitter/X: "[product name] demo" OR "[product name]" filter:videos
TikTok: search "[product name]" — short demos and reviews
Instagram: search "[product name]" — reels and stories
Company website: check homepage, /demo, /features, /about for embedded videos
Company blog: [company url]/blog — often has video walkthroughs
Company YouTube channel: youtube.com/@[company] or youtube.com/c/[company]
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action channel --channel-url "youtube.com/@[company]"
imperium-crawl search --query "site:producthunt.com [product name]" --count 5
imperium-crawl batch-scrape --urls "[company].com,[company].com/demo,[company].com/features" \
  --extraction-schema "extract any video URLs or embedded YouTube links"
```

### Strategy 6 — Educational & Media

**WebSearch queries:**
```
"[product name]" site:freecodecamp.org (full tutorials)
"[product name]" site:datacamp.com
"[product name]" site:udemy.com
"[product name]" site:medium.com + "review|demo|tutorial"
"[product name]" site:dev.to
"[product name]" + "conference|summit|keynote|pitch day" site:youtube.com
"[product name]" + "podcast|interview|founder story" site:youtube.com
"[product name]" on TechCrunch, The Verge, Wired (embedded videos)
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "[product name] conference talk"
imperium-crawl youtube --action search --query "[product name] founder interview"
imperium-crawl search --query "[product name] tutorial freecodecamp OR udemy OR datacamp" --count 10
```

### Strategy 7 — Mobile App Specific (if applicable)

**WebSearch queries:**
```
"[app name] app review" site:youtube.com
"[app name] app walkthrough [year]" site:youtube.com
"[app name] iOS review" site:youtube.com
"[app name] Android review" site:youtube.com
App Store preview video (visible on app listing page)
Google Play Store video (visible on app listing page)
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "[app name] app review 2025"
imperium-crawl youtube --action search --query "[app name] iOS Android walkthrough"
```

### Strategy 8 — Investor/Pitch (reveals business strategy)

**WebSearch queries:**
```
"[company name] pitch" site:youtube.com
"[company name] demo day" site:youtube.com
"[company name] Y Combinator" site:youtube.com
"[company name] funding" site:youtube.com
"[founder name] pitch" site:youtube.com
"[founder name] interview" site:youtube.com
```

**imperium-crawl equivalent:**
```bash
imperium-crawl youtube --action search --query "[company name] pitch demo day"
imperium-crawl youtube --action search --query "[founder name] pitch interview"
# Get transcripts from pitch videos for competitive intelligence:
imperium-crawl youtube --action transcript --url "youtube.com/watch?v=VIDEO_ID"
```

## Video Priority Ranking

| Priority | Video Type | Why It Matters |
|----------|-----------|----------------|
| 1 | Official product demo | Shows intended UX at its best |
| 2 | Onboarding / setup walkthrough | Reveals friction and time-to-value |
| 3 | Honest third-party review | Unbiased — shows real pros and cons |
| 4 | Comparison video (vs competitors) | Direct competitive positioning |
| 5 | Founder pitch / investor demo | Reveals vision, strategy, and roadmap |
| 6 | Conference talk | Shows thought leadership and market positioning |
| 7 | User-made tutorial | Shows real daily usage, not marketing |
| 8 | Podcast / interview | Reveals business model, culture, strategy |

## Minimum Video Targets

- Top 5 competitors: 5+ videos each
- Top 6-15 competitors: 2-3 videos each
- Top 16-20 competitors: At least 1 video each
- **Total video library target: 50-80 videos**

## imperium-crawl Transcript Advantage

With imperium-crawl, you can extract transcripts from key videos — no YouTube API key needed:

```bash
# Get full transcript for analysis
imperium-crawl youtube --action transcript --url "youtube.com/watch?v=VIDEO_ID"

# Search a channel's videos
imperium-crawl youtube --action channel --channel-url "youtube.com/@competitor"
```

This enables:
- Keyword extraction from competitor pitches
- Feature mention frequency analysis
- Competitor roadmap hints from founder talks
- Pricing discussion extraction from reviews
