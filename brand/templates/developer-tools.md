# Developer Tools — Brand Voice Template

Technical, direct, no-BS. Code speaks louder than marketing copy. Developers are the most marketing-averse audience on the planet — earn their trust through substance, documentation quality, and genuine technical depth. Zero fluff.

---

## Brand Archetype

**Primary:** Creator
**Secondary:** Sage

The Creator-Sage blend builds brands that developers actually respect. You've built something genuinely well-engineered and you let the work speak for itself. Your brand shows, not tells. A code snippet is worth a thousand marketing words.

---

## Color Palette

| Slot | Hex | Name | Usage |
|------|-----|------|-------|
| Primary | `#3B82F6` | Code Blue | Logo, primary CTAs, links |
| Primary Dark | `#2563EB` | Deep Blue | Hover states, active elements |
| Secondary | `#10B981` | Terminal Green | Success states, CLI output, active status |
| Secondary Dark | `#059669` | Dark Green | Hover states, verified elements |
| Accent | `#F59E0B` | Warning Amber | Deprecation notices, important callouts |
| Accent Alt | `#EF4444` | Error Red | Error states, breaking changes, destructive actions |
| Neutral 900 | `#0F172A` | Terminal Dark | Code blocks, dark UI elements |
| Neutral 500 | `#64748B` | Comment Gray | Secondary text, code comments, borders |
| Neutral 200 | `#E2E8F0` | Line | Dividers, code block borders, table rules |
| Neutral 50 | `#F8FAFC` | Background | Page backgrounds, card surfaces |

**Mode:** Dark mode default (developers live in dark mode). Light mode fully supported.

---

## Typography

| Slot | Font | Fallback |
|------|------|----------|
| Heading | Geist | Inter, system-ui, sans-serif |
| Body | Inter | -apple-system, sans-serif |
| Accent | Geist Mono | JetBrains Mono, Fira Code, monospace |

---

## Voice Settings

```
Formal ←——————————→ Casual
          [5]

Technical ←——————————→ Simple
  [2]

Serious ←——————————→ Playful
      [4]

Reserved ←——————————→ Bold
          [5]
```

**Voice summary:** Our voice is precise, technical, and respectful of the reader's expertise. We sound like a senior engineer writing documentation — clear, concise, opinionated when it matters, and always backed by working code.

---

## Sample Copy

### Tagline
> Build better. Ship faster. Debug less.

### Landing Page Hero
> A type-safe ORM that doesn't make you hate your life. Auto-generated types from your schema, zero runtime overhead, and migrations that actually work. If you've ever rage-quit a query builder, this is for you.
>
> ```bash
> npm install @acme/orm
> npx acme init
> ```
>
> From zero to first query in under 60 seconds. [Read the quickstart →]

### Email Subject
> v3.0: Breaking changes, migration guide, and why it's worth it

### Tweet
> New in v3.0: Connection pooling is now automatic. No config. No tuning. Just works. Cold starts went from 340ms → 12ms. Upgrade guide: [link]. Changelog: [link]. Yes, there are breaking changes. Yes, they're worth it.

### Error Message
> `TypeError: Cannot read property 'id' of undefined at UserModel.findById (user.ts:42)`. The record you're querying doesn't exist. Check that the ID is valid and the record hasn't been deleted. If you're using soft deletes, pass `{ includeSoftDeleted: true }`. [Docs: Querying →]

---

## Writing Rules

1. **Show, don't tell.** A code example beats a paragraph of explanation. Always include runnable code when possible.
2. **Be precise.** "12ms p99 latency" not "blazing fast." "TypeScript 5.0+" not "modern TypeScript." Numbers, versions, specifics.
3. **Respect their time.** Developers skim. Lead with the code, follow with the explanation. Put the `TL;DR` first.
4. **No marketing speak.** "Revolutionary AI-powered platform" makes developers close the tab. Just say what it does and show them the code.
5. **Own your tradeoffs.** Every technical decision has downsides. Acknowledge them upfront. "This adds ~2KB to your bundle. Here's why we think it's worth it."
6. **Changelog is sacred.** Breaking changes clearly marked. Migration paths documented. Deprecation warnings shipped in the version before removal.
7. **Error messages are documentation.** Every error should tell the developer exactly what went wrong, why, and how to fix it. Include the relevant file and line number. Link to docs.
