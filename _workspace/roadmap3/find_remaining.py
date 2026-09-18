"""치환 표를 가상으로 적용한 뒤, 남는 비유 낱말이 어떤 자리에 있는지 분류한다.

자리: 띠 라벨(axis-label) / 아이콘 alt / aria-label / 그 밖(화면·노트 본문)
"""
import json
import logging
import re
from collections import Counter
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("find_remaining")

WORDS = ["두뇌", "손발", "조종", "열쇠", "정거장", "내 PC의 에이전트", "하루 흐름"]

html = Path("topics/sk-hynix-ai-agent-guide-edu/index.html").read_text(encoding="utf-8")
for path in sorted(Path("_workspace/roadmap3/tables").glob("P*.jsonl")):
  for line in path.read_text(encoding="utf-8").splitlines():
    if not line.strip():
      continue
    item = json.loads(line)
    for rule in item.get("replace") or []:
      html = html.replace(rule["old"], rule["new"], 1)

kinds = Counter()
samples = {}
for word in WORDS:
  for m in re.finditer(re.escape(word), html):
    around = html[max(0, m.start() - 120):m.end() + 60]
    if 'class="axis-label"' in around[-200:] and around.rfind('class="axis-label"') > around.rfind(">", 0, 120):
      kind = "띠 라벨"
    elif re.search(r'alt="[^"]*$', html[max(0, m.start() - 60):m.start()]):
      kind = "아이콘 alt"
    elif re.search(r'aria-label="[^"]*$', html[max(0, m.start() - 60):m.start()]):
      kind = "aria-label"
    elif 'class="axis-label"' in html[max(0, m.start() - 60):m.start()]:
      kind = "띠 라벨"
    else:
      kind = "본문"
    kinds[(word, kind)] += 1
    samples.setdefault((word, kind), around.replace("\n", " ")[-150:])

log.info("%-18s %-10s %s", "낱말", "자리", "개수")
log.info("-" * 60)
for (word, kind), n in sorted(kinds.items(), key=lambda x: (-x[1], x[0])):
  log.info("%-18s %-10s %d", word, kind, n)
log.info("\n합계 %d곳", sum(kinds.values()))

log.info("\n'본문'으로 분류된 것의 앞뒤 (표에서 빠진 진짜 문장일 수 있다)")
for (word, kind), text in samples.items():
  if kind == "본문":
    log.info("  [%s] …%s", word, text)
