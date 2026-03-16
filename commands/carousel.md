---
name: imperium:carousel
description: Create a PPTX carousel or slide deck. Choose from 6 types and 21 layouts with brand-applied styling.
user-invocable: true
---

# Carousel Generator

You are creating a PPTX carousel or slide deck using the Imperium carousel skill. Follow this workflow exactly.

## Step 1: Determine Carousel Type

Ask the user what type of carousel they want. Present these options:

1. **LinkedIn Carousel** — Square (1080x1080), 5-10 slides, one idea per slide, CTA at end
2. **Pitch Deck** — 16:9, 10-15 slides, investor-ready (Problem > Solution > Market > Traction > Ask)
3. **Educational Deck** — 16:9, 10-20 slides, tutorial/course format with progressive learning
4. **Product Demo Deck** — 16:9, 8-12 slides, feature showcase with screenshots
5. **Case Study Deck** — 16:9, 6-10 slides, Challenge > Approach > Results > Learnings
6. **Internal Report** — 16:9, 5-15 slides, metrics dashboard and progress updates

If the user's request already implies a type, confirm it and move on.

## Step 2: Gather Content

Ask for:
1. **Topic / subject** — What is this carousel about?
2. **Key points** — What are the main messages or data points to include?
3. **Target audience** — Who will see this? (investors, LinkedIn followers, team, clients)
4. **Number of slides** — Or use the type's default range
5. **Images** — Three paths:
   - **User has images:** Get file paths, verify they exist with `ls`
   - **User wants images but has none:** Trigger image sourcing — reference `skills/visual-media/SKILL.md`. Save to `media/images/[topic-slug]/` and use paths in slide plan.
   - **No images needed:** Use text-only layouts (content_single, content_bullets, etc.)

   After creating the slide plan (Step 4): if any slides use image layouts (image_full, image_left, image_right, image_grid, title_image) AND no image paths are available → offer to source images for those slides.

If the user provides a rough outline or content dump, use it to structure the slides. If they give minimal input, generate the content based on the topic.

## Step 3: Check Brand System

Read `brand/brand.json` if it exists. Apply brand colors and fonts to the carousel. If no brand file exists, use professional defaults (dark navy theme).

Reference the brand integration section in the carousel skill: `skills/carousel/SKILL.md`.

## Step 4: Plan the Slides

Create a slide plan table and show it to the user:

```
| # | Layout | Title | Key Content |
|---|--------|-------|-------------|
| 1 | title_bold | "Hook headline" | Cover slide |
| 2 | content_single | "Point 1" | Main message |
| ... | ... | ... | ... |
| N | cta_slide | "Take Action" | CTA with button |
```

Confirm with the user before generating. Let them adjust the plan.

## Step 5: Generate the Carousel

1. Write a Python script that imports layouts from `skills/carousel/cookbook/`
2. Set the correct slide dimensions for the carousel type
3. Call each layout function with the planned content
4. Save the .pptx file with a descriptive filename
5. Run the script with `python3`

**Slide dimensions by type:**
- LinkedIn Carousel: `Inches(10) x Inches(10)`
- All others (16:9): `Inches(13.333) x Inches(7.5)`

## Step 6: Report Results

After generation, report:
- File path of the generated .pptx
- Total slides created
- Layout types used
- File size
- Any manual steps needed (e.g., "replace [IMAGE] placeholders with your screenshots")

## Content Rules

Follow the writing rules from the carousel skill:
- One idea per slide
- Max 30 words per slide (LinkedIn) / 50 words (others)
- Font minimum: 24pt body, 36pt titles
- 40% whitespace target
- Always end with a CTA slide
- Hook on the first slide — stop the scroll / grab attention

## Available Layouts

Reference the 21 layouts in `skills/carousel/cookbook/`:

**Title (4):** title_centered, title_bold, title_image, title_gradient
**Content (8):** content_single, content_bullets, content_two_column, content_quote, content_stats, content_comparison, content_timeline, content_checklist
**Image (4):** image_full, image_left, image_right, image_grid
**Data (3):** data_bar_chart, data_pie_chart, data_table
**Special (2):** cta_slide, divider_slide

Full layout documentation: `skills/carousel/references/layout-guide.md`
