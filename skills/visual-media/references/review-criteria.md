# Visual Media Review Criteria

Scoring and classification rules for image and video evaluation. Extends the research skill's validation rules with content-specific criteria.

**Cross-reference:** For competitor screenshots and product UI images, also apply the validation rules from `skills/research/references/validation.md` (KEEP/MAYBE/REJECT classification, naming conventions, common traps).

---

## Relevance Checklist (General/Stock Images)

Score each criterion YES/NO. Image must pass at least 4 of 5 to be relevant.

1. **Topic match** — Does the image actually depict the topic, not just a loosely related concept?
2. **Specificity** — Is it specific enough to add value? (A laptop on a desk is NOT specific to "AI coaching")
3. **Audience resonance** — Would the target audience immediately connect this image to the content?
4. **Emotional alignment** — Does the image evoke the right emotion for the content? (inspiring, professional, urgent, warm)
5. **Context fit** — Does the image work for the intended platform and content format?

---

## Quality Scoring (1-5)

| Score | Label | Description | Example |
|-------|-------|-------------|---------|
| 5 | Excellent | Professional-grade, sharp, perfect composition | Magazine-quality photo, perfect lighting |
| 4 | Good | High quality, minor imperfections | Solid stock photo, slightly generic composition |
| 3 | Acceptable | Usable but not impressive | Decent quality, predictable framing |
| 2 | Poor | Low resolution, bad composition, or dated | Grainy, bad crop, early-2010s stock feel |
| 1 | Reject | Unusable — blurry, broken, wrong content | Thumbnail resolution, corrupted file, wrong subject |

**Minimum for approval:** Score 3+ for general content, Score 4+ for brand-critical content (pitch decks, landing pages).

---

## Brand Fit Evaluation

When `brand/brand.json` exists, evaluate these dimensions:

### Color Harmony
- Does the image's dominant color palette complement the brand colors?
- Would the image look natural on a slide/post with the brand's background color?
- Strong clashes (e.g., brand is navy/gold, image is neon green) = auto-reject

### Tone Match
- Brand personality: formal → need polished, corporate imagery
- Brand personality: playful → can use casual, colorful, creative imagery
- Brand personality: technical → prefer clean, minimal, data-oriented visuals
- Mismatch between image mood and brand personality = downgrade score by 1

### Visual Consistency
- Would this image look like it belongs with other brand content?
- Does it support or undermine the brand's visual identity?

---

## Platform-Specific Specs

### LinkedIn Post Image
- **Ideal:** 1080 x 1350px (portrait, 4:5 ratio)
- **Minimum:** 552 x 368px
- **Format:** JPG, PNG
- **Notes:** Portrait outperforms landscape on mobile feeds

### LinkedIn Carousel
- **Ideal:** 1080 x 1080px (square, 1:1 ratio)
- **Format:** Images used within PPTX slides
- **Notes:** Must be readable when slide is viewed at phone-screen size

### General Web / Blog
- **Ideal:** 1200 x 630px (landscape, ~1.9:1 ratio)
- **Minimum:** 600 x 315px
- **Notes:** This is the og:image ratio for social previews

### Presentation (16:9)
- **Ideal:** 1920 x 1080px
- **Minimum:** 1280 x 720px
- **Notes:** Must look good on projector/screen share

---

## Content-Specific Traps

### Watermarks
- Visible watermark = **instant REJECT**
- Subtle/semi-transparent watermarks in corners — check carefully
- Shutterstock, Getty, Adobe Stock watermarks are most common

### AI-Generated Artifacts
- Extra or malformed fingers/hands
- Gibberish text in signs, books, or screens
- Uncanny facial expressions or skin textures
- Impossible reflections or shadows
- Repeating patterns that break reality
- If detected = **REJECT** (AI images hurt credibility)

### Copyright Indicators
- Stock photo ID numbers visible
- Source attribution baked into image
- "Sample" or "Preview" text overlays
- If detected = **REJECT**

### Generic Stock Cliches (downgrade by 1 point)
- Handshake in front of city skyline
- Person pointing at invisible holographic screen
- Diverse team high-fiving in glass office
- Businessman jumping over chasm
- These are SO overused they signal "low effort" to the audience

---

## Free-Use Source Preference

Always prioritize sources with clear free-use licenses:

| Source | License | Attribution? | Commercial Use? |
|--------|---------|-------------|-----------------|
| **Unsplash** | Unsplash License | No (appreciated) | Yes |
| **Pexels** | Pexels License | No | Yes |
| **Pixabay** | Pixabay License | No | Yes |
| **Coverr** (video) | Free | No | Yes |
| **Mixkit** (video) | Free | No | Yes |

**Avoid** unless user has paid access: Shutterstock, Getty, Adobe Stock, iStock.

---

## Review Workflow Summary

For each downloaded image:

1. **Read** the image file using the Read tool (multimodal visual review)
2. **Score** relevance (pass 4/5 checklist items?)
3. **Score** quality (1-5 scale)
4. **Check** brand fit (if brand.json exists)
5. **Check** content traps (watermarks, AI artifacts, copyright)
6. **Verdict:** APPROVE (score 3+, passes relevance, no traps) / MAYBE (borderline) / REJECT (fails any critical check)
7. **Log** verdict with 1-line reason
