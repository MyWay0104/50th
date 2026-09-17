"""UI 사양 문서의 F절 CSS 블록을 index.html 의 <style id="scene-styles"> 끝에 붙인다.

- 이미 붙어 있으면(표식 주석이 있으면) 그 구간을 새 내용으로 바꾼다 → 여러 번 돌려도 안전하다
- S41·S42 는 LAB08 로 합쳐질 예정이므로 장면 전용 선택자에 LAB08 을 함께 넣는다

사용법: python _workspace/roadmap2/apply_css_patch.py <index.html> <사양.md> [추가 CSS 파일 ...]
"""
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("apply_css_patch")

START = "/* >>> ROADMAP2-PATCH START >>> */"
END = "/* <<< ROADMAP2-PATCH END <<< */"


def load_patch(spec_path: Path) -> str:
    """사양 문서에서 'F. 붙여 넣을 CSS 블록' 절의 css 코드 블록을 꺼낸다."""
    text = spec_path.read_text(encoding="utf-8")
    section = text.split("## F. 붙여 넣을 CSS 블록", 1)[1]
    match = re.search(r"```css\n(.*?)```", section, re.S)
    if match is None:
        raise SystemExit("사양 문서에서 css 블록을 찾지 못했습니다")
    css = match.group(1).rstrip("\n")
    # 합쳐질 장면(S41+S42 → LAB08)에도 같은 규칙이 걸리게 한다
    css = css.replace(
        '.scene[data-scene-id="S41"] .time-block:has(> .tb-icon),',
        '.scene[data-scene-id="LAB08"] .time-block:has(> .tb-icon),\n      .scene[data-scene-id="S41"] .time-block:has(> .tb-icon),',
    ).replace(
        '.scene[data-scene-id="S41"] .tb-icon,',
        '.scene[data-scene-id="LAB08"] .tb-icon,\n      .scene[data-scene-id="S41"] .tb-icon,',
    )
    return css


def main(index_path: str, spec_path: str, extra_paths: list[str]) -> None:
    """패치 구간을 만들거나 교체한다."""
    index = Path(index_path)
    html = index.read_text(encoding="utf-8")
    parts = [load_patch(Path(spec_path))]
    for extra in extra_paths:
        parts.append(Path(extra).read_text(encoding="utf-8").rstrip("\n"))
    block = f"      {START}\n" + "\n\n".join(parts) + f"\n      {END}\n"

    if START in html:
        pattern = re.compile(r"[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n", re.S)
        html = pattern.sub(lambda _: block, html, count=1)
        log.info("기존 패치 구간을 교체했습니다")
    else:
        style = re.search(r'(<style id="scene-styles">.*?)([ \t]*</style>)', html, re.S)
        if style is None:
            raise SystemExit('<style id="scene-styles"> 를 찾지 못했습니다')
        html = html[: style.end(1)] + block + html[style.start(2):]
        log.info("패치 구간을 새로 붙였습니다")

    index.write_text(html, encoding="utf-8", newline="\n")
    log.info("패치 %d자 → %s", len(block), index)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
