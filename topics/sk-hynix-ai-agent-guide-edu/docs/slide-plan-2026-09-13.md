# AI Agent Guide 사내 교육 — 슬라이드 제작 계획

작성일: 2026-09-13 · 개정: 2026-09-13 (사용자 결정 반영 v0.2)

## 확정된 결정 (v0.2)

| 항목 | 결정 |
|---|---|
| 디자인 기준 | `new_md/DESIGN-Notion.md`를 `DESIGN.md`로 고정. 교육 자료 컨셉에 맞춰 **최소한만** 사용 (오프화이트 배경, 근검정 글자, 파랑 액센트 하나, 헤어라인 카드, 그림자 없음, 스티커 팔레트 미사용, 남색 반전은 표지·마무리 2장만) |
| 폴더 처리 | 현재 폴더 `topics/sk-hynix-ai-agent-guide-edu/`를 그대로 topic으로 승격. 조사 자료는 `docs/`로 이동 |
| 구간 표지 D1–D7 | **생략**. 대신 하루 시간표 G01에서 구간·시각을 보여주고, 각 구간 첫 장면 상단에 작은 구간 라벨(예: "B2 · 10:00–10:40")을 넣는다 |
| 애니메이션 | **고려하지 않음**. PDF가 최종이므로 모든 장면은 정지 상태로 완성. HyperFrames 구조상 필수인 `data-start`/`data-duration`과 빈 paused 타임라인만 등록하고 GSAP 트윈은 쓰지 않는다 |
| 서브에이전트 | 슬라이드 단위 담당 3개 신설: `slide_content_writer`(내용), `slide_ui_designer`(UI 디자인), `lecture_expert`(강의 전문가). 정의는 `.claude/agents/*.md`와 `.codex/agents/*.toml` 양쪽에 둠 |

장수: 본문 44 + 시간표 G01 + 마무리 G02 = **46장**, 부록 6장 = **총 52장**.
대상 topic: `topics/sk-hynix-ai-agent-guide-edu/`
최종 산출물: 발표자용 PDF (16:9, 1920×1080). PPTX는 선택.
기준 문서: `ai_agent_guide_storyboard/_workspace/ppt_content_plan.md` (S01–S44, 부록 A01–A06), `ppt_visual_plan.md`, `topic_intake.md`, `storyboard.json`, `AI_Agent_Guide_강의소재_조사정리.md`, `research_claude.md`, `research_local.md`, `AI_Agent_Guide_출처목록.md`
(2026-09-14 이동: 조사 자료 4개는 이 폴더 `docs/`, v0.1 스토리보드는 `docs/storyboard_v0.1/`, v0.2 기획 3종은 저장소 루트 `_workspace/`에 있다. 진행 상태는 7절.)

---

## 1. 문제 분석 — 지금 어디까지 와 있나

이 저장소의 제작 파이프라인은 `intake → content plan → visual plan → HyperFrames build → overview QA → 사용자 Edit/Aim 검토 → PDF/PPTX export`다.

폴더에 있는 자료를 파이프라인 단계에 대응시키면 다음과 같다.

| 파이프라인 단계 | 폴더 안의 대응 자료 | 상태 |
|---|---|---|
| 조사·근거 | 강의소재 조사정리, 출처목록, research_claude, research_local | 완료 (조사 기준일 2026-09-13) |
| intake | `_workspace/topic_intake.md` | 완료 (v0.1). 브랜드 DESIGN 미선정 |
| content plan | `_workspace/ppt_content_plan.md` — 본문 40장 + 자유실습 진행 4장 + 부록 6장 | 완료 (v0.1) |
| visual plan | `_workspace/ppt_visual_plan.md` — 레이아웃 매핑, 글자 크기, 자산 목록 | 완료 (v0.1) |
| HyperFrames build | `index.html`, `overview.html`, `DESIGN.md`, `meta.json`, `hyperframes.json`, `exports/` | **없음** |
| overview QA / 사용자 검토 / export | — | **없음** |

즉, **무엇을 말할지는 이미 정해져 있고, 이 저장소에서 실제 슬라이드를 만드는 일이 남아 있다.** 이 계획은 그 제작 작업을 어떤 순서로, 어떤 단위로, 어떤 결정을 거쳐 진행할지 정한다.

### 기존 콘티의 시간표 (변경 없이 유지)

