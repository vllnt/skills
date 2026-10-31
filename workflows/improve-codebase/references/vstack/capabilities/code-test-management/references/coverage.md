# Coverage and opportunities

## Discover surfaces and personas

Inspect entry points, exports, routes, schema, authorization, pricing, docs, and actual tests. A repository may expose several surfaces. Derive personas from distinct intent, access, and interface; merge identical behavior. Include operators and adversarial callers where evidenced. Accessibility, locale, device, and paid tiers matter when they change the journey. Do not invent an operator UI or infer that operators only use a CLI.

| Surface | Representative real verification |
|---|---|
| Web | Browser → real backend → persisted result; keyboard/accessibility and relevant viewport journeys |
| Backend | Real handler/transport → owned services → isolated store; denial, retry, rollback/recovery |
| CLI/TUI | Built process, args/stdin, stdout/stderr, exit status, filesystem effects, noninteractive behavior |
| Library/SDK | Consumer imports built/packed public API; runtime, type, and export contracts |
| MCP | Real client and transport; schema errors, authority denial, cancellation, actual tool outcome |
| Mobile | App on device/emulator; offline/recovery, deep links, accessibility |

Unit tests prove narrow logic; integration tests prove real collaboration; E2E tests exercise the delivered artifact as a consumer. UI and multi-step chains describe journeys, not mutually exclusive test levels. Choose applicable layers by risk, not a mandatory Cartesian product.

## Map protection

For broad audits, use rows of persona + journey and columns for relevant unit, integration, E2E/UI, and chain checks. Mark covered, partial, gap, unknown, or N/A with a reason. Link covered cells to actual assertions and run evidence. A mocked seam cannot establish its real integration contract. Cross-persona tests must drive both actors with distinct sessions and real intermediate state.

Sweep these composition risks where applicable:

- A → B → C wiring never exercised together; wrong shape, argument order, units, or missing fields.
- Producer/consumer drift hidden by separately hardcoded fixtures.
- Invalid state sequences, repeated terminal operations, expiry, and recovery.
- Write → read and encode → decode round trips; include independently known expected values because two equally wrong codecs can round-trip successfully.
- Partial failures, rollback/compensation, cleanup, and error propagation.
- Authenticated but unauthorized callers, wrong tenant, alternate entry points, and forbidden side effects.
- Duplicate delivery and retry after partial completion, including idempotency-key scope/collisions.
- Concurrent operations against shared state. Use controlled interleavings when possible; parallel invocation alone does not prove a race occurred.
- Malformed or hostile input through the real boundary to the sink.
- Dependent features affected by shared-module changes.

## Gaps and opportunities

Prioritize by evidenced impact, likelihood, and reach; explain uncertainty instead of manufacturing precise scores. Look for zero-test personas, weak denial tests, a real seam test replacing brittle mock-heavy tests, faster isolated setup, missing recovery behavior, and public contracts worth pinning. Report product/design findings separately from authorized testing changes.

Each actionable item names the location, persona/journey, plausible defect, risk, test file/name, arrange/act/assert, real dependencies, exceptions, and acceptance command. Dedupe one test that genuinely closes several gaps, without claiming it covers every layer. A small feature needs a short list, not a repository-wide census.
