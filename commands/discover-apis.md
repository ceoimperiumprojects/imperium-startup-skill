---
name: imperium:discover-apis
description: Discover hidden APIs on any website. Maps endpoints, authentication, and data flows for competitive intelligence or integration research.
user-invocable: true
---

# API Discovery Workflow

You are performing hidden API discovery using the Imperium Startup framework. Reference the full skill documentation at `skills/api-discovery/SKILL.md` and patterns reference at `skills/api-discovery/references/api-patterns.md`.

## Step 1: Gather Target Information

Ask the user:
1. **What is the target URL?** (e.g., `https://competitor.com`)
2. **What is your goal?** (competitive intelligence, find integration points, security research, architecture study)
3. **Do you have an account on the target site?** (logged-in sessions reveal more API endpoints)
4. **Any specific features you want to investigate?** (e.g., their search, real-time features, checkout flow)

If the user provides only a URL, proceed with competitive intelligence as the default goal.

## Step 2: Initial Reconnaissance

### 2A: Check if the site is a Single Page Application (SPA)

Use WebFetch to load the target URL and analyze the HTML source:

**SPA indicators:**
- Minimal HTML body with a mount point (`<div id="root">`, `<div id="app">`, `<div id="__next">`)
- Large JavaScript bundles in `<script>` tags
- Framework signatures in the HTML:
  - `__NEXT_DATA__` script tag → Next.js
  - `data-reactroot` attribute → React
  - `ng-version` attribute → Angular
  - `data-v-` prefixed attributes → Vue.js
  - `__NUXT__` or `__nuxt` → Nuxt.js
  - `__sveltekit` → SvelteKit

**Server-rendered indicators:**
- Full HTML content visible in source
- Traditional `<form>` elements with `action` attributes
- Minimal JavaScript
- Server-side template markers (Jinja, ERB, Blade, Thymeleaf)

Report the finding:
```
TARGET: [url]
TYPE: SPA (React/Next.js) | Server-Rendered | Hybrid (SSR + SPA)
FRAMEWORK: [detected framework]
API DISCOVERY POTENTIAL: High (SPA) | Medium (Hybrid) | Low (Server-Rendered)
```

### 2B: Extract API Hints from Source

Analyze the page source for API clues:

1. **Script tags** — Look for embedded configuration objects:
   ```javascript
   window.__CONFIG__ = { apiUrl: "https://api.target.com", wsUrl: "wss://..." }
   ```

2. **Meta tags** — Some frameworks embed API URLs in meta tags

3. **CSP headers** — The `connect-src` directive lists allowed API domains:
   ```
   Content-Security-Policy: connect-src api.target.com wss://ws.target.com analytics.target.com
   ```

4. **JavaScript bundles** — Search for API URL patterns in JS files:
   - Strings containing `/api/`
   - Strings containing `graphql`
   - Strings containing `wss://`
   - Fetch/axios base URL configuration

5. **Next.js `__NEXT_DATA__`** — Contains the initial API response data and page props

6. **Link/preconnect headers** — `<link rel="preconnect" href="https://api.target.com">` reveals API domains

## Step 3: Check for imperium-crawl Availability

Check if `imperium-crawl` is available as an MCP tool or CLI command.

### If imperium-crawl IS available:

Run automated discovery:
```bash
# Full API discovery with 15-second wait for all calls to fire
imperium-crawl discover-apis --url "[target_url]" --wait-seconds 15

# If the site requires interaction to reveal APIs
imperium-crawl discover-apis --url "[target_url]" --wait-seconds 20 --interact --navigate-links 5
```

### If imperium-crawl is NOT available:

Proceed with manual analysis using the tools available:

1. **WebFetch** — Fetch the page and analyze HTML source, headers, and embedded data
2. **WebSearch** — Search for `"[target] API" OR "[target] API documentation"` to find any public API docs
3. **Source analysis** — Parse JavaScript bundles for hardcoded API URLs and endpoint patterns
4. **Known API pattern matching** — Use the patterns reference to identify likely endpoints based on the product type

Guide the user through manual browser-based discovery:

```
MANUAL DISCOVERY INSTRUCTIONS:

1. Open [target_url] in Chrome/Edge
2. Open DevTools (F12) → Network tab
3. Check "Preserve log" checkbox
4. Filter by "Fetch/XHR"
5. Clear the network log
6. Refresh the page and wait 15 seconds
7. Note all API calls that appear

Then interact with the site:
- Use the search feature
- Navigate to different pages
- Scroll down (trigger lazy loading)
- Open menus, modals, dropdowns
- Check notifications area
- Visit settings/profile pages

For each API call, note:
- URL, Method, Status Code
- Request headers (especially Authorization)
- Response body structure
```

## Step 4: Analyze and Categorize Discoveries

Organize all discovered information into these categories:

### 4A: API Architecture

```
BASE URL(S):
  → Primary API: [url]
  → Secondary: [url] (if exists)
  → GraphQL: [url] (if exists)

VERSIONING: [v1/v2/date-based/none]
PROTOCOL: REST | GraphQL | gRPC-Web | Mixed
FORMAT: JSON | XML | Protocol Buffers
```

### 4B: Authentication Analysis

