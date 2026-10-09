# Rule 02 — Validate Before Building

**Type:** agent instruction  
**Priority:** mandatory  
**Applies to:** product ideas, feature requests, automation, and new infrastructure

## Rules

1. Before implementing, inspect the current repository, existing products, tools, workflows, and prior decisions that may already solve the problem.
2. Identify whose pain or unmet need is being addressed and what observable evidence supports it.
3. Compare implementation against reuse, configuration, documentation, integration, and process changes.
4. State the expected marginal value, maintenance burden, risk, reversibility, and resource cost at a level proportionate to the task.
5. Prefer the smallest experiment that can distinguish a promising idea from a weak one.
6. Do not build merely because an implementation is possible or inexpensive.
7. If the need is uncertain, recommend observation or validation rather than presenting assumptions as facts.
8. If an existing solution is sufficient, explain how to reuse it instead of creating a duplicate.
9. Prefer work that demonstrably creates new value, enables new observation, closes a data-to-decision loop, improves through feedback, or creates reusable foundations.
10. Treat a UI as a connection between real experience and useful data, not merely a screen. Specify how observations will be structured, interpreted, and returned to a meaningful decision or action.
11. Evaluate the full loop: real-world contact → observation/recording → structure and storage → interpretation/proposal → human decision/action → outcome observation → improvement. Data collection alone is not a value proposition.
12. Include maintenance and operational burden in the value judgment; a technically feasible artifact is not automatically worth building.

## Completion check

Record the problem, existing alternatives checked, key assumptions, and the evidence that would justify proceeding.

## Related contracts

- [Rule index](./README.md)
- [Harness workflow](../docs/harness-workflow.md)
