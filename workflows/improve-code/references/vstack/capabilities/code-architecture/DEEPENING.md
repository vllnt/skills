# Consolidating shallow modules

Use this reference only when consolidation is a supported option.

1. Keep pure or local behavior behind its existing owner when that reduces demonstrated friction.
2. For an owned remote dependency, define a boundary only when its transport or contract must vary. Test the real transport in an isolated environment when material.
3. For a third party, reuse the existing integration owner. Mocks isolate local logic but do not prove the external contract; use a sandbox or contract check when needed.
4. Replace tests only after the new owner proves the preserved success and failure behavior. Keep distinct regression coverage.

Do not create adapters or extra seams solely to satisfy a pattern.
