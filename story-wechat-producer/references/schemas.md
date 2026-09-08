# Record schemas

Use stable IDs. Do not make downstream assets depend on exact prose wording.

## Project sources and legacy compatibility

New projects use `schema_version: 2` and `sources`, an ordered registry. Each entry has a unique `source_id`, `source_type` (`film`, `animation`, or `manga`), `version`, and `order`. A subtitle-only video entry supports drafting with visual/audio checks pending. A source path existing does not mean its content is verified.

```json
{
  "sources": [
    {"source_id": "AN-S01E03", "source_type": "animation", "version": "BD", "order": 1, "season": 1, "episode": 3, "video": "media/03.mkv", "subtitle": "media/03.ass"},
    {"source_id": "MG-V02", "source_type": "manga", "version": "指定出版社第2卷", "order": 2, "volume": 2, "path": "pages/vol02", "reading_order": "rtl"}
  ]
}
```

This shows valid input forms; it does not authorize merging those adaptations' plots. Use separate evidence records and explicit comparison where both are requested. Relative paths resolve against the registry JSON's directory. `manga.path` may be an image, page directory, PDF, or archive; page extraction and actual decoding belong to source acceptance. Manga reading order is `rtl`, `ltr`, `vertical`, or `unverified`; do not choose it from the language alone.

Initialize a new project with either:

```text
python scripts/init_project.py --root <new-project> --title <title> --video <movie> --subtitle <subtitles> --dry-run
python scripts/init_project.py --root <new-project> --title <title> --sources-json <registry.json> --dry-run
```

Remove `--dry-run` after the destination preflight. The initializer creates templates and validates source paths, not media decoding or completed review. It retains historical output directory names such as `05_必选截图/原片PNG` for project compatibility; manga pages may use that archival source-image directory too.

When resuming schema-v1 `project.json`, treat `source.video` and `source.subtitle` as one `FILM-01` entry; the helper `normalize_source_registry(project, project_directory)` provides that normalized view without rewriting the old project. Do not initialize over an existing project, discard its extra fields, or reset progress/authorization. New single-video projects retain `source.video`/`source.subtitle` alongside the registry for legacy readers. Existing bare-time records map to that sole source only; multi-source projects must resolve every bare locator explicitly. Retain `shot_id`, old time fields, and `source_video_hash_or_id` when consuming old records, adding generalized fields as needed.

## Source locator

Use `source_id` plus `source_locator` in factual, reveal, dispute, coverage, paragraph, and image records. A record spanning several sources uses an ordered `source_refs` list, not one continuous fabricated timestamp.

- Video: `{"start_time":"00:10:00.000","end_time":"00:10:08.000"}`; the source ID identifies the movie/episode. A still frame can use `timecode`.
- Manga: `{"volume":"2","chapter":"11","file_page":17,"page_file":"017.png","printed_page":"15","panel_ids":["P02","P03"],"reading_order":"rtl"}`. `file_page` is a **1-based** position in the checked file/page map; `printed_page` is the visible label, which may be absent. Use the page filename or file page that actually exists; unknown labels remain null/omitted. Panel IDs follow the verified page reading order, not arbitrary crop filenames.
- Crops: record `crop_xywh` relative to the full page image, its dimensions, and PDF rendering settings when relevant. A double-page spread records both file pages and the spread mapping. Page/panel coordinates are source references, never video timestamps.

## Character reveal record

| Field | Meaning |
| --- | --- |
| `character_id` | Stable internal ID, for example `CHAR-07` |
| `display_name` | Reader-facing name; routine orientation is allowed without exposing a concealed identity |
| `first_visible` | First source locator where the character appears |
| `first_clear_face` | First useful recognition frame or panel locator |
| `first_named` | First source locator naming the character |
| `identity_reveal` | Later disclosure locator, if different |
| `ability_reveal` | First demonstrated or stated ability |
| `wardrobe_states` | Source-ranged costume/hair/identity variants |
| `spoiler_rule` | Identity, relationship, or other meaningful reveal that must not be disclosed early |
| `recognition_shots` | Candidate face and role image references |

## Fact card

Recommended fields:

```text
fact_id
source_id
source_locator
location_or_time_card
known_identity_state
speaker_or_actor
visible_action
dialogue_summary
immediate_result
next_story_effect
screenshot_candidates
claim_type
evidence_source
evidence_level
uncertainty_or_cross_check
```

