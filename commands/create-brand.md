---
name: imperium:create-brand
description: Run the brand identity wizard. Creates brand colors, fonts, visual system, and tone-of-voice guide.
user-invocable: true
---

# Brand Identity Wizard

You are running the Imperium Brand Identity creation system. This wizard creates a complete brand foundation — visual identity, tone-of-voice, and structured brand files.

## Pre-Flight Check

Before starting the wizard, check if a brand already exists:

```bash
test -f brand/brand.json && echo "EXISTS" || echo "NEW"
```

### If brand.json EXISTS → Update Mode

1. Read the existing `brand/brand.json`
2. Present a summary to the user:
   - Brand name and archetype
   - Current color palette (show hex codes)
   - Current voice settings (the 4 spectrums)
   - Current vocabulary highlights
3. Ask: "Your brand profile already exists. What would you like to update?"
   - **Colors** — Update the color palette
   - **Fonts** — Change typography selections
   - **Voice** — Adjust voice spectrum settings
   - **Vocabulary** — Add/remove preferred and avoided words
   - **Platforms** — Adjust platform-specific tone rules
   - **Everything** — Full re-run of the wizard
4. Run only the relevant wizard steps from the brand-voice skill
5. Regenerate only the affected output files
6. Show a before/after diff summary

### If brand.json does NOT exist → Full Wizard

Run the complete Brand Creation Wizard from the `brand-voice` skill.

## Wizard Execution

Reference: `skills/brand-voice/SKILL.md` for the full wizard process.

Walk through all 6 steps, one at a time:
1. **Company Basics** — Name, industry, audience, values, positioning, stage
2. **Brand Personality** — Select primary and secondary archetypes
3. **Visual Identity** — Build 10-color palette, select 3 fonts, set mode preference
4. **Voice Character** — Rate the 4 spectrums (formal/casual, technical/simple, serious/playful, reserved/bold)
5. **Vocabulary Patterns** — Define preferred words, avoided words, jargon policy, emoji policy
6. **Platform Adaptations** — Set tone adjustments for LinkedIn, Twitter, email, blog, docs, pitch decks

Important: Ask one section at a time. Confirm answers before moving to the next step. Do not overwhelm the user with all questions at once.

## Output Generation

After completing the wizard, generate 4 files:

### 1. `brand/brand.json`
Structured brand data with all wizard answers. Follow the schema defined in the brand-voice skill. This file is the single source of truth used by all other skills.

### 2. `brand/config.json`
Output preferences and generation settings. Controls how other skills interact with the brand system.

### 3. `brand/brand-system.md`
Design philosophy and visual rules document covering: color usage rules, typography scale, spacing system, component guidelines, accessibility requirements.

### 4. `brand/tone-of-voice.md`
Complete writing guide covering: voice identity, the 4 spectrums, writing principles, vocabulary guide, platform-specific guides with examples, content patterns, grammar rules, do/don't examples.

Reference the voice templates at `brand/templates/` for style inspiration when generating these files.

## Preview Summary

After generating all files, show the user a preview:

```
Brand Profile: [Company Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Archetype:   [Primary] + [Secondary]
Voice:       [Summary statement]

Colors:
  ● Primary:     [hex] ████
  ● Secondary:   [hex] ████
  ● Accent:      [hex] ████

Typography:
  Heading:  [Font Name]
  Body:     [Font Name]
  Accent:   [Font Name]

Voice Spectrum:
  Formal ←——→ Casual:     [N]/10
  Technical ←——→ Simple:   [N]/10
  Serious ←——→ Playful:    [N]/10
  Reserved ←——→ Bold:      [N]/10

Files generated:
  ✓ brand/brand.json
  ✓ brand/config.json
  ✓ brand/brand-system.md
  ✓ brand/tone-of-voice.md
```

Tell the user: "Your brand system is ready. All content generation skills will now use these settings automatically. Run `/imperium:create-brand` again to update any section."
