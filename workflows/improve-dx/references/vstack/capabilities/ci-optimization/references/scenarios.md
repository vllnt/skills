# CI scenario checks

Use isolated fixtures or authorized non-production runs. These are acceptance cases, not claims that a provider has been exercised. Capture baseline failure and candidate behavior for the case you repair.

| Scenario | Evidence and expected decision |
|---|---|
| Documentation-only change with required validation | Prove selection says not applicable and the stable required gate completes. A workflow-level filter that leaves the gate pending is not equivalent protection. |
| Selected test job fails, is cancelled, or unexpectedly skipped | Gate runs and rejects each state; it cannot turn missing test evidence into success. A failed selection job also rejects. |
| Shared lockfile changes; file deleted/renamed; shallow checkout lacks base | Include all affected dependents or run the full suite. Empty target lists are not proof of no impact. |
| Merge-queue revision differs from PR head | Validate the actual merge candidate and correct base; preserve required check identity. |
| Warm build cache hides changed compiler flags or environment | Baseline fixture demonstrates stale output; revised keys miss on changed inputs, hit on identical inputs, and restore all required outputs. Compare uncached output behavior. |
| Fork attempts to seed a cache consumed by release | Reject cross-trust writes/restores and keep secrets unavailable. Test using inert markers, never real secrets or a live release. |
| New parallel matrix shortens wall time but doubles runner minutes | Report both latency and billed cost, including runner multipliers/setup. Accept only against the project's actual tradeoff; unknown rates mean unknown savings. |
| Cancel superseded validation with a child service | Verify only the intended run is cancelled and owned processes/services and locks are cleaned. Simulate interrupted cleanup and identify the recovery owner; do not cancel deployment work. |
| Remote history/API or specialty CLI unavailable | Produce configuration findings and local selection/status fixtures, list unavailable timing/security evidence, and avoid claiming measured remote improvement. |

For a provider-neutral status fixture, enumerate required target sets and feed the gate successful, failed, cancelled, skipped, and missing results. Include both proven-not-applicable and unknown-selection cases. Test the actual implementation when available; a table walkthrough alone cannot prove provider status semantics.
