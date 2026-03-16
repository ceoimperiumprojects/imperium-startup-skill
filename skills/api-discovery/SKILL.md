---
name: api-discovery
description: 'Hidden API discovery and intelligence tool. Detects internal APIs, REST/GraphQL endpoints, WebSocket connections, and authentication patterns on any website. Useful for competitive intelligence, integration building, and understanding how SPA applications work under the hood. Triggers on: hidden API, discover APIs, endpoint, SPA, intercept, XHR, fetch requests, websocket, internal API, reverse engineer API, API patterns, API endpoints, API mapping.'
user-invocable: false
---

# API Discovery & Intelligence Skill

## Overview

Modern web applications — especially Single Page Applications (SPAs) — communicate almost entirely through hidden APIs. These APIs are never documented publicly, yet they power every feature: product listings, search, real-time updates, user authentication, notifications, and payment flows.

This skill systematically discovers and maps these APIs, turning opaque frontends into transparent, analyzable systems.

**Use Cases:**

- **Competitive intelligence** — Understand how competitors build their products at the API level. What data do they expose? How do they paginate? What real-time features use WebSockets?
- **Integration opportunities** — Find unofficial APIs that you can integrate with before official APIs exist (or when they never will)
- **Security research** — Map the attack surface of a web application by understanding every endpoint it calls
- **Architecture learning** — Study how successful apps architect their API layers, authentication flows, and real-time data systems
- **Product building** — Reverse-engineer data models and business logic from API responses to build better competing products

**Why This Matters for Startups:**

When you see a competitor's polished UI, you only see 20% of the product. The API layer reveals the other 80% — the data model, the business rules, the scalability approach, the edge cases they handle. This skill gives you X-ray vision into any web application.

---

## Core Capabilities

---

### 1. Discover APIs (`discover_apis`)

**Purpose:** Intercept all XHR/fetch requests a website makes, revealing hidden API endpoints that power the frontend.

#### When `imperium-crawl` is available:

```bash
# Basic discovery — load page and capture all API calls
imperium-crawl discover-apis --url "target.com" --wait-seconds 10

# Extended discovery — navigate multiple pages to find more endpoints
imperium-crawl discover-apis --url "target.com" --wait-seconds 15 --navigate-links 5

# Deep discovery — interact with forms, buttons, modals to trigger API calls
imperium-crawl discover-apis --url "target.com" --wait-seconds 20 --interact --max-depth 3

# Discovery with authentication (if you have an account)
imperium-crawl discover-apis --url "target.com" --wait-seconds 15 --cookies "session=abc123"
```

This loads the page in a headless browser, waits for API calls to fire, and returns all discovered endpoints with methods, headers, request/response bodies, and timing data.

#### When `imperium-crawl` is NOT available (manual approach):

Follow this systematic process:

**Step 1: Prepare the Browser**
1. Open Chrome/Edge → DevTools (F12) → Network tab
2. Check "Preserve log" (so navigation doesn't clear results)
3. Filter by "Fetch/XHR" to hide static assets
4. Optional: Enable "Disable cache" for cleaner results

**Step 2: Passive Discovery — Initial Page Load**
1. Clear the Network tab
2. Navigate to the target URL
3. Wait 10-15 seconds for all initial API calls to complete
4. Document every request that appears

**Step 3: Active Discovery — User Actions**
Trigger API calls by performing common user actions:
- Scroll down (lazy loading / infinite scroll)
- Use search functionality
- Click through navigation / categories
- Open modals and popups
- Toggle filters and sort options
- Switch between list/grid views
- Click "Load more" buttons
- Visit user profile / settings pages
- Check notification areas
- Try the signup/login flow (without submitting real data)

**Step 4: Document Each API Call**
For every request captured, record:
- Full URL (including query parameters)
- HTTP method (GET, POST, PUT, PATCH, DELETE)
- Request headers (especially Authorization, Content-Type, custom headers)
- Request body (for POST/PUT/PATCH)
- Response status code
- Response headers (rate limit headers, cache headers, CORS)
- Response body structure (field names, data types, nesting)
- Timing (how long the request took)

#### What to Look For:

**Base API URL patterns:**
- `api.company.com` — dedicated API subdomain (common in mature products)
- `company.com/api/v2/` — path-based API (common in monoliths)
- `company.com/graphql` — GraphQL endpoint
- `company.com/_next/data/` — Next.js data routes
- `company.com/__api/` — framework-specific internal routes
- Third-party APIs (analytics, payments, CDN) — useful to understand tech stack

**Authentication detection:**
- `Authorization: Bearer eyJ...` — JWT token (decode at jwt.io for claims)
- `Cookie: session=...` — Cookie-based session
- `X-API-Key: ...` or `?api_key=...` — API key authentication
- `Authorization: Basic ...` — Basic auth (rare in SPAs)
- OAuth redirect flows — watch for `/oauth/authorize` redirects
- CSRF tokens — `X-CSRF-Token` header or hidden form fields

**Pagination patterns:**
- Cursor-based: `?cursor=abc123` or `?after=abc123` (modern, scalable)
- Offset-based: `?offset=20&limit=10` (traditional, simple)
- Page-based: `?page=2&per_page=25` (traditional)
- Link headers: `Link: <url>; rel="next"` (RFC 5988)
- Response metadata: `{"next_cursor": "abc", "has_more": true}`

**Rate limiting detection:**
- `X-RateLimit-Limit` — max requests per window
- `X-RateLimit-Remaining` — requests left
- `X-RateLimit-Reset` — when window resets
- `Retry-After` header on 429 responses
- Custom rate limit headers (vary by provider)

**Real-time connections:**
- WebSocket URLs: `wss://ws.company.com/...`
- Server-Sent Events: `text/event-stream` content type
- Long polling: requests that hang for 30+ seconds
- Socket.IO: `/socket.io/?EIO=4&transport=polling`

---

### 2. Query APIs (`query_api`)

**Purpose:** Test discovered endpoints to understand their behavior, data models, and business logic.

#### When `imperium-crawl` is available:

```bash
# Simple GET request
imperium-crawl query-api --url "api.target.com/v1/products" --method GET

# GET with query parameters
imperium-crawl query-api --url "api.target.com/v1/products?category=electronics&limit=5" --method GET

# POST with JSON body
imperium-crawl query-api --url "api.target.com/v1/search" --method POST \
  --body '{"query": "test", "filters": {"price_min": 0}}'

# Request with custom headers
imperium-crawl query-api --url "api.target.com/v1/products" --method GET \
  --headers '{"Accept": "application/json", "X-Requested-With": "XMLHttpRequest"}'

# GraphQL introspection query
imperium-crawl query-api --url "target.com/graphql" --method POST \
  --body '{"query": "{__schema{types{name,fields{name,type{name}}}}}"}'
```

#### When `imperium-crawl` is NOT available:

Use WebFetch MCP tool or browser DevTools console:

```javascript
// From browser console (same-origin only)
fetch('/api/v1/products')
  .then(r => r.json())
  .then(data => console.log(JSON.stringify(data, null, 2)));
```

Or use curl from terminal:

```bash
curl -s "https://api.target.com/v1/products" \
  -H "Accept: application/json" | jq .
```

Note: Without proper authentication tokens or cookies, most endpoints will return 401/403.

#### Analysis Checklist:

For each endpoint you query, analyze:

- **Response format** — JSON (most common), XML (legacy), Protocol Buffers (high-performance), MessagePack (binary JSON)
- **Data richness** — What fields are exposed? Are there fields that shouldn't be public? Nested objects that reveal the data model?
- **Error response patterns** — What does a 400 look like? 404? 500? Consistent error schema indicates API maturity
- **Rate limiting behavior** — Make 5-10 rapid requests. Do you get throttled? At what threshold?
- **CORS headers** — `Access-Control-Allow-Origin: *` means callable from any browser. Specific domain means restricted
- **Caching headers** — `Cache-Control`, `ETag`, `Last-Modified` reveal caching strategy
- **API version in URL** — `v1`, `v2`, `v3` indicates maturity and iteration speed
- **Response size** — Are they over-fetching? Sending 50 fields when frontend shows 5? (common inefficiency)
- **Null handling** — Do they omit null fields or include them? Reveals backend conventions
- **ID formats** — Sequential integers (guessable), UUIDs (not guessable), or custom IDs (e.g., Stripe's `cus_...`)

---

### 3. Monitor WebSockets (`monitor_websocket`)

**Purpose:** Observe real-time data streams to understand live features like notifications, chat, price updates, collaborative editing, and live dashboards.

#### When `imperium-crawl` is available:

```bash
# Monitor WebSocket for 30 seconds
imperium-crawl monitor-websocket --url "wss://ws.target.com/stream" --duration 30

# Monitor with initial subscription message
imperium-crawl monitor-websocket --url "wss://ws.target.com/stream" --duration 30 \
  --send '{"type": "subscribe", "channel": "updates"}'

# Monitor Socket.IO connection
imperium-crawl monitor-websocket --url "wss://ws.target.com/socket.io/?EIO=4&transport=websocket" \
  --duration 60
```

#### When `imperium-crawl` is NOT available:

**Browser DevTools approach:**
1. Open DevTools → Network tab → Filter by "WS"
2. Navigate to a page with real-time features
3. Click on the WebSocket connection that appears
4. Switch to the "Messages" tab
5. Watch messages flow — green arrows are sent, red are received
6. Document message formats, frequency, and patterns

**What to analyze in WebSocket streams:**

- **Connection handshake** — What initial messages are exchanged? Authentication tokens sent?
- **Message format** — JSON, binary (Protocol Buffers), or plain text?
- **Message types** — What event categories exist? (`update`, `notification`, `ping`, `subscribe`)
- **Frequency** — How often do messages arrive? (every 100ms for real-time, every 30s for heartbeat)
- **Payload size** — Are messages compact (optimized) or verbose (over-sending)?
- **Reconnection behavior** — What happens when connection drops? Auto-reconnect with backoff?
- **Channel/room system** — Can you subscribe to specific data streams?

---

## SPA Detection

Before running API discovery, determine if the target is a Single Page Application. SPAs are the richest targets for API discovery because they make all data requests through JavaScript.

### Detection Methods:

**1. View Page Source Check**
Right-click → View Page Source. If the HTML body is mostly empty with a single mount point, it's an SPA:
```html
<!-- SPA indicator — nearly empty body -->
<body>
  <div id="root"></div>
  <script src="/static/js/main.abc123.js"></script>
</body>
```
vs.
```html
<!-- Server-rendered — content in HTML -->
<body>
  <header>...</header>
  <main>
    <h1>Product Name</h1>
    <div class="product-grid">...</div>
  </main>
</body>
```

**2. Framework Detection**
Check browser console for framework globals:
- **React:** `window.__REACT_DEVTOOLS_GLOBAL_HOOK__` or `document.querySelector('[data-reactroot]')`
- **Vue:** `window.__VUE_DEVTOOLS_GLOBAL_HOOK__` or `document.querySelector('[data-v-]')`
- **Angular:** `document.querySelector('[ng-version]')` or `window.ng`
- **Svelte:** check for `__svelte` attributes in DOM
- **Next.js:** `window.__NEXT_DATA__` (SSR + SPA hybrid — still rich API calls)
- **Nuxt:** `window.__NUXT__`

**3. Network Behavior**
SPAs have a distinctive network pattern:
- Initial load: 1 HTML file + many JS/CSS bundles
- After load: burst of XHR/fetch API calls to populate the page
- Navigation: URL changes without full page reload (History API)
- Subsequent pages: only API calls, no new HTML documents

**4. URL Pattern**
- Hash routing: `site.com/#/dashboard` (older SPAs)
- History API: `site.com/dashboard` but no full reload (modern SPAs)
- Check: click links and watch the Network tab. If no new `document` type appears, it's an SPA

### Hybrid Detection

Modern sites are often hybrids (SSR + SPA):
- **Next.js / Nuxt / Remix** — Server-render initial HTML, then hydrate into SPA
- These still make many API calls and are good targets for discovery
- Look for `__NEXT_DATA__` or similar hydration payloads in page source — these contain the initial API response data

---

## Common API Patterns Reference

### REST API Conventions

Standard CRUD pattern:
```
GET    /api/v1/resources              → List (with pagination)
GET    /api/v1/resources/:id          → Get single resource
POST   /api/v1/resources              → Create new resource
PUT    /api/v1/resources/:id          → Full update (replace)
PATCH  /api/v1/resources/:id          → Partial update
DELETE /api/v1/resources/:id          → Delete
```

Common extensions:
```
GET    /api/v1/resources/:id/children → Nested resources
POST   /api/v1/resources/search       → Complex search (body too large for GET query params)
POST   /api/v1/resources/batch        → Batch operations
GET    /api/v1/resources/count        → Count without fetching data
GET    /api/v1/resources/export       → CSV/PDF export
POST   /api/v1/resources/import       → Bulk import
```

### GraphQL APIs

GraphQL uses a single endpoint for everything:
```
POST /graphql

# Query — read operations
{"query": "{ products(first: 10) { id name price } }"}

# Mutation — write operations
{"query": "mutation { createProduct(input: {name: \"Test\"}) { id } }"}

# Introspection — discover the entire schema
{"query": "{__schema{types{name,fields{name,type{name}}}}}"}

# Named queries with variables
{"query": "query GetProduct($id: ID!) { product(id: $id) { id name } }", "variables": {"id": "123"}}
```

Detection clues:
- Single POST endpoint (usually `/graphql` or `/api/graphql`)
- Request body always has a `query` field
- Response always has a `data` field (and optionally `errors`)
- `Content-Type: application/json` both ways

### Authentication Patterns

**Bearer Token (JWT):**
Most common in SPAs. Token stored in localStorage or memory.
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```
Decode the JWT payload at jwt.io to find: user ID, roles, expiration, issuer.

**Cookie-Based Sessions:**
Traditional web apps. Cookie set by server, sent automatically by browser.
```
Cookie: session=abc123def456; _csrf=xyz789
```

**API Key:**
Common for public/developer APIs. Usually in header or query param.
```
X-API-Key: sk_live_abc123
?api_key=sk_live_abc123
```

**OAuth 2.0 Flows:**
Watch for redirect chains:
1. App redirects to `provider.com/oauth/authorize?client_id=...&redirect_uri=...`
2. User authenticates at provider
3. Provider redirects back to `app.com/callback?code=...`
4. App exchanges code for access token (server-side)

---

## Output Format

For each target analyzed, generate a structured API intelligence report:

```json
{
  "target": "https://target.com",
  "scan_date": "2025-01-15",
  "is_spa": true,
  "framework": "React (Next.js)",
  "base_url": "https://api.target.com",
  "api_version": "v2",
  "auth_type": "bearer_jwt",
  "auth_details": {
    "token_location": "localStorage",
    "token_key": "auth_token",
    "jwt_algorithm": "RS256",
    "token_expiry": "24h",
    "refresh_mechanism": "POST /auth/refresh"
  },
  "total_endpoints": 15,
  "endpoints": [
    {
      "method": "GET",
      "path": "/v2/products",
      "full_url": "https://api.target.com/v2/products",
      "auth_required": true,
      "rate_limited": true,
      "rate_limit": "100/minute",
      "response_format": "json",
      "pagination": {
        "type": "cursor",
        "param": "after",
        "default_page_size": 50
      },
      "query_params": ["category", "sort", "search", "after", "limit"],
      "response_fields": ["id", "name", "price", "description", "images", "created_at"],
      "notes": "Returns product catalog. Supports filtering by category and full-text search."
    },
    {
      "method": "POST",
      "path": "/v2/search",
      "full_url": "https://api.target.com/v2/search",
      "auth_required": false,
      "rate_limited": true,
      "rate_limit": "30/minute",
      "response_format": "json",
      "request_body": {
        "query": "string",
        "filters": "object",
        "page": "number",
        "size": "number"
      },
      "notes": "Full-text search with faceted filtering. Uses Elasticsearch under the hood (visible in error responses)."
    }
  ],
  "websockets": [
    {
      "url": "wss://ws.target.com/updates",
      "purpose": "Real-time price and inventory updates",
      "protocol": "custom JSON",
      "message_format": "json",
      "message_types": ["price_update", "stock_change", "heartbeat"],
      "avg_frequency": "2 messages/second",
      "auth_required": true,
      "notes": "Requires auth token in initial connection as query param"
    }
  ],
  "graphql": {
    "endpoint": "/graphql",
    "introspection_enabled": true,
    "schema_types": 45,
    "notable_queries": ["products", "user", "orders", "recommendations"],
    "notable_mutations": ["createOrder", "updateProfile", "addToCart"],
    "notes": "Full introspection available. Schema suggests they use Shopify-style architecture."
  },
  "third_party_apis": [
    {"service": "Stripe", "endpoint": "api.stripe.com", "purpose": "Payments"},
    {"service": "Segment", "endpoint": "api.segment.io", "purpose": "Analytics"},
    {"service": "Algolia", "endpoint": "*.algolia.net", "purpose": "Search"},
    {"service": "Cloudinary", "endpoint": "res.cloudinary.com", "purpose": "Image CDN"}
  ],
  "security_observations": {
    "cors": "Restricted to target.com origins",
    "csp": "Present and strict",
    "hsts": true,
    "api_key_exposure": "No API keys visible in frontend code",
    "over_fetching": "User endpoint returns email and phone — potential PII concern"
  },
  "competitive_insights": [
    "Uses cursor pagination — indicates large datasets and modern architecture",
    "WebSocket for real-time pricing suggests dynamic pricing engine",
    "GraphQL with 45 types — complex data model, heavy investment in API layer",
    "Algolia for search instead of building in-house — focus on core product over infrastructure",
    "Auth token expires every 24h with silent refresh — good security practice"
  ]
}
```

---

## Discovery Workflow Summary

```
STEP 1: SPA Detection
  → View source, check framework globals, observe network behavior

STEP 2: Passive Discovery (page load)
  → Record all API calls made on initial page load
  → Note base URLs, auth patterns, response formats

STEP 3: Active Discovery (interaction)
  → Trigger API calls through search, navigation, scrolling, modals
  → Look for CRUD endpoints, pagination, error patterns

STEP 4: WebSocket Discovery
  → Check for real-time connections (WS tab in DevTools)
  → Monitor message formats and frequency

STEP 5: GraphQL Introspection
  → If GraphQL detected, try introspection query
  → Map queries, mutations, and types

STEP 6: Analysis & Report
  → Structure findings into the output format above
  → Add competitive insights and strategic observations
  → Flag security concerns or over-exposed data
```

---

## Ethics & Legal Guidelines

This skill is designed for **legitimate research and intelligence gathering** only.

**DO:**
- Only discover publicly accessible APIs (those called by the browser without special access)
- Use for competitive research, integration planning, and architecture learning
- Respect `robots.txt` and Terms of Service
- Rate-limit your own queries — don't hammer discovered endpoints
- Report genuine security vulnerabilities through responsible disclosure

**DO NOT:**
- Bypass or circumvent authentication mechanisms
- Access data you are not authorized to see
- Abuse rate limits or cause service degradation
- Scrape personal data or PII in bulk
- Violate CFAA (Computer Fraud and Abuse Act) or equivalent local laws
- Use discovered APIs for commercial scraping without permission
- Reverse-engineer APIs to build direct clones that violate IP

**Gray Areas:**
- Using public APIs that have no Terms of Service — generally OK for small-scale research
- Inspecting your own accounts' API traffic — always OK
- Testing endpoints with modified parameters — OK if you don't access unauthorized data
- GraphQL introspection — it's a feature, not a vulnerability, but don't abuse what you find

**When in doubt:** If an endpoint clearly isn't meant to be public, don't use it. The goal is intelligence and learning, not exploitation.
