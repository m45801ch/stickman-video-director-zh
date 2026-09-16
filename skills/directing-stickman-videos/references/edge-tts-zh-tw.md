# Edge TTS — Taiwan Mandarin export

Use this reference when the user selects Taiwanese Mandarin narration or asks for an external Edge TTS voice track.

## Voice defaults

- Default: `zh-TW-HsiaoChenNeural` — friendly, positive female voice
- Alternatives: `zh-TW-HsiaoYuNeural` — female Taiwanese Mandarin; `zh-TW-YunJheNeural` — male Taiwanese Mandarin
- Keep one selected voice for the whole video. Do not switch voices between clips.

## Install and verify

```bash
python -m pip install edge-tts
edge-tts --list-voices
```

If the selected voice is absent from the local list, use a currently listed `zh-TW` voice and tell the user which one was substituted.

## Project generator

The reusable generator is `scripts/edge_tts_generate.py`. It accepts one `.txt` file for a continuous track or a folder of numbered `.txt` files for independently assembled clips. It uses the same voice for every input and refuses to overwrite existing output unless `--force` is supplied.

For twelve clips, place `vo-01.txt` through `vo-12.txt` in `narration/`, preview the commands, then generate:

```bash
python skills/directing-stickman-videos/scripts/edge_tts_generate.py --input narration --output-dir audio/vo-zh-tw --voice zh-TW-HsiaoChenNeural --dry-run
python skills/directing-stickman-videos/scripts/edge_tts_generate.py --input narration --output-dir audio/vo-zh-tw --voice zh-TW-HsiaoChenNeural
```

Remove `--dry-run` only after checking the input order and output paths.

## Export one continuous track

Put the approved Traditional Chinese narration in `vo-zh-tw.txt`, then run:

```bash
edge-tts --voice zh-TW-HsiaoChenNeural --file vo-zh-tw.txt --write-media vo-zh-tw.mp3 --write-subtitles vo-zh-tw.srt
```

For independently assembled clips, split the approved narration at the storyboard row boundaries and export `vo-01.mp3` through `vo-NN.mp3`, where `NN` is the requested clip count. For example, a 120-second video with 12 clips uses `vo-01.mp3` through `vo-12.mp3`. Prefer the continuous track when the editor supports it; it produces more consistent pauses and prosody.

## Assembly guidance

Use the SRT only for editing alignment; do not burn subtitles into the generated visuals unless the user explicitly requests captions. Mix the external narration above BGM and SFX, and preserve the exact approved script without adding or repeating lines.
