# Workflow and acceptance checks

Use the phases as a default shape, not as universal fixed counts. Choose story blocks and image count from the selected film, episodes, or chapters and the article's needs.

Apply acceptance checks internally and continue within the user's authorized deliverables. Only explicit user checkpoints require staged approval. Preserve completed work on resume; a wording edit does not require reindexing sources or exporting unchanged images.

## Phase 0: Editorial contract

Establish from the user's brief, asking only about material gaps:

- full plot recap, thematic interpretation, or both;
- friend-telling-a-story tone, degree of commentary, spoiler notice, and target length;
- source frames or manga pages/panels versus cover/derivative art;
- target deliverable such as Markdown, DOCX, or WeChat-ready assets;
- explicit user checkpoints and files that must remain frozen.

Acceptance: the requested deliverables, spoiler boundary, and any user checkpoints are clear. A complete illustrated-article request covers the necessary local phases. An outline-only or text-only request ends at that deliverable. Upload and publication are separate actions governed by existing user authorization.

## Phase 1: Source acceptance and searchable index

Create or reuse the source registry described in `schemas.md`. Give each input a stable source ID, edition/version, and position in the selected story order. Record file hashes when reproducibility matters. Keep a movie and its manga adaptation as separate sources even when names and scenes coincide.

For video, verify each file with `ffprobe`: duration, dimensions, frame rate, streams, and relevant color information. Pair subtitles with the correct episode and check timing near the beginning, middle, and end; do not apply one film's offset across episodes. Parse ASS/SRT into searchable events, separating dialogue from lyrics, notes, and typography. Form virtual source-time ranges around story turns and retain boundary context. Repeated episode recaps, credits, previews, and alternate cuts must be marked instead of counted as new events.

For manga, inventory edition, volume/chapter, page files or archive/PDF order, printed page labels where available, and reading direction. Inspect page images to verify spread pairing, speech-bubble speakers, caption/narrator boxes, and panel sequence; OCR alone cannot settle these. Reference file pages separately from printed pages, and give panels page-local IDs in the verified reading order. Keep neighboring panels when an action crosses a gutter. A blank or missing page is a material source gap, not permission to invent the transition.

If only subtitles or OCR are available, start the supported fact/prose work and mark source-image checks pending. Request accessible videos/pages only for the phases that require them. Path existence and successful extraction do not mean the media has been visually or aurally reviewed.

Create character reveal records before the final prose: first appearance, first recognizable face, first named identity, first disclosed ability, and major costume or identity changes, using source locators rather than bare timestamps.

Mark which disclosures carry a real mystery or reversal. A routine name can help recognition before the source introduces it explicitly; a concealed identity or relationship must not be exposed by prose or an illustration early.

Acceptance:

- registered originals remain unchanged;
- blocks cover the agreed episode/chapter range; exclusions, overlapping review context, recaps, and extras are explicit;
- each locator resolves to its own source and source order is distinct from narration order;
- final image work starts only when its actual video/page source is available.

## Phase 2: Fact cards and dispute isolation

Analyze each story block using `schemas.md`. Confirm speakers, actions, transformations, and temporal state using the appropriate video/audio or page context; subtitles/OCR only accelerate search.

Reuse the source index and inspect additional low-resolution frames for ambiguous sequences. Put unresolved speaker identity, hidden causality, soul/consciousness claims, flashback versus present-time questions, and open-ending identity claims into the dispute list.

Merge through one integrator. Check source order and within-source locator order, duplicate events, cross-episode/chapter handoffs, reveal order, and factual wording. Do not compare two episodes by bare timestamp or sort manga by an unverified filename alphabetically.

Keep `claim_type`, `evidence_source`, and `evidence_level` separate. Attribute character statements until independent work evidence establishes the underlying claim. In manga, distinguish spoken bubbles, inner monologue, and narrator boxes. When needed, research a specific newcomer comprehension gap using `qa-and-build.md`; keep external supplements separate from source fact cards.

Acceptance:

- every important story claim traces to a source ID, time/page/panel locator, claim type, and evidence source;
- disputes remain isolated instead of being “solved” by confident prose;
- writing proceeds when included in the user's task, without an extra phase-specific permission request.

## Phase 3: Coverage map and single-author narration

First create a coverage map with chapters and required event groups. Then one writer converts accepted fact cards into prose.

Write for someone who has not seen or read the story. Introduce necessary identities, relationships, and settings at the point of need. Use plot causality to organize the article; the fact table stays in source order even if narration supplies earlier context. Preserve meaningful mysteries and signal time shifts. Explain difficult transitions and choices without cataloguing every shot or panel. Across episodes/chapters, restore only the context a newcomer needs and avoid repeatedly introducing the same person.

