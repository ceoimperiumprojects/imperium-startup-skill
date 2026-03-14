#!/usr/bin/env python3
"""Financial Model Generator — creates 18-month revenue projections with three scenarios.

Usage:
    python financial_model.py --starting-mrr 5000 --monthly-growth 0.15 \\
        --starting-customers 50 --arpu 100 --monthly-churn 0.05 \\
        --monthly-burn 10000 --cash 200000

Outputs JSON with bear/base/bull projections for 18 months.
"""

import argparse
import json


def project_scenario(starting_mrr, growth_rate, starting_customers, arpu, churn_rate, monthly_burn, cash, months=18):
    projections = []
    mrr = starting_mrr
    customers = starting_customers
    remaining_cash = cash

    for month in range(1, months + 1):
        churned = int(customers * churn_rate)
        new_customers = max(1, int(customers * growth_rate))
        customers = customers - churned + new_customers
        mrr = customers * arpu

        revenue = mrr
        net_burn = monthly_burn - revenue
        remaining_cash = remaining_cash - net_burn

        projections.append({
            "month": month,
            "customers": customers,
            "new_customers": new_customers,
            "churned_customers": churned,
            "mrr": round(mrr, 2),
            "arr": round(mrr * 12, 2),
            "revenue": round(revenue, 2),
            "burn": round(monthly_burn, 2),
            "net_burn": round(max(0, net_burn), 2),
            "cash_remaining": round(remaining_cash, 2),
            "runway_months": round(remaining_cash / net_burn, 1) if net_burn > 0 else float('inf'),
            "profitable": revenue >= monthly_burn
        })

    return projections


def main():
    parser = argparse.ArgumentParser(description="Generate financial projections")
    parser.add_argument("--starting-mrr", type=float, required=True, help="Current MRR")
    parser.add_argument("--monthly-growth", type=float, default=0.15, help="Base monthly growth rate (default: 15%)")
    parser.add_argument("--starting-customers", type=int, required=True, help="Current customer count")
    parser.add_argument("--arpu", type=float, required=True, help="Average Revenue Per User")
    parser.add_argument("--monthly-churn", type=float, default=0.05, help="Monthly churn rate (default: 5%)")
    parser.add_argument("--monthly-burn", type=float, required=True, help="Monthly operating expenses")
    parser.add_argument("--cash", type=float, required=True, help="Cash in bank")
    parser.add_argument("--months", type=int, default=18, help="Projection period (default: 18)")

    args = parser.parse_args()

    scenarios = {
        "bear": project_scenario(
            args.starting_mrr, args.monthly_growth * 0.5, args.starting_customers,
            args.arpu, args.monthly_churn * 1.5, args.monthly_burn * 1.1, args.cash, args.months
        ),
        "base": project_scenario(
            args.starting_mrr, args.monthly_growth, args.starting_customers,
            args.arpu, args.monthly_churn, args.monthly_burn, args.cash, args.months
        ),
        "bull": project_scenario(
            args.starting_mrr, args.monthly_growth * 1.5, args.starting_customers,
            args.arpu, args.monthly_churn * 0.7, args.monthly_burn, args.cash, args.months
        ),
    }

    summary = {}
    for name, projections in scenarios.items():
        last = projections[-1]
        breakeven_month = None
        for p in projections:
            if p["profitable"]:
                breakeven_month = p["month"]
                break

        summary[name] = {
            "end_mrr": last["mrr"],
            "end_arr": last["arr"],
            "end_customers": last["customers"],
            "end_cash": last["cash_remaining"],
            "cash_out_month": next((p["month"] for p in projections if p["cash_remaining"] <= 0), None),
            "breakeven_month": breakeven_month,
        }

    output = {
        "assumptions": {
            "starting_mrr": args.starting_mrr,
            "monthly_growth_base": args.monthly_growth,
            "starting_customers": args.starting_customers,
            "arpu": args.arpu,
            "monthly_churn": args.monthly_churn,
            "monthly_burn": args.monthly_burn,
            "cash": args.cash,
        },
        "summary": summary,
        "projections": scenarios,
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
