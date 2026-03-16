# Slide Style Presets — Complete Reference

All 12 style presets with full CSS, font stacks, color codes, and visual descriptions.

---

## 1. Midnight

**Vibe:** Professional tech presentation. Sleek, modern, trustworthy.

**When to use:** Investor pitches, product launches, conference talks, SaaS demos.

```css
:root {
  --bg: #0f172a;
  --text: #f1f5f9;
  --accent: #3b82f6;
  --heading-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
/* Additional styles */
.slide { background: #0f172a; }
h1, h2, h3 { font-weight: 700; }
strong { color: #3b82f6; }
pre { background: #1e293b; border: 1px solid #334155; }
code { background: #1e293b; color: #93c5fd; }
blockquote { border-left-color: #3b82f6; }
.stat-number { color: #3b82f6; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #0f172a | Slide background |
| Text | #f1f5f9 | Body text, bullets |
| Accent | #3b82f6 | Highlights, stats, strong text |
| Surface | #1e293b | Code blocks, cards |
| Border | #334155 | Subtle dividers |
| Muted | #94a3b8 | Secondary text |

---

## 2. Clean

**Vibe:** Minimal and clear. The content is the star.

**When to use:** Academic presentations, internal team meetings, documentation, any context where simplicity is key.

```css
:root {
  --bg: #ffffff;
  --text: #1e293b;
  --accent: #2563eb;
  --heading-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #ffffff; }
h1, h2, h3 { font-weight: 600; color: #0f172a; }
strong { color: #2563eb; }
pre { background: #f8fafc; border: 1px solid #e2e8f0; color: #1e293b; }
code { background: #f1f5f9; color: #1e40af; }
blockquote { border-left-color: #2563eb; color: #475569; }
.counter { color: #94a3b8; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #ffffff | Slide background |
| Text | #1e293b | Body text |
| Heading | #0f172a | Titles (slightly darker) |
| Accent | #2563eb | Links, highlights |
| Surface | #f8fafc | Code blocks |
| Border | #e2e8f0 | Dividers |

---

## 3. Startup

**Vibe:** Dark, bold, modern. Purple-pink gradients. Y Combinator demo day energy.

**When to use:** Startup pitches, product launches, demo days, landing page screenshots.

```css
:root {
  --bg: #0a0a0a;
  --text: #fafafa;
  --accent: #a855f7;
  --heading-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #0a0a0a; }
h1, h2 {
  background: linear-gradient(135deg, #a855f7, #ec4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 800;
}
h3 { color: #a855f7; }
strong { color: #c084fc; }
pre { background: #18181b; border: 1px solid #27272a; }
code { background: #18181b; color: #c084fc; }
blockquote { border-left-color: #a855f7; }
.stat-number {
  background: linear-gradient(135deg, #a855f7, #ec4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #0a0a0a | Slide background |
| Text | #fafafa | Body text |
| Primary | #a855f7 | Gradient start |
| Secondary | #ec4899 | Gradient end |
| Surface | #18181b | Code blocks, cards |
| Border | #27272a | Subtle dividers |

---

## 4. Corporate

**Vibe:** Boardroom-ready. Professional, serious, trustworthy.

**When to use:** Board meetings, enterprise sales, executive briefings, quarterly reviews.

```css
:root {
  --bg: #f8fafc;
  --text: #1e3a5f;
  --accent: #1e40af;
  --heading-font: 'Georgia', 'Palatino Linotype', 'Times New Roman', serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #f8fafc; }
h1, h2, h3 { color: #1e3a5f; font-weight: 600; }
strong { color: #1e40af; }
pre { background: #ffffff; border: 1px solid #cbd5e1; color: #334155; }
code { background: #e2e8f0; color: #1e3a5f; }
blockquote { border-left-color: #1e40af; font-family: 'Georgia', serif; }
.stat-number { color: #1e40af; }
.progress { background: #1e40af; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #f8fafc | Slide background |
| Text | #1e3a5f | Body text (navy) |
| Accent | #1e40af | Highlights, data |
| Surface | #ffffff | Cards, code blocks |
| Border | #cbd5e1 | Dividers |

---

## 5. Creative

**Vibe:** Bold and unapologetic. Large type, warm background, red accents.

**When to use:** Creative agency pitches, brand presentations, marketing decks, design reviews.

```css
:root {
  --bg: #fef3c7;
  --text: #1c1917;
  --accent: #dc2626;
  --heading-font: 'Georgia', 'Palatino Linotype', 'Times New Roman', serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #fef3c7; }
h1 { font-size: clamp(3rem, 6vw, 8rem); font-weight: 900; letter-spacing: -0.02em; }
h2 { font-weight: 800; }
strong { color: #dc2626; }
pre { background: #1c1917; color: #fef3c7; border-radius: 12px; }
code { background: #fde68a; color: #92400e; }
blockquote { border-left-color: #dc2626; font-weight: 500; }
.stat-number { color: #dc2626; font-size: clamp(3rem, 6vw, 8rem); }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #fef3c7 | Warm amber background |
| Text | #1c1917 | Near-black text |
| Accent | #dc2626 | Red highlights |
| Surface-dark | #1c1917 | Code blocks |
| Surface-light | #fde68a | Inline code |

---

## 6. Developer

**Vibe:** Terminal/IDE aesthetic. For developers, by developers.

**When to use:** Technical talks, API demos, engineering team presentations, dev tool pitches.

```css
:root {
  --bg: #0d1117;
  --text: #c9d1d9;
  --accent: #58a6ff;
  --heading-font: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', 'Consolas', monospace;
  --body-font: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', 'Consolas', monospace;
}
.slide {
  background: #0d1117;
  background-image: radial-gradient(#161b22 1px, transparent 1px);
  background-size: 20px 20px;
}
h1, h2, h3 { color: #58a6ff; font-weight: 600; }
h1::before { content: '# '; color: #484f58; }
strong { color: #3fb950; }
pre {
  background: #161b22;
  border: 1px solid #30363d;
  border-left: 3px solid #58a6ff;
}
code { background: #161b22; color: #79c0ff; }
blockquote { border-left-color: #3fb950; color: #8b949e; }
.stat-number { color: #3fb950; }
ul li::marker { color: #58a6ff; }
.counter { font-family: monospace; }
/* Green for success, blue for info, yellow for warning */
.text-green { color: #3fb950; }
.text-yellow { color: #d29922; }
.text-red { color: #f85149; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #0d1117 | GitHub dark bg |
| Text | #c9d1d9 | Standard text |
| Blue | #58a6ff | Headings, links |
| Green | #3fb950 | Success, highlights |
| Yellow | #d29922 | Warnings |
| Red | #f85149 | Errors |
| Surface | #161b22 | Code blocks |
| Border | #30363d | Dividers |
| Dot grid | #161b22 | Subtle background pattern |

---

## 7. Warm

**Vibe:** Inviting and human. Like a well-designed coffee shop menu.

**When to use:** Community updates, non-profit pitches, customer-facing presentations, workshops.

```css
:root {
  --bg: #fdf6e3;
  --text: #3c2415;
  --accent: #c2410c;
  --heading-font: 'Georgia', 'Palatino Linotype', 'Times New Roman', serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #fdf6e3; }
h1, h2, h3 { color: #3c2415; }
strong { color: #c2410c; }
pre { background: #3c2415; color: #fdf6e3; border-radius: 8px; }
code { background: #fef0c7; color: #92400e; }
blockquote { border-left-color: #c2410c; color: #78350f; }
.stat-number { color: #c2410c; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #fdf6e3 | Cream/parchment |
| Text | #3c2415 | Warm brown |
| Accent | #c2410c | Burnt orange |
| Dark | #78350f | Deep brown |
| Code bg | #3c2415 | Dark for contrast |
| Highlight | #fef0c7 | Light amber |

---

## 8. Neon

**Vibe:** High-energy, attention-grabbing. Cyberpunk meets startup.

**When to use:** Launch events, hackathon presentations, gaming/entertainment industry, social media screenshots.

```css
:root {
  --bg: #000000;
  --text: #ffffff;
  --accent: #00ff88;
  --heading-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #000000; }
h1, h2 {
  background: linear-gradient(135deg, #00ff88, #00d4ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 800;
}
h3 { color: #00ff88; }
strong { color: #00ff88; }
pre {
  background: #0a0a0a;
  border: 1px solid #00ff8833;
  box-shadow: 0 0 20px #00ff8811;
}
code { background: #0a0a0a; color: #00ff88; }
blockquote { border-left-color: #00d4ff; }
.stat-number {
  background: linear-gradient(135deg, #00ff88, #00d4ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none;
}
.progress { background: linear-gradient(90deg, #00ff88, #00d4ff); }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #000000 | Pure black |
| Text | #ffffff | Pure white |
| Neon Green | #00ff88 | Primary neon |
| Neon Blue | #00d4ff | Secondary neon |
| Glow | #00ff8811 | Box shadows |
| Surface | #0a0a0a | Code blocks |

---

## 9. Nature

**Vibe:** Earthy, organic, grounded. Like a walk through a forest.

**When to use:** Sustainability pitches, health/wellness, environmental topics, outdoor brands.

```css
:root {
  --bg: #1a2e1a;
  --text: #e8f5e9;
  --accent: #66bb6a;
  --heading-font: 'Georgia', 'Palatino Linotype', 'Times New Roman', serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #1a2e1a; }
h1, h2, h3 { color: #a5d6a7; font-weight: 600; }
strong { color: #66bb6a; }
pre { background: #0d1f0d; border: 1px solid #2e7d32; }
code { background: #0d1f0d; color: #81c784; }
blockquote { border-left-color: #66bb6a; color: #c8e6c9; }
.stat-number { color: #66bb6a; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #1a2e1a | Dark forest |
| Text | #e8f5e9 | Light green-white |
| Heading | #a5d6a7 | Medium green |
| Accent | #66bb6a | Bright green |
| Surface | #0d1f0d | Deeper forest |
| Border | #2e7d32 | Green border |

---

## 10. Minimal

**Vibe:** Maximum restraint. Black text on white. Nothing extra.

**When to use:** When the content must speak entirely for itself. Design reviews, academic, editorial.

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --accent: #000000;
  --heading-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
.slide { background: #ffffff; }
h1, h2, h3 {
  font-weight: 300;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
h1 { font-size: clamp(2rem, 3.5vw, 4rem); }
strong { font-weight: 700; text-decoration: underline; text-decoration-thickness: 2px; }
pre { background: #fafafa; border: 1px solid #e5e5e5; color: #171717; }
code { background: #f5f5f5; color: #171717; }
blockquote { border-left-color: #000000; border-left-width: 2px; }
.stat-number { font-weight: 200; font-size: clamp(3rem, 6vw, 8rem); }
.progress { background: #000000; height: 1px; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #ffffff | White |
| Text | #000000 | Black |
| Surface | #fafafa | Subtle gray |
| Border | #e5e5e5 | Hairline dividers |

---

## 11. Retro

**Vibe:** Vintage warmth. Serif fonts, muted earth tones. Analog in a digital world.

**When to use:** Storytelling, brand origin stories, history presentations, editorial content.

```css
:root {
  --bg: #2d1b14;
  --text: #f5e6d3;
  --accent: #e07a3a;
  --heading-font: 'Georgia', 'Palatino Linotype', 'Times New Roman', serif;
  --body-font: 'Georgia', 'Palatino Linotype', 'Times New Roman', serif;
}
.slide { background: #2d1b14; }
h1, h2, h3 { color: #f5e6d3; font-weight: 400; font-style: italic; }
h1 { font-size: clamp(2.5rem, 5vw, 6rem); }
strong { color: #e07a3a; font-style: normal; }
pre { background: #1a0f09; border: 1px solid #5c3a25; color: #d4a574; }
code { background: #3d2416; color: #e07a3a; }
blockquote {
  border-left-color: #e07a3a;
  font-style: italic;
  color: #d4a574;
}
.stat-number { color: #e07a3a; font-family: 'Georgia', serif; font-weight: 400; }
.progress { background: #e07a3a; }
```

**Color Palette:**
| Role | Hex | Usage |
|------|-----|-------|
| Background | #2d1b14 | Dark mahogany |
| Text | #f5e6d3 | Parchment |
| Accent | #e07a3a | Burnt orange |
| Secondary | #d4a574 | Warm tan |
| Surface | #1a0f09 | Deep dark |
| Border | #5c3a25 | Brown border |

---

## 12. Gradient

**Vibe:** Dynamic, modern, eye-catching. Each slide feels like a new experience.

**When to use:** Creative pitches, portfolio presentations, event introductions, social media content.

```css
:root {
  --bg: linear-gradient(135deg, #667eea, #764ba2);
  --text: #ffffff;
  --accent: #fbbf24;
  --heading-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
  --body-font: 'Segoe UI', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
}
h1, h2, h3 { color: #ffffff; font-weight: 800; text-shadow: 0 2px 10px rgba(0,0,0,0.2); }
strong { color: #fbbf24; }
pre { background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); }
code { background: rgba(0,0,0,0.2); color: #fbbf24; }
blockquote { border-left-color: #fbbf24; text-shadow: 0 1px 5px rgba(0,0,0,0.2); }
.stat-number { color: #fbbf24; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }

/* Per-slide gradient rotation */
.slide:nth-child(6n+1) { background: linear-gradient(135deg, #667eea, #764ba2); }
.slide:nth-child(6n+2) { background: linear-gradient(135deg, #f093fb, #f5576c); }
.slide:nth-child(6n+3) { background: linear-gradient(135deg, #4facfe, #00f2fe); }
.slide:nth-child(6n+4) { background: linear-gradient(135deg, #43e97b, #38f9d7); }
.slide:nth-child(6n+5) { background: linear-gradient(135deg, #fa709a, #fee140); }
.slide:nth-child(6n+6) { background: linear-gradient(135deg, #a18cd1, #fbc2eb); }
```

**Gradient Palette:**
| Slide | Start | End | Mood |
|-------|-------|-----|------|
| 1 | #667eea | #764ba2 | Purple dream |
| 2 | #f093fb | #f5576c | Pink energy |
| 3 | #4facfe | #00f2fe | Ocean blue |
| 4 | #43e97b | #38f9d7 | Fresh green |
| 5 | #fa709a | #fee140 | Sunset warm |
| 6 | #a18cd1 | #fbc2eb | Soft lavender |

---

## Preset Selection Guide

| Audience | Recommended Presets |
|----------|-------------------|
| Investors | Midnight, Startup, Corporate |
| Developers | Developer, Midnight, Minimal |
| Executives | Corporate, Clean, Minimal |
| Creative teams | Creative, Neon, Gradient |
| General audience | Clean, Warm, Nature |
| Social media screenshots | Neon, Startup, Gradient |
| Academic / Research | Clean, Minimal, Corporate |
| Storytelling | Retro, Warm, Nature |

## Font Stack Details

All presets use web-safe font stacks that work without any external font loading:

| Stack | Fonts | Platform Coverage |
|-------|-------|-------------------|
| Sans-serif | Segoe UI → Helvetica Neue → system-ui → -apple-system → sans-serif | Windows, macOS, Linux |
| Serif | Georgia → Palatino Linotype → Times New Roman → serif | Windows, macOS, Linux |
| Monospace | Fira Code → Cascadia Code → JetBrains Mono → Consolas → monospace | Dev machines, fallback everywhere |

No external font loading means:
- Zero network requests
- Instant rendering
- Works offline
- No FOUT (flash of unstyled text)

If brand fonts are specified and are not web-safe, add `@font-face` with base64-encoded font data inline for true self-containment, or accept the system fallback.