Integrate background briefly where it resolves a named difficulty. Distinguish the selected version, other adaptations, external knowledge, and personal interpretation naturally. Keep source IDs and research notes in sidecar records; use readable references where helpful. Use the available `story-wechat-writer` for prose and voice without making it a required dependency.

Use this paragraph rhythm when it fits:

`where/goal -> what happens -> response -> result -> next move`

Run a factual review and a voice review separately. A bounded correction should fix demonstrated problems without opening an unrelated rewrite.

Acceptance:

- the article remains understandable without images;
- major actions and causal transitions are not reduced to location labels;
- identity mysteries and key reversals are not revealed early; routine names support recognition;
- report-like phrases and backstage review notes are absent from reader prose;
- commentary has concrete scene support, background earns its place, and headings are used only when helpful;
- stable paragraph IDs and fact-card links exist outside visible copy.

## Phase 4: Illustration manifest

Plan images before export. Every record needs a stable paragraph ID, purpose, source ID and main/alternative locator, visible subject, composition requirement, reveal-order restriction, and risk note. Video uses source timecodes; manga uses page/panel references and planned crop coordinates when appropriate. Retain legacy screenshot IDs and filenames when resuming an existing project.

Include a character-recognition checklist. Important characters normally need a clear-face image and, when useful, a separate action or role image.

Scout frames or page previews around each candidate. Reject unusable video transitions, severe blur, blocked subjects, and images implying more than the source shows. For manga, verify the whole page/spread before accepting a panel crop; do not cut off bubble tails, omit a causal neighboring panel, join nonadjacent panels as a continuous action, or expose a later page's reveal early.

Acceptance:

- all paragraph IDs resolve exactly once;
- every image has an editorial purpose;
- all major characters and turns are adequately covered;
- the manifest passes review before export; continue to export if it is part of the requested deliverable.

## Phase 5: Final source-image export

Export selected frames from the registered video stream, or render/copy the actual manga page from the checked manifest. Keep an untouched archival source-image set. Video archival frames should not add subtitles, watermark, crop, scaling, sharpening, or recoloring unless requested. Manga's printed lettering and original marks are part of the source; do not remove them. Treat panel crops, compression, and mobile sizing as documented derivatives.

Keep an export ledger with filename, image ID, source ID and locator, source hash/version, dimensions, byte size, hash, derivative crop/render details, and visual result. Preserve alternatives until the final visual check passes.

Create two sets when useful:

- archival: source-resolution lossless frames or faithful manga page exports;
- publishing: non-destructive derivatives sized and compressed for mobile/WeChat use.

Acceptance:

- file set exactly matches the checked manifest;
- all files decode and have expected dimensions;
- no unusable video transitions, wrong subjects, manga sequence errors, or misleading crops;
- every final image has been visually inspected with a recorded reviewer and result; agent inspection is sufficient unless the user requested human approval. Escalate unresolved questions together and never invent a human review.

## Phase 6: Mechanical article build

Treat Markdown or another plain-text source as the only text authority. Bind images by stable paragraph IDs. Generate DOCX mechanically; do not make the DOCX a second hand-edited text source.

Keep dynamic structure and hashes in one generated manifest rather than repeating hard-coded counts across scripts and reports. Updating frozen inputs requires a recorded re-lock action and a rebuild within the authorized revision; respect files the user explicitly froze.

Acceptance:

- source paragraphs reassemble exactly after image insertion;
- all images occur once and in manifest order;
- reopened DOCX text and media match the inputs;
- rendered pages show no clipping, overlap, blank pages, broken headings, or distorted images;
- an archive build and a publishing-size build are distinguished when file size matters.

## Phase 7: Cover and derivative art

Keep this phase independent from plot screenshots. For AI character art, first freeze a reference sheet covering face, hair, hat/accessories, costume layers, and pose or era variants. Generate from a clean master and use masked local edits for single-region changes.

Acceptance:

- the chosen cover version is explicit;
- source frames/panels and AI art are not confused;
- repeated whole-image regeneration has not introduced identity or costume drift;
- any upload or publication follows the user's authorization for that action.

## Review roles

When review capacity exists, separate these perspectives:

1. source-familiar reviewer: facts, speakers, source locators, panel/episode order, reveals;
2. newcomer reviewer: can identify characters and follow causality;
3. document reviewer: structure, image order, rendering, mobile readability.

Agents can perform these reviews with the relevant evidence and visual tools. One reviewer can cover multiple roles, but the questions must remain distinct; human approval applies only when requested or needed to resolve a blocker.
