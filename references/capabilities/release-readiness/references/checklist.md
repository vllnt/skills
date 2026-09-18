# Public-release checks

Derive essential requirements from intended distribution and repository policy. These are inspection prompts, not a fixed scorecard. Existing equivalent documentation and workflows count; do not add files solely to satisfy names in this list.

| Area | Evidence and action |
|---|---|
| License and redistribution | Inspect license and bundled dependencies/assets for intended use. A nonempty license file alone does not establish rights. Ask for an unresolved license decision; do not choose one silently. |
| Public instructions | Confirm users can identify the project, install or obtain it where applicable, and use supported behavior. Validate commands against source. Exact headings and byte counts are irrelevant. |
| Secrets and private data | Review included/tracked content and applicable history with available scanners and inspection. Pattern matches are leads, not proven leaks; no matches do not prove absence. Redact reports. For a real exposure, identify revocation/rotation and cleanup needs; never rewrite shared history automatically. |
| Contribution and security | Reuse existing guidance. Add separate documents only if useful or required. Never invent contacts; unresolved private reporting channels remain explicit gaps. |
| CI and required checks | Inspect effective triggers, job conditions, commands, dependencies, and candidate-specific results. Follow [ci-validation.md](ci-validation.md). CI optimization owns performance changes; this readiness check consumes candidate evidence. Missing optional lint is not an automatic blocker. |
| Change history | Use existing direct entries, fragments, generated notes, or another established release source. Changelog maintenance owns those artifacts; preserve historical versions. New projects do not need invented prior releases. |
| Version and packaging | Verify current installation/version claims and produced artifacts where relevant. Follow [version-sync.md](version-sync.md); do not replace historical versions blindly. |
| Ignore rules | Inspect whether generated or sensitive files can be accidentally included. A particular `.gitignore` is not mandatory if existing controls suffice. |
| Hosted metadata | Inspect only when access is available and relevant. Description/topics are usually optional; no arbitrary count. Hosted edits require authority. |
| Agent guidance and aliases | Optional. Preserve existing conventions and authoritative owners; do not add aliases merely for coverage. |
| Templates and docs structure | Optional. Reuse existing contribution paths. No mandatory issue templates, PR templates, or docs directory. |
| LLM catalogs | Optional unless actual project policy requires them. Follow [llms-generation.md](llms-generation.md) only when relevant. |
| TODOs | Evaluate actual unfinished behavior or misleading promises, not keyword counts. Do not create or move issues as a side effect. |
| Release messaging | Use [release-messaging.md](release-messaging.md) for concrete drafts; style preferences do not replace correctness checks. |

Report requirement, evidence, applicability, result (PASS/GAP/UNVERIFIED/NOT APPLICABLE), impact, and smallest recovery. Separate essential gaps from optional improvements. Missing access prevents claims about inaccessible settings, not local findings or authorized repairs.

For fixes, reuse coherent owners and apply already-authorized reversible edits without a blanket interview. Preserve unrelated work. Confirm consequential license/disclosure decisions and externally effectful operations when not already authorized. Create documentation only when the consumer's requirements call for it; review all changed content and links before claiming readiness.
