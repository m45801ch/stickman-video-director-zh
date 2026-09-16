#!/usr/bin/env python3
"""Concatenate video clips and mix voice, music, and sound effects with FFmpeg."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm"}
TIMESTAMP_RE = re.compile(r"(?P<start>\d{2}:\d{2}:\d{2}[,.]\d{3})\s+-->\s+(?P<end>\d{2}:\d{2}:\d{2}[,.]\d{3})")


def discover_videos(folder: Path) -> list[Path]:
    if not folder.is_dir():
        raise FileNotFoundError(f"Video folder does not exist: {folder}")
    videos = sorted(
        (path for path in folder.iterdir() if path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS),
        key=lambda path: path.name.lower(),
    )
    if not videos:
        raise ValueError(f"No video clips found in: {folder}")
    return videos


def segment_key(path: Path) -> str:
    match = re.search(r"(\d+)$", path.stem)
    return str(int(match.group(1))) if match else path.stem.lower()


def match_voice_segments(videos: list[Path], voice_dir: Path) -> list[tuple[Path, Path]]:
    if not voice_dir.is_dir():
        raise FileNotFoundError(f"Voice folder does not exist: {voice_dir}")
    voices = sorted(voice_dir.glob("*.mp3"), key=lambda path: path.name.lower())
    by_key: dict[str, Path] = {}
    for voice in voices:
        key = segment_key(voice)
        if key in by_key:
            raise ValueError(f"Duplicate voice segment number: {voice.name}")
        by_key[key] = voice
    pairs: list[tuple[Path, Path]] = []
    for video in videos:
        key = segment_key(video)
        voice = by_key.get(key)
        if voice is None:
            raise ValueError(f"Missing voice segment for {video.name}; expected a matching numbered MP3")
        pairs.append((video, voice))
    return pairs


def ffprobe_duration(path: Path) -> float:
    if not shutil.which("ffprobe"):
        raise RuntimeError("ffprobe is not installed or not available on PATH")
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def build_segment_audio_filter(
    clip_durations: list[float],
    voice_count: int,
    bgm: bool,
    sfx_count: int,
    voice_volume: float = 1.0,
    bgm_volume: float = 0.2,
    sfx_volume: float = 0.35,
) -> str:
    if voice_count != len(clip_durations) or voice_count < 1:
        raise ValueError("One voice segment and duration are required for every video clip")
    filters: list[str] = []
    labels: list[str] = []
    offset_ms = 0
    for index, duration in enumerate(clip_durations):
        delay = offset_ms
        filters.append(
            f"[{index + 1}:a]aresample=48000,adelay={delay}|{delay},volume={voice_volume}[voice{index}]"
        )
        labels.append(f"[voice{index}]")
        offset_ms += round(duration * 1000)
    next_input = voice_count + 1
    if bgm:
        filters.append(f"[{next_input}:a]aresample=48000,volume={bgm_volume}[bgm]")
        labels.append("[bgm]")
        next_input += 1
    for index in range(sfx_count):
        label = f"sfx{index}"
        filters.append(f"[{next_input}:a]aresample=48000,volume={sfx_volume}[{label}]")
        labels.append(f"[{label}]")
        next_input += 1
    filters.append(
        "".join(labels)
        + f"amix=inputs={len(labels)}:duration=longest:dropout_transition=2[mix]"
    )
    return ";".join(filters)


def parse_srt_timestamp(value: str) -> int:
    hours, minutes, rest = value.replace(",", ".").split(":")
    seconds, milliseconds = rest.split(".")
    return ((int(hours) * 60 + int(minutes)) * 60 + int(seconds)) * 1000 + int(milliseconds.ljust(3, "0")[:3])


def format_srt_timestamp(milliseconds: int) -> str:
    milliseconds = max(0, milliseconds)
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def merge_srt_files(srt_paths: list[Path], clip_durations: list[float], output: Path) -> None:
    if len(srt_paths) != len(clip_durations):
        raise ValueError("One SRT path and duration are required for every video clip")
    blocks: list[str] = []
    offset_ms = 0
    for srt_path, duration in zip(srt_paths, clip_durations):
        if srt_path.exists():
            content = srt_path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()
            for block in content.split("\n\n") if content else []:
                lines = block.splitlines()
                for line_index, line in enumerate(lines):
                    match = TIMESTAMP_RE.fullmatch(line.strip())
                    if match:
                        start = format_srt_timestamp(parse_srt_timestamp(match.group("start")) + offset_ms)
                        end = format_srt_timestamp(parse_srt_timestamp(match.group("end")) + offset_ms)
                        lines[line_index] = f"{start} --> {end}"
                        break
                blocks.append("\n".join(lines))
        offset_ms += round(duration * 1000)
    if blocks:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            "\n\n".join(f"{index}\n{block.split(chr(10), 1)[1] if block[:1].isdigit() and chr(10) in block else block}" for index, block in enumerate(blocks, 1)) + "\n",
            encoding="utf-8",
        )


def quote_concat_path(path: Path) -> str:
    """Quote a path for FFmpeg's concat demuxer list format."""
    return "'" + str(path.resolve()).replace("'", "'\\''") + "'"


