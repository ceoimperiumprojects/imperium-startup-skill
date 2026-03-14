# Outbound Infrastructure

## Email Deliverability Setup

### Domain Setup
- [ ] Buy a separate sending domain (not your main domain)
  - Pattern: `try[company].com`, `get[company].com`, `[company]mail.com`
- [ ] Set up SPF record
- [ ] Set up DKIM (1024 or 2048 bit)
- [ ] Set up DMARC (start with `p=none`, move to `p=quarantine`)
- [ ] Add MX records
- [ ] Set up Google Workspace or Microsoft 365 on sending domain

### Domain Warming
- Week 1: 5-10 emails/day (personal conversations)
- Week 2: 15-25 emails/day (mix of personal + cold)
- Week 3: 30-50 emails/day
- Week 4+: 50-100 emails/day per mailbox (max)
- Use a warming service (Instantly, Warmbox)

### Sending Best Practices
- Max 50-100 emails per mailbox per day
- Spread sends throughout the day (not all at once)
- Use 3-5 mailboxes for rotation
- Remove bounces immediately
- Monitor spam complaints (<0.1%)
- Track inbox placement rate

### List Hygiene
- Verify all emails before sending (NeverBounce, ZeroBounce)
- Remove catch-all domains (higher bounce risk)
- Remove role-based emails (info@, support@, sales@)
- Remove unengaged after 4 sends with no open
- Re-verify lists older than 90 days

## Tech Stack Recommendations

### Prospecting & Enrichment
| Tool | Best For | Price Range |
|------|----------|-------------|
| Apollo | All-in-one prospecting + enrichment | $49-119/mo |
| LinkedIn Sales Navigator | Decision-maker research | $80-130/mo |
| Clay | Data enrichment + automation | $149-349/mo |
| Clearbit | Real-time enrichment | Custom pricing |

### Sequencing & Sending
| Tool | Best For | Price Range |
|------|----------|-------------|
| Instantly | High-volume cold email | $30-78/mo |
| Smartlead | Multi-mailbox rotation | $39-94/mo |
| Lemlist | Personalized images/video | $39-69/mo |
| Outreach | Enterprise sales engagement | Custom |

### CRM
| Tool | Best For | Price Range |
|------|----------|-------------|
| HubSpot (Free) | Early stage, all-in-one | Free-$45/mo |
| Pipedrive | Visual pipeline management | $15-49/mo |
| Salesforce | Enterprise, customizable | $25-300/mo |
| Close | Inside sales teams | $29-149/mo |

## Metrics to Track

| Metric | Target | Red Flag |
|--------|--------|----------|
| Deliverability rate | >95% | <90% |
| Open rate | >50% | <30% |
| Reply rate (total) | >5% | <2% |
| Positive reply rate | >2% | <0.5% |
| Bounce rate | <3% | >5% |
| Spam complaint rate | <0.1% | >0.3% |
| Meeting booking rate | >2% | <0.5% |
