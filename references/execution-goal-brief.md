# Execution goal brief

Read this reference only after the Design Handoff and implementation plan are
approved and the human has explicitly authorized implementation.

## Purpose

Turn the approved phase into one bounded brief for `实施任务X`. The brief may be
used as a `/goal` prompt when Goal mode is available, or as the implementation
task's opening prompt. It is an execution contract, not a new design decision.

## Prepare facts first

Before writing the brief, inspect the repository and verify only the facts that
will constrain work:

- applicable `AGENTS.md` files and the approved Design Handoff;
- linked implementation plan and exact file/module ownership;
- current Git state and relevant existing behavior;
- real validation commands and their baseline result, if safe to run.

If a required fact or command cannot be verified, say so in the brief and make
it the first preflight check. Do not invent commands, baselines, or file paths.

## Required brief shape

```text
You are 实施任务<X>, the primary implementation owner for <approved phase>.

Read: <AGENTS.md paths>, <approved handoff>, <linked plan>, and
<other authoritative project documents>.

Goal and completion: <approved outcome and measurable acceptance criteria>.

Owned scope: <allowed files/modules/contracts>. Do not modify: <frozen or
out-of-scope areas>. Integration responsibility remains with this task.

Preflight: <verified commands and expected baseline>, or <the exact first check
when a command or fact is unverified>. If preflight materially disagrees with
the handoff, stop implementation and return a concise Status Update with
evidence.

Required work: <ordered, bounded implementation steps>.

Validation: <commands, manual checks, and evidence required>. Do not delete,
skip, weaken, or exclude tests/checks to claim success. Do not claim a command
passed unless it was actually run in this task.

Safety and authority: <approval, external-action, data, dependency, and
runtime-default boundaries from the handoff and AGENTS.md>.

Stop conditions: <approval gate, unverified prerequisite, scope conflict, or
project-defined repair limit>. Report blockers factually; do not broaden scope.

Return: a factual implementation handoff with changed files, validation
evidence, unmet acceptance criteria, residual risks, and the exact next
decision required.
```

## Keep it compatible with this workflow

- The approved Design Handoff remains the phase authority; the brief only makes
  it executable.
- Do not create a generic root `PROGRESS.md` or `BLOCKED.md`. Use the required
  Status Update and Design Handoff; create a project-specific blocker record
  only when the project's `AGENTS.md` requires it.
- The implementation task may delegate only within the task-topology rules in
  the main Skill. It remains responsible for integration and evidence.
- A completed implementation brief does not approve release readiness or
  replace the coordinator's decision to start a read-only review.
