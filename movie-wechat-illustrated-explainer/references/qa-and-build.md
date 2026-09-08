# Frame export, build, and QA

## Formal evidence hierarchy

Prefer:

1. local master frame, audio, subtitle, and explicit title cards;
2. continuity across nearby frames and dialogue;
3. official character/material references when needed for cover design;
4. user memory or third-party summaries as leads to verify, not final evidence.

Do not use a player screenshot as proof of source resolution. Do not treat subtitle text alone as enough to identify the speaker.

## Efficient media strategy

- Keep one master film.
- Store virtual block ranges and subtitle indexes as text or a small database.
- Use low-resolution contact sheets for scouting and disputes.
- Seek directly to timecodes; do not load the whole film into memory.
- Limit simultaneous decoders when storage is slow.
- Export source-resolution frames only after the manifest is approved.

Example archival export shape; discover the local FFmpeg path rather than assuming it:

```powershell
ffmpeg -nostdin -hide_banner -loglevel error -n `
  -ss <HH:MM:SS.mmm> -i <master-video> `
  -map 0:v:0 -frames:v 1 -an -sn -dn `
  -c:v png -pix_fmt rgb24 <output.png>
```

For exact frame-sensitive cases, verify seek behavior around the target and compare neighboring frames. Record the final selected timecode rather than assuming the first candidate is correct.

## Mechanical checks by phase

### Sources and blocks

- master exists and is unchanged;
- dimensions, duration, and frame rate recorded;
- subtitle encoding and event range usable;
- virtual blocks cover the intended film span continuously.

### Facts and disputes

- IDs unique;
- timecodes parse and sit inside their block;
- merged order is monotonic unless a deliberate flashback record says otherwise;
- no duplicate event cards;
- evidence level present;
- unresolved claims appear in the dispute list and not as objective narration.

### Narration

- all required coverage groups represented;
- character names obey reveal timing;
- visible text contains no internal timecodes, IDs, review instructions, or image placeholders unless the user requests them;
- no invented group psychology, unseen mechanism, or complete causality;
- duplicate paragraphs and repeated conclusions checked.

### Screenshot manifest and exports

- stable paragraph IDs resolve exactly once;
- required and alternative sets are distinct;
- all timecodes fall inside the film;
- final filenames match the approved set;
- each image decodes and has expected dimensions;
- no black frames, transitions, severe blur, blocked face, subtitle burn-in, player UI, or wrong subject;
- every final image was visually viewed, not only hashed.

### DOCX

- the article source is still the text authority;
- text reconstructed from split paragraphs matches the source;
- images occur once and in order;
- embedded media hashes match the chosen output profile;
- no floating-image surprises unless intentionally designed;
- reopen the DOCX and inspect OOXML counts;
- render all pages and check clipping, overlap, blank pages, orphan headings, image distortion, and abnormal whitespace.

If the preferred renderer is unavailable, report that failure and use an explicitly named alternative such as Word-to-PDF plus PDF page rendering. Do not describe a fallback as the original renderer succeeding.

## Two human reviews

Factual review asks:

- Who performs each action?
- Is the speaker confirmed?
- Is this present action, flashback, dream, simulation, or montage?
- Does the wording exceed what the film establishes?

Newcomer review asks:

- Can I recognize every important person when introduced?
- Can I explain why the story moves from one scene to the next?
- Does each image help recognition, action, turn, or mood?

## Freeze and revision policy

Freeze final inputs only after creative review. Keep hashes and dynamic counts in one manifest. When text, screenshot placement, or exported media changes:

1. verify the exact intended change and stable IDs;
2. check whether any image binding is affected;
3. update the source or manifest, not the DOCX by hand;
4. regenerate counts and hashes through one explicit re-lock step;
5. rebuild and repeat mechanical plus rendered QA;
6. version the output and handoff instead of leaving old reports that claim obsolete counts.

## Honest completion boundary

Passing these checks proves only that the chosen sources, mappings, and document are internally consistent and visually reviewed. It does not prove philosophical interpretations, legal publication rights, platform acceptance, or audience performance.