| 구간 | 시각 | 주제 | 이론 | 안내 실습 | 확인 | 슬라이드 |
|---|---|---|---:|---:|---:|---|
| B1 | 09:00–09:40 | LLM 원리와 첫 호출 | 24 | 14 | 2 | S01–S08 |
| B2 | 10:00–10:40 | 외부 근거와 기사 RAG | 14 | 22 | 4 | S09–S14 |
| B3 | 11:00–11:40 | SQL Tool과 Streamlit | 14 | 24 | 2 | S15–S21 |
| 점심 | 11:40–13:20 | | | | | |
| B4 | 13:20–14:00 | Claude Code와 개발 계획 | 16 | 20 | 4 | S22–S27 |
| B5 | 14:20–15:00 | Claude Code로 앱 개선 | 16 | 21 | 3 | S28–S33 |
| B6 | 15:20–16:00 | 지식 축적과 Skill | 16 | 18 | 6 | S34–S40 |
| B7 | 16:00–17:30 | 자유 실습과 Q&A | 자유 80 + 공유 10 | | | S41–S44 |

교육 활동 합계 330분, 본문 44장. 이론 슬라이드 약 27장에 이론 100분이므로 장당 약 3.7분이다. 실습 중심 하루 강의로 적절하다.

중심 메시지: **"LLM에게 맡길 일과 코드·데이터·사람이 책임질 일을 구분하면, 비전공자도 작은 업무 도구부터 만들고 개선할 수 있다."**

---

## 2. 설계 — 콘티에서 바꾸거나 더할 것

기존 콘티 ID(S01–S44, A01–A06)는 그대로 유지한다. 사용자 코멘트와 수정 요청을 번호로 연결하기 위해서다. 추가 장면은 별도 ID를 쓴다.

### 2-1. 추가할 장면 (총 2장)

| 새 ID | 위치 | 내용 | data-skill | 이유 |
|---|---|---|---|---|
| G01 | S01 다음 | 하루 시간표 (7구간·휴식·점심·자유실습) | `steps` | 전체 흐름을 한 장에서 보여줌. 구간 표지를 생략하는 대신 이 장이 위치 안내를 맡음 |
| G02 | S44 다음 | 오늘 남길 4가지 성과 (조사정리 1절의 학습 성과 4개) | `title-bullets` | 폐회를 중심 메시지로 마무리 |

구간 표지 D1–D7은 사용자 결정으로 생략한다. 대신 각 구간의 첫 장면(S01, S09, S15, S22, S28, S34, S41) 상단에 작은 구간 라벨을 넣는다.

결과: 본문 44 + 추가 2 = **46장**, 부록 6장 = **총 52장**.

### 2-2. 레이아웃 재배분

콘티는 `title-bullets`를 17장에 쓴다 (실습 안내 7장, 자유실습 4장, 확인·요청 화면 등). visual plan 4절도 "모든 화면을 카드형 UI로 만들지 않는다"고 경고한다. 허용 data-skill 11종 중 콘티가 안 쓴 `stat`, `title-tags`, `quote`, `evolution-flow`를 목적에 맞게 사용한다.

| 장면 | 콘티 레이아웃 | 제안 | 이유 |
|---|---|---|---|
| S02 강사 소개 | split | `title-tags` | 경력·프로젝트를 태그로, 화면 캡처 확보 전에도 완성 가능 |
| S08/S13/S19/S26/S32/S37 실습 안내판 | title-bullets | `title-bullets` 유지 + 시간 배분을 숫자 블록으로 | 안내판 성격은 맞음. 4분/6분/4분/2분 같은 배분을 크게 보여 타이머 없이도 읽히게 |
| S17 스크립트·Workflow·Agent | compare | `evolution-flow` 검토 후 결정 | 단, 콘티는 "진화 단계로 표시하지 않는다"고 명시했으므로 우열 느낌이 나면 `compare` 유지 |
| S21 오전 실습 전체 구조 | split | `split` 유지, 구조도는 CSS 개념도 | |
| S39 자유 실습 선택 주제 | compare | `compare` 유지 (3열) | |
| S44 실습 공유 | title-bullets | `quote` | 발표 질문 3개를 큰 글자로 |
| G02 마무리 | — | `title-bullets` | |

나머지 `steps`(S04/S10/S16/S28), `split`, `compare`, `title-image`(S20)는 콘티 그대로.

### 2-3. 애니메이션은 쓰지 않는다 (결정됨)

