#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/Yixuan-Wang/khep.git"
CODEX_ALLOWED_FRONTMATTER_KEYS = {
    "allowed-tools",
    "description",
    "license",
    "metadata",
    "name",
}


def default_skills_dest(target: str) -> Path:
    if target == "codex":
        codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
        return codex_home / "skills"
    return Path.home() / ".claude" / "skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install all Khep skills.")
    parser.add_argument(
        "--target",
        choices=("claude", "codex"),
        default="claude",
        help="Skill host to install for. Defaults to claude.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        help="Override the destination skills directory.",
    )
    return parser.parse_args()


def strip_unsupported_frontmatter_keys(
    content: str,
    allowed_keys: set[str],
) -> tuple[str, list[str]]:
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return content, []

    closing_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return content, []

    stripped_keys: list[str] = []
    sanitized_lines = [lines[0]]
    skip_current_value = False

    for line in lines[1:closing_index]:
        if line[:1] in (" ", "\t") or not line.strip():
            if not skip_current_value:
                sanitized_lines.append(line)
            continue

        key, separator, _value = line.partition(":")
        if not separator:
            if not skip_current_value:
                sanitized_lines.append(line)
            continue

        key = key.strip().strip("\"'")
        skip_current_value = key not in allowed_keys
        if skip_current_value:
            stripped_keys.append(key)
            continue

        sanitized_lines.append(line)

    sanitized_lines.extend(lines[closing_index:])
    return "".join(sanitized_lines), stripped_keys


def sanitize_codex_skill(skill_dir: Path) -> list[str]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return []

    content = skill_md.read_text()
    sanitized_content, stripped_keys = strip_unsupported_frontmatter_keys(
        content,
        CODEX_ALLOWED_FRONTMATTER_KEYS,
    )
    if stripped_keys:
        skill_md.write_text(sanitized_content)

    return stripped_keys


def main() -> None:
    args = parse_args()
    skills_dest = args.dest or default_skills_dest(args.target)
    skills_dest.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        clone_path = Path(tmp) / "khep"
        subprocess.run(
            ["git", "clone", "--depth=1", REPO_URL, str(clone_path)],
            check=True,
        )

        skills_src = clone_path / "skills"
        count_skills = 0
        for skill_dir in sorted(skills_src.iterdir()):
            if not skill_dir.is_dir():
                continue
            dest = skills_dest / skill_dir.name
            is_reinstall = dest.exists()
            if is_reinstall:
                shutil.rmtree(dest)

            shutil.copytree(skill_dir, dest)
            stripped_keys = []
            if args.target == "codex":
                stripped_keys = sanitize_codex_skill(dest)

            count_skills += 1
            target_label = args.target.capitalize()
            if is_reinstall:
                print(f"Reinstalled for {target_label}: {skill_dir.name}")
            else:
                print(f"Installed for {target_label}: {skill_dir.name}")
            if stripped_keys:
                stripped_keys_text = ", ".join(stripped_keys)
                print(
                    f"  Stripped Codex-incompatible frontmatter: {stripped_keys_text}"
                )

    print(f"\nDone. {count_skills} skill(s) installed to {skills_dest}")


if __name__ == "__main__":
    main()
