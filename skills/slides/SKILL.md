---
name: slides
description: 'HTML presentation slide creator with 12 style presets. Generates self-contained HTML files that work as presentations in any browser. Zero dependencies — no npm, no framework, just open the file. Supports speaker notes, keyboard navigation, and print-to-PDF. Triggers on: HTML slides, web presentation, browser slides, HTML presentation, reveal.js alternative, simple slides, quick presentation, keynote alternative.'
user-invocable: false
---

# HTML Presentation Slides

Create self-contained HTML presentations that run in any browser with zero dependencies. One file, no build step, no internet required.

## Keywords

HTML slides, web presentation, browser slides, HTML presentation, reveal.js alternative, simple slides, quick presentation, keynote alternative, slide deck, presentation, slides, powerpoint alternative, google slides alternative, speaker notes, fullscreen presentation

## What This Creates

A single `.html` file that:
- Opens in any browser as a full-screen presentation
- Arrow keys and spacebar navigate between slides
- Escape key shows slide overview grid
- F key toggles fullscreen mode
- P key shows/hides presenter notes
- Ctrl+P prints to PDF (use Chrome for best results)
- Responsive — adapts to any screen size
- No internet required — all styles and scripts are inline
- Works offline, works on any OS, works forever (no dependencies to break)

## Base HTML Template