`storyboard.json`의 `presentation_minutes`는 수업 운영 시간이고, HyperFrames의 `data-start`/`data-duration`은 원래 애니메이션 초 단위다. PDF가 최종이므로 애니메이션은 고려하지 않는다.

- 모든 장면은 정지 상태로 완성한다. 클릭·호버·순차 강조가 있어야만 읽히는 장면은 만들지 않는다.
- HyperFrames 구조와 lint가 요구하는 것만 남긴다: 각 씬에 `data-start`/`data-duration`(씬당 5초, 순번×5), `#root`에 전체 `data-duration`(52장 × 5초 = 260초), `window.__timelines.main`에 빈 paused 타임라인 등록. GSAP 트윈은 작성하지 않는다.
- overview.html은 index.html의 마크업을 복제하므로 애니메이션이 없으면 두 파일 동기화도 단순해진다.

### 2-4. 디자인 기준 (결정됨: Notion 최소 적용)

`new_md/DESIGN-Notion.md`를 `DESIGN.md`로 고정한다. Notion 문서는 마케팅 사이트 기준이라 교육 자료에는 다음처럼 **최소한만** 가져온다.

| 항목 | Notion 원문 | 이 교육 자료에서의 적용 |
|---|---|---|
| 배경 | 따뜻한 오프화이트 `#f6f5f4`, 카드는 흰색 | 그대로. 슬라이드 배경 오프화이트, 카드·패널 흰색 + 1px 헤어라인 `#e6e6e6` |
| 글자색 | 근검정 `#000000`(95%), 보조 `#31302e`, 흐림 `#615d59`, 캡션 `#a39e98` | 그대로 4단계 |
| 구조 액센트 | 파랑 `#0075de` 하나 | 그대로. 강조 밑줄·현재 단계 표시·링크에만 |
| 스티커 팔레트 6색 | 장식 전용 | **사용 안 함**. 예외: 비교 화면의 상태 점(초록 `#1aae39`, 주황 `#dd5b00`) |
| 남색 반전 밴드 `#213183` | 히어로 한 곳 | 표지 S01과 마무리 G02 두 장에만 |
| 그림자 | 여러 겹 미세 그림자 | **사용 안 함**. 헤어라인만 |
| 모서리 | 4–16px, pill | 카드 12px 하나만 |
| 폰트 | Inter, 제목 700 자간 음수, 본문 400 | Paperlogy 우선, 폴백 `Pretendard, "Malgun Gothic", Inter, sans-serif`. 제목 700 자간 음수, 본문 400 유지 |
| 크기 | 웹 기준 64px 이하 | 1920×1080 기준 제목 72–88px, 항목 40–48px, 보조 32–36px, 캡션 28px |

색·폰트·크기는 모두 `:root` 변수로 두어 나중에 사내 브랜드 문서가 생기면 변수만 교체한다. 사내 렌더 환경에서 한글 폰트 제공 여부를 확인하고 외부 CDN에만 의존하지 않는다.

### 2-5. topic 폴더 처리 (결정됨: 기존 폴더 승격)

현재 폴더 `topics/sk-hynix-ai-agent-guide-edu/`에 `index.html`, `overview.html`, `DESIGN.md`, `BRIEF.md`, `topic.json`, `meta.json`, `hyperframes.json`, `assets/`, `exports/`를 추가한다. 조사 자료 4개 md는 `docs/`로 옮기고, `ai_agent_guide_storyboard/_workspace/`의 기획 3종은 저장소 규약대로 루트 `_workspace/`에 복사해 갱신한다. `validate_topic.py`가 추가 파일을 막지 않는 것은 확인했다.

### 2-6. 사실 경계와 문구 QA 체크리스트

조사정리 5절과 research_claude 2절의 "고쳐야 할 표현"을 빌드 단계 체크리스트로 승격한다. 각 슬라이드 문구를 쓸 때 다음을 검사한다.

