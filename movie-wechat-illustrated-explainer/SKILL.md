---
name: movie-wechat-illustrated-explainer
description: Turn a lawful local movie and subtitles into a Chinese WeChat illustrated story explainer for readers who have not seen the film, with source verification, conversational narration, optional background research, original-frame illustrations, and DOCX build QA. Use for full-movie public-account graphic explainers; not for short-video production or generic reviews without source evidence.
---

# Movie WeChat Illustrated Explainer

Build the article as an evidence pipeline, not as a one-pass summary from memory:

`local film -> subtitle/shot index -> character reveal table -> fact cards + disputes -> newcomer-friendly narration -> screenshot manifest -> original-frame exports -> mechanical DOCX -> render and review`

## Start and resume

1. Inspect the existing project before creating anything. Resume from its last accepted phase and preserve user files.
2. Use the existing brief for the film version, local paths, article type, spoiler policy, length, and deliverables. Ask only for missing inputs or choices that materially block the task. A full recap normally includes the ending; place a brief spoiler notice before it.
3. A request for a complete illustrated article authorizes the necessary local preparation, writing, frame export, layout, and checks. Continue through those phases without renewed permission. Stop at a narrower requested deliverable, an explicit user checkpoint, or a genuine blocker. Phase acceptance means passing checks, not automatically obtaining human approval.
4. Use `scripts/init_project.py --dry-run` to check a new workspace, then initialize within the authorized task. Never reinitialize an existing project to resume it. Uploading a draft and publishing each require applicable user authorization; reuse authorization already given for that action.

## Non-negotiable boundaries

- Use one lawful local master film for formal analysis and frame export. Virtual time blocks are time ranges, not duplicated video files.
- Never bypass DRM, membership controls, or platform download restrictions. A web player may help inspect metadata, but it is not the formal 1080P screenshot source.
- Record claim type separately from evidence source and level: observable fact, character statement, inference, or interpretation. Clear dialogue proves what was said, not that its proposition is true.
- Protect identity mysteries, motive reversals, and key suspense reveals. Record first appearance, first clear face, first named identity, first disclosed ability, and later identity/wardrobe changes separately; harmless names and orientation need not wait for an on-screen introduction.
- Parallel analysis may produce independent fact cards, but one integrator owns the merged fact table and one writer owns final prose.
- Plot illustrations come from the film master. AI images belong to covers or clearly labeled derivative sections and must not impersonate film frames.
- Editing or generating an artifact does not authorize upload or publication.

## Phase routing

Read [references/workflow.md](references/workflow.md) when planning, starting, resuming, or advancing a project phase.

Read [references/schemas.md](references/schemas.md) before creating character, fact, dispute, paragraph, screenshot, or build-manifest records.

Read [references/qa-and-build.md](references/qa-and-build.md) when researching background, extracting final frames, building DOCX, changing frozen inputs, or performing final review.

## Writing contract

- Assume the reader has never seen the film. Introduce who matters, what they want, and the situation needed to understand their next choice. Tell the story in natural Chinese paragraphs, like sharing it with a friend.
- Keep the plot's causal chain and major turns. Add necessary orientation, use consistent names, and make small ordering changes when these improve understanding; preserve meaningful reveal boundaries and make flashbacks or time shifts clear.
- Make the causal links between major actions clear: current goal -> obstacle -> action -> result -> next move. Use this rhythm where it fits; a transition, quiet moment, or commentary paragraph need not contain every element.
- Let difficulty determine detail. Explain an unfamiliar setting or idea where it affects an action; do not reproduce every shot or front-load a theory lecture. Alternate events with scene-supported personal judgment, marking interpretation naturally.
- Use headings only when they help navigation; place or stage names can mark real transitions. Avoid report-style sections, mandatory reaction slogans, and announcing how the reader must feel. Let an opening detail gain meaning by the ending when the story supports it.
- Keep evidence notes, timecodes, IDs, and uncertainty governance out of the reader-facing prose unless they are editorially useful.
- If a fact remains disputed, use attributed language such as “角色甲认为” or omit it. Do not fill gaps with invented psychology, unseen causality, or a complete mechanism.

When `anime-film-commentary-writer` is available and appropriate to the brief, use it for drafting and voice revision with the accepted facts, spoiler boundary, and background sources. This workflow retains responsibility for source verification, illustrations, and build QA. The writing contract above remains sufficient when that skill is unavailable.

## Screenshot contract

Every final image must have a job: identify a person, establish a place, show an action, mark a turn, or carry a theme. Bind it to a stable paragraph ID rather than a verbatim sentence.

Scout with low-resolution contact sheets or individual previews. Export selected frames from the checked manifest at source resolution, keeping a main and alternative timecode until visual review passes. Visually inspect every final image with available image-viewing tools; record the actual reviewer and result. Bring unresolved recognition or scene questions to the user together, and never label an agent review as human approval.

## Completion report

Keep brief progress updates during the task. At delivery or an agreed checkpoint, report:

- inputs and evidence boundary;
- created or changed files;
- relevant record and media counts;
- validation and visual-review results;
- unresolved disputes and residual risks;
- any actual decision or missing input blocking completion; do not manufacture a next-phase approval request.

Do not claim that structural validation proves factual accuracy, visual quality, copyright clearance, upload compatibility, or publication success.
