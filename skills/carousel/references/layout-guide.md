# Carousel Layout Guide — 21 Templates

Quick reference for every slide layout in the cookbook. Each entry describes what the layout looks like, when to use it, and what parameters it accepts.

---

## Title Layouts (4)

### 1. `title_centered`
**Visual:** Centered title and subtitle stacked vertically on a solid-color background. A thin accent-colored horizontal line separates title from subtitle.

**When to use:** Cover slides, opening slides, section restarts.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Main title text |
| `body` | str | Subtitle text |

---

### 2. `title_bold`
**Visual:** Large bold title left-aligned with a vertical accent bar on the left edge. Subtitle sits below in regular weight.

**When to use:** High-impact openers, bold statements, startup pitch covers.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Main title (3-6 words ideal) |
| `body` | str | Subtitle or tagline |

---

### 3. `title_image`
**Visual:** Full-bleed background image with a semi-transparent dark overlay. Title and subtitle centered over the image.

**When to use:** Visual cover slides, product screenshots, lifestyle imagery.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Overlay title |
| `body` | str | Overlay subtitle |
| `image_path` | str | Path to background image |

---

### 4. `title_gradient`
**Visual:** Two-color diagonal gradient background (primary to secondary color). Title and subtitle centered.

**When to use:** Elegant openers when no image is available but you want more visual interest than a solid color.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Main title |
| `body` | str | Subtitle |

---

## Content Layouts (8)

### 5. `content_single`
**Visual:** One big piece of text centered on the slide. Small label/category at top in accent color. Maximum whitespace.

**When to use:** LinkedIn carousel slides (one idea per slide), key takeaways, bold statements.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Small label at top (optional) |
| `body` | str | The single key point (under 15 words) |

---

### 6. `content_bullets`
**Visual:** Title at top-left with accent underline. Bullet points listed below with dot markers. Clean spacing between items.

**When to use:** Feature lists, agenda slides, key points, any list of 3-8 items.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `body` | str | Bullets separated by `\n` |
| `items` | list[str] | Alternative: list of bullet strings |

---

### 7. `content_two_column`
**Visual:** Full-width title at top. Two text columns below separated by a thin vertical accent divider. Each column can have its own heading.

**When to use:** Comparing two topics, pros/cons (non-competitive), feature categories, two perspectives.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `body` | str | Split on `\|\|\|` for left/right |
| `left_title` | str | Left column heading |
| `right_title` | str | Right column heading |
| `left_body` | str | Left column text |
| `right_body` | str | Right column text |

---

### 8. `content_quote`
**Visual:** Large decorative opening quotation mark in accent color. Quote text in italic below it. Attribution line in accent color with em-dash prefix.

**When to use:** Customer testimonials, founder quotes, industry expert quotes, inspirational statements.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Attribution (or use `attribution` kwarg) |
| `body` | str | The quote text |
| `attribution` | str | Quote source name |

---

### 9. `content_stats`
**Visual (single):** Small label at top, massive number in accent color centered, context text below in regular size.
**Visual (multi):** Multiple stat blocks side by side, each with a big number and label.

**When to use:** Traction slides, KPI highlights, market size, impressive metrics.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Label above stat |
| `body` | str | Context below stat |
| `stat` | str | The big number (e.g., "10M+") |
| `stats` | list[dict] | Multiple stats: `[{value, label}]` |

---

### 10. `content_comparison`
**Visual:** Two side-by-side panels on dark card backgrounds. "VS" circle in accent color between them. Each panel has a heading and bullet list.

**When to use:** Before/after, us vs. them, old way vs. new way, competitor comparison.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `left_title` | str | Left panel heading |
| `right_title` | str | Right panel heading |
| `left_items` | list[str] | Left bullet points |
| `right_items` | list[str] | Right bullet points |

---

### 11. `content_timeline`
**Visual:** Horizontal line across the slide with circular milestone markers. Date labels above each marker, description labels below.

**When to use:** Product roadmap, company history, project phases, growth milestones.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `milestones` | list[dict] | `[{date, label}]` — 3-6 items ideal |
| `body` | str | Fallback: `date: label` per line |

---

### 12. `content_checklist`
**Visual:** Title at top. Vertical list of items, each with a green checkmark or white square icon on the left and text on the right.

**When to use:** Feature availability, progress tracking, requirements met, action items.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `body` | str | Items separated by `\n` |
| `items` | list[str] | Checklist item strings |
| `checked` | list[bool] | Which items are checked |

---

## Image Layouts (4)

