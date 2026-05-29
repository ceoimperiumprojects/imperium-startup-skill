# Imperium Brain — Measurable Metrics

Centralized quality metrics for all 18 skills. Organized into 4 tiers — from fully automated structural checks to manual quality assessment.

**Version:** 2.2.0
**Last updated:** 2026-03-16
**Skills covered:** 18/18

---

## Tier 1: Structural Integrity (Automated, Pass/Fail)

These checks run automatically via `evals/eval-runner.py`. Every check must PASS for a release.

| # | Check | What It Validates | Pass Criteria |
|---|-------|-------------------|---------------|
| S1 | Skill files exist | All 18 `skills/*/SKILL.md` files | All 18 present, non-empty |
| S2 | Frontmatter valid | YAML frontmatter in each SKILL.md | `name`, `description` fields present |
| S3 | References exist | All files in `skills/*/references/` | Non-zero file size |
| S4 | Cross-references resolve | File path patterns in SKILL.md body | Referenced paths exist on disk |
| S5 | plugin.json sync | `skills` array matches `skills/` dirs | 1:1 mapping, no orphans |
| S6 | Command frontmatter | Each `commands/*.md` file | `name: imperium:*`, `user-invocable: true` |
| S7 | Hooks command count | `hooks.json` prompt string | Correct slash command count |
| S8 | Eval coverage | Eval scenarios per domain | >= 2 evals per skill domain |
| S9 | Brand integration | 7 content skills reference brand | Mention `brand.json` or brand system |
| S10 | Marketplace sync | `marketplace.json` counts & version | Matches reality (skills, commands, version) |
| S11 | Agent files exist | `plugin.json` agents array | All agent .md files present |
| S12 | Cookbook completeness | `skills/carousel/cookbook/` | 21 layout files + `__init__.py` |
| S13 | Eval references | `expected_references` in evals.json | All referenced files exist in skill dirs |
| S14 | Eval skills in routing | `expected_skills` in evals.json | Each maps to routing table entry |
| S15 | Eval assertion quality | Assertions per eval | >= 2 assertions per scenario |
| S16 | Routing completeness | Routing table coverage | Every skill dir appears in at least one row |
| S17 | Counts consistency | Cross-file counts | SKILL.md, README, hooks, plugin.json agree |

---

## Tier 2: Routing Accuracy (Automated, Per-Eval)

Each eval scenario in `evals/evals.json` defines routing expectations.

| Check | What It Validates | Pass Criteria |
|-------|-------------------|---------------|
| R1 | Expected skills mapping | `expected_skills` array | Maps to valid skill directory |
| R2 | Expected references exist | `expected_references` array | Files exist in matched skill's `references/` |
| R3 | Assertion count | `assertions` array per eval | >= 2 assertions per scenario |
| R4 | Routing table coverage | All skill dirs in routing | Every `skills/*` dir appears in >= 1 eval |

---

## Tier 3: Output Quality (Per-Skill Metrics)

Extracted from individual SKILL.md files. These define what "good output" looks like for each skill.

### LinkedIn
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Hook length | 140-210 characters | Character count of first line |
| Post length | 700-1800 characters | Total character count |
| No links in body | 0 links before CTA | URL regex scan |
| Hashtag count | Max 5 | Count `#` tokens |
| Closing question | Present at END | Last sentence ends with `?` |
| Readability | 8th grade level | Flesch-Kincaid score |
| Quality Score | /80 | 8 dimensions x /10 each |
| Line breaks | Every 1-2 sentences | Blank line ratio |

### Carousel
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Words per slide (LinkedIn) | 20-30 | Word count per slide |
| Words per slide (other) | 40-60 | Word count per slide |
| Ideas per slide | 1 | Manual review |
| Whitespace | ~40% | Layout density check |
| CTA slide | Last slide | Position check |
| Font minimum | 24pt body / 36pt title | Style check |
| Correct dimensions | 1080x1080 or 1920x1080 | PPTX metadata |

### Brand Voice
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Voice spectrums | 4 spectrums (1-10 each) | Count spectrum definitions |
| Contrast | WCAG AA compliant | Contrast ratio check |
| Color palette | 10 colors | Count in brand.json |
| Font stack | 3 fonts (heading/body/accent) | Count in brand.json |
| Vocabulary lists | Present | Non-empty vocabulary array |
| Platform adaptations | 6 platforms | Count platform entries |

### SOP
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Action verbs | Every step starts with verb | First word POS check |
| Banned phrases | 0 matches | Scan for "please", "try to", "maybe" |
| Role assignment | Every step has owner | Role field present |
| Time estimates | Per step or section | Time notation present |
| Escalation path | Defined | Section exists |
| Prerequisites | Listed | Section exists |

### Slides
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Font sizing | CSS clamp() used | Regex for clamp() |
| Keyboard nav | Arrow key support | JS event listeners present |
| Dependencies | Zero external | No CDN links |
| Responsive | Media queries | CSS @media present |
| Print styles | @media print | CSS print rules present |

### Video
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Templates | 5 types with timing | Template count |
| Captions | Mandatory | Caption track or text overlay |
| Hook timing | 2-3 seconds | Script timestamp |
| CTA clarity | Clear action | CTA section present |
| Shot list | Complete | Shot list section present |

