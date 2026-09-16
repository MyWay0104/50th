"""덱의 화면 글자와 발표자 노트를 한 파일로 뽑는다.

검토 서브에이전트에게 원문을 통째로 읽히지 않고 정리본만 주기 위해 쓴다.

사용:
    python scripts/deck/dump_deck_text.py topics/<topic> -o _workspace/<topic>-text.md
"""
from __future__ import annotations

import argparse
import html
import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

SECTION_RE = re.compile(r'<section [^>]*data-scene-id="([^"]+)"[^>]*data-skill="([^"]*)"?.*?</section>', re.S)
SCENE_RE = re.compile(r'<section ([^>]*)>(.*?)</section>', re.S)
NOTE_RE = re.compile(r'<aside class="speaker-note">(.*?)</aside>', re.S)


def clean(markup: str) -> str:
    """태그를 지우고 공백을 정리한다."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", markup))).strip()


def main() -> None:
    """장면마다 쪽번호·장면 ID·화면 글자·노트를 적는다."""
    parser = argparse.ArgumentParser(description="덱 본문 추출")
    parser.add_argument("topic", type=Path, help="topics/<topic> 폴더 또는 index.html")
    parser.add_argument("-o", "--out", type=Path, required=True, help="저장할 마크다운 경로")
    args = parser.parse_args()

    index_path = args.topic if args.topic.suffix == ".html" else args.topic / "index.html"
    index_html = index_path.read_text(encoding="utf-8")
    body = index_html[index_html.index("<body"):]
    lines = [f"# {index_path.parent.name} — 화면 글자와 발표자 노트", ""]
    scenes = SCENE_RE.findall(body)
    for number, (attrs, inner) in enumerate([s for s in scenes if 'class="scene' in s[0]], 1):
        sid = (re.search(r'data-scene-id="([^"]+)"', attrs) or re.search("(x)", "x")).group(1)
        skill = (re.search(r'data-skill="([^"]+)"', attrs) or re.search("(x)", "x")).group(1)
        note_match = NOTE_RE.search(inner)
        note = note_match.group(1) if note_match else ""
        head = inner[: note_match.start()] if note_match else inner
        screen = clean(head).replace(f"{number} / {len(scenes)}", "").strip()
        lines += [f"## {number}쪽 · {sid} · data-skill {skill}", "", f"- 화면: {screen}", f"- 노트: {clean(note)}", ""]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines), encoding="utf-8")
    logger.info("%d장 → %s (%d자)", number, args.out, args.out.stat().st_size)


if __name__ == "__main__":
    main()
