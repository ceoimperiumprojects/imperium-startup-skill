---
name: video
description: 'Video content creation bridge to Remotion. Provides startup-specific video templates (pitch video, product demo, social clip, investor update, hiring video) with brand integration. Detects Remotion project and guides video creation. Falls back to HTML slides or carousel if Remotion is not available. Triggers on: video, MP4, Remotion, demo video, explainer, social clip, video content, animation, motion graphics, video pitch.'
user-invocable: false
---

# Video Content Creation — Remotion Bridge

Create startup video content using Remotion for programmatic video generation. This skill detects your Remotion setup, provides startup-specific templates, and bridges brand identity into video compositions.

## Keywords

video, MP4, Remotion, demo video, explainer, social clip, video content, animation, motion graphics, video pitch, product demo, investor update, hiring video, pitch video, video script, video template, startup video, promotional video, video marketing, screen recording, animated explainer

## Setup Detection

Before any video creation, detect the user's Remotion environment:

### Step 1: Check for Remotion Project

```
Look for these indicators (in order):
1. remotion.config.ts or remotion.config.js in project root
2. package.json containing "remotion" or "@remotion/cli" as a dependency
3. src/Root.tsx or src/Video.tsx (common Remotion entry points)
4. Any .tsx files importing from "remotion"
```

### Step 2: Route Based on Detection

**If Remotion is found:**
- Confirm version (check package.json for version number)
- Identify existing compositions (look for `<Composition>` components)
- Enter full video creation mode — generate compositions, sequences, and render commands
- Check for `@remotion/lambda` for cloud rendering capability

**If Remotion is NOT found:**
- Inform the user that Remotion is required for video rendering
- Offer three paths:
  1. **Install Remotion**: `npx create-video@latest` — sets up a full Remotion project
  2. **Use HTML slides instead**: Suggest `/imperium:create-slides` for presentation content that can be screen-recorded
  3. **Use carousel instead**: Suggest `/imperium:create-carousel` for visual slide decks (PPTX)
- If user chooses to install, guide them through setup and then continue with video creation

## Brand Integration

Before generating any video content, check if `brand/brand.json` exists in the project.

**If brand files exist:**
- Read `brand/brand.json` and extract: primary color, secondary color, accent color, fonts
- Read `brand/tone-of-voice.md` for script writing style
- Map brand colors to Remotion theme variables:
  ```typescript
  const theme = {
    primaryColor: brand.colors.primary,      // Main backgrounds, key text
    secondaryColor: brand.colors.secondary,  // Supporting elements
    accentColor: brand.colors.accent,        // CTAs, highlights, emphasis
    headingFont: brand.fonts.heading,        // Titles, section headers
    bodyFont: brand.fonts.body,              // Body text, captions
    backgroundColor: brand.colors.background // Slide backgrounds
  };
  ```
- Apply tone-of-voice rules to video script and captions
- Use brand logo if `brand/assets/logo.svg` or `brand/assets/logo.png` exists

**If no brand files exist:**
- Use a clean, modern default theme:
  - Background: #0F172A (dark slate)
  - Text: #F8FAFC (near white)
  - Accent: #3B82F6 (blue)
  - Heading font: Inter or system sans-serif
  - Body font: Inter or system sans-serif
- Use a confident, professional default voice

## Video Templates

### 1. Pitch Video (60–90 seconds)

**Purpose:** Concise startup pitch for investors, website hero, or cold outreach.

**Structure:**
| Section | Duration | Content | Visual Direction |
|---------|----------|---------|------------------|
| Hook | 5s | Bold statement or surprising stat that frames the problem | Full-screen text animation, dramatic pause |
| Problem | 15s | Paint the pain point vividly — who suffers, how much, why now | Icons/illustrations of the problem, dark/tense mood |
| Solution | 20s | Your product as the answer — what it does in one sentence, then show it | Product screenshots/demo with animated callouts |
| Demo | 20s | Live product walkthrough or key feature showcase | Screen recording with cursor highlights, zoom effects |
| Traction | 10s | Key metrics that prove momentum — users, revenue, growth rate | Animated counters, chart animations, logos of customers |
| CTA | 10s | Clear ask — visit site, book demo, join waitlist | Brand logo, URL, QR code, strong closing statement |

