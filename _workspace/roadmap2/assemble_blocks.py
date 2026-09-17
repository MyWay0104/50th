"""빌더가 만든 조각(P1~P4, APP)을 index.html 의 BLOCK 구간에 끼운다.

기존 BLOCK 구간(AM1 · AM2 · PM · APP)을 통째로 들어내고, 새 BLOCK 주석 5쌍과 조각 내용을 넣는다.
조립 뒤에는 반드시 `python scripts/sync_overview.py <topic> --renumber` 로 순번을 다시 매긴다.

사용법: python _workspace/roadmap2/assemble_blocks.py <index.html> <blocks 폴더>
"""
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("assemble_blocks")

NEW_BLOCKS = ["P1", "P2", "P3", "P4", "APP"]
REGION_RE = re.compile(r"[ \t]*<!-- BLOCK:\w+ START -->.*<!-- BLOCK:\w+ END -->[ \t]*\n", re.S)
SECTION_RE = re.compile(r'<section\b[^>]*class="scene\b', re.S)


def main(index_path: str, blocks_dir: str) -> None:
    """BLOCK 구간 전체를 새 조각으로 바꾼다."""
    index = Path(index_path)
    html = index.read_text(encoding="utf-8")
    region = REGION_RE.search(html)
    if region is None:
        raise SystemExit("BLOCK 구간을 찾지 못했습니다")

    parts = []
    total = 0
    for name in NEW_BLOCKS:
        fragment = (Path(blocks_dir) / f"{name}.html").read_text(encoding="utf-8").strip("\n")
        count = len(SECTION_RE.findall(fragment))
        total += count
        log.info("BLOCK %s: 장면 %d개", name, count)
        parts.append(f"      <!-- BLOCK:{name} START -->\n{fragment}\n      <!-- BLOCK:{name} END -->\n")

    html = html[: region.start()] + "".join(parts) + html[region.end():]
    index.write_text(html, encoding="utf-8", newline="\n")
    log.info("조립 완료: 장면 %d개 → %s", total, index)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
