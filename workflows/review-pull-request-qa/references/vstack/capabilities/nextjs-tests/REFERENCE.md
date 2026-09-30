## Contract

- Input: A Next.js revision, route or flow, expected behavior, environment, and authorized test scope.
- Output: Reproducible findings, observed evidence, coverage gaps, and the smallest recommended repair.
- Effects: Diagnosis without source repairs. Authorized tests may start a local server and exercise isolated test data; the caller owns repairs and convergence.

### Acceptance

- The report identifies the revision, route, expected behavior, environment, and checked states or viewports.
- Rendering, hydration, and interaction claims have observed browser evidence.
- Findings are reproducible and supported by sanitized evidence.
- Browser gaps are explicit and never become browser-behavior claims.

## Procedure

1. Discover applicable instructions, scripts, lockfile, installed Next.js version, router conventions, tests, candidate revision, route, expected behavior, and authorized environment. Use version-matched guidance for routing, caching, and Server Actions.
2. Match a running server to the repository through workspace, launch logs, URL, and port. Inspect configuration or launch the approved command in a managed session; never kill an unrelated server.
3. Use installed Playwright, Cypress, browser automation, browser MCP, or authorized manual evidence. Optional Next.js DevTools diagnostics complement logs, builds, and tests; do not install or require a vendor tool. If browser execution is unavailable, run permitted source, unit/server, or HTTP checks, skip browser-only steps, and report the browser-coverage gap.
4. For a bug, reproduce it with an isolated failing scenario. Start console, page-error, request, and server-diagnostic collection before navigation, without retaining secrets.
5. Navigate to the real route, await meaningful readiness, execute the flow with observable role or name assertions, and verify the visible outcome, navigation, and required persisted state.
6. Cover direct entry or reload, relevant client navigation, loading, error, empty, and auth states, plus supported viewports. For a responsive public UI, include mobile and desktop; state narrower coverage.
7. Check accessible names, semantics, keyboard operation, and focus when they affect the requested browser flow. Use [Ui accessibility](../ui-accessibility/REFERENCE.md) in review mode for a full accessibility assessment when relevant and available.
8. Return findings, evidence, coverage, and limits. Test a repaired candidate only when supplied and authorized; otherwise name the exact follow-up route and check. Send material uncertainties and proof to the caller's Quality Validation pool; otherwise return the next decisive check.

## Pitfalls

- A click, URL change, screenshot, quiet console, HTTP result, or accessibility tree alone does not prove the requested user flow. Observe the required browser outcome.
- HTTP checks prove status, headers, redirects, and bodies; they do not prove rendering, hydration, or interaction.
