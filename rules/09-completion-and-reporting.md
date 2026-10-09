# Rule 09 — Verify and Report Honestly

**Type:** agent instruction  
**Priority:** mandatory for non-trivial work

## Rules

1. Compare actual outcomes with the stated acceptance criteria.
2. Run the smallest relevant checks that provide meaningful evidence.
3. Report changed resources, checks performed, observed results, unresolved risks, and what remains unverified.
4. Separate observation, interpretation, hypothesis, decision, and unknown.
5. Report resource usage only when measured; label estimates and unknowns explicitly.
6. Never imply a control is enforced, an issue is resolved, a file is pushed, or a deployment is live unless evidence confirms it.
7. If verification fails or results conflict, state the failure and the next discriminating step. Do not hide failed checks behind a success summary.
8. Record decisions, tests, and evidence through DDD's canonical mechanisms when applicable.
9. State whether the outcome changes the intended real-world decision, behavior, observation, or capability; if that effect has not been observed, label it as a hypothesis rather than a demonstrated benefit.
10. When relevant, report what the work revealed about the original assumptions and whether the governing principle or success criterion should be reconsidered.

## Completion check

A reader can independently understand what changed, what evidence supports the result, what was not checked, and what should happen next.

## Related contracts

- [Harness workflow](../docs/harness-workflow.md)
- [DDD documentation](https://github.com/bonsai/DDD/tree/main/docs)
