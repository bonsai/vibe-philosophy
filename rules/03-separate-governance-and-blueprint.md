# Rule 03 — Separate Governance, Blueprint, and Task

**Type:** agent instruction  
**Priority:** mandatory  
**Applies to:** planning, design, implementation, and policy changes

## Rules

1. Keep durable constraints separate from desired outcomes and immediate tasks.
2. Treat **governance/declarations** as rules that constrain multiple tasks; treat a **blueprint** as the desired state, user experience, and acceptance criteria; treat a **task** as bounded work that may change as evidence arrives.
3. Keep narrative, motivation, and philosophical rationale distinct from executable requirements. Link them where useful; do not make agents infer acceptance criteria from metaphor.
4. Preserve existing invariants unless an authorized policy change explicitly changes them.
5. Before a consequential change, identify scope, exclusions, dependencies, acceptance criteria, verification, and recovery path.
6. Do not duplicate canonical work records, lifecycle rules, or evidence schemas owned by DDD. Reference the canonical records instead.
7. When documents disagree, identify the source and conflict; do not quietly merge incompatible requirements.

## Completion check

A reviewer can tell what must remain true, what outcome is wanted, what will change, and how success will be checked.

## Related contracts

- [Harness workflow](../docs/harness-workflow.md)
- [Runtime controls](../docs/runtime-controls.md)
- [DDD documentation](https://github.com/bonsai/DDD/tree/main/docs)
