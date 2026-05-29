#!/usr/bin/env python3
"""Generate LinkedIn carousel: imperium-brain — The Ultimate Startup OS"""
import sys
import os

# Add cookbook to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills", "carousel"))

from pptx import Presentation
from pptx.util import Inches

from cookbook import (
    title_bold, content_single, content_stats,
    content_bullets, divider_slide, cta_slide
)

# Colors — Imperium Tech brand (dark navy + cyan accent)
colors = {
    'primary': '0b1121',
    'secondary': '141e33',
    'accent': '00d4ff',
    'text': 'ffffff',
    'bg': '0b1121',
}
fonts = {'heading': 'Arial Black', 'body': 'Arial'}

# Create presentation — LinkedIn square format
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(10)

# --- Slide 1: COVER ---
title_bold(prs,
    title="I Built a Startup OS\nInside Claude Code",
    body="18 skills. 87 evals. Zero config. Here's what it does.",
    colors=colors, fonts=fonts)

# --- Slide 2: The Problem ---
content_single(prs,
    title="THE PROBLEM",
    body="Every startup founder uses\n10+ tools to run their business.\n\nWhat if ONE plugin could\nreplace them all?",
    colors=colors, fonts=fonts)

# --- Slide 3: Stats ---
content_stats(prs,
    title="", body="",
    colors=colors, fonts=fonts,
    stats=[
        {"value": "18", "label": "Domain Skills"},
        {"value": "8", "label": "AI Agents"},
        {"value": "20", "label": "Slash Commands"},
    ])

# --- Slide 4: Divider ---
divider_slide(prs,
    title="What's Inside?",
    body="Three pillars of startup intelligence",
    colors=colors, fonts=fonts)

# --- Slide 5: Startup Ops ---
content_bullets(prs,
    title="Startup Ops (9 skills)",
    body="",
    colors=colors, fonts=fonts,
    items=[
        "CEO Advisor — strategy, fundraising, board prep",
        "CTO Advisor — architecture, stack selection, tech debt",
        "Product Manager — PRDs, RICE prioritization, roadmaps",
        "Marketing — SEO, CRO, copywriting, 19 traction channels",
        "Sales & GTM — 137 triggers, cold email, 11 GTM plays",
        "Finance — SaaS metrics, runway, financial modeling",
        "Founder — idea validation, Mom Test, 10-book knowledge base",
        "Legal — entity structure, contracts, compliance",
        "Engineering — agent design, RAG, MCP, CI/CD",
    ])

# --- Slide 6: Research ---
content_single(prs,
    title="COMPETITIVE INTELLIGENCE",
    body="9-phase research framework\n\n12 search strategies\nTop-20 scoring system\nHidden API discovery\n\nKnow your market better\nthan your competitors know themselves.",
    colors=colors, fonts=fonts)

# --- Slide 7: Content Creation ---
content_bullets(prs,
    title="Content Creation (7 skills)",
    body="",
    colors=colors, fonts=fonts,
    items=[
        "LinkedIn — 12 post types, 55+ hooks, algorithm 2025",
        "Carousel — 21 PPTX layouts, auto brand integration",
        "Brand Voice — colors, fonts, voice spectrums, 6 platforms",
        "HTML Slides — zero-dep presentations, 12 style presets",
        "Video — 5 templates, Remotion bridge, shot lists",
        "SOP — runbooks, playbooks, process maps",
        "Visual Media — AI-powered image sourcing & review",
    ])

# --- Slide 8: The Secret Sauce ---
content_single(prs,
    title="THE SECRET SAUCE",
    body="Intelligent routing that\nUNDERSTANDS your intent.\n\nSay \"write a data-driven post\nabout our market\"\n\nIt runs research FIRST,\nthen writes the post.",
    colors=colors, fonts=fonts)

# --- Slide 9: Stats slam ---
content_stats(prs,
    title="", body="",
    colors=colors, fonts=fonts,
    stats=[
        {"value": "87", "label": "Eval Scenarios"},
        {"value": "80+", "label": "Reference Docs"},
        {"value": "7", "label": "Source Repos"},
    ])

# --- Slide 10: CTA ---
cta_slide(prs,
    title="Your AI Co-Founder\nis One Install Away",
    body="Open source. MIT license. Works out of the box.",
    colors=colors, fonts=fonts,
    button_text="Install Now",
    handle="github.com/ceoimperiumprojects/imperium-brain")

# Save
output_path = "linkedin-carousel-imperium-brain.pptx"
prs.save(output_path)
print(f"Carousel saved: {output_path}")
print(f"Total slides: {len(prs.slides)}")
print(f"Format: 1080x1080 (LinkedIn square)")
