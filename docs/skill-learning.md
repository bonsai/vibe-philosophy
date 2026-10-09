# Vibe AI Skill Learning

**Type:** learning-model  
**Status:** proposed  
**Scope:** Vibe-specific model for turning experience into reusable capability.

## Purpose

Define how Vibe AI can improve its working methods without turning a single error, unverified assumption, or model-generated claim into permanent policy.

DDD already provides the shared concepts for Issues, Documents, Decisions, Tests, Evidence, and Feedback. This document defines the additional meaning and promotion rules for a **Skill**.

## Definitions

- **Observation:** what was directly seen during an action or test.
- **Failure case:** an expected outcome, actual outcome, and supporting evidence.
- **Hypothesis:** a proposed explanation or improvement that is not yet established.
- **Candidate skill:** a reusable procedure or constraint proposed from experience.
- **Validated skill:** a candidate that has passed stated checks in relevant contexts.
- **Retired skill:** a skill that is superseded, no longer applicable, or shown to be harmful.

A skill is a reusable method with an applicability boundary and a verification method. It is not merely a confidence score or a list of instructions.

## Learning loop

Attempt → Observation → Failure/Success Analysis → Hypothesis → Candidate Skill → Validation → Adoption → Monitoring

1. Capture the task context, intended outcome, actual result, and evidence.
2. Compare the outcome with the acceptance criteria.
3. Separate the observed failure from the hypothesized cause.
4. Propose the smallest reusable change: a checklist, procedure, test, constraint, or tool improvement.
5. Define where the skill applies, where it does not apply, and how to test it.
6. Validate against relevant cases, including counterexamples when practical.
7. Adopt it only after the required review and authorization.
8. Monitor subsequent use and revise or retire it when evidence changes.

## Promotion criteria

A candidate may be promoted when:
- the problem and evidence are documented;
- its proposed cause is distinguished from observed facts;
- the scope and preconditions are explicit;
- a verification method exists;
- relevant counterexamples or regressions have been considered;
- adoption does not conflict with higher-priority declarations or safety constraints;
- any required human approval has been obtained.

One failure may justify a narrow defensive check, but it does not automatically justify a universal rule. Repeated patterns strengthen a hypothesis; they do not remove the need to validate it.

## Skill record

A skill record should contain, at minimum:

- **ID and title**
- **Status:** candidate, validated, deprecated, or retired
- **Purpose:** the problem it addresses
- **Applicability:** preconditions and context
- **Procedure or constraint**
- **Evidence:** related Issues, tests, observations, and outcomes
- **Verification:** how to determine whether it worked
- **Limitations:** known exceptions and counterexamples
- **Provenance:** when and why it was introduced or changed
- **Review condition:** what evidence should trigger reconsideration

Use existing DDD Documents, Issues, Decisions, and Evidence as canonical records and link to them. Do not create a second evidence database just for skills.

## Skill versus policy

A skill describes a reusable way to perform or evaluate work. A governing policy declares what must or must not happen.

- A candidate skill can be explored without changing policy.
- A validated skill can be adopted within an existing authorization.
- A skill that changes permissions, invariants, security boundaries, or other governing rules must go through the policy-change process in [autonomy-model.md](autonomy-model.md).
- The agent must never silently edit AGENTS.md or other governing contracts because a new skill appears useful.

## Evaluation

Assess a skill by observable outcomes, not self-reported confidence alone:

- success rate on relevant cases;
- recurrence of the target failure;
- regressions or unintended side effects;
- time and effort saved, where measurable;
- applicability limits and exceptions;
- quality of supporting evidence.

Do not claim that a failure will “never happen again.” State which failure mode was addressed and what verification supports the claim.

## Relationship to DDD

Use DDD's existing lifecycle and source-of-truth rules for recording observations, decisions, changes, tests, and evidence. This document defines only the Vibe-specific promotion process from experience to reusable skill.