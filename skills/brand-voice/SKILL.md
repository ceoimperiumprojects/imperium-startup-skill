---
name: brand-voice
description: 'Brand identity and tone-of-voice generator. Use when the user wants to define brand colors, fonts, visual identity, writing voice, tone guidelines, or brand system. Triggers on: brand, brand identity, voice, tone of voice, colors, fonts, visual identity, brand guide, brand system, writing style, brand persona, brand values.'
user-invocable: false
---

# Brand Voice

Complete brand identity creation system. Generates visual identity (colors, fonts, spacing), tone-of-voice guidelines, platform-specific writing rules, and structured brand files. Built for founders who need a cohesive brand without hiring an agency.

## Keywords

Brand, brand identity, voice, tone of voice, colors, fonts, visual identity, brand guide, brand system, writing style, brand persona, brand values, brand archetype, color palette, typography, design system, brand guidelines, logo usage, brand consistency, messaging framework, brand personality, brand positioning, brand voice generator, brand kit

## Brand Creation Wizard

Run this wizard step by step. Ask one section at a time. Do not dump all questions at once — founders need space to think through each decision. After each section, confirm the answers before moving forward.

### Step 1: Company Basics

Gather foundational context. These answers shape everything downstream.

Ask the user:
1. **Company name** — What is the name of your startup?
2. **One-line description** — In one sentence, what does your company do?
3. **Industry / vertical** — What space do you operate in? (SaaS, fintech, healthtech, edtech, e-commerce, marketplace, dev tools, AI/ML, consumer app, other)
4. **Target audience** — Who is your primary customer? Be specific: role, company size, demographics, psychographics
5. **Core values** — List 3-5 values that define your company's DNA (e.g., transparency, speed, craftsmanship, boldness, empathy)
6. **Competitive positioning** — How are you different from competitors? What is your unique angle?
7. **Stage** — Where are you? (idea, pre-seed, seed, Series A, growth)

Store answers internally — they feed into every subsequent step.

### Step 2: Brand Personality — Archetype Selection

Brand archetypes are psychological blueprints that define how your brand shows up in the world. They shape voice, visual identity, and emotional connection with your audience.

Present the 12 archetypes and ask the user to pick 1 primary and 1 secondary:

| Archetype | Core Drive | Voice Traits | Example Brands |
|-----------|-----------|--------------|----------------|
| **Innovator** | Progress, vision | Forward-thinking, confident, inspiring | Tesla, Apple |
| **Sage** | Knowledge, truth | Authoritative, thoughtful, educational | Google, Harvard |
| **Hero** | Mastery, achievement | Bold, empowering, action-oriented | Nike, FedEx |
| **Creator** | Originality, expression | Imaginative, expressive, detail-obsessed | Adobe, Lego |
| **Explorer** | Freedom, discovery | Adventurous, independent, daring | Patagonia, Jeep |
| **Ruler** | Control, stability | Commanding, premium, assured | Mercedes, Rolex |
| **Caregiver** | Service, protection | Warm, nurturing, trustworthy | Johnson & Johnson, TOMS |
| **Rebel** | Revolution, disruption | Provocative, fearless, unapologetic | Harley-Davidson, Virgin |
| **Magician** | Transformation | Visionary, charismatic, mystical | Disney, Dyson |
| **Lover** | Connection, beauty | Sensual, elegant, passionate | Chanel, Godiva |
| **Jester** | Joy, fun | Witty, playful, irreverent | Old Spice, Dollar Shave Club |
| **Everyman** | Belonging, relatability | Genuine, down-to-earth, honest | IKEA, Target |

After selection, confirm: "Your brand archetype is **[Primary]** with **[Secondary]** influence. This means your brand will feel [description]. Does that resonate?"

### Step 3: Visual Identity

#### Color Palette (10 colors)

Guide the user through building a complete palette. Ask for preferences or suggest based on archetype.

