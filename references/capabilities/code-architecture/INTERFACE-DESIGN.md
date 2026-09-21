# Interface Design

Compare alternative interfaces when the trade-off matters, not for every candidate. Remain read-only. Use existing project terminology and applicable instructions; no fixed glossary file or language-specific type system is assumed.

1. Frame observed caller needs, constraints, dependencies, and behavior to preserve. Use [DEEPENING.md](DEEPENING.md) for relevant dependency risks.
2. Compare a small number of plausible designs, including keeping or simplifying the existing interface. Prefer current callers over speculative flexibility. Use independent reviewers for a material unresolved trade-off; otherwise compare sequentially without blocking on delegation.
3. For each design, show the caller-facing contract (inputs, outcomes, invariants, ordering, and errors), a usage example, hidden complexity, dependency ownership, and regression checks.
4. Recommend the smallest design with a demonstrated benefit. Explain maintenance cost, migration risk, locality, and what evidence could change the recommendation.

Offer dialog for consequential unresolved choices, but do not require a user interview before producing a useful design. See [LANGUAGE.md](LANGUAGE.md) for optional terminology.
