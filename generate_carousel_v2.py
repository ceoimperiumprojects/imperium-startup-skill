#!/usr/bin/env python3
"""Generate LinkedIn carousel v2: imperium-brain — story-driven angle"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills", "carousel"))

from pptx import Presentation
from pptx.util import Inches

from cookbook import (
    title_bold, content_single, content_stats,
    content_bullets, content_comparison, content_quote,
    divider_slide, cta_slide
)

# Imperium Tech brand colors
colors = {
    'primary': '0b1121',
    'secondary': '141e33',
    'accent': '00d4ff',
    'text': 'ffffff',
    'bg': '0b1121',
}
fonts = {'heading': 'Arial Black', 'body': 'Arial'}

prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(10)

# --- Slide 1: HOOK ---
title_bold(prs,
    title="I Replaced 10\nStartup Tools\nWith One Plugin",
    body="And it runs inside Claude Code.",
    colors=colors, fonts=fonts)

# --- Slide 2: The pain ---
content_single(prs,
    title="THE REALITY",
    body="Notion for docs.\nLinear for roadmaps.\nCanva for carousels.\nHubSpot for sales.\nSEMrush for SEO.\n\nToo many tabs.\nToo many subscriptions.\nZero integration.",
    colors=colors, fonts=fonts)

# --- Slide 3: The shift ---
content_single(prs,
    title="THE IDEA",
    body="What if your AI assistant\nalready knew:\n\nHow to write a pitch deck?\nHow to validate an idea?\nHow to write cold emails\nthat actually get replies?",
    colors=colors, fonts=fonts)

# --- Slide 4: Divider ---
divider_slide(prs,
    title="So I Built It.",
    body="7 repos. 10 books. 121K+ impressions of tested content.",
    colors=colors, fonts=fonts)

# --- Slide 5: Before / After ---
content_comparison(prs,
    title="Before vs After",
    body="",
    colors=colors, fonts=fonts,
    left_title="WITHOUT",
    left_items="Google 'cold email template'\nCopy generic framework\nHope it works\nSwitch between 5 apps\nStart from zero every time",
    right_title="WITH IMPERIUM",
    right_items="137 proven sales triggers\n34 battle-tested templates\nPersonalized to your ICP\nOne command, full pipeline\nBrand-consistent every time")

# --- Slide 6: What you get ---
content_stats(prs,
    title="", body="",
    colors=colors, fonts=fonts,
    stats=[
        {"value": "18", "label": "Domain Skills"},
        {"value": "87", "label": "Eval Tests"},
        {"value": "80+", "label": "Reference Docs"},
    ])

# --- Slide 7: The killer features ---
content_bullets(prs,
    title="It Thinks, Not Just Executes",
    body="",
    colors=colors, fonts=fonts,
    items=[
        'Say "write a data-driven post" — it researches first',
        'Say "on-brand carousel" — it reads your brand.json',
        'Say "validate my idea" — 5 fatal questions + scorecard',
        'Say "cold email" — 137 triggers, <100 words, ready to send',
        'Say "pitch deck" — 12-slide investor structure, auto-branded',
    ])

# --- Slide 8: Quote ---
content_quote(prs,
    title="",
    body="The best tools don't add complexity.\nThey absorb it.",
    colors=colors, fonts=fonts)

# --- Slide 9: The stack ---
content_single(prs,
    title="ONE INSTALL. ZERO CONFIG.",
    body="CEO advisor\nCTO advisor\nProduct manager\nMarketing + Sales\nFinance + Legal\nResearch engine\nLinkedIn + Carousel + Video\nBrand system\n\nAll in one plugin.",
    colors=colors, fonts=fonts)

# --- Slide 10: CTA ---
cta_slide(prs,
    title="Stop Tab-Switching.\nStart Building.",
    body="Open source. MIT license. Works in 30 seconds.",
    colors=colors, fonts=fonts,
    button_text="Get imperium-brain",
    handle="github.com/ceoimperiumprojects/imperium-brain")

output_path = "linkedin-carousel-imperium-brain-v2.pptx"
prs.save(output_path)
print(f"Carousel saved: {output_path}")
print(f"Total slides: {len(prs.slides)}")
