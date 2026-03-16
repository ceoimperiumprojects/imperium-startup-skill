# API Patterns Reference

Comprehensive reference for identifying, classifying, and analyzing APIs discovered through browser interception, source code analysis, and network monitoring.

---

## REST API Patterns by Industry

### E-Commerce

E-commerce platforms typically expose rich, well-structured APIs due to the complexity of product catalogs, inventory, pricing, and checkout flows.

**Common Endpoints:**
```
GET    /api/v1/products                     → Product listing with filters
GET    /api/v1/products/:id                 → Product detail (includes variants, images, reviews)
GET    /api/v1/products/:id/reviews         → Paginated reviews
GET    /api/v1/categories                   → Category tree
POST   /api/v1/search                       → Full-text product search with facets
GET    /api/v1/cart                          → Current cart state
POST   /api/v1/cart/items                   → Add to cart
PATCH  /api/v1/cart/items/:id               → Update quantity
DELETE /api/v1/cart/items/:id               → Remove from cart
POST   /api/v1/checkout                     → Create checkout session
POST   /api/v1/orders                       → Place order
GET    /api/v1/orders/:id                   → Order status + tracking
GET    /api/v1/recommendations              → Personalized recommendations
GET    /api/v1/inventory/:sku               → Real-time stock levels
```

**Distinctive Patterns:**
- Dynamic pricing: watch for price changes between requests or location-based pricing (different prices per region)
- Inventory checks: real-time stock API calls, often via WebSocket for "X people viewing" or "only 3 left"
- Cart sessions: token-based or cookie-based cart persistence
- Search: often powered by Algolia, Elasticsearch, or Meilisearch (visible in network calls)
- CDN patterns: product images served from dedicated CDN with transformation params (width, height, quality)

**Intelligence Value:**
- Product data model reveals what they track (variants, metadata, custom fields)
- Search facets reveal product taxonomy
- Recommendation API reveals ML/AI investment
- Checkout flow reveals payment integrations and upsell strategy

---

### SaaS / B2B Platforms

SaaS products tend to have the most sophisticated APIs due to multi-tenancy, role-based access, and integration needs.

**Common Endpoints:**
```
POST   /api/v1/auth/login                   → Authentication
POST   /api/v1/auth/refresh                 → Token refresh
GET    /api/v1/me                           → Current user profile
GET    /api/v1/organizations/:id            → Organization/workspace
GET    /api/v1/organizations/:id/members    → Team members
POST   /api/v1/invitations                  → Invite team member
GET    /api/v1/projects                     → List projects/workspaces
POST   /api/v1/projects                     → Create project
GET    /api/v1/projects/:id/resources       → Domain-specific resources
GET    /api/v1/activity                     → Activity/audit log
GET    /api/v1/notifications                → User notifications
GET    /api/v1/billing/subscription         → Current plan details
POST   /api/v1/billing/checkout             → Upgrade/change plan
GET    /api/v1/integrations                 → Connected integrations
POST   /api/v1/webhooks                     → Webhook configuration
GET    /api/v1/api-keys                     → API key management
```

**Distinctive Patterns:**
- Multi-tenancy: organization ID in path or header (`X-Org-Id`)
- RBAC: permission errors reveal role hierarchy
- Audit logging: activity endpoints show what they track
- Feature flags: sometimes visible in user/org config response (e.g., `features: ["beta_ai", "advanced_analytics"]`)
- Usage metering: endpoints for tracking API calls, storage, seats

**Intelligence Value:**
- Feature flags reveal upcoming features and A/B tests
- Permission model reveals target customer complexity (simple team vs. enterprise)
- Billing API reveals pricing architecture and self-serve vs. sales-led
- Integration endpoints reveal ecosystem strategy

---

### Social Media / Community Platforms

Social platforms expose rich content and interaction APIs, often with aggressive rate limiting.

**Common Endpoints:**
```
GET    /api/v1/feed                         → Personalized feed (algorithmic)
GET    /api/v1/feed/chronological            → Chronological feed
GET    /api/v1/posts                        → User's posts
POST   /api/v1/posts                        → Create post
GET    /api/v1/posts/:id                    → Single post with comments
POST   /api/v1/posts/:id/like              → Like/react
POST   /api/v1/posts/:id/comments          → Comment on post
GET    /api/v1/users/:id                    → User profile
GET    /api/v1/users/:id/followers          → Follower list
POST   /api/v1/users/:id/follow            → Follow user
GET    /api/v1/notifications                → Notification stream
GET    /api/v1/messages                     → Direct messages
POST   /api/v1/messages                     → Send message
GET    /api/v1/trending                     → Trending topics/content
GET    /api/v1/search                       → Universal search (users, posts, tags)
POST   /api/v1/media/upload                 → Media upload (image, video)
```

