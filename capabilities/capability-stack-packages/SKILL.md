---
name: capability-stack-packages
description: Discover a stack's accessible source repositories and published packages, verify latest and canary releases, and compare consumer dependencies without installing or maintaining a fixed package list.
---

## Contract

- Input: A requested package or inventory scope, authorized owners, source hosts, registries, channel policy, and target consumers.
- Output: Current scoped inventory, latest or canary evidence, consumer constraints, compatibility gaps, and coverage ledger.
- Effects: Read-only discovery. Do not install, publish, retag, edit configuration, change access, or maintain a fixed package list.

### Acceptance

- The report identifies owners, registries, scope, exclusions, time, pagination coverage, visibility, and access gaps.
- Each candidate has accessible source or source-gap evidence plus current tags, versions, dates, deprecation, peers, engines, and channel eligibility.
- Relevant consumer declarations and lock resolutions are compared without claiming installation or runtime compatibility.
- The result remains read-only package evidence and does not select versions or recommend adoption.

## Procedure

1. Resolve requested scope, authorized owners, source hosts, registries, target consumers, exclusions, visibility, and access limits. Keep private evidence out of public results.
2. Paginate each selected source owner within scope. Inspect revisions, root or workspace manifests, and publish configuration. Resolve truncated trees and label archives, forks, examples, and private evidence. Enumerate all accessible owners only for an explicitly account-wide inventory.
3. Paginate registry listings and scoped search. Union source, publication, consumer manifest, and lockfile names; deduplicate by registry and name while retaining registry-only candidates.
4. Read candidate tags, versions, dates, deprecation, exports, peers, engines, and available integrity or provenance. Distinguish not found, denied, transport failure, and source-only evidence.
5. Compare tags, dates, releases, and permitted channel policy. Report missing canaries, prereleases under latest, unpublished sources, and deprecation. Call a canary stale only under an applicable freshness policy.
6. Compare consumer declarations and lock resolutions with candidates. Intersect peer, engine, runtime, and platform constraints; leave missing metadata or resolution unverified.
7. Return the coverage ledger and next read for every gap. Send material discovery or compatibility uncertainties and evidence to the caller's Quality Validation pool. Use [GitHub/npm procedure](references/github-npm.md) only for those providers.

## Pitfalls

- Latest and canary tags are mutable evidence, not compatibility proof.
- Pagination, denied access, and source-only packages change coverage. Do not report a complete inventory beyond the stated accessible scope.
