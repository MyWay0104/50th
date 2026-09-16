"""BLOCK 조각 파일이 덱 규약을 지키는지 검사한다.

빌더 서브에이전트가 만든 `<section class="scene ...">` 조각을 index.html 에 끼우기 전에 확인한다.
검사 항목: 장면 ID 순서, 허용 data-skill, 필수 요소, 금지 마크업(인라인 style·br·hex·외부 이미지),
CSS 에 없는 클래스, data-editable 누락, 금지 문자열(사내 규칙 파일).

사용:
    python scripts/deck/check_fragment.py topics/<topic>/index.html blocks/B2.html --ids S09 S10 S11
    python scripts/deck/check_fragment.py topics/<topic>/index.html blocks/B2.html --rules topics/<topic>/deck-rules.json
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

ALLOWED_SKILLS = {
    "title", "title-bullets", "title-image", "title-tags", "split", "stat",
    "steps", "compare", "evolution-flow", "quote", "kindergarten-notice",
    "photo-cover", "video-cover", "image-feature",
}
SECTION_RE = re.compile(r'<section\b[^>]*class="scene\b[^"]*"[^>]*>.*?</section>', re.S)
SCENE_ID_RE = re.compile(r'data-scene-id="([^"]+)"')
SKILL_RE = re.compile(r'data-skill="([^"]+)"')
# span·div 는 편집 대상 요소 안의 조각인 경우가 많아 data-editable 검사에서 뺀다
TEXT_LEAF_RE = re.compile(r"<(p|h1|h2|h3|li|td|th)\b([^>]*)>([^<>]*[가-힣A-Za-z0-9][^<>]*)</\1>")
# HyperFrames 런타임이 쓰는 클래스라 CSS 에 없어도 된다
RUNTIME_CLASSES = {"clip"}


def load_rules(path: Path | None) -> dict:
    """사내 규칙 파일을 읽는다. 없으면 빈 규칙."""
    if not path:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def defined_classes(index_html: str) -> set[str]:
    """index.html 의 scene-styles 에 정의된 클래스 이름을 모은다."""
    match = re.search(r'<style id="scene-styles">(.*?)</style>', index_html, re.S)
    if not match:
        raise SystemExit("index.html 에 <style id=\"scene-styles\"> 가 없다.")
    return set(re.findall(r"\.([a-zA-Z][\w-]*)", match.group(1)))


def check_scene(scene: str, css_classes: set[str], rules: dict, problems: list[str]) -> None:
    """장면 하나를 검사해 문제를 problems 에 담는다."""
    sid = (SCENE_ID_RE.search(scene) or re.match("", "")).group(1) if SCENE_ID_RE.search(scene) else "?"
    skill_match = SKILL_RE.search(scene)
    if not skill_match or skill_match.group(1) not in ALLOWED_SKILLS:
        problems.append(f"{sid}: data-skill 이 없거나 허용값이 아니다({skill_match.group(1) if skill_match else '없음'})")
    if '<aside class="speaker-note">' not in scene:
        problems.append(f"{sid}: 발표자 노트(.speaker-note)가 없다")
    for pattern, message in (
        (r"\sstyle=\"", "인라인 style 속성"),
        (r"<br\s*/?>", "<br> 태그"),
        (r'src="https?://', "외부 URL 이미지"),
        (r"#[0-9a-fA-F]{3,6}\b(?![^<]*</pre>)", "마크업 안 hex 색"),
    ):
        if re.search(pattern, scene):
            problems.append(f"{sid}: {message}")
    for img in re.findall(r"<img\b[^>]*>", scene):
        if 'alt="' not in img:
            problems.append(f"{sid}: alt 없는 이미지 {img[:60]}")
    allowed = css_classes | RUNTIME_CLASSES | set(rules.get("allow_classes", []))
    for cls in {c for attr in re.findall(r'class="([^"]+)"', scene) for c in attr.split()}:
        if cls not in allowed:
            problems.append(f"{sid}: CSS 에 없는 클래스 .{cls}")
    # 코드 블록 안 글자는 pre 자체가 편집 대상이라 검사에서 뺀다
    scene_no_code = re.sub(r"<pre[^>]*>.*?</pre>", " ", scene, flags=re.S)
    for tag, attrs, text in TEXT_LEAF_RE.findall(scene_no_code):
        if text.strip() and "data-editable" not in attrs and "aria-hidden" not in attrs:
            problems.append(f"{sid}: data-editable 없는 글자 <{tag}>{text.strip()[:20]}")
    for word in rules.get("forbidden_strings", []):
        if word in scene:
            problems.append(f"{sid}: 금지 문자열 {word!r}")


def main() -> int:
    """조각 파일을 검사하고 문제 수를 종료 코드로 돌려준다."""
    parser = argparse.ArgumentParser(description="BLOCK 조각 검사")
    parser.add_argument("index", type=Path, help="topics/<topic>/index.html")
    parser.add_argument("fragment", type=Path, help="검사할 조각 파일")
    parser.add_argument("--ids", nargs="*", default=None, help="기대하는 장면 ID 순서")
    parser.add_argument("--rules", type=Path, default=None, help="사내 규칙 JSON")
    args = parser.parse_args()

    index_html = args.index.read_text(encoding="utf-8")
    fragment = args.fragment.read_text(encoding="utf-8")
    css_classes = defined_classes(index_html)
    rules = load_rules(args.rules)

    scenes = SECTION_RE.findall(fragment)
    ids = [SCENE_ID_RE.search(s).group(1) for s in scenes if SCENE_ID_RE.search(s)]
    logger.info("장면 %d개: %s", len(scenes), " ".join(ids))
    problems: list[str] = []
    if args.ids and ids != args.ids:
        problems.append(f"장면 ID 순서가 다르다. 기대 {args.ids} / 실제 {ids}")
    for scene in scenes:
        check_scene(scene, css_classes, rules, problems)

    if problems:
        logger.info("결과: 문제 %d건", len(problems))
        for item in problems:
            logger.info("  %s", item)
        return 1
    logger.info("결과: 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
