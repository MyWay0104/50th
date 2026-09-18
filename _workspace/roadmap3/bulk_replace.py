"""장면별 치환 표로 다루기 어려운 자리를 파일 전체에서 한 번에 바꾼다.

치환 표(apply_table.py)는 장면 단위로 "원문이 딱 한 번 나올 것"을 요구한다.
아이콘 대체 글자(alt)처럼 같은 글자가 여러 장면에 흩어져 있는 자리는 표로 만들 수 없어
여기서 파일 전체를 대상으로 처리한다.

대상
  (a) 아이콘 alt   — 그림 파일은 그대로 두고 대체 글자만 전문용어로 바꾼다
  (b) 진행 띠 라벨 — 표지 두 장(RAG · Tool)에 남은 비유 라벨
  (c) aria-label   — 화면 낭독기가 읽는 띠 이름
  (d) CSS 주석     — slide_ui/*.css 안의 한국어 주석 (화면에는 안 보이나 유지보수용)

반드시 V3(치환 표 적용) 뒤에 돌린다. 먼저 돌리면 표의 원문이 어긋난다.

사용법: python _workspace/roadmap3/bulk_replace.py [--dry]
"""
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("bulk_replace")

INDEX = Path("topics/sk-hynix-ai-agent-guide-edu/index.html")
CSS_DIR = Path("_workspace/roadmap2/slide_ui")

# (a) 아이콘 대체 글자 — (그림 파일, 지금 글자, 새 글자)
#     그림 파일까지 함께 맞춰 바꿔야 다른 곳의 같은 글자를 건드리지 않는다
ALT_RULES = [
    ("brain.svg", "두뇌 아이콘", "LLM 아이콘"),
    ("book-open.svg", "책 아이콘", "RAG 아이콘"),
    ("hand.svg", "손발 아이콘", "Tool 아이콘"),
    ("joystick.svg", "조종 아이콘", "Agent 아이콘"),
    ("laptop.svg", "내 PC의 에이전트 아이콘", "Coding Agent 아이콘"),
    ("key.svg", "열쇠 아이콘", "인증 키 아이콘"),
    ("key.svg", "준비 아이콘", "인증 키 아이콘"),  # L6: key.svg 의 대체 글자를 한 가지로
]

# (b) 진행 띠 라벨 (지금 글자, 새 글자)
AXIS_RULES = [
    ("두뇌", "LLM"),
    ("책", "RAG"),
    ("손발", "Tool"),
    ("조종", "Agent"),
    ("내 PC의 에이전트", "Coding Agent"),
]

# (c) 낭독기가 읽는 띠 이름
ARIA_RULES = [("오늘의 여섯 정거장", "오늘의 여섯 단계")]

# (d) CSS 주석 (지금 글자, 새 글자)
CSS_RULES = [
    ("하루 흐름 칩 줄", "강의 순서 칩 줄"),
    ("지나온 정거장 채움", "지나온 단계 채움"),
    ("정거장 사이 연결선", "단계 사이 연결선"),
    ("여섯 정거장 좌표", "여섯 단계 좌표"),
    ("아직 받지 않은 것(셋째 열쇠 등)", "아직 받지 않은 것(데이터 조회용 토큰 등)"),
    ("아직 받지 않은 셋째 열쇠", "아직 받지 않은 데이터 조회용 토큰"),
    ("열쇠 지도 축소판: 아직 받지 않은 열쇠 칩", "인증 키 지도 축소판: 아직 받지 않은 키 칩"),
    ("열쇠 축소판(열쇠 아이콘 + 칩 3개)", "인증 키 축소판(인증 키 아이콘 + 칩 3개)"),
    ("열쇠 지도 칩", "인증 키 지도 칩"),
]


def replace_index(html: str) -> tuple[str, int]:
    """index.html 안의 (a)(b)(c) 를 바꾸고 바뀐 횟수를 돌려준다."""
    total = 0

    for icon, old, new in ALT_RULES:
        # 그림 파일과 대체 글자가 붙어 있는 형태만 바꾼다
        pattern = re.compile(rf'(src="assets/img/icons/{re.escape(icon)}"[^>]*?alt=")({re.escape(old)})(")')
        html, n = pattern.subn(rf"\g<1>{new}\g<3>", html)
        if n:
            log.info("  alt %-28s %-16s → %-18s %d곳", icon, old, new, n)
        total += n

    for old, new in AXIS_RULES:
        pattern = re.compile(rf'(class="axis-label"[^>]*>){re.escape(old)}(</span>)')
        html, n = pattern.subn(rf"\g<1>{new}\g<2>", html)
        if n:
            log.info("  띠 라벨  %-16s → %-18s %d곳", old, new, n)
        total += n

    for old, new in ARIA_RULES:
        pattern = re.compile(rf'(aria-label="){re.escape(old)}(")')
        html, n = pattern.subn(rf"\g<1>{new}\g<2>", html)
        if n:
            log.info("  aria    %-16s → %-18s %d곳", old, new, n)
        total += n

    return html, total


def replace_css(dry: bool) -> int:
    """slide_ui/*.css 의 한국어 주석을 바꾸고 바뀐 횟수를 돌려준다."""
    total = 0
    # 00_global_css_patch.md 안의 css 블록도 패치의 원본이므로 함께 본다
    for path in sorted([*CSS_DIR.glob("*.css"), *CSS_DIR.glob("*.md")]):
        text = path.read_text(encoding="utf-8")
        before = text
        here = 0
        for old, new in CSS_RULES:
            n = text.count(old)
            if n:
                text = text.replace(old, new)
                here += n
        if here and text != before:
            log.info("  CSS %-22s %d곳", path.name, here)
            if not dry:
                path.write_text(text, encoding="utf-8")
            total += here
    return total


def main(dry: bool) -> None:
    """index.html 과 CSS 파일의 남은 비유 낱말을 일괄로 바꾼다."""
    html = INDEX.read_text(encoding="utf-8")
    src_before = len(re.findall(r'src="assets/img/icons/[\w-]+\.svg"', html))

    new_html, n_index = replace_index(html)

    src_after = len(re.findall(r'src="assets/img/icons/[\w-]+\.svg"', new_html))
    if src_before != src_after:
        log.error("그림 파일 주소가 바뀌었다(%d → %d). 저장하지 않는다.", src_before, src_after)
        return

    n_css = replace_css(dry)

    if not dry:
        INDEX.write_text(new_html, encoding="utf-8")
    log.info("\n%sindex.html %d곳 · CSS %d곳 (그림 파일 주소 %d개 그대로)",
             "[확인만] " if dry else "", n_index, n_css, src_after)


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
