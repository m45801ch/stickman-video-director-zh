---
name: directing-stickman-videos
description: Use when turning copy, notes, articles, or topics into stick-figure videos, kinetic line-animation explainers, motivational shorts, or Gemini Omni Flash prompt packages with selectable duration, narration language, and voice.
---

# Directing Stickman Videos

## Core contract

Turn one source into a confirmed director's proposal and then a user-selected number of standalone prompts for approximately ten-second Gemini Omni Flash clips. The default is six clips for approximately one minute. Preserve the source's meaning while strengthening its hook, progression, and closing callback.

## Setup gate

Require these before planning:

- source material
- aspect ratio: `16:9`, `9:16`, or `1:1`
- theme: light (white background, black figure) or dark (black background, white figure)
- narration language and voice, when the user has a preference
- total duration and/or number of clips, when the user has a preference; default to approximately 60 seconds and 6 clips

If anything is missing, ask for all missing items in one concise message and stop. Never select an aspect ratio or theme silently. Do not re-ask choices already supplied.

Urgency, generation cost, client pressure, and requests to "pick normal settings" do not waive this gate.

## Workflow

1. Read `references/storyboard-template.md` and produce Phase A in the user's language, with narration in the selected language and a reference translation when useful.
2. Stop after the director's proposal and request explicit approval.
3. If the user changes ratio, theme, narration, scene structure, or global style, recompose Phase A and request approval again.
4. Only after approval of the current Phase A, read `references/omni-flash-prompt-contract.md` and produce Phase B.
5. Use `references/examples.md` only when a concrete end-to-end example would resolve ambiguity.

Topic approval, schedule pressure, or approval of an older draft is not approval of the current Phase A.

## Output rules

- For the default approximately 60-second English video, target 130–150 spoken words. For Chinese narration, target the requested duration and prioritize natural Taiwanese Mandarin phrasing over a word-count match.
- If duration is specified without a clip count, calculate `ceil(total seconds / 10)` clips and distribute the final remainder naturally. If clip count is specified without duration, target approximately 10 seconds per clip. If both are specified, honor both and adjust individual clip lengths within a practical range.
- Build exactly the requested number of storyboard rows and standalone prompts; never silently revert to six. For the default case, use six rows and six prompts.
- Give each clip three timed beats, at least four relevant visual devices, and a visual change every two to three seconds.
- Keep character proportions, line weight, theme, and narrator consistent.
- Limit the video to three saturated accent colors. Name them only with ordinary descriptive words such as vivid red, electric blue, or warm gold.
- Never place hexadecimal, RGB, HSL, Pantone, or other technical color notation inside a model prompt. Treat palette choices as visual art direction, never visible content.
- For the light theme, request a flat, uniform, digitally pure-white canvas and forbid gray or off-white tint, texture, gradients, shadows, lighting, bloom, fog, and three-dimensional background depth. Do not express the white as a color code.
- Make each model prompt self-contained and repeat all critical locks.
- Treat narration as audio-only. Quote exact dialogue and forbid alteration, repetition, captions, subtitles, or visual transcription.
- Default generated clips to no visible words, letters, numbers, interface copy, or technical annotations. Make cards and notifications icon-only. Put any optional two-to-five-word overlay in a separate post-production note, never inside the generation prompt.
- Match every clip ending to the next clip opening.
- Do not invent unsupported facts, statistics, quotations, or product claims.

## Narration and TTS

- English remains the default narration language for backward compatibility.
- If the user requests Taiwanese Mandarin, use Traditional Chinese and default to Microsoft Edge TTS voice `zh-TW-HsiaoChenNeural` (female) or offer `zh-TW-YunJheNeural` (male) and `zh-TW-HsiaoYuNeural` (female) as alternatives.
- Keep the selected language, voice, locale, pace, and delivery identical across all requested prompts. Replace “English dialogue” with “selected-language dialogue” everywhere.
- When external audio is requested, read `references/edge-tts-zh-tw.md` and use `scripts/edge_tts_generate.py` to generate the MP3/SRT files when the runtime has `edge-tts` installed. Provide a per-clip script/export plan and treat generated narration as audio-only during final assembly.
- When video clips and audio assets are available and assembly is requested, read `references/ffmpeg-assembly.md` and use `scripts/assemble_video.py` to create the final MP4. Do not claim the final video exists until the command succeeds.

## Revision rules

Recompose rather than rename:

- `16:9`: stage action across left, center, and right; use lateral tracking and negative space.
- `9:16`: use depth, stacked motion, vertical reveals, and interface-safe placement.
- `1:1`: use compact central composition and shorter travel paths.

Theme changes invert background and base line art while preserving accent semantics and contrast. A global change invalidates prior approval.

## Final check

Apply the checklist in the loaded reference. Repair any failed condition before responding.