1. temperature 0 = 정확·항상 동일 → "선택의 다양성 감소. 사실성·완전 재현성은 보장 안 함"
2. RAG = 학습·기억·환각 제거 → "검색한 외부 근거를 현재 답변에 이용. 검색·자료 품질·검증은 여전히 필요"
3. Tool 하나 = 자율 Agent → "정해진 순서의 작업 흐름과, 모델이 다음 행동을 고르는 Agent를 구분"
4. 로컬 실행 = 자료가 로컬에만 머묾 → "실행 위치와 모델 처리 위치는 다름"
5. 로컬 접근 = 컴퓨터로 하는 모든 일 → "허용된 파일·명령 도구와 권한 범위"
6. Skill·MCP·Subagent = 상하위 단계 → "절차·연결 규약·작업 분담이라는 서로 다른 역할"
7. CLAUDE.md = 권한 강제 → "모델이 읽는 지침. 보안 장치 아님"
8. Obsidian 연계 = 나와 같은 판단을 하는 분신 → "과거 결정과 근거를 찾아 판단을 돕는 보조자"
9. Transformer 원형 = 현재 모든 LLM → "원 논문은 encoder–decoder, 현재 많은 생성 모델은 decoder 중심"
10. LangChain → LangGraph → Deep Agents 순서로 모두 배워야 → "문제에 필요한 추상화 수준을 고름"
11. 오전 vLLM API를 오후 Claude Code에서 그대로 → "지원 모델·인증·게이트웨이는 별도 확인"
12. 성능 수치·절감 시간·이용자 수 → 측정 자료 없으면 넣지 않음
13. 사내 모델명·주소·API 키·설치 명령 → 슬라이드에 넣지 않고 역할 이름만 표시

Part Finder는 "공개 Beta 설계 기반 개념 예시", Dokmo·Obsidian은 "개인 기록"으로 표시한다.

### 2-7. 자산 처리 원칙

visual plan 5절의 자산 표에서 실제 캡처가 필요한 것은 강사만 제공할 수 있다. 흐름 검토가 막히지 않도록 두 그룹으로 나눈다.

| 그룹 | 장면 | 처리 |
|---|---|---|
| 자산 없이 완성 가능 | S01, G01, S03–S07, S09–S12, S14–S17, S19, S22–S25, S27, S28, S30, S33, S35, S36, S38–S43, G02, A01–A06 | CSS 개념도·텍스트·가상 데이터로 1차 완성 |
| 실제 화면 대기 | S02(강사 프로젝트), S08(고정 입력 호출 결과), S13(기사 본문·검색 결과), S18(가상 카탈로그는 제작 가능), S20·S24·S29·S32(Streamlit), S26(Claude Code), S31(Dokmo), S34·S37(Vault 예제) | 점선 박스 + "실제 화면 교체 예정" 라벨로 자리만 잡고, 사용자가 `assets/`에 넣으면 교체 |

가상 데이터(장비별 건수 CSV, 가상 카탈로그 3행, 교육용 스키마)는 제작 시 만들되 "개념 예시"를 표시한다.

---

## 3. 구현 — 단계별 작업 순서

### 3-0. 서브에이전트 구성 (결정됨)

기존 5개 에이전트는 **덱 단위**, 신설 3개는 **슬라이드 단위**로 역할을 나눈다. 같은 일을 두 곳에서 하지 않도록 경계를 둔다.

| 에이전트 | 단위 | 하는 일 | 산출물 |
|---|---|---|---|
| `topic_intake_router` (기존) | 덱 | 요청·DESIGN·출력 타입 정리 | `_workspace/topic_intake.md` |
| `ppt_content_planner` (기존) | 덱 | 줄거리·장면 순서·data-skill 초안 | `_workspace/ppt_content_plan.md` |
| `ppt_visual_designer` (기존) | 덱 | 디자인 시스템(`:root` 변수, 폰트, 여백 규칙) | `_workspace/ppt_visual_plan.md` |
| **`slide_content_writer`** (신설) | 슬라이드 | 화면 문구·발표자 노트·출처 최종 문장. 사실 경계 체크리스트 대조 | `_workspace/slide_copy/<차수>.md` |
| **`slide_ui_designer`** (신설) | 슬라이드 | 장면별 배치·글자 크기·색 역할·플레이스홀더 규격. 애니메이션 없음 | `_workspace/slide_ui/<차수>.md` |
| **`lecture_expert`** (신설) | 차수 | 강사·교수설계 검토 9항목. 빌드 전·후 2회 | `_workspace/lecture_review/<차수>-pre|post.md` |
| `hyperframes_ppt_builder` (기존) | 덱 | index.html·overview.html 구현 | topic 파일 |
| `ppt_overview_qa` (기존) | 덱 | 구조·lint·export gate | `_workspace/ppt_qa_report.md` |

