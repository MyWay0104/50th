"""index.html 을 원본으로 overview.html 을 재생성한다.

사용 대상: `<style id="scene-styles">` 규약을 따르는 deck topic.
- --renumber: 장면 id(s-N), data-start, data-duration, .page-num, #root data-duration 을 순번으로 다시 매긴다.
- overview 생성: .codex/skills/hyperframes-overview/template.html 의 placeholder 를 치환한다.
  장면 변환 규칙은 hyperframes-overview SKILL.md 3절(clip·id·timing 제거, data-slide 추가)을 따른다.
- --check: 파일을 쓰지 않고 overview.html 이 최신인지 검사한다.

템플릿은 읽기만 한다. scene-styles 가 없는 topic 은 아무것도 쓰지 않고 실패로 종료한다.
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / ".codex" / "skills" / "hyperframes-overview" / "template.html"
DEFAULT_SECONDS = 5

SECTION_RE = re.compile(r'<section\b[^>]*\bclass="scene\b[^"]*"[^>]*>.*?</section>', re.S)
OPEN_TAG_RE = re.compile(r"^<section\b[^>]*>", re.S)
SCENE_STYLES_RE = re.compile(r'<style id="scene-styles">(.*?)</style>', re.S)
ROOT_VARS_RE = re.compile(r":root\s*\{(.*?)\}", re.S)
ROOT_DURATION_RE = re.compile(r'(<div id="root"[^>]*?\bdata-duration=")([^"]*)(")', re.S)
PAGE_NUM_RE = re.compile(r'(<div class="page-num">)(.*?)(</div>)', re.S)
ACCENT_RE = re.compile(r"--accent:\s*(#[0-9a-fA-F]{6})\s*;")
REMOVED_ATTRS = ("id", "data-start", "data-duration", "data-track-index", "data-media-start")

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeckSource:
    """index.html 에서 뽑아낸 overview 재료."""

    scenes: list[str]
    scene_vars: str
    scene_styles: str
    accent_hex: str


class SyncError(Exception):
    """topic 이 이 스크립트의 규약을 따르지 않을 때 발생한다."""


def _read(path: Path) -> str:
    """UTF-8 텍스트 파일을 읽는다."""
    return path.read_text(encoding="utf-8")


def _set_attr(tag: str, name: str, value: str) -> str:
    """여는 태그의 속성 값을 바꾸거나, 없으면 추가한다."""
    pattern = re.compile(rf'(\s{re.escape(name)}=")[^"]*(")')
    if pattern.search(tag):
        return pattern.sub(lambda m: f"{m.group(1)}{value}{m.group(2)}", tag, count=1)
    return tag[:-1] + f' {name}="{value}">'


def _remove_attr(tag: str, name: str) -> str:
    """여는 태그에서 속성을 제거한다."""
    return re.sub(rf'\s{re.escape(name)}="[^"]*"', "", tag)


def _find_scenes(index_html: str) -> list[re.Match[str]]:
    """장면 section 블록을 찾는다. 중첩 section 은 규약 위반으로 본다."""
    matches = list(SECTION_RE.finditer(index_html))
    if not matches:
        raise SyncError('index.html 에서 <section class="scene ..."> 장면을 찾지 못했다.')
    for number, match in enumerate(matches, 1):
        if match.group(0).count("<section") != 1:
            raise SyncError(f"{number}번째 장면 안에 section 이 중첩되어 있다. 장면 안에서는 section 을 쓰지 않는다.")
    return matches


def renumber(index_html: str, seconds: int) -> str:
    """장면 id·타이밍·쪽번호와 #root 전체 길이를 순번 기준으로 다시 매긴다."""
    matches = _find_scenes(index_html)
    total = len(matches)
    counter = iter(range(1, total + 1))

    def _renumber_block(match: re.Match[str]) -> str:
        number = next(counter)
        block = match.group(0)
        open_tag = OPEN_TAG_RE.match(block).group(0)
        new_tag = _set_attr(open_tag, "id", f"s-{number}")
        new_tag = _set_attr(new_tag, "data-start", str((number - 1) * seconds))
        new_tag = _set_attr(new_tag, "data-duration", str(seconds))
        new_tag = _set_attr(new_tag, "data-track-index", "0")
        block = new_tag + block[len(open_tag):]
        return PAGE_NUM_RE.sub(lambda m: f"{m.group(1)}{number} / {total}{m.group(3)}", block)

    renumbered = SECTION_RE.sub(_renumber_block, index_html)
    if not ROOT_DURATION_RE.search(renumbered):
        raise SyncError('#root 의 data-duration 속성을 찾지 못했다.')
    return ROOT_DURATION_RE.sub(lambda m: f"{m.group(1)}{total * seconds}{m.group(3)}", renumbered, count=1)


def parse_source(index_html: str) -> DeckSource:
    """index.html 에서 장면·토큰·장면 CSS·액센트 색을 뽑는다."""
    style_match = SCENE_STYLES_RE.search(index_html)
    if not style_match:
        raise SyncError('<style id="scene-styles"> 가 없다. 이 topic 은 sync_overview.py 규약을 따르지 않는다.')
    css = style_match.group(1)
    vars_match = ROOT_VARS_RE.search(css)
    if not vars_match:
        raise SyncError("scene-styles 안에 :root { ... } 토큰 블록이 없다.")
    accent_match = ACCENT_RE.search(vars_match.group(1))
    if not accent_match:
        raise SyncError(":root 에 --accent: #RRGGBB; 토큰이 없다.")
    scene_styles = (css[: vars_match.start()] + css[vars_match.end():]).strip("\n")
    return DeckSource(
        scenes=[m.group(0) for m in _find_scenes(index_html)],
        scene_vars=vars_match.group(1).strip("\n"),
        scene_styles=scene_styles,
        accent_hex=accent_match.group(1).lower(),
    )


