"""치환 표의 묶음 간 불일치를 고치고 하나로 합친다.

고치는 것
  1) 401 고정 구절: P3 의 "401은 인증 문제입니다" → "401은 인증 키 문제입니다" (ROADMAP3 3-6절)
합치는 것
  P1~P4 를 scene_map 순서로 정렬해 merged.jsonl 로 저장한다.

사용법: python _workspace/roadmap3/fix_and_merge.py <scene_map.md> <표 폴더>
"""
import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("fix_and_merge")

# 묶음 간 통일이 필요한 문구 (틀린 표기 → 맞는 표기)
UNIFY = [("401은 인증 문제입니다", "401은 인증 키 문제입니다")]


def scene_order(scene_map_path: str) -> dict[str, int]:
    """장면 매핑표에서 장면 ID → 순번을 읽는다."""
    order: dict[str, int] = {}
    for line in Path(scene_map_path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*s-\d+\s*\|\s*(\S+)", line)
        if m:
            order[m.group(2)] = int(m.group(1))
    return order


def main(scene_map_path: str, table_dir: str) -> None:
    """표를 고쳐 저장하고 하나로 합친다."""
    order = scene_order(scene_map_path)
    items: list[tuple[int, str, dict]] = []
    fixed_total = 0

    for path in sorted(Path(table_dir).glob("P[0-9].jsonl")):
        lines = path.read_text(encoding="utf-8").splitlines()
        out_lines = []
        fixed_here = 0
        for line in lines:
            if not line.strip():
                continue
            item = json.loads(line)
            for rule in item.get("replace") or []:
                for wrong, right in UNIFY:
                    if wrong in rule.get("new", ""):
                        rule["new"] = rule["new"].replace(wrong, right)
                        fixed_here += 1
            out_lines.append(json.dumps(item, ensure_ascii=False))
            items.append((order.get(item["sid"], 999), path.name, item))
        if fixed_here:
            path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
            log.info("%s: 고정 문구 %d곳 통일", path.name, fixed_here)
            fixed_total += fixed_here

    items.sort(key=lambda x: x[0])
    merged = Path(table_dir) / "merged.jsonl"
    merged.write_text(
        "\n".join(json.dumps(item, ensure_ascii=False) for _, _, item in items) + "\n",
        encoding="utf-8",
    )
    log.info("통일 %d곳 · 병합 %d장면 → %s", fixed_total, len(items), merged)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
