from __future__ import annotations

import logging
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".codex" / "agents"
SKILL_DIR = ROOT / ".agents" / "skills"
WORKSPACE_DIR = ROOT / "_workspace"

REQUIRED_AGENT_FIELDS = ("name", "description", "developer_instructions")
REQUIRED_SKILL_FIELDS = ("name", "description")

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _check_agent(path: Path) -> list[str]:
    text = _read_text(path)
    errors: list[str] = []
    try:
        tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"{path}: invalid TOML: {exc}")

    for field in REQUIRED_AGENT_FIELDS:
        if not re.search(rf"(?m)^{field}\s*=", text):
            errors.append(f"{path}: missing {field}")

    for marker in ("Role:", "Input:", "Process:", "Output:", "Quality checks:", "Handoff path:"):
        if marker not in text:
            errors.append(f"{path}: developer_instructions missing {marker}")

    return errors


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}

    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def _check_skill(path: Path) -> list[str]:
    text = _read_text(path)
    data = _frontmatter(text)
    errors: list[str] = []
    for field in REQUIRED_SKILL_FIELDS:
        if not data.get(field):
            errors.append(f"{path}: missing frontmatter {field}")
    return errors


def _check_required_paths() -> list[str]:
    errors: list[str] = []
    for path in (AGENT_DIR, SKILL_DIR, WORKSPACE_DIR):
        if not path.exists():
            errors.append(f"{path}: required path does not exist")
    if not (WORKSPACE_DIR / "orchestration-plan.md").exists():
        errors.append("_workspace/orchestration-plan.md: missing orchestration plan")
    return errors


def main() -> int:
    errors = _check_required_paths()

    if AGENT_DIR.exists():
        agent_files = sorted(AGENT_DIR.glob("*.toml"))
        if not agent_files:
            errors.append(".codex/agents: no agent TOML files found")
        for path in agent_files:
            errors.extend(_check_agent(path))

    if SKILL_DIR.exists():
        skill_files = sorted(SKILL_DIR.glob("*/SKILL.md"))
        if not skill_files:
            errors.append(".agents/skills: no SKILL.md files found")
        for path in skill_files:
            errors.extend(_check_skill(path))

    if errors:
        logger.error("Codex harness validation failed:")
        for error in errors:
            logger.error("- %s", error)
        return 1

    logger.info("Codex harness validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
