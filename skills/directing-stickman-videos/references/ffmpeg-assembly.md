# FFmpeg assembly

Use this reference after the requested video clips and external narration audio exist.

## Inputs

- `clips/clip-01.mp4`, `clips/clip-02.mp4`, ... in filename order
- `audio/vo-zh-tw.mp3` from Edge TTS, preferably one continuous track, or
- `audio/voice/vo-01.mp3`, `vo-02.mp3`, ... for per-clip alignment
- Optional `audio/bgm.mp3`
- Optional SFX tracks, supplied with `--sfx`; align them to the final timeline before mixing

## Assemble

```bash
python skills/directing-stickman-videos/scripts/assemble_video.py \
  --videos clips \
  --voice audio/vo-zh-tw.mp3 \
  --bgm audio/bgm.mp3 \
  --sfx audio/sfx.mp3 \
  --output output/stickman-final.mp4
```

Use `--dry-run` first. The default mix keeps voice at full level, BGM at `0.2`, and SFX at `0.35`. Adjust with `--voice-volume`, `--bgm-volume`, and `--sfx-volume` when needed. Use `--force` only when intentionally replacing an existing MP4.

For per-clip alignment, use matching numbered files. The tool measures every video with `ffprobe`, delays each voice segment to the cumulative start time, warns when a voice segment differs from its video by more than 0.25 seconds, and merges matching SRT files into `output/stickman-final.srt`:

```bash
python skills/directing-stickman-videos/scripts/assemble_video.py \
  --videos clips \
  --voice-dir audio/voice \
  --bgm audio/bgm.mp3 \
  --output output/stickman-final.mp4
```

The tool writes a temporary concat list, encodes a broadly compatible H.264/AAC MP4, loops BGM until the voice/video ends, and removes the temporary list after a real run. It does not burn SRT subtitles into the video; the merged SRT remains a separate subtitle file.
