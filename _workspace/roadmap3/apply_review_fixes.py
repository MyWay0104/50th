"""V2 용어 검증(review_terms.md) 지적과 인증 키 표기 결정(안 '나')을 치환 표에 반영한다.

두 가지 일을 한다.
  1) EDITS  — 이미 표에 있는 항목의 `new` 값을 고친다. (sid, 번호, 바꿀 부분, 새 부분)
  2) ADDS   — 표에 없던 자리(주로 "쥐여 주기")를 새 치환 항목으로 더한다.

바꿀 부분을 찾지 못하면 그 자리를 보고하고 아무것도 저장하지 않는다.
원본 확인 없이 덮어쓰면 표가 조용히 어긋나기 때문이다.

사용법: python _workspace/roadmap3/apply_review_fixes.py
"""
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("apply_review_fixes")

TABLE = Path("_workspace/roadmap3/tables/merged.jsonl")

# (장면, replace 번호, 지금 new 안에 있는 글자, 새 글자, 사유)
EDITS = [
  # ── 높음 5건 ──────────────────────────────────────────────
  ("S04", 0, "LLM은 텍스트를 생성할 뿐, 외부 데이터 조회나 계산은 하지 못합니다.",
            "LLM은 문장을 만들 뿐, 자료를 조회하지 못하고 계산도 보장하지 못합니다.", "H1 LLM 정의"),
  ("S04", 2, "LLM은 텍스트를 생성할 뿐이라 물어보면 대답만 하고, 조회나 계산은 하지 못합니다.",
            "LLM은 문장을 만들 뿐이라 물어보면 대답만 하고, 자료를 조회하지 못하고 계산도 보장하지 못합니다.", "H2 노트 짝"),
  ("N03", 0, "Tool 실습에서 직접 반복문으로 돌려 본 호출에 붙인 이름이 Agent 루프이고,",
            "모델이 결과를 보고 다음 도구 호출을 정하는 반복이 Agent 루프이고,", "H3 Agent 루프 정의 복원"),
  ("T03", 1, "실습 04b에서 직접 반복문으로 돌려 본 호출이 Agent 루프의",
            "실습 04b에서 반복문으로 직접 돌린 도구 호출 반복이 Agent 루프의", "H4 호출은 루프가 아니다"),
  ("T03", 10, "화면의 '직접 반복문으로'는 실습 코드에 그 반복이 적혀 있었다는 뜻이고,",
             "화면의 '반복문으로 직접 돌린'은 실습 코드에 그 반복이 적혀 있었다는 뜻이고,", "H4 노트 짝"),

  # ── 중간 ──────────────────────────────────────────────────
  ("LAB06", 8, ">데이터 조회용 액세스 토큰<", ">데이터 조회용 토큰<", "M2 · ⑧ 이름 하나로"),
  ("A05", 3, "데이터 조회용 액세스 토큰은 만료되기도", "데이터 조회용 토큰은 만료되기도", "M3 · ⑧"),
  ("E01", 15, "셋째인 데이터 조회용 액세스 토큰은 게이트웨이 밖, 다른 플랫폼에서 발급합니다.",
             "데이터 조회용 토큰은 사내 LLM 게이트웨이가 아니라 다른 플랫폼에서 발급합니다.", "M10 · ⑧"),
  ("S23", 8, "그래서 Coding Agent라고 부릅니다.",
            "그래서 파일과 명령을 도구로 쓰는 Coding Agent입니다.", "M5 인과 바로잡기"),
  ("G01", 3, '<span class="dg-sub" data-editable="true">답 생성</span>',
            '<span class="dg-sub" data-editable="true">모델 호출</span>', "M6 G02와 같은 글자"),
  ("G01", 0, "LLM에 RAG와 Tool을 붙이고, Agent와 Coding Agent를 거쳐 업무에 적용합니다.",
            "LLM에 RAG와 Tool을 붙이고 Agent로 묶은 뒤, Coding Agent로 내 업무에 적용합니다.", "M7 G02와 한 쌍"),
  ("D05", 1, 'aria-label="학습 단계 여섯 칸"', 'aria-label="오늘의 여섯 단계"', "M8 한 가지 이름"),
  ("D06", 1, 'aria-label="학습 단계 여섯 칸"', 'aria-label="오늘의 여섯 단계"', "M8 한 가지 이름"),
  ("S44", 2, "여섯 학습 단계를", "여섯 단계를", "M9 한 가지 이름"),
  ("G02", 6, "여섯 학습 단계를", "여섯 단계를", "M9 한 가지 이름"),
  ("LAB04b", 1, ">조회용 토큰을 받아<", ">데이터 조회용 토큰을 받아<", "M12 처음 나오는 자리"),

  # ── 인증 키 표기: 사용자 결정 '나' (정의 자리 E01만 긴 이름) ──
  ("LAB01", 3, '"true">채팅용 API 키</span>', '"true">채팅용 키</span>', "안 나 · 정의 자리 밖"),
  ("LAB01", 3, '"true">임베딩용 API 키</span>', '"true">임베딩용 키</span>', "안 나 · 정의 자리 밖"),
  ("LAB01", 7, "채팅용 API 키와 임베딩용 API 키를 하나씩", "채팅용 키와 임베딩용 키를 하나씩", "안 나 · 정의 자리 밖"),
  ("LAB04b", 5, "채팅용 API 키", "채팅용 키", "안 나 · 정의 자리 밖"),
  ("N02", 5, "채팅용 API 키", "채팅용 키", "안 나 · 정의 자리 밖"),
  ("S23", 3, ">채팅용 API 키<", ">채팅용 키<", "안 나 · 정의 자리 밖"),
  ("LAB06", 6, ">채팅용 API 키<", ">채팅용 키<", "안 나 · M4를 결정에 맞춰 뒤집음"),
  ("LAB06", 11, "확인할 것은 키입니다. 오전과 같은 키이고,",
               "확인할 것은 키입니다. 오전과 같은 채팅용 키이고,", "M14 · 무슨 키인지 밝힘"),

  # ── 낮음 ──────────────────────────────────────────────────
  ("T03", 0, "다음은 모델이 결과를 보고 호출을 정하는 Agent 루프입니다.",
            "다음은 모델이 결과를 보고 다음 도구 호출을 정하는 Agent 루프입니다.", "L2 고정 정의와 같은 글자"),
  ("T03", 3, ">Agent 루프는 아직<", ">Agent는 아직<", "L3 아래 항목과 맞춤"),
]

