# final-touch — 사용자 수정 12건 반영 기록 (2026-09-17)

대상: `topics/sk-hynix-ai-agent-guide-edu/index.html`(57장, 최종본) · 브랜치 `final-touch`(main에서 분기, 끝나면 main 병합) · shrimp F1–F8.

## 문제 분석

v0.4 57장에 사용자가 12가지 수정을 요청했다. 대부분이 57장 전체에 걸친 가로 방향 수정(구간 표시·쪽번호·시간 정보·반말·출처 삭제)이어서, 장면 단위로 새로 만드는 방식보다 "구조 제거 스크립트 → 문구 치환 표 → 시각 배치 명세 → 일괄 적용 → 검토" 순서가 안전하다. 한국어 판단(존댓말·제목·시간 문장)은 서브에이전트가 표로 만들고, 오케스트레이터는 표를 장면 범위에서 정확히 1회 치환해 적용했다.

## 설계 — 요청별 처리

| # | 요청 | 처리 |
|---|---|---|
| 1 | 기/승/전/결 문구 삭제 | 막 태그 7곳, G01 괄호선(기·승·전·결), S01 하루 흐름 칩 삭제. 노트의 '네 막' 문장은 문구 표로 바꿈 |
| 2 | 첫 시간표 외 시간 정보 삭제 | 구간 시각 칩 삭제, 실습 안내판 안내 줄의 시각·분 삭제, 시간 블록 "N분" → 순서 번호(S41–S43은 번호 숨김), 진행 띠 시각 삭제, 문장 속 시각은 순서 표현으로. 노트의 시각·분도 순서 표현으로(G01 시간표 노트만 예외) |
| 3 | 반말 → 존댓말 | 화면 평서형 문장 전부 '…합니다/…입니다'. 카드 의문 라벨도 '…나요'. 명사형 라벨은 그대로 |
| 4 | 제목 간결화 | 14장 변경(예: G00 '왜 이런 순서로 배우나' → 'AI를 잘 활용하는 공부법', S41–S43 '자유 실습 1–3단계', 부록 10장 '부록 ·' 접두어) |
| 5 | B1–B7 표시 삭제 | 모든 장면 eyebrow 삭제, S02 'B○에서 다룸', G02 구간 칩, G01 번호 원 B1–B7 → 1–7, 문장 속 'B2' 등 |
| 6 | 이미지 확대 | G00 썸네일 +21%, S05 원 논문 그림 340 → 386px, A01 280 → 360px, A10 승인 카드 폭 +13% |
| 7 | 4쪽 제목 | S02 '강사 소개' |
| 8 | 표지 정리 | 제목·부제('SK hynix 사내 교육', '내 업무에 적용할 작은 AI 도구 만들기')·강사 줄('강사 · NAND Implant기술 이상우 TL')과 아이콘 타일만 |
| 9 | '근거:'와 비공식 출처 삭제 | 출처 줄은 Anthropic·OpenAI·LangChain/LangGraph·vLLM·Streamlit·Claude Code 공식 문서와 논문만. 화면 캡션의 '교안 내용 재구성'과 노트의 교안 연계 문장도 출처 표현만 삭제(내용은 유지). 가상 데이터 표기(S18·S35)는 출처 접두어 없이 유지. G00 유튜브 출처는 URL과 함께 유지(요청). S30 작업 기록 양식의 '근거:'는 '이유:'로 |
| 10 | 쪽번호 삭제 | `.page-num` 57개 삭제 |
| 11 | 시각 자료 보강 | Simple Icons 로고 12종 + vLLM 로고 + Lucide 아이콘 44종을 받아 문맥에 맞게 배치(로고 29·아이콘 145). 자리표시 10곳 유지, 57장 모두 이미지 또는 인포그래픽 |
| 12 | SK hynix 느낌 색 | DESIGN-Notion.md 안의 Sticker Orange `#dd5b00`을 강조색, Deep Orange `#793400`을 표지·마무리 배경과 경고 점으로. 화면·노트의 '파랑' 표현도 '주황'으로 |

오케스트레이터 결정: 오전/오후는 시각이 아니라 순서 표현이라 유지("오전 앱"). G02 네 카드 제목은 G00 네 단계와 같은 명사형(설명하기·고르기·전달하기·검증하기). 부록은 구간 표시가 사라져 제목에 '부록 ·' 접두어.

## 구현

| 작업 | 커밋 | 내용 |
|---|---|---|
| F1 구조 제거·주황 테마 | `db1eb7b` | `apply_ft_structure.py` |
| F2 자산 | `db1eb7b` | `fetch_ft_assets.py`, `assets/img/LICENSES.md` |
| F3 문구 표 | `7770a76` | slide_content_writer 3개 → `final_touch/copy_{B1-B3,B4-B7,APP}.jsonl` |
| F4 시각 배치 명세 | `22e09e8` | slide_ui_designer → `final_touch/visual_spec.{jsonl,md}` |
| F5 강사 사전 검토 | `e318145` | `lecture_review/final-touch-pre.md` → `final_touch/copy_ORCH.jsonl` |
| F6 적용 | `40b3c30` | visual 142 → steps → copy 91 → sweep |
| F7 마지막 검토 | `c2d1c27`, `b4ab10d` | 시각 2 + 내용 1 → `apply_ft_final.py`, `apply_ft_final2.py` |

## 코드

적용 도구는 세션 scratchpad의 일회성 스크립트다(저장소 밖). 재현이 필요하면 이 표의 입력 파일(`_workspace/final_touch/*.jsonl`)과 순서를 따른다.

```text
apply_ft_visual.py → apply_ft_steps.py → apply_ft_copy.py → apply_ft_sweep.py → sync_overview.py
검사: validate_topic.py · hyperframes lint · sync_overview.py --check · qa_ft.py · Playwright 넘침 검사
```

## 테스트 방법

- `python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu` 통과, `npx hyperframes lint` 오류 0(경고 9: 기존 2 + 같은 아이콘을 한 장면에서 반복 쓴 영상 렌더용 경고 7, 덱 출력과 무관).
- `qa_ft.py`: 화면 시간(G01 제외)·'근거:'(출처 줄)·B1–B7·교안·평서 종결 0, 쪽번호·eyebrow·막 태그 0, 시각 요소 없는 장면 0.
- Playwright: 57장 넘침 0, 깨진 이미지 0, overview 콘솔 오류 0.

## 향후 개선사항 (사용자 확인 필요)

- 실습 안내판(S08·S13·S19·S20·S26·S32·S37·S40–S43)은 사내 실습 HTML에 맞춰 다시 고칠 예정이라, 배치 통일과 'S08 실습 가이드 해당 장' 중복은 그때 함께 정한다.
- G00 유튜브 출처(공식 문서가 아님)와 논문·백서 출처를 "공식 문서" 범위에 둘지, A10 사내 배포 패키지 승인 카드 이미지를 수강생에게 보여도 되는지.
- A10 승인 카드 속 글자는 원 화면이라 강의실 뒤에서 작다(칸을 넓혀 13% 키움). 필요하면 강의 중 확대해 보여 준다.
- 캡처 10곳을 확보하지 못하면 캡처가 있다고 전제한 노트 문장을 화면의 '대체' 안내에 맞게 바꾼다.
