"""장면 ID ↔ HTML 순번 매핑표를 index.html 에서 만든다.

기획 문서의 매핑표를 손으로 고치면 실제 파일과 어긋나므로, 항상 이 스크립트로 다시 만든다.

사용:
    python scripts/deck/scene_map.py topics/<topic> -o _workspace/scene-map.md
"""
from __future__ import annotations

import argparse
import html as htmlmod
import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

SECTION_RE = re.compile(r'(<section id="(s-\d+)" class="scene[^"]*" data-skill="([^"]+)" data-scene-id="([^"]+)".*?</section>)', re.S)
TITLE_RE = re.compile(r'<h[12] class="[^"]*(?:scene-title|hero-title)[^"]*"[^>]*>(.*?)</h[12]>', re.S)
CHIP_RE = re.compile(r'class="block-chip"[^>]*>([^<]+)<')


def main() -> None:
    """순번·id·장면 ID·data-skill·블록·제목 표를 만든다."""
    parser = argparse.ArgumentParser(description="장면 매핑표 생성")
    parser.add_argument("topic", type=Path, help="topics/<topic> 폴더 또는 index.html")
    parser.add_argument("-o", "--out", type=Path, default=None, help="저장 경로(없으면 화면 출력)")
    args = parser.parse_args()

    index_path = args.topic if args.topic.suffix == ".html" else args.topic / "index.html"
    text = index_path.read_text(encoding="utf-8")
    rows = ["| 순번 | HTML id | 장면 ID | data-skill | 블록 | 제목 |", "|---:|---|---|---|---|---|"]
    for number, (scene, node_id, skill, scene_id) in enumerate(SECTION_RE.findall(text), 1):
        title_match = TITLE_RE.search(scene)
        title = htmlmod.unescape(re.sub(r"<[^>]+>", "", title_match.group(1))).strip() if title_match else "-"
        chip = CHIP_RE.search(scene)
        rows.append(f"| {number} | {node_id} | {scene_id} | `{skill}` | {chip.group(1).strip() if chip else '-'} | {title} |")
    table = "\n".join(rows) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(table, encoding="utf-8")
        logger.info("%d행 → %s", len(rows) - 2, args.out)
    else:
        logger.info(table)


if __name__ == "__main__":
    main()
