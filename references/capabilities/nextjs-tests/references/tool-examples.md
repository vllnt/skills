# Next.js verification examples

Adapt these patterns to repository scripts, installed versions and test fixtures. They describe test behavior, not commands verified against your application.

## Browser regression

Use an isolated test backend with no real billing or email effects. This example assumes the repository owns `test`, `expect` and an `orders` fixture with scoped `read` and cleanup support; implement through its existing fixture interface, not a production admin credential.

A browser regression test for a checkout, for example:

1. Registers console-error and page-error listeners before navigation, so hydration failures are captured.
2. Opens the page, fills the form through accessible labels, and submits through the button's accessible name.
3. Waits for the visible confirmation, reads the order id from the page, and polls the fixture's authoritative backend record until it is confirmed.
4. Fails if any console or page error was captured.

Write it with the installed runner's current API, as its documentation describes.


Add the relevant rejected-payment/validation path, duplicate-submission protection and reload persistence checks. Assert authoritative backend data, not a response manufactured by a browser route mock. MSW is useful for deterministic error UI tests; label those mocked tests rather than backend integration.

## Equivalent browser tools

With an installed browser CLI, inspect its help for navigation, console capture, accessibility tree, screenshots and interaction commands. Arrange capture before navigation where supported; otherwise use a runner that supports listeners for early errors. Record the browser/tool version and actual results. Do not assume optional flags or a DevTools MCP exist.

Wait for application readiness (a visible enabled control or expected data), not a fixed sleep. Network-idle is unreliable for streaming/polling pages. Select viewports from supported devices and changed layout breakpoints.

## HTTP-only diagnostics

An authorized HTTP client can check a target route's status, redirect chain, cache headers or server-rendered markup. Verify the base URL belongs to the selected app first. Report, for example: “HTTP 200 and expected server HTML observed; client hydration and checkout outcome not tested.” Never infer a working UI from a successful response.

## Regression evidence

For a fix, record the isolated before-fix failure and final passing run, including the tested revision. If execution is unavailable, return the test and source findings as unexecuted work, explain the missing capability and continue checks that can run.
