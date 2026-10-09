# Vibe Philosophy

**The philosophy and governance harness for Vibe AI.**

This repository defines how an AI development agent should frame problems, decide whether to build, execute work, verify outcomes, and learn from feedback. It is not itself the agent runtime.

## Start here

1. [`AGENTS.md`](./AGENTS.md) — operating contract and non-negotiable invariants.
2. [`001`](./001) — the philosophical foundation: autonomous development, feedback, tacit knowledge, distributed cognition, and the limits of self-correction.
3. [Harness workflow](./docs/harness-workflow.md) — the operational cycle that turns the principles into agent behavior.
4. [Autonomy model](./docs/autonomy-model.md) — the Vibe-specific boundary between capability, permission, and responsibility.
5. [Skill learning](./docs/skill-learning.md) — how evidence becomes a reusable skill without turning one-off failures into universal rules.
6. [Vibe principles](./原則.md) — how to judge value, decide whether to build, and connect AI work to real-world outcomes.

## Relationship to DDD

[DDD](https://github.com/bonsai/DDD/tree/main/docs) owns the shared development method: Issues, Documents, decisions, evidence, tests, lifecycle, and traceability. This repository does not duplicate those models. It adds the Vibe-specific philosophy, autonomy boundaries, and skill-learning policy.

## The harness loop

```text
INTENT
  ↓
CHECK EXISTING SOLUTIONS + VALIDATE PAIN
  ↓
DECLARATION (invariants) + BLUEPRINT (desired outcome)
  ↓
TASK (bounded change)
  ↓
EXECUTION
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
- **Bound autonomy:** agents can propose improvements, but cannot silently change their own governing contract.
- **Keep philosophy practical:** use thinkers as lenses for inquiry, not as role-play personas or substitutes for evidence.

## Scope

This repository owns philosophy, agent behavior contracts, autonomy boundaries, skill-learning rules, and the Vibe harness workflow. Runtime code and provider-specific integrations belong in implementation repositories.

## Language

The foundational essay is in Japanese. Agent-facing rules are written to be directly actionable; supporting essays explain why those rules exist.