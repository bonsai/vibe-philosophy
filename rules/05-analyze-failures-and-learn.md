# Rule 05 — Turn Failures into Evidence-Based Learning

**Type:** agent instruction  
**Priority:** mandatory when a failure or unexpected result occurs

## Rules

1. Describe the expected result, actual result, context, and reproducible evidence before proposing a fix.
2. Distinguish direct observations from interpretations, hypotheses, decisions, and unknowns.
3. Investigate root causes rather than only suppressing symptoms. State confidence and plausible alternatives.
4. Search available history and canonical DDD evidence for related failures before repeating an approach.
5. Bound retries. If an approach fails repeatedly, change the hypothesis or stop; do not repeat it indefinitely.
6. Propose the smallest discriminating test that can distinguish likely causes.
7. Do not turn one incident into a universal rule without evidence of generality and consideration of counterexamples.
8. Promote lessons into reusable skills only through the review process in [Skill Learning](../docs/skill-learning.md).
9. Never silently modify governing policy, increase autonomy, widen permissions, or raise budgets as a result of a failure or success.
10. Record findings using existing DDD evidence and decision mechanisms instead of inventing a parallel source of truth.
11. Turn failure into learning by locating which assumption, hypothesis, execution step, observation, or evaluation criterion failed; preserve the lesson in a reusable form only when supported by evidence.
12. Revisit success criteria when repeated real-world results suggest the metric itself is incomplete or misaligned, rather than optimizing a proxy without question.

## Completion check

A failure report identifies evidence, likely cause and confidence, the next test or fix, and whether any reusable lesson is justified.

## Related contracts

- [Skill learning](../docs/skill-learning.md)
- [Harness workflow](../docs/harness-workflow.md)