차수(B1–B7) 하나를 처리하는 순서:

```text
slide_content_writer ─┐
                      ├─> lecture_expert (pre) ─> 수정 요청 반영 ─> hyperframes_ppt_builder
slide_ui_designer ────┘                                                      │
                                                                             v
                                       lecture_expert (post) + ppt_overview_qa ─> 사용자 overview 검토
```

- `slide_content_writer`와 `slide_ui_designer`는 같은 차수를 병렬로 진행할 수 있다. 단 UI 담당은 문구 결과를 읽어야 하므로 문구가 먼저 끝난 뒤 시작하거나, 콘티 초안 문구로 시작한 뒤 최종 문구로 재확인한다.
- `lecture_expert`의 수정 요청은 담당자별로 나뉘어 오므로 오케스트레이터(이 세션)가 해당 에이전트에 다시 전달한다. 보류 항목은 사용자에게 모아서 묻는다.
- 정의 파일: `.claude/agents/{slide_content_writer,slide_ui_designer,lecture_expert}.md`(Claude Code가 읽음), `.codex/agents/*.toml`(저장소 규약·`validate_codex_port.py` 검증 통과). 새 `.claude/agents` 파일은 세션을 다시 시작해야 Agent 도구 목록에 나타날 수 있다.

### Phase 0. 골격 (결정 완료, 바로 진행 가능)

1. `DESIGN.md`는 Notion 문서 복사 + 상단에 "교육 자료 최소 적용 규칙"(2-4 표) 추가.
2. topic 승격: `DESIGN.md` 복사, `BRIEF.md`(목적·대상·시간표·중심 메시지), `topic.json`, `meta.json`, `hyperframes.json`(루트 복사본), `assets/`, `exports/` 생성. 조사 자료를 `docs/`로 이동.
3. 이 저장소 규약의 `_workspace/` 문서 갱신: 기존 `ai_agent_guide_storyboard/_workspace/` 3개 파일을 `_workspace/`로 옮기고, 2-1·2-2의 추가 장면과 레이아웃 변경을 `ppt_content_plan.md`·`ppt_visual_plan.md`에 반영. `storyboard.json`도 동기화.
4. 참고 스킬 읽기: `.codex/skills/hyperframes/SKILL.md`, `house-style.md`, `hyperframes-slide/SKILL.md`, 사용할 `hyperframes-slide-work-*`(title, title-bullets, title-tags, split, compare, steps, title-image, quote, stat, evolution-flow), `hyperframes-overview/template.html`, `gsap/`.

완료 기준: `python scripts/validate_topic.py topics/sk-hynix-ai-agent-guide-edu`가 필수 파일 누락 오류 없이 통과 (index/overview는 골격만).

### Phase 1. index.html·overview.html 골격

1. `index.html`: `#root`에 `data-output-type` 없음(deck), `data-composition-id="main"`, `data-width="1920"`, `data-height="1080"`, `data-duration="260"`. `:root` 변수(색·폰트·크기)를 DESIGN.md의 최소 적용 규칙 기준으로 정의. 씬 공통 CSS와 data-skill별 CSS. `window.__timelines.main`에 빈 paused 타임라인만 등록(트윈 없음).
2. `overview.html`: `hyperframes-overview/template.html` 기반 완성형. `:root` 변수·씬 CSS·마크업을 index에서 복제. `class="edit-btn"`, Aim UI(`data-aim`), `data-editable="true"`, Done 시 patch 클립보드 복사. 각 씬에 `data-slide` 번호와 `.speaker-note`(콘티의 발표 멘트 요지)를 넣어 PPTX export 시 발표자 노트로 들어가게 한다.
3. 글자 크기 출발점 (visual plan 4절): 제목 72–88px, 본문 40–48px, 출처 28–32px. 슬라이드당 주제 하나, 핵심 항목 1–4개. 코드 비교는 영역당 5–7줄.

완료 기준: 표지 S01 한 장으로 validate + `npx hyperframes lint` 통과, `npm run preview:port`로 렌더 확인.

### Phase 2. 빌드 A — 오전 (S01, G01, S02–S21: 22장)

B1 → B2 → B3 순서로 3-0의 차수 처리 순서를 적용한다. 차수마다 `slide_content_writer` → `slide_ui_designer` → `lecture_expert`(pre) → 수정 반영 → `hyperframes_ppt_builder` → validate + lint → `lecture_expert`(post). 2-7 대기 자산은 플레이스홀더로 둔다.

