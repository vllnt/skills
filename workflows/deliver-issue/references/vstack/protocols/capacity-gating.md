## Contract

- Input: A planned large job (long session, batch, evaluation, parallel fan-out), its target host, its priority, and any shared quota signal configured by consumer rules.
- Output: A level of `green`, `amber`, or `red`, with the decision to start, limit, or queue, and its evidence.
- Effects: Reads host and quota state, and queues or limits only work the caller owns. It never deletes data or stops another owner's work to free resources.

### Acceptance

- Host headroom and any configured quota signal are read on the target host before a large job starts.
- The decision follows the level and the job's priority; a configured signal that is missing or stale counts as `amber` and is reported once.
- Parallel workers, builds, reviewers, and critics stay within the level's limits.
- No development server, watcher, or test runner the caller started is left running unattended.

## Procedure

1. Read headroom on the target host with one quick command: available memory, disk usage of the working volume, load average, and core count. Example default limits, to replace with consumer rules: available memory below 20% of total, disk above 85% used, or load average above the core count each means do not start. Headroom within every limit is `green`, any limit exceeded is `red`, and an unreadable measurement is `amber`.
2. When consumer rules configure a shared quota or capacity signal, read only its level and timestamp. A configured signal that is missing, unreadable, or older than its rule's maximum age (default: two check intervals) counts as `amber`; report it once to its owner. With no signal configured, use headroom alone.
3. Take the worst of headroom and signal as the level. Example default behavior, to replace with consumer rules:
   - `green`: start normally; parallel workers, the full reviewer set, and an independent critic as useful.
   - `amber`: only top-priority work starts, or only work the requester marks urgent when no priority is defined. One worker at a time; two or three key review angles run sequentially; an independent critic only for critical changes such as security, releases, data, or infrastructure.
   - `red`: start nothing new and queue everything, except an emergency class when consumer rules define one.

   Reduced capacity never waives required review or proof: queue the work, or report it blocked, rather than accept it with fewer checks.
4. Queue by preparing the workspace and brief without starting the worker. Release queued work by consumer-defined priority when the level improves; recheck on the next scheduled check or completion event, not by polling.
5. Keep resource hygiene during and after work:
   - Cap workers and parallel builds to the current headroom; recheck before adding parallel workers.
   - Never leave development servers, watchers, or test runners running unattended.
   - Never delete repositories, data, volumes, backups, or unpushed work to free resources; report pressure to the resource owner.
   - When a session is flagged for leaking memory or saturating CPU, its owner fixes or restarts it and confirms to whoever flagged it.

## Pitfalls

- Small read-only commands need no gate; gating every action wastes more than it saves.
- A green level at start does not cover later fan-out; recheck before adding parallel workers.