### Visual Media
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Protocol phases | 5-phase workflow | Phase count in output |
| Relevance score | >= 4/5 | Score in review output |
| Quality score | 1-5 scale | Score in review output |
| Brand fit | Matches brand.json | Color/style alignment |
| Content trap rejection | Bad images rejected | Rejection reason logged |

### CEO Advisor
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Dashboard metrics | 8 metrics | Count in output |
| Stage-adaptive frameworks | Present | Framework selection logic |
| DECIDE framework | Applied for decisions | Framework steps present |

### Product Manager
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Quality gates | 5 gates | Gate count in PRD review |
| RICE/ICE scoring | Applied | Score columns present |
| Anti-patterns | Flagged | Anti-pattern warnings |
| AARRR metrics | Referenced | Metric categories present |

### Marketing
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Dashboard metrics | 8 metrics | Count in output |
| Anti-patterns | 7 flagged | Anti-pattern list check |
| CRO framework | Applied | Conversion elements present |
| Traction channels | 19 available | Channel count |

### Sales & GTM
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Triggers referenced | 137 in knowledge | Trigger database size |
| Reply rate benchmarks | Present | Benchmark citations |
| Cold email length | < 100 words | Word count |
| Email sequence | 4-email minimum | Sequence length |

### Finance
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| SaaS metric formulas | 15+ formulas | Formula count |
| Red flag thresholds | Defined | Threshold values present |
| LTV:CAC ratio | > 3:1 benchmark | Ratio calculation |
| Runway calculation | Present | Months calculated |

### Founder
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Fatal questions | 5 questions | Question count |
| Scorecard dimensions | 7 (28-35 = strong) | Dimension count |
| Mom Test compliance | Applied | Non-leading questions |

### Legal
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Entity comparison | Table format | Comparison table present |
| Contract checklist | Complete | Checklist items |
| Compliance checklist | Complete | Checklist items |

### CTO Advisor
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Dashboard metrics | 8 metrics | Count in output |
| Red flags | Identified | Red flag warnings |
| ADR format | Applied | ADR structure present |
| Build-vs-buy framework | Applied | Framework steps |

### Engineering Advanced
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Agent+RAG metrics | Defined | Metric definitions |
| Pipeline effectiveness | Measured | CI/CD metrics |
| Tool definitions | Complete | Tool schema present |

### Research
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Phase coverage | 9 phases | Phase count in output |
| Search strategies | 12 strategies | Strategy count |
| Top-20 scoring | Applied | Score table present |
| Gap analysis | Generated | Gap analysis document |

### API Discovery
| Dimension | Target | How to Measure |
|-----------|--------|----------------|
| Endpoint analysis | 15-point checklist | Check count |
| SPA detection | Automated | Detection logic present |
| Structured output | JSON format | Valid JSON output |

---

## Tier 4: Content Depth (Manual Assessment, 1-10)

For periodic manual review. Rate each dimension 1-10.

| Dimension | Description | How to Assess |
|-----------|-------------|---------------|
| Specificity | Concrete numbers, names, examples vs generic advice | Count specific data points per output |
| Actionability | Can user execute immediately vs needs more research | Count direct action items |
| Brand alignment | Output matches brand.json when brand exists | Side-by-side comparison |
| Framework completeness | All framework steps applied vs partial | Step coverage percentage |
| Edge case coverage | Handles unusual inputs gracefully | Test with edge case prompts |

---

## Priority Order for Polishing

Ordered by user impact and content volume:

| Priority | Skill | Why |
|----------|-------|-----|
| 1 | linkedin | Highest usage, most visible output, quality directly measurable |
| 2 | carousel | Complex output (PPTX), many layout combinations |
| 3 | research | Longest skill (1800+ lines), most phases, highest complexity |
| 4 | sop | Enterprise use case, strictest format requirements |
| 5 | brand-voice | Foundation for all content, cascading quality impact |
| 6 | sales-gtm | Largest reference set (137 triggers), measurable outcomes |
| 7 | founder | 10-book knowledge base, validation frameworks |
| 8 | ceo-advisor | Strategic decisions, high-stakes output |
| 9 | product-manager | PRD quality gates, prioritization accuracy |
| 10 | marketing | 19 traction channels, broad surface area |
| 11 | cto-advisor | Architecture decisions, tech debt assessment |
| 12 | finance | Formula accuracy critical, red flag thresholds |
| 13 | slides | HTML output quality, CSS correctness |
| 14 | video | Remotion bridge complexity, template timing |
| 15 | visual-media | Image review accuracy, brand fit |
| 16 | engineering-advanced | Agent/RAG architecture patterns |
| 17 | legal | Compliance accuracy, entity comparison |
| 18 | api-discovery | Endpoint detection, SPA handling |

---

## Running Metrics

```bash
# Run all automated checks (Tier 1 + Tier 2)
python3 evals/eval-runner.py

# Results saved to evals/results/YYYY-MM-DD-HHMMSS.md

# Hourly automated loop
/imperium:eval-loop
```
