---
name: imperium:create-slides
description: Create an HTML presentation. Zero dependencies — generates a single .html file that works as slides in any browser. 12 style presets available.
user-invocable: true
---

# Create HTML Slides

You are creating an HTML presentation using the Imperium Slides framework. The output is a single self-contained .html file that works as a full presentation in any browser.

## Step 1: Gather Content

Ask the user for:

1. **Topic/title** of the presentation
2. **Audience** — who is this for? (investors, team, customers, conference, etc.)
3. **Key points** — what must be covered? (or let the user provide an outline)
4. **Number of slides** — suggest 8-15 for most presentations
5. **Style preference** — show the 12 presets or ask for a vibe

Skip any questions the user has already answered.

If the user provides a document, outline, or topic and says "make slides" — use your judgment on audience, slide count, and style. Don't over-ask.

## Step 2: Select Style

Present the 12 style presets:

```
Choose a style (or describe what you want):

 1. Midnight    — Dark navy, white text, blue accent (tech/professional)
 2. Clean       — White bg, dark text, minimal (universal)
 3. Startup     — Dark bg, purple-pink gradient (demo day energy)
 4. Corporate   — Light gray, navy, serif headings (boardroom)
 5. Creative    — Bold warm colors, large type (creative pitches)
 6. Developer   — Terminal dark, monospace, grid bg (tech talks)
 7. Warm        — Cream bg, brown text, organic (friendly)
 8. Neon        — Black bg, neon green-blue glow (high energy)
 9. Nature      — Forest green palette (sustainability/wellness)
10. Minimal     — Pure black & white, max whitespace (editorial)
11. Retro       — Vintage colors, serif fonts (storytelling)
12. Gradient    — Smooth gradient per slide (dynamic/creative)
```

If the user's brand exists (`brand/brand.json`), also offer:
- **Brand** — uses your brand colors and fonts with a dark or light base

Load full preset CSS from `skills/slides/references/style-presets.md`.

## Step 3: Load Brand (if available)

Check if `brand/brand.json` exists.

**If found:**
- Load brand colors and fonts
- If user selected "Brand" style: override preset colors entirely with brand palette
- If user selected a named preset: apply the preset but swap the accent color to brand primary
- Add brand logo to the title slide if logo file exists in `brand/assets/`

**If not found:**
- Apply the selected preset as-is
- Mention: "No brand found. Using preset defaults. Run `/imperium:create-brand` to set up your brand."

## Step 4: Generate the Presentation

Create a complete, working .html file using the template from `skills/slides/SKILL.md`.

### Content Generation Rules

1. **Title slide** — always first. Presentation title + subtitle (audience or date).

2. **Content slides** — follow the user's outline. For each point:
   - Write a clear, short headline (under 8 words)
   - Use 3-5 bullet points maximum per slide
   - Bold key terms with `<strong>` tags (renders in accent color)
   - Add speaker notes with talking points

3. **Choose the right slide type** for each piece of content:
   - Data/metrics → stats grid slide
   - Comparison → two-column slide
   - Quote/testimonial → quote slide
   - Code/technical → code slide
   - Visual → image slide
   - Everything else → standard content slide

4. **CTA/closing slide** — always last. Clear next step or thank you.

5. **Slide count guidance:**
   - 5-minute talk → 8-10 slides
   - 10-minute talk → 12-18 slides
   - 20-minute talk → 20-30 slides
   - Pitch deck → 10-14 slides
   - Quick update → 5-8 slides

### HTML Generation Rules

- Use the full base template from the SKILL.md
- Replace CSS variables with the selected preset values
- Generate each slide as a `<div class="slide">` element
- Add `class="slide-title"` for title/CTA slides
- Include `<div class="notes">` inside every slide with speaker notes
- Ensure all JavaScript is included inline (navigation, overview, touch)
- Set the `<title>` tag to the presentation title
- The file must be completely self-contained — no external references

## Step 5: Save and Guide

1. **Save the file** — write it to the current directory or a specified path
   - Default filename: `{topic-slug}-slides.html` (e.g., `q1-update-slides.html`)
   - Ask if the user wants a different filename/location

2. **Provide instructions:**
   ```
   Your presentation is ready!

   Open: {filepath}

   Controls:
   → / Space  — Next slide
   ← — Previous slide
   F — Fullscreen
   P — Speaker notes
   Esc — Slide overview
   Ctrl+P — Print to PDF (Chrome recommended)

   Touch: Swipe left/right on mobile
   Share: Just send the .html file — recipients double-click to view
   ```

3. **Offer enhancements:**
   - "Want to adjust any slides? Tell me which ones"
   - "Need a different style? I can re-theme instantly"
   - "Want to add more slides? Just describe the content"
   - "Need a PDF version? Open in Chrome and press Ctrl+P"

## Reference

Load the slides skill from `skills/slides/SKILL.md` for the HTML template, slide types, and style preset definitions.

Load style details from `skills/slides/references/style-presets.md` for complete CSS per preset.
