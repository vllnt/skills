# Page audit measurements

Heuristic resource and timing measurements to take through an available browser evaluator. They are not scores or conformance checks. Write each measurement as a small script from the current MDN documentation of the APIs named below, run it through the browser tool's evaluate command (its help says how to pass a script file), and return machine-readable JSON. Inspect and sanitize all outputs before sharing, including page text and resource URLs.

## Resource weight

From the Resource Timing API: request count, total bytes, bytes per initiator type, and the ten slowest and ten heaviest requests. Cross-origin timing restrictions and cache hits can yield zero or missing sizes, so the totals are not complete transferred page weight. Encoded body size and transfer size are different quantities. Resource URLs still need privacy review.

## Render-blocking candidates

From the document head: synchronous external scripts, stylesheets that apply to all or screen media, and third-party script hosts. Confirm timing and blocking in an actual browser trace; markup order alone does not establish causality.

## Navigation phases

From the Navigation Timing API: redirect, DNS, connection, TLS, time to first byte, response download, DOM processing, and load phases, or an explicit error when no navigation entry exists.

## Interpreting results

- These are **heuristics from one browser session**. Resource and timing signals need traces or comparable measurements before a causal claim. See [measurement workflow](../REFERENCE.md).