**Distinctive Patterns:**
- Feed algorithms: multiple feed endpoints (ranked vs. chronological) reveal algorithm investment
- Real-time: heavy WebSocket usage for notifications, typing indicators, presence
- Media pipeline: dedicated upload endpoints with progress callbacks
- Rate limiting: aggressive per-endpoint limits, often with different tiers
- Engagement tracking: hidden analytics calls on every scroll/view/tap

**Intelligence Value:**
- Feed endpoints reveal algorithm sophistication
- Engagement tracking reveals what metrics they optimize for
- Media pipeline reveals infrastructure investment
- Social graph API complexity reveals network effects strategy

---

### Fintech / Financial Services

Financial APIs are security-heavy with strict authentication and compliance requirements.

**Common Endpoints:**
```
POST   /api/v1/auth/login                   → Login with MFA
POST   /api/v1/auth/mfa/verify             → MFA verification
GET    /api/v1/accounts                     → List financial accounts
GET    /api/v1/accounts/:id/balance         → Account balance
GET    /api/v1/accounts/:id/transactions    → Transaction history
POST   /api/v1/transfers                    → Initiate transfer
GET    /api/v1/transfers/:id/status         → Transfer status
GET    /api/v1/cards                        → Payment cards
POST   /api/v1/cards/:id/freeze             → Freeze/unfreeze card
GET    /api/v1/statements                   → Monthly statements
GET    /api/v1/analytics/spending           → Spending analytics
GET    /api/v1/exchange-rates               → Currency rates
POST   /api/v1/payments                     → Make payment
GET    /api/v1/beneficiaries                → Saved recipients
```

**Distinctive Patterns:**
- Multi-factor auth: watch for MFA challenge-response flows
- Idempotency: `Idempotency-Key` header on write operations (prevents duplicate transactions)
- Signed requests: HMAC signatures on sensitive operations
- Compliance headers: `X-Request-ID` for audit trails
- Real-time: WebSocket for live balance updates and transaction notifications
- Versioning: strict versioning with deprecation headers

**Intelligence Value:**
- Auth flow complexity reveals security maturity
- Transaction API reveals supported payment rails
- Analytics endpoints reveal data science investment
- Real-time capabilities reveal infrastructure sophistication

---

## GraphQL Detection & Introspection

### Identifying GraphQL Endpoints

**URL patterns to look for:**
```
/graphql
/api/graphql
/gql
/query
/v1/graphql
```

**Request signatures:**
- Method: always POST (sometimes GET for queries)
- Content-Type: `application/json`
- Body always contains `query` field (string) and optionally `variables` (object) and `operationName` (string)

**Response signatures:**
- Always contains `data` field at root
- Errors in `errors` array (can coexist with `data`)
- No HTTP status codes for business errors (everything returns 200 with errors in body)

### Introspection Techniques

**Full schema introspection query:**
```graphql
{
  __schema {
    types {
      name
      kind
      fields {
        name
        type {
          name
          kind
          ofType {
            name
            kind
          }
        }
        args {
          name
          type {
            name
          }
        }
      }
    }
    queryType { name }
    mutationType { name }
    subscriptionType { name }
  }
}
```

**Lightweight type list (start here):**
```graphql
{
  __schema {
    types {
      name
      kind
    }
  }
}
```

Filter out internal types (those starting with `__`). The remaining types reveal the data model.

**Query discovery:**
```graphql
{
  __schema {
    queryType {
      fields {
        name
        description
        args { name type { name } }
      }
    }
  }
}
```

**Mutation discovery:**
```graphql
{
  __schema {
    mutationType {
      fields {
        name
        description
        args { name type { name } }
      }
    }
  }
}
```

**When introspection is disabled:**
Some production APIs disable introspection. Alternatives:
- Look for GraphQL error messages that leak type names
- Check for publicly available schema files (`.graphql` or `schema.json`)
- Use field suggestion errors: query a wrong field name and the error may suggest valid fields
- Check the JS bundle — GraphQL queries are often embedded as template literals
- Look for Apollo Client DevTools data in `window.__APOLLO_CLIENT__`

### GraphQL Intelligence Analysis

