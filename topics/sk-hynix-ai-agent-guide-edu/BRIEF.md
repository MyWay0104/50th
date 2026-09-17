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
| B1 | 09:00–09:40 | LLM 원리와 첫 호출 | S01, G01, G00, S02–S08 |
| B2 | 10:00–10:40 | 외부 근거와 기사 RAG | S09–S14 |
| B3 | 11:00–11:40 | SQL Tool과 Streamlit | S15–S21 |
| 점심 | 11:40–13:20 | | |
| B4 | 13:20–14:00 | Claude Code와 개발 계획 | S22–S27 |
| B5 | 14:20–15:00 | Claude Code로 앱 개선 | S28–S33 |
| B6 | 15:20–16:00 | 지식 축적과 Skill | S34–S40 |
| B7 | 16:00–17:30 | 자유 실습과 Q&A | S41–S44, G02 |
| 부록 | — | 질문 대응·후속 학습 | A01–A10 |

총 57장 (본문 47 + 부록 10, v0.4). 구간 표지는 없고 G01 시간표와 각 장면 상단 구간 표시로 위치를 안내한다. 애니메이션은 쓰지 않는다.

v0.4 개정(2026-09-16): 기-승-전-결 막 태그 7곳, 장면마다 한 줄 요지(`.thesis`)와 설명 문단(`.explain`), 모든 장면에 시각 요소 1개 이상(인라인 `.dg` 도식·원 논문 그림·플레이스홀더), G00(왜 이런 순서로 배우나)과 부록 A07–A10(LangGraph·Agentic RAG·하네스·HITL) 추가. 결정 원본은 `docs/slide-plan-v0.4-visual-narrative.md` 12-1절.

final-touch(2026-09-17): 사용자 수정 12건 반영 — SK hynix 주황 테마(`#dd5b00`·`#793400`), 구간 표시(B1–B7)·쪽번호·기승전결 태그 삭제, 첫 시간표 밖 시간 정보 삭제(실습 안내판은 순서 번호), 화면 존댓말, 제목 간결화(부록 '부록 ·'), 출처는 공식 문서·논문만, 로고·아이콘 보강. 기록은 `_workspace/final_touch.md`.

v0.5 재구성(2026-09-17 밤, `ROADMAP1.md`): 사내 실습 흐름(오전 5구간·오후 3구간)에 맞춰 57장 → **50장**으로 재편. 시각은 G01(시작·점심·종료)과 G03(점심 안내)에만 두고 구간별 시각은 없음(강사가 유연하게 진행). 실습 안내판 5개(실습 1~5) + 선택 과제(M01), 소단계마다 개념 칩. 신설 E01·L01·R01·G03·C01~C04·M01, 오후 축은 "오전 챗봇 개선"에서 "Claude Code 사용 방향 세 가지"로. 부록 10장 유지(A04에 Skill 통합). 장면 매핑표 `_workspace/roadmap1/scene_map_v0.5.md`, v0.4 원본 백업 `_workspace/roadmap1/backup_v0.4/`. 사용자 overview 검토·export 대기.

## 구현

- `index.html`: 원본 슬라이드 소스. 장면 id는 순번 `s-N`, 콘티 ID는 `data-scene-id`, 발표자 노트는 `.speaker-note`.
- `overview.html`: `scripts/sync_overview.py`로 `index.html`에서 재생성하는 검토 화면. Edit/Aim 포함.
- `DESIGN.md`: Notion 최소 적용 규칙 + 원문.
- `docs/`: 조사 자료, 출처 목록, 제작 계획서(`slide-plan-2026-09-13.md`), v0.4 콘티(`slide-plan-v0.4-visual-narrative.md`), v0.1 스토리보드 보관본.
- `assets/img/`: 원 논문 그림(`b1/`), 참고 영상 썸네일(`common/`), 승인 카드 그림(`appendix/`). 강사 캡처가 없는 장면은 `[IMG-PLACEHOLDER · P-<장면ID>]` 점선 자리표시.
- `exports/`: 최종 PDF/PPTX 위치.
- 기획·검토 산출물: 루트 `_workspace/` (content plan, visual plan, slide_copy, slide_ui, lecture_review, ppt_qa_report, v0.4_progress).

## 코드

```powershell
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --renumber
python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu
npx hyperframes lint topics\sk-hynix-ai-agent-guide-edu
```

## 테스트 방법

1. `overview.html`을 브라우저 또는 preview 서버에서 연다.
2. 50장이 순서대로 보이고 글자가 화면 밖으로 넘치지 않는지 확인한다.
3. `Edit`로 문구를 고치고 `Done`을 눌러 patch를 클립보드로 복사한다.
4. patch를 agent에 전달하면 `index.html`에 반영한 뒤 overview를 재생성한다.
5. 최종 확인 후 PDF 또는 PPTX export를 요청한다.

## 향후 개선사항

- 실제 실습 HTML·Streamlit·Claude Code·ddokmo 화면 캡처로 플레이스홀더 10곳 교체.
- 사내 모델·권한·설치 경로가 확정되면 실습 안내 장면 문구 확정.
- 사내 브랜드 디자인 문서가 생기면 `:root` 토큰만 교체.
