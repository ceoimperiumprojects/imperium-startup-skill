---
name: legal
description: 'Startup legal guidance and compliance frameworks. Use when the user mentions contracts, terms of service, privacy policy, entity structure, incorporation, IP protection, NDAs, employment agreements, equity, vesting, GDPR, compliance, regulatory, legal risk, licensing, or any legal topic for startups. Also triggers on: legal, lawyer, law, LLC, C-corp, Delaware, trademark, patent, copyright, data protection, CCPA, terms, agreement, contract review.'
user-invocable: false
---

# Legal

Legal frameworks for startup founders. Not legal advice — frameworks to understand what you need and when to get a real lawyer.

**IMPORTANT DISCLAIMER:** This skill provides general frameworks and checklists. It is NOT a substitute for qualified legal counsel. Always consult a lawyer for your specific situation.

## Keywords

Legal, contracts, terms of service, privacy policy, entity structure, incorporation, IP, NDA, employment agreement, equity, vesting, GDPR, compliance, regulatory, licensing, LLC, C-corp, Delaware, trademark, patent, copyright, data protection, CCPA

## Core Domains

### 1. Entity Structure

**When to incorporate:**
- Before accepting money from anyone
- Before hiring anyone (including contractors)
- Before launching commercially

**Entity comparison:**

| Factor | LLC | C-Corp (Delaware) | S-Corp |
|--------|-----|-------------------|--------|
| Fundraising | Hard (VCs don't invest in LLCs) | Standard for VC | Not VC-compatible |
| Taxes | Pass-through | Double taxation | Pass-through |
| Equity | Complex membership units | Simple stock | Limited shareholders |
| Best for | Lifestyle business, consulting | VC-backed startup | Small profitable business |

**Default recommendation for VC-track startups:** Delaware C-Corp.

**Why Delaware?**
- Most VCs require it
- Well-established corporate law
- Chancery Court specializes in business disputes
- Standard templates (NVCA) assume Delaware

### 2. Contracts & Agreements

**Essential contracts by stage:**

| Stage | Must Have | Should Have |
|-------|----------|-------------|
| Pre-seed | Co-founder agreement, IP assignment | NDA template |
| Seed | + Employment agreements, contractor agreements | + Advisor agreements (FAST) |
| Revenue | + Terms of Service, Privacy Policy, DPA | + MSA, SLA |
| Series A+ | + Stock option plan, board consents | + ROFR, D&O insurance |

**Co-founder agreement must include:**
- Equity split and vesting schedule (4 years, 1 year cliff standard)
- Roles and responsibilities
- IP assignment to company
- What happens if someone leaves
- Decision-making process (voting, deadlocks)
- Non-compete and non-solicitation

**Contractor vs Employee:**

| Factor | Employee | Contractor |
|--------|----------|------------|
| Control | You control how/when they work | They control how/when |
| Equipment | You provide | They provide |
| Exclusivity | Usually exclusive | Can work for others |
| Benefits | Required | Not required |
| Tax | You withhold | They pay self-employment |
| IP | Usually work-for-hire | Must have IP assignment |
| Risk | Misclassification is expensive | |

### 3. IP Protection

**IP types for startups:**

| Type | What It Protects | Cost | Timeline |
|------|-----------------|------|----------|
| Trademark | Brand name, logo | $250-1500 | 6-12 months |
| Copyright | Code, content, designs | Free (automatic) | Immediate |
| Patent | Inventions, processes | $5K-15K+ | 2-4 years |
| Trade secret | Proprietary info, algorithms | $0 (process cost) | Ongoing |

**IP assignment is critical:**
- Every founder must assign IP to the company
- Every employee must sign an invention assignment agreement
- Every contractor must have an IP assignment clause
- If you skip this, you don't own your own product

### 4. Compliance & Data Protection

**GDPR essentials (if you have EU users):**
- Lawful basis for processing (consent, contract, legitimate interest)
- Privacy policy explaining what/why/how you process data
- Data processing agreements with all vendors
- Right to access, rectify, delete (user requests)
- Data breach notification (72 hours)
- Data Protection Officer (if processing at scale)

**CCPA essentials (if you have California users):**
- Right to know what data you collect
- Right to delete
- Right to opt out of sale
- Updated privacy policy with CCPA disclosures

**General compliance checklist:**
- [ ] Privacy policy published and current
- [ ] Terms of service published and current
- [ ] Cookie consent mechanism (EU)
- [ ] Data processing agreements with vendors
- [ ] Data retention policy defined
- [ ] Security incident response plan
- [ ] Regular security reviews

### 5. Equity & Compensation

**Standard vesting:**
- 4-year vesting, 1-year cliff
- Monthly vesting after cliff
- Single trigger acceleration (sometimes)
- Double trigger acceleration (sometimes for founders)

**Option pool:**
- Typical: 10-20% of fully diluted shares
- Created pre-money in fundraising (dilutes founders, not investors)
- 409A valuation needed for strike price
- ISO vs NSO: ISOs are tax-advantaged for employees

**Advisor equity (FAST agreement):**
| Involvement | Standard | Strategic | Expert |
|-------------|----------|-----------|--------|
| Idea stage | 0.25% | 0.5% | 1.0% |
| Development | 0.15% | 0.35% | 0.6% |
| Revenue | 0.10% | 0.25% | 0.5% |

2-year vesting, no cliff is standard for advisors.

## When to Get a Lawyer

- **Always:** Fundraising (term sheet review, closing docs)
- **Always:** Hiring first employees (employment law varies by state/country)
- **Always:** If someone threatens legal action
- **Probably:** Before launching (ToS, Privacy Policy review)
- **Probably:** International expansion (local law varies significantly)
- **Maybe:** Standard contractor agreements (templates often sufficient)

## Reference Files

- `references/contracts.md` — Contract templates, negotiation frameworks, red flags
- `references/entity-structure.md` — Incorporation guides, entity comparison, Delaware process
- `references/compliance.md` — GDPR, CCPA, data protection, security compliance
