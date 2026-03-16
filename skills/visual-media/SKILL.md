---
name: visual-media
description: 'Image and video sourcing with AI-powered visual review. Searches for relevant visuals, downloads candidates, and uses Claude multimodal Read tool to visually evaluate each image for relevance, quality, and brand fit. Works standalone or as prerequisite for LinkedIn posts, carousels, and research. Use when the user mentions: image, images, photo, find images, find visuals, stock photo, stock video, b-roll, visual media, pictures, find pictures, source images, get images.'
user-invocable: false
---

# Visual Media Sourcing Skill

Intelligent image and video sourcing with AI-powered visual review. Finds, downloads, and visually evaluates media using Claude's multimodal capabilities.

---

## When to Source Images

Detect whether image sourcing is needed based on context signals.

### AUTO-SOURCE (proceed without asking)
- User explicitly asks for images ("find images", "get photos", "source visuals")
- Carousel plan includes image layouts (image_full, image_left, image_right, image_grid, title_image)
- Post type is Product Launch, Case Study, or Behind the Scenes
- User mentions "with images", "add photos", "include visuals"

### RECOMMEND (suggest, don't auto-run)
- Post type is Milestone, Educational, or Personal Story
- Product Demo decks without user-provided screenshots
- Behind the Scenes content without user photos
- Tell user: "An image would boost engagement ~50%. Want me to find relevant images?"

### SKIP (do not source)
- User said "text only" or "no images"
- Content type is SOP, runbook, or playbook
- Carousel plan uses only text layouts (content_single, content_bullets, etc.)
- Question/Poll post type (text-only performs better)

### ALREADY PROVIDED (use what exists)
- User gave specific file paths to images
- `media/images/` directory has files matching the current topic
- Research phase already captured relevant screenshots

---

## Image Sourcing Protocol

### Phase 1: Search

Build diverse search queries from the topic to maximize coverage.

1. Extract 2-3 core concepts from the topic
2. Generate 3-5 search queries combining concepts with visual terms:
   - `"[topic] high quality photo"`
   - `"[topic] professional image"`
   - `"[topic] stock photo free use"`
   - `"[topic] [specific aspect] visual"`
   - `"[topic] unsplash OR pexels OR pixabay"`
3. Prioritize free-use sources:
   - **Unsplash** (unsplash.com) — high quality, free commercial use
   - **Pexels** (pexels.com) — free, no attribution required
   - **Pixabay** (pixabay.com) — free, CC0 license
4. Use WebSearch for each query
5. If imperium-crawl is available, also use: `imperium-crawl search --query "[topic] free stock photo" --count 10`
6. Collect 8-15 candidate image URLs

### Phase 2: Download

1. Create download directory: `media/images/[topic-slug]/`
   - Topic slug: lowercase, hyphens for spaces, no special chars (e.g., `ai-team-collaboration`)
2. Download each candidate:
   ```bash
   curl -sL -o "media/images/[topic-slug]/candidate_[N].jpg" "[URL]"
   ```
3. Verify each download:
   - File size > 10KB (smaller = broken/placeholder)
   - Valid image format (jpg, png, webp)
   - File actually exists after download
4. Skip broken downloads silently — move to next candidate
5. Log: "Downloaded X/Y candidates successfully"

### Phase 3: Visual Review

**CRITICAL STEP — This is what makes this skill valuable.**

For EACH downloaded image, use the **Read tool** on the file path. Claude's multimodal capability will see the actual image contents.

Evaluate each image on 4 criteria:

**RELEVANCE** (most important):
- Does the image actually depict the topic?
- Is it specific enough? (not a generic "business" stock photo for an AI topic)
- Would the target audience immediately connect this image to the content?
- Is it the right type? (photo vs illustration vs screenshot — match the need)

**QUALITY:**
- Sharp and well-composed? (not blurry, cropped badly, or low-res)
- Professional enough for the intended use?
- Good lighting and color? (not washed out or oversaturated)
- Minimum resolution for intended platform (see review-criteria.md)

**BRAND FIT** (if brand.json exists):
- Read `brand/brand.json` for color palette and personality
- Does the image complement (not clash with) the brand colors?
- Does the mood/tone match the brand personality?
- Would this look natural alongside brand content?

