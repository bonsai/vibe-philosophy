# Vibe AI Harness Workflow

This document operationalizes the repository's philosophy. `AGENTS.md` remains the governing contract; this file explains the working cycle.

## 1. Intake: understand before acting

Capture the request, intended beneficiary, current situation, constraints, and expected outcome. Preserve the user's vocabulary, but resolve ambiguity where it affects implementation.

Questions:
- What is painful, blocked, or newly possible?
- Who experiences it, and in what context?
- What would count as a meaningful improvement?
- What must not change?

If no concrete pain or opportunity can be identified, do not manufacture one. Record the uncertainty or ask a focused question.

## 2. Discovery: challenge the need to build

Before proposing implementation:
- Search the current repository and known ecosystem for an existing solution.
- Distinguish a missing capability from a discoverability, configuration, or workflow problem.
- Estimate marginal value, cost, maintenance burden, and reversibility.
- Identify what evidence would disprove the idea.

Use this decision set:

- **Already exists:** reuse, connect, document, or improve discovery.
- **Low marginal value:** do not build; explain why.
- **Pain uncertain:** interview, observe, prototype, or test the hypothesis.
- **Value plausible:** define a small acceptance test.
- **Value demonstrated:** implement the smallest useful slice.

## 3. Declaration and blueprint

Keep the two artifacts separate.

### Declaration
A declaration states what must remain true across tasks: safety boundaries, interfaces, data ownership, compatibility, and project-specific invariants.

### Blueprint
A blueprint states the desired outcome: user scenario, observable behavior, acceptance criteria, and known trade-offs. It can evolve when evidence changes.

Do not hide task instructions inside permanent policy. Do not treat an aspirational blueprint as a guarantee.

## 4. Task and execution

Break work into bounded, reviewable changes. Each task should specify:
- outcome
- scope and exclusions
- dependencies
- acceptance criteria
- verification method

Inspect the existing implementation before editing. Prefer reuse and small diffs. Seek approval before destructive, externally visible, costly, or production-impacting actions.

## 5. Verification and evidence

Report only checks actually performed. Keep these categories separate:
- **Observation:** directly seen output or behavior
- **Interpretation:** meaning inferred from observations
- **Hypothesis:** plausible explanation not yet established
- **Decision:** chosen action and its rationale
- **Unknown:** information still missing

A successful edit is not proof of a successful runtime. A passing test is evidence only for the behavior it covers.

## 6. Reflection and learning

After execution, compare acceptance criteria with observed outcomes. For failures, record:
- expected result
- actual result
- evidence and reproduction steps
- candidate causes with confidence
- next discriminating test

Only promote a lesson into a reusable skill after checking whether it generalizes and whether counterexamples exist. Keep raw observations and curated skills distinct so that a one-off event does not become a universal rule.

## 7. Governed self-modification

The agent may propose edits to skills, workflow documents, and even `AGENTS.md`, but must not silently apply changes to governing policy.

For policy changes:
1. State the observed problem and supporting evidence.
2. Propose the exact rule change and its scope.
3. Identify compatibility and safety implications.
4. Obtain explicit human authorization.
5. Make a reviewable diff and record the rationale.

## 8. Completion report

For non-trivial tasks, return:
- requested intent
- changed files and behavior
- evidence and checks run
- unverified claims and remaining risks
- the next smallest useful action

Do not claim a push, deployment, integration, or test result unless it actually happened.
