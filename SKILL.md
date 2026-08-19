---
name: project-phase-orchestrator
description: Use when starting or coordinating a medium or large software project that needs phased design, implementation, review, human approval, and durable handoffs.
---

# Project Phase Orchestrator

Coordinate a project as small, evidence-backed phases. The human owns approval;
the coordinator owns the workflow; an implementation task is the sole writer;
review is separate and read-only.

## Before creating tasks

1. Read the global and project `AGENTS.md` files and project documentation.
   They override this Skill's defaults, including model choices, safety rules,
   validation commands, and review-round limits.
2. Identify the current logical phase and its boundary. Do not turn a broad
   project goal into an unbounded implementation run.
3. Start with a Design Handoff in `Draft` status. Record assumptions separately
   from confirmed decisions.
4. Attach the implementation plan to the Design Handoff: embed it there or link
   a stable plan file from it. Avoid a plan that exists only in chat history.

Use [the templates](references/templates.md) for the handoff and role briefs.

## Execution goal brief

After the handoff and plan are approved and the human explicitly authorizes
implementation, prepare an execution goal brief before creating `实施任务X`.
First verify the relevant repository state, editable-file ownership, baseline
validation commands, and any facts the brief will claim. Use
[the execution-goal-brief reference](references/execution-goal-brief.md).

The brief makes one approved implementation phase independently executable. It
does not replace `AGENTS.md`, the approved Design Handoff, human approval
gates, or the separate read-only review. It must not create parallel writers
unless the project rules explicitly permit non-overlapping ownership.

## Project state snapshot

At a terminal handoff, before a planned task or coordinator change, or when
context is no longer reliable, update the project-root `DEV_STATE.md` from
verified code, Git state, the current handoff, and actual validation evidence.
Use [the dev-state reference](references/dev-state.md).

`DEV_STATE.md` is a concise current snapshot for resuming work. It does not
replace the Design Handoff, implementation plan, project specification, or
source code as the authority for scope and evidence. On re-entry, read it with
the applicable `AGENTS.md` files and current phase handoff, then verify any
claim that matters to the next action.

## Project-level specification

When project intake and requirements are produced by other Skills, create one
`docs/PROJECT_DEVELOPMENT_SPEC.md` before the first coordinated phase. It is
the stable project-level companion to phase-specific Design Handoffs and SDDs;
link to the intake and approved requirements instead of copying them.

Use the Project Development Specification template to separate:

- **short-term objective** — the current deliverable and measurable acceptance;
- **long-term direction** — a non-binding future form, scale, or integration;
- **future-compatibility constraints** — only the reversible seams, contracts,
  and data choices worth preserving now.

Do not implement future features merely because they are documented as a
long-term direction. Revisit them only when their explicit promotion trigger is
met and the human approves a new phase. Record project milestones as time
windows, effort ranges, dependencies, and replanning triggers—not delivery
guarantees. Keep project-wide safety and runtime constraints in `AGENTS.md`.

## Default lifecycle

```text
Coordinator / design stage
  -> Design Handoff (Draft)
  -> human approves handoff and implementation plan
  -> human explicitly authorizes implementation
  -> one implementation task (sole writer)
  -> required validation
  -> proportionate, read-only review
  -> bounded fix-and-review loop
  -> terminal handoff / human decision
```

Approval is a human gate, not an `审批任务` or child agent. Never treat tests,
synthetic evaluation, a prior approval, or a completed design as authorization
for a different runtime default, external action, deployment, retention change,
or scope expansion.

## Communication checkpoints

Use the coordinator as the communication hub. A child reports to its parent;
implementation and review tasks do not negotiate scope or exchange unstructured
messages directly.

Use a concise Stage Status Update only at a state change: phase start, a
material decision, a blocker, new risk, validation result, ready-for-review, or
terminal handoff. Do not maintain a chronological work diary or report every
command. Write the same fact into the Design Handoff only when it changes
scope, approval needs, acceptance evidence, a material risk, or the phase
status.

When a read-only review finds actionable issues, the coordinator sends one
Review Rework Request to the original implementation task. It states the
finding, the bounded requested change, verification required, and prohibited
scope expansion. The implementation task replies with a Status Update and then
its factual handoff; it does not argue the finding away without evidence.

Use [the status and rework templates](references/templates.md#coordination-messages)
for these messages.

## Task topology

- Normally, `方案` is the first stage of `协调任务X`, not a separate conversation.
  Create `方案任务X` only when the human requests a discussion-only task; it must
  finish with a handoff and must not create, coordinate, or review implementation.
- Reuse one active coordinator conversation for consecutive small phases only
  when the prior phase has a terminal handoff, no implementation/review child is
  active, the project boundary is unchanged, and context remains reliable.
- Start a new coordinator conversation for independently long-running work,
  material architecture or authority changes, unreliable context, a new owner,
  or when the human asks for separation.
- When a new coordinator conversation is indicated, the outgoing coordinator
  automatically prepares or updates the transition Design Handoff. It must not
  create or switch to a new top-level coordinator conversation without explicit
  human confirmation. Request that confirmation with the reason, proposed
  `协调任务X` name, handoff path, and next-phase boundary. After confirmation,
  the incoming coordinator must read the handoff before it begins planning.
- After all three gates are satisfied, create exactly one project-scoped
  `实施任务X` child for the phase. It owns implementation, integration, tests,
  and its factual completion handoff.
- Create `审查任务X` only after required validation, when the risk or project
  rules warrant it. It is a separate, strictly read-only child conversation.
- Do not create a writer per plan item. Further delegation is only for
  independent read-only investigation or explicitly non-overlapping ownership;
  the implementation task remains accountable for integration.

Use `协调任务X`, `实施任务X`, and `审查任务X` as visible names, with a monotonically
increasing phase number. If task APIs need ASCII IDs, map them predictably to
`coordinator_x`, `implementation_x`, and `review_x`.

## Handoff discipline

Every phase handoff should make the next task independent of compacted chat
history. It must state: goal and scope; decisions and assumptions; acceptance
criteria; linked implementation plan; validation commands and evidence; changed
files or a statement that no files changed; remaining risks; current status; and
the exact human decision required next.

The implementation task returns factual changes and fresh validation evidence.
The coordinator verifies that evidence against the approved acceptance criteria,
records residual risk and approval boundaries, then reports one consolidated
status to the human.

## Coordinator operating rules

- Do planning, sequencing, monitoring, and handoff consolidation in the
  coordinator; do not implement or review inline if child tasks are required.
- Give each child a bounded scope, file/area ownership, acceptance criteria,
  safety constraints, validation commands, and handoff destination.
- Do not start a reviewer while the writer is still making changes.
- Return review findings to the original implementation task for a bounded
  repair loop. Follow any project-defined limit; if none exists, propose a
  limit and obtain human confirmation before exceeding it.
- Stop at an approval gate instead of guessing. Report the specific decision,
  evidence, trade-off, and consequence of each option.

## Completion report

Report: phase and status; acceptance criteria result; modified files; commands
and results freshly run; review findings and repair-round count; remaining
risks; and the next human decision. Distinguish confirmed evidence from
assumptions and from work not freshly verified.
