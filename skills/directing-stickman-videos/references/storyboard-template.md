# Director's Proposal Contract

Use this contract for Phase A. Present a readable production proposal and stop for confirmation before writing model prompts.

## Rewrite the source

Create one natural narration in the selected language for the requested total duration. If no duration is supplied, target approximately 55–65 seconds. For English, target 130–150 words for the default minute; for Taiwanese Mandarin, write natural Traditional Chinese and use duration rather than English word count as the primary constraint.

- Preserve the source's core claim, names, numbers, and factual meaning.
- Strengthen a weak opening with an immediate hook.
- Remove repetition and secondary branches from long sources.
- Expand short sources with a relevant example, progression, reframe, or callback.
- Prefer clear spoken language to literal translation.
- Simplify wording before increasing speaking speed.
- Do not invent research, statistics, quotations, product claims, or factual details.

Use the user's language for planning explanations. Keep the voiceover in the selected narration language and give a reference translation when the planning language differs.

## Header contract

Present these items in order:

1. English title and reference-language title
2. Core message and opening hook
3. Chosen aspect ratio and light/dark theme
4. Narrator identity, locale, speaking pace, spoken-length metric, and estimated duration
5. Up to three saturated accent colors, named in ordinary language, and what each represents
6. BGM direction, emotional turn, tone, and narrative arc

Default the narrator only after required setup is complete: a bright, energetic adult female voice speaking natural American English. If Taiwanese Mandarin is selected, use Microsoft Edge TTS `zh-TW-HsiaoChenNeural` unless the user chooses another voice. Infer tone and accent colors from the source when the user did not specify them.

## Narrative patterns

Choose the pattern that fits the source:

- Motivational: strong hook → recognition → escalation → reframe → action → payoff and CTA
- Educational: surprising hook → setup → mechanism → consequence → practical meaning → takeaway
- Commercial: pain point → consequence → product reveal → mechanism → proof or use case → benefit and CTA

## Storyboard contract

Produce exactly the requested number of approximately ten-second rows. If the user did not specify a duration or count, produce six rows for approximately 60 seconds:

| Time | Narrative purpose | Stick-figure scene | Motion, camera, and transition | Selected-language VO | Reference translation | BGM / SFX |
|---|---|---|---|---|---|---|

Give each row a different narrative job. Allocate natural sentence boundaries; use approximately 18–25 English words per row for English, or a similar ten-second spoken duration for Taiwanese Mandarin.

## Visual-density recipe

Build every row from three sequential beats:

- `0–3s`: establish or inherit the visual premise.
- `3–7s`: transform, escalate, or explain the metaphor.
- `7–10s`: deliver a climax and create the next transition.

Use at least four relevant devices per row:

- expressive stick-figure action
- environmental transformation
- concrete visual metaphor
- diagram, arrow, or icon-only symbol
- particles, energy, fluid, explosion, or light
- camera push, pull, pan, orbit, shake, or tracking move
- foreground wipe or object crossing the lens
- match cut, shape morph, or motion-matched transition
- interaction with another figure or oversized object

Require a perceptible visual change every two to three seconds. Make every effect clarify or intensify the spoken idea; omit unrelated spectacle.

## Palette and text

Keep the background and stick figure monochrome according to the selected theme. Use no more than three saturated accent colors across the video. Assign semantic meaning such as anxiety, danger, energy, discovery, or success.

Name colors only with ordinary descriptive language. Do not use hexadecimal, RGB, HSL, Pantone, or other technical color notation anywhere in the proposal or production prompts.

Default the generated video to no visible words, letters, numbers, captions, subtitles, interface copy, or technical annotations. Make message bubbles, content cards, meters, clocks, and notifications icon-only. After the storyboard, optionally list concise two-to-five-word English overlays for post-production, including their target clips and safe placement; never carry those overlays into the video-generation prompts.

## Composition by aspect ratio

- `16:9`: use left-center-right staging, lateral tracking, horizontal match cuts, and deliberate negative space. Reserve clean space for optional post-production overlays when useful.
- `9:16`: use foreground/background depth, vertical reveals, stacked motion, foreground passes, and interface-safe overlay space.
- `1:1`: keep action compact and center-weighted. Use short travel paths and avoid crucial events at extreme edges.

Changing ratio requires new staging, camera paths, transition geometry, and overlay-safe negative space. Changing theme requires inverted base colors and a fresh contrast check.

## Continuity

End each row with a visible interface that the next row inherits: a pose, moving object, filled frame, travel direction, shape, or camera motion. Name both sides of every connection in the proposal.

## Confirmation ending

End Phase A by asking the user to:

- approve the current proposal and generate the requested Omni Flash prompts;
- revise a named scene or narration passage; or
- change a global setting such as aspect ratio, theme, palette, voice, or tone.

Do not include final model prompts. A global change invalidates approval and requires a revised Phase A.

## Phase A checks

- Source, aspect ratio, and theme are known.
- Selected-language narration matches the requested total duration; the default is approximately 55–65 seconds. English is 130–150 words for the default minute, while Taiwanese Mandarin is checked by spoken duration and natural phrasing.
- The storyboard has exactly the requested number of rows; the default is six.
- Every storyboard row has a distinct narrative purpose.
- Every row has three beats, at least four visual devices, audio, and a transition.
- Visual change occurs approximately every two to three seconds.
- No more than three saturated accent colors are used.
- No technical color notation is present.
- Any proposed text is clearly separated as a post-production overlay and absent from generated scenes.
- Every adjacent pair has a named continuity connection.
- The ending returns to the central message.
- No unsupported factual detail was added.
