---
name: improve-ui
description: Improve an interface’s hierarchy, consistency, responsiveness, and accessibility while preserving journeys.
---

# Improve UI

Improve one interface without changing its supported journeys. Assessment skips interface changes and validates only findings and proposed checks.

## Workflow

1. Confirm the platform, screens, journeys, constraints, design system, candidate, evidence type, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles.
2. Inspect layouts and applicable loading, empty, error, validation, disabled, focus, and feedback states; compare usability and shared-component impact.
3. Apply an authorized correction at the owning boundary, preserving content, navigation, platform-relevant accessible interaction, and supported states.
4. Exercise the supported target environment for affected layouts, content, interaction, journeys, and regressions. For web, use `capability-ui-accessibility` for a requested full accessibility assessment when available.
5. Validate the interface or assessment report against its mode-specific criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive work, or assess perspectives sequentially and state unavailable independence; triage findings, repair only authorized interface gaps, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue authorized repair or report revision and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; missing visual or interaction proof remains a gap, and N/A needs a reason.

## Definition of Done

- Affected screens, journeys, constraints, and evidence are identified.
- Assessment returns findings and checks without repair.
- Authorized changes preserve supported interaction and applicable accessibility requirements.
- Observed layouts, access behavior, and limits are reported.
- Completion requires current mode-specific validation acceptance; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
