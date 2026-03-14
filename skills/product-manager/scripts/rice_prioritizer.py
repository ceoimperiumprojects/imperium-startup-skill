#!/usr/bin/env python3
"""RICE Prioritization Calculator — scores and ranks features by RICE framework.

Usage:
    python rice_prioritizer.py --features features.json

features.json format:
[
  {
    "name": "Feature A",
    "reach": 1000,
    "impact": 2,
    "confidence": 80,
    "effort": 3
  }
]

Or interactive mode:
    python rice_prioritizer.py --interactive
"""

import argparse
import json
import sys


def calculate_rice(feature):
    reach = feature["reach"]
    impact = feature["impact"]
    confidence = feature["confidence"] / 100
    effort = feature["effort"]

    score = (reach * impact * confidence) / effort if effort > 0 else 0
    return round(score, 1)


def main():
    parser = argparse.ArgumentParser(description="RICE Prioritization Calculator")
    parser.add_argument("--features", type=str, help="Path to features JSON file")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")

    args = parser.parse_args()

    features = []

    if args.features:
        with open(args.features) as f:
            features = json.load(f)
    elif args.interactive:
        print("Enter features (empty name to finish):")
        print("Impact scale: 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal")
        print("Confidence: 100=high, 80=medium, 50=low")
        print()

        while True:
            name = input("Feature name (empty to finish): ").strip()
            if not name:
                break
            try:
                reach = int(input("  Reach (users/quarter): "))
                impact = float(input("  Impact (0.25-3): "))
                confidence = int(input("  Confidence (50-100): "))
                effort = float(input("  Effort (person-months): "))
                features.append({
                    "name": name,
                    "reach": reach,
                    "impact": impact,
                    "confidence": confidence,
                    "effort": effort
                })
            except ValueError:
                print("  Invalid input, skipping this feature.")
        print()
    else:
        print("Provide --features <file> or --interactive", file=sys.stderr)
        sys.exit(1)

    results = []
    for feature in features:
        score = calculate_rice(feature)
        results.append({
            "name": feature["name"],
            "reach": feature["reach"],
            "impact": feature["impact"],
            "confidence": feature["confidence"],
            "effort": feature["effort"],
            "rice_score": score
        })

    results.sort(key=lambda x: x["rice_score"], reverse=True)

    for i, r in enumerate(results):
        r["rank"] = i + 1

    output = {
        "ranked_features": results,
        "recommendation": f"Top priority: {results[0]['name']} (RICE: {results[0]['rice_score']})" if results else "No features to rank"
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