What the schema reveals:
- **Type count** — More types = more complex data model = more mature product
- **Mutation names** — Direct map to user actions (createProject, sendMessage, upgradePlan)
- **Subscription types** — Reveal real-time capabilities
- **Enum values** — Reveal valid states, categories, and business rules (e.g., `OrderStatus: PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELLED`)
- **Input types** — Reveal what parameters each action accepts
- **Connection types** — Relay-style pagination indicates modern architecture
- **Deprecated fields** — Show evolution and what's being phased out

---

## WebSocket Patterns & Use Cases

### Common WebSocket Implementations

**Raw WebSocket:**
```
URL: wss://ws.target.com/stream
Messages: Custom JSON format
Handshake: Standard WebSocket upgrade
```

**Socket.IO:**
```
URL: wss://target.com/socket.io/?EIO=4&transport=websocket
Messages: Prefixed with packet type (0=open, 2=ping, 3=pong, 4=message, 42=event)
Detection: Look for /socket.io/ in URL
Example message: 42["event_name",{"data":"value"}]
```

**SignalR:**
```
URL: wss://target.com/hub?id=...
Messages: JSON with invocationId, target, arguments
Detection: /hub or /signalr in URL, negotiate endpoint
```

**ActionCable (Rails):**
```
URL: wss://target.com/cable
Messages: {"command":"subscribe","identifier":"{\"channel\":\"ChatChannel\"}"}
Detection: /cable in URL
```

**Phoenix Channels (Elixir):**
```
URL: wss://target.com/socket/websocket?token=...
Messages: ["join_ref","ref","topic","event",payload]
Detection: /socket/websocket in URL, array-formatted messages
```

### WebSocket Use Cases by Feature

| Feature | Message Pattern | Frequency | Intelligence Value |
|---------|---------------|-----------|-------------------|
| Chat / Messaging | User-to-user messages, typing indicators | Per interaction | Core product investment |
| Notifications | Push alerts, badges | Per event | Engagement strategy |
| Live Feeds | New posts, comments, reactions | 1-10/sec | Real-time infrastructure |
| Collaborative Editing | Document operations (OT/CRDT) | 10-100/sec | Deep tech investment |
| Real-time Dashboard | Metric updates | 1-5/sec | Analytics capabilities |
| Live Pricing | Price ticker updates | 0.1-10/sec | Pricing engine complexity |
| Presence | Online/offline status | Every 15-30s | Social features maturity |
| Gaming / Interactive | State updates | 10-60/sec (tick rate) | Performance requirements |
| IoT / Monitoring | Sensor data, alerts | Varies | Device ecosystem size |

### Message Pattern Analysis

When monitoring WebSocket messages, classify each message:

```
MESSAGE ANALYSIS TEMPLATE:

Direction: client → server | server → client | bidirectional
Type: command | event | query | response | heartbeat | error
Encoding: JSON | binary | text | MessagePack
Size: tiny (<100B) | small (<1KB) | medium (<10KB) | large (>10KB)
Frequency: burst | periodic (interval) | on-demand | continuous stream
Auth: per-message | connection-level | none visible
Schema: consistent (typed) | variable (dynamic) | mixed
```

---

## Authentication Flow Patterns

### JWT (JSON Web Token) Flow

```
1. User submits credentials
   POST /api/auth/login {email, password}

2. Server returns token pair
   Response: {access_token: "eyJ...", refresh_token: "eyJ...", expires_in: 3600}

3. Client stores tokens
   Location: localStorage | sessionStorage | httpOnly cookie | in-memory

4. Client sends access token with each request
   Header: Authorization: Bearer eyJhbGciOiJSUzI1NiIs...

5. When access token expires, use refresh token
   POST /api/auth/refresh {refresh_token: "eyJ..."}

6. Server returns new token pair
   Response: {access_token: "new_eyJ...", refresh_token: "new_eyJ...", expires_in: 3600}
```

