#!/usr/bin/env python3
"""
Imperium Brain — Automated Eval Runner
Runs structural and routing checks on the plugin.
Generates a Markdown report in evals/results/.

Usage: python3 evals/eval-runner.py
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# --- Config ---
ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
COMMANDS_DIR = ROOT / "commands"
AGENTS_DIR = ROOT / "agents"
EVALS_FILE = ROOT / "evals" / "evals.json"
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".claude-plugin" / "marketplace.json"
HOOKS_JSON = ROOT / "hooks" / "hooks.json"
SKILL_MD = ROOT / "SKILL.md"
README_MD = ROOT / "README.md"
RESULTS_DIR = ROOT / "evals" / "results"

EXPECTED_SKILLS = [
    "ceo-advisor", "cto-advisor", "product-manager", "marketing",
    "sales-gtm", "finance", "founder", "legal", "engineering-advanced",
    "research", "api-discovery", "brand-voice", "linkedin", "carousel",
    "video", "slides", "sop", "visual-media"
]

CONTENT_SKILLS = [
    "brand-voice", "linkedin", "carousel", "video", "slides", "sop", "visual-media"
]

EXPECTED_AGENTS = [
    "ceo-strategist", "cto-architect", "growth-marketer", "sales-hunter",
    "product-analyst", "market-researcher", "content-creator", "brand-architect"
]

COOKBOOK_LAYOUTS = [
    "__init__", "content_bullets", "content_checklist", "content_comparison",
    "content_quote", "content_single", "content_stats", "content_timeline",
    "content_two_column",
    "data_bar_chart", "data_pie_chart", "data_table",
    "image_full", "image_grid", "image_left", "image_right",
    "title_bold", "title_centered", "title_gradient", "title_image",
    "cta_slide", "divider_slide"
]


class Result:
    PASS = "PASS"
    FAIL = "FAIL"
    WARN = "WARN"

    def __init__(self, status, check_name, message, details=None):
        self.status = status
        self.check_name = check_name
        self.message = message
        self.details = details or []


def parse_frontmatter(filepath):
    """Parse YAML-like frontmatter between --- markers using regex."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip("'\"")
    return fm


def read_text(filepath):
    """Read file text, return empty string on error."""
    try:
        return filepath.read_text(encoding="utf-8")
    except Exception:
        return ""


# --- Tier 1 Checks ---

def check_skill_files_exist():
    """S1: All 18 SKILL.md files exist and are non-empty."""
    missing = []
    empty = []
    for skill in EXPECTED_SKILLS:
        p = SKILLS_DIR / skill / "SKILL.md"
        if not p.exists():
            missing.append(skill)
        elif p.stat().st_size == 0:
            empty.append(skill)
    issues = []
    if missing:
        issues.append(f"Missing: {', '.join(missing)}")
    if empty:
        issues.append(f"Empty: {', '.join(empty)}")
    if issues:
        return Result(Result.FAIL, "S1_skill_files_exist",
                      f"{len(missing)} missing, {len(empty)} empty SKILL.md files", issues)
    return Result(Result.PASS, "S1_skill_files_exist",
                  f"All {len(EXPECTED_SKILLS)} SKILL.md files present and non-empty")


def check_frontmatter_valid():
    """S2: YAML frontmatter in each SKILL.md has required fields."""
    issues = []
    for skill in EXPECTED_SKILLS:
        p = SKILLS_DIR / skill / "SKILL.md"
        if not p.exists():
            continue
        fm = parse_frontmatter(p)
        if fm is None:
            issues.append(f"{skill}: no frontmatter found")
            continue
        for field in ["name", "description"]:
            if field not in fm or not fm[field]:
                issues.append(f"{skill}: missing '{field}' in frontmatter")
    if issues:
        return Result(Result.FAIL, "S2_frontmatter_valid",
                      f"{len(issues)} frontmatter issues", issues)
    return Result(Result.PASS, "S2_frontmatter_valid",
                  f"All {len(EXPECTED_SKILLS)} skills have valid frontmatter")


def check_references_exist():
    """S3: All reference files exist and are non-empty."""
    issues = []
    total = 0
    for skill in EXPECTED_SKILLS:
        refs_dir = SKILLS_DIR / skill / "references"
        if not refs_dir.exists():
            issues.append(f"{skill}: no references/ directory")
            continue
        for f in refs_dir.iterdir():
            if f.is_file():
                total += 1
                if f.stat().st_size == 0:
                    issues.append(f"{skill}/references/{f.name}: empty file")
    if issues:
        return Result(Result.WARN, "S3_references_exist",
                      f"{len(issues)} reference issues (total: {total})", issues)
    return Result(Result.PASS, "S3_references_exist",
                  f"All {total} reference files are non-empty")


