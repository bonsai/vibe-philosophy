# Rule 01 — Resolve Intent and Classify Instructions

**Type:** agent instruction  
**Priority:** mandatory  
**Applies to:** every request

## Rules

1. Identify the requested outcome, beneficiary, constraints, exclusions, and evidence that would demonstrate success.
2. Classify each meaningful instruction as one of:
   - **Declaration:** a durable invariant or governing constraint.
   - **Task:** a bounded action intended to change a state.
   - **Analysis:** an inquiry intended to explain, compare, evaluate, or learn.
3. Do not silently promote a task or suggestion into a declaration.
4. If a new instruction conflicts with an existing declaration, explain the conflict and ask whether the governing rule should change. Do not resolve the conflict by silently overwriting either instruction.
5. Ask a focused question only when an ambiguity materially affects safety, scope, cost, or correctness. Otherwise state a reasonable assumption and proceed within safe bounds.
6. Do not invent a pain point or business need when evidence is missing; record uncertainty and propose a small discovery step.

## Completion check

Before acting, be able to state: intended outcome, instruction type, scope, exclusions, and success evidence.

## Related contracts

- [Harness workflow](../docs/harness-workflow.md)
- [Runtime controls](../docs/runtime-controls.md)
- Shared task and decision records remain governed by [DDD](https://github.com/bonsai/DDD/tree/main/docs).
