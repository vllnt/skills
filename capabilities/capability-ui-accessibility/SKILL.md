---
name: capability-ui-accessibility
description: Build, review, and repair accessible web interfaces with applicable standards and explicit browser, keyboard, and assistive-technology evidence.
---

# Capability UI Accessibility

Use this skill to author, review, or repair requested web UI. Discover the consumer repository's supported platforms, accessibility requirements, and installed tools. Review is read-only; use isolated authorized data for state-changing journeys. Missing tooling narrows evidence, never creates a pass.

## Procedure

1. Define the changed route or component, relevant states, primary task, target revision, and applicable requirements. Use installed browser and axe tooling, or an equivalent, when available; otherwise perform bounded source/manual review and report the missing evidence. Do not install tools automatically.
2. Build with native semantics first: use correct elements and landmarks; add ARIA only for behavior HTML cannot express. Every control needs a name, keyboard operation, visible focus, logical DOM/tab order, and valid state.
3. Check changed forms, images, dynamic content, dialogs, and navigation. Labels and errors must be associated; meaningful images need text alternatives; decorative images use empty `alt`; focusable content must never be hidden from assistive technology.
4. For custom widgets, implement the complete role, name, state, focus, and keyboard contract. Modal dialogs move focus in, contain it while open, and restore it on close. Do not use positive `tabindex` or remove focus visibility without an equivalent.
5. For an accessibility claim, verify changed routes and states in a real browser: axe has zero unresolved applicable violations; the keyboard-only primary task succeeds with visible, unobscured focus and no unintended trap; manual checks cover applicable contrast, zoom/reflow, errors/status, text alternatives, and complex-widget screen-reader behavior when in scope and available.
6. Run Lighthouse only when requested or required. Treat it as a diagnostic, never WCAG proof. Compare the current UI with the DoD; repair authorized gaps and repeat affected browser, keyboard, and manual checks. In review mode, return findings only. When material risk or uncertainty remains, use independent review and critique perspectives when available, otherwise sequential perspectives. These perspectives assess this procedure; the caller owns overall convergence. Missing browser, assistive-technology, or authority evidence is incomplete with its next check.

## Definition of Done

- The changed UI, relevant states, primary task, target revision, and applicable requirements are identified.
- Every claimed accessible flow has applicable browser axe, keyboard, and manual evidence; untested assistive technology or browser coverage is explicit.
- Authorized repairs preserve semantic, focus, label, contrast, and custom-widget contracts across affected states.
- A score or source-only result is never reported as accessibility conformance.
