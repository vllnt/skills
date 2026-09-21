---
name: improve-ui
description: Improve an interface’s hierarchy, consistency, responsiveness, and accessibility while preserving journeys.
---

## Goal

Improve one interface while preserving its supported journeys, or return an assessment with proposed checks.

### Definition of Done

- Affected screens, journeys, constraints, design system, and evidence are explicit.
- Assessment returns findings and checks without changing the interface.
- Authorized changes preserve supported interaction and applicable accessibility requirements.
- Observed layouts, access behavior, and limits are reported.
- Current validation accepts the selected mode; an unmet required criterion remains REVISE or BLOCKED.

## Boundaries

- Do not treat a screenshot as proof of keyboard, assistive, responsive, or runtime behavior. Obtain the relevant evidence or report the gap.

## Workflow

1. Resolve platform, screens, journeys, constraints, candidate, evidence type, and acceptance criteria from the request, instructions, and loaded principles.
2. Inspect layout and applicable loading, empty, error, validation, disabled, focus, and feedback states. Identify shared-component impact.
3. In change mode, apply the smallest authorized correction at the owning boundary while preserving content, navigation, supported states, and accessible interaction.
4. Exercise the target environment for affected layouts, content, interaction, journeys, and regressions. For a requested full web accessibility assessment, use [UI accessibility](references/vstack/capabilities/ui-accessibility/REFERENCE.md) in review mode with the scope, candidate, and evidence. Use [Web performance](references/vstack/capabilities/web-performance/REFERENCE.md) only when performance is requested; in assessment mode, inspect criteria and propose checks only.
5. For substantive work, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its self-assess, independent interface review, critique, triage, improve, and renewed-verdict loop directly. In assessment mode, revise only the report or gather permitted evidence.
