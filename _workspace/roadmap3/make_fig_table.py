"""자리표시(placeholder) 12곳을 도식 이미지로 바꾸는 치환 표를 만든다.

자리표시는 원래 "나중에 사내 캡처가 들어올 자리"였다. 사내 서버를 쓸 수 없어
같은 내용을 도식으로 그려 넣는다. 원래의 캡처 조건은 ROADMAP3 에 옮겨 적어,
나중에 진짜 캡처로 다시 바꿀 수 있게 한다.

사용법: python _workspace/roadmap3/make_fig_table.py
"""
import json
import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("make_fig_table")

INDEX = Path("topics/sk-hynix-ai-agent-guide-edu/index.html")
OUT = Path("_workspace/roadmap3/tables/F1.jsonl")
SPEC = Path("_workspace/roadmap3/placeholder-specs.md")

# 장면 → (이미지 파일, 대체 글자)
FIGS = {
    "S02":    ("fig-s02.png",    "만들며 배운 것 세 가지 — 구조, 데이터 검증, 사용자 동선"),
    "LAB01":  ("fig-lab01.png",  "인증 키 세 가지와 각각의 접근 대상 — 채팅용 키는 채팅 모델, 임베딩용 키는 임베딩 모델, 데이터 조회용 토큰은 사내 데이터"),
    "LAB02":  ("fig-lab02.png",  "체인 도식 — 템플릿에서 모델로, 모델에서 응답으로"),
    "LAB03":  ("fig-lab03.png",  "관찰할 것 세 가지 — temperature에 따른 차이, 봇의 성격, 답의 틀"),
    "LAB04":  ("fig-lab04.png",  "찾아온 조각을 점수 순으로 둔 표와 근거로 답하는 방식"),
    "LAB04b": ("fig-lab04b.png", "도구 호출 기록 — 바퀴마다 도구 이름, 넣은 값, 결과"),
    "LAB05":  ("fig-lab05.png",  "장비 조회 Agent 화면을 화면·처리·데이터 세 영역으로 나눈 그림"),
    "LAB06":  ("fig-lab06.png",  "내 PC, 설정 파일, 사내 LLM 게이트웨이 세 층"),
    "LAB07":  ("fig-lab07.png",  "읽히고 설명 받을 요청 세 가지 — 요약, 구조, 버그"),
    "S29":    ("fig-s29.png",    "웹 화면판의 입력 칸과 결과 영역이 코드의 어느 줄에 해당하는지 보여 주는 그림"),
    "C02":    ("fig-c02.png",    "질문에서 코드 실행을 거쳐 결과 표가 나오는 흐름"),
    "C04":    ("fig-c04.png",    "노트 한 장 안에서 원문과 내 의견과 다음 할 일을 나눠 적은 모습"),
}

PH_RE = re.compile(r'[ \t]*<div class="placeholder[^"]*">.*?</div>\s*</div>\n?', re.S)


def main() -> None:
    """장면마다 자리표시 한 덩어리를 찾아 이미지 태그로 바꾸는 표를 쓴다."""
    html = INDEX.read_text(encoding="utf-8")
    rows: list[dict] = []
    specs: list[str] = ["# 자리표시 원래 사양 (도식으로 바꾸기 전 기록)", ""]
    specs.append("사내 캡처를 확보하면 이 조건대로 찍어 도식을 대체할 수 있다.", )
    specs.append("")
    specs.append("| 장면 | 넣을 자료 | 조건 | 지금 들어간 도식 |")
    specs.append("|---|---|---|---|")
    misses: list[str] = []

    for sid, (fig, alt) in FIGS.items():
        m = re.search(rf'<section [^>]*data-scene-id="{sid}".*?</section>', html, re.S)
        if m is None:
            misses.append(f"{sid}: 장면 없음")
            continue
        scene = m.group(0)
        found = PH_RE.findall(scene)
        if len(found) != 1:
            misses.append(f"{sid}: 자리표시 {len(found)}개 (1개여야 함)")
            continue
        old = found[0]

        # 원래 사양을 기록해 둔다
        want = re.search(r"넣을 자료:\s*([^<]*)<", old)
        cond = re.search(r"조건:\s*([^<]*)<", old)
        specs.append(
            f"| {sid} | {want.group(1).strip() if want else '-'} "
            f"| {(cond.group(1).strip() if cond else '-').replace('|', '·')} | `{fig}` |"
        )

        indent = re.match(r"[ \t]*", old).group(0)
        new = f'{indent}<img class="fig-img" src="assets/img/appendix/{fig}" alt="{alt}">\n'
        rows.append({"sid": sid, "replace": [{"where": "screen", "old": old, "new": new}]})

    if misses:
        log.info("처리하지 못한 장면 %d개 — 저장하지 않았다", len(misses))
        for x in misses:
            log.info("  %s", x)
        return

    OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    SPEC.write_text("\n".join(specs) + "\n", encoding="utf-8")
    log.info("자리표시 %d곳 → %s", len(rows), OUT)
    log.info("원래 사양 기록 → %s", SPEC)


if __name__ == "__main__":
    main()
