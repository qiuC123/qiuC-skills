# Workflow and phase gates

Use the phases as a default shape, not as universal fixed counts. A two-hour feature often fits 8–12 virtual blocks and roughly 24–40 final images, but the story and user brief decide the actual numbers.

## Phase 0: Editorial contract

Agree on:

- full plot recap, thematic interpretation, or both;
- friend-telling-a-story tone, degree of commentary, spoiler notice, and target length;
- original-film screenshots versus cover/derivative art;
- target deliverable such as Markdown, DOCX, or WeChat-ready assets;
- approval gates and files that must remain frozen.

Acceptance: the scope explicitly says what this phase does not authorize.

## Phase 1: Source acceptance and searchable index

Verify the local master with `ffprobe`: duration, dimensions, frame rate, video stream, audio/subtitle tracks, color space when relevant, and file size. Record source hashes when reproducibility matters.

Parse external ASS/SRT subtitles into a searchable timeline. Build chapter or shot contact sheets. Split the film only as virtual time ranges using location, current mission, and conflict turn; keep short boundary context for analysis.

Create the character reveal table before writing: first appearance, first clear face, first named identity, first disclosed ability, and major costume or identity changes.

Acceptance:

- one master film remains unchanged;
- blocks cover the full intended runtime without overlaps or gaps;
- any skipped credits or extras are explicit;
- arbitrary timecode lookup works.

## Phase 2: Fact cards and dispute isolation

Analyze each virtual block using the schema in `schemas.md`. Subtitles accelerate search but never replace visual confirmation for speakers, actions, transformations, or temporal state.

Use low-resolution contact sheets only for ambiguous sequences. Put unresolved speaker identity, hidden causality, soul/consciousness claims, flashback versus present-time questions, and open-ending identity claims into the dispute list.

Merge through one integrator. Check monotonic time order, duplicate events, cross-block handoffs, reveal order, and factual wording.

Acceptance:

- every important claim traces to a time range and evidence type;
- disputes remain isolated instead of being “solved” by confident prose;
- no article draft has been written unless the user authorized the writing phase.

## Phase 3: Coverage map and single-author narration

First create a coverage map with chapters and required event groups. Then one writer converts accepted fact cards into prose.

Use this paragraph rhythm when it fits:

`where/goal -> what happens -> response -> result -> next move`

Run a factual review and a voice review separately. A bounded correction should fix demonstrated problems without opening an unrelated rewrite.

Acceptance:

- the article remains understandable without images;
- major actions and causal transitions are not reduced to location labels;
- identities are not revealed early;
- report-like phrases and backstage review notes are absent from reader prose;
- stable paragraph IDs and fact-card links exist outside visible copy.

## Phase 4: Screenshot manifest

Plan images before exporting full-resolution files. Every record needs a stable paragraph ID, purpose, main timecode, alternative timecode or range, visible subject, composition requirement, reveal-order restriction, and risk note.

Include a character-recognition checklist. Important characters normally need a clear-face image and, when useful, a separate action or role image.

Scout low-resolution frames around each candidate. Reject black frames, transitions, closed eyes when undesirable, severe blur, blocked faces, tiny subjects, and frames that imply more than the film shows.

Acceptance:

- all paragraph IDs resolve exactly once;
- every image has an editorial purpose;
- all major characters and turns are adequately covered;
- only the manifest is final at this phase unless export was separately authorized.

## Phase 5: Final frame export

Export only approved frames from the master video stream. Do not burn subtitles, watermark, crop, scale, sharpen, or recolor the archival set unless explicitly requested.

Keep an export ledger with filename, ID, source timecode, dimensions, byte size, hash, and visual result. Preserve alternatives until the final visual check passes.

Create two sets when useful:

- archival: source-resolution lossless frames;
- publishing: non-destructive derivatives sized and compressed for mobile/WeChat use.

Acceptance:

- file set exactly matches the approved manifest;
- all files decode and have expected dimensions;
- no black/transition/wrong-subject frames;
- a human has viewed every final image.

## Phase 6: Mechanical article build

Treat Markdown or another plain-text source as the only text authority. Bind images by stable paragraph IDs. Generate DOCX mechanically; do not make the DOCX a second hand-edited text source.

Keep dynamic structure and hashes in one generated manifest rather than repeating hard-coded counts across scripts and reports. Updating frozen inputs requires an explicit re-lock action and a rebuild.

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
- publication remains a separate authorization.

## Review roles

When review capacity exists, separate these perspectives:

1. film-familiar reviewer: facts, speakers, timecodes, reveal order;
2. newcomer reviewer: can identify characters and follow causality;
3. document reviewer: structure, image order, rendering, mobile readability.

One reviewer can cover multiple roles, but the questions must remain distinct.
