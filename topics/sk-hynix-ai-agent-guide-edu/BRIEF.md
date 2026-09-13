# AI Agent Guide 사내 교육

## 문제 분석

- 출력 타입: `deck` (16:9, 1920×1080)
- 회사/브랜드: SK hynix 사내 교육. 브랜드 디자인 문서가 없어 `new_md/DESIGN-Notion.md`를 최소 적용한다.
- 디자인 원본: `C:\LSW_Coding\3_slide_master_v2\new_md\DESIGN-Notion.md` → 이 폴더의 `DESIGN.md`
- 최종 산출물: 발표자용 PDF. PPTX는 선택. 사용자 overview 최종 확인 전 export 금지.
- 수강생: AI 경험자와 처음인 사람이 섞인 사내 인원. Python·웹개발 숙련을 전제하지 않는다.
- 중심 메시지: **LLM에게 맡길 일과 코드·데이터·사람이 책임질 일을 구분하면, 비전공자도 작은 업무 도구부터 만들고 개선할 수 있다.**

## 설계

하루 시간표 (교육 활동 330분):

| 구간 | 시각 | 주제 | 장면 |
|---|---|---|---|
| B1 | 09:00–09:40 | LLM 원리와 첫 호출 | S01, G01, S02–S08 |
| B2 | 10:00–10:40 | 외부 근거와 기사 RAG | S09–S14 |
| B3 | 11:00–11:40 | SQL Tool과 Streamlit | S15–S21 |
| 점심 | 11:40–13:20 | | |
| B4 | 13:20–14:00 | Claude Code와 개발 계획 | S22–S27 |
| B5 | 14:20–15:00 | Claude Code로 앱 개선 | S28–S33 |
| B6 | 15:20–16:00 | 지식 축적과 Skill | S34–S40 |
| B7 | 16:00–17:30 | 자유 실습과 Q&A | S41–S44, G02 |
| 부록 | — | 질문 대응·후속 학습 | A01–A06 |

총 52장 (본문 46 + 부록 6). 구간 표지는 없고 G01 시간표와 각 장면 상단 구간 표시로 위치를 안내한다. 애니메이션은 쓰지 않는다.

## 구현

- `index.html`: 원본 슬라이드 소스. 장면 id는 순번 `s-N`, 콘티 ID는 `data-scene-id`, 발표자 노트는 `.speaker-note`.
- `overview.html`: `scripts/sync_overview.py`로 `index.html`에서 재생성하는 검토 화면. Edit/Aim 포함.
- `DESIGN.md`: Notion 최소 적용 규칙 + 원문.
- `docs/`: 조사 자료, 출처 목록, 제작 계획서(`slide-plan-2026-09-13.md`), v0.1 스토리보드 보관본.
- `assets/`: 실제 화면 캡처 자리. 없는 장면은 점선 플레이스홀더.
- `exports/`: 최종 PDF/PPTX 위치.
- 기획·검토 산출물: 루트 `_workspace/` (content plan, visual plan, slide_copy, slide_ui, lecture_review, ppt_qa_report).

## 코드

```powershell
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --renumber
python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu
npx hyperframes lint topics\sk-hynix-ai-agent-guide-edu
```

## 테스트 방법

1. `overview.html`을 브라우저 또는 preview 서버에서 연다.
2. 52장이 순서대로 보이고 글자가 화면 밖으로 넘치지 않는지 확인한다.
3. `Edit`로 문구를 고치고 `Done`을 눌러 patch를 클립보드로 복사한다.
4. patch를 agent에 전달하면 `index.html`에 반영한 뒤 overview를 재생성한다.
5. 최종 확인 후 PDF 또는 PPTX export를 요청한다.

## 향후 개선사항

- 실제 실습 HTML·Streamlit·Claude Code·Dokmo 화면 캡처로 플레이스홀더 교체.
- 사내 모델·권한·설치 경로가 확정되면 실습 안내 장면 문구 확정.
- 사내 브랜드 디자인 문서가 생기면 `:root` 토큰만 교체.
