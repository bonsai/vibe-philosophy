# Vibe Philosophy

**The philosophy and governance harness for Vibe AI.**

This repository defines how an AI development agent should frame problems, decide whether to build, execute work, verify outcomes, and learn from feedback. It is not itself the agent runtime.

## Start here

### Agent instruction rules

The numbered files at the repository root are source essays and conceptual material, not executable instruction files. Use the focused Markdown rules below as actionable guidance:

- [Rule index](./rules/README.md) — choose rules relevant to the task.
- [01 — Intent and instruction classification](./rules/01-intent-and-classification.md)
- [02 — Validate before building](./rules/02-validate-before-building.md)
- [03 — Separate governance, blueprint, and task](./rules/03-separate-governance-and-blueprint.md)
- [04 — Execute in bounded, verifiable steps](./rules/04-execute-with-bounds.md)
- [05 — Analyze failures and learn](./rules/05-analyze-failures-and-learn.md)
- [06 — Security, cost, and guardrails](./rules/06-security-cost-and-guardrails.md)
- [07 — Model and resource selection](./rules/07-model-and-resource-selection.md)
- [08 — Human authority and collaboration](./rules/08-human-authority-and-collaboration.md)
- [09 — Completion and reporting](./rules/09-completion-and-reporting.md)

1. [AGENTS.md](./AGENTS.md) — operating contract and non-negotiable invariants.
2. [001](./001) — the philosophical foundation: autonomous development, feedback, tacit knowledge, distributed cognition, and the limits of self-correction.
3. [Harness workflow](./docs/harness-workflow.md) — the operational cycle that turns the principles into agent behavior.
4. [Autonomy model](./docs/autonomy-model.md) — the Vibe-specific boundary between capability, permission, and responsibility.
5. [Runtime controls](./docs/runtime-controls.md) — the integrated harness, security, cost-management, guardrail, and stop/recovery contract.
6. [Skill learning](./docs/skill-learning.md) — how evidence becomes a reusable skill without turning one-off failures into universal rules.
7. [Vibe principles](./原則.md) — how to judge value, decide whether to build, and connect AI work to real-world outcomes.

## Relationship to DDD

[DDD](https://github.com/bonsai/DDD/tree/main/docs) owns the shared development method and canonical work records: Issues, Documents, Decisions, Tests, Evidence, lifecycle, and traceability. This repository complements DDD with Vibe-specific agent behavior, autonomy, runtime control policy, and skill learning. It does not duplicate DDD's record schemas or lifecycle.

The runtime-control contract is integrated rather than four separate checklists: the harness coordinates execution; autonomy determines authority; security limits access and data exposure; cost management bounds resource use; guardrails define allowed, approval-required, and prohibited actions. All apply before, during, and after execution.

## The harness loop

```text
INTENT
  ↓
CHECK EXISTING SOLUTIONS + VALIDATE PAIN
  ↓
DECLARATION (invariants) + BLUEPRINT (desired outcome)
  ↓
AUTHORIZE SCOPE + SET SECURITY / COST LIMITS
  ↓
TASK (bounded change)
  ↓
EXECUTION UNDER GUARDRAILS
  ↓
VERIFICATION (evidence)
  ↓
REFLECTION (what happened and why)
  ↓
LEARNING (reviewed reusable skills)
  └──────────────────────────────→ next intent
```

## Core distinctions

| Concept | Meaning |
|---|---|
| Intent | The outcome or change someone wants |
| Declaration | A durable constraint or invariant |
| Blueprint | A description of the desired state and acceptance criteria |
| Task | A bounded action that may change as evidence arrives |
| Observation | What was actually seen or measured |
| Hypothesis | An explanation that still needs testing |
| Feedback | Evidence comparing expected and actual outcomes |
| Skill | A reusable method supported by experience and review |

## Design principles

- **Do not build by default:** check existing solutions, real pain, and marginal value first.
- **Keep policy separate from work:** governing declarations should not be mixed with task instructions.
- **Make feedback inspectable:** retain the evidence behind conclusions.
- **Learn cautiously:** a failure is a signal, not proof of a universal rule.
- **Bound autonomy:** agents can propose improvements, but cannot silently change their governing contract.
- **Enforce least privilege and bounded cost:** tool access is not authorization; budgets and approval gates must apply throughout execution.
- **Stop safely:** ambiguity, policy conflict, suspected exposure, budget exhaustion, or unexplained side effects must halt the affected action.
- **Keep philosophy practical:** use thinkers as lenses for inquiry, not as role-play personas or substitutes for evidence.

## Scope

This repository owns philosophy, agent behavior contracts, autonomy boundaries, runtime-control policy, skill-learning rules, and the Vibe harness workflow. Runtime code and provider-specific integrations belong in implementation repositories.

## Language

The foundational essay is in Japanese. Agent-facing rules are written to be directly actionable; supporting essays explain why those rules exist.
