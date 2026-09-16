import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "skills" / "directing-stickman-videos" / "scripts" / "assemble_video.py"
SPEC = importlib.util.spec_from_file_location("assemble_video", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AssembleVideoTests(unittest.TestCase):
    def test_discovers_numbered_video_clips_in_order(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "clip-02.mp4").touch()
            (folder / "clip-01.mp4").touch()
            (folder / "readme.txt").touch()

            clips = MODULE.discover_videos(folder)

            self.assertEqual([clip.name for clip in clips], ["clip-01.mp4", "clip-02.mp4"])

    def test_builds_audio_filter_with_voice_bgm_and_sfx_levels(self):
        audio_filter = MODULE.build_audio_filter(
            audio_input_count=3,
            voice_volume=1.0,
            bgm_volume=0.2,
            sfx_volume=0.35,
        )

        self.assertEqual(
            audio_filter,
            "[1:a]volume=1.0[voice];[2:a]volume=0.2[bgm];[3:a]volume=0.35[sfx];"
            "[voice][bgm][sfx]amix=inputs=3:duration=first:dropout_transition=2[mix]",
        )

    def test_command_maps_concatenated_video_and_mixed_audio(self):
        command = MODULE.build_ffmpeg_command(
            concat_list=Path("concat.txt"),
            voice=Path("voice.mp3"),
            bgm=Path("bgm.mp3"),
            sfx=[Path("sfx.mp3")],
            output=Path("final.mp4"),
            audio_filter="[1:a]volume=1.0[voice];[2:a]volume=0.2[bgm];[3:a]volume=0.35[sfx];[voice][bgm][sfx]amix=inputs=3:duration=first:dropout_transition=2[mix]",
        )

        self.assertIn("-f", command)
        self.assertIn("concat", command)
        self.assertIn("-stream_loop", command)
        self.assertIn("[mix]", command)
        self.assertEqual(command[-1], "final.mp4")

    def test_matches_voice_segments_to_video_numbers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "vo-02.mp3").touch()
            (folder / "vo-01.mp3").touch()

            pairs = MODULE.match_voice_segments(
                [Path("clip-01.mp4"), Path("clip-02.mp4")], folder
            )

            self.assertEqual([voice.name for _, voice in pairs], ["vo-01.mp3", "vo-02.mp3"])

    def test_builds_delayed_per_clip_voice_filter(self):
        audio_filter = MODULE.build_segment_audio_filter(
            clip_durations=[10.0, 10.5],
            voice_count=2,
            bgm=False,
            sfx_count=0,
        )

        self.assertIn("[1:a]aresample=48000,adelay=0|0,volume=1.0[voice0]", audio_filter)
        self.assertIn("[2:a]aresample=48000,adelay=10000|10000,volume=1.0[voice1]", audio_filter)
        self.assertIn("[voice0][voice1]amix=inputs=2:duration=longest", audio_filter)

    def test_merges_segment_srt_with_cumulative_offsets(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            first = folder / "vo-01.srt"
            second = folder / "vo-02.srt"
            output = folder / "all.srt"
            first.write_text("1\n00:00:00,000 --> 00:00:01,200\n第一段\n", encoding="utf-8")
            second.write_text("1\n00:00:00,000 --> 00:00:00,800\n第二段\n", encoding="utf-8")

            MODULE.merge_srt_files([first, second], [10.0, 10.5], output)

            merged = output.read_text(encoding="utf-8")
            self.assertIn("00:00:10,000 --> 00:00:10,800", merged)
            self.assertIn("第二段", merged)


if __name__ == "__main__":
    unittest.main()
