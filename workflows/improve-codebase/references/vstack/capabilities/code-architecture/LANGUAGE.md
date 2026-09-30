# Architecture vocabulary

Use the consumer's established terms. This optional reference clarifies a finding; it never requires renaming code or documentation.

- **Interface:** what a caller must know: inputs, outcomes, invariants, ordering, failures, required configuration, and relevant performance limits.
- **Implementation:** behavior hidden behind that interface.
- **Seam:** a place where behavior can change without changing callers.
- **Depth:** useful behavior hidden behind a small, learnable interface.

Check whether an abstraction earns its cost:

1. Delete it mentally. If its complexity disappears rather than returning to callers, it may be a pass-through.
2. Keep a seam only for a current need: variation, test isolation, safety, or contract ownership.
3. Test observable behavior through the caller-facing contract. Internal tests may exist, but do not expose internals only for tests.
