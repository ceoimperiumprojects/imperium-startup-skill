# Validation Rules

Quality gates for all research artifacts: screenshots, images, and videos.

## Screenshot & Image Validation

**EVERY image collected must be validated before adding to the research library.** Without this step, you end up with a folder full of random logos, stock photos, social media avatars, and unrelated graphics instead of actual product UI screenshots.

### Relevance Check (must pass ALL)

- Is this actually showing the product's UI/interface?
- Is this the CORRECT product? (not a different product with similar name)
- Is this a current version? (not an outdated/old UI)
- Is this a real screenshot? (not a mockup/rendering unless labeled as such)

### Content Type Classification

**KEEP:**
- Product UI screenshot (dashboard, main screen, feature)
- Product onboarding/signup flow
- Product mobile app screenshot
- Product pricing page screenshot
- Product settings/config screen
- Product in-context usage (real user's screen)

**MAYBE** (keep only if real UI unavailable):
- Marketing mockup
- Comparison infographic (if contains real UI elements)

**REJECT:**
- Company logo only
- Team/founder photo
- Generic stock photo
- Social media post screenshot (unless showing product)
- Blog post header image
- Unrelated product with similar name
- Icon or favicon only
- Certificate/badge/award image
- Blurry or unreadable image
- Duplicate of already-collected image

### Image Naming Convention

```
[competitor]_[screen-type]_[number].png

Examples:
crewclaw_dashboard_01.png
crewclaw_onboarding_01.png
crewclaw_pricing_01.png
uniclaw_chat-ui_01.png
uniclaw_mobile_01.png
```

### Validation Workflow

1. Collect all images from search/scraping
2. Look at EACH image — does it actually show the product UI?
3. If the image is a logo, stock photo, or unrelated — REJECT immediately
4. If the image shows product UI — classify by screen type and KEEP
5. If unsure — open the source page to check context
6. Name kept images with the convention above
7. Log rejected images with reason (for audit trail)

### Visual Verification with Read Tool

**CRITICAL:** The validation checks above MUST be performed visually, not assumed from filename or URL alone.

For each downloaded image:
1. Use the **Read tool** on the image file path — Claude will see the image contents
2. Apply the Relevance Check criteria while looking at the actual image
3. Classify as KEEP / MAYBE / REJECT based on what you SEE, not what you expect
4. Log your verdict with a 1-line reason

This catches: wrong-product screenshots, stock photos with misleading filenames, heavily stylized marketing mockups, and outdated UI that URLs don't reveal.

### Common Traps

- Google Image results for "[product] UI" often return blog headers, not actual UI
- Many competitor pages use stylized mockups that look like UI but aren't real
- Products with generic names (e.g., "Flow", "Base") will return images of wrong products
- App Store screenshots are often heavily designed marketing images, not raw UI
- Social media previews (og:image) are almost never product screenshots

### imperium-crawl Screenshot Capture

When imperium-crawl is available, capture verified screenshots directly:

```bash
# Full-page screenshot of a competitor's product
imperium-crawl screenshot --url "https://competitor.com/dashboard" --full-page

# Pricing page capture
imperium-crawl screenshot --url "https://competitor.com/pricing" --full-page

# Multiple pages in sequence
imperium-crawl screenshot --url "https://competitor.com/features"
imperium-crawl screenshot --url "https://competitor.com/about"
```

---

## Video Relevance Validation

**For EACH video found, VALIDATE before documenting:**

### Relevance Check (before documenting)

- Is this video actually about the correct product/company? (Generic names like "Flow" or "Base" will return wrong results)
- Does the video show the ACTUAL product? (not just talking about it)
- Is this the current version? (check publish date — older than 6 months may show outdated UI)
- Is this a real demo/review? (not a spam/clickbait video with misleading title)
- Is the video in a language we can understand? (or has subtitles?)

### REJECT if:

- Wrong product (same name, different company)
- Clickbait title with no actual product shown
- Video is just reading the product's website out loud with no new info
- Under 30 seconds with no substance
- Auto-generated/AI-narrated content farm video
- Product shown is a completely different version (e.g., v1 when v3 exists)

### KEEP if:

- Shows actual product UI in use
- Has real user/reviewer opinions
- Demonstrates features with screen recording
- Founder/team explaining the product
- Side-by-side comparison with competitors

### Video Library Index

After collecting, create master index sorted by:
1. **By competitor** — All videos for each competitor grouped
2. **By type** — All demos together, all reviews together, etc.
3. **By watch priority** — Must-watch first
4. **By recency** — Newest first (most current product state)
5. **By views** — Most popular first (market signal)
