---
name: imperium:create-video
description: Create startup video content. Supports pitch videos, product demos, social clips, investor updates, and hiring videos. Bridges to Remotion for rendering.
user-invocable: true
---

# Create Video

You are creating startup video content using the Imperium Video framework. This command bridges to Remotion for programmatic video generation.

## Step 1: Detect Environment

Check for Remotion project in the current working directory:

1. Look for `remotion.config.ts` or `remotion.config.js`
2. Check `package.json` for `"remotion"` or `"@remotion/cli"` dependency
3. Look for `src/Root.tsx` or `src/Video.tsx`

**If Remotion is found:**
- Confirm: "Remotion project detected. Ready to create video compositions."
- Continue to Step 2.

**If Remotion is NOT found:**
- Inform the user and offer three options:
  1. **Set up Remotion now**: Guide them through `npx create-video@latest`
  2. **Create HTML slides instead**: Redirect to `/imperium:create-slides`
  3. **Create a PPTX carousel instead**: Redirect to `/imperium:create-carousel`
- If user chooses option 1, guide setup then continue to Step 2.
- If user chooses option 2 or 3, hand off to that command.

## Step 2: Choose Video Type

Present the 5 video templates:

```
Which type of video do you want to create?

1. Pitch Video (60-90s) — Concise startup pitch for investors or website
2. Product Demo (2-3 min) — Detailed product walkthrough
3. Social Clip (15-30s) — Scroll-stopping content for social media
4. Investor Update (60s) — Monthly/quarterly update for investors
5. Hiring Video (30-60s) — Attract talent with culture and role showcase
```

Ask the user to pick one, or describe what they need and recommend the best fit.

## Step 3: Gather Content

Based on the chosen video type, ask for the relevant information.

### For Pitch Video:
1. What does your product do? (one sentence)
2. What problem does it solve? (and for whom)
3. Key feature to demo (or provide screenshots/description)
4. Traction metrics (users, revenue, growth — pick top 2-3)
5. CTA — what should viewers do? (URL, sign up, book demo)

### For Product Demo:
1. What product/feature are you demoing?
2. Who is the target audience?
3. Top 3 features to showcase
4. For each feature: what's the user benefit?
5. CTA — what should viewers do next?

### For Social Clip:
1. What's the one key message or insight?
2. Target platform (TikTok, Instagram, LinkedIn, Twitter)?
3. Tone: educational, entertaining, provocative, or inspirational?
4. CTA: follow, visit site, try product, or comment?

### For Investor Update:
1. Key metric this period (and growth %)
2. Top 3-5 milestones achieved
3. Key challenge and how you're addressing it
4. Top 3 priorities for next period
5. Specific ask from investors

### For Hiring Video:
1. What role are you hiring for?
2. What does your team/company build?
3. How do you describe your culture in one sentence?
4. 3 key things about the role (impact, not tasks)
5. Where should candidates apply? (URL)

Skip any questions the user has already answered in their initial request.

## Step 4: Load Brand

Check if `brand/brand.json` exists in the project.

**If found:**
- Load brand colors, fonts, and tone of voice
- Apply to video theme:
  - Primary color → backgrounds, key text
  - Secondary color → supporting elements
  - Accent color → CTAs, highlights
  - Heading font → titles
  - Body font → body text, captions
- Confirm: "Brand loaded — using your brand colors and fonts."

**If not found:**
- Use the default dark theme (slate background, white text, blue accent)
- Mention: "No brand found. Using default theme. Run `/imperium:create-brand` to set up your brand."

## Step 5: Generate Video Content

Produce these deliverables:

### A. Video Script
Complete shot-by-shot script using this format:

```markdown
# {Video Title} — Script

## Overview
- Type: {Pitch Video / Product Demo / etc.}
- Duration: {target duration}
- Dimensions: {1920x1080 / 1080x1920 / 1080x1080}
- FPS: 30

## Shot List

### Shot 1: {Section Name} (0:00–0:XX)
**Visual:** {What's on screen}
**Text overlay:** {Any text displayed}
**Narration:** "{What is said}"
**Animation:** {Motion/transition description}
**Music:** {Volume/mood at this point}

### Shot 2: {Section Name} (0:XX–0:XX)
...
```

### B. Remotion Composition Code

Generate a complete, working Remotion composition:

1. **Main composition file** (`src/compositions/{VideoType}.tsx`)
   - Import Remotion primitives: `useCurrentFrame`, `useVideoConfig`, `interpolate`, `spring`, `Sequence`, `AbsoluteFill`
   - Define the composition component with typed props
   - Map each script section to a `<Sequence>` with correct frame timing
   - Apply brand theme throughout

2. **Section components** for each shot
   - Individual components for hook, problem, solution, demo, traction, CTA, etc.
   - Animations using `interpolate` and `spring`
   - Text animations (fade in, slide up, typewriter)
   - Number counter animations for metrics

3. **Theme/config** from brand or defaults

4. **Registration** in `src/Root.tsx` — add the new `<Composition>` with correct dimensions, FPS, and duration

### C. Render Instructions

Provide the exact commands to preview and render:

```bash
# Preview the video in browser
npx remotion preview src/index.ts

# Render to MP4
npx remotion render src/index.ts {composition-id} out/{filename}.mp4

# Render with specific quality
npx remotion render src/index.ts {composition-id} out/{filename}.mp4 --codec h264 --crf 18
```

If the video needs a vertical version (social clip, hiring video):
```bash
# Render vertical version
npx remotion render src/index.ts {composition-id}-vertical out/{filename}-vertical.mp4
```

## Step 6: Offer Next Steps

After generating the video:

1. **Preview**: "Run `npx remotion preview` to see your video in the browser"
2. **Adjust**: "Want to change timing, text, or colors? Just tell me what to update"
3. **Render**: "When you're happy, render with the command above"
4. **Multi-format**: "Need this in a different aspect ratio? I can create a vertical/square version"
5. **Series**: "Want to create more videos? I can batch-generate a content series"

## Reference

Load the video skill from `skills/video/SKILL.md` for detailed template structures, timing guides, and brand integration rules.

Load video type details from `skills/video/references/video-types.md` for full script templates and platform-specific guidance.
