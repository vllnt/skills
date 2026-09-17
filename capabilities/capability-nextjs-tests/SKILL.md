---
name: capability-nextjs-tests
description: Verify and diagnose Next.js pages, hydration, runtime errors, routing and user flows using repository-native tests and available browser tooling.
---

# Capability Nextjs Tests

Verify and diagnose requested Next.js behavior. Browser evidence is required for rendering, hydration, and interaction claims; HTTP checks establish only status, headers, redirects, and response bodies. Return findings for an authorized repair owner; this skill does not implement fixes.

## Procedure

1. Discover consumer instructions, scripts, lockfile, installed Next.js version, router conventions, tests, candidate revision, route, expected outcome, and authorized environment. Use version-matched guidance for routing, caching, and Server Actions.
2. Match any running server to the repository by workspace, launch logs, URL, and port. A process or MCP listing is discovery evidence only; inspect configuration or launch the approved command in a managed session. Never kill an unrelated server.
3. Use installed Playwright, Cypress, browser automation, browser MCP, or authorized manual evidence. Optional Next.js DevTools diagnostics complement logs/build/tests; do not install or require a vendor tool.
4. For a bug, reproduce it with an isolated failing scenario. Start console, page-error, request, and server-diagnostic collection before navigation, without retaining secrets.
5. Navigate to the real route, await meaningful readiness, execute the flow with observable role/name assertions, and verify visible outcome, navigation, and required persisted state. A click, URL change, screenshot, or quiet console alone is insufficient.
6. Cover direct entry/reload and relevant client navigation, loading/error/empty/auth states, and supported viewports. For responsive public UI, include mobile and desktop; scope narrower products with stated coverage.
7. For the requested flow, check accessible names, semantics, keyboard operation, and focus where they affect browser behavior. A full accessibility assessment belongs to `capability-ui-accessibility` when requested and available; an accessibility tree is not a full audit.
8. Report reproducible findings and the smallest repair, then compare the current evidence with the DoD. Test a repaired candidate only when it is supplied and authorized; otherwise name the exact follow-up route and check. When material risk or uncertainty remains, use independent review and critique perspectives when available, otherwise cover them sequentially. These perspectives assess this procedure; the caller owns overall convergence. Missing access or authority is incomplete with its next decisive check.

When browser execution is unavailable, use source, unit/server, and HTTP checks, report browser gaps, and continue safe work. Return target, routes/states/viewports, tools and results, sanitized artifacts, findings, and limits. See [tool examples](references/tool-examples.md) and [optional integrations](references/mcp-plugins.md) when relevant.

## Definition of Done

- The report identifies the revision, route, expected outcome, environment, and checked states/viewports.
- Every rendering, hydration, or interaction claim has observed browser evidence; absent browser access is an explicit gap, not a claim.
- Findings are reproducible, evidence-backed, and include the smallest recommended repair; this capability makes no repair.