**CONTENT TRAPS** (auto-reject):
- Visible watermarks
- AI-generated artifacts (uncanny hands, text gibberish, weird patterns)
- Copyright indicators or stock photo IDs
- Offensive, misleading, or inappropriate content
- Text-heavy images that won't work at small sizes

**Verdict for each image:**
- **APPROVE** — Good relevance, quality, and fit. Ready to use.
- **MAYBE** — Decent but not great. Keep as backup.
- **REJECT** — Poor relevance, quality issues, or content traps. Delete.

For detailed scoring criteria: `references/review-criteria.md`

### Phase 4: Select & Present

1. Rank approved images by quality (best first)
2. Present top 3-5 to user:

```
## Image Results for "[topic]"

### Image 1 (Recommended)
[Read the image to show it]
- **File:** `media/images/[slug]/candidate_3.jpg`
- **Score:** 8.5/10
- **Why:** [1-line reason — e.g., "Shows diverse team collaborating on laptops — directly depicts remote collaboration"]

### Image 2
[Read the image to show it]
- **File:** `media/images/[slug]/candidate_7.jpg`
- **Score:** 7.8/10
- **Why:** [1-line reason]

### Image 3
...

**Rejected:** X images didn't pass visual review (generic stock, wrong topic, low quality)
```

3. Let user pick, or auto-select top-ranked if they said "just pick the best"

### Phase 5: Fallback

If fewer than 2 images approved after Phase 3:

1. **Try again:** Generate 3 more search queries with different angles:
   - Different terminology for the same concept
   - More specific or more general queries
   - Different source focus (e.g., specifically target Unsplash API)
2. **Repeat Phases 2-3** with new candidates
3. **Still insufficient?** Be honest:
   - "I couldn't find strong matches for this specific topic."
   - "A photo of YOU performing much better than any stock image on LinkedIn anyway — that's your best bet for this one."
   - "Consider creating a custom graphic or screenshot instead."

---

## Video Sourcing

Same pattern as images, adapted for video limitations.

### Search
- Search for stock video, b-roll, demo clips, explainer videos
- Use queries: `"[topic] stock video"`, `"[topic] b-roll footage"`, `"[topic] demo clip"`
- Sources: Pexels Videos, Pixabay Videos, Coverr, Mixkit
- If imperium-crawl available: `imperium-crawl youtube --action search --query "[topic] b-roll"`

### Download & Organize
- Save to `media/video/[topic-slug]/`
- For large video files, save URL references instead of downloading:
  ```
  media/video/[topic-slug]/video-library.md
  ```

### Review Limitations
- Claude cannot watch video files directly
- Review via: metadata, title/description relevance, source credibility
- If thumbnails are available, use Read tool on thumbnails
- Check video duration (15-60 seconds for social, 1-5 minutes for demos)

### Output
Curated video reference library:
```markdown
## Video Library: [topic]

### Recommended
1. **[Title]** — [Source URL]
   - Duration: X:XX | Resolution: 1080p
   - Relevance: [why it fits]
   - License: [free/attribution/paid]

### Alternatives
2. ...
```

---

## Output Convention

All sourced media follows this directory structure:

```
media/
  images/
    [topic-slug]/          # Downloaded + approved images
      candidate_1.jpg
      candidate_3.jpg      # (numbering may skip rejected files)
      ...
  video/
    [topic-slug]/          # Downloaded clips or URL references
      video-library.md     # Curated reference list
      clip_1.mp4           # (if small enough to download)
      ...
```

---

## Integration Points

### With Carousel (`skills/carousel`)
- Carousel detects image layouts in slide plan → triggers visual-media if no images provided
- Visual-media saves approved images to `media/images/[topic-slug]/`
- Carousel references file paths in image layout functions (image_full, image_left, etc.)

### With LinkedIn (`skills/linkedin`)
- LinkedIn post generator evaluates if post type benefits from images
- If sourcing needed → invokes visual-media protocol
- Approved image path included in posting package
- Target format: 1080x1350px portrait for LinkedIn

### With Research (`skills/research`)
- Research Phase 2B (UI/UX Audit) captures competitor screenshots
- Visual-media's review criteria complement research's validation.md
- For competitor screenshots, apply BOTH research validation rules AND visual-media quality checks
- Cross-reference: `skills/research/references/validation.md`

### Standalone
- User runs `/imperium:find-images` directly
- Full protocol: search → download → visual review → present results
- User picks images for any purpose
