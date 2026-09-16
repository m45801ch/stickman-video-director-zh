#!/usr/bin/env python3
"""Generate MP3 and SRT narration files with Microsoft Edge TTS."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_VOICE = "zh-TW-HsiaoChenNeural"


def discover_inputs(source: Path) -> list[Path]:
    """Return text files in deterministic filename order."""
    if source.is_file():
        if source.suffix.lower() != ".txt":
            raise ValueError(f"Input file must be .txt: {source}")
        return [source]
    if not source.is_dir():
        raise FileNotFoundError(f"Input path does not exist: {source}")
    inputs = sorted(source.glob("*.txt"), key=lambda path: path.name.lower())
    if not inputs:
        raise ValueError(f"No .txt narration files found in: {source}")
    return inputs


def build_command(
    executable: list[str],
    source: Path,
    media: Path,
    subtitles: Path,
    voice: str,
    rate: str,
    volume: str,
    pitch: str,
) -> list[str]:
    return [
        *executable,
        "--voice",
        voice,
        "--rate",
        rate,
        "--volume",
        volume,
        "--pitch",
        pitch,
        "--file",
        str(source),
        "--write-media",
        str(media),
        "--write-subtitles",
        str(subtitles),
    ]


def find_executable() -> list[str]:
    edge_tts = shutil.which("edge-tts")
    if edge_tts:
        return [edge_tts]
    try:
        import edge_tts  # noqa: F401
    except ImportError as exc:
        raise RuntimeError(
            "edge-tts is not installed. Run: python -m pip install edge-tts"
        ) from exc
    return [sys.executable, "-m", "edge_tts"]


def generate(
    source: Path,
    output_dir: Path,
    voice: str,
    rate: str,
    volume: str,
    pitch: str,
    force: bool = False,
    dry_run: bool = False,
) -> list[tuple[Path, Path]]:
    inputs = discover_inputs(source)
    executable = ["edge-tts"] if dry_run else find_executable()
    output_dir.mkdir(parents=True, exist_ok=True)
    generated: list[tuple[Path, Path]] = []

    for input_path in inputs:
        media_path = output_dir / f"{input_path.stem}.mp3"
        subtitles_path = output_dir / f"{input_path.stem}.srt"
        targets = (media_path, subtitles_path)
        existing = [path for path in targets if path.exists()]
        if existing and not force:
            names = ", ".join(str(path) for path in existing)
            raise FileExistsError(f"Refusing to overwrite existing output: {names}. Use --force.")

        command = build_command(
            executable,
            input_path,
            media_path,
            subtitles_path,
            voice,
            rate,
            volume,
            pitch,
        )
        if dry_run:
            print(subprocess.list2cmdline(command))
        else:
            subprocess.run(command, check=True)
        generated.append(targets)
    return generated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Edge TTS MP3 and SRT files from one .txt file or a folder of segments."
    )
    parser.add_argument("--input", required=True, type=Path, help="A .txt narration file or folder of .txt segments")
    parser.add_argument("--output-dir", required=True, type=Path, help="Folder for generated MP3 and SRT files")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help=f"Edge TTS voice (default: {DEFAULT_VOICE})")
    parser.add_argument("--rate", default="+0%", help="Speaking-rate adjustment, for example +5%% or -5%%")
    parser.add_argument("--volume", default="+0%", help="Volume adjustment")
    parser.add_argument("--pitch", default="+0Hz", help="Pitch adjustment")
    parser.add_argument("--force", action="store_true", help="Overwrite existing MP3 and SRT files")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without calling Edge TTS")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        generated = generate(
            source=args.input,
            output_dir=args.output_dir,
            voice=args.voice,
            rate=args.rate,
            volume=args.volume,
            pitch=args.pitch,
            force=args.force,
            dry_run=args.dry_run,
        )
    except (FileNotFoundError, FileExistsError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"Dry run: {len(generated)} narration segment(s).")
    else:
        print(f"Generated {len(generated)} narration segment(s) in {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
