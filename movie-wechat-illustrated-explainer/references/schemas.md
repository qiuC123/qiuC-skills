# Record schemas

Use stable IDs. Do not make downstream assets depend on exact prose wording.

## Character reveal record

| Field | Meaning |
| --- | --- |
| `character_id` | Stable internal ID, for example `CHAR-07` |
| `display_name` | Reader-facing name; routine orientation is allowed without exposing a concealed identity |
| `first_visible` | First on-screen timecode |
| `first_clear_face` | First useful recognition frame |
| `first_named` | First time the film names the character |
| `identity_reveal` | Later disclosure time, if different |
| `ability_reveal` | First demonstrated or stated ability |
| `wardrobe_states` | Time-ranged costume/hair/identity variants |
| `spoiler_rule` | Identity, relationship, or other meaningful reveal that must not be disclosed early |
| `recognition_shots` | Candidate face and role frames |

## Fact card

Recommended fields:

```text
fact_id
start_time
end_time
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
- `evidence_source`: the frame, audio, subtitle, or title-card reference and what it establishes. Confirm speakers visually or through adequate context; preserve attribution in dialogue summaries.
- `evidence_level`: the existing shorthand below, used only alongside the type and source, never as a truth score.

Evidence levels (retain the letters for existing records):

- `A`: explicit dialogue, title card, or unambiguous visible action; dialogue establishes that the statement was made, not that its content is true;
- `B`: clear visual fact without an explicit verbal label;
- `C`: supported context or incomplete attribution; use careful wording;
- `D`: interpretation, thematic conclusion, or unresolved claim; keep out of the objective fact body.

An evidence letter does not replace a short explanation of why the claim is safe.

For example, in fictional practice material, “队长说桥是敌人炸的” is `character_statement` with direct audio evidence and level `A`. It cannot become “敌人炸了桥” without independent support. Record any independently observed event separately. When resuming older cards, add type and source before drafting from them; do not infer either from the letter alone.

## Optional background source record

Create only when external research resolves a specific comprehension gap. Use the selection rules in `qa-and-build.md`.

```text
source_id
reader_question
source_kind        original_novel|official_material|interview|real_world_reference
title_author_url_or_edition
locator            page, section, or verified quotation location when available
work_version
supported_claim
limits_or_difference_from_film
intended_use       paragraph_id or planned story beat
```

Research notes and source IDs stay outside visible prose. Cite or attribute reader-facing supplements naturally; a novel-only event or a real-world theory must not become a film fact. Mark sources that were not verified and omit unsupported specifics.

## Dispute record

```text
dispute_id
time_range
claim_at_risk
what_the_film_supports
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
time_range
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
time_range         00:10:00.000-00:12:30.000
visible_text       <reader-facing paragraph>
```

The paragraph ID remains stable when wording changes. If a paragraph is split or merged, update the mapping explicitly instead of reusing an ambiguous ID.

## Screenshot manifest record

```text
shot_id
paragraph_id
fact_ids
status             required|alternative
purpose            person|place|action|turn|theme
main_timecode
alternative_timecode_or_range
visible_subject
composition_requirement
reveal_order_rule
risk_note
output_filename
```

## Export ledger record

```text
shot_id
source_timecode
source_video_hash_or_id
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
  "schema_version": 1,
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
