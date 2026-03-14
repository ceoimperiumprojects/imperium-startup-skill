---
name: finance
description: 'Startup financial management and analysis. Use when the user mentions financial modeling, SaaS metrics, unit economics, burn rate, runway, fundraising financials, investor reporting, cap table, dilution, cash management, budgeting, pricing analysis, revenue forecasting, or any startup finance topic. Also triggers on: CFO, MRR, ARR, CAC, LTV, churn rate, NRR, gross margin, burn multiple, Rule of 40, Magic Number, term sheet, valuation, FP&A, P&L, cash flow.'
user-invocable: false
---

# Finance

Strategic financial frameworks for startup CFOs and founders. Numbers-driven, decisions-focused. Not financial analysis for its own sake — models that drive decisions, fundraises that don't kill the company, board packages that earn trust.

## Keywords

CFO, finance, financial model, burn rate, runway, unit economics, LTV, CAC, fundraising, Series A, Series B, term sheet, cap table, dilution, cash flow, board financials, FP&A, SaaS metrics, ARR, MRR, net dollar retention, gross margin, scenario planning, cash management, burn multiple, Rule of 40, Magic Number, ARPU, payback period, churn, revenue, P&L

## Key Questions (Ask These First)

- **What's your burn multiple?** (Net burn ÷ Net new ARR. >2x is a problem.)
- **If fundraising takes 6 months instead of 3, do you survive?**
- **Show me unit economics per cohort, not blended.** (Blended hides deterioration.)
- **What's your NDR?** (>100% means you grow without signing a single new customer.)
- **What are your decision triggers?** (At what runway do you start cutting?)

## Core Domains

### 1. Financial Modeling

Build bottoms-up models, not top-down fantasies.

**Three-statement model:** P&L → Balance Sheet → Cash Flow
**Headcount cost model:** Loaded cost per role × hiring plan × timeline
**Revenue model:** Customers × ARPU × retention × expansion

**Projection principles:**
- Bottom-up: # customers × ARPU, not "if we get 1% of TAM"
- Three scenarios: Bear / Base / Bull (with clear assumptions for each)
- Monthly granularity for first 18 months, quarterly after
- Every assumption must be labeled and justifiable

### 2. SaaS Metrics & Unit Economics

**Revenue Metrics:**

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| MRR | Sum of monthly recurring revenue | Growing MoM |
| ARR | MRR × 12 | >2x YoY at Series A/B |
| ARPU | MRR / # customers | Stable or growing |
| MoM Growth | (This month - Last month) / Last month | >15% early stage |
| Net New MRR | New + Expansion - Contraction - Churn | Positive |
| Quick Ratio | (New + Expansion) / (Contraction + Churn) | >4 excellent, >2 good |

**Unit Economics:**

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| CAC | Total S&M spend / New customers | Declining over time |
| LTV | ARPU × Gross Margin / Monthly Churn Rate | >3x CAC |
| LTV:CAC | LTV / CAC | >3:1 |
| Payback Period | CAC / (ARPU × Gross Margin) | <12 months SaaS |
| Gross Margin | (Revenue - COGS) / Revenue | >70% SaaS |

**Retention Metrics:**

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| Logo Churn | Customers lost / Starting customers | <5% monthly |
| Revenue Churn | MRR lost / Starting MRR | <3% monthly |
| Net Revenue Retention | (Start MRR + Expansion - Contraction - Churn) / Start MRR | >100% good, >120% great |

**Capital Efficiency:**

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| Burn Rate | Monthly cash outflow | Track trend |
| Runway | Cash / Monthly Burn | >12 months |
| Burn Multiple | Net Burn / Net New ARR | <1.5x excellent, <2x good |
| Rule of 40 | Revenue Growth % + Profit Margin % | >40% |
| Magic Number | (QoQ Revenue Change × 4) / Last Q S&M Spend | >1.0 efficient |
| Revenue per FTE | ARR / # employees | Track trend |

### 3. Fundraising Finance

**Valuation models:**
- DCF (Discounted Cash Flow) — for later stage
- Revenue multiples — most common for SaaS
- Precedent transactions — comparable deals
- Venture method — target return backward calculation

**Term sheet essentials:**
- Valuation (pre-money vs post-money)
- Liquidation preference (1x non-participating is standard)
- Board composition and protective provisions
- Pro-rata rights and anti-dilution
- Option pool (negotiate pre-money inclusion)

**Data room contents:** See `references/investor-reporting.md`

### 4. Cash Management

**Runway extension tactics (non-dilutive):**
- Negotiate longer payment terms with vendors
- Collect revenue upfront (annual billing discounts)
- Cut discretionary spending (conferences, perks, unused tools)
- Defer non-essential hires
- Revenue-based financing or venture debt

**Decision triggers:**
- 12+ months runway: Business as usual
- 9-12 months: Start fundraising prep
- 6-9 months: Active fundraising, hiring freeze
- <6 months: Emergency mode — cut to extend

### 5. Business Health Diagnostic

Four dimensions to evaluate:

**Growth & Retention:** MRR growth, NRR, churn trends
**Unit Economics:** CAC, LTV, payback, margins
**Capital Efficiency:** Burn multiple, Rule of 40, Magic Number
**Strategic Position:** Market share, competitive dynamics, PMF signals

Rate each: 🟢 Healthy | 🟡 Watch | 🔴 Action Required

## Red Flags

- Burn multiple rising while growth slows
- Gross margin declining MoM
- NDR < 100% (revenue shrinks without new churn)
- Cash runway < 9 months with no fundraise in process
- LTV:CAC declining across successive cohorts
- Single customer > 20% of ARR (concentration risk)
- Blended metrics hiding per-cohort deterioration

## Reference Files

- `references/financial-modeling.md` — Three-statement models, projections, budgeting
- `references/saas-metrics.md` — Complete SaaS metrics guide with calculations
- `references/investor-reporting.md` — Board financial packages, investor updates, data room

## Scripts

- `scripts/saas_metrics_calculator.py` — Calculate all SaaS metrics from input data
- `scripts/financial_model.py` — Generate financial projections with scenarios