**JWT Decoding Intelligence:**
Decode the JWT payload (it's just Base64) to extract:
- `sub` — user ID format (UUID, integer, custom)
- `iss` — issuer (often reveals auth service: Auth0, Firebase, Cognito)
- `exp` — expiration time (security posture indicator)
- `aud` — audience (may reveal internal service names)
- `roles` / `permissions` — RBAC model
- Custom claims — feature flags, org ID, plan tier

### OAuth 2.0 Authorization Code Flow

```
1. App redirects user to provider
   GET https://provider.com/oauth/authorize
     ?client_id=abc123
     &redirect_uri=https://app.com/callback
     &response_type=code
     &scope=read+write
     &state=random_csrf_token

2. User authenticates at provider

3. Provider redirects back with authorization code
   GET https://app.com/callback?code=AUTH_CODE&state=random_csrf_token

4. App exchanges code for tokens (server-side)
   POST https://provider.com/oauth/token
     {grant_type: "authorization_code", code: "AUTH_CODE", redirect_uri: "...", client_id: "...", client_secret: "..."}

5. Provider returns access token
   Response: {access_token: "...", token_type: "Bearer", expires_in: 3600, refresh_token: "..."}
```

**Intelligence from OAuth:**
- `client_id` in frontend code reveals provider (Google, GitHub, Facebook, etc.)
- Requested `scope` reveals what data they access from the provider
- Multiple OAuth providers listed = broad social login support

### API Key Patterns

```
Header-based:
  X-API-Key: sk_live_EXAMPLE_KEY_REPLACE_ME
  Authorization: Api-Key abc123

Query param (less secure):
  GET /api/data?api_key=abc123

Prefix conventions (reveal provider):
  sk_live_ / sk_test_   → Stripe
  pk_live_ / pk_test_   → Stripe (publishable)
  AIza...               → Google
  AKIA...               → AWS
  ghp_                  → GitHub
  xoxb-                 → Slack Bot
  Bearer sk-...         → OpenAI
```

### Session Cookie Patterns

```
Set-Cookie: session=abc123; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=86400

Analysis:
- HttpOnly → Not accessible from JavaScript (good security)
- Secure → Only sent over HTTPS
- SameSite=Strict → CSRF protection
- Max-Age / Expires → Session duration
- Domain → Scope of the session
- Cookie name → Often reveals framework:
    - JSESSIONID → Java (Tomcat, Spring)
    - PHPSESSID → PHP
    - _session_id → Ruby on Rails
    - connect.sid → Express.js
    - csrftoken → Django
    - laravel_session → Laravel
```

---

## API Versioning Schemes

### URL Path Versioning
```
/api/v1/resources
/api/v2/resources
```
Most common. Easy to discover. Multiple versions running simultaneously indicates migration period.

### Header Versioning
```
Accept: application/vnd.company.v2+json
X-API-Version: 2
Api-Version: 2024-01-15
```
Harder to discover but more elegant. Date-based versions (Stripe style) indicate continuous evolution.

### Query Parameter Versioning
```
/api/resources?version=2
```
Less common. Easy to discover.

### What Versioning Reveals:
- **v1 only** — Young API, possibly unstable
- **v1 + v2** — Active development, migration period, growing product
- **v1 + v2 + v3+** — Mature API, long-running product, backwards compatibility commitment
- **Date-based** — Sophisticated API team (likely inspired by Stripe)
- **No versioning** — Either very simple API or poor API practices

---

## Rate Limiting Strategies & Detection

### Common Rate Limit Headers

```
X-RateLimit-Limit: 100          → Max requests per window
X-RateLimit-Remaining: 95       → Requests remaining
X-RateLimit-Reset: 1640000000   → Unix timestamp when window resets
Retry-After: 30                 → Seconds to wait (on 429 response)

# GitHub style
X-RateLimit-Resource: core      → Which resource pool is being used

# Cloudflare style
CF-Cache-Status: DYNAMIC        → Not cached (hits origin)
```

### Rate Limiting Strategies (what they reveal)

| Strategy | Detection | Implication |
|----------|-----------|-------------|
| Fixed window | Consistent reset times | Simple implementation |
| Sliding window | Variable remaining counts | More sophisticated |
| Token bucket | Burst allowed, then steady | Optimized for user experience |
| Per-endpoint limits | Different limits per path | Granular control, mature API |
| Per-user tier | Limits change with plan | Monetized API access |
| IP-based | Same limits without auth | Basic protection |
| Adaptive | Limits change under load | Advanced infrastructure |

### Testing Rate Limits Safely

To detect rate limits without causing issues:
1. Make 5 requests over 10 seconds — note rate limit headers
2. Calculate the limit from headers (don't need to hit it)
3. If no headers, make requests gradually increasing frequency
4. Stop at first sign of throttling (429 or degraded responses)
5. Document the apparent threshold and window size

---

## CORS & Security Header Analysis

### CORS Headers

```
# Permissive (callable from any origin)
Access-Control-Allow-Origin: *

# Restricted (only callable from specific origins)
Access-Control-Allow-Origin: https://app.target.com

# Dynamic (reflects request origin — potential misconfiguration)
Access-Control-Allow-Origin: [varies per request]

# Methods allowed
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS

# Custom headers allowed
Access-Control-Allow-Headers: Authorization, Content-Type, X-Custom-Header

# Credentials allowed (cookies, auth headers)
Access-Control-Allow-Credentials: true

# Preflight cache duration
Access-Control-Max-Age: 86400
```

**What CORS reveals:**
- `*` origin — Public API, callable from any website
- Specific origin — Private API, only their frontend should call it
- Credentials: true — API uses cookies or auth headers
- Many allowed methods — Full CRUD API
- Custom headers — Internal header conventions

### Security Headers Analysis

```
# Content Security Policy — reveals trusted sources
Content-Security-Policy: default-src 'self'; script-src 'self' cdn.target.com; connect-src api.target.com wss://ws.target.com

# From CSP you can extract:
# - API domains (connect-src)
# - CDN domains (script-src, img-src)
# - WebSocket URLs (connect-src wss://)
# - Third-party services (analytics, payments)

# Strict Transport Security
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

# Frame protection
X-Frame-Options: DENY

# Content type enforcement
X-Content-Type-Options: nosniff

# Referrer policy
Referrer-Policy: strict-origin-when-cross-origin
```

**CSP is a goldmine for API discovery.** The `connect-src` directive explicitly lists every domain the frontend is allowed to make requests to — including API servers, WebSocket servers, analytics endpoints, and third-party services.

### Server Identification

```
# Server header
Server: nginx/1.21.0    → Infrastructure choice
Server: cloudflare      → Using Cloudflare
Server: AmazonS3        → Static hosting on S3
Server: gunicorn         → Python (Django/Flask/FastAPI)
Server: Cowboy           → Elixir/Erlang (Phoenix)

# Technology markers
X-Powered-By: Express   → Node.js
X-Powered-By: PHP/8.1   → PHP
X-Runtime: 0.042         → Ruby on Rails
X-Request-Id: uuid       → Good observability practice

# CDN / Proxy indicators
CF-RAY: abc123-SJC       → Cloudflare (SJC = San Jose)
X-Cache: HIT             → CDN cache hit
X-Served-By: cache-sjc   → Fastly / Varnish
Via: 1.1 vegur           → Heroku
```

---

## API Response Anti-Patterns (Red Flags)

Things that indicate poor API design (potential competitive weakness):

| Anti-Pattern | Detection | Implication |
|-------------|-----------|-------------|
| Over-fetching | Response 10x larger than what UI displays | Wasted bandwidth, lazy backend |
| N+1 queries | UI makes dozens of sequential requests | Poor API design, slow UX |
| No pagination | Single request returns all data | Won't scale |
| Sequential IDs | Resource IDs are 1, 2, 3... | Security risk (enumerable) |
| Verbose errors | Stack traces in production responses | Security risk, immature ops |
| Mixed auth | Some endpoints need auth, similar ones don't | Inconsistent security model |
| No versioning | Breaking changes without version bump | Unstable for integrators |
| Hardcoded secrets | API keys visible in frontend JS bundle | Critical security issue |
| No rate limiting | No throttle on any endpoint | Vulnerable to abuse |
| Inconsistent naming | Mix of camelCase, snake_case, kebab-case | Multiple teams, no standards |

---

## Quick Reference: Tech Stack Detection from API Patterns

| Pattern | Likely Stack |
|---------|-------------|
| `/wp-json/wp/v2/` | WordPress |
| `/api/v1/` + `X-Request-Id` + snake_case | Ruby on Rails |
| `/_next/data/` + `__NEXT_DATA__` | Next.js |
| `/graphql` + Relay connection types | Facebook-style (React + Relay) |
| `/rest/api/2/` + `JSESSIONID` | Atlassian (Jira, Confluence) |
| `/api/` + `csrftoken` cookie | Django |
| `/api/` + `connect.sid` cookie | Express.js |
| `/api/` + `laravel_session` cookie | Laravel |
| `Fly-Request-Id` header | Deployed on Fly.io |
| `X-Vercel-Id` header | Deployed on Vercel |
| `/supabase/` or `supabase.co` | Supabase backend |
| `/rest/v1/` + `apikey` header | Supabase PostgREST |
| `firebaseio.com` | Firebase |
| `.appspot.com` | Google App Engine |
| `herokuapp.com` | Heroku |
