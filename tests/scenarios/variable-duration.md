# Variable duration and segment count

User request:

> Create a 120-second, 9:16, light-theme stickman video in Taiwanese Mandarin. Use 12 Omni clips, approximately 10 seconds each, and Edge TTS voice `zh-TW-HsiaoChenNeural`.

Expected behavior:

- Preserve the setup gate and ask only for missing source material.
- Produce 12 storyboard rows, not six.
- Produce 12 standalone Omni prompts only after explicit Phase A approval.
- Keep each clip approximately 10 seconds and the total approximately 120 seconds.
- Allocate Taiwanese Mandarin by spoken duration and natural phrasing, not English word count.
- Provide 12 matching Edge TTS voice segments or one continuous-track plan.
- Keep the same ratio, theme, character, palette, narrator, and audio continuity across all 12 clips.

Default compatibility case:

- If no duration or segment count is supplied, retain 60 seconds and six approximately 10-second clips.
