# GitHub and npm discovery

1. Read the requested package or inventory scope, the consumer's selected GitHub owners, and npm registries/scopes. Confirm available credentials without displaying tokens or complete credential configuration.
2. List repositories for each selected owner through the supported API or CLI with pagination. Include authorized private repositories; record inaccessible scope. Enumerate an account and its accessible organizations only for an account-wide request, then deduplicate repositories.
3. Read each default-branch revision and tree. If a recursive tree is truncated, traverse the omitted directories; do not call it complete. Inspect package manifests, workspace definitions, and publication configuration. Exclude dependencies/vendor outputs from source scanning; retain evidence for intentionally excluded examples/private packages.
4. Use the installed npm CLI's supported read-only package-access listing, when authorized and available. Confirm its actual account visibility; access listings do not prove unseen private packages are absent. Do not use access-changing subcommands.
5. Supplement with paginated public registry search, filtering exact scope boundaries. Union results with discovered source and consumer package names, including unscoped packages only where ownership is evidenced. npm search is an index, not an authoritative full-scope ledger. GitHub Packages is a different registry from npmjs.org.
6. For every name, query its explicitly selected registry's metadata (dist-tags, versions, and publish times) through the registry endpoint or the installed npm CLI's read-only view command, taking its options from the CLI's help. Read each candidate exact version's peers, engines, exports, deprecated flag, and distribution metadata. Do not use `npx`, install, lifecycle scripts, or publish to inspect metadata.
7. Compare dist-tags and the version list by publish time and semver. Prefer a non-prerelease / LTS when one exists; otherwise report the newest usable prerelease. Record absent tags; do not invent them. `latest` can be a prerelease or older than another tag — report facts and the chosen release with reason.
8. Inspect consumer manifests and lockfiles without rewriting them. Distinguish declared ranges, resolved versions, source/workspace links, overrides, and missing lock evidence. Check compatible peer intersections, including framework/TypeScript/native targets; keep private repository names out of public summaries.
9. Return an evidence table and coverage ledger with read time and scope. Report any rate limits, timeouts, missing auth, incomplete pages/trees, or unsupported registries. Retry only when the cause changes; continue unaffected sources.

## Scenario checks

- More than one page of repositories/packages: collect all pages and deduplicate repeated results.
- Published package has no accessible source: retain it with registry evidence and a source gap.
- Repository has a package manifest but registry returns 404: do not list it as published.
- `latest` is a prerelease or older than another publish: preserve exact facts and explain the selected release.
- Only a prerelease exists: report version and reason; do not claim a non-prerelease exists.
- Shared configs require incompatible TypeScript peers: return the incompatible set and a compatible alternative or unresolved decision.
- Declared range and lockfile disagree: report both; do not claim a tag is installed.
- Private package is denied or a recursive tree is truncated: return partial coverage rather than an empty or complete inventory.
- API and source metadata agree: still require the executing caller to prove installation and runtime behavior.
- A single-package request: inspect the selected package and its declared consumers; do not enumerate unrelated owners or repositories.

## Official references

- [GitHub repositories and pagination](https://docs.github.com/en/rest/repos/repos)
- [npm access listing](https://docs.npmjs.com/cli/access/)
- [npm view metadata](https://docs.npmjs.com/cli/commands/npm-view/)
- [npm scope and visibility](https://docs.npmjs.com/package-scope-access-level-and-visibility/)
