# DEV_STATE.md snapshot

Read this reference only when a terminal handoff, planned task change, or
unreliable context requires a resumable current-state snapshot.

## Evidence rules

Build the snapshot from the actual repository, Git state, current Design
Handoff, and tests or checks that were actually run. Record unknown facts as
`Unverified` or `Not run`; never infer success from a plan, old chat message, or
documentation alone.

Do not paste code, command logs, passwords, API keys, tokens, private keys,
cookies, personal data, or raw production records. Keep detailed phase scope,
approval decisions, and full validation evidence in the Design Handoff.

## Required shape

```markdown
# Development state

Last verified: <date/time or unknown>
Phase and status: <phase / Planning | Implementing | Ready for review | Complete | Blocked>

## Current goal
<one or two sentences>

## Completed and verified
- <confirmed result and short evidence reference>

## Key decisions
- <decision and why; link to the authoritative handoff when available>

## Important files and modules
- `<path>` — <why it matters>

## Validation evidence
- `<command or check>` — <actual result, or Not run>

## Known issues and risks
- <current limitation, blocker, rejected approach, or Unverified item>

## Exact next task
<the next bounded action and its prerequisite or required human decision>
```

## Update and resume rules

- Replace stale, duplicated, or superseded facts; this file is a current
  snapshot, not a chronological diary.
- Update it at phase close or before a planned handoff. Do not update it after
  every command or routine status message.
- If multiple tasks or worktrees must read it, follow the repository's
  documentation policy so the intended snapshot is available to them.
- When resuming, read `AGENTS.md`, the current Design Handoff, and
  `DEV_STATE.md`; verify the snapshot against the repository before changing
  code.
