---
name: improve-ui
description: Improve an interface’s hierarchy, consistency, responsiveness, and accessibility while preserving journeys, or assess it read-only for evidence-backed findings.
---

## Goal

Improve one interface while preserving its supported journeys, or in assess mode return evidence-backed findings on its usability, responsiveness, consistency, and accessibility without changing it.

### Definition of Done

- Platform, screens, audience, task, journeys, candidate, environment, constraints, design system, and evidence types are explicit.
- Change mode: authorized changes preserve supported interaction and applicable accessibility; observed layouts, access behavior, and limits are reported.
- Assess mode: the main journey and platform-relevant states are assessed or excluded. Findings separate observations, preferences, and hypotheses, each with priority, location, state or viewport, impact, correction, and acceptance check; unobserved interaction and accessibility gaps are explicit.
- Validation accepts the selected mode (assess: the declared coverage); an unmet required criterion remains REVISE or BLOCKED.

## Boundaries

- A screenshot is not proof of keyboard, assistive, responsive, or runtime behavior; obtain the evidence or report the gap. A missing observation is incomplete, not a pass; N/A needs a reason.
- Assess mode does not repair the interface, install anything, create hosted issues, or change external state.

## Workflow

1. Resolve platform, screens, audience, task, journeys, constraints, candidate and environment, rules, evidence type, and acceptance criteria. In assess mode also bound the scope and the permitted read-only evidence.
2. Trace the main journey and applicable layout, content, feedback, loading, empty, error, validation, disabled, focus, and success states; identify shared-component impact.
3. In change mode, apply the smallest authorized correction at the owning boundary, preserving content, navigation, supported states, and accessible interaction. Reuse the project's design system; for a new React web component with none, default to `@vllnt/ui` per [default packages](references/vstack/capabilities/project-alignment/references/default-packages.md).
4. Exercise the target environment, with screenshots, for affected layouts, content, interaction, journeys, and regressions. Check platform interaction and accessibility; for web, inspect semantics, names, keyboard and focus, contrast, and motion, using [UI accessibility](references/vstack/capabilities/ui-accessibility/REFERENCE.md) in review mode for a requested full assessment and [Web performance](references/vstack/capabilities/web-performance/REFERENCE.md) only when performance is requested (in review mode when assessing). Distinguish source, screenshot, automated, keyboard, and assistive evidence.
5. In assess mode, return strengths and findings ordered by priority. For substantive work, use [Quality validation](references/vstack/protocols/quality-validation.md), with [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in review mode for medium and high tiers of change work; in assess mode run it read-only, revising only the report or gathering permitted evidence until the declared coverage is accepted.