def write_concat_list(videos: list[Path], destination: Path) -> None:
    destination.write_text(
        "\n".join(f"file {quote_concat_path(video)}" for video in videos) + "\n",
        encoding="utf-8",
    )


def build_audio_filter(
    audio_input_count: int,
    voice_volume: float,
    bgm_volume: float,
    sfx_volume: float,
) -> str:
    if audio_input_count < 1:
        raise ValueError("At least a voice input is required")
    filters = [f"[1:a]volume={voice_volume}[voice]"]
    labels = ["[voice]"]
    if audio_input_count >= 2:
        filters.append(f"[2:a]volume={bgm_volume}[bgm]")
        labels.append("[bgm]")
    for index in range(3, audio_input_count + 1):
        label = "sfx" if audio_input_count == 3 else f"sfx{index - 3}"
        filters.append(f"[{index}:a]volume={sfx_volume}[{label}]")
        labels.append(f"[{label}]")
    filters.append(
        "".join(labels)
        + f"amix=inputs={audio_input_count}:duration=first:dropout_transition=2[mix]"
    )
    return ";".join(filters)


def build_ffmpeg_command(
    concat_list: Path,
    voice: Path,
    bgm: Path | None,
    sfx: list[Path],
    output: Path,
    audio_filter: str,
) -> list[str]:
    command = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list)]
    command.extend(["-i", str(voice)])
    if bgm:
        command.extend(["-stream_loop", "-1", "-i", str(bgm)])
    for effect in sfx:
        command.extend(["-i", str(effect)])
    command.extend(
        [
            "-filter_complex",
            audio_filter,
            "-map",
            "0:v:0",
            "-map",
            "[mix]",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(output),
        ]
    )
    return command


def build_segment_ffmpeg_command(
    concat_list: Path,
    voices: list[Path],
    bgm: Path | None,
    sfx: list[Path],
    output: Path,
    audio_filter: str,
) -> list[str]:
    command = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list)]
    for voice in voices:
        command.extend(["-i", str(voice)])
    if bgm:
        command.extend(["-stream_loop", "-1", "-i", str(bgm)])
    for effect in sfx:
        command.extend(["-i", str(effect)])
    return command + [
        "-filter_complex",
        audio_filter,
        "-map",
        "0:v:0",
        "-map",
        "[mix]",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-shortest",
        "-movflags",
        "+faststart",
        str(output),
    ]


def find_ffmpeg() -> str:
    executable = shutil.which("ffmpeg")
    if not executable:
        raise RuntimeError("ffmpeg is not installed or not available on PATH")
    return executable