완료 기준: 22장이 index와 overview 양쪽에 같은 순서·번호로 존재. lint 통과. `npm run snapshot -- topics/sk-hynix-ai-agent-guide-edu -- --at <씬 순번×5-1>`로 대표 장면 5개 이상 스냅샷 확인. 차수별 `lecture_review/*-post.md`에 "수정 필요" 항목이 남아 있지 않음.

### Phase 3. overview 검토 1회차 (사용자)

사용자가 `overview.html`에서 Edit/Aim으로 수정하고 patch를 붙여넣으면 index·overview 양쪽에 반영한다. 이 시점에 실제 화면 자산이 있으면 `assets/`에 받아 교체한다.

### Phase 4. 빌드 B — 오후 + 부록 (S22–S44, G02, A01–A06: 30장)

B4 → B5 → B6 → B7 → 부록 순서로 Phase 2와 같은 차수 처리 순서를 적용한다. 부록은 본문 뒤 별도 번호 구간(`data-slide` 47–52)으로 두고 각 장 제목에 "부록" 표기. 부록은 `lecture_expert` 검토를 생략할 수 있다.

완료 기준: 총 52장. validate + lint 통과. `_workspace/ppt_qa_report.md` 작성(구조, data-skill, edit-btn, Aim, lint 결과, 문구 체크리스트 결과, 플레이스홀더 남은 장면 목록).

### Phase 5. overview 검토 2회차 (사용자)

전체 59장 검토. 남은 플레이스홀더 교체. 사용자가 "최종 확인"을 말하기 전에는 export하지 않는다 (Export gate).

### Phase 6. Export

1. PPTX: `.codex/skills/hyperframes-overview-pptx-export/scripts/export_overview_to_pptx.mjs`로 `--expected-slides 52`. `.speaker-note`가 발표자 노트로 들어간다.
2. PDF: 같은 스크립트가 만든 1920×1080 PNG 52장을 PDF로 묶는 경로와, 브라우저 인쇄 경로 중 사내 환경에서 안정적인 쪽을 확인해 사용. 한 장면 한 페이지, 편집 UI·썸네일·진행 도구 제외.
3. 출력한 PDF 전 페이지를 렌더해 순서·잘림·한글 폰트 확인. `exports/`에 저장하고 버전·검증일을 파일명에 표시.

---

## 4. 코드 — 장면 구현 규약 요약

```html
<!-- 씬 하나의 기본 형태 (index.html) -->
<section class="scene clip"
         data-skill="split"          <!-- 허용 11종 중 하나 -->
         data-start="50"             <!-- HyperFrames 구조상 필수. 순번×5초. 수업 시간 아님 -->
         data-duration="5"           <!-- HyperFrames 구조상 필수 -->
         data-track-index="0"
         id="s10">                   <!-- 콘티 ID를 소문자로 -->
  <span class="block-label">B2 · 10:00–10:40</span>   <!-- 구간 첫 장면에만 -->
  <!-- 콘텐츠: 제목, 좌우 영역, 출처. 모두 정지 상태로 완성 -->
</section>
```

- 콘티 ID(S10)와 HTML `id`(`s10`), overview의 `data-slide`(순번)를 매핑표로 `_workspace/ppt_visual_plan.md`에 기록한다.
- 타임라인은 `window.__timelines.main = gsap.timeline({ paused: true })` 한 줄만 둔다. 트윈을 추가하지 않는다. 씬은 처음부터 최종 상태로 보이게 CSS만으로 배치한다.
- 색·폰트·크기는 전부 `:root` 변수. DESIGN 교체 시 변수만 바꾼다.

---

## 5. 테스트 방법

| 시점 | 명령 | 확인할 것 |
|---|---|---|
| HTML 수정 후 매번 | `python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu` | 필수 파일, data-skill, edit-btn, Aim |
| HTML 수정 후 매번 | `npx hyperframes lint topics\sk-hynix-ai-agent-guide-edu` | HyperFrames 문법 |
| 차수 완료 시 | `npm run preview:port -- topics/sk-hynix-ai-agent-guide-edu` | 렌더·잘림·폰트 |
| 차수 완료 시 | `npm run snapshot -- topics/sk-hynix-ai-agent-guide-edu -- --at ...` | 대표 장면 최종 상태 |
| Phase 4 완료 시 | index·overview 씬 수·순서 비교 스크립트 | 양쪽 동기화 |
| Export 후 | PDF 전 페이지 렌더 | 52장, 순서, 한글, 편집 UI 없음 |
| 에이전트 정의 변경 시 | `python scripts\validate_codex_port.py` | `.codex/agents/*.toml` 필수 필드·섹션 |

