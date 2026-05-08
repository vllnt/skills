# Accessibility Audit — Deep Checklist

Loaded on-demand by `SKILL.md`. Covers **WCAG 2.2 Level AA**, **ADA Title III** (US), **European Accessibility Act / EAA** (mandatory June 28, 2025), **EN 301 549** (EU procurement), **Section 508** (US federal).

---

## Applicability Quick Test

| Service | Likely required |
|---------|-----------------|
| Public-facing US website (place of public accommodation) | ADA Title III (DOJ position: WCAG 2.1 AA) |
| US federal procurement / federal-funded | Section 508 → WCAG 2.0 AA refresh |
| EU B2C e-commerce, banking, transport, e-books, ICT (after 2025-06-28) | EAA → EN 301 549 → WCAG 2.1 AA minimum |
| EU public sector | Web Accessibility Directive → EN 301 549 |
| Anything serious in 2026+ | Use **WCAG 2.2 AA** as the working bar |

---

## WCAG 2.2 AA — Full Checklist (BLOCKING when applicable)

### 1. Perceivable

| ID | SC | Check |
|----|----|----|
| 1.1.1 | A | Non-text content has text alternative (alt, aria-label, role + name) |
| 1.2.1–1.2.5 | A/AA | Captions, audio description, transcripts for media |
| 1.3.1 | A | Info & relationships conveyed in markup (semantics, not just visuals) |
| 1.3.2 | A | Meaningful sequence preserved when CSS removed |
| 1.3.3 | A | Instructions don't rely on shape/color/size alone |
| 1.3.4 | AA | Orientation not locked to portrait/landscape unless essential |
| 1.3.5 | AA | Input purpose programmatically identified (autocomplete attrs) |
| 1.4.1 | A | Color is not the sole means of conveying info |
| 1.4.3 | AA | Contrast 4.5:1 normal text, 3:1 large (≥18.66px bold or ≥24px) |
| 1.4.4 | AA | Text resizable to 200% without loss of content/function |
| 1.4.5 | AA | Images of text avoided unless essential |
| 1.4.10 | AA | Reflow at 320 CSS px / 256 CSS px (vertical scroll OK) |
| 1.4.11 | AA | Non-text contrast ≥3:1 for UI components and graphical objects |
| 1.4.12 | AA | Text spacing adjustable (line-height 1.5×, paragraph 2×, letter 0.12em, word 0.16em) without loss |
| 1.4.13 | AA | Hover/focus content dismissible, hoverable, persistent |

### 2. Operable

| ID | SC | Check |
|----|----|----|
| 2.1.1 | A | All functionality keyboard-accessible |
| 2.1.2 | A | No keyboard trap |
| 2.1.4 | A | Single-character key shortcuts disablable / remappable |
| 2.2.1 | A | Timing adjustable / extendable / disablable |
| 2.2.2 | A | Pause/stop/hide for moving/blinking/auto-updating content |
| 2.3.1 | A | No content flashing >3× per second over flash threshold |
| 2.4.3 | A | Focus order is meaningful |
| 2.4.4 | A | Link purpose clear from link text (or surrounding context) |
| 2.4.5 | AA | Multiple ways to find pages (nav, search, sitemap) |
| 2.4.6 | AA | Headings & labels descriptive |
| 2.4.7 | AA | Focus visible |
| **2.4.11** | **AA** (new in 2.2) | Focus not obscured (minimum) — at least partly visible |
| **2.4.12** | AAA | (Focus not obscured — enhanced; AAA, advisory) |
| 2.5.1 | A | Pointer gestures: multipoint/path-based have single-pointer alternative |
| 2.5.2 | A | Pointer cancellation: down-event ≠ commit |
| 2.5.3 | A | Label in name: visible label text is part of accessible name |
| 2.5.4 | A | Motion actuation has UI alternative |
| **2.5.7** | **AA** (new in 2.2) | Dragging movements have single-pointer alternative |
| **2.5.8** | **AA** (new in 2.2) | Target size minimum 24×24 CSS px (with exceptions) |

