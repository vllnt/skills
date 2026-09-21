# Version reference synchronization

Discover the target package and authoritative version from manifests, release configuration, tags, or the approved release plan. A monorepo may have several independent versions. Tags are evidence, not automatically the source of truth; no tags does not require creating a release before local documentation can be checked.

Inspect current installation commands, download links, badges, and generated catalogs in the authorized scope. Read matches in context. Update only claims that mean the current release; preserve `Since v1.2.3`, compatibility ranges, dependency versions, migration examples, and historical changelog sections. Do not globally replace every old version string.

Apply authorized reversible documentation fixes without another confirmation round. Ask only when release identity or intended compatibility is consequentially ambiguous. For instruction files, preserve authoritative owners and use instruction-maintenance procedures before editing. Do not touch version manifests, tags, hosted releases, or unrelated packages unless separately within scope.

Regenerate catalogs only if they are established generated artifacts affected by the edit; reuse the existing generator and review the output for privacy and unrelated churn. Do not create optional catalogs as a side effect.

Verify current claims against the authoritative version and inspect the diff for preserved historical claims. Validate download targets using available authorized evidence; missing remote access means link existence is unverified, not that a guessed latest URL is safe. Report changed paths, intentionally retained old versions, evidence, and unresolved discrepancies.