Required distinctions:

- `claim_type`: `observable_fact`, `character_statement`, `inference`, or `interpretation`.
- `evidence_source`: the source frame, audio, subtitle, page/panel, speech bubble, narrator box, or visible text reference and what was actually checked. OCR or subtitles alone are textual evidence. Confirm speakers with adequate source context and preserve speech/thought/narrator attribution.
- `evidence_level`: the existing shorthand below, used only alongside the type and source, never as a truth score.

Evidence levels (retain the letters for existing records):

- `A`: explicit dialogue, source text, or unambiguous visible action; speech establishes that the statement was made, not that its content is true;
- `B`: clear visual fact without an explicit verbal label;
- `C`: supported context or incomplete attribution; use careful wording;
- `D`: interpretation, thematic conclusion, or unresolved claim; keep out of the objective fact body.

An evidence letter does not replace a short explanation of why the claim is safe.

For example, in fictional practice material, “队长说桥是敌人炸的” is `character_statement` with direct audio evidence and level `A`. It cannot become “敌人炸了桥” without independent support. Record any independently observed event separately. When resuming older cards, add type and source before drafting from them; do not infer either from the letter alone.

## Optional background source record

Create only when external research resolves a specific comprehension gap. Use the selection rules in `qa-and-build.md`.

```text
background_source_id
reader_question
source_kind        original_edition|adaptation|official_material|interview|real_world_reference
title_author_url_or_edition
locator            page, section, or verified quotation location when available
work_version
supported_claim
limits_or_difference_from_target_work
intended_use       paragraph_id or planned story beat
```

Research notes and source IDs stay outside visible prose. Cite or attribute supplements naturally; another adaptation's event or a real-world theory must not become a fact of the selected version. Mark unverified sources and omit unsupported specifics. Existing background `source_id` fields can be retained with a distinct namespace; do not confuse them with registered plot media.

## Dispute record

```text
dispute_id
source_refs
claim_at_risk
what_the_source_supports
what_remains_unknown
safe_reader_wording
forbidden_overstatement
verification_needed
status
```

Typical disputes include speaker identity, off-screen action executors, flashback versus present state, mechanical causality, soul/consciousness claims, and open-ending identities.

## Coverage map

```text
chapter_id
chapter_title
source_refs
current_goal
required_events
causal_handoff_to_next_chapter
required_characters
required_disputes_to_handle_safely
```

## Paragraph record

Keep metadata outside visible prose, for example in a sidecar JSON/CSV/Markdown table:

```text
paragraph_id       C03-P07
chapter_id         C03
fact_ids           F03-09,F03-10
background_source_ids  optional, only for supplements actually used
source_refs        ordered source IDs + time/page/panel locators
visible_text       <reader-facing paragraph>
```

The paragraph ID remains stable when wording changes. If a paragraph is split or merged, update the mapping explicitly instead of reusing an ambiguous ID.

## Illustration manifest record

```text
shot_id
paragraph_id
fact_ids
status             required|alternative
purpose            person|place|action|turn|theme
source_id
main_locator
alternative_source_ref
crop_xywh          optional page crop, with full-image dimensions
visible_subject
composition_requirement
reveal_order_rule
risk_note
output_filename
```

## Export ledger record

```text
shot_id
source_id
source_locator
source_hash_or_version
source_video_hash_or_id  legacy video field, preserve when already used
derivation         video frame | page export | panel crop, with crop/render settings
filename
width
height
pixel_format
byte_size
sha256
visual_check       reviewer (agent|human), result, and unresolved issue if any
```

## Build manifest

Keep generated build facts in one machine-readable file such as `build_manifest.json`:

```json
{
  "schema_version": 2,
  "source_registry": {"path": "project.json", "sha256": "..."},
  "article_source": {"path": "...", "sha256": "..."},
  "screenshot_manifest": {"path": "...", "sha256": "..."},
  "export_ledger": {"path": "...", "sha256": "..."},
  "paragraph_count": 0,
  "text_block_count": 0,
  "body_fragment_count": 0,
  "image_count": 0,
  "image_set_sha256": "...",
  "output_profile": "archive"
}
```

Counts are outputs of parsing, not manually repeated constants. A release lock may freeze the manifest hash after creative review; record human approval separately only when it actually occurred.
