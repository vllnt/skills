# Mock exception gate

A test double is a substitute dependency: a stub returns configured values, a mock also checks interactions, and a fake implements a simplified behavior. All can disagree with reality. A passing double-based test is not evidence that the real dependency works.

## Prefer reality

Use pure functions directly, real owned modules, temporary files, isolated databases with the relevant engine/constraints, local services, and authorized provider test environments. Do not send real email, charge money, or use production credentials to avoid a mock. A different database engine or emulator must not stand in for production locking/transaction guarantees it does not implement.

Clock/randomness controls are reasonable for deterministic boundary cases when they do not replace the behavior under test. A fake clock does not prove real scheduling, event-loop, lease, or concurrency behavior. Restore controls after each test and retain relevant real-runtime checks.

## Permit a boundary double only with evidence

Record, near the test or in the test documentation:

1. **Boundary and reason:** exact substituted operation; why local reality or an authorized sandbox is unavailable, unsafe, or cannot produce the needed failure.
2. **Contract evidence:** the relevant version and independently verified request/response, errors, serialization, and semantics. Prefer a shared contract suite run against both the real adapter/provider test environment and the double. Types or copied docs alone do not establish runtime behavior.
3. **Strictness:** reject unexpected calls or input; no universal success responses or permissive catch-all. Include relevant malformed data, denials, timeouts, and partial failure cases.
4. **Outcome proof:** assert the real system's state or output, not just that the mock returned its configured value. Do not compute the expected result using the same production algorithm being tested.
5. **Sensitivity:** a plausible broken mapping, omitted required call, swallowed error, or duplicate effect causes the intended test assertion to fail in an isolated experiment.
6. **Limits and revalidation:** state which real integration remains untested and rerun contract verification when the dependency, adapter, or double changes.

A verified double supports only the checked behavior. If contract evidence is unavailable, label the test provisional and keep the integration gap open. Do not claim it eliminates false-positive risk.

## Example

For a retrying payment adapter, use the real application handler and isolated ledger. Prefer a provider sandbox for request/signature and response compatibility. If a deterministic connection failure requires a local fault-injecting server, document that exception, drive the real HTTP adapter, assert ledger consistency and retry limits, and challenge it with a broken deduplication guard. The fault server does not prove that the payment provider executes a charge exactly once; retain separate provider-contract evidence and report its limits.
