# Search Strategy Matrix

12 search strategies to cast the widest possible net when mapping an ecosystem. Run ALL of these for comprehensive coverage.

## Strategy Table

| # | Strategy | Search Queries | Best For | imperium-crawl Equivalent |
|---|----------|---------------|----------|--------------------------|
| 1 | Direct name | "[category] software", "[category] app", "[category] tool" | Finding obvious competitors | `imperium-crawl search --query "[category] software" --count 20` |
| 2 | Alternative-to | site:alternativeto.net "[known competitor]" | Finding lesser-known alternatives | `imperium-crawl search --query "site:alternativeto.net [competitor]" --count 10` |
| 3 | Review sites | site:g2.com "[category]", site:capterra.com "[category]" | B2B/SaaS products | `imperium-crawl batch-scrape --urls "g2.com/categories/[cat],capterra.com/[cat]" --extraction-schema "extract product names, ratings, descriptions"` |
| 4 | App stores | "[category]" on App Store / Play Store | Mobile apps | `imperium-crawl search --query "[category] app store" --count 20` |
| 5 | Product Hunt | site:producthunt.com "[category]" | New/indie products | `imperium-crawl search --query "site:producthunt.com [category]" --count 15` |
| 6 | GitHub | "[category]" site:github.com, "awesome [category]" | Open-source | `imperium-crawl search --query "awesome [category] github" --count 20` |
| 7 | "vs" searches | "[competitor A] vs", "[competitor A] alternatives" | Finding head-to-head competitors | `imperium-crawl search --query "[competitor] alternatives" --count 15` |
| 8 | Reddit | "[category] recommendations" site:reddit.com | Community favorites | `imperium-crawl reddit --action search --query "[category] recommendations"` |
| 9 | Listicles | "best [category] [year]", "top [category] tools [year]" | Curated lists | `imperium-crawl search --query "best [category] tools 2025" --count 20` |
| 10 | Investor angle | "[category] startup funding [year]" | VC-backed competitors | `imperium-crawl search --query "[category] startup funding" --count 10` |
| 11 | Regional | "[category] [country/region]" | Regional variants | `imperium-crawl search --query "[category] [region]" --count 10` |
| 12 | Niche | "[specific use case] [category]" | Vertical-specific tools | `imperium-crawl search --query "[use case] [category]" --count 10` |

## Recommended Execution Order

1. **Strategies 1, 7, 9** first — these find the most competitors fastest
2. **Strategies 2, 3, 5** next — community/review sites reveal hidden gems
3. **Strategies 6, 8** — open-source and Reddit for community favorites
4. **Strategies 4, 10, 11, 12** — specialized searches for completeness

## imperium-crawl Batch Approach

When imperium-crawl is available, run multiple search strategies in sequence and aggregate:

```bash
# Phase 1: Cast wide net
imperium-crawl search --query "[category] software tools" --count 20
imperium-crawl search --query "[known competitor] alternatives" --count 20
imperium-crawl search --query "best [category] tools 2025" --count 20

# Phase 2: Deep dive on found competitors
imperium-crawl batch-scrape --urls "comp1.com,comp2.com,comp3.com" \
  --extraction-schema "extract company name, tagline, pricing model, key features, founded year, team size"

# Phase 3: Review sites for ratings and sentiment
imperium-crawl search --query "site:g2.com [category]" --count 10
imperium-crawl search --query "site:capterra.com [category]" --count 10
```

## Tier 1 Fallback (WebSearch only)

Without imperium-crawl, run each strategy as a WebSearch query. Key differences:
- Run queries one at a time (no parallelism)
- Manually visit and read each result with WebFetch
- No structured JSON output — extract data manually
- Expect 3-5x more time for the same coverage