**Script Guidelines:**
- Hook must create tension or curiosity in under 5 seconds
- Problem section: use "you" language — speak to the audience's pain
- Solution: lead with the outcome, not the feature
- Traction: pick 2-3 metrics maximum, animate them counting up
- CTA: one clear action, repeat the URL or QR code

**Music Mood:** Inspirational, building momentum. Start subtle, crescendo at traction.

### 2. Product Demo (2–3 minutes)

**Purpose:** Detailed product walkthrough for website, sales enablement, or onboarding.

**Structure:**
| Section | Duration | Content | Visual Direction |
|---------|----------|---------|------------------|
| Context | 15s | Who this is for and what problem it solves | Title card + brief problem statement |
| Feature 1 | 30s | Core feature deep-dive with use case | Screen recording + animated annotations |
| Feature 2 | 30s | Second key feature with real example | Screen recording + callout overlays |
| Feature 3 | 30s | Third feature or workflow demonstration | Screen recording + transition animations |
| Summary | 15s | Recap key benefits (not features) | Benefit bullets animating in |
| CTA | 10s | Sign up, start trial, book demo | Logo + URL + action button animation |

**Script Guidelines:**
- Open with the user's goal, not your product name
- Each feature section: show the action, then explain the benefit
- Use captions throughout — many viewers watch without sound
- Transitions between features should feel natural, not jarring
- End on the strongest benefit, not the last feature

**Technical Notes:**
- Record at 1920x1080 minimum for screen captures
- Use 2x zoom on small UI elements
- Add cursor highlighting or spotlight effects
- Include keyboard shortcut callouts where relevant

**Music Mood:** Upbeat, modern, not distracting. Consistent energy throughout.

### 3. Social Clip (15–30 seconds)

**Purpose:** Scroll-stopping content for TikTok, Instagram Reels, LinkedIn, or Twitter/X.

**Structure:**
| Section | Duration | Content | Visual Direction |
|---------|----------|---------|------------------|
| Hook | 3s | Pattern interrupt — bold text, surprising claim, or question | Large text animation, high contrast |
| Value | 15–20s | One insight, tip, stat, or product highlight | Fast cuts, text overlays, dynamic movement |
| CTA | 3–5s | Follow, visit, try it, comment | Brand logo + clear action text |

**Format Options:**
- **Vertical (9:16)**: TikTok, Instagram Reels, YouTube Shorts — 1080x1920
- **Square (1:1)**: LinkedIn feed, Instagram feed — 1080x1080
- **Horizontal (16:9)**: Twitter/X, YouTube, website embed — 1920x1080

**Script Guidelines:**
- First 2 seconds must stop the scroll — use motion, bold text, or a provocative statement
- One idea only — do not cram multiple points
- Text overlays are mandatory — assume no sound
- Use brand colors aggressively for recognition
- End with a hook for the next video or a clear CTA

**Music Mood:** Trending audio if possible, energetic beat, bass-driven.

### 4. Investor Update Video (60 seconds)

**Purpose:** Monthly or quarterly update for investors, advisory board, or team.

**Structure:**
| Section | Duration | Content | Visual Direction |
|---------|----------|---------|------------------|
| Key Metric | 10s | The one number that matters most this period | Large animated number with context |
| Milestones | 20s | What was achieved — launches, hires, deals, features | Timeline or milestone cards animating in |
| Challenges | 10s | Honest blockers and how you're addressing them | Clean text on subtle background |
| Next Quarter | 15s | Top 3 priorities and targets | Numbered list with icons |
| Ask | 5s | Specific help needed — intros, advice, resources | Direct text with contact info |

**Script Guidelines:**
- Lead with your strongest metric — revenue, users, or growth rate
- Milestones: be specific with dates and numbers
- Challenges: be honest but solution-oriented — "We hit X, so we're doing Y"
- Next quarter: concrete goals with measurable targets
- Ask: be specific — "We need intros to Series A funds focused on B2B SaaS"