| Slot | Role | Usage |
|------|------|-------|
| **Primary** | Main brand color | Logo, primary CTAs, key UI elements |
| **Primary Dark** | Darker shade of primary | Hover states, active states, headers |
| **Secondary** | Complementary brand color | Secondary buttons, highlights, badges |
| **Secondary Dark** | Darker shade of secondary | Secondary hover states |
| **Accent** | Pop color for emphasis | Notifications, alerts, feature highlights |
| **Accent Alt** | Alternative accent | Tags, labels, progress indicators |
| **Neutral 900** | Darkest neutral | Body text, headings |
| **Neutral 500** | Mid neutral | Secondary text, borders |
| **Neutral 200** | Light neutral | Backgrounds, dividers |
| **Neutral 50** | Lightest neutral | Page backgrounds, cards |

**Color psychology guidance to share with user:**
- Blue: Trust, stability, professionalism (fintech, enterprise, healthcare)
- Green: Growth, health, sustainability (healthtech, fintech, eco)
- Purple: Premium, creative, innovative (AI, luxury, creative tools)
- Red/Orange: Energy, urgency, passion (consumer, food, fitness)
- Black/Dark: Luxury, power, sophistication (premium products)
- Teal/Cyan: Modern, fresh, tech-forward (SaaS, dev tools)

Ensure the palette passes WCAG AA contrast requirements. Primary text color on background must have at least 4.5:1 contrast ratio.

#### Typography (3 fonts)

| Slot | Usage | Style Guidance |
|------|-------|---------------|
| **Heading font** | H1-H6, display text, hero sections | Personality carrier — can be more expressive |
| **Body font** | Paragraphs, UI text, forms | Readability first — clean, high x-height |
| **Accent font** | Code blocks, data, special callouts | Monospace or distinctive serif for contrast |

Suggest from proven web-safe and Google Fonts options:

**Sans-serif options:** Inter, Plus Jakarta Sans, DM Sans, Outfit, Space Grotesk, Satoshi, General Sans, Switzer, Cabinet Grotesk, Geist
**Serif options:** Fraunces, Playfair Display, Lora, Source Serif Pro, Newsreader, Literata
**Monospace options:** JetBrains Mono, Fira Code, IBM Plex Mono, Source Code Pro, Geist Mono

#### Mode Defaults

Ask: Does your product/website lean **light mode**, **dark mode**, or **both** (with toggle)?

Set default mode and note which palette colors to adjust for each mode. Dark mode requires different neutral values and potentially adjusted primary/accent saturation.

### Step 4: Voice Character

Define the brand voice on 4 spectrums. Ask the user to rate each from 1-10.

```
Formal ←——————————→ Casual
  1  2  3  4  5  6  7  8  9  10

Technical ←——————————→ Simple
  1  2  3  4  5  6  7  8  9  10

Serious ←——————————→ Playful
  1  2  3  4  5  6  7  8  9  10

Reserved ←——————————→ Bold
  1  2  3  4  5  6  7  8  9  10
```

**Interpretation guide:**

| Spectrum | 1-3 | 4-6 | 7-10 |
|----------|-----|-----|------|
| Formal/Casual | Corporate, polished, third-person | Professional but approachable | First-person, conversational, contractions |
| Technical/Simple | Assumes expertise, uses jargon | Explains complex ideas clearly | Avoids jargon, uses analogies, 8th-grade reading level |
| Serious/Playful | No humor, straight facts | Occasional wit, light touch | Humor is a core tool, memes welcome |
| Reserved/Bold | Understated, measured claims | Confident but not aggressive | Makes big claims, uses superlatives, provocative |

After ratings, generate a **Voice Summary Statement**: "Our brand voice is [adjective], [adjective], and [adjective]. We sound like [metaphor — e.g., 'a smart friend who happens to be an expert' or 'a confident mentor who respects your time']."

### Step 5: Vocabulary Patterns

Define the linguistic rules that keep the brand voice consistent across all writers and channels.

#### Words We Use (Brand Vocabulary)
Ask the user to provide or collaboratively build a list of 10-20 preferred words/phrases that capture the brand. Examples:
- Instead of "users" → "makers" or "builders" or "teams"
- Instead of "product" → "platform" or "toolkit" or "workspace"
- Instead of "buy" → "get started" or "unlock" or "upgrade"
- Action words that match the brand energy