def to_overview_scene(block: str, number: int) -> str:
    """index 장면을 overview 장면으로 바꾼다: clip·id·timing 제거, data-slide 추가."""
    open_tag = OPEN_TAG_RE.match(block).group(0)
    new_tag = open_tag
    for name in REMOVED_ATTRS:
        new_tag = _remove_attr(new_tag, name)
    new_tag = re.sub(
        r'class="([^"]*)"',
        lambda m: 'class="' + " ".join(c for c in m.group(1).split() if c != "clip") + '"',
        new_tag,
        count=1,
    )
    new_tag = _set_attr(new_tag, "data-slide", str(number))
    return new_tag + block[len(open_tag):]


def _hex_to_rgb(hex_color: str) -> str:
    """#RRGGBB 를 'R, G, B' 문자열로 바꾼다."""
    value = hex_color.lstrip("#")
    return ", ".join(str(int(value[i : i + 2], 16)) for i in (0, 2, 4))


def _replace_line_placeholder(template: str, name: str, content: str) -> str:
    """한 줄에 단독으로 있는 {{NAME}} 만 치환한다. 주석 안의 설명용 표기는 건드리지 않는다."""
    pattern = re.compile(rf"^([ \t]*)\{{\{{{name}\}}\}}[ \t]*$", re.M)
    if not pattern.search(template):
        raise SyncError(f"템플릿에서 단독 줄 placeholder {{{{{name}}}}} 를 찾지 못했다.")
    return pattern.sub(lambda m: content, template, count=1)


def build_overview(template: str, topic_id: str, source: DeckSource) -> str:
    """템플릿 placeholder 를 채워 overview.html 문자열을 만든다."""
    slides_html = "\n\n".join(
        to_overview_scene(block, number) for number, block in enumerate(source.scenes, 1)
    )
    html = _replace_line_placeholder(template, "SCENE_VARS", source.scene_vars)
    html = _replace_line_placeholder(html, "SCENE_STYLES", source.scene_styles)
    html = _replace_line_placeholder(html, "SLIDES_HTML", slides_html)
    replacements = {
        "{{TOPIC_ID}}": topic_id,
        "{{SLIDE_COUNT}}": str(len(source.scenes)),
        "{{ACCENT_HEX}}": source.accent_hex,
        "{{ACCENT_RGB}}": _hex_to_rgb(source.accent_hex),
    }
    for key, value in replacements.items():
        html = html.replace(key, value)
    return html


def parse_args() -> argparse.Namespace:
    """명령행 인자를 읽는다."""
    parser = argparse.ArgumentParser(description="index.html 에서 overview.html 을 재생성한다.")
    parser.add_argument("topic", type=Path, help="topics/<topic-name> 경로")
    parser.add_argument("--renumber", action="store_true", help="장면 id·타이밍·쪽번호를 순번으로 다시 매긴다")
    parser.add_argument("--seconds", type=int, default=DEFAULT_SECONDS, help="장면당 data-duration(초), 기본 5")
    parser.add_argument("--check", action="store_true", help="파일을 쓰지 않고 overview.html 이 최신인지 검사한다")
    return parser.parse_args()


def main() -> int:
    """스크립트 진입점."""
    args = parse_args()
    topic = args.topic if args.topic.is_absolute() else (Path.cwd() / args.topic)
    index_path = topic / "index.html"
    overview_path = topic / "overview.html"
    try:
        if not index_path.exists():
            raise SyncError(f"{index_path} 가 없다.")
        if not TEMPLATE_PATH.exists():
            raise SyncError(f"템플릿 {TEMPLATE_PATH} 가 없다.")
        index_html = _read(index_path)
        parse_source(index_html)  # 규약 검사: 실패하면 아무 파일도 쓰지 않는다.

        if args.renumber:
            index_html = renumber(index_html, args.seconds)

        source = parse_source(index_html)
        overview_html = build_overview(_read(TEMPLATE_PATH), topic.name, source)
    except SyncError as exc:
        logger.error("sync_overview 실패: %s", exc)
        return 1

    if args.check:
        current = _read(overview_path) if overview_path.exists() else ""
        index_current = _read(index_path)
        if current != overview_html or index_current != index_html:
            logger.error("overview.html 또는 index.html 순번이 최신이 아니다. sync_overview.py 를 다시 실행한다.")
            return 1
        logger.info("최신 상태: 장면 %d개", len(source.scenes))
        return 0

    if args.renumber:
        index_path.write_text(index_html, encoding="utf-8", newline="\n")
    overview_path.write_text(overview_html, encoding="utf-8", newline="\n")
    logger.info("overview.html 재생성 완료: 장면 %d개 (renumber=%s)", len(source.scenes), args.renumber)
    return 0


if __name__ == "__main__":
    sys.exit(main())
