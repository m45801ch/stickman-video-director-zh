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
- visual style and theme:
  - `Style 1 (Classic Minimalist)`: light (white background, black figure) or dark (black background, white figure)
  - `Style 2 (Modern Beanie Zeke)`:
    - `Style 2A (Modern Studio Tech)`: pure white high-key studio, subtle light-gray perspective grid, floating cyan/blue glass UI
    - `Style 2B (Cinematic Story)`: full-color narrative environments, cinematic lighting & depth
- narration language and voice, when the user has a preference
- total duration and/or number of clips, when the user has a preference; default to approximately 60 seconds and 6 clips

If anything is missing, ask for all missing items in one concise message and stop. If a user specifies only light or dark theme, default to Style 1. Never select an aspect ratio or style silently. Do not re-ask choices already supplied.

Urgency, generation cost, client pressure, and requests to "pick normal settings" do not waive this gate.

## Workflow

1. Read `references/storyboard-template.md` and `references/style-catalog.md`, then produce Phase A in the user's language, with narration in the selected language and a reference translation when useful.
2. Stop after the director's proposal and request explicit approval.
3. If the user changes ratio, style, theme, narration, scene structure, or global direction, recompose Phase A and request approval again.
4. Only after approval of the current Phase A, read `references/omni-flash-prompt-contract.md` and produce Phase B.
5. Use `references/examples.md` only when a concrete end-to-end example would resolve ambiguity.
6. When the user asks to generate stills first (先生圖), follow `## Stills pipeline` below before any video prompts. Stills never substitute Phase B approval.

Topic approval, schedule pressure, or approval of an older draft is not approval of the current Phase A.

## Output rules

- For the default approximately 60-second English video, target 130–150 spoken words. For Chinese narration, target the requested duration and prioritize natural Taiwanese Mandarin phrasing over a word-count match.
- If duration is specified without a clip count, calculate `ceil(total seconds / 10)` clips and distribute the final remainder naturally. If clip count is specified without duration, target approximately 10 seconds per clip. If both are specified, honor both and adjust individual clip lengths within a practical range.
- Build exactly the requested number of storyboard rows and standalone prompts; never silently revert to six. For the default case, use six rows and six prompts.
- Give each clip three timed beats, at least four relevant visual devices, and a visual change every two to three seconds.
- Keep character proportions, line weight, style, and narrator consistent across all clips.
- For Style 1, limit the video to three saturated accent colors named with ordinary descriptive words (e.g. vivid red, electric blue, warm gold). For light theme, enforce a flat, digitally pure-white canvas with no textures, gradients, or 3D depth.
- For Style 2 (Modern Beanie Zeke), enforce character consistency:
  - Clip 1: `A minimalist 2D animated stick figure wearing a bright red beanie (smooth knit, no pom-pom) and a yellow t-shirt, with simple black stick limbs and shorts. Simple black lines, vibrant colors, smooth 2D animation style.`
  - Clips 2–6: `The same minimalist 2D animated stick figure in a bright red beanie and yellow shirt... Simple black lines, vibrant colors, smooth 2D animation style.`
  - No detailed eyes, pupils, or photorealistic features (avoids bug-eye deformation).
- For Style 2A (Modern Studio Tech), enforce: `in a modern bright white studio space with subtle light-gray perspective grid lines on the floor plane. High-key studio lighting, clean white negative space, sleek glowing cyan and electric blue glass holographic UI elements.` Always include negative constraint: `STRICTLY MINIMALIST, NO CIRCUIT BOARD TEXTURES, NO SCI-FI WALL PANELS, NO CRACKED CONCRETE.`
- For Style 2B (Cinematic Story), specify full-color narrative setting and cinematic lighting while preserving the 2D animated stick-figure character design.
- For all styles, avoid abstract liquid/shape morphing. Drive motion with concrete character actions (leaping, touching glass, drawing luminous lines, opening doors) with timed beats across `[0–3s]`, `[3–7s]`, and `[7–10s]`. Never leave the character idle.
- Lock narrator voice description verbatim across all clips. Mandate BGM continuity from clip 1.
- Treat narration as audio-only (`Audio voiceover only, strictly no speech bubbles, no dialogue boxes`). Quote exact dialogue and forbid alteration, repetition, captions, subtitles, or visual transcription.
- Never place technical color notation (hex, RGB, Pantone) inside generation prompts.
- Default generated clips to no visible words, letters, numbers, or interface copy. Put optional two-to-five-word overlays in a separate post-production note.
- Match every clip ending to the next clip opening.
- Do not invent unsupported facts, statistics, quotations, or product claims.

## Stills pipeline (asset-first, first-frame only)

When stills are requested, generate in this order and never skip ahead:

1. Character assets: reference sheet (multi-view) → solo full-body → per-character variants. Lock headwear, clothing, limbs, line weight verbatim. Variants must restate the full design; never write "same as R2" — external image tools cannot resolve cross-references.
2. Scene master: one clean establishing still per location, no people, with reserved negative space.
3. Prop assets: each prop isolated on plain background first (two angles where structure matters), then its in-context version. Icon-only, no legible text or numbers.
4. First-frame stills: one per clip, in story order, using locked assets as references.

First-frame stills are NOT video-action prompts:

- A still describes exactly one opening moment: the clip's first frame, a single frozen decisive instant inherited from the previous clip's ending. Never compress two sequential actions (e.g. pull THEN stumble) into one still.
- Multi-action evolution belongs to the video prompt's `[0–3s]`, `[3–7s]`, `[7–10s]` beats, not the still.
- Translate video-only camera language into static equivalents for stills: camera shake → slight Dutch tilt; motion → motion blur, dust trails, coiled poses; no idle standing.
- State shot size and angle explicitly per still (e.g. wide / medium / close-up, eye-level / low-angle / top-down 90°). Video camera moves stay in the video prompt only.

@tag contract (applies to every still prompt):

- Maintain an asset registry with exact tags. Tags carry the asset-number prefix so they match filenames exactly, e.g. `@a4-maintenance-bay` for the scene, `@a1-cable-reel` / `@a3-floor-hole` / `@a5-payoff-stand` for props, `@stickman-azhe` / `@xiaolin` for cast. A tag is the filename base: output files append only a variant suffix (e.g. tag `@a1-cable-reel` → files `a1-cable-reel-sheet`, `a1-cable-reel-inbay`). Never use an unprefixed tag alongside a prefixed filename.
- Open every still prompt with its scene in both languages: Chinese `在@a4-maintenance-bay中` and English `In @a4-maintenance-bay, ...`.
- Mark every prop and character inline with its tag in BOTH the Chinese and English text — never use a bare name where a tag exists.
- Prepend each prompt with a checklist header naming its cast, scene, and props, e.g. `> 本張使用｜人物：@stickman-azhe｜場景：@a4-maintenance-bay｜道具：@a1-cable-reel @a3-floor-hole`, so the user can verify coverage before generating.
- Assign every still prompt an English output filename derived from its tag, placed on the line right after the section header, e.g. `檔名：a1-cable-reel-sheet` (no file extension — the generator appends it). Section headers carry the same English slug as the filename (e.g. `## A7 計數器 click-counter`), so header, tag, and filename always match. Isolated sheets and in-context variants get separate filenames (e.g. `a1-cable-reel-sheet` vs `a1-cable-reel-inbay`). Storyboard first-frames use their clip code as filename (e.g. `## C1 ...` → `檔名：c1`). Filenames use the exact `@tag` slug so saved files map back to registry entries.
- Machine-parseable layout: each prompt block is contiguous lines with no blank lines inside it (`##` header → `檔名：` → checklist → `中：` → `EN：` → code fence). Each `中：` paragraph and each English prompt is a single unbroken line (no manual wrapping). Blank lines appear only between blocks, never inside one.
- Repeat full character, palette (ordinary color names only), style, and negative locks verbatim in every prompt. No "same as above" shortcuts.

Style unity lock (per-style, prevents drift across independently generated stills):

- Foreground render is shared by all styles: `clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills`. Backgrounds are locked per style and must never be mixed:
  - Style 1 Light: `flat uniform digitally pure-white canvas, no shading, no texture, no gradients, no 3D depth, up to three saturated accent colors named in ordinary words`.
  - Style 1 Dark: `flat uniform pitch-black canvas with pure white line art, up to three saturated accent colors named in ordinary words`.
  - Style 2A Studio Tech: `modern bright white studio space with subtle light-gray perspective grid lines on the floor plane, high-key studio lighting, clean white negative space, sleek glowing cyan and electric blue glass holographic UI elements`, plus negatives `no circuit board textures, no sci-fi wall panels, no spaceship corridors, no cracked concrete, no grunge textures`.
  - Style 2B Cinematic Story: `rich full-color cinematic environment with warm color grade, soft volumetric lighting, shallow depth of field, and soft shadows only`, plus negatives `no photorealistic rendering, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures`.
- Pick the ONE style chosen at the setup gate and repeat its background sentence verbatim in characters, scenes, props, and every first-frame still of that project. A 2B project must never contain 2A grid/glass wording and vice versa.
- Isolated reference sheets may use a plain background but must keep the shared foreground render (outlines, fills, shading); never switch one asset to photorealistic, 3D, or grunge aesthetics.
- Never abbreviate locks as "same style".

## Narration and TTS

- English remains the default narration language for backward compatibility.
- If the user requests Taiwanese Mandarin, use Traditional Chinese and default to Microsoft Edge TTS voice `zh-TW-HsiaoChenNeural` (female) or offer `zh-TW-YunJheNeural` (male) and `zh-TW-HsiaoYuNeural` (female) as alternatives.
- Keep the selected language, voice, locale, pace, and delivery identical across all requested prompts. Replace "English dialogue" with "selected-language dialogue" everywhere.
- When external audio is requested, read `references/edge-tts-zh-tw.md` and use `scripts/edge_tts_generate.py` to generate the MP3/SRT files when the runtime has `edge-tts` installed. Provide a per-clip script/export plan and treat generated narration as audio-only during final assembly.
- When video clips and audio assets are available and assembly is requested, read `references/ffmpeg-assembly.md` and use `scripts/assemble_video.py` to create the final MP4. Do not claim the final video exists until the command succeeds.

## Revision rules

Recompose rather than rename:

- `16:9`: stage action across left, center, and right; use lateral tracking and negative space.
- `9:16`: use depth, stacked motion, vertical reveals, and interface-safe placement.
- `1:1`: use compact central composition and shorter travel paths.

Theme or style changes require a fresh visual balance check. A global change invalidates prior approval.

## Final check

Apply the checklist in the loaded reference. Repair any failed condition before responding.
