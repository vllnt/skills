---
name: capability-stack-packages
description: Discover a stack's accessible source repositories and published packages, verify latest and canary releases, and compare consumer dependencies without installing or maintaining a fixed package list.
---

# Capability Stack Packages

Return current package inventory and compatibility evidence. Read repositories and registries; discover owners, scopes, exclusions, consumers, and channel policy from applicable rules. Do not install, publish, retag, edit configuration, change access, or maintain a fixed package list.

## Procedure

1. Resolve the requested package or inventory scope, authorized owners, source hosts, registries, and target consumers. Record time, visibility, exclusions, and access limits; keep private evidence out of public results.
2. Paginate each selected source owner within that scope; inspect revisions, root/workspace manifests, and publish configuration. Resolve truncated trees and label archive, fork, example, and private evidence. Enumerate all accessible owners only for an explicitly account-wide inventory.
3. Paginate registry listings and scope search; union source, publication, and consumer manifest/lockfile names. Deduplicate by registry/name; registry-only entries remain candidates.
4. Read each candidate's tags, versions, dates, deprecation, exports, peers, engines, and available integrity/provenance. Distinguish not-found, denial, transport failure, and source-only evidence; latest/canary tags are mutable evidence, not compatibility proof.
5. Compare tags, dates, releases, and permitted channel policy. Report missing canaries, prereleases under latest, unpublished sources, and deprecation. Call a canary stale only under an applicable freshness policy; otherwise report facts without selecting a channel.
6. Compare consumer declarations and lock resolutions with candidates; intersect peer, engine, runtime, and platform constraints. Missing metadata or resolution remains unverified.
7. For material unresolved discovery or compatibility questions, use independent discovery, review, and critique perspectives when available; otherwise cover them sequentially and report the limit. Reuse caller evidence only when scope, candidate, environment, and read time remain current.
8. Return latest/canary evidence, consumer constraints, incompatible groups, and a coverage ledger. Compare the current inventory with the DoD; repeat affected reads after corrections. Finish only for the stated accessible scope with exhausted pagination; gaps have their next read, never a false complete result.

Use the [GitHub/npm procedure](references/github-npm.md) only for those providers; otherwise use the selected provider's equivalent supported read APIs.

## Definition of Done

- The report identifies selected owners, registries, scope, exclusions, time, pagination coverage, visibility, and access gaps.
- Each discovered candidate has source or source-gap evidence plus current tags, exact versions, dates, deprecation, peers, engines, and channel eligibility where accessible.
- Relevant consumer declarations and lock resolutions are compared without claiming installation or runtime compatibility.
- The output is read-only package evidence; it does not select versions, recommend adoption, install, publish, or retag.
