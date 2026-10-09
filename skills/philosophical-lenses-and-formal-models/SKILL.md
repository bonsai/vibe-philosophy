---
name: philosophical-lenses-and-formal-models
description: Use Socratic questioning, Platonic conceptual models, Aristotelian classification, civic inclusion/exclusion analysis, set diagrams, and group-theoretic symmetry to clarify concepts without collapsing historical differences.
---

# Philosophical Lenses and Formal Models

## Purpose

Help an agent investigate concepts and institutions without pretending that a fluent interpretation is established truth. Combine three distinct philosophical methods with explicit set-theoretic and algebraic models. Keep historical claims, interpretive hypotheses, formal consequences, and present-day normative judgments separate.

## Core rule

**Use philosophers as different inquiry methods, not as interchangeable authorities.** Never infer that a formal model proves a historical interpretation or that an ancient classification justifies a modern policy.

## 1. Three philosophical lenses

### Socrates — expose assumptions through questions

Use elenchus-style questioning to test definitions and claims.

Ask:
- What exactly does this term mean here?
- Is the definition consistent across examples?
- What counterexample would defeat it?
- Does the answer rely on an assumption that has not been defended?
- Has the question already smuggled in the desired conclusion?

Output:
- claim under examination;
- working definition;
- assumptions surfaced;
- counterexample or contradiction;
- unresolved question.

Do not present every Socratic dialogue as a transcript of the historical Socrates' exact views. The dialogues are literary and philosophical sources whose authorship, dramatic framing, and interpretation matter.

### Plato — examine models, ideals, and political order

Use Platonic inquiry to ask what a concept is meant to be, how an ideal model differs from actual cases, and how education, knowledge, and political structure shape the proposed order.

For political analysis, distinguish:
- an ideal or theoretical city;
- the roles assigned within that model;
- actual historical institutions;
- the author's argument about justice and rule.

In the *Republic*, the city is organized through roles commonly described as rulers/guardians, auxiliaries, and producers. Do not treat these roles as a direct equivalent of the historical legal categories “citizen” and “slave.” They answer different classificatory questions.

Output:
- ideal/model being proposed;
- parts and roles;
- relation between knowledge, authority, and rule;
- gap between model and historical reality;
- objections and alternative interpretations.

### Aristotle — define categories, causes, and practical distinctions

Use Aristotelian methods to define terms, distinguish kinds, inspect causes and purposes, and ask how a category operates in practice.

Questions:
- What are the defining conditions for membership?
- Which distinctions are essential and which are contingent?
- What purpose is the institution said to serve?
- Does the stated purpose match its observed operation?
- Which exceptions expose a weak definition?

In the *Politics*, Aristotle discusses citizenship through participation in deliberative or judicial functions, with qualifications depending on the constitution; he also defends a theory of “natural slavery.” These positions belong to their historical and argumentative context. Explain them critically rather than endorsing them, and do not project a single timeless definition of citizenship onto all Greek poleis.

Output:
- terms and definitions;
- classification criteria;
- causes, functions, and purposes;
- exceptions and disputed cases;
- distinction between descriptive analysis and normative endorsement.

## 2. Citizen and slave: analyze the boundary

Treat “citizen” and “slave” as historically situated legal, social, and political categories—not universal natural kinds.

For any case, specify:
1. **Place and period:** which polity and date?
2. **Source:** which primary text, law, inscription, or modern scholarship supports the claim?
3. **Dimension:** legal status, political participation, freedom of movement, property, labor, kinship, or social recognition?
4. **Authority:** who assigns, records, or enforces the category?
5. **Exceptions:** freed people, resident foreigners, women, children, conquered populations, or other groups may occupy distinct positions.
6. **Normative question:** is the task describing a historical system, interpreting its justification, or evaluating it ethically today?

Never collapse “not a citizen” into “slave.” These categories are not exhaustive complements in every society. A person may be free but lack citizenship; legal and social statuses may overlap in complex ways.

When using Plato or Aristotle, state whose argument is being reconstructed and separate it from the agent's evaluation.

## 3. Venn diagrams and set theory

Use sets to make definitions and overlaps visible.

Let the universe U be the explicitly defined population under study. Define:
- C = people classified as citizens under the selected legal/historical definition;
- S = people classified as enslaved under the selected legal/historical definition;
- F = people classified as free under that definition;
- P = people permitted to participate in a specified political function.

Do not assume in advance that C and S partition U, or that F is exactly the complement of S, until the chosen source and definitions establish that. In a particular model, test:
- intersection: C ∩ S;
- exclusion: C ∩ S = ∅, if justified by the rules of that specific system;
- coverage: C ∪ S = U, only if the categories really are exhaustive;
- political participation: P ⊆ C, if the legal rules and definition support it;
- exceptions and uncertain membership.