**Tone:** Confident but transparent. Investors respect honesty over spin.

**Music Mood:** Subtle, ambient background. This is about data, not hype.

### 5. Team / Hiring Video (30–60 seconds)

**Purpose:** Attract talent by showcasing culture, mission, and open roles.

**Structure:**
| Section | Duration | Content | Visual Direction |
|---------|----------|---------|------------------|
| Culture Hook | 5s | One sentence that captures your team's energy | Bold text or team photo with animation |
| What We Build | 15s | Mission and product impact — why it matters | Product shots mixed with impact visuals |
| Team Vibe | 15s | How the team works — remote, async, rituals, values | Candid team photos or workspace shots |
| The Role | 10s | What you're looking for — key skills and impact | Role title + 3 key bullet points |
| Apply CTA | 5s | How to apply — URL, email, or job board link | Brand logo + careers URL |

**Script Guidelines:**
- Lead with energy and authenticity — avoid corporate language
- Show, don't tell — "We ship weekly" beats "We move fast"
- Highlight what makes your team different — rituals, tools, values
- Role description: focus on impact ("You'll build X that affects Y users")
- CTA: make it easy — one link, no hoops

**Music Mood:** Energetic, uplifting, reflects team personality.

## Video Script Framework

For every video, generate a complete script document containing:

### Shot List
```
Shot #  | Time    | Visual                  | Text/Narration              | Notes
--------|---------|-------------------------|-----------------------------|--------
1       | 0:00-05 | Full-screen text anim   | "What if you could..."      | Hook
2       | 0:05-20 | Problem illustration    | "Every day, teams waste..." | Tension
...
```

### Visual Direction
- Color palette (from brand or template default)
- Typography choices with sizes
- Animation style: smooth/snappy/minimal/bold
- Transition type between sections: cut/fade/slide/morph

### Timing Guide
- Total duration target
- Per-section breakdown with flexibility ranges
- Pacing notes (where to breathe, where to punch)

### Music Direction
- Mood keywords (3-5 descriptors)
- BPM range suggestion
- Recommended sources: Artlist, Epidemic Sound, YouTube Audio Library
- When music should swell, drop, or fade

### Captions/Subtitles
- All spoken text formatted for subtitle generation
- Recommended caption style: font, size, position, background
- Highlight keywords in captions for emphasis

## Remotion Composition Structure

When generating Remotion code, follow this structure:

```typescript
// src/compositions/{VideoType}/index.tsx
import { Composition } from 'remotion';
import { {VideoType} } from './{VideoType}';

// Register the composition
<Composition
  id="{video-type}"
  component={{VideoType}}
  durationInFrames={fps * totalSeconds}
  fps={30}
  width={1920}
  height={1080}
  defaultProps={{
    theme: brandTheme,
    content: scriptContent,
  }}
/>
```

Each section of the video maps to a Remotion `<Sequence>`:
```typescript
<Sequence from={startFrame} durationInFrames={sectionFrames}>
  <SectionComponent {...sectionProps} />
</Sequence>
```

### Rendering Commands
```bash
# Preview in browser
npx remotion preview src/index.ts

# Render to MP4
npx remotion render src/index.ts {composition-id} out/video.mp4

# Render specific quality
npx remotion render src/index.ts {composition-id} out/video.mp4 --codec h264 --crf 18

# Render vertical (9:16)
npx remotion render src/index.ts {composition-id} out/video.mp4 --height 1920 --width 1080
```

## Quality Checklist

Before delivering any video composition:

- [ ] Brand colors and fonts applied (if brand exists)
- [ ] All text is readable at target resolution
- [ ] Animations are smooth (no jarring jumps)
- [ ] Timing matches the script breakdown
- [ ] Captions included for accessibility
- [ ] CTA is clear and visible
- [ ] File renders without errors
- [ ] Output format matches target platform requirements
- [ ] Music/audio direction is documented
- [ ] Thumbnail frame identified (best frame for preview)