### 3. Understandable

| ID | SC | Check |
|----|----|----|
| 3.1.1 | A | Page language declared (`<html lang>`) |
| 3.1.2 | AA | Language of parts marked when different |
| 3.2.1 | A | On-focus does not change context |
| 3.2.2 | A | On-input does not change context unexpectedly |
| 3.2.3 | AA | Consistent navigation across pages |
| 3.2.4 | AA | Consistent identification of components |
| **3.2.6** | **A** (new in 2.2) | Consistent help (contact info, chat, etc. in same relative location) |
| 3.3.1 | A | Error identification |
| 3.3.2 | A | Labels or instructions for inputs |
| 3.3.3 | AA | Error suggestion provided when known |
| 3.3.4 | AA | Error prevention for legal/financial/data submissions (review/correct/cancel) |
| **3.3.7** | **A** (new in 2.2) | Redundant entry: previously entered info auto-populated or selectable |
| **3.3.8** | **AA** (new in 2.2) | Accessible authentication (no cognitive function test like image-puzzle without alternative) |

### 4. Robust

| ID | SC | Check |
|----|----|----|
| 4.1.1 | (obsolete in 2.2) | (no longer required) |
| 4.1.2 | A | Name, role, value programmatically determinable for UI components |
| 4.1.3 | AA | Status messages exposed to AT (aria-live, role=status/alert) |

---

## Beyond WCAG (jurisdictional)

### EAA-specific (EN 301 549 §5–13 + chapters)
- Hardware + software accessibility requirements
- Synchronized media for telecom + audiovisual services
- Real-time text (RTT) for voice/video communications
- Compatibility with assistive technologies (AT)

### ADA Title III
- DOJ has stated WCAG 2.1 AA is the de-facto bar (April 2024 final rule for state/local; private guidance varies)
- Mobile apps included
- Reasonable modifications for accessibility-blocking flows

### Section 508 (US federal)
- Procurement: Voluntary Product Accessibility Template (VPAT) / Accessibility Conformance Report (ACR)
- Aligns with EN 301 549 since 2018 refresh

---

## Accessibility Statement (REQUIRED when EAA or WAD applies)

Must include:

- [ ] Conformance status (full / partial / non-conformant) and target standard (WCAG 2.2 AA / EN 301 549)
- [ ] Known limitations + workarounds
- [ ] Date of statement + last review
- [ ] Feedback mechanism (email + form) for users to report inaccessibility
- [ ] Enforcement procedure / national contact body (EU: per member state)
- [ ] Compatibility statement (browsers, AT versions tested)

---

## Procurement / B2B

- [ ] VPAT 2.4 (or later) / ACR available on request
- [ ] EN 301 549-aligned for EU procurement
- [ ] Roadmap for known non-conformances

---

## Verification Tooling

| Layer | Tool |
|-------|------|
| Static analysis | axe-core (DevTools), Lighthouse, WAVE, Pa11y |
| Manual | Keyboard-only test, screen reader (NVDA / VoiceOver), 200% zoom, reflow at 320px, OS high-contrast |
| Color | WCAG color-contrast calculator, APCA (advisory) |

**Automated tools catch ~30–40% of issues.** Manual review of keyboard, focus, reading order, ARIA correctness is required.

---

## Quick "go-live" gate (any FAIL = BLOCKER)

1. All interactive elements keyboard-reachable, focus visible, no traps.
2. Color contrast 4.5:1 on body text, 3:1 on large text + UI components.
3. All form inputs labeled.
4. `<html lang>` set; landmarks (`<nav>`, `<main>`, `<header>`, `<footer>`) present.
5. Images have alt or are explicitly decorative (alt="").
6. Accessibility statement published (when EAA / WAD applies).
7. Target size ≥24×24 CSS px (WCAG 2.2 new).
