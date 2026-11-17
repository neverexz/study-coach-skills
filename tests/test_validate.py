"""Repository checks catch broken installable packages, not teaching quality."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


VALIDATOR = Path(__file__).resolve().parents[1] / "tools" / "validate.py"


class ValidateRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repository"
        self.lesson = self.root / "skills" / "lesson"
        self.lesson.mkdir(parents=True)
        self.entrypoint = self.lesson / "SKILL.md"
        self.entrypoint.write_text(
            "---\nname: lesson\ndescription: Use when studying a supplied lesson.\n---\n"
            "# Lesson\n\nExplain the selected passage.\n",
            encoding="utf-8",
        )

    def run_check(self, root=None):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(root or self.root)],
            cwd=self.temp.name,
            text=True,
            capture_output=True,
        )

    def assert_invalid(self):
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def test_valid_package_can_move_and_be_checked_from_other_directory(self):
        moved = Path(self.temp.name) / "moved repository"
        shutil.copytree(self.root, moved)
        result = self.run_check(moved)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_frontmatter_is_reported(self):
        self.entrypoint.write_text("# Lesson\nNo metadata.\n")
        self.assertIn("SKILL.md", self.assert_invalid())

    def test_wrong_folder_name_is_reported(self):
        self.entrypoint.write_text(self.entrypoint.read_text().replace("name: lesson", "name: other"))
        self.assertIn("name", self.assert_invalid())

    def test_duplicate_yaml_keys_are_rejected(self):
        self.entrypoint.write_text(self.entrypoint.read_text().replace("name: lesson", "name: lesson\nname: lesson"))
        self.assertIn("duplicate", self.assert_invalid().lower())

    def test_empty_description_is_rejected(self):
        self.entrypoint.write_text(self.entrypoint.read_text().replace("Use when studying a supplied lesson.", "''"))
        self.assertIn("description", self.assert_invalid())

    def test_missing_local_reference_is_reported(self):
        with self.entrypoint.open("a") as stream:
            stream.write("\nRead [rubric](references/rubric.md).\n")
        self.assertIn("rubric.md", self.assert_invalid())

    def test_reference_outside_installable_skills_is_rejected(self):
        outside = self.root / "private.md"
        outside.write_text("This file will not be installed.\n")
        with self.entrypoint.open("a") as stream:
            stream.write("\nRead [private](../../private.md).\n")
        self.assertIn("private.md", self.assert_invalid())

    def test_encoded_sibling_reference_and_anchor_are_supported(self):
        reference = self.root / "skills" / "progress" / "references" / "state format.md"
        reference.parent.mkdir(parents=True)
        reference.write_text("# State\n")
        (reference.parents[1] / "SKILL.md").write_text(
            "---\nname: progress\ndescription: Use when resuming.\n---\n# Progress\n"
        )
        with self.entrypoint.open("a") as stream:
            stream.write("\nRead [state](../progress/references/state%20format.md#state).\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_malformed_example_json_is_reported(self):
        example = self.lesson / "references" / "example.json"
        example.parent.mkdir()
        example.write_text('{"invalid": }')
        self.assertIn("example.json", self.assert_invalid())

    def test_invalid_yaml_type_is_reported(self):
        self.entrypoint.write_text("---\n- lesson\n---\n# Lesson\n")
        self.assert_invalid()

    def test_directory_without_entrypoint_is_reported(self):
        self.entrypoint.unlink()
        self.assertIn("SKILL.md", self.assert_invalid())

    def test_external_links_and_code_examples_do_not_require_local_files(self):
        with self.entrypoint.open("a") as stream:
            stream.write("\n[Source](https://example.test/source#part)\n")
            stream.write("\n```markdown\n[example](not-a-real-file.md)\n```\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
