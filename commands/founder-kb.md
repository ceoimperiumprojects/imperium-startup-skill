---
name: founder-kb
description: 'Semantic search over the startup book knowledge base. Use when the user wants to search books, find specific advice from startup literature, or query the founder knowledge base. Triggers on: search books, knowledge base, founder-kb, book search, startup literature, what does [book] say about.'
user-invocable: true
---

# /imperium:founder-kb — Knowledge Base Search

Search the founder-ai-mentor knowledge base: 10 startup books, 2,019 chunks, semantic search powered by local embeddings.

## Available Books

| Book | Author | Chunks | Domain |
|------|--------|--------|--------|
| The Lean Startup | Eric Ries | 185 | Methodology |
| The Startup Owner's Manual | Steve Blank | 267 | Customer Development |
| Never Split the Difference | Chris Voss | 227 | Negotiation |
| $100M Offers | Alex Hormozi | 163 | Offer Creation |
| $100M Leads | Alex Hormozi | 281 | Lead Generation |
| Zero to One | Peter Thiel | 114 | Strategy |
| Hooked | Nir Eyal | 129 | Product/Engagement |
| Traction | Weinberg & Mares | 163 | Growth Channels |
| Obviously Awesome | April Dunford | 77 | Positioning |
| Founder's Guide | Custom | ~350 | Mindset & Productivity |

## How to Use

### If founder-kb CLI is installed:

Run the search wrapper script:
```bash
python skills/founder/scripts/founder_kb_search.py "your query here"
python skills/founder/scripts/founder_kb_search.py "pricing strategy" -k 10
python skills/founder/scripts/founder_kb_search.py "customer interviews" -s startup-owners-manual
```

Or use founder-kb directly:
```bash
founder-kb search "how to validate a startup idea"
founder-kb search "negotiation tactics" --source never-split-the-difference
founder-kb compare "pricing" --source1 100m-offers --source2 obviously-awesome
founder-kb sources
```

### If founder-kb CLI is NOT installed:

Use the distilled reference files instead — they contain the key insights from each book:

| Topic | Reference File |
|-------|---------------|
| Negotiation | `skills/sales-gtm/references/negotiation-tactics.md` |
| Offer creation | `skills/sales-gtm/references/offer-creation.md` |
| Lead generation | `skills/sales-gtm/references/lead-generation-advanced.md` |
| Traction channels | `skills/marketing/references/traction-channels.md` |
| Product positioning | `skills/marketing/references/product-positioning-advanced.md` |
| Habit-forming products | `skills/product-manager/references/habit-forming-products.md` |
| Contrarian strategy | `skills/ceo-advisor/references/contrarian-strategy.md` |
| Team leadership | `skills/ceo-advisor/references/team-leadership.md` |
| Lean startup | `skills/founder/references/lean-startup-methodology.md` |
| Customer development | `skills/founder/references/customer-development-advanced.md` |
| Founder mindset | `skills/founder/references/founder-mindset.md` |
| Founder productivity | `skills/founder/references/founder-productivity.md` |
| All books summary | `skills/founder/references/book-insights-index.md` |

## Workflow

1. Determine user's query topic
2. Try founder-kb search if available (richer, semantic results)
3. Fall back to reference files (always available, zero dependencies)
4. Synthesize insights into actionable advice
5. Cite the source book and relevant frameworks

## Setup (Optional)

To install the full semantic search:
```bash
bash skills/founder/scripts/setup_founder_kb.sh
```

Requires: Python 3.10+, ~2GB disk for models (sentence-transformers).
