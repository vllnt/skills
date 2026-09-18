# Build Landing Page

Drafts a page from scratch for one conversion goal and reviews a landing page with prioritized, evidence-backed fixes.

Output is a framework-independent specification and copy. Optional design and browser tools may help when available; their absence limits only the evidence they would provide.

## Two modes

| Mode | You say | You get |
|---|---|---|
| **Write** | "write a landing page for…", "draft the hero", "value prop for…" | Section-by-section spec + recommended copy (headlines, subheads, CTAs, body) + per-section rationale |
| **Review** | "review / audit / score my landing page <url>" | Evidence-backed prioritized fixes; scorecard only where the supplied evidence supports it |

## Entry points

- `SKILL.md` — task routing and completion criteria
- `references/structure-blueprints.md` — section library, archetypes, above-the-fold, awareness→structure
- `references/copywriting-formulas.md` — headline/CTA formulas, PAS/AIDA/BAB/FAB/StoryBrand, value-prop, objections
- `references/review-rubric.md` — 15-dimension scoring + portable URL audit + report format

## Smoke test

> "Write a landing page for a tool that auto-generates invoices for freelancers. Goal: free-trial signups."

Expect: a brief check (goal/audience locked), then a spec + copy doc starting with a hero that passes the 5-second test.

> "Review https://example.com — why isn't it converting?"

Expect: evidence-backed findings and top fixes; without a browser, static findings with explicit unverified dimensions.

## Install

Copy this entire folder into your agent runtime’s skill directory; keep `references/` beside `SKILL.md`.

## Requires / optional

- **Review mode:** any available browser for live behavior; source/HTTP/copy review remains useful with explicit evidence limits.
- **Optional bridges:** use consumer-approved design, research, or browser tools when they add useful evidence.
