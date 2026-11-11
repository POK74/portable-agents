"""Validate portable agent manifests without provider credentials."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "agents"
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def validate_agent(directory: Path) -> list[str]:
    errors = []
    manifest_path = directory / "agent.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{manifest_path}: {exc}"]
    if not isinstance(manifest, dict):
        return [f"{manifest_path}: expected a JSON object"]
    if not SLUG.fullmatch(directory.name) or manifest.get("id") != directory.name:
        errors.append(f"{manifest_path}: id must match the lowercase directory slug")
    for field in ("name", "version", "description"):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            errors.append(f"{manifest_path}: {field} must be a nonempty string")
    instructions = manifest.get("instructions")
    if instructions != "instructions.md" or not (directory / "instructions.md").is_file():
        errors.append(f"{manifest_path}: instructions must refer to an existing instructions.md")
    return errors


def validate_all(root: Path = AGENTS) -> list[str]:
    if not root.is_dir():
        return [f"{root}: missing agents directory"]
    directories = sorted(path for path in root.iterdir() if path.is_dir())
    if not directories:
        return [f"{root}: no agents found"]
    return [error for directory in directories for error in validate_agent(directory)]


if __name__ == "__main__":
    problems = validate_all()
    if problems:
        print("\n".join(problems))
        raise SystemExit(1)
    print("All agent manifests are valid.")
