"""index.html 의 BLOCK 구간을 조각 파일로 바꾸거나 꺼낸다.

index.html 에 `<!-- BLOCK:B2 START -->` … `<!-- BLOCK:B2 END -->` 주석이 있는 topic 에서 쓴다.
묶음(차수) 단위로 다시 만들 때, 빌더는 조각 파일만 만들고 조립은 이 스크립트가 한다.

사용:
    python scripts/deck/splice_blocks.py topics/<topic>/index.html blocks B2 B3
    python scripts/deck/splice_blocks.py topics/<topic>/index.html blocks B2 --extract
"""
from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def block_span(index_html: str, name: str) -> tuple[int, int]:
    """BLOCK 주석 사이의 시작·끝 위치를 돌려준다."""
    start = re.search(rf"<!--\s*BLOCK:{re.escape(name)}\s+START\s*-->", index_html)
    end = re.search(rf"<!--\s*BLOCK:{re.escape(name)}\s+END\s*-->", index_html)
    if not start or not end or end.start() < start.end():
        raise SystemExit(f"BLOCK:{name} 주석을 찾지 못했다.")
    return start.end(), end.start()


def main() -> None:
    """조각을 끼우거나(--extract 면) 꺼낸다."""
    parser = argparse.ArgumentParser(description="BLOCK 조각 조립·추출")
    parser.add_argument("index", type=Path, help="topics/<topic>/index.html")
    parser.add_argument("blocks_dir", type=Path, help="조각 파일 폴더")
    parser.add_argument("names", nargs="+", help="BLOCK 이름 (예: B2 B3 APP)")
    parser.add_argument("--extract", action="store_true", help="index 에서 조각을 꺼내 파일로 저장")
    args = parser.parse_args()

    index_html = args.index.read_text(encoding="utf-8")
    args.blocks_dir.mkdir(parents=True, exist_ok=True)
    for name in args.names:
        start, end = block_span(index_html, name)
        target = args.blocks_dir / f"{name}.html"
        if args.extract:
            target.write_text(index_html[start:end].strip("\n") + "\n", encoding="utf-8")
            logger.info("BLOCK:%s 추출 → %s (%d자)", name, target, end - start)
            continue
        fragment = target.read_text(encoding="utf-8").strip("\n")
        index_html = index_html[:start] + "\n" + fragment + "\n      " + index_html[end:]
        logger.info("BLOCK:%s 교체 (%d자)", name, len(fragment))
    if not args.extract:
        args.index.write_text(index_html, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
