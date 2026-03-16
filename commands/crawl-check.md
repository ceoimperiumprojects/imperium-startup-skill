---
name: imperium:crawl-check
description: Check if imperium-crawl is installed and show available research capabilities.
user-invocable: true
---

# imperium-crawl Availability Check

Check whether imperium-crawl is installed and show the user what research capabilities are available.

## Step 1: Check Installation

Run:
```bash
command -v imperium-crawl >/dev/null 2>&1 && echo "INSTALLED" || echo "NOT_INSTALLED"
```

## Step 2: If Installed

Run `imperium-crawl --version` and report:

```
imperium-crawl is installed (version X.X.X)

Available research tools:

  SEARCH
    imperium-crawl search --query "..." --count 20
    Bulk web search with structured JSON output.

  BATCH SCRAPE
    imperium-crawl batch-scrape --urls "url1,url2" --extraction-schema "..."
    Parallel scraping with AI-powered data extraction.

  AI EXTRACT
    imperium-crawl ai-extract --url URL --schema '{...}'
    Extract structured data from any page using AI.

  YOUTUBE (no API key needed)
    imperium-crawl youtube --action search --query "..."
    imperium-crawl youtube --action video --url "..."
    imperium-crawl youtube --action transcript --url "..."
    imperium-crawl youtube --action channel --channel-url "..."
    Search videos, get metadata, extract transcripts, browse channels.

  REDDIT (no API key needed)
    imperium-crawl reddit --action search --query "..."
    imperium-crawl reddit --action posts --subreddit "..." --sort top --time month
    imperium-crawl reddit --action comments --url "..."
    Search Reddit, get subreddit posts, extract comment threads.

  SCREENSHOT
    imperium-crawl screenshot --url URL --full-page
    Capture full-page screenshots of competitor products.

You are in Tier 2 (Deep Research) mode.
All 9 research phases can use imperium-crawl for faster, deeper data collection.
```

## Step 3: If NOT Installed

Report:

```
imperium-crawl is NOT installed.

You are in Tier 1 (Quick Research) mode.
Using WebSearch + WebFetch for research — this works fine but has limitations:

  WHAT YOU'RE MISSING:
  - Bulk search with JSON output (search)
  - Parallel scraping of 20+ sites at once (batch-scrape)
  - AI-powered structured data extraction (ai-extract)
  - YouTube search, transcripts, and channel browsing (youtube) — NO API KEY NEEDED
  - Reddit search, posts, and comment mining (reddit) — NO API KEY NEEDED
  - Full-page screenshots of competitor products (screenshot)

  INSTALL:
  npm install -g imperium-crawl

  After installing, run /imperium:crawl-check again to verify.

  NOTE: WebSearch + WebFetch still work great for quick research.
  imperium-crawl adds depth and speed for comprehensive projects.
```

## CLI Syntax Reminders

If installed, also show these common gotchas:

```
SYNTAX REMINDERS:
- Boolean flags — NO value: --full-page (not --full-page true)
- JSON params — SINGLE QUOTES: --schema '{"key":"value"}'
- Batch URLs — COMMA-SEPARATED IN QUOTES: --urls "url1,url2"
- Freshness codes: pd=day, pw=week, pm=month, py=year
```
