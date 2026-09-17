# Vstack

Vstack includes the reusable packages, skills, methods, and project rules used across Vstack projects. This profile defines its web, desktop, mobile, backend, CLI, and stateless-service preferences. The profile applies to project creation and alignment, not to building this Markdown collection. Apply it when selected by the user or bound by applicable user/project instructions. Preserve intentional project exceptions and resolve consequential conflicts before changing them.

## Stack

| Surface | Preferred foundation |
|---|---|
| Web | Next.js and TypeScript. |
| Desktop | Tauri with a Next.js frontend compatible with static export. |
| iOS, Android, tablets | Expo and React Native with TypeScript. |
| Stateful backend | Convex as the canonical owner of durable business state and final authorization. |
| CLI | TypeScript and Effect. |
| Lightweight stateless API | TypeScript and Effect; no database or persistent backend without a concrete requirement. |

## Package reuse

- Source organization: [vllnt on GitHub](https://github.com/vllnt); npm scope: [@vllnt on npm](https://www.npmjs.com/org/vllnt). Inspect actual consumer use when assessing adoption.
- No generator is selected by this profile. Use one only when independently selected and verified for the project.
- Inspect the selected repositories and organizations; membership does not make every package relevant to every product.

1. Search the relevant accessible `vllnt` repositories and npm scope `@vllnt` before implementing a foundation already covered by them. Bound discovery to needed functions; enumerate the entire selected catalog only for an inventory request. Use `capability-stack-packages` when available; otherwise discover source manifests, registry listings, and current metadata directly, exhaust relevant pagination, and report coverage gaps. Do not maintain a fixed package list.
2. Prefer compatible packages and supported extension points for an actual need. Evaluate config, backend components/helpers, logging, analytics, and UI; record an evidence-based exception when another choice better preserves a required contract.
3. Verify exact versions, permitted channels, exports, peer/runtime compatibility, maintenance, license, and required setup. For development and testing, prefer a compatible, nondeprecated canary when available. This profile supplies that channel preference; do not ask again for each reversible adoption. If canary is missing, incompatible, or stale under an explicit freshness policy, explain the fallback or unresolved choice. An older compatible canary without a freshness policy retains the testing preference; report its age rather than inventing a cutoff. Production follows its explicit project release policy.
4. Reuse the repository package manager and lockfile. Keep configs shared while retaining consumer-specific paths and platform settings.
5. Do not add unused packages, fork a package for convenience, or implement a duplicate foundation merely to avoid investigating its public API. Propose the smallest extension or documented gap when coverage is insufficient.

## Data and runtime boundaries

- Convex owns canonical durable application state, business invariants, and access decisions for stateful products. Clients may keep UI state, caches, and optimistic/offline views with explicit reconciliation.
- Keep business truth out of duplicate client stores or a second application database. Third-party records remain external authority where unavoidable; define their synchronization and conflict boundary explicitly.
- Presentation checks improve UX; repeat security and business validation at the authoritative backend boundary.
- Stateless services may transform requests and call declared external systems; do not give them a competing durable data store by default.
- Keep desktop UI compatible with the shell: Next.js server routes, server actions, and request-time rendering do not run inside a static frontend bundle. Put required server behavior in the declared backend. Verify native packaging separately. See [Tauri's Next.js guide](https://v2.tauri.app/start/frontend/nextjs/).
- Check React Native/Expo compatibility independently: web React or DOM support does not imply mobile support. See [Convex React Native support](https://docs.convex.dev/client/react-native).
- Select Effect and its runtime adapters from the chosen version's exports and documentation; do not mix incompatible package generations. See [Effect documentation](https://effect.website/docs/).

## Binding to a project

1. Make this profile available through a user-selected document or applicable user/project instruction reference. Installing an individual skill does not install or activate this profile.
2. Record the selected surfaces, package sources, allowed release channels, data/service owners, environments, verification commands, and justified exceptions in the consumer's owning instructions/configuration.
3. Use `build-project` for a new baseline and `improve-project` for adapting an existing project. Both use `capability-project-alignment` for target decisions and `capability-stack-packages` for live package evidence, with standalone fallbacks.
4. A preferred target does not authorize destructive migration, production cutover, or overwriting existing work. Follow established scope and preserve a viable staged path.
