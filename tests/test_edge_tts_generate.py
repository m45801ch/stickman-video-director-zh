import importlib.util
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "skills" / "directing-stickman-videos" / "scripts" / "edge_tts_generate.py"
SPEC = importlib.util.spec_from_file_location("edge_tts_generate", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class EdgeTtsGenerateTests(unittest.TestCase):
    def test_discovers_numbered_text_segments_in_order(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "vo-02.txt").write_text("第二段", encoding="utf-8")
            (folder / "vo-01.txt").write_text("第一段", encoding="utf-8")
            (folder / "notes.md").write_text("忽略", encoding="utf-8")

            inputs = MODULE.discover_inputs(folder)

            self.assertEqual([path.name for path in inputs], ["vo-01.txt", "vo-02.txt"])

    def test_builds_edge_tts_command_with_same_voice_and_subtitles(self):
        command = MODULE.build_command(
            executable=["edge-tts"],
            source=Path("vo-01.txt"),
            media=Path("vo-01.mp3"),
            subtitles=Path("vo-01.srt"),
            voice="zh-TW-HsiaoChenNeural",
            rate="+0%",
            volume="+0%",
            pitch="+0Hz",
        )

        self.assertEqual(
            command,
            [
                "edge-tts",
                "--voice",
                "zh-TW-HsiaoChenNeural",
                "--rate",
                "+0%",
                "--volume",
                "+0%",
                "--pitch",
                "+0Hz",
                "--file",
                "vo-01.txt",
                "--write-media",
                "vo-01.mp3",
                "--write-subtitles",
                "vo-01.srt",
            ],
        )

    def test_argument_parser_supports_help_and_defaults(self):
        with patch.object(sys, "argv", ["edge_tts_generate.py", "--help"]):
            with self.assertRaises(SystemExit) as exit_info:
                MODULE.parse_args()

        self.assertEqual(exit_info.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
