"""장면 ID 가 바뀌는 안내판에 기존 장면 전용 CSS 규칙을 그대로 물려준다.

예: [data-scene-id="S13"] 로 시작하는 규칙을 [data-scene-id="LAB04"] 로 복제한다.
복제한 규칙은 02_scene_alias.css 로 저장하고, apply_css_patch.py 가 패치 구간에 함께 붙인다.

사용법: python _workspace/roadmap2/make_scene_alias_css.py <scene-styles.css> <출력.css>
"""
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("make_scene_alias_css")

# 옛 장면 ID → 그 장면을 본떠 만드는 새 장면 ID 들
ALIASES = {
    "S08": ["LAB01", "LAB02", "LAB03"],
    "S13": ["LAB04"],
    "S19": ["LAB04b"],
    "S20": ["LAB05"],
    "S26": ["LAB06", "LAB07"],
    "S41": ["LAB08"],
}
RULE_RE = re.compile(r"([^{}]+)\{([^{}]*)\}")
PATCH_START = "/* >>> ROADMAP2-PATCH START >>> */"


def main(css_path: str, out_path: str) -> None:
    """원본 규칙(패치 구간 앞)에서 장면 전용 규칙을 찾아 새 ID 로 복제한다."""
    css = Path(css_path).read_text(encoding="utf-8").split(PATCH_START, 1)[0]
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    lines = ["", "      /* ===== ROADMAP2 장면 ID 별칭: 안내판 ID 가 바뀌어도 기존 장면 전용 규칙이 걸리게 복제 ===== */"]
    count = 0
    for match in RULE_RE.finditer(css):
        selector, body = match.group(1).strip(), match.group(2).strip()
        for old_id, new_ids in ALIASES.items():
            token = f'[data-scene-id="{old_id}"]'
            if token not in selector:
                continue
            for new_id in new_ids:
                new_selector = " ".join(selector.replace(token, f'[data-scene-id="{new_id}"]').split())
                lines.append(f"      {new_selector} {{ {' '.join(body.split())} }}")
                count += 1
    Path(out_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("별칭 규칙 %d개 → %s", count, out_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
