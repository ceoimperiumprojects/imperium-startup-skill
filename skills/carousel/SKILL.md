---
name: carousel
description: 'PPTX carousel and slide deck creator with 21 layout templates. Generates professional presentations, LinkedIn carousels, pitch decks, and educational slide decks using python-pptx. Applies brand colors and fonts when brand system is configured. Triggers on: carousel, PPTX, PowerPoint, deck, pitch deck design, slide deck, presentation slides, presentation design, LinkedIn carousel, carousel post.'
user-invocable: false
---

# Carousel / PPTX Skill

Create professional PPTX slide decks and carousels using python-pptx. 21 layout templates, 6 carousel types, automatic brand integration. Outputs production-ready `.pptx` files.

## Keywords

Carousel, PPTX, PowerPoint, deck, pitch deck design, slide deck, presentation slides, presentation design, LinkedIn carousel, carousel post, slides, slideshow, pitch presentation, investor deck, product deck, demo deck, case study deck, internal report, slide layout, slide template, python-pptx, presentation builder, content slides, data slides

## Prerequisites

Before generating any carousel, verify that python-pptx is available:

```python
# Check if python-pptx is installed
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    print("python-pptx is ready")
except ImportError:
    print("python-pptx is not installed. Installing...")
    # Run: pip install python-pptx Pillow
```

If python-pptx is not installed, run `pip install python-pptx Pillow` before proceeding. Do NOT attempt to generate slides without the library installed.

## Brand Integration

Before generating any carousel, check for and apply the brand system:

### Step 1: Check for brand.json

```python
import json
import os

brand_path = 'brand/brand.json'
colors = None
fonts = None

if os.path.exists(brand_path):
    with open(brand_path, 'r') as f:
        brand = json.load(f)

    # Extract colors (strip '#' prefix if present)
    brand_colors = brand.get('colors', {})
    colors = {
        'primary': brand_colors.get('primary', '1a1a2e').lstrip('#'),
        'secondary': brand_colors.get('secondary', '16213e').lstrip('#'),
        'accent': brand_colors.get('accent', 'e94560').lstrip('#'),
        'text': brand_colors.get('text', 'ffffff').lstrip('#'),
        'bg': brand_colors.get('background', '1a1a2e').lstrip('#'),
    }

    # Extract fonts
    brand_fonts = brand.get('fonts', brand.get('typography', {}))
    fonts = {
        'heading': brand_fonts.get('heading', brand_fonts.get('display', 'Arial Black')),
        'body': brand_fonts.get('body', brand_fonts.get('text', 'Arial')),
    }

    print(f"Brand applied: {brand.get('company_name', 'Custom brand')}")
else:
    print("No brand.json found — using professional defaults")
```

### Step 2: Apply Defaults If No Brand

```python
# Professional defaults — dark navy theme, clean and modern
if not colors:
    colors = {
        'primary': '1a1a2e',    # Dark navy
        'secondary': '16213e',   # Darker navy
        'accent': 'e94560',      # Coral red accent
        'text': 'ffffff',        # White text
        'bg': '1a1a2e',          # Dark navy background
    }

if not fonts:
    fonts = {
        'heading': 'Arial Black',  # Bold, widely available
        'body': 'Arial',           # Clean, universal
    }
```

## Carousel Types

### 1. LinkedIn Carousel

**Format:** 1080x1080px (square), 5-10 slides
**Purpose:** Social media content — educational, promotional, thought leadership

**Structure:**
1. **Cover slide** — Hook headline that stops the scroll. Use `title_bold` or `title_centered`.
2. **Content slides** (3-8) — One point per slide. Use `content_single` exclusively.
3. **CTA slide** — Clear call to action. Use `cta_slide`.

**Slide size setup:**
```python
from pptx import Presentation
from pptx.util import Inches, Emu

prs = Presentation()
# LinkedIn carousel: 1080x1080px = 10 inches x 10 inches at 108 DPI
# python-pptx uses EMU (English Metric Units): 1 inch = 914400 EMU
prs.slide_width = Inches(10)
prs.slide_height = Inches(10)
```

**Content rules:**
- Maximum 20-30 words per slide
- One idea per slide — no multi-point slides
- Use large font (36pt+ body)
- Strong contrast (dark bg + white text)
- CTA on the last slide: follow, comment, share, link
- Hook on the first slide: question, bold claim, or surprising stat

