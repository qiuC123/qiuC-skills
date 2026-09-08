---
name: story-wechat-producer
description: 制作电影、动画电影、动画剧集与漫画的中文公众号图文解说，串联素材核验、故事文案、原片截图或漫画页格配图、DOCX 排版与检查。面向没看过故事的读者，也可从已有字幕、初稿或配图继续。纯文案用 story-wechat-writer；不负责视频制作。
---

# 故事公众号图文制作

Produce a readable story with illustrations traceable to the chosen edition. Sources may be films, animation films or episodes, or manga; the output medium is a WeChat article.

`available sources -> source index and facts -> story narration -> illustration manifest -> checked source images -> DOCX -> render and review`

## Start and resume

1. Inspect the existing project before creating anything. Resume from its last accepted phase and preserve user files.
2. Use the existing brief for source type, version, selected episodes/chapters, local paths, article type, spoiler policy, length, and deliverables. Ask only for gaps that materially block the task. A full recap covers the ending of the agreed scope; ongoing series or selected chapters do not imply permission to spoil later material.
3. A request for a complete illustrated article authorizes the necessary local preparation, writing, frame export, layout, and checks. Continue through those phases without renewed permission. Stop at a narrower requested deliverable, an explicit user checkpoint, or a genuine blocker. Phase acceptance means passing checks, not automatically obtaining human approval.
4. Use `scripts/init_project.py --dry-run` to check a new workspace, then initialize within the authorized task. It accepts legacy `--video`/`--subtitle` or `--sources-json` for several episodes, manga, and subtitle-only starts; see [schemas.md](references/schemas.md). Never reinitialize an existing project to resume it. Uploading a draft and publishing each require applicable user authorization; reuse authorization already given for that action.

## Non-negotiable boundaries

- Maintain a source registry with a stable ID for each movie, episode, or manga edition/chapter file. Keep originals unchanged; virtual blocks are references, not duplicated source files. Compare adaptations explicitly instead of mixing their events as one timeline.
- Time locators always include the source ID. Manga locators identify edition, volume/chapter, file page or page-image filename, printed page where available, panel, and reading order. Do not invent manga timecodes or equate printed page numbers with PDF page indexes.
- Subtitles and OCR support finding candidates; they do not establish unviewed action, panel order, or who speaks. A text-only start permits a supported draft and pending-image plan; final source illustrations require access to the actual video or page images.
- Never bypass DRM, membership controls, or platform download restrictions. Use available source resolution honestly, without claiming a web preview or enlarged image is a source-quality frame.
- Record claim type separately from evidence source and level: observable fact, character statement, inference, or interpretation. Clear dialogue proves what was said, not that its proposition is true.
- Protect identity mysteries, motive reversals, and key suspense reveals. Record first appearance, first clear face, first named identity, first disclosed ability, and later identity/wardrobe changes separately; harmless names and orientation need not wait for an on-screen introduction.
- Parallel analysis may produce independent fact cards, but one integrator owns the merged fact table and one writer owns final prose.
- Plot illustrations come from the registered video or actual manga page images. Preserve speech bubbles, reading order, and cross-panel causality when cropping. AI images belong to covers or clearly labeled derivative sections and must not impersonate source frames or panels.
- Editing or generating an artifact does not authorize upload or publication.

## Phase routing

Read [references/workflow.md](references/workflow.md) when planning, starting, resuming, or advancing a project phase.

Read [references/schemas.md](references/schemas.md) before creating character, fact, dispute, paragraph, screenshot, or build-manifest records.

Read [references/qa-and-build.md](references/qa-and-build.md) when researching background, extracting final frames, building DOCX, changing frozen inputs, or performing final review.

## Writing contract

- Assume the reader has never seen or read the story. Introduce who matters, what they want, and the situation needed to understand their next choice. Tell the story in natural Chinese paragraphs, like sharing it with a friend.
- Keep the plot's causal chain and major turns. Add necessary orientation, use consistent names, and make small ordering changes when these improve understanding; preserve meaningful reveal boundaries and make flashbacks or time shifts clear.
- Make the causal links between major actions clear: current goal -> obstacle -> action -> result -> next move. Use this rhythm where it fits; a transition, quiet moment, or commentary paragraph need not contain every element.
- Let difficulty determine detail. Explain an unfamiliar setting or idea where it affects an action; do not reproduce every shot or front-load a theory lecture. Alternate events with scene-supported personal judgment, marking interpretation naturally.
- Use headings only when they help navigation; place or stage names can mark real transitions. Avoid report-style sections, mandatory reaction slogans, and announcing how the reader must feel. Let an opening detail gain meaning by the ending when the story supports it.
- Keep evidence notes, timecodes, IDs, and uncertainty governance out of the reader-facing prose unless they are editorially useful.
- If a fact remains disputed, use attributed language such as “角色甲认为” or omit it. Do not fill gaps with invented psychology, unseen causality, or a complete mechanism.

Use `story-wechat-writer` when available for drafting and voice revision with accepted facts, spoiler boundaries, and background sources. A prose-only request goes directly to that writer. This workflow retains responsibility for source verification, illustrations, and build QA; the writing contract above is sufficient when the writer is unavailable.

## Illustration contract

Every final image must have a job: identify a person, establish a place, show an action, mark a turn, or carry a theme. Bind it to a stable paragraph ID rather than a verbatim sentence.

Scout with contact sheets, frames, or manga page previews. Keep main and alternative source locators until review passes. Export video frames at source resolution; retain manga page originals and record panel crop coordinates as derivatives. Visually inspect every final image and its necessary surrounding context; record the actual reviewer and result. Bring unresolved recognition or scene questions to the user together, and never label an agent review as human approval.

## Completion report

Keep brief progress updates during the task. At delivery or an agreed checkpoint, report:

- inputs and evidence boundary;
- created or changed files;
- relevant record and media counts;
- validation and visual-review results;
- unresolved disputes and residual risks;
- any actual decision or missing input blocking completion; do not manufacture a next-phase approval request.

Do not claim that structural validation proves factual accuracy, visual quality, copyright clearance, upload compatibility, or publication success.