def assemble(
    videos_dir: Path,
    voice: Path | None,
    output: Path,
    voice_dir: Path | None = None,
    bgm: Path | None = None,
    sfx: list[Path] | None = None,
    voice_volume: float = 1.0,
    bgm_volume: float = 0.2,
    sfx_volume: float = 0.35,
    force: bool = False,
    dry_run: bool = False,
) -> Path:
    videos = discover_videos(videos_dir)
    if voice is None and voice_dir is None:
        raise ValueError("Provide either a continuous --voice file or a per-clip --voice-dir")
    if voice is not None and voice_dir is not None:
        raise ValueError("Use either --voice or --voice-dir, not both")
    if voice is not None and not voice.is_file():
        raise FileNotFoundError(f"Voice file does not exist: {voice}")
    effects = sfx or []
    missing_effects = [path for path in effects if not path.is_file()]
    if missing_effects:
        raise FileNotFoundError(f"SFX file does not exist: {missing_effects[0]}")
    if bgm is not None and not bgm.is_file():
        raise FileNotFoundError(f"BGM file does not exist: {bgm}")
    if output.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing output: {output}. Use --force.")

    output.parent.mkdir(parents=True, exist_ok=True)
    concat_list = output.with_suffix(".concat.txt")
    write_concat_list(videos, concat_list)
    if voice_dir is not None:
        pairs = match_voice_segments(videos, voice_dir)
        clip_durations = [ffprobe_duration(video) for video, _ in pairs]
        voice_paths = [segment_voice for _, segment_voice in pairs]
        for (video, segment_voice), clip_duration in zip(pairs, clip_durations):
            voice_duration = ffprobe_duration(segment_voice)
            difference = voice_duration - clip_duration
            if abs(difference) > 0.25:
                direction = "longer" if difference > 0 else "shorter"
                print(
                    f"Warning: {segment_voice.name} is {abs(difference):.2f}s {direction} than {video.name}",
                    file=sys.stderr,
                )
        audio_filter = build_segment_audio_filter(
            clip_durations,
            len(voice_paths),
            bgm is not None,
            len(effects),
            voice_volume,
            bgm_volume,
            sfx_volume,
        )
        command = build_segment_ffmpeg_command(
            concat_list, voice_paths, bgm, effects, output, audio_filter
        )
        srt_output = output.with_suffix(".srt")
        if srt_output.exists() and not force:
            raise FileExistsError(f"Refusing to overwrite existing subtitles: {srt_output}. Use --force.")
        merge_srt_files(
            [segment_voice.with_suffix(".srt") for segment_voice in voice_paths],
            clip_durations,
            srt_output,
        )
    else:
        input_count = 1 + (1 if bgm else 0) + len(effects)
        audio_filter = build_audio_filter(input_count, voice_volume, bgm_volume, sfx_volume)
        command = build_ffmpeg_command(concat_list, voice, bgm, effects, output, audio_filter)
    try:
        if dry_run:
            print(subprocess.list2cmdline(command))
        else:
            find_ffmpeg()
            subprocess.run(command, check=True)
    finally:
        if not dry_run and concat_list.exists():
            concat_list.unlink()
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Concatenate video clips and mix voice, BGM, and SFX into an MP4."
    )
    parser.add_argument("--videos", required=True, type=Path, help="Folder containing numbered video clips")
    voice_group = parser.add_mutually_exclusive_group(required=True)
    voice_group.add_argument("--voice", type=Path, help="One continuous voice MP3 file")
    voice_group.add_argument("--voice-dir", type=Path, help="Folder with matching vo-01.mp3, vo-02.mp3, ... files")
    parser.add_argument("--bgm", type=Path, help="Optional BGM file; loops until the voice/video ends")
    parser.add_argument("--sfx", action="append", type=Path, default=[], help="Optional SFX file; repeat for multiple tracks")
    parser.add_argument("--output", required=True, type=Path, help="Final MP4 output path")
    parser.add_argument("--voice-volume", type=float, default=1.0, help="Voice volume multiplier")
    parser.add_argument("--bgm-volume", type=float, default=0.2, help="BGM volume multiplier")
    parser.add_argument("--sfx-volume", type=float, default=0.35, help="SFX volume multiplier")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    parser.add_argument("--dry-run", action="store_true", help="Print the FFmpeg command without running it")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        assemble(
            videos_dir=args.videos,
            voice=args.voice,
            output=args.output,
            voice_dir=args.voice_dir,
            bgm=args.bgm,
            sfx=args.sfx,
            voice_volume=args.voice_volume,
            bgm_volume=args.bgm_volume,
            sfx_volume=args.sfx_volume,
            force=args.force,
            dry_run=args.dry_run,
        )
    except (FileNotFoundError, FileExistsError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Assembled video: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