def check_cross_references():
    """S4: File path patterns in SKILL.md body resolve to existing files."""
    issues = []
    path_pattern = re.compile(r'(?:references/|skills/|commands/|agents/)[\w\-/]+\.(?:md|py|json|sh)')
    for skill in EXPECTED_SKILLS:
        p = SKILLS_DIR / skill / "SKILL.md"
        if not p.exists():
            continue
        text = read_text(p)
        for match in path_pattern.finditer(text):
            ref_path = match.group(0)
            # Try relative to skill dir first, then project root
            candidates = [
                SKILLS_DIR / skill / ref_path,
                ROOT / ref_path,
            ]
            if not any(c.exists() for c in candidates):
                issues.append(f"{skill}/SKILL.md references '{ref_path}' — not found")
    if issues:
        return Result(Result.WARN, "S4_cross_references",
                      f"{len(issues)} unresolved cross-references", issues)
    return Result(Result.PASS, "S4_cross_references",
                  "All cross-references in SKILL.md files resolve")


def check_plugin_json_sync():
    """S5: plugin.json skills array matches skills/ directories."""
    issues = []
    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S5_plugin_json_sync", f"Cannot read plugin.json: {e}")

    plugin_skills = [s.replace("./skills/", "") for s in data.get("skills", [])]
    actual_skills = [d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]

    in_json_not_disk = set(plugin_skills) - set(actual_skills)
    in_disk_not_json = set(actual_skills) - set(plugin_skills)

    if in_json_not_disk:
        issues.append(f"In plugin.json but not on disk: {', '.join(in_json_not_disk)}")
    if in_disk_not_json:
        issues.append(f"On disk but not in plugin.json: {', '.join(in_disk_not_json)}")
    if issues:
        return Result(Result.FAIL, "S5_plugin_json_sync",
                      "plugin.json skills array out of sync", issues)
    return Result(Result.PASS, "S5_plugin_json_sync",
                  f"plugin.json skills array matches {len(actual_skills)} skill directories")


def check_command_frontmatter():
    """S6: Each command .md has valid frontmatter with name and user-invocable."""
    issues = []
    count = 0
    for f in sorted(COMMANDS_DIR.iterdir()):
        if not f.name.endswith(".md"):
            continue
        count += 1
        fm = parse_frontmatter(f)
        if fm is None:
            issues.append(f"{f.name}: no frontmatter")
            continue
        name = fm.get("name", "")
        if not name.startswith("imperium:"):
            issues.append(f"{f.name}: name '{name}' doesn't start with 'imperium:'")
        if fm.get("user-invocable", "").lower() != "true":
            issues.append(f"{f.name}: user-invocable not set to true")
    if issues:
        return Result(Result.FAIL, "S6_command_frontmatter",
                      f"{len(issues)} command frontmatter issues", issues)
    return Result(Result.PASS, "S6_command_frontmatter",
                  f"All {count} commands have valid frontmatter")


