"""치환 표에서 고정 문구(401 안내·환경 파일 안전·채팅용 키)가 든 항목을 모아 보여 준다.

묶음마다 글자가 다르면 적용 뒤 덱 안에서 표현이 섞이므로 미리 맞춘다.
"""
import json
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("show_fixed_phrases")

KEYS = {
    "401": "401",
    "환경 파일 안전": "환경 파일에는",
    "채팅용 키": "채팅용 키",
    "채팅용 API 키": "채팅용 API 키",
}


def main(table_dir: str, which: str) -> None:
    """지정한 고정 문구가 든 항목을 묶음별로 출력한다."""
    needle = KEYS[which]
    for path in sorted(Path(table_dir).glob("P*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            for i, rule in enumerate(item.get("replace") or []):
                if needle in rule.get("new", ""):
                    log.info("%s %s [%d] %s", path.name, item["sid"], i, rule.get("where", "screen"))
                    log.info("   %s", rule["new"][:150])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