### 13. `image_full`
**Visual:** Full-bleed image covering the entire slide. Semi-transparent dark strip at the bottom holds title and body text.

**When to use:** Hero images, product screenshots, photography-driven slides.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Overlay title (on bottom strip) |
| `body` | str | Overlay body text |
| `image_path` | str | Path to image file |

---

### 14. `image_left`
**Visual:** Left 45% is image (or placeholder), right 55% has title, accent bar, and body text.

**When to use:** Product feature + explanation, team member + bio, concept + description.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Right-side heading |
| `body` | str | Right-side body text |
| `image_path` | str | Path to left image |

---

### 15. `image_right`
**Visual:** Mirror of `image_left`. Left 55% text, right 45% image. Alternating with `image_left` creates visual rhythm.

**When to use:** Same as `image_left` but alternated for variety.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Left-side heading |
| `body` | str | Left-side body text |
| `image_path` | str | Path to right image |

---

### 16. `image_grid`
**Visual:** Title at top. 2x2 grid of images below with optional captions under each cell. Bordered placeholder boxes if no images provided.

**When to use:** Product gallery, team photos, feature screenshots, comparison images.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `images` | list[str] | List of 4 image paths |
| `captions` | list[str] | List of 4 caption strings |

---

## Data Layouts (3)

### 17. `data_bar_chart`
**Visual:** Title at top. Column chart below using python-pptx native charting. Accent-colored bars with category labels on x-axis.

**When to use:** Revenue growth, quarterly metrics, comparative data, survey results.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Chart title |
| `categories` | list[str] | X-axis labels |
| `values` | list[float] | Single series data |
| `series_data` | dict | Multi-series: `{name: [values]}` |

---

### 18. `data_pie_chart`
**Visual:** Title at top. Pie chart centered below with percentage data labels and a legend on the right.

**When to use:** Market share, budget allocation, user segments, category breakdown.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Chart title |
| `body` | str | Optional footnote text |
| `categories` | list[str] | Slice labels |
| `values` | list[float] | Slice values |

---

### 19. `data_table`
**Visual:** Title at top. Table with accent-colored header row and alternating row shading (secondary / bg colors). Centered text in all cells.

**When to use:** Pricing comparison, feature matrix, data summaries, financial tables.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Slide heading |
| `headers` | list[str] | Column header labels |
| `rows` | list[list[str]] | Table data rows |
| `col_widths` | list[float] | Column widths in inches |

---

## Special Layouts (2)

### 20. `cta_slide`
**Visual:** Centered headline, supporting text, and a rounded-rectangle "button" shape in accent color with CTA text. Optional social handle below.

**When to use:** Final slide of any carousel/deck, landing page link, demo booking, newsletter signup.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | CTA headline |
| `body` | str | Supporting text |
| `button_text` | str | Button label (default: "Learn More") |
| `url` | str | CTA URL (saved to slide notes) |
| `handle` | str | Social handle or contact info |

---

### 21. `divider_slide`
**Visual:** Full accent-color background (visual break from dark slides). Large section title centered. Optional section number in top-left corner.

**When to use:** Between major sections of a long deck, chapter breaks, topic transitions.

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `title` | str | Section title |
| `body` | str | Optional subtitle |
| `section_number` | str | Section number (e.g., "01") |

---

## Layout Selection Matrix

| Carousel Type | Recommended Layouts |
|--------------|-------------------|
| **LinkedIn Carousel** | title_centered/title_bold, content_single (x5-8), cta_slide |
| **Pitch Deck** | title_gradient, content_bullets, content_stats, content_timeline, data_bar_chart, content_comparison, cta_slide |
| **Educational Deck** | title_image, content_bullets, content_checklist, content_two_column, divider_slide, image_left/right |
| **Product Demo** | title_bold, image_full, image_left, image_right, content_comparison, content_checklist, cta_slide |
| **Case Study** | title_centered, content_quote, content_stats, data_bar_chart, data_table, content_timeline, cta_slide |
| **Internal Report** | title_centered, content_bullets, data_bar_chart, data_pie_chart, data_table, content_stats |

## Color & Font Defaults

When no brand system is configured, all layouts use:

```python
colors = {
    'primary': '1a1a2e',    # Dark navy
    'secondary': '16213e',   # Darker navy
    'accent': 'e94560',      # Coral red
    'text': 'ffffff',        # White
    'bg': '1a1a2e',          # Dark navy background
}

fonts = {
    'heading': 'Arial Black',
    'body': 'Arial',
}
```

These can be overridden by the brand system via `brand/brand.json`.
