# Frame export, build, and QA

## Formal evidence hierarchy

Prefer:

1. local master frame, audio, subtitle, and explicit title cards;
2. continuity across nearby frames and dialogue;
3. official character/material references when needed for cover design;
4. user memory or third-party summaries as leads to verify, not final evidence.

Do not use a player screenshot as proof of source resolution. Do not treat subtitle text alone as enough to identify the speaker.

## Optional background research

Research only a concrete comprehension gap: a setting needed to follow a choice, an unfamiliar concept, or a movie/novel difference the user wants explained. Use the film as the authority for film events. For supplements, prefer the original novel in an identified edition, official materials or a verifiable interview, and authoritative primary references for real-world claims. Summaries can suggest search leads but do not settle disputes.

Record each source using the optional background schema. State what it supports, its version, and its limits. Do not import a novel-only scene into the film timeline, turn a character's theory into an established mechanism, or present a fictional premise as proven science. Verify exact quotations and claims about creator intent; otherwise paraphrase within the evidence or omit the detail.

Insert a brief, conversational explanation where the story needs it, using attribution such as “原著在这里补充了……” or “我更倾向于理解为……”. Keep the plot moving; omit research that does not help the reader understand a scene or choice. Provide readable source links or edition references near the supplement or in a short reference note, without exposing the research ledger as article prose. Missing background evidence should block only that supplement unless it is essential to the requested explanation.

## Efficient media strategy

- Keep one master film.
- Store virtual block ranges and subtitle indexes as text or a small database.
- Use low-resolution contact sheets for scouting and disputes.
- Seek directly to timecodes; do not load the whole film into memory.
- Limit simultaneous decoders when storage is slow.
- Export source-resolution frames only after the manifest passes review; user approval is needed only at an agreed checkpoint.

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
- claim type, evidence source, and level present; explicit dialogue remains attributed unless its content is independently established;
- unresolved claims appear in the dispute list and not as objective narration.

### Narration

- all required coverage groups represented;
- character names aid recognition while preserving concealed identities and meaningful reveal timing;
- a newcomer can follow relationships, goals, necessary settings, and causal transitions, including any deliberate ordering changes;
- background sources support the specific supplements used, with version boundaries and personal interpretations clear;
- visible text contains no internal timecodes, IDs, review instructions, or image placeholders unless the user requests them;
- no invented group psychology, unseen mechanism, or complete causality;
- duplicate paragraphs and repeated conclusions checked.

### Screenshot manifest and exports

- stable paragraph IDs resolve exactly once;
- required and alternative sets are distinct;
- all timecodes fall inside the film;
- final filenames match the checked manifest;
- each image decodes and has expected dimensions;
- no black frames, transitions, severe blur, blocked face, subtitle burn-in, player UI, or wrong subject;
- every final image was visually inspected, not only hashed; record whether the reviewer was an agent or a human. Collect unresolved recognition or scene questions for the user, without claiming unperformed review.

### DOCX

- the article source is still the text authority;
- text reconstructed from split paragraphs matches the source;
- images occur once and in order;
- embedded media hashes match the chosen output profile;
- no floating-image surprises unless intentionally designed;
- reopen the DOCX and inspect OOXML counts;
- render all pages and check clipping, overlap, blank pages, orphan headings, image distortion, and abnormal whitespace.

If the preferred renderer is unavailable, report that failure and use an explicitly named alternative such as Word-to-PDF plus PDF page rendering. Do not describe a fallback as the original renderer succeeding.

## Factual and newcomer reviews

These are review perspectives, not mandatory human approval gates. Agents may perform them; use human review when the user requests it or a material question remains unresolved.

Factual review asks:

- Who performs each action?
- Is the speaker confirmed?
- Is this present action, flashback, dream, simulation, or montage?
- Does the wording exceed what the film establishes?
- Is a character's statement still attributed, and is external context distinct from film facts?

Newcomer review asks:

- Can I recognize every important person when introduced?
- Can I explain why the story moves from one scene to the next?
- Does each unfamiliar idea arrive with enough explanation, without interrupting the story with a lecture?
- Does each image help recognition, action, turn, or mood?

## Freeze and revision policy

Freeze final inputs only after creative review. Keep hashes and dynamic counts in one manifest. When text, screenshot placement, or exported media changes:

1. verify the exact intended change and stable IDs;
2. check whether any image binding is affected;
3. update the source or manifest, not the DOCX by hand;
4. regenerate counts and hashes through one explicit re-lock step;
5. rebuild and repeat mechanical plus rendered QA;
6. version the output and handoff instead of leaving old reports that claim obsolete counts.

Reuse unchanged source indexes, fact cards, and exported frames. Recheck facts or select new frames only when the revision affects them; still render all pages of the final rebuilt DOCX because pagination can change. Re-locking is a recorded build operation within the authorized revision, not a new approval gate; an explicit user freeze remains binding.

## Honest completion boundary

Passing these checks proves only that the chosen sources, mappings, and document are internally consistent and visually reviewed. It does not prove philosophical interpretations, legal publication rights, platform acceptance, or audience performance.
