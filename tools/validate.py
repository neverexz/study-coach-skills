"""Check installable skill metadata, bundled references and example JSON offline."""

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


class UniqueKeysLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in result:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate YAML key: {key}", key_node.start_mark
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def prose_lines(text):
    """Fenced examples are illustrative, not resource dependencies."""
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, suffix = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            yield line


def validate_repository(root: Path) -> list[str]:
    skills = (root / "skills").resolve()
    errors = []
    packages = sorted(p for p in skills.iterdir() if p.is_dir()) if skills.is_dir() else []
    if not packages:
        return [f"{skills}: no skill packages found"]

    for package in packages:
        entrypoint = package / "SKILL.md"
        try:
            content = entrypoint.read_text(encoding="utf-8")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL)
            if not match:
                errors.append(f"{entrypoint}: missing YAML frontmatter")
            else:
                metadata = yaml.load(match.group(1), Loader=UniqueKeysLoader)
                if not isinstance(metadata, dict):
                    errors.append(f"{entrypoint}: frontmatter must be a mapping")
                else:
                    name = metadata.get("name")
                    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != package.name:
                        errors.append(f"{entrypoint}: name must match its hyphen-case folder")
                    description = metadata.get("description")
                    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                        errors.append(f"{entrypoint}: description must be nonempty text, at most 1024 characters")
        except (OSError, UnicodeError, yaml.YAMLError, TypeError) as exc:
            errors.append(f"{entrypoint}: {exc}")

        for document in package.rglob("*.md"):
            try:
                for line in prose_lines(document.read_text(encoding="utf-8")):
                    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
                        url = urlsplit(target.strip().strip("<>"))
                        if url.scheme in {"https", "http", "mailto"} or not url.path:
                            continue
                        destination = (document.parent / unquote(url.path)).resolve()
                        if url.scheme or url.netloc or not destination.is_relative_to(skills) or not destination.exists():
                            errors.append(f"{document}: missing or unbundled reference {target}")
            except (OSError, UnicodeError, ValueError) as exc:
                errors.append(f"{document}: {exc}")

        for example in package.rglob("*.json"):
            try:
                json.loads(example.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, ValueError) as exc:
                errors.append(f"{example}: invalid JSON: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root)
    if errors:
        print("\n".join(errors))
        return 1
    print("Skill metadata, bundled references and example JSON are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