**Example flow:**
| Slide | Layout | Content |
|-------|--------|---------|
| 1 | `title_bold` | "5 Things I Wish I Knew Before Raising My Seed Round" |
| 2 | `content_single` | "1. Your first investor sets the terms for everyone after" |
| 3 | `content_single` | "2. Warm intros convert 10x better than cold emails" |
| 4 | `content_single` | "3. Due diligence starts before the first meeting" |
| 5 | `content_single` | "4. Your cap table is your company's DNA — protect it" |
| 6 | `content_single` | "5. The best pitch is a story, not a spreadsheet" |
| 7 | `cta_slide` | "Follow for more startup insights" |

---

### 2. Pitch Deck

**Format:** 16:9 (widescreen), 10-15 slides
**Purpose:** Investor presentations, fundraising

**Structure:**
1. Cover — `title_gradient` or `title_image`
2. Problem — `content_single` or `content_bullets`
3. Solution — `content_bullets` or `image_left`
4. Market Size — `content_stats` (TAM/SAM/SOM)
5. Product — `image_full` or `image_right`
6. Business Model — `content_two_column` or `data_table`
7. Traction — `content_stats` or `data_bar_chart`
8. Competition — `content_comparison`
9. Go-to-Market — `content_timeline` or `content_bullets`
10. Team — `image_grid` or `content_two_column`
11. Financials — `data_bar_chart` or `data_table`
12. The Ask — `cta_slide`

**Slide size setup:**
```python
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
```

**Content rules:**
- Maximum 40-50 words per slide
- Lead with the insight, not the data
- Numbers should be specific: "$2.3M ARR" not "growing revenue"
- Every slide should answer one question an investor has
- Notes field: add speaker notes for the presenter

---

### 3. Educational Deck

**Format:** 16:9, 10-20 slides
**Purpose:** Tutorials, courses, workshops, onboarding

**Structure:**
1. Cover — `title_centered`
2. Agenda/Overview — `content_bullets`
3. Section dividers — `divider_slide`
4. Concept slides — `content_single`, `content_bullets`
5. Examples — `image_left`, `image_right`, `content_two_column`
6. Practice/Exercise — `content_checklist`
7. Summary — `content_bullets`
8. Resources/Next Steps — `cta_slide`

**Content rules:**
- Progressive complexity — start simple, build up
- One concept per slide
- Use section dividers between topics
- Include visual examples where possible
- Alternate between text-heavy and visual slides for rhythm

---

### 4. Product Demo Deck

**Format:** 16:9, 8-12 slides
**Purpose:** Feature showcases, product walkthroughs, sales demos

**Structure:**
1. Cover — `title_bold`
2. Problem/Pain Point — `content_single`
3. Product Overview — `image_full`
4. Feature 1 — `image_left`
5. Feature 2 — `image_right`
6. Feature 3 — `image_left`
7. Before/After — `content_comparison`
8. Social Proof — `content_quote` or `content_stats`
9. Pricing — `data_table`
10. CTA — `cta_slide`

**Content rules:**
- Lead with the user's pain, not your features
- Show, don't tell — screenshots and mockups on every feature slide
- Use `image_left` and `image_right` alternating for visual rhythm
- End with clear next step (book demo, sign up, etc.)

---

### 5. Case Study Deck

**Format:** 16:9, 6-10 slides
**Purpose:** Customer success stories, portfolio pieces, results showcases

**Structure:**
1. Cover — `title_centered` (client name + project)
2. Client Context — `content_bullets` or `content_two_column`
3. Challenge — `content_single` (the core problem)
4. Approach — `content_timeline` or `content_checklist`
5. Solution — `image_left` or `image_right`
6. Results — `content_stats` (key metrics)
7. Data Deep Dive — `data_bar_chart` or `data_table`
8. Testimonial — `content_quote`
9. Learnings — `content_bullets`
10. CTA — `cta_slide`

**Content rules:**
- Tell a story: challenge → approach → results
- Lead with specific, quantifiable results
- Include a client quote
- Data visualizations for credibility

---

### 6. Internal Report

**Format:** 16:9, 5-15 slides
**Purpose:** Team updates, board reports, quarterly reviews, sprint retrospectives

**Structure:**
1. Cover — `title_centered`
2. Executive Summary — `content_bullets`
3. Key Metrics — `content_stats`
4. Performance Data — `data_bar_chart`
5. Breakdown — `data_pie_chart`
6. Detailed Numbers — `data_table`
7. Timeline / Roadmap — `content_timeline`
8. Action Items — `content_checklist`
9. Next Steps — `content_bullets`

**Content rules:**
- Lead with the headline ("Revenue up 34% QoQ")
- Use data layouts heavily — this audience wants numbers
- Section dividers for multi-topic reports
- Action items should be concrete and assigned

---

## 21 Layout Templates

All layouts are Python functions in the `cookbook/` directory. Each function has the signature:

```python
def add_slide(prs, title="", body="", colors=None, fonts=None, **kwargs)
```

### Title Layouts (4)

| # | Layout | File | Description |
|---|--------|------|-------------|
| 1 | Title Centered | `cookbook/title_centered.py` | Centered title + subtitle, full background, accent line separator |
| 2 | Title Bold | `cookbook/title_bold.py` | Large bold left-aligned title with vertical accent bar |
| 3 | Title Image | `cookbook/title_image.py` | Title over background image with semi-transparent overlay |
| 4 | Title Gradient | `cookbook/title_gradient.py` | Title with two-color diagonal gradient background |

### Content Layouts (8)

| # | Layout | File | Description |
|---|--------|------|-------------|
| 5 | Content Single | `cookbook/content_single.py` | Single key point in large text, maximum whitespace |
| 6 | Content Bullets | `cookbook/content_bullets.py` | Title + bullet point list with accent underline |
| 7 | Content Two Column | `cookbook/content_two_column.py` | Two-column text with vertical divider |
| 8 | Content Quote | `cookbook/content_quote.py` | Large quote with decorative quotation mark and attribution |
| 9 | Content Stats | `cookbook/content_stats.py` | Big number/metric with context (single or multi-stat) |
| 10 | Content Comparison | `cookbook/content_comparison.py` | Side-by-side panels with VS circle |
| 11 | Content Timeline | `cookbook/content_timeline.py` | Horizontal timeline with milestone markers |
| 12 | Content Checklist | `cookbook/content_checklist.py` | Checklist with checkmark/square icons |

### Image Layouts (4)

| # | Layout | File | Description |
|---|--------|------|-------------|
| 13 | Image Full | `cookbook/image_full.py` | Full-bleed image with bottom text overlay strip |
| 14 | Image Left | `cookbook/image_left.py` | Image left 45%, text right 55% |
| 15 | Image Right | `cookbook/image_right.py` | Text left 55%, image right 45% |
| 16 | Image Grid | `cookbook/image_grid.py` | 2x2 image grid with captions |

### Data Layouts (3)

| # | Layout | File | Description |
|---|--------|------|-------------|
| 17 | Bar Chart | `cookbook/data_bar_chart.py` | Column chart with categories and values |
| 18 | Pie Chart | `cookbook/data_pie_chart.py` | Pie chart with percentage labels and legend |
| 19 | Data Table | `cookbook/data_table.py` | Styled table with colored header and alternating rows |

### Special Layouts (2)

| # | Layout | File | Description |
|---|--------|------|-------------|
| 20 | CTA Slide | `cookbook/cta_slide.py` | Call-to-action with button shape and optional handle |
| 21 | Divider Slide | `cookbook/divider_slide.py` | Section divider with accent background and large text |

## Carousel Generation Workflow

Follow this exact workflow when generating a carousel:

### Step 1: Understand the Request

Determine:
- **Type**: Which of the 6 carousel types? (LinkedIn, pitch deck, educational, product demo, case study, internal report)
- **Topic**: What is the content about?
- **Slide count**: How many slides? (Use type defaults if not specified)
- **Special requirements**: Images? Data? Charts? Specific branding?

### Step 2: Generate Slide Plan

Create a table mapping each slide to a layout and content:

```
| Slide # | Layout | Title | Key Content | Notes |
|---------|--------|-------|-------------|-------|
| 1 | title_bold | "Hook headline" | ... | Cover slide |
| 2 | content_single | "TIP #1" | "Key point" | ... |
```

### Step 3: Check Brand System

```python
import json, os

colors = None
fonts = None

if os.path.exists('brand/brand.json'):
    with open('brand/brand.json') as f:
        brand = json.load(f)
    brand_colors = brand.get('colors', {})
    colors = {
        'primary': brand_colors.get('primary', '1a1a2e').lstrip('#'),
        'secondary': brand_colors.get('secondary', '16213e').lstrip('#'),
        'accent': brand_colors.get('accent', 'e94560').lstrip('#'),
        'text': brand_colors.get('text', 'ffffff').lstrip('#'),
        'bg': brand_colors.get('background', '1a1a2e').lstrip('#'),
    }
    brand_fonts = brand.get('fonts', brand.get('typography', {}))
    fonts = {
        'heading': brand_fonts.get('heading', 'Arial Black'),
        'body': brand_fonts.get('body', 'Arial'),
    }
```

### Step 4: Generate Python Script

Write a complete Python script that:
1. Imports the necessary cookbook modules
2. Creates a Presentation object with correct dimensions
3. Calls layout functions for each slide
4. Saves the .pptx file

**Example script structure:**

