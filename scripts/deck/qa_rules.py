"""덱의 사내 하우스 룰을 정적으로 검사한다.

`hyperframes check` 가 보는 것(레이아웃 겹침·런타임 오류·명암비)과 겹치지 않는, 우리 교육에만 있는 규칙만 본다.
규칙은 JSON 파일로 준다(`--rules`). 파일이 없으면 아무 검사도 하지 않고 구조 요약만 출력한다.

규칙 파일 예: scripts/deck/rules.sk-hynix.json

사용:
    python scripts/deck/qa_rules.py topics/<topic> --rules topics/<topic>/deck-rules.json
"""
from __future__ import annotations

import argparse
import html
import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

SECTION_RE = re.compile(r'<section [^>]*data-scene-id="([^"]+)"(.*?)</section>', re.S)
NOTE_RE = re.compile(r'<aside class="speaker-note">(.*?)</aside>', re.S)
SOURCE_RE = re.compile(r'<p class="source"[^>]*>(.*?)</p>', re.S)
VISUAL_RE = re.compile(r'<img |class="dg|class="data-table|class="code-card|class="placeholder|class="steps|class="compare-grid|class="time-blocks|class="dist|class="quote-points')


def plain_text(markup: str) -> str:
    """태그와 코드 블록을 지운 글자만 남긴다."""
    without_code = re.sub(r"<pre[^>]*>.*?</pre>", " ", markup, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", without_code)))


def main() -> int:
    """규칙 위반 수를 종료 코드로 돌려준다."""
    parser = argparse.ArgumentParser(description="덱 하우스 룰 검사")
    parser.add_argument("topic", type=Path, help="topics/<topic> 폴더 또는 index.html")
    parser.add_argument("--rules", type=Path, default=None, help="규칙 JSON")
    args = parser.parse_args()

    index_path = args.topic if args.topic.suffix == ".html" else args.topic / "index.html"
    index_html = index_path.read_text(encoding="utf-8")
    rules = json.loads(args.rules.read_text(encoding="utf-8")) if args.rules else {}
    scenes = SECTION_RE.findall(index_html)
    logger.info("장면 %d개 · %s", len(scenes), index_path)

    violations: list[str] = []
    counts: dict[str, int] = {}
    for sid, body in scenes:
        note_match = NOTE_RE.search(body)
        note = note_match.group(1) if note_match else ""
        head = body[: body.find('<aside class="speaker-note">')] if note_match else body
        screen = plain_text(head)
        sources = " ".join(SOURCE_RE.findall(head))
        for rule in rules.get("forbidden_patterns", []):
            if sid in rule.get("except_scenes", []):
                continue
            target = {"screen": screen, "note": plain_text(note), "source": plain_text(sources)}[rule.get("where", "screen")]
            found = re.findall(rule["pattern"], target)
            if found:
                counts[rule["name"]] = counts.get(rule["name"], 0) + len(found)
                violations.append(f"{sid} · {rule['name']} {len(found)}건: {found[0] if isinstance(found[0], str) else found[0][0]}")
        if rules.get("require_visual", True) and not VISUAL_RE.search(head):
            violations.append(f"{sid} · 시각 요소(이미지·도식·표·코드)가 없다")
    for name, pattern in (rules.get("forbidden_markup") or {}).items():
        hits = len(re.findall(pattern, index_html))
        if hits:
            counts[name] = hits
            violations.append(f"마크업 · {name} {hits}건")

    if counts:
        logger.info("위반 요약: %s", ", ".join(f"{k} {v}" for k, v in counts.items()))
    if violations:
        logger.info("위반 %d건", len(violations))
        for item in violations[:60]:
            logger.info("  %s", item)
        return 1
    logger.info("결과: 위반 0건")
    return 0


if __name__ == "__main__":
    sys.exit(main())
