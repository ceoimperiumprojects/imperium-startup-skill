#!/usr/bin/env python3
"""
Founder KB Search — Wrapper for semantic search over the startup book knowledge base.

Requires: founder-kb CLI installed (pip install -e /path/to/founder-ai-mentor)
Gracefully degrades if dependencies are not available.
"""

import argparse
import json
import subprocess
import shutil
import sys
from pathlib import Path


# Resolve the bundled chroma_db path relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
BUNDLED_DB = SCRIPT_DIR / "founder-kb" / "chroma_db"


def check_founder_kb():
    """Check if founder-kb CLI is available."""
    return shutil.which("founder-kb") is not None


def search(query: str, top_k: int = 5, source: str | None = None) -> dict:
    """Run semantic search via founder-kb CLI."""
    if not check_founder_kb():
        return {
            "error": "founder-kb not installed",
            "help": "Run: bash skills/founder/scripts/setup_founder_kb.sh",
            "fallback": "Use the markdown reference files in skills/*/references/ instead."
        }

    cmd = ["founder-kb", "--json"]
    # Use bundled DB if available, otherwise let founder-kb use its default
    if BUNDLED_DB.exists():
        cmd.extend(["--db-path", str(BUNDLED_DB)])
    cmd.extend(["search", query, "--top-k", str(top_k)])
    if source:
        cmd.extend(["--source", source])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            return {"error": f"founder-kb error: {result.stderr.strip()}"}
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        return {"error": "Search timed out (60s limit)"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON from founder-kb", "raw": result.stdout[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(
        description="Search the founder knowledge base (10 startup books, 2000+ chunks)"
    )
    parser.add_argument("query", help="Semantic search query")
    parser.add_argument("-k", "--top-k", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument("-s", "--source", help="Filter by source (e.g., 'zero-to-one')")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Raw JSON output")
    parser.add_argument("--check", action="store_true", help="Check if founder-kb is installed")

    args = parser.parse_args()

    if args.check:
        installed = check_founder_kb()
        status = {"installed": installed, "path": shutil.which("founder-kb")}
        print(json.dumps(status, indent=2))
        sys.exit(0 if installed else 1)

    results = search(args.query, args.top_k, args.source)

    if args.json_output:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif "error" in results:
        print(f"⚠ {results['error']}")
        if "help" in results:
            print(f"  → {results['help']}")
        if "fallback" in results:
            print(f"  → {results['fallback']}")
        sys.exit(1)
    else:
        for i, r in enumerate(results, 1):
            relevance = r.get("relevance", 0)
            source = r.get("source", "unknown")
            text = r.get("text", "")
            print(f"\n{'='*60}")
            print(f"Result {i} | Relevance: {relevance:.0%} | Source: {source}")
            print(f"{'='*60}")
            print(text[:500])
            if len(text) > 500:
                print(f"\n  ... ({len(text)} chars total)")


if __name__ == "__main__":
    main()
