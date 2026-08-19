# Project phase orchestration templates

Adapt these templates to the repository's rules. Keep security/runtime controls
in the project's `AGENTS.md`; do not copy them blindly into every handoff.

## Coordination messages

Use these as task-to-task messages. They are not a chronological work log.

### Stage Status Update

```markdown
## Status Update — <phase> / <task>

- State: Planning | Implementing | Blocked | Ready for review | Complete
- Decision now: <what the coordinator can decide from this update>
- Completed since last update:
- Evidence: <test / command / document / observed result>
- Risk or blocker:
- Needed from coordinator or human: <or "None">
- Next update trigger: <specific event, not a time-based promise>
- Persist in Design Handoff: Yes / No — <what must be recorded, if anything>
```

Send only when a decision, risk, evidence, or state changes. For routine work,
remain silent. If the update changes phase status, scope, approval needs,
acceptance evidence, or a material risk, update the Design Handoff as well.

### Review Rework Request

```markdown
## Review Rework Request — <phase> / round <N>

- Finding: <short, evidence-backed problem>
- Impact: <acceptance, safety, regression, or maintainability impact>
- Requested change: <bounded change>
- Must not change: <scope / files / behavior that remain out of scope>
- Verification required: <tests or checks>
- Return format: Status Update, then updated implementation handoff
```

The coordinator sends this to the original implementation task. The reviewer
remains read-only; it does not fix the issue itself.

## Project Development Specification

Create this once near project start at `docs/PROJECT_DEVELOPMENT_SPEC.md`.
Update it only for durable project decisions; use Design Handoffs for
phase-specific facts and plans.

```markdown
# Project Development Specification — <project name>

Status: Draft | Approved | Superseded
Owner: <human / coordinator>
Links: <project intake>, <approved requirements>, <architecture overview>

## Project context
- Problem and target users:
- Constraints and assumptions:
- Project-wide non-goals:

## Goals

### Short-term objective — current deliverable
- What must be demonstrably delivered now:
- Measurable success and acceptance criteria:
- Explicitly excluded from the current delivery:

### Long-term direction — non-binding
- Desired future form, scale, integrations, or operating model:
- Known uncertainties:
- This direction does not authorize current scope:

### Future-compatibility constraints
- Reversible decisions / extension seams to preserve now:
- Contract, data, migration, or dependency choices to avoid locking in:
- Explicit deferrals (future work not to build now):
- Promotion triggers requiring a new approved phase:

## Architecture and durable boundaries
- Module ownership and dependency direction:
- Data classification, contracts, and compatibility policy:
- External-service, security, and approval boundaries:
- Observability and failure-handling expectations:

## Lifecycle and authority
- Phase naming and coordinator-reuse policy:
- Human approval matrix:
- Design Handoff, implementation, validation, review, and terminal-handoff rules:
- Change-control and ADR triggers:

## Milestones and delivery forecast
| Milestone | Outcome | Effort range / time window | Dependencies | Replan trigger |
| --- | --- | --- | --- | --- |
| <M1> | <outcome> | <range> | <dependency> | <condition> |

Notes:
- A forecast is not an acceptance criterion or delivery guarantee.
- A missed timebox produces evidence, blockers, and an explicit human decision:
  reduce scope, extend, or create a new phase.

## Quality and release policy
- Definition of Ready / Definition of Done:
- Required validation evidence and review thresholds:
- Release, rollback, incident, and feedback rules (if in scope):

## Documentation map
- Phase handoffs:
- Implementation plans:
- ADRs:
- Test evidence / runbooks:
```

## Design Handoff

```markdown
# Design Handoff — <phase name>

Status: Draft | Approved | Implementing | Implemented | Reviewed | Blocked
Owner: <coordinator task>
Phase: <X>

## Goal and scope
- Problem:
- In scope:
- Out of scope:

## Decisions and assumptions
- Confirmed decisions:
- Assumptions to validate:
- Alternatives rejected and why:
- Technical and safety constraints:

## Acceptance criteria
- [ ] User-visible behavior:
- [ ] Error and edge cases:
- [ ] Security, performance, compatibility, and observability:

## Attached implementation plan
- Plan location or embedded plan:
- Ordered steps:
- Affected modules / contracts / data:
- Ownership and non-overlap:

## Validation plan
- Automated tests and commands:
- Manual checks:
- Evidence required before default, external, or production-affecting changes:

## Risks and approval gates
- Known risks:
- Decisions requiring human approval:
- Exact next human instruction needed:
```

## Coordinator brief

```text
Act as 协调任务<X> for <project / milestone>.

Read applicable AGENTS.md files, the current Design Handoff, and linked plan.
Do planning and coordination only until the human has approved both the handoff
and plan and explicitly authorized implementation. Keep the current coordinator
conversation if reuse conditions hold; otherwise explain why a new coordinator
conversation is needed. Do not implement inline. When authorized, create one
project-scoped 实施任务<X> as the sole writer with a bounded brief. After its
required validation completes, decide whether a separate read-only 审查任务<X>
is proportionate under project rules. Consolidate evidence, risks, and the next
human decision in the terminal handoff.
```

## Implementation brief

```text
You are 实施任务<X>, the sole writer for <approved milestone>.

Read AGENTS.md, the Approved Design Handoff, and its attached plan. Own only:
<bounded scope / file areas>. Do not broaden scope, invoke external or
production-affecting actions, or change runtime defaults without the listed
human approval. Implement the whole approved phase in this task, using the
repository's test and validation conventions. You may delegate only independent
read-only investigation or explicitly non-overlapping file work; you remain
responsible for integration. Return a factual handoff with changed files,
commands and outcomes, unmet criteria, and residual risks. Do not self-approve
release readiness.
```

## Review brief

```text
You are 审查任务<X>, a strictly read-only reviewer for <approved milestone>.

Read AGENTS.md, the Approved Design Handoff, implementation handoff, and the
actual diff. Do not edit files, run mutating operations, or create external
effects. Check the approved scope, acceptance criteria, security and data
boundaries, regressions, and whether validation evidence supports the claims.
Report actionable findings ordered by severity, each with evidence, impact, and
file/location when available. State explicitly if no blocking findings exist.
Return findings to the coordinator; do not fix them yourself.
```
