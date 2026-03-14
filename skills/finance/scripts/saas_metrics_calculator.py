#!/usr/bin/env python3
"""SaaS Metrics Calculator — calculates key SaaS metrics from input data.

Usage:
    python saas_metrics_calculator.py --mrr 50000 --customers 100 --new-customers 15 \\
        --churned-customers 5 --expansion-mrr 3000 --contraction-mrr 1000 \\
        --churned-mrr 2000 --sm-spend 20000 --cash 500000 --monthly-burn 40000 \\
        --cogs 10000

All amounts in your base currency. Outputs JSON with all calculated metrics.
"""

import argparse
import json
import sys


def calculate_metrics(args):
    metrics = {}

    # Revenue Metrics
    mrr = args.mrr
    metrics["mrr"] = mrr
    metrics["arr"] = mrr * 12
    metrics["arpu"] = round(mrr / args.customers, 2) if args.customers > 0 else 0

    new_mrr = args.new_customers * (mrr / args.customers) if args.customers > 0 else 0
    net_new_mrr = new_mrr + args.expansion_mrr - args.contraction_mrr - args.churned_mrr
    metrics["net_new_mrr"] = round(net_new_mrr, 2)

    churn_contraction = args.contraction_mrr + args.churned_mrr
    new_expansion = new_mrr + args.expansion_mrr
    metrics["quick_ratio"] = round(new_expansion / churn_contraction, 2) if churn_contraction > 0 else float('inf')

    # Unit Economics
    metrics["cac"] = round(args.sm_spend / args.new_customers, 2) if args.new_customers > 0 else 0

    gross_margin = (mrr - args.cogs) / mrr if mrr > 0 else 0
    metrics["gross_margin_pct"] = round(gross_margin * 100, 1)

    monthly_churn_rate = args.churned_customers / args.customers if args.customers > 0 else 0
    metrics["monthly_churn_rate_pct"] = round(monthly_churn_rate * 100, 2)

    arpu = metrics["arpu"]
    ltv = (arpu * gross_margin) / monthly_churn_rate if monthly_churn_rate > 0 else float('inf')
    metrics["ltv"] = round(ltv, 2)

    cac = metrics["cac"]
    metrics["ltv_cac_ratio"] = round(ltv / cac, 2) if cac > 0 else float('inf')
    metrics["cac_payback_months"] = round(cac / (arpu * gross_margin), 1) if (arpu * gross_margin) > 0 else float('inf')

    # Retention
    metrics["logo_churn_rate_pct"] = round((args.churned_customers / args.customers) * 100, 2) if args.customers > 0 else 0
    metrics["revenue_churn_rate_pct"] = round((args.churned_mrr / mrr) * 100, 2) if mrr > 0 else 0

    nrr = (mrr + args.expansion_mrr - args.contraction_mrr - args.churned_mrr) / mrr if mrr > 0 else 0
    metrics["net_revenue_retention_pct"] = round(nrr * 100, 1)

    # Capital Efficiency
    metrics["monthly_burn"] = args.monthly_burn
    metrics["runway_months"] = round(args.cash / args.monthly_burn, 1) if args.monthly_burn > 0 else float('inf')

    net_new_arr = net_new_mrr * 12
    net_burn = args.monthly_burn
    metrics["burn_multiple"] = round((net_burn * 12) / net_new_arr, 2) if net_new_arr > 0 else float('inf')

    # Health Assessment
    health = {}
    health["ltv_cac"] = "green" if metrics["ltv_cac_ratio"] >= 3 else ("yellow" if metrics["ltv_cac_ratio"] >= 1.5 else "red")
    health["runway"] = "green" if metrics["runway_months"] >= 12 else ("yellow" if metrics["runway_months"] >= 6 else "red")
    health["churn"] = "green" if metrics["monthly_churn_rate_pct"] <= 5 else ("yellow" if metrics["monthly_churn_rate_pct"] <= 10 else "red")
    health["quick_ratio"] = "green" if metrics["quick_ratio"] >= 4 else ("yellow" if metrics["quick_ratio"] >= 2 else "red")
    health["nrr"] = "green" if metrics["net_revenue_retention_pct"] >= 100 else ("yellow" if metrics["net_revenue_retention_pct"] >= 85 else "red")
    health["gross_margin"] = "green" if metrics["gross_margin_pct"] >= 70 else ("yellow" if metrics["gross_margin_pct"] >= 50 else "red")

    metrics["health"] = health

    return metrics


def main():
    parser = argparse.ArgumentParser(description="Calculate SaaS metrics")
    parser.add_argument("--mrr", type=float, required=True, help="Monthly Recurring Revenue")
    parser.add_argument("--customers", type=int, required=True, help="Total active customers")
    parser.add_argument("--new-customers", type=int, default=0, help="New customers this month")
    parser.add_argument("--churned-customers", type=int, default=0, help="Customers lost this month")
    parser.add_argument("--expansion-mrr", type=float, default=0, help="Expansion MRR (upsells)")
    parser.add_argument("--contraction-mrr", type=float, default=0, help="Contraction MRR (downgrades)")
    parser.add_argument("--churned-mrr", type=float, default=0, help="Churned MRR (cancellations)")
    parser.add_argument("--sm-spend", type=float, default=0, help="Total Sales & Marketing spend")
    parser.add_argument("--cash", type=float, default=0, help="Cash in bank")
    parser.add_argument("--monthly-burn", type=float, default=0, help="Monthly burn rate")
    parser.add_argument("--cogs", type=float, default=0, help="Cost of Goods Sold (monthly)")

    args = parser.parse_args()
    metrics = calculate_metrics(args)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
