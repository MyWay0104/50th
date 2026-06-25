from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path


DECK_SKILLS = {
    "title",
    "title-bullets",
    "title-image",
    "title-tags",
    "split",
    "stat",
    "steps",
    "compare",
    "evolution-flow",
    "quote",
    "kindergarten-notice",
}

CARD_NEWS_SKILLS = {
    "photo-cover",
    "video-cover",
    "stat",
    "image-feature",
}

REQUIRED_TOPIC_FILES = ("index.html", "overview.html", "meta.json", "hyperframes.json", "DESIGN.md")
REQUIRED_TOPIC_DIRS = ("exports",)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _detect_output_type(index_html: str) -> str:
    if 'data-output-type="card-news"' in index_html:
        return "card-news"
    return "deck"


def _extract_skills(html: str) -> set[str]:
    return set(re.findall(r'data-skill="([^"]+)"', html))


def validate_topic(topic_path: Path) -> list[str]:
    errors: list[str] = []
    if not topic_path.exists():
        return [f"{topic_path}: topic path does not exist"]

    for filename in REQUIRED_TOPIC_FILES:
        if not (topic_path / filename).exists():
            errors.append(f"{topic_path / filename}: required file missing")

    for dirname in REQUIRED_TOPIC_DIRS:
        if not (topic_path / dirname).is_dir():
            errors.append(f"{topic_path / dirname}: required directory missing")

    index_path = topic_path / "index.html"
    overview_path = topic_path / "overview.html"
    if not index_path.exists() or not overview_path.exists():
        return errors

    index_html = _read(index_path)
    overview_html = _read(overview_path)
    output_type = _detect_output_type(index_html)
    allowed = CARD_NEWS_SKILLS if output_type == "card-news" else DECK_SKILLS
    invalid_skills = sorted(_extract_skills(index_html) - allowed)

    if invalid_skills:
        errors.append(f"{index_path}: invalid data-skill values for {output_type}: {', '.join(invalid_skills)}")
    if 'class="edit-btn"' not in overview_html:
        errors.append(f"{overview_path}: missing class=\"edit-btn\"")
    if "Aim" not in overview_html and "data-aim" not in overview_html:
        errors.append(f"{overview_path}: missing Aim UI or data-aim")
    if '[data-editable="true"]' not in overview_html and 'data-editable="true"' not in overview_html:
        errors.append(f"{overview_path}: missing editable fields")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a HyperFrames topic folder.")
    parser.add_argument("topic", type=Path, help="Path to topics/<topic-name>")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_topic(args.topic)
    if errors:
        logger.error("Topic validation failed:")
        for error in errors:
            logger.error("- %s", error)
        return 1

    logger.info("Topic validation passed: %s", args.topic)
    return 0


if __name__ == "__main__":
    sys.exit(main())
