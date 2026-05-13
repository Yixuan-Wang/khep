#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/Yixuan-Wang/khep.git"
SKILLS_DEST = Path.home() / ".claude" / "skills"


def main() -> None:
    SKILLS_DEST.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        clone_path = Path(tmp) / "khep"
        clone_result = subprocess.run(
            ["git", "clone", "--depth=1", REPO_URL, str(clone_path)],
            check=True,
        )
    
        skills_src = clone_path / "skills"
        count_skills = 0
        for skill_dir in sorted(skills_src.iterdir()):
            if not skill_dir.is_dir():
                continue
            dest = SKILLS_DEST / skill_dir.name
            is_reinstall = dest.exists()
            if is_reinstall:
                shutil.rmtree(dest)

            shutil.copytree(skill_dir, dest)
            count_skills += 1
            if is_reinstall:
                print(f"Reinstalled: {skill_dir.name}")
            else:
                print(f"Installed: {skill_dir.name}")

    print(f"\nDone. {count_skills} skill(s) installed to {SKILLS_DEST}")


if __name__ == "__main__":
    main()