lint를 못 돌리면 이유를 보고한다. 문구 체크리스트(2-6)는 자동화 대상이 아니므로 QA 보고서에 장면별로 수기 기록한다.

---

## 6. 향후 개선사항과 미확정 항목

계획을 실행으로 옮기기 전·중에 사용자 확인이 필요한 항목이다. 콘티 7절과 조사정리 10절의 내용을 그대로 이어받는다.

- Naver 기사·Streamlit 최종 실습 HTML과 ZIP 판본. 실습 안내판(S08/S13/S19/S20/S26/S32/S37)의 단계 이름을 실제 HTML 장 이름과 맞춰야 한다. → 2026-09-15: 최종 판본이 정해진 뒤 결정(v0.4 계획서 12-1절 7번).
- 사내 모델·임베딩·도구 호출 지원 범위, DataLake 읽기 권한, Claude Code 승인 설치·접속 방식. 슬라이드에는 역할 이름만 넣지만 실습 안내 문구의 전제가 된다.
- 공개 가능한 Part Finder·Dokmo·Streamlit·Claude Code 화면 캡처.
- 16:00–16:20 휴식을 별도로 둘지. 두면 자유 실습이 70분이 되고 S41–S43 시각을 조정한다. → **2026-09-15 결정: 휴식 없음(현행 유지)**.
- 사내 브랜드 DESIGN 문서가 나중에 생기면 `:root` 변수만 교체한다.

이 계획은 제작 순서와 결정 사항을 정한 문서이며, HTML·PDF 제작이나 사내 실행 검증을 완료했다는 뜻이 아니다.

---

## 7. 진행 상태 (v0.3 · 2026-09-14)

Phase 0–4를 shrimp-task-manager 작업 10개로 나눠 계획 → 실행 → 검증 순서로 진행했다. Phase 3(사용자 overview 검토 1회차)은 사용자 부재로 에이전트 내부 검토로 대신했으며, 사용자 검토는 아직 하지 않았다.

| Phase | 결과 |
|---|---|
| 0 topic 승격 | `DESIGN.md`(Notion 최소 적용), `BRIEF.md`, 메타 파일, `assets/`·`exports/`, 조사 자료 `docs/` 이동, `_workspace/` v0.2 기획 3종·52행 매핑표 |
| 1 골격 | `index.html` 디자인 토큰·컴포넌트 CSS, `scripts/sync_overview.py`(overview 재생성·순번 정리·최신 검사), 컴포넌트 카탈로그 |
| 2 오전 22장 | 문구 → UI → 강사 사전 검토 → 빌드 → 검증. 빌드 검수로 격자 높이·코드 글꼴 문제 수정 |
| 3 내부 검토 1회차 | 강사 사후 검토(스크린샷 판독) 4건 반영 |
| 4 오후·부록 30장 | 같은 루프로 제작, 총 52장 |

확정 결정 대비 달라진 점:

- 장면 id는 계획의 `s10` 대신 **순번 `s-N`** 을 쓴다. overview patch의 `## Slide N`과 맞추기 위해서다. 콘티 ID는 `data-scene-id`에 둔다.
- 오후 문구 담당을 2개가 아닌 3개(B4–B5, B6–B7+G02, 부록)로 나눴다.
- 코드 글꼴을 JetBrains Mono 웹폰트로 고정했다. 브라우저와 HyperFrames 렌더러의 폭 차이 때문이다.
- `split-grid`·`compare-grid`는 남은 높이를 채우지 않는다(`.fill` 변형으로만 채움).

남은 일:

1. 사용자 overview 검토 (Edit/Aim patch → `index.html` 반영 → `sync_overview.py`).
2. `_workspace/ppt_qa_report.md` 사용자 확인 목록(P1–P5, N1–N2, Q1–Q7) 답변과 자리표시 교체.
3. 실제 화면 자산(S20 Streamlit 등) 교체.
4. 사용자 최종 확인 후 Phase 6 PDF/PPTX export.
