# Issue Parallelism

Assess parallel work; do not dispatch it.

1. Map explicit dependencies, shared files or services, owners, and repository coordination rules.
2. Identify the bottleneck, a ready set, and work that must remain serialized.
3. Propose independent lanes only when their likely effects and shared resources are understood.
4. Recommend the first action that unlocks the most useful work. A lane is not an assignment or authority to create branches.

Report unknown dependencies as a coverage gap rather than a safe lane.
