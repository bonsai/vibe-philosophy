# Rule 07 — Match Capability to Cost and Risk

**Type:** agent instruction  
**Priority:** mandatory for non-trivial work

## Rules

1. Choose a model, tool, and execution environment appropriate to task complexity, sensitivity, reliability requirements, and budget.
2. Prefer the least expensive adequate option, including local or reusable methods where appropriate; do not sacrifice required quality or safety merely to reduce cost.
3. Start with a bounded discovery step when it can reduce uncertainty before expensive analysis or broad agent fan-out.
4. Escalate to a more capable model or tool only when the current approach lacks the capability or evidence needed, and state the reason.
5. Set limits on retries, recursive work, parallel agents, search/API calls, and elapsed time.
6. Estimate usage before expensive work when practical. Clearly distinguish estimates from measured cost and unknown usage.
7. Do not invent provider prices, token counts, or savings. Report measurements only when the environment provides them.
8. Ask for approval when a run would exceed its authorized budget or create a material unapproved financial commitment.

## Completion check

The chosen approach is fit for purpose, bounded, and cost claims are labeled as measured, estimated, or unknown.

## Related contracts

- [Runtime controls](../docs/runtime-controls.md)
- [Autonomy model](../docs/autonomy-model.md)
