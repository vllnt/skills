# Review Rubric + URL Audit

How to audit any landing page and return prioritized, concrete fixes. Primary input is a **live URL** using any available browser; use pasted copy, supplied screenshots, HTTP content or local source for a bounded partial review when needed.

---

## URL Audit Workflow

Use an installed browser tool for rendered/interactive evidence; the optional CLI examples below require matching installed help. If no browser works, continue static content/structure analysis and explicitly mark live layout, console, interaction and speed unknown. Do not demand one tool or invent an audit. Capture supported viewports, not a universal fixed device set.

```bash
# 1. Load + structure/copy extraction
agent-browser open <url>
agent-browser snapshot -i                 # accessibility tree = section order, headings, CTAs, forms

# 2. Visual hierarchy at the 3 breakpoints that matter
agent-browser set viewport 1920 1080 && agent-browser screenshot lp-desktop.png
agent-browser set viewport 768 1024  && agent-browser screenshot lp-tablet.png
agent-browser set viewport 375 667   && agent-browser screenshot lp-mobile.png

# 3. Is the page even healthy? (broken page = lost conversions)
agent-browser console --level error
agent-browser network --failed
```

Read-only. **Never submit forms or trigger a purchase during an audit.**

### What to extract before scoring
- Hero: headline, subhead, primary CTA label, what's above the fold (from desktop + mobile shots)
- Section order (from snapshot) vs the canonical conversion order
- Every CTA: label, count, whether they share one goal (attention ratio)
- Proof present: logos, testimonials (named?), numbers, guarantees
- Friction: form field count, steps, required account, nav links that leak attention
- Health: console errors, failed requests, mobile layout breakage

---

## The 15-Dimension Rubric

Score each observed dimension **0–5** (0 observed absent, 3 adequate, 5 strong). Unknown is N/A, not zero. Multiply by weight; normalize a complete rubric to 100. This is an editorial assessment, not measured conversion lift or release approval.

| # | Dimension | What "5" looks like | Weight |
|---|---|---|---|
| 1 | **Clarity (5-sec test)** | Stranger gets what/who/next-action in 5s | ×3 |
| 2 | **Single goal / attention ratio** | One conversion action; ratio ≈ 1:1, nav stripped | ×2 |
| 3 | **Value proposition** | Unique, specific, outcome-led; differentiated | ×2 |
| 4 | **Above-the-fold completeness** | Headline+subhead+CTA+trust+visual, no scroll | ×2 |
| 5 | **Visual hierarchy → CTA** | Eye funnels to a high-contrast CTA | ×1 |
| 6 | **Benefit-led copy** | Features paired with "so what?" benefits | ×2 |
| 7 | **Social proof** | Named testimonials, logos, real numbers, well-placed | ×2 |
| 8 | **Objection handling / FAQ** | Real objections answered | ×1 |
| 9 | **Risk reversal** | Guarantee / free trial / no-card / easy cancel | ×1 |
| 10 | **CTA quality** | First-person, action+value, repeated, low-friction | ×2 |
| 11 | **Specificity / proof** | Numbers and concrete claims, not vague adjectives | ×1 |
| 12 | **Readability / scannability** | Short, you-focused, subhead-only read works | ×1 |
| 13 | **Trust signals** | Security, credibility, social, no broken elements | ×1 |
| 14 | **Friction** | Minimal form fields/steps; fast time-to-value | ×2 |
| 15 | **Mobile + speed/health** | Clean mobile layout, no console errors, fast | ×2 |

**Score = Σ(dimension × weight)**, max = 5 × (sum of weights = 25) = **125 → normalize to /100** (`score×100/125`). Round to nearest whole.

For partial evidence, show the observed weighted subtotal and covered maximum, list N/A dimensions, and do not present a complete /100 verdict. For complete reviews, higher scores indicate stronger rubric alignment, not proven conversion performance. Validate lift with authorized analytics or experiments; do not claim causation from copy review.

---

## Report Format

```markdown
## Landing Page Audit: <url>
**Score: <n>/100** — <one-line verdict>
Captured: desktop / tablet / mobile screenshots, console (<n> errors)

### Top 5 fixes (do these first — ranked by impact × ease)
1. [impact HIGH / effort LOW] <problem>
   → Why: <conversion reasoning>
   → Fix: "<concrete rewrite or change>"
2. ...

### Scorecard
| # | Dimension | Score /5 | Note |
|---|-----------|----------|------|
| 1 | Clarity (5-sec) | 2 | Headline is a tagline, not an outcome — "<quote>" |
| ... | | | |

### Quick wins (low effort)
- <…>

### Bigger bets (higher effort, higher upside)
- <…>

### Health flags
- <console errors / mobile breakage / slow assets, if any>
```

---

## Prioritization (impact × effort)

Rank every finding so the user knows what to do **first**:

```
            LOW effort        HIGH effort
HIGH    ┌──────────────┬──────────────┐
impact  │  DO FIRST    │  PLAN / BET  │
        ├──────────────┼──────────────┤
LOW     │  quick win   │  SKIP/LATER  │
impact  └──────────────┴──────────────┘
```

Highest-leverage fixes almost always live in **dimensions weighted ×3/×2**: the hero's 5-second clarity, the single-goal/attention ratio, the value prop, CTA quality, friction, and mobile health. Start there.

---

## Review Tone

- Lead with **evidence scope + score (when complete) + verdict**, then the **5 fixes**, then the scorecard. Busy founders read top-down.
- Every finding is **specific + actionable**: quote the offending copy, give the rewrite. "Weak headline" is useless; `"Welcome to Acme" → "Invoice clients in 60 seconds"` is a fix.
- Be a collaborative adversary: name what's losing conversions plainly, but always pair the critique with the concrete move.