```
AUTH TYPE: JWT Bearer | Cookie Session | API Key | OAuth | None Detected
TOKEN LOCATION: Authorization header | Cookie | Query param
TOKEN FORMAT: JWT (algorithm, expiry) | Opaque | Session ID
REFRESH MECHANISM: [endpoint or "none detected"]
MFA DETECTED: Yes | No
OAUTH PROVIDERS: [Google, GitHub, etc. if applicable]
```

### 4C: Endpoint Inventory

For each discovered or inferred endpoint, document:

```
[METHOD] [PATH]
  Auth Required: Yes/No
  Rate Limited: Yes/No (headers observed)
  Pagination: cursor/offset/page/none
  Response: [brief description]
  Notes: [anything notable]
```

Group endpoints by domain:
- **Authentication** — login, register, refresh, logout, MFA
- **User/Account** — profile, settings, preferences
- **Core Product** — the main domain resources (products, projects, messages, etc.)
- **Search** — search endpoints and autocomplete
- **Media** — upload, download, CDN URLs
- **Real-time** — WebSocket URLs, SSE endpoints
- **Analytics** — tracking, events, metrics (often third-party)
- **Billing** — subscription, payment, invoicing
- **Admin/Internal** — endpoints that shouldn't be public

### 4D: Third-Party Services Detection

Identify external services the target uses:
```
PAYMENTS: Stripe | PayPal | Braintree | [other]
ANALYTICS: Segment | Mixpanel | Amplitude | Google Analytics
SEARCH: Algolia | Elasticsearch | Meilisearch | Typesense
AUTH: Auth0 | Firebase Auth | Cognito | Clerk
CDN: Cloudflare | Fastly | CloudFront | Vercel
HOSTING: AWS | GCP | Azure | Vercel | Fly.io | Heroku
ERROR TRACKING: Sentry | Bugsnag | Datadog
FEATURE FLAGS: LaunchDarkly | Statsig | Flagsmith
```

### 4E: WebSocket & Real-time Analysis

```
WEBSOCKET URL: [wss://...]
PROTOCOL: Native WS | Socket.IO | SignalR | ActionCable | Phoenix
PURPOSE: [chat, notifications, live updates, etc.]
MESSAGE FORMAT: JSON | Binary | Text
MESSAGE TYPES: [list observed message types]
FREQUENCY: [messages per second/minute]
AUTH: [how auth is handled on the WS connection]
```

## Step 5: Generate Intelligence Report

Present the findings in a structured format:

```markdown
# API Intelligence Report: [Target Name]

## Executive Summary
- **Target:** [URL]
- **App Type:** SPA (React) / Server-Rendered / Hybrid
- **API Maturity:** Early / Growing / Mature / Enterprise-Grade
- **Total Endpoints Discovered:** [N]
- **Auth Complexity:** Simple / Moderate / Complex (MFA, OAuth, etc.)
- **Real-time Capabilities:** None / Basic / Advanced

## API Architecture
[Details from Step 4A]

## Authentication
[Details from Step 4B]

## Endpoints
[Organized inventory from Step 4C]

## Third-Party Stack
[Details from Step 4D]

## Real-Time Features
[Details from Step 4E]

## Competitive Insights
- [Key architectural decisions and what they imply]
- [Technology choices and maturity signals]
- [Data model observations]
- [Performance and scalability indicators]

## Integration Opportunities
- [Endpoints that could be useful to integrate with]
- [Data that could be accessed programmatically]
- [Webhooks or event streams available]

## Recommendations
- [Suggested next steps based on the user's goal]
```

## Step 6: Suggest Next Steps

Based on the user's stated goal, recommend follow-up actions:

**For Competitive Intelligence:**
- Deep-dive into specific endpoints that reveal business logic
- Compare API structure with your own architecture
- Analyze their data model against yours (what fields they track that you don't)
- Monitor their API for changes over time (new endpoints = new features coming)
- Check if they expose a GraphQL schema via introspection

**For Integration Building:**
- Identify which endpoints return the data you need
- Test if endpoints work without authentication (public data)
- Look for webhook support for real-time integration
- Check rate limits to understand usage constraints
- Search for official API documentation or developer portals

**For Security Research:**
- Document the full attack surface (all endpoints, auth mechanisms)
- Check for over-exposed data in API responses
- Look for sequential/guessable resource IDs
- Test CORS configuration for misconfigurations
- Check if GraphQL introspection is enabled in production
- Look for verbose error messages that leak implementation details

**For Architecture Study:**
- Analyze their pagination strategy (cursor vs. offset — scalability signal)
- Study their auth token lifecycle (expiry, refresh mechanism)
- Evaluate their real-time architecture (WebSocket vs. polling vs. SSE)
- Look at their caching strategy (CDN, response headers, ETags)
- Identify their database from API response patterns (MongoDB-style IDs vs. UUIDs vs. sequential)

## Output Deliverables

At the end of the workflow, the user should have:

1. **API Map** — Complete inventory of discovered endpoints with methods, auth requirements, and descriptions
2. **Auth Analysis** — How the target handles authentication and what it reveals about their security posture
3. **Tech Stack Profile** — All third-party services identified from API calls
4. **Intelligence Brief** — Strategic insights derived from API analysis (what their architecture says about their product maturity, team size, and technical decisions)
5. **Action Items** — Concrete next steps based on the user's goal
