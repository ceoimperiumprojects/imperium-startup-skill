# Complete SaaS Metrics Guide

## Revenue Metrics

### MRR (Monthly Recurring Revenue)
**Formula:** Sum of all monthly subscription revenue
**Components:**
- New MRR: Revenue from new customers
- Expansion MRR: Revenue from upgrades/upsells
- Contraction MRR: Revenue lost from downgrades
- Churned MRR: Revenue lost from cancellations
- **Net New MRR = New + Expansion - Contraction - Churned**

### ARR (Annual Recurring Revenue)
**Formula:** MRR × 12
**Note:** Only use for annual/multi-year contracts. Don't annualize monthly revenue if most contracts are monthly.

### ARPU (Average Revenue Per User)
**Formula:** MRR / Total active customers
**Best practice:** Track by segment (SMB vs Enterprise), by cohort (sign-up month), by plan tier.

### Quick Ratio
**Formula:** (New MRR + Expansion MRR) / (Contraction MRR + Churned MRR)
**Interpretation:**
- >4.0: Excellent — growing fast with low churn
- 2.0-4.0: Good — healthy growth
- 1.0-2.0: Concerning — growth is fragile
- <1.0: Shrinking — revenue is declining

## Unit Economics

### CAC (Customer Acquisition Cost)
**Formula:** Total Sales & Marketing Spend / New Customers Acquired
**Variations:**
- Blended CAC: All S&M / all new customers
- Paid CAC: Paid marketing spend / paid customers only
- Fully loaded CAC: Include salaries, tools, overhead
**Best practice:** Calculate per channel, not just blended.

### LTV (Lifetime Value)
**Formula:** ARPU × Gross Margin % / Monthly Churn Rate
**Alternative:** Average customer lifespan × ARPU × Gross Margin
**Best practice:** Calculate per cohort. Blended LTV hides deterioration.

### LTV:CAC Ratio
**Target:** >3:1
- <1:1: Losing money on every customer
- 1-3:1: Not efficient enough for sustainable growth
- 3-5:1: Healthy
- >5:1: May be under-investing in growth

### CAC Payback Period
**Formula:** CAC / (ARPU × Gross Margin %)
**Target:** <12 months for SaaS
**Interpretation:** How many months to recover the cost of acquiring a customer.

### Gross Margin
**Formula:** (Revenue - COGS) / Revenue × 100
**SaaS benchmark:** >70%
**COGS for SaaS:** Hosting, third-party APIs, customer support, onboarding costs

## Retention Metrics

### Logo Churn (Customer Churn)
**Formula:** Customers lost in period / Customers at start of period
**Monthly benchmark:** <5% (SMB), <2% (Mid-market), <1% (Enterprise)

### Revenue Churn (MRR Churn)
**Formula:** MRR lost in period / MRR at start of period
**Monthly benchmark:** <3%

### Net Revenue Retention (NRR / NDR)
**Formula:** (Starting MRR + Expansion - Contraction - Churn) / Starting MRR × 100
**Benchmarks:**
- >120%: World-class (Snowflake, Twilio)
- 100-120%: Good (growing even without new customers)
- <100%: Revenue shrinks over time (unsustainable)

### Gross Revenue Retention
**Formula:** (Starting MRR - Contraction - Churn) / Starting MRR × 100
**Benchmark:** >85%

## Capital Efficiency

### Burn Rate
- **Gross burn:** Total monthly cash outflow
- **Net burn:** Cash outflow minus cash inflow
- **Formula:** Net burn = Total expenses - Total revenue

### Runway
**Formula:** Cash in bank / Monthly net burn
**Targets:** >18 months (comfortable), >12 months (ok), <9 months (start fundraising), <6 months (emergency)

### Burn Multiple
**Formula:** Net Burn / Net New ARR
**Benchmarks:**
- <1x: Amazing efficiency
- 1-1.5x: Excellent
- 1.5-2x: Good
- 2-3x: Concerning
- >3x: Unsustainable

### Rule of 40
**Formula:** Revenue Growth Rate (%) + Profit Margin (%)
**Benchmark:** >40% (combined growth + profitability should exceed 40)

### Magic Number
**Formula:** (Current Quarter Revenue - Previous Quarter Revenue) × 4 / Previous Quarter S&M Spend
**Benchmarks:**
- >1.0: Efficient — spend more on S&M
- 0.5-1.0: Okay — optimize before scaling
- <0.5: Inefficient — fix unit economics first
