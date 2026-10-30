# Default @vllnt packages

Preferred foundations for Vstack projects, from the [@vllnt npm scope](https://www.npmjs.com/org/vllnt). For a listed function, use its package before custom code or a third-party alternative. Keep an existing equivalent only when consumer rules or a contract in use require it, and record that exception.

## Channel rules

- Stable packages: default to the latest stable release.
- Canary-only packages: pin the exact version listed here until a stable release exists. Moving the pin is a deliberate change with its own verification.
- `@vllnt/typescript` and `@vllnt/eslint-config`: default to the 2.x line.
- Before relying on an entry, confirm it is still published, not deprecated, and compatible with the consumer's framework, TypeScript, and runtime peers.
- For a function not listed, use the Stack packages procedure when installed; otherwise query the registry scope directly. Do not name, assume, or create a package; report the gap as a package request.

## Tooling and UI

| Function | Package | Channel |
|---|---|---|
| TypeScript configuration | `@vllnt/typescript` | stable, 2.x |
| ESLint configuration | `@vllnt/eslint-config` | stable, 2.x |
| Web UI components | `@vllnt/ui` | stable |
| Shared and native UI primitives | `@vllnt/ui-core`, `@vllnt/ui-native` | canary-only, pin `0.1.0-canary.20260917105553.sha7466647a4ba5` |
| Structured logging | `@vllnt/logger` | stable |
| Client analytics with consent | `@vllnt/analytics` | stable |
| `llms.txt`, `llms-full.txt`, and raw-markdown pages for Next.js | `@vllnt/next-llms` | canary-only, pin `0.1.0-canary.bca5ab7` |

`@vllnt/ui-native` is for Expo and React Native; do not infer mobile support for `@vllnt/ui` or `@vllnt/analytics` from React compatibility.

## Convex

Use `@vllnt/convex-helpers` for host-side builders, errors, validators, pagination, HTTP, env, and observability. Mount a component below only when the product needs its function; membership in this table does not make every component relevant.

| Function | Package | Channel |
|---|---|---|
| Host helpers | `@vllnt/convex-helpers` | stable |
| Event ledger and activity feed | `@vllnt/convex-events` | stable |
| Analytics rollups, funnels, retention | `@vllnt/convex-analytics` | stable |
| Consent ledger | `@vllnt/convex-consent` | stable |
| Do-not-contact list and opt-in proof | `@vllnt/convex-suppression` | stable |
| Roles and grants | `@vllnt/convex-permissions` | stable |
| Membership and relationship graph | `@vllnt/convex-memberships` | stable |
| Invitations | `@vllnt/convex-invitations` | stable |
| Hashed-secret tokens | `@vllnt/convex-tokens` | stable |
| Feature flags | `@vllnt/convex-flags` | stable |
| A/B experiments | `@vllnt/convex-experiments` | stable |
| Idempotency keys | `@vllnt/convex-idempotency` | stable |
| Usage metering | `@vllnt/convex-metering` | stable |
| Consumable balances and spend ledger | `@vllnt/convex-wallet` | stable |
| Transactional email queue | `@vllnt/convex-email` | stable |
| Notifications inbox | `@vllnt/convex-notifications` | stable |
| Comments and annotations | `@vllnt/convex-comments` | stable |
| Reactions, votes, likes | `@vllnt/convex-reactions` | stable |
| Unique slugs and handles | `@vllnt/convex-slugs` | stable |
| Provider-neutral music catalog | `@vllnt/convex-music` | stable |
| Ephemeral subject groups | `@vllnt/convex-buckets` | canary-only, pin `0.1.0-canary.0` |
| XP, levels, streaks | `@vllnt/convex-progression` | canary-only, pin `0.1.0-canary.0` |
| Scheduled per-subject allowances | `@vllnt/convex-quota` | canary-only, pin `0.1.0-canary.0` |

## Other

`@vllnt/dig` (canary-only, pin `0.1.0-canary.fcb1735`) is a TypeScript client for a local knowledge-base daemon. Use it only when a project already runs that daemon.
