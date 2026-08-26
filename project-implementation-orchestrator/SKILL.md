---
name: project-implementation-orchestrator
description: Orchestrate multiple subagents to implement an already-approved, bounded plan. Use only when the user explicitly invokes this skill and the objective, scope, acceptance criteria, and implementation direction are settled; coordinate execution packages, file ownership, integration, verification, and delivery without redesigning the project.
---

# Project Implementation Orchestrator

Implement the agreed plan. Do not perform requirements analysis, solution design, or implementation planning.

## Entry gate

Before delegating, confirm that the request states or links to all of the following:

- the objective and in-scope modules;
- the intended implementation direction;
- acceptance criteria and required checks; and
- constraints that affect ownership, compatibility, or release.

If any item is materially unclear, explain the gap and ask the user for a decision. Do not invent a plan, create a design handoff, require a phase number, or begin implementation on an assumed design.

## Main agent responsibilities

Act as the sole integrator. Retain responsibility for:

- decomposing the approved work into executable packages;
- assigning and enforcing file ownership;
- dynamically dispatching subagents and resolving conflicts;
- inspecting real changes, applying integration changes, and controlling Git actions;
- running incremental and final validation; and
- reporting the delivered result, checks run, and unresolved exceptions.

Do not mechanically assign one agent to each checklist item. Form a package around a coherent module boundary, a dependency slice, or a set of files with one safe owner. Keep tightly coupled changes together; split only work that can proceed independently without competing edits.

## Package and ownership rules

For every active package, record internally:

- purpose, acceptance criteria, dependencies, and verification command;
- owned paths, plus read-only paths it may inspect;
- the implementing agent; and
- integration or review status.

Give one active agent exclusive write ownership of each file. Treat shared configuration, generated files, lockfiles, migrations, formatting sweeps, and Git metadata as main-agent-owned unless explicitly assigned. Do not assign overlapping ownership. If a package must change another package's file, route that change through the file owner or the main agent.

Work in the shared workspace. Inspect the current diff before assigning work and again when an agent finishes. Do not overwrite, discard, reset, stash, or revert changes merely because they were not expected. First identify their owner and intent. After a failed, timed-out, or interrupted task, preserve its changes until the main agent has inspected and either integrated, reassigned, or deliberately reverted only the confirmed residual edits.

## Dynamic scheduling

Maintain a ready queue of packages whose dependencies are satisfied. At each scheduling point, calculate:

```text
dispatch_now = min(R, C, O)
```

Where:

- `R` is the number of ready packages that are useful to delegate now;
- `C` is the number of available subagent slots; and
- `O` is the number of ready packages with independent, conflict-free ownership.

Dispatch that many packages. Recalculate after any agent completes, blocks, fails, or releases ownership. Use rolling dispatch: hand the next ready package to a newly available agent immediately instead of waiting for the whole current batch.

When a module needs follow-up work, reuse its original implementer when that preserves context and does not delay more valuable ready work. Assign an independent reviewer only to an agent that did not implement the reviewed module.

## Coordination rules

Tell each subagent exactly which paths it owns, which paths are read-only, its completion criteria, and the required focused checks. Require it to report changed files, commands run, results, and remaining risks.

Use the repository's established formatter, linter, test runner, and generation commands. Do not run a broad formatter across files owned by other agents. Do not create commits, switch branches, rebase, merge, push, force-push, or alter Git history unless the user explicitly requests that Git operation. If commits are requested, the main agent creates them only after integration validation.

## Design exceptions

Treat a design flaw discovered during implementation as one of these exceptions:

1. **Local clarification** — a choice stays within the approved scope, preserves public contracts, and does not change acceptance criteria. Resolve it using repository conventions and record the decision in the final report.
2. **Scoped plan gap** — a missing decision changes a module boundary, contract, test expectation, or nontrivial behavior, but is isolated. Pause only affected packages, state the impact and options, and wait for the user's decision before changing direction.
3. **Fundamental conflict** — the approved design cannot meet its acceptance criteria, security requirements, data constraints, or compatibility commitments. Stop all dependent packages, preserve completed evidence, and request a revised plan from the user.

Never disguise a category 2 or 3 exception as an implementation detail. Do not use a new design as a reason to continue without approval.

## Retries and recovery

Retry only when new evidence justifies a changed attempt: a new error message, failing test, repository convention, narrowed reproduction, dependency result, or user decision. State the evidence and what changes in the next attempt. Do not repeat the same approach after the same failure without new evidence.

If an agent cannot proceed, release or narrow its ownership before assigning replacement work. Prefer a focused repair package over restarting unrelated work.

## Verification and delivery

After each package, inspect its actual diff and run the package's focused verification before integration. Resolve ownership conflicts and formatting issues before starting dependent packages.

Before delivery, the main agent must:

1. inspect the combined diff for scope, unintended changes, and cross-module conflicts;
2. run the required incremental checks that have not already been invalidated by later changes;
3. run the final joint validation required by the acceptance criteria; and
4. report changed areas, validation results, exceptions, and any work intentionally left pending.

Do not claim completion from subagent reports alone. Completion requires the main agent's integrated diff review and final validation.
