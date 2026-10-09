---
name: lean-and-logical-proof
description: Translate claims into explicit propositions, distinguish premises from conclusions, use contraposition carefully, and verify formal consequences with Lean.
---

# Lean and Logical Proof

## Purpose
Use formal logic and Lean to check what follows from stated premises, without mistaking formal validity for empirical truth.

## Procedure
1. Translate the informal claim into a precise proposition.
2. Define every term and type needed to express it.
3. Separate premises, definitions, assumptions, and conclusion.
4. Attempt a proof or find a counterexample.
5. Use Lean to check the proof against the formal statement.
6. Independently examine whether the premises are supported by evidence.
7. Report proof status and model limitations.

## Contraposition
From P → Q, one can derive ¬Q → ¬P constructively. The reverse direction generally requires classical reasoning.

Lean example:
```lean
theorem contraposition {P Q : Prop}
    (h : P → Q) : ¬ Q → ¬ P := by
  intro hnq hp
  exact hnq (h hp)
```

## Distinctions that must remain explicit
- Writing a proposition is not proving it.
- A proof from premises does not validate the premises against reality.
- A proof about a formal model does not establish that the model faithfully represents the world.
- A theorem checker validates the formal proof and statement, not the source quality of historical or empirical claims.

## Output
- Formal statement
- Definitions and premises
- Proof or counterexample
- Lean verification status
- Evidence for premises
- Limits and unresolved assumptions

## Verification
Report whether the Lean proof was actually run. If it was not run, label the code as an unverified example rather than claiming successful compilation.