# (장면, where, 원문, 새 글자, 사유) — 표에 없던 자리를 더한다
ADDS = [
  # M13 "쥐여 주기" 4곳 + 같은 뿌리의 잔향 3곳
  ("S16", "screen", ">도구 쥐여 주기<", ">도구 연결(bind_tools)<", "M13 카드 ①"),
  ("S16", "screen", "# 카드 ① 도구 쥐여 주기", "# 카드 ① 도구 연결", "M13 코드 주석"),
  ("S16", "note", "bind_tools로 도구를 쥐여 주면", "bind_tools로 도구를 연결하면", "M13 노트"),
  ("T02", "screen", ">계산 도구 쥐여 주기<", ">계산 도구 연결<", "M13 ③열"),
  ("T02", "screen", "계산 함수를 도구로 쥐여 주고", "계산 함수를 도구로 연결하고", "M13 화면 설명"),
  ("T02", "note", "계산 도구를 쥐여 준 뒤", "계산 도구를 연결한 뒤", "M13 노트"),
  ("LAB04b", "screen", '<span class="nowrap">쥐여 주기</span>', '<span class="nowrap">연결하기</span>', "M13 시간 블록 2"),
  ("LAB04b", "note", "도구 세 개를 쥐여 주고", "도구 세 개를 연결하고", "M13 노트"),
  # H5 실습-예고 짝 복원 + '손으로' 제거
  ("LAB04b", "note",
   "다음 구간에서 이것을 손으로 돌려 본 반복이라고 부를 텐데, 여기서 '손으로'는 반복문을 우리가 직접 코드로 짜서 돌렸다는 뜻입니다.",
   "다음 구간에서는 이 반복을 '반복문으로 직접 돌린 도구 호출 반복'이라고 부르겠습니다.", "H5 예고-회수 짝"),
  # M11 사람이 하는 행동(HITL)을 화면에 남긴다
  ("LAB07", "screen", "승인 요청은 명령 실행과 파일 수정에서 뜹니다.",
   "승인 요청은 명령 실행과 파일 수정에서 뜨니, 무엇을 하려는지 읽고 승인합니다.", "M11 관찰-행동 짝"),
]


def main() -> None:
  """표를 읽어 지적 사항을 반영하고 다시 저장한다."""
  items = [json.loads(l) for l in TABLE.read_text(encoding="utf-8").splitlines() if l.strip()]
  by_sid = {it["sid"]: it for it in items}
  misses = []

  for sid, idx, find, repl, why in EDITS:
    rules = (by_sid.get(sid) or {}).get("replace") or []
    if idx >= len(rules) or find not in rules[idx].get("new", ""):
      misses.append(f"EDIT {sid} #{idx} ({why}): 못 찾음 → {find[:60]}")
      continue
    rules[idx]["new"] = rules[idx]["new"].replace(find, repl, 1)

  for sid, where, old, new, why in ADDS:
    it = by_sid.get(sid)
    if it is None:
      misses.append(f"ADD {sid} ({why}): 장면이 표에 없음")
      continue
    it.setdefault("replace", []).append({"where": where, "old": old, "new": new})

  if misses:
    log.info("반영하지 못한 항목 %d개 — 저장하지 않았다", len(misses))
    for m in misses:
      log.info("  %s", m)
    return

  TABLE.write_text("\n".join(json.dumps(it, ensure_ascii=False) for it in items) + "\n", encoding="utf-8")
  log.info("반영 완료: 고침 %d곳 · 새 항목 %d곳 → %s", len(EDITS), len(ADDS), TABLE)


if __name__ == "__main__":
  main()
