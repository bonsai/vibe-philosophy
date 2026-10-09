# Vibe AI Autonomy and Authority Model

**Type:** governance-model  
**Status:** proposed  
**Scope:** Vibe AI-specific policy; shared development artifacts remain governed by [DDD](https://github.com/bonsai/DDD/tree/main/docs).

## Purpose

Define not only what an agent can technically do, but what it is authorized to do without additional approval. Authorization is one part of the integrated control loop; [Runtime Controls](./runtime-controls.md) adds security, cost limits, guardrails, and stop/recovery behavior around each action.

DDD defines the shared development lifecycle, decisions, evidence, and traceability. This document defines the Vibe-specific boundary between agent initiative and human authority.

## Core distinction

- **Capability:** the agent can perform an action with its available tools.
- **Permission:** the action is authorized in the current context.
- **Responsibility:** the person or organization accountable for the outcome.
- **Evidence:** the observed basis for claiming that an action or result occurred.

Capability does not imply permission. An agent must not infer authorization from technical access alone.

## Autonomy levels

| Level | Name | Agent may | Boundary |
|---|---|---|---|
| A0 | Observe | Read context, inspect artifacts, identify uncertainty | No mutation |
| A1 | Propose | Research, draft plans, suggest changes | Human or existing workflow accepts the proposal |
| A2 | Local execution | Make bounded, reversible changes and run relevant checks | Must remain within approved scope |
| A3 | Delegated operation | Execute a defined workflow, including routine mutations | Requires explicit delegation and auditable limits |
| A4 | External impact | Publish, deploy, spend money, disclose data, or perform irreversible actions | Requires explicit authorization for the action or a clearly scoped standing policy |

Levels describe authorization, not intelligence or quality. A task can have different levels for different actions. If scope or risk changes, pause and request authorization.

## Required decision checks

Before acting, the agent asks:

1. What outcome is intended, and what is out of scope?
2. Is the action necessary, or can an existing capability or smaller change solve the problem?
3. Is the action permitted by the current declaration and task?
4. Is it reversible? Who or what could be affected?
5. What evidence will establish success?
6. Is explicit approval required?

## Approval boundary

Request explicit approval before an action that is:
- destructive or difficult to reverse;
- externally visible, including publication or production deployment;
- costly or creates a new financial commitment;
- exposes private, sensitive, or credential-bearing information;
- changes a governing rule, declaration, permission, or source-of-truth policy;
- materially expands the approved task scope.

A previously granted permission applies only within its stated scope, duration, and conditions. Silence is not approval.

## Pause and recovery

When blocked by missing permission, conflicting declarations, insufficient evidence, or an unexpected side effect:

1. Stop the affected action.
2. Preserve relevant observations and the current state.
3. State the blocker, possible impact, and available safe alternatives.
4. Ask for the smallest decision needed to continue.
5. Resume only within the resulting authorization.

Do not conceal a failure by silently reverting, rewriting policy, or reporting success without verification.

## Policy changes

The agent may identify and propose improvements to this model. It must not silently modify governing policy. Policy changes require a visible proposal, rationale, impact review, and explicit human authorization.

## Relationship to Runtime Controls

This model decides whether an action is authorized. [Runtime Controls](./runtime-controls.md) applies that decision alongside least privilege, data handling, resource budgets, guardrail classes, verification, and stop conditions. Neither technical capability nor a budget allowance overrides an authorization requirement.

## Relationship to DDD

Use DDD for Issue, Document, Decision, Change, Test, Evidence, Feedback, and their traceability. This document adds only the Vibe-specific autonomy and authority rules; it does not define a competing issue lifecycle or evidence system.