def check_hooks_command_count():
    """S7: hooks.json prompt mentions correct command count."""
    try:
        data = json.loads(HOOKS_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S7_hooks_command_count", f"Cannot read hooks.json: {e}")

    prompt = ""
    for hook in data.get("hooks", {}).get("SessionStart", []):
        for h in hook.get("hooks", []):
            if h.get("type") == "prompt":
                prompt = h.get("prompt", "")

    # Count actual commands
    actual_count = len([f for f in COMMANDS_DIR.iterdir() if f.name.endswith(".md")])

    # Find count in prompt
    count_match = re.search(r'(\d+)\s+slash commands', prompt)
    if not count_match:
        return Result(Result.WARN, "S7_hooks_command_count",
                      "No command count found in hooks.json prompt")

    hooks_count = int(count_match.group(1))
    if hooks_count != actual_count:
        return Result(Result.FAIL, "S7_hooks_command_count",
                      f"hooks.json says {hooks_count} commands, actual is {actual_count}")
    return Result(Result.PASS, "S7_hooks_command_count",
                  f"hooks.json correctly reports {actual_count} slash commands")


def check_eval_coverage():
    """S8: At least 2 eval scenarios per skill domain."""
    try:
        data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S8_eval_coverage", f"Cannot read evals.json: {e}")

    domain_counts = {}
    for ev in data.get("evals", []):
        # Count by expected_skills, not domain
        for skill in ev.get("expected_skills", []):
            domain_counts[skill] = domain_counts.get(skill, 0) + 1

    low = []
    for skill in EXPECTED_SKILLS:
        count = domain_counts.get(skill, 0)
        if count < 2:
            low.append(f"{skill}: {count} evals (need >= 2)")

    if low:
        return Result(Result.WARN, "S8_eval_coverage",
                      f"{len(low)} skills with < 2 evals", low)
    return Result(Result.PASS, "S8_eval_coverage",
                  f"All skills have >= 2 eval scenarios")


def check_brand_integration():
    """S9: 7 content skills mention brand.json or brand system."""
    issues = []
    for skill in CONTENT_SKILLS:
        p = SKILLS_DIR / skill / "SKILL.md"
        if not p.exists():
            issues.append(f"{skill}: SKILL.md missing")
            continue
        text = read_text(p).lower()
        if "brand" not in text:
            issues.append(f"{skill}: no mention of brand system")
    if issues:
        return Result(Result.FAIL, "S9_brand_integration",
                      f"{len(issues)} content skills missing brand integration", issues)
    return Result(Result.PASS, "S9_brand_integration",
                  f"All {len(CONTENT_SKILLS)} content skills reference brand system")


def check_marketplace_sync():
    """S10: marketplace.json counts and version match reality."""
    try:
        data = json.loads(MARKETPLACE_JSON.read_text(encoding="utf-8"))
        plugin_data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S10_marketplace_sync", f"Cannot read files: {e}")

    issues = []
    mp_desc = data.get("description", "") + " " + data.get("plugins", [{}])[0].get("description", "")
    mp_version = data.get("plugins", [{}])[0].get("version", "")
    plugin_version = plugin_data.get("version", "")

    if mp_version != plugin_version:
        issues.append(f"Version mismatch: marketplace={mp_version}, plugin.json={plugin_version}")

    # Check skill count in description
    skill_match = re.search(r'(\d+)\s+skills', mp_desc)
    if skill_match:
        mp_skills = int(skill_match.group(1))
        if mp_skills != len(EXPECTED_SKILLS):
            issues.append(f"Skill count: marketplace says {mp_skills}, actual is {len(EXPECTED_SKILLS)}")

    # Check command count in description
    cmd_count = len([f for f in COMMANDS_DIR.iterdir() if f.name.endswith(".md")])
    cmd_match = re.search(r'(\d+)\s+commands', mp_desc)
    if cmd_match:
        mp_cmds = int(cmd_match.group(1))
        if mp_cmds != cmd_count:
            issues.append(f"Command count: marketplace says {mp_cmds}, actual is {cmd_count}")

    if issues:
        return Result(Result.FAIL, "S10_marketplace_sync",
                      f"{len(issues)} marketplace sync issues", issues)
    return Result(Result.PASS, "S10_marketplace_sync",
                  "marketplace.json counts and version match reality")


def check_agent_files_exist():
    """S11: All agent files from plugin.json exist."""
    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S11_agent_files_exist", f"Cannot read plugin.json: {e}")

    issues = []
    agents = data.get("agents", [])
    for agent_path in agents:
        full = ROOT / agent_path.lstrip("./")
        if not full.exists():
            issues.append(f"Missing: {agent_path}")
        elif full.stat().st_size == 0:
            issues.append(f"Empty: {agent_path}")

    if issues:
        return Result(Result.FAIL, "S11_agent_files_exist",
                      f"{len(issues)} agent file issues", issues)
    return Result(Result.PASS, "S11_agent_files_exist",
                  f"All {len(agents)} agent files present")


def check_cookbook_completeness():
    """S12: carousel/cookbook/ has all 21 layout files + __init__.py."""
    cookbook_dir = SKILLS_DIR / "carousel" / "cookbook"
    if not cookbook_dir.exists():
        return Result(Result.FAIL, "S12_cookbook_completeness",
                      "skills/carousel/cookbook/ directory missing")

    missing = []
    for layout in COOKBOOK_LAYOUTS:
        f = cookbook_dir / f"{layout}.py"
        if not f.exists():
            missing.append(f"{layout}.py")

    if missing:
        return Result(Result.FAIL, "S12_cookbook_completeness",
                      f"{len(missing)} cookbook files missing", missing)
    actual = len([f for f in cookbook_dir.iterdir() if f.name.endswith(".py")])
    return Result(Result.PASS, "S12_cookbook_completeness",
                  f"Cookbook complete: {actual} Python files including __init__.py")


# --- Tier 2 Checks ---

def check_eval_references_exist():
    """S13: expected_references in evals.json resolve to actual files."""
    try:
        data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S13_eval_references_exist", f"Cannot read evals.json: {e}")

    issues = []
    for ev in data.get("evals", []):
        for ref in ev.get("expected_references", []):
            found = False
            for skill in ev.get("expected_skills", []):
                ref_path = SKILLS_DIR / skill / "references" / ref
                if ref_path.exists():
                    found = True
                    break
            if not found:
                issues.append(f"Eval '{ev['id']}': reference '{ref}' not found in any expected skill")

    if issues:
        return Result(Result.FAIL, "S13_eval_references_exist",
                      f"{len(issues)} eval references don't resolve", issues)
    return Result(Result.PASS, "S13_eval_references_exist",
                  "All eval expected_references resolve to actual files")


def check_eval_skills_in_routing():
    """S14: expected_skills in evals map to routing table entries."""
    routing_text = read_text(SKILL_MD)
    issues = []

    try:
        data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S14_eval_skills_in_routing", f"Cannot read evals.json: {e}")

    for ev in data.get("evals", []):
        for skill in ev.get("expected_skills", []):
            pattern = f"skills/{skill}"
            if pattern not in routing_text:
                issues.append(f"Eval '{ev['id']}': skill '{skill}' not in routing table")

    if issues:
        return Result(Result.FAIL, "S14_eval_skills_in_routing",
                      f"{len(issues)} eval skills not in routing table", issues)
    return Result(Result.PASS, "S14_eval_skills_in_routing",
                  "All eval expected_skills appear in routing table")


def check_eval_assertions_quality():
    """S15: Each eval has >= 2 assertions."""
    try:
        data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        return Result(Result.FAIL, "S15_eval_assertions_quality", f"Cannot read evals.json: {e}")

    issues = []
    for ev in data.get("evals", []):
        count = len(ev.get("assertions", []))
        if count < 2:
            issues.append(f"Eval '{ev['id']}': only {count} assertions (need >= 2)")

    if issues:
        return Result(Result.FAIL, "S15_eval_assertions_quality",
                      f"{len(issues)} evals with < 2 assertions", issues)
    total = len(data.get("evals", []))
    return Result(Result.PASS, "S15_eval_assertions_quality",
                  f"All {total} evals have >= 2 assertions")


def check_routing_table_completeness():
    """S16: Every skill directory appears in the routing table."""
    routing_text = read_text(SKILL_MD)
    issues = []
    for skill in EXPECTED_SKILLS:
        pattern = f"skills/{skill}"
        if pattern not in routing_text:
            issues.append(f"{skill}: not referenced in routing table")

    if issues:
        return Result(Result.FAIL, "S16_routing_table_completeness",
                      f"{len(issues)} skills missing from routing table", issues)
    return Result(Result.PASS, "S16_routing_table_completeness",
                  f"All {len(EXPECTED_SKILLS)} skills in routing table")


def check_counts_consistency():
    """S17: SKILL.md, README, hooks.json, plugin.json skill/command counts agree."""
    issues = []

    skill_count = len(EXPECTED_SKILLS)
    cmd_count = len([f for f in COMMANDS_DIR.iterdir() if f.name.endswith(".md")])
    agent_count = len([f for f in AGENTS_DIR.iterdir() if f.name.endswith(".md")])

    # Check SKILL.md
    skill_md_text = read_text(SKILL_MD)
    sm_match = re.search(r'(\d+)\s+skills', skill_md_text)
    if sm_match and int(sm_match.group(1)) != skill_count:
        issues.append(f"SKILL.md says {sm_match.group(1)} skills, actual is {skill_count}")

    cm_match = re.search(r'(\d+)\s+commands', skill_md_text)
    if cm_match and int(cm_match.group(1)) != cmd_count:
        issues.append(f"SKILL.md says {cm_match.group(1)} commands, actual is {cmd_count}")

    # Check README
    readme_text = read_text(README_MD)
    rm_skill = re.search(r'(\d+)\s+Skills', readme_text)
    if rm_skill and int(rm_skill.group(1)) != skill_count:
        issues.append(f"README says {rm_skill.group(1)} skills, actual is {skill_count}")

    rm_cmd = re.search(r'(\d+)\s+Slash Commands', readme_text)
    if rm_cmd and int(rm_cmd.group(1)) != cmd_count:
        issues.append(f"README says {rm_cmd.group(1)} commands, actual is {cmd_count}")

    # Check hooks.json
    try:
        hooks_data = json.loads(HOOKS_JSON.read_text(encoding="utf-8"))
        prompt = ""
        for hook in hooks_data.get("hooks", {}).get("SessionStart", []):
            for h in hook.get("hooks", []):
                if h.get("type") == "prompt":
                    prompt = h.get("prompt", "")
        hk_cmd = re.search(r'(\d+)\s+slash commands', prompt)
        if hk_cmd and int(hk_cmd.group(1)) != cmd_count:
            issues.append(f"hooks.json says {hk_cmd.group(1)} commands, actual is {cmd_count}")
    except Exception:
        issues.append("Cannot read hooks.json for count check")

    if issues:
        return Result(Result.FAIL, "S17_counts_consistency",
                      f"{len(issues)} count mismatches", issues)
    return Result(Result.PASS, "S17_counts_consistency",
                  f"All counts consistent: {skill_count} skills, {cmd_count} commands, {agent_count} agents")


# --- Report Generation ---

def run_all_checks():
    """Run all checks and return list of Results."""
    checks = [
        check_skill_files_exist,
        check_frontmatter_valid,
        check_references_exist,
        check_cross_references,
        check_plugin_json_sync,
        check_command_frontmatter,
        check_hooks_command_count,
        check_eval_coverage,
        check_brand_integration,
        check_marketplace_sync,
        check_agent_files_exist,
        check_cookbook_completeness,
        check_eval_references_exist,
        check_eval_skills_in_routing,
        check_eval_assertions_quality,
        check_routing_table_completeness,
        check_counts_consistency,
    ]
    results = []
    for check_fn in checks:
        try:
            results.append(check_fn())
        except Exception as e:
            results.append(Result(Result.FAIL, check_fn.__name__,
                                  f"Check crashed: {e}"))
    return results


def generate_report(results):
    """Generate a Markdown report from results."""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S")

    try:
        plugin_data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
        version = plugin_data.get("version", "unknown")
    except Exception:
        version = "unknown"

    try:
        evals_data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
        eval_count = len(evals_data.get("evals", []))
    except Exception:
        eval_count = "?"

    passes = sum(1 for r in results if r.status == Result.PASS)
    fails = sum(1 for r in results if r.status == Result.FAIL)
    warns = sum(1 for r in results if r.status == Result.WARN)

    lines = []
    lines.append("# Imperium Brain — Eval Results")
    lines.append(f"**Run:** {timestamp} | **Version:** {version} | **Evals:** {eval_count}")
    lines.append("")

    # Summary
    status_emoji = {Result.PASS: "PASS", Result.FAIL: "FAIL", Result.WARN: "WARN"}
    lines.append(f"## Summary: {passes} PASS | {fails} FAIL | {warns} WARN")
    lines.append("")

    if fails == 0 and warns == 0:
        lines.append("> All checks passing. Plugin is healthy.")
        lines.append("")

    # Failures
    fail_results = [r for r in results if r.status == Result.FAIL]
    if fail_results:
        lines.append("## Failures (must fix)")
        lines.append("")
        for r in fail_results:
            lines.append(f"### FAIL: {r.check_name}")
            lines.append(f"{r.message}")
            if r.details:
                for d in r.details:
                    lines.append(f"  - {d}")
            lines.append("")

    # Warnings
    warn_results = [r for r in results if r.status == Result.WARN]
    if warn_results:
        lines.append("## Warnings (should fix)")
        lines.append("")
        for r in warn_results:
            lines.append(f"### WARN: {r.check_name}")
            lines.append(f"{r.message}")
            if r.details:
                for d in r.details:
                    lines.append(f"  - {d}")
            lines.append("")

    # Passes
    pass_results = [r for r in results if r.status == Result.PASS]
    if pass_results:
        lines.append("## Passing")
        lines.append("")
        for r in pass_results:
            lines.append(f"- **{r.check_name}**: {r.message}")
        lines.append("")

    return "\n".join(lines)


def main():
    # Ensure results directory exists
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    print("Running imperium-brain eval checks...")
    print(f"Root: {ROOT}")
    print()

    results = run_all_checks()

    # Print summary to console
    passes = sum(1 for r in results if r.status == Result.PASS)
    fails = sum(1 for r in results if r.status == Result.FAIL)
    warns = sum(1 for r in results if r.status == Result.WARN)

    for r in results:
        icon = {"PASS": "+", "FAIL": "X", "WARN": "!"}[r.status]
        print(f"  [{icon}] {r.check_name}: {r.message}")
        if r.details and r.status != Result.PASS:
            for d in r.details[:5]:  # Show max 5 details
                print(f"      - {d}")
            if len(r.details) > 5:
                print(f"      ... and {len(r.details) - 5} more")

    print()
    print(f"Summary: {passes} PASS | {fails} FAIL | {warns} WARN")

    # Write report
    report = generate_report(results)
    filename = datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".md"
    report_path = RESULTS_DIR / filename
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport saved: {report_path}")

    # Exit code
    sys.exit(1 if fails > 0 else 0)


if __name__ == "__main__":
    main()
