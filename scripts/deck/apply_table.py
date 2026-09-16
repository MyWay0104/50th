"""문구·배치 치환 표(JSON Lines)를 index.html 에 적용한다.

덱 전체를 한 번에 고칠 때 쓴다. 서브에이전트는 표만 만들고, 실제 수정은 이 스크립트가 한다.
`old` 는 그 장면 안에서 정확히 한 번 나와야 하며, 하나라도 어긋나면 그 항목만 건너뛰고 보고한다.
`--dry` 로 먼저 확인한 뒤 적용한다.

표 형식 (한 줄에 장면 하나):
  문구(copy):  {"sid": "S09", "title": "새 제목", "source": "출처: …", "replace": [{"where": "screen|note", "old": "…", "new": "…"}]}
               title·source 는 생략하거나 null 이면 그대로, source 가 "" 면 출처 줄 삭제
  배치(visual): {"sid": "S09", "old": "<div …>", "new": "<div …>"}   (노트 앞부분에서만 치환)

사용:
    python scripts/deck/apply_table.py topics/<topic>/index.html copy_B1.jsonl --kind copy --dry
    python scripts/deck/apply_table.py topics/<topic>/index.html visual_spec.jsonl --kind visual --css visual_spec.css
"""
from __future__ import annotations

import argparse
import json
import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

TITLE_RES = (
    re.compile(r'(<h2 class="scene-title"[^>]*>)(.*?)(</h2>)', re.S),
    re.compile(r'(<h1 class="hero-title"[^>]*>)(.*?)(</h1>)', re.S),
)
SOURCE_RE = re.compile(r'(<p class="source"[^>]*>)(.*?)(</p>)', re.S)
NOTE_MARK = '<aside class="speaker-note">'


def find_scene(index_html: str, sid: str) -> re.Match[str] | None:
    """장면 section 을 찾는다."""
    return re.search(rf'<section [^>]*data-scene-id="{re.escape(sid)}".*?</section>', index_html, re.S)


def split_note(scene: str) -> tuple[str, str]:
    """장면을 화면 부분과 발표자 노트로 나눈다."""
    cut = scene.find(NOTE_MARK)
    return (scene[:cut], scene[cut:]) if cut >= 0 else (scene, "")


def apply_copy(scene: str, item: dict, misses: list[str]) -> str:
    """문구 표 한 줄을 장면에 적용한다."""
    sid = item["sid"]
    head, note = split_note(scene)
    for index, rule in enumerate(item.get("replace") or []):
        old, new, where = rule["old"], rule["new"], rule.get("where", "screen")
        part = note if where == "note" else head
        if part.count(old) != 1:
            misses.append(f"{sid} replace[{index}] {where} {part.count(old)}회: {old[:40]}")
            continue
        if where == "note":
            note = note.replace(old, new)
        else:
            head = head.replace(old, new)
    title = item.get("title")
    if title:
        for regex in TITLE_RES:
            if regex.search(head):
                head = regex.sub(lambda m: m.group(1) + title + m.group(3), head, count=1)
                break
        else:
            misses.append(f"{sid}: 제목 요소가 없다")
    source = item.get("source")
    if source is not None:
        if source == "":
            head, count = re.subn(r'\n[ \t]*<p class="source"[^>]*>.*?</p>', "", head, count=1, flags=re.S)
            if not count:
                misses.append(f"{sid}: 지울 출처 줄이 없다")
        elif SOURCE_RE.search(head):
            head = SOURCE_RE.sub(lambda m: m.group(1) + source + m.group(3), head, count=1)
        else:
            indent = re.search(r"\n([ \t]*)<aside", scene)
            pad = indent.group(1) if indent else "  "
            head = head.rstrip() + f'\n{pad}<p class="source" data-editable="true">{source}</p>\n{pad}'
    return head + note


def apply_visual(scene: str, item: dict, misses: list[str], topic_dir: Path) -> str:
    """배치 표 한 줄을 장면의 화면 부분에 적용한다."""
    sid, old, new = item["sid"], item["old"], item["new"]
    if re.search(r'\sstyle="|#[0-9a-fA-F]{3,6}\b|<br', new):
        misses.append(f"{sid}: new 에 인라인 style·hex·<br> 가 있다")
        return scene
    missing = [src for src in re.findall(r'src="([^"]+)"', new) if not (topic_dir / src).exists()]
    if missing:
        misses.append(f"{sid}: 없는 파일 {missing}")
        return scene
    head, note = split_note(scene)
    if head.count(old) != 1:
        misses.append(f"{sid}: old {head.count(old)}회")
        return scene
    return head.replace(old, new) + note


def append_css(index_html: str, css: str) -> str:
    """scene-styles 끝에 CSS 블록을 붙인다."""
    start = index_html.index('id="scene-styles"')
    end = index_html.index("</style>", start)
    line_start = index_html.rfind("\n", 0, end) + 1
    body = "".join(f"      {line}\n" if line.strip() else "\n" for line in css.strip("\n").splitlines())
    return index_html[:line_start] + body + index_html[line_start:]


def main() -> None:
    """표를 읽어 적용하고 못 찾은 항목을 보고한다."""
    parser = argparse.ArgumentParser(description="치환 표 적용")
    parser.add_argument("index", type=Path, help="topics/<topic>/index.html")
    parser.add_argument("tables", type=Path, nargs="+", help="치환 표 JSONL (여러 개면 순서대로)")
    parser.add_argument("--kind", choices=("copy", "visual"), default="copy")
    parser.add_argument("--css", type=Path, default=None, help="함께 붙일 CSS 파일(배치 표와 같이 쓴다)")
    parser.add_argument("--dry", action="store_true", help="파일을 쓰지 않고 확인만")
    args = parser.parse_args()

    index_html = args.index.read_text(encoding="utf-8")
    topic_dir = args.index.parent
    misses: list[str] = []
    applied = 0
    for table in args.tables:
        for line in table.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            match = find_scene(index_html, item["sid"])
            if not match:
                misses.append(f"{item['sid']}: 장면이 없다")
                continue
            scene = match.group(0)
            new_scene = apply_copy(scene, item, misses) if args.kind == "copy" else apply_visual(scene, item, misses, topic_dir)
            index_html = index_html[:match.start()] + new_scene + index_html[match.end():]
            applied += 1
    if args.css and not args.dry:
        index_html = append_css(index_html, args.css.read_text(encoding="utf-8"))
    if not args.dry:
        args.index.write_text(index_html, encoding="utf-8", newline="\n")
    logger.info("장면 %d개 처리, 못 찾음 %d건%s", applied, len(misses), " (dry)" if args.dry else "")
    for miss in misses:
        logger.info("  %s", miss)


if __name__ == "__main__":
    main()
