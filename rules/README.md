# Vibe AI Instruction Rules

These files contain the repository's operative, focused agent instructions. The former `原則.md` has been distilled into the relevant rules; no separate principle document is required. Load only the rules relevant to the current task; for consequential changes, always load Rules 01, 04, 06, and 09.

## Rules

| Rule | When to load | Main obligation |
|---|---|---|
| [01 — Intent and classification](./01-intent-and-classification.md) | Every request | Resolve outcome and distinguish declaration, task, and analysis |
| [02 — Validate before building](./02-validate-before-building.md) | New ideas, features, automation, infrastructure | Verify real need and existing alternatives first |
| [03 — Governance, blueprint, task](./03-separate-governance-and-blueprint.md) | Planning and design | Keep durable rules, desired outcomes, and bounded work distinct |
| [04 — Bounded execution](./04-execute-with-bounds.md) | Every implementation or tool-driven change | Work in small, scoped, verifiable increments |
| [05 — Failure and learning](./05-analyze-failures-and-learn.md) | Failures, unexpected results, retrospectives | Use evidence and tested hypotheses; avoid premature generalization |
| [06 — Security, cost, guardrails](./06-security-cost-and-guardrails.md) | Every consequential action | Check authority, least privilege, budget, approval, and stop conditions |
| [07 — Model and resource selection](./07-model-and-resource-selection.md) | Non-trivial or expensive work | Match capability to risk and bounded cost |
| [08 — Human authority and collaboration](./08-human-authority-and-collaboration.md) | Ambiguous goals, policy decisions, value trade-offs | Clarify uncertainty and preserve explicit authority |
| [09 — Completion and reporting](./09-completion-and-reporting.md) | Every non-trivial task | Report observed outcomes and evidence honestly |

## Precedence and boundaries

1. The repository's root [AGENTS.md](../AGENTS.md) is the governing agent contract.
2. [Runtime controls](../docs/runtime-controls.md) and [Autonomy model](../docs/autonomy-model.md) define Vibe-specific safety and authorization constraints.
3. These rule files operationalize those contracts for recurring task patterns.
4. Shared task records, decisions, tests, evidence, and lifecycle conventions remain owned by [DDD](https://github.com/bonsai/DDD/tree/main/docs).

When rules appear to conflict, do not silently pick a convenient interpretation. Apply the stricter safe constraint, surface the conflict, and request a decision when needed.

## Source material

The historical numbered essays `000`–`005` now live in [`archive/`](../archive/README.md). Treat them as source essays, drafts, and conceptual material, not active instructions. These rules distill actionable obligations without treating every historical proposal, code sketch, or philosophical claim as current policy.
