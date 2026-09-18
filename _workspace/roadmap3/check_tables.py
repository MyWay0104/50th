"""치환 표를 집계하고, 원문이 index.html 의 해당 장면에 정확히 한 번 나오는지 미리 센다.

apply_table.py --dry 와 같은 판정을 하되, 묶음별·장면별로 어디가 어긋나는지 함께 보여 준다.
"""
import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("check_tables")

NOTE_MARK = '<aside class="speaker-note">'


def find_scene(html: str, sid: str) -> str | None:
  """장면 section 을 찾는다."""
  m = re.search(rf'<section [^>]*data-scene-id="{re.escape(sid)}".*?</section>', html, re.S)
  return m.group(0) if m else None


def main(index_path: str, table_dir: str) -> None:
  """표를 읽어 항목 수와 원문 일치 여부를 집계한다."""
  html = Path(index_path).read_text(encoding="utf-8")
  total = {"replace": 0, "delete": 0, "title": 0, "miss": 0, "scene": 0}
  problems = []

  for path in sorted(Path(table_dir).glob("P*.jsonl")):
    n_rep = n_del = n_title = n_miss = n_scene = 0
    for line in path.read_text(encoding="utf-8").splitlines():
      if not line.strip():
        continue
      item = json.loads(line)
      sid = item["sid"]
      n_scene += 1
      scene = find_scene(html, sid)
      if scene is None:
        problems.append(f"{path.name} {sid}: 장면을 찾지 못함")
        n_miss += 1
        continue
      cut = scene.find(NOTE_MARK)
      head, note = (scene[:cut], scene[cut:]) if cut >= 0 else (scene, "")

      if item.get("title"):
        n_title += 1
        # apply_table.py 의 TITLE_RES 와 같은 조건으로 검사한다
        if not re.search(r'<h2 class="scene-title"[^>]*>', head) and not re.search(r'<h1 class="hero-title"[^>]*>', head):
          problems.append(f"{path.name} {sid}: title 을 넣을 요소가 없다(표지의 is-section 문제일 수 있음)")
          n_miss += 1

      for i, rule in enumerate(item.get("replace") or []):
        n_rep += 1
        if rule.get("new") == "":
          n_del += 1
        part = note if rule.get("where") == "note" else head
        count = part.count(rule["old"])
        if count != 1:
          problems.append(f"{path.name} {sid} replace[{i}] {rule.get('where','screen')} {count}회: {rule['old'][:50]}")
          n_miss += 1

    log.info("%-10s 장면 %2d · 치환 %3d(삭제 %2d) · title %d · 어긋남 %d", path.name, n_scene, n_rep, n_del, n_title, n_miss)
    total["replace"] += n_rep
    total["delete"] += n_del
    total["title"] += n_title
    total["miss"] += n_miss
    total["scene"] += n_scene

  log.info("\n합계: 장면 %d · 치환 %d(삭제 %d) · title %d · **어긋남 %d**",
           total["scene"], total["replace"], total["delete"], total["title"], total["miss"])
  if problems:
    log.info("\n어긋난 항목 (최대 40개)")
    for p in problems[:40]:
      log.info("  %s", p)


if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])
