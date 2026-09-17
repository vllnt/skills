---
name: capability-ui-accessibility
description: Build, review, and repair accessible web interfaces with applicable standards and explicit browser, keyboard, and assistive-technology evidence.
---

## Contract

- Input: A changed UI route or component, relevant states, primary task, target revision, applicable requirements, and authorized mode.
- Output: Evidence-backed accessibility findings or authorized repairs, with untested coverage and remaining work.
- Effects: Review is read-only. Authoring or repair may change authorized UI; state-changing journeys use isolated authorized data.

### Acceptance

- The changed UI, relevant states, primary task, target revision, and applicable requirements are identified.
- Each claimed accessible flow has applicable browser, axe, keyboard, and manual evidence.
- Authorized repairs preserve semantic, focus, label, contrast, and custom-widget contracts across affected states.
- Untested assistive technology or browser coverage is explicit, and scores or source-only results are never conformance claims.

## Procedure

1. Discover supported platforms, accessibility requirements, and installed tools. Use browser and axe tooling, or an equivalent, when available; otherwise conduct bounded source or manual review and report missing evidence. Do not install tools automatically.
2. In review, inspect the following contracts without changing UI. For authorized authoring or repair, build with native semantics first. Give every control a name, keyboard operation, visible focus, logical DOM or tab order, and valid state; use ARIA only for behavior HTML cannot express.
3. Check forms, images, dynamic content, dialogs, and navigation. Associate labels and errors, provide text alternatives for meaningful images, use empty `alt` for decorative images, and keep focusable content available to assistive technology.
4. For custom widgets, inspect or, in authorized authoring/repair, implement the complete role, name, state, focus, and keyboard contract. Modal dialogs move focus in, contain it while open, and restore it on close.
5. Verify changed routes and states in a real browser: report applicable axe violations and repair them only in authorized authoring/repair mode, complete the keyboard-only primary task with visible unobscured focus and no unintended trap, and manually check applicable contrast, zoom or reflow, errors or status, text alternatives, and complex-widget screen-reader behavior when in scope and available.
6. Run Lighthouse only when requested or required. In review mode, return findings only. Repair authorized gaps, rerun affected evidence, and send material uncertainty and proof to the caller's Quality Validation pool. Return the next check for missing browser, assistive-technology, or authority evidence.

## Pitfalls

- A Lighthouse score is diagnostic, never WCAG proof.
- Do not use positive `tabindex` or hide focus visibility without an equivalent accessible interaction.