An empty intersection or subset relation is a claim to establish from definitions and evidence, not a fact to insert merely to make the diagram tidy.

### Required diagram annotation

Every diagram must identify:
- the universe U;
- the definition of each set;
- the source and period;
- whether boundaries are documented, inferred, disputed, or hypothetical;
- individuals/cases that remain unclassified.

A Venn diagram illustrates set relations. It does not, by itself, explain causation, power, legitimacy, or why a boundary was created.

## 4. Group theory: investigate transformations and symmetry

Use group theory only when a meaningful set of transformations has been defined.

A group G consists of a set of transformations with an associative operation, an identity, and inverses. For a model of categories or a diagram, ask:
- What objects are transformed?
- What transformations are allowed?
- What must each transformation preserve?
- Is composition closed, and does each transformation have an inverse?
- Which properties remain invariant?

Possible exploratory uses:
- relabeling equivalent elements without changing the structure;
- permutations of a finite set of cases;
- symmetries of a diagram or classification;
- transformations that preserve a specified relation.

Do **not** assume that historical status changes form a group. Enslavement, emancipation, citizenship acquisition, and disenfranchisement are often directed, constrained, and non-reversible processes. They may be better modeled as a state-transition system, directed graph, monoid, category, or relation rather than a group.

A symmetry in a mathematical model does not imply equality, justice, or symmetry in the real institution. State exactly what the transformation preserves.

## 5. Logic, contraposition, and Lean

Turn informal claims into explicit propositions before attempting proof.

Example schema:
- P: every member of set A satisfies condition R;
- Q: a particular object x belongs to A and therefore satisfies R.

If P → Q is established, its contrapositive is ¬Q → ¬P in classical logic. More precisely, from P → Q one can derive ¬Q → ¬P constructively; the reverse equivalence generally needs classical reasoning.

Use Lean to verify the logical consequence of formal definitions and premises. Do not confuse:
- writing a proposition with proving it;
- proving a theorem from premises with validating the premises against historical evidence;
- proving a set relation in a model with proving that the model faithfully represents reality.

Minimal Lean example:

```lean
theorem contraposition {P Q : Prop}
    (h : P → Q) : ¬ Q → ¬ P := by
  intro hnq hp
  exact hnq (h hp)
```

For a historical claim, the hard work may be establishing and justifying the premises, not proving the formal implication.

## 6. Suggested agent workflow

1. **Scope:** identify the exact question, polity, period, source base, and intended use.
2. **Socratic pass:** challenge definitions and expose assumptions.
3. **Platonic pass:** identify the ideal model, roles, and theory of order; distinguish it from historical reality.
4. **Aristotelian pass:** classify terms, criteria, causes, purposes, and exceptions.
5. **Boundary pass:** analyze citizen/slave/free/participant categories without forcing them into a false binary.
6. **Set pass:** define U and each set; draw or describe overlaps only after stating membership criteria.
7. **Symmetry pass:** propose transformations and invariants; reject group theory if reversibility or closure fails.
8. **Formalization pass:** write propositions, assumptions, and counterexamples; use Lean only for claims expressible in its logic.
9. **Evidence pass:** check historical sources and mark fact, interpretation, hypothesis, and unknown separately.
10. **Review:** ask what the model omits, whose perspective is absent, and what evidence would change the conclusion.

## 7. Output contract

For a substantive analysis, report:
- **Question and scope**
- **Definitions and source context**
- **Socratic challenges**
- **Platonic model**
- **Aristotelian classification**
- **Set relations / Venn model**
- **Group or transformation model** (or explain why group theory does not fit)
- **Formal propositions and proof status**
- **Historical evidence and uncertainty**
- **Counterexamples, excluded perspectives, and next test**

## 8. Safety against false certainty

- Do not fabricate historical sources or quotations.
- Do not present contested interpretations as settled fact.
- Do not use mathematical notation to disguise unsupported assumptions.
- Do not infer that a category is exhaustive merely because a diagram contains two circles.
- Do not infer a group's existence from a set of transformations until group axioms are checked.
- Do not infer moral legitimacy from historical existence or formal consistency.
- Explicitly mark what is known, unknown, unexamined, prohibited, not done, impossible under current conditions, or beyond the current reasoning model.

## Guiding principle

**Question the definition; distinguish the ideal from the historical; test the classification; define the transformation; prove only what follows from stated premises; and leave unsupported conclusions visibly unresolved.**