Every presentation uses this template. Style presets override the CSS variables.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<style>
  /* ===== RESET ===== */
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 100%; height: 100%; overflow: hidden; }

  /* ===== THEME VARIABLES ===== */
  :root {
    --bg: {{BG_COLOR}};
    --text: {{TEXT_COLOR}};
    --accent: {{ACCENT_COLOR}};
    --heading-font: {{HEADING_FONT}};
    --body-font: {{BODY_FONT}};
    --code-font: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', 'Consolas', monospace;
  }

  /* ===== SLIDE CONTAINER ===== */
  .slide {
    width: 100vw;
    height: 100vh;
    display: none;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 5vw;
    font-family: var(--body-font);
    background: var(--bg);
    color: var(--text);
    position: relative;
  }
  .slide.active { display: flex; }

  /* ===== TYPOGRAPHY ===== */
  h1 {
    font-size: clamp(2rem, 4vw, 5rem);
    font-family: var(--heading-font);
    margin-bottom: 2vh;
    line-height: 1.2;
    text-align: center;
  }
  h2 {
    font-size: clamp(1.5rem, 3vw, 3.5rem);
    font-family: var(--heading-font);
    margin-bottom: 2vh;
    line-height: 1.3;
  }
  h3 {
    font-size: clamp(1.2rem, 2.2vw, 2.5rem);
    font-family: var(--heading-font);
    margin-bottom: 1.5vh;
  }
  p {
    font-size: clamp(1rem, 2vw, 2rem);
    line-height: 1.6;
    max-width: 80%;
    text-align: center;
  }
  ul, ol {
    font-size: clamp(0.9rem, 1.8vw, 1.8rem);
    line-height: 2;
    text-align: left;
    max-width: 75%;
  }
  li { margin-bottom: 0.5vh; }
  strong { color: var(--accent); }
  code {
    font-family: var(--code-font);
    background: rgba(0,0,0,0.15);
    padding: 0.2em 0.5em;
    border-radius: 4px;
    font-size: 0.9em;
  }
  pre {
    font-family: var(--code-font);
    background: rgba(0,0,0,0.3);
    padding: 2vw;
    border-radius: 8px;
    font-size: clamp(0.7rem, 1.4vw, 1.2rem);
    line-height: 1.6;
    text-align: left;
    max-width: 85%;
    overflow-x: auto;
    white-space: pre-wrap;
  }
  blockquote {
    font-size: clamp(1.2rem, 2.5vw, 2.5rem);
    font-style: italic;
    border-left: 4px solid var(--accent);
    padding-left: 2vw;
    max-width: 75%;
    line-height: 1.5;
  }
  blockquote cite {
    display: block;
    font-size: 0.6em;
    font-style: normal;
    margin-top: 1vh;
    opacity: 0.7;
  }

  /* ===== LAYOUT HELPERS ===== */
  .slide-title {
    text-align: center;
  }
  .slide-title h1 {
    font-size: clamp(2.5rem, 5vw, 6rem);
    margin-bottom: 3vh;
  }
  .slide-title p {
    font-size: clamp(1rem, 2vw, 2rem);
    opacity: 0.8;
  }
  .two-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4vw;
    width: 85%;
    align-items: start;
    text-align: left;
  }
  .two-columns h2 {
    grid-column: 1 / -1;
    text-align: center;
  }
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 3vw;
    width: 80%;
    text-align: center;
  }
  .stat-number {
    font-size: clamp(2rem, 4vw, 5rem);
    font-weight: 800;
    color: var(--accent);
    font-family: var(--heading-font);
  }
  .stat-label {
    font-size: clamp(0.8rem, 1.4vw, 1.2rem);
    opacity: 0.7;
    margin-top: 0.5vh;
  }
  .image-full {
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
  }
  .image-side {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4vw;
    width: 90%;
    align-items: center;
  }
  .image-side img {
    width: 100%;
    border-radius: 8px;
  }

  /* ===== SPEAKER NOTES ===== */
  .notes { display: none; }
  .show-notes .notes {
    display: block;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0,0,0,0.92);
    color: #e2e8f0;
    padding: 2vh 3vw;
    font-size: clamp(0.8rem, 1.5vw, 1.1rem);
    line-height: 1.6;
    font-family: var(--body-font);
    z-index: 100;
    max-height: 25vh;
    overflow-y: auto;
    border-top: 2px solid var(--accent);
  }

  /* ===== SLIDE COUNTER ===== */
  .counter {
    position: fixed;
    bottom: 1.5vh;
    right: 2vw;
    font-size: clamp(0.7rem, 1.2vw, 1rem);
    opacity: 0.4;
    font-family: var(--body-font);
    z-index: 50;
  }

  /* ===== PROGRESS BAR ===== */
  .progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: var(--accent);
    transition: width 0.3s ease;
    z-index: 50;
  }

  /* ===== OVERVIEW MODE ===== */
  .overview .slide {
    display: flex !important;
    width: 23vw;
    height: 23vh;
    font-size: 0.25em;
    border: 2px solid transparent;
    cursor: pointer;
    border-radius: 8px;
    transition: border-color 0.2s;
  }
  .overview .slide:hover { border-color: var(--accent); }
  .overview .slide.active { border-color: var(--accent); }
  body.overview-mode {
    overflow: auto;
    display: flex;
    flex-wrap: wrap;
    gap: 1vw;
    padding: 2vw;
    background: #111;
  }
  body.overview-mode .progress,
  body.overview-mode .counter { display: none; }

  /* ===== PRINT STYLES ===== */
  @media print {
    .slide {
      display: flex !important;
      page-break-after: always;
      height: 100vh;
    }
    .progress, .counter { display: none; }
    .notes { display: none; }
  }

  /* ===== TRANSITIONS ===== */
  .slide {
    animation: fadeIn 0.3s ease;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>

<div class="progress" id="progress"></div>
<div class="counter" id="counter"></div>

<!-- ===== SLIDES START ===== -->

<!-- Title Slide -->
<div class="slide slide-title">
  <h1>{{PRESENTATION_TITLE}}</h1>
  <p>{{SUBTITLE}}</p>
  <div class="notes">Speaker notes go here. Press P to show/hide.</div>
</div>

<!-- Content Slide Example -->
<div class="slide">
  <h2>{{Slide Title}}</h2>
  <ul>
    <li>Point one</li>
    <li>Point two</li>
    <li>Point three</li>
  </ul>
  <div class="notes">Additional context for the speaker.</div>
</div>

<!-- Quote Slide Example -->
<div class="slide">
  <blockquote>
    "The best way to predict the future is to create it."
    <cite>— Peter Drucker</cite>
  </blockquote>
</div>

<!-- Stats Slide Example -->
<div class="slide">
  <h2>Key Numbers</h2>
  <div class="stats-grid">
    <div>
      <div class="stat-number">10K+</div>
      <div class="stat-label">Active Users</div>
    </div>
    <div>
      <div class="stat-number">99.9%</div>
      <div class="stat-label">Uptime</div>
    </div>
    <div>
      <div class="stat-number">4.8★</div>
      <div class="stat-label">Rating</div>
    </div>
  </div>
</div>

<!-- Two-Column Slide Example -->
<div class="slide">
  <div class="two-columns">
    <h2>Comparison</h2>
    <div>
      <h3>Before</h3>
      <ul>
        <li>Manual process</li>
        <li>Hours of work</li>
        <li>Error-prone</li>
      </ul>
    </div>
    <div>
      <h3>After</h3>
      <ul>
        <li>Automated</li>
        <li>Minutes</li>
        <li>Reliable</li>
      </ul>
    </div>
  </div>
</div>

<!-- Code Slide Example -->
<div class="slide">
  <h2>How It Works</h2>
  <pre><code>// Example code block
const result = await imperium.analyze({
  target: 'competitors',
  depth: 'full'
});
console.log(result.insights);</code></pre>
</div>

<!-- CTA/Closing Slide -->
<div class="slide slide-title">
  <h1>Thank You</h1>
  <p>{{CTA — website, email, or next step}}</p>
</div>

<!-- ===== SLIDES END ===== -->

<script>
(function() {
  const slides = document.querySelectorAll('.slide');
  let current = 0;
  let overviewMode = false;

  function show(n) {
    if (overviewMode) return;
    slides[current].classList.remove('active');
    current = Math.max(0, Math.min(n, slides.length - 1));
    slides[current].classList.add('active');
    updateUI();
  }

  function updateUI() {
    document.getElementById('counter').textContent = (current + 1) + ' / ' + slides.length;
    document.getElementById('progress').style.width = ((current + 1) / slides.length * 100) + '%';
  }

  function toggleOverview() {
    overviewMode = !overviewMode;
    document.body.classList.toggle('overview-mode', overviewMode);
    if (!overviewMode) {
      show(current);
    }
  }

  // Keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (overviewMode && e.key === 'Escape') {
      toggleOverview();
      return;
    }
    if (overviewMode) return;

    switch(e.key) {
      case 'ArrowRight':
      case ' ':
      case 'ArrowDown':
        e.preventDefault();
        show(current + 1);
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
        e.preventDefault();
        show(current - 1);
        break;
      case 'Home':
        e.preventDefault();
        show(0);
        break;
      case 'End':
        e.preventDefault();
        show(slides.length - 1);
        break;
      case 'f':
        if (document.fullscreenElement) {
          document.exitFullscreen();
        } else {
          document.documentElement.requestFullscreen().catch(function(){});
        }
        break;
      case 'p':
        document.body.classList.toggle('show-notes');
        break;
      case 'Escape':
        toggleOverview();
        break;
    }
  });

  // Click navigation in overview mode
  slides.forEach(function(slide, index) {
    slide.addEventListener('click', function() {
      if (overviewMode) {
        current = index;
        toggleOverview();
      }
    });
  });

  // Touch support for mobile
  let touchStartX = 0;
  let touchStartY = 0;
  document.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  });
  document.addEventListener('touchend', function(e) {
    const dx = e.changedTouches[0].screenX - touchStartX;
    const dy = e.changedTouches[0].screenY - touchStartY;
    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 50) {
      if (dx < 0) show(current + 1);
      else show(current - 1);
    }
  });

  // Hash-based navigation (allows linking to specific slides)
  function checkHash() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#slide-')) {
      const n = parseInt(hash.replace('#slide-', '')) - 1;
      if (!isNaN(n) && n >= 0 && n < slides.length) {
        show(n);
      }
    }
  }
  window.addEventListener('hashchange', checkHash);

  // Initialize
  checkHash();
  show(current);
})();
</script>
</body>
</html>
```

## Style Presets

12 visual themes available. Each preset overrides the CSS `:root` variables.

### 1. Midnight
Dark navy background with white text and electric blue accents. Professional, modern, great for tech presentations.
```css
:root {
  --bg: #0f172a;
  --text: #f1f5f9;
  --accent: #3b82f6;
  --heading-font: 'Segoe UI', system-ui, sans-serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```

### 2. Clean
White background with dark text. Minimal, distraction-free. Works for any context.
```css
:root {
  --bg: #ffffff;
  --text: #1e293b;
  --accent: #2563eb;
  --heading-font: 'Segoe UI', system-ui, sans-serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```

### 3. Startup
Dark background with gradient accent elements. Modern startup aesthetic.
```css
:root {
  --bg: #0a0a0a;
  --text: #fafafa;
  --accent: #a855f7;
  --heading-font: 'Segoe UI', system-ui, sans-serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```
Additional: accent gradient from `#a855f7` to `#ec4899` on headings.

### 4. Corporate
Light gray background, navy text. Professional and boardroom-ready.
```css
:root {
  --bg: #f8fafc;
  --text: #1e3a5f;
  --accent: #1e40af;
  --heading-font: 'Georgia', 'Times New Roman', serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```

### 5. Creative
Bold colors, oversized typography. For pitches that need to stand out.
```css
:root {
  --bg: #fef3c7;
  --text: #1c1917;
  --accent: #dc2626;
  --heading-font: 'Georgia', 'Times New Roman', serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```

### 6. Developer
Terminal aesthetic. Dark background, monospace font, green accents.
```css
:root {
  --bg: #0d1117;
  --text: #c9d1d9;
  --accent: #58a6ff;
  --heading-font: 'Fira Code', 'Cascadia Code', 'Consolas', monospace;
  --body-font: 'Fira Code', 'Cascadia Code', 'Consolas', monospace;
}
```
Additional: green (#3fb950) for code highlights, subtle grid background.

### 7. Warm
Cream background with warm brown text. Friendly, approachable, human.
```css
:root {
  --bg: #fdf6e3;
  --text: #3c2415;
  --accent: #c2410c;
  --heading-font: 'Georgia', 'Times New Roman', serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```

### 8. Neon
Black background with neon gradient text. High-energy, attention-grabbing.
```css
:root {
  --bg: #000000;
  --text: #ffffff;
  --accent: #00ff88;
  --heading-font: 'Segoe UI', system-ui, sans-serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```
Additional: headings use gradient `linear-gradient(135deg, #00ff88, #00d4ff)` with `-webkit-background-clip: text`.

### 9. Nature
Forest green palette. Organic, grounded, eco-friendly feel.
```css
:root {
  --bg: #1a2e1a;
  --text: #e8f5e9;
  --accent: #66bb6a;
  --heading-font: 'Georgia', 'Times New Roman', serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```

### 10. Minimal
Pure black and white. Maximum whitespace, maximum clarity.
```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --accent: #000000;
  --heading-font: 'Segoe UI', system-ui, sans-serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```
Additional: headings use letter-spacing: 0.05em, lighter font-weight.

### 11. Retro
Vintage color palette with serif fonts. Nostalgic, distinctive.
```css
:root {
  --bg: #2d1b14;
  --text: #f5e6d3;
  --accent: #e07a3a;
  --heading-font: 'Georgia', 'Palatino Linotype', serif;
  --body-font: 'Georgia', 'Palatino Linotype', serif;
}
```

### 12. Gradient
Smooth gradient backgrounds that shift per slide. Dynamic, modern.
```css
:root {
  --bg: linear-gradient(135deg, #667eea, #764ba2);
  --text: #ffffff;
  --accent: #fbbf24;
  --heading-font: 'Segoe UI', system-ui, sans-serif;
  --body-font: 'Segoe UI', system-ui, sans-serif;
}
```
Additional: each slide uses a different gradient from a curated palette:
- Slide 1: `#667eea → #764ba2`
- Slide 2: `#f093fb → #f5576c`
- Slide 3: `#4facfe → #00f2fe`
- Slide 4: `#43e97b → #38f9d7`
- Slide 5: `#fa709a → #fee140`
- Slide 6+: cycle through the palette

## Brand Integration

Before generating slides, check if `brand/brand.json` exists.

**If brand files exist:**
- Override any preset with brand colors:
  - `brand.colors.primary` → `--accent`
  - `brand.colors.background` → `--bg` (or use a preset and just override accent)
  - `brand.colors.text` → `--text`
- Use brand fonts:
  - `brand.fonts.heading` → `--heading-font`
  - `brand.fonts.body` → `--body-font`
- Add brand logo to title slide if `brand/assets/logo.svg` or `brand/assets/logo.png` exists
- Apply tone-of-voice to slide content

**If no brand files exist:**
- Use the selected preset as-is
- Default to "Midnight" preset if no preference given

## Slide Types

When generating presentations, use these slide patterns:

### Title Slide
Centered layout. Large heading, subtitle, optional logo. Used for opening and section breaks.
```html
<div class="slide slide-title">
  <h1>Presentation Title</h1>
  <p>Subtitle or tagline</p>
</div>
```

### Content Slide
Title with bullet points. The workhorse slide for most content.
```html
<div class="slide">
  <h2>Section Title</h2>
  <ul>
    <li><strong>Key point</strong> — supporting detail</li>
    <li><strong>Key point</strong> — supporting detail</li>
    <li><strong>Key point</strong> — supporting detail</li>
  </ul>
</div>
```

### Quote Slide
Large quote with attribution. Use for customer testimonials, founding principles, or impactful statements.
```html
<div class="slide">
  <blockquote>
    "The quote goes here."
    <cite>— Attribution</cite>
  </blockquote>
</div>
```

### Code Slide
Syntax-displayed code block. For technical presentations, API demos, architecture explanations.
```html
<div class="slide">
  <h2>Implementation</h2>
  <pre><code>const example = 'code here';</code></pre>
</div>
```

### Stats/Numbers Slide
Grid of key metrics. For traction, impact, or comparison data.
```html
<div class="slide">
  <h2>By The Numbers</h2>
  <div class="stats-grid">
    <div>
      <div class="stat-number">{{NUMBER}}</div>
      <div class="stat-label">{{LABEL}}</div>
    </div>
  </div>
</div>
```

### Two-Column Slide
Side-by-side content. For comparisons, before/after, pros/cons.
```html
<div class="slide">
  <div class="two-columns">
    <h2>Title</h2>
    <div><!-- Left column --></div>
    <div><!-- Right column --></div>
  </div>
</div>
```

### Image Slide
Full-bleed image or side-by-side image with text.
```html
<!-- Full bleed -->
<div class="slide" style="padding: 0;">
  <img class="image-full" src="{{IMAGE_URL}}" alt="{{ALT}}">
</div>

<!-- Side by side -->
<div class="slide">
  <div class="image-side">
    <img src="{{IMAGE_URL}}" alt="{{ALT}}">
    <div>
      <h2>Title</h2>
      <p>Description alongside the image.</p>
    </div>
  </div>
</div>
```

### CTA/Closing Slide
Final slide with clear call to action.
```html
<div class="slide slide-title">
  <h1>Get Started</h1>
  <p>website.com | hello@company.com</p>
</div>
```

## Best Practices

### Content Rules
- Maximum 6 bullet points per slide — less is more
- One idea per slide — if it needs two ideas, make two slides
- Use `<strong>` for key terms — they render in the accent color
- Keep headlines under 8 words
- Speaker notes can be verbose — slides should not be

### Design Rules
- Default padding (5vw) keeps content away from edges — don't override unless full-bleed
- Use `clamp()` for font sizes — already built into the template for responsiveness
- Stats grid auto-fits: 2 stats = 2 columns, 3 = 3 columns, 4 = 2x2 grid
- Code blocks have overflow-x auto — long lines won't break the layout

### Presentation Tips
- F for fullscreen before presenting
- Test with Ctrl+P to verify PDF output looks correct
- Speaker notes (P key) only show on presenter's screen in browser
- Share the .html file directly — recipients just double-click to view
- Works in Chrome, Firefox, Safari, Edge — no compatibility issues
