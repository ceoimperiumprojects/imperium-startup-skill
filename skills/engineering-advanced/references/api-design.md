# API Design Best Practices

## REST API Rules

### Resource Naming
- Use nouns: `/users`, `/orders`, `/products`
- NOT verbs: ~~`/getUsers`~~, ~~`/createOrder`~~
- Plural nouns for collections: `/users` not `/user`
- Nested resources for relationships: `/users/{id}/orders`
- Max 2 levels deep: `/users/{id}/orders` (not `/users/{id}/orders/{id}/items/{id}/details`)

### HTTP Methods
| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| GET | Read resource(s) | Yes | Yes |
| POST | Create resource | No | No |
| PUT | Replace resource entirely | Yes | No |
| PATCH | Update resource partially | No | No |
| DELETE | Remove resource | Yes | No |

### Status Codes
| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | Valid auth, insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate resource, state conflict |
| 422 | Unprocessable | Valid syntax, invalid semantics |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Error | Server-side failure |

### Pagination
**Cursor-based (recommended for real-time):**
```json
{
  "data": [...],
  "meta": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

**Offset-based (for static data):**
```json
{
  "data": [...],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 150
  }
}
```

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      { "field": "email", "issue": "missing" }
    ]
  }
}
```

### Versioning
- URL path: `/v1/users` (most common, easiest)
- Header: `Accept: application/vnd.api+json;version=1`
- Query param: `/users?version=1` (least recommended)

### Authentication
- API keys for server-to-server
- OAuth 2.0 for user-facing applications
- JWT for stateless auth (short expiry + refresh token)

### Rate Limiting
- Return `429` with `Retry-After` header
- Include rate limit headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`
- Per-user and per-IP limits
- Document limits clearly

## GraphQL Considerations

### When GraphQL Over REST
- Multiple related resources needed in one request
- Clients with varied data needs (mobile vs web)
- Rapidly evolving API (no versioning needed)
- Real-time subscriptions needed

### When REST Over GraphQL
- Simple CRUD APIs
- File uploads
- Caching (REST caching is simpler)
- Team unfamiliar with GraphQL
