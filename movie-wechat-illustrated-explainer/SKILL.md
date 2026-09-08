---
name: movie-wechat-illustrated-explainer
description: Turn a lawful local movie and subtitles into a fact-traceable Chinese WeChat public-account illustrated plot explainer, including source validation, timeline fact cards, reveal-order narration, screenshot planning and export, and DOCX build QA. Use for full-movie public-account graphic explainers; not for short-video production or generic reviews without source evidence.
---

# Movie WeChat Illustrated Explainer

Build the article as an evidence pipeline, not as a one-pass summary from memory:

`local film -> subtitle/shot index -> character reveal table -> fact cards + disputes -> ordered narration -> screenshot manifest -> original-frame exports -> mechanical DOCX -> render and review`

## Start and resume

1. Inspect the existing project before creating anything. Resume from its last accepted phase and preserve user files.
2. If no project exists, confirm the local film path, subtitle path when available, intended article type, spoiler policy, target length, and whether the user wants staged approval.
3. Default to staged approval for a full workflow. Finish and report the authorized phase, then stop. Do not silently proceed to screenshots, DOCX, upload, or publication.
4. Use `scripts/init_project.py --dry-run` to preview a new workspace. Run it without `--dry-run` only after the user authorizes initialization.

## Non-negotiable boundaries

- Use one lawful local master film for formal analysis and frame export. Virtual time blocks are time ranges, not duplicated video files.
- Never bypass DRM, membership controls, or platform download restrictions. A web player may help inspect metadata, but it is not the formal 1080P screenshot source.
- Keep four claim levels separate: screen/dialogue fact, character judgment, supported contextual inference, and unresolved interpretation. Do not promote the last two into objective fact.
- Preserve reveal order. Record first appearance, first clear face, first named identity, first disclosed ability, and later identity/wardrobe changes separately.
- Parallel analysis may produce independent fact cards, but one integrator owns the merged fact table and one writer owns final prose.
- Plot illustrations come from the film master. AI images belong to covers or clearly labeled derivative sections and must not impersonate film frames.
- Editing or generating an artifact does not authorize upload or publication.

## Phase routing

Read [references/workflow.md](references/workflow.md) when planning, starting, resuming, or advancing a project phase.

Read [references/schemas.md](references/schemas.md) before creating character, fact, dispute, paragraph, screenshot, or build-manifest records.

Read [references/qa-and-build.md](references/qa-and-build.md) before extracting final frames, building DOCX, changing frozen inputs, or performing final review.

## Writing contract

- Tell the story in natural, short Chinese paragraphs, like a friend recounting the film.
- Follow the film's disclosure order. Do not use later knowledge to name an earlier anonymous figure.
- For each narrative unit, keep the causal chain visible: current goal -> obstacle -> action -> immediate result -> next question or destination.
- Keep evidence notes, timecodes, IDs, and uncertainty governance out of the reader-facing prose unless they are editorially useful.
- If a fact remains disputed, use attributed language such as “角色甲认为” or omit it. Do not fill gaps with invented psychology, unseen causality, or a complete mechanism.

## Screenshot contract

Every final image must have a job: identify a person, establish a place, show an action, mark a turn, or carry a theme. Bind it to a stable paragraph ID rather than a verbatim sentence.

Scout with low-resolution contact sheets or individual previews. Export only approved frames from the master at source resolution, keeping a main and alternative timecode until visual approval.

## Completion report

For each phase, report:

- inputs and evidence boundary;
- created or changed files;
- record and media counts;
- validation and visual-review results;
- unresolved disputes and residual risks;
- the exact decision required for the next phase.

Do not claim that structural validation proves factual accuracy, visual quality, copyright clearance, upload compatibility, or publication success.