```python
#!/usr/bin/env python3
"""Generate [carousel type]: [topic]"""
import sys
import os

# Add cookbook to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx import Presentation
from pptx.util import Inches

# Import layouts
from cookbook import (
    title_bold, content_single, cta_slide
)

# Brand colors and fonts
colors = {
    'primary': '1a1a2e',
    'secondary': '16213e',
    'accent': 'e94560',
    'text': 'ffffff',
    'bg': '1a1a2e',
}
fonts = {'heading': 'Arial Black', 'body': 'Arial'}

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)   # Square for LinkedIn
prs.slide_height = Inches(10)

# --- Slide 1: Cover ---
title_bold(prs, title="Your Hook Here", body="Subtitle", colors=colors, fonts=fonts)

# --- Slide 2: Point 1 ---
content_single(prs, title="TIP #1", body="Your key point here", colors=colors, fonts=fonts)

# ... more slides ...

# --- Final: CTA ---
cta_slide(prs, title="Ready?", body="Take action now",
          colors=colors, fonts=fonts, button_text="Follow Me",
          handle="@yourhandle")

# Save
output_path = "my-carousel.pptx"
prs.save(output_path)
print(f"Carousel saved: {output_path}")
print(f"Total slides: {len(prs.slides)}")
```

### Step 5: Run the Script

Execute the generated Python script:
```bash
python3 generate_carousel.py
```

### Step 6: Report Results

After successful generation, report:
- Output file path
- Total slide count
- Layout breakdown (which layouts were used)
- File size
- Any notes (e.g., "add your images to the placeholder slots")

## Writing Rules for Carousel Content

### Word Count Limits
| Carousel Type | Max Words/Slide | Title Max | Body Max |
|---------------|----------------|-----------|----------|
| LinkedIn Carousel | 30 | 10 | 20 |
| Pitch Deck | 50 | 8 | 40 |
| Educational Deck | 60 | 8 | 50 |
| Product Demo | 40 | 8 | 30 |
| Case Study | 50 | 8 | 40 |
| Internal Report | 60 | 8 | 50 |

### Visual Design Rules
1. **Contrast**: Dark background + light text OR light background + dark text. Never low contrast.
2. **Font size**: Minimum 24pt for body text, 36pt+ for titles. LinkedIn carousels: 36pt body minimum.
3. **Whitespace**: Target 40% whitespace on every slide. Content should not fill the entire slide.
4. **Consistency**: Same colors, fonts, and layout rhythm throughout the deck.
5. **One idea per slide**: Every slide should communicate exactly one concept.
6. **Visual rhythm**: Alternate layout types — don't use the same layout 5 times in a row. Exception: LinkedIn carousels using `content_single` throughout (this is intentional).

### Content Writing Rules
1. **Hook first**: The cover slide must stop the scroll. Use a question, bold claim, surprising stat, or contrarian take.
2. **Specifics over generics**: "Grew 340% in 6 months" beats "experienced significant growth."
3. **Active voice**: "We built X" not "X was built by us."
4. **Numbers are magnetic**: Include at least 2-3 data points in any carousel.
5. **CTA is mandatory**: Every carousel ends with a clear call to action.
6. **No walls of text**: If a slide needs more than 50 words, split it into two slides.

## Cookbook Reference

All 21 layout functions are in `skills/carousel/cookbook/`. Each is a standalone Python module with an `add_slide()` function. See `skills/carousel/references/layout-guide.md` for detailed documentation of every layout including visual descriptions, use cases, and parameter tables.

To import all layouts:
```python
from cookbook import ALL_LAYOUTS

# Use by name
ALL_LAYOUTS['title_centered'](prs, title="Hello", colors=colors, fonts=fonts)
```

To import specific layouts:
```python
from cookbook import title_bold, content_single, cta_slide
```

## Output Format

All generated carousels are saved as `.pptx` files. The default output location is the current working directory. The filename should be descriptive:

- LinkedIn carousel: `linkedin-carousel-[topic].pptx`
- Pitch deck: `pitch-deck-[company].pptx`
- Educational deck: `edu-deck-[topic].pptx`
- Product demo: `demo-deck-[product].pptx`
- Case study: `case-study-[client].pptx`
- Internal report: `report-[period].pptx`

## Error Handling

If python-pptx is not installed:
1. Inform the user
2. Offer to install it: `pip install python-pptx Pillow`
3. After installation, re-run the generation script

If an image path is invalid:
1. Use the placeholder fallback (colored rectangle with "[IMAGE]" text)
2. Note in the output which slides need images added manually

If brand.json has unexpected format:
1. Fall back to professional defaults
2. Log which brand fields were missing
3. Continue with generation — never fail silently