#### Words We Avoid (Anti-Vocabulary)
Words that damage the brand voice. Build a list of 10-15 words:
- Overused buzzwords (synergy, disrupt, revolutionize, leverage, utilize)
- Words that feel wrong for the brand personality
- Competitors' language or taglines
- Overpromising words (guarantee, never fails, always works)

#### Industry Jargon Policy
Ask: How does your brand handle technical/industry jargon?
- **Use freely** — Our audience is technical and expects it
- **Use with context** — Use jargon but always explain it on first use
- **Avoid entirely** — Write for a general audience, no jargon
- **Define a glossary** — Maintain a specific list of approved technical terms

#### Emoji Usage Policy
Ask: What is your brand's emoji policy?
- **No emojis** — Professional, clean, text-only
- **Minimal emojis** — Occasional single emoji for emphasis (social only)
- **Moderate emojis** — Use in social, email subjects, casual copy
- **Emoji-heavy** — Part of the brand personality, use liberally

### Step 6: Platform Adaptations

The same brand voice adapts to different contexts. Define how.

For each platform, specify:
- **Tone shift** — How does the base voice adjust?
- **Length** — Typical content length
- **Formatting** — Structural conventions
- **Example** — Sample sentence in this platform's voice

| Platform | Tone Shift | Key Rules |
|----------|-----------|-----------|
| **LinkedIn** | +1 formal, +1 serious | Professional but human. Lead with insight, not promotion. Use line breaks for readability. 1200-1500 chars for posts. |
| **Twitter/X** | +2 casual, +1 bold | Punchy, opinionated, concise. Hooks in first line. Thread format for depth. Hot takes welcome. Max impact in 280 chars. |
| **Email** | Baseline voice | Personal, direct, scannable. Subject line is everything. One CTA per email. Mobile-first formatting. |
| **Blog** | +1 technical, baseline else | Educational, thorough, well-structured. SEO-aware headlines. Use code blocks, tables, examples. 1000-2500 words. |
| **Documentation** | +2 technical, +2 formal, -2 playful | Clear, precise, task-oriented. Imperative mood. Code examples. No marketing speak. Progressive disclosure. |
| **Pitch Deck** | +2 bold, +1 formal | Confident, concise, data-backed. One idea per slide. Headlines that make a claim, not a topic. |

---

## Output Generation

After completing all 6 steps, generate the following 4 files in `brand/`:

### File 1: `brand/brand.json`

Structured brand data. Used by other skills to maintain brand consistency.

```json
{
  "brand": {
    "name": "Company Name",
    "tagline": "One-line tagline",
    "description": "One-paragraph brand description",
    "industry": "Industry/vertical",
    "stage": "Current stage",
    "values": ["value1", "value2", "value3"],
    "positioning": "Competitive positioning statement"
  },
  "archetype": {
    "primary": "Archetype Name",
    "secondary": "Archetype Name",
    "summary": "Voice summary statement"
  },
  "colors": {
    "primary": "#hexcode",
    "primaryDark": "#hexcode",
    "secondary": "#hexcode",
    "secondaryDark": "#hexcode",
    "accent": "#hexcode",
    "accentAlt": "#hexcode",
    "neutral900": "#hexcode",
    "neutral500": "#hexcode",
    "neutral200": "#hexcode",
    "neutral50": "#hexcode"
  },
  "typography": {
    "heading": "Font Name",
    "body": "Font Name",
    "accent": "Font Name"
  },
  "mode": "light | dark | both",
  "voice": {
    "formal_casual": 7,
    "technical_simple": 5,
    "serious_playful": 6,
    "reserved_bold": 8
  },
  "vocabulary": {
    "preferred": ["word1", "word2"],
    "avoided": ["word1", "word2"],
    "jargon_policy": "use_freely | use_with_context | avoid | glossary",
    "emoji_policy": "none | minimal | moderate | heavy"
  },
  "platforms": {
    "linkedin": { "tone_shift": "+1 formal", "max_length": 1500 },
    "twitter": { "tone_shift": "+2 casual, +1 bold", "max_length": 280 },
    "email": { "tone_shift": "baseline", "max_length": null },
    "blog": { "tone_shift": "+1 technical", "word_count": "1000-2500" },
    "docs": { "tone_shift": "+2 technical, +2 formal", "max_length": null },
    "pitch": { "tone_shift": "+2 bold, +1 formal", "max_length": null }
  }
}
```

