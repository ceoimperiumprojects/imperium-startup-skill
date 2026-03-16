---
name: imperium:find-images
description: Find and download high-quality images or video with AI-powered visual review. Searches free sources, downloads candidates, and uses Claude's multimodal vision to evaluate each one for relevance, quality, and brand fit.
user-invocable: true
---

# Image & Video Sourcing

You are finding and curating visual media using the Imperium visual-media skill. Follow this workflow.

## Step 1: Understand the Request

Ask for (or extract from the user's message):

1. **Topic** — What images are needed? Be specific.
2. **Quantity** — How many images? (default: 3-5 approved)
3. **Purpose** — What are they for?
   - LinkedIn post (target: 1080x1350px portrait)
   - Carousel/deck (target: 1080x1080px square or 1920x1080px 16:9)
   - General content / blog / website
   - Research / reference library
4. **Style preference** — Photo, illustration, screenshot, or any?
5. **Video?** — If user mentions video, b-roll, or clips, include video sourcing.

If the user gives a clear topic in one message, skip the Q&A and proceed directly.

## Step 2: Check Brand Context

Read `brand/brand.json` if it exists. Extract:
- Color palette (for brand fit evaluation)
- Brand personality (for tone matching)
- Confirm: "Found your brand profile. I'll evaluate images for brand fit too."

If no brand: "No brand profile found. I'll use general quality criteria."

## Step 3: Execute Sourcing Protocol

Reference the full protocol in `skills/visual-media/SKILL.md`:

1. **Search** — Build 3-5 queries, search free sources, collect 8-15 candidate URLs
2. **Download** — Save to `media/images/[topic-slug]/`, verify file integrity
3. **Visual Review** — Use Read tool on EACH image. Evaluate relevance, quality, brand fit, content traps
4. **Select** — Rank approved images, present top results with scores and reasons
5. **Fallback** — If insufficient results, try alternative queries or advise the user

Detailed review criteria: `skills/visual-media/references/review-criteria.md`

## Step 4: Present Results

Show approved images with:
- The image itself (via Read tool)
- File path
- Quality score (X/10)
- 1-line relevance reason
- Platform-specific notes (if applicable)

Let the user pick their favorites or confirm the top-ranked selection.

If user wants video too, present a curated video library with URLs, descriptions, and relevance notes.
