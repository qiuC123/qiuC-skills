# Workflow and acceptance checks

Use the phases as a default shape, not as universal fixed counts. A two-hour feature often fits 8–12 virtual blocks and roughly 24–40 final images, but the story and user brief decide the actual numbers.

Apply acceptance checks internally and continue within the user's authorized deliverables. Only explicit user checkpoints require staged approval. Preserve completed work on resume; a wording edit does not require reindexing the film or exporting unchanged frames.

## Phase 0: Editorial contract

Establish from the user's brief, asking only about material gaps:

- full plot recap, thematic interpretation, or both;
- friend-telling-a-story tone, degree of commentary, spoiler notice, and target length;
- original-film screenshots versus cover/derivative art;
- target deliverable such as Markdown, DOCX, or WeChat-ready assets;
- explicit user checkpoints and files that must remain frozen.

Acceptance: the requested deliverables, spoiler boundary, and any user checkpoints are clear. A complete illustrated-article request covers the necessary local phases. An outline-only or text-only request ends at that deliverable. Upload and publication are separate actions governed by existing user authorization.

## Phase 1: Source acceptance and searchable index

Verify the local master with `ffprobe`: duration, dimensions, frame rate, video stream, audio/subtitle tracks, color space when relevant, and file size. Record source hashes when reproducibility matters.

Parse external ASS/SRT subtitles into a searchable timeline. Build chapter or shot contact sheets. Split the film only as virtual time ranges using location, current mission, and conflict turn; keep short boundary context for analysis.

Create the character reveal table before writing: first appearance, first clear face, first named identity, first disclosed ability, and major costume or identity changes.

Mark which disclosures carry a real mystery or reversal. A routine name can help recognition before the film says it aloud; a concealed identity or relationship must not be exposed by prose or an illustration early.

Acceptance:

- one master film remains unchanged;
- blocks cover the full intended runtime without overlaps or gaps;
- any skipped credits or extras are explicit;
- arbitrary timecode lookup works.

## Phase 2: Fact cards and dispute isolation

Analyze each virtual block using the schema in `schemas.md`. Subtitles accelerate search but never replace visual confirmation for speakers, actions, transformations, or temporal state.

Reuse the source index and inspect additional low-resolution frames for ambiguous sequences. Put unresolved speaker identity, hidden causality, soul/consciousness claims, flashback versus present-time questions, and open-ending identity claims into the dispute list.

Merge through one integrator. Check monotonic time order, duplicate events, cross-block handoffs, reveal order, and factual wording.

Keep `claim_type`, `evidence_source`, and `evidence_level` separate. Attribute character statements until independent film evidence establishes the underlying claim. When needed, research a specific newcomer comprehension gap using the background guidance in `qa-and-build.md`; keep those sources separate from film fact cards.

Acceptance:

- every important film claim traces to a time range, claim type, and evidence source;
- disputes remain isolated instead of being “solved” by confident prose;
- writing proceeds when included in the user's task, without an extra phase-specific permission request.

## Phase 3: Coverage map and single-author narration

First create a coverage map with chapters and required event groups. Then one writer converts accepted fact cards into prose.

Write for someone who has not seen the film. Introduce necessary identities, relationships, and settings at the point of need. Use plot causality to organize the article; the fact table stays in source-time order even if narration briefly supplies earlier context. Preserve meaningful mysteries and signal time shifts. Length comes from explaining difficult transitions and choices, not describing every shot.

Integrate background as a short, conversational explanation where it resolves a named difficulty. Distinguish the movie, the novel, external knowledge, and personal interpretation in reader-friendly language. Keep source IDs and research notes in sidecar records; use readable references where helpful. Use the available `anime-film-commentary-writer` for prose and voice if appropriate, without making it a required dependency.

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

## Phase 4: Screenshot manifest

Plan images before exporting full-resolution files. Every record needs a stable paragraph ID, purpose, main timecode, alternative timecode or range, visible subject, composition requirement, reveal-order restriction, and risk note.

Include a character-recognition checklist. Important characters normally need a clear-face image and, when useful, a separate action or role image.

Scout low-resolution frames around each candidate. Reject black frames, transitions, closed eyes when undesirable, severe blur, blocked faces, tiny subjects, and frames that imply more than the film shows.

Acceptance:

- all paragraph IDs resolve exactly once;
- every image has an editorial purpose;
- all major characters and turns are adequately covered;
- the manifest passes review before export; continue to export if it is part of the requested deliverable.

## Phase 5: Final frame export

Export selected frames from the checked manifest and master video stream. Do not burn subtitles, watermark, crop, scale, sharpen, or recolor the archival set unless explicitly requested.

Keep an export ledger with filename, ID, source timecode, source video hash or stable version ID, dimensions, byte size, hash, and visual result. Preserve alternatives until the final visual check passes.

Create two sets when useful:

- archival: source-resolution lossless frames;
- publishing: non-destructive derivatives sized and compressed for mobile/WeChat use.

Acceptance:

- file set exactly matches the checked manifest;
- all files decode and have expected dimensions;
- no black/transition/wrong-subject frames;
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
- film frames and AI art are not confused;
- repeated whole-image regeneration has not introduced identity or costume drift;
- any upload or publication follows the user's authorization for that action.

## Review roles

When review capacity exists, separate these perspectives:

1. film-familiar reviewer: facts, speakers, timecodes, reveal order;
2. newcomer reviewer: can identify characters and follow causality;
3. document reviewer: structure, image order, rendering, mobile readability.

Agents can perform these reviews with the relevant evidence and visual tools. One reviewer can cover multiple roles, but the questions must remain distinct; human approval applies only when requested or needed to resolve a blocker.