### File 2: `brand/config.json`

Output preferences used by content generation skills.

```json
{
  "output": {
    "default_format": "markdown",
    "file_naming": "kebab-case",
    "date_format": "YYYY-MM-DD",
    "content_directory": "brand/",
    "asset_directory": "brand/assets/"
  },
  "generation": {
    "always_check_brand": true,
    "enforce_vocabulary": true,
    "check_contrast_ratio": true,
    "auto_platform_adapt": true
  },
  "templates": {
    "directory": "brand/templates/",
    "use_brand_colors": true,
    "use_brand_fonts": true
  }
}
```

### File 3: `brand/brand-system.md`

Comprehensive design philosophy and visual rules document. Include:

1. **Design Philosophy** — The "why" behind visual choices, connected to brand values and archetype
2. **Color System** — Full palette with hex codes, usage rules, do/don't examples, dark mode adjustments
3. **Typography System** — Font pairings, size scale (using a modular scale like 1.25 or 1.333), weight usage, line height rules
4. **Spacing System** — Base unit (typically 4px or 8px), spacing scale, consistent padding/margin rules
5. **Component Guidelines** — How brand applies to buttons, cards, inputs, navigation, modals
6. **Imagery & Iconography** — Photo style, illustration style, icon set recommendations
7. **Layout Principles** — Grid system, max content width, responsive breakpoints
8. **Accessibility** — Color contrast requirements, focus states, screen reader considerations

### File 4: `brand/tone-of-voice.md`

Complete writing guide. Include:

1. **Voice Identity** — Summary statement, archetype description, the "feel" of the brand
2. **The 4 Spectrums** — Current settings with explanation of what they mean in practice
3. **Writing Principles** — 5-7 rules every writer follows (e.g., "Clarity beats cleverness", "Lead with the benefit")
4. **Vocabulary Guide** — Preferred words, avoided words, jargon rules, emoji rules with examples
5. **Platform Guides** — For each platform: tone adjustments, length, formatting, 3 example messages (good vs bad)
6. **Content Patterns** — How to write: headlines, CTAs, error messages, success messages, onboarding text, empty states, loading states
7. **Grammar & Style** — Oxford comma stance, capitalization rules, number formatting, date formatting, contraction usage
8. **Do / Don't Examples** — 10 before/after pairs showing the brand voice in action

---

## Brand Update Mode

Before running the wizard, check if `brand/brand.json` exists.

**If it exists:**
1. Read the existing brand.json
2. Present a summary: "I found your existing brand profile: [name], [archetype], [voice summary]. What would you like to update?"
3. Offer section-by-section updates:
   - `update colors` — Modify the color palette
   - `update fonts` — Change typography
   - `update voice` — Adjust voice spectrum settings
   - `update vocabulary` — Add/remove preferred and avoided words
   - `update platforms` — Adjust platform-specific rules
   - `update all` — Full re-run of the wizard
4. After updates, regenerate only the affected output files
5. Show a diff summary of what changed

**If it does not exist:**
Run the full wizard from Step 1.

---

## Brand Consistency Check

When other skills reference the brand system, they should:
1. Read `brand/brand.json` for structured data (colors, fonts, voice settings)
2. Read `brand/tone-of-voice.md` for writing guidance
3. Apply vocabulary rules (preferred/avoided words)
4. Adjust voice for the target platform
5. Use brand colors in any visual output

This ensures every piece of content — from a tweet to a pitch deck — sounds and looks like it came from the same company.

## Reference Files

- `references/voice-guide.md` — Examples of different brand voice styles with before/after comparisons
- `brand/templates/tech-startup.md` — Modern tech startup voice template
- `brand/templates/enterprise-saas.md` — Professional B2B enterprise voice template
- `brand/templates/consumer-app.md` — Consumer-facing app voice template
- `brand/templates/developer-tools.md` — Developer tools voice template
- `brand/templates/creative-agency.md` — Creative/design agency voice template
