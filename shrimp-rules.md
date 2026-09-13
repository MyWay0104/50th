# Development Guidelines

AI Agent 전용 작업 규칙이다. 일반 개발 지식은 적지 않는다. 이 저장소에서만 통하는 규칙만 적는다.

## 1. 프로젝트 개요

- HyperFrames(HTML + GSAP composition)로 **16:9 발표 슬라이드덱(`deck`)** 또는 **카드뉴스(`card-news`)** 를 topic 단위로 제작하는 작업 공간이다.
- 일반 애플리케이션이 아니다. 빌드 산출물·테스트 프레임워크·npm 의존성이 **없다**. `npx hyperframes`를 그때그때 받아 실행한다.
- **기본 최종 산출물은 PDF/PPTX**다. MP4는 사용자가 영상을 명시적으로 요청할 때만 만든다.
- **규칙 원본은 `AGENTS.md`** 다. 이 문서·`CLAUDE.md`·스킬 문서와 충돌하면 `AGENTS.md`를 따른다.
- 환경: Windows / PowerShell, Python 3.11+ (`tomllib` 사용), Node 20+.

## 2. 디렉터리 맵

| 경로 | 역할 | 수정 규칙 |
|---|---|---|
| `AGENTS.md` | 저장소 전체 규칙 원본 | 규칙 변경 시에만 수정. 수정하면 7절 동기화 표 적용 |
| `CLAUDE.md` | Claude Code용 요약 안내 | `AGENTS.md`와 내용이 어긋나지 않게 유지 |
| `new_md/DESIGN-*.md` | 사용자가 넣은 디자인 원본 | **읽기 전용**. 편집하지 말고 topic의 `DESIGN.md`에 복사해 사용 |
| `topics/<slug>/` | 독립 HyperFrames 프로젝트 1개 | 작업 대상 |
| `topics/_template/`, `topics/_card_news_template/` | scaffold 참고본 | **수정 금지** |
| `topics/oxxodok_50th/` | 완성 사례(참고용) | **수정 금지**. 구조를 참고만 |
| `_workspace/` | 파이프라인 단계 산출물 | `orchestration-plan.md` 삭제 금지(검증기가 요구) |
| `.codex/agents/*.toml` | 역할별 subagent 계약 (8개) | 7절 동기화 표 적용 |
| `.claude/agents/*.md` | Claude Code 실행용 subagent 정의 (슬라이드 단위 3개) | `.codex/agents`의 같은 이름 toml과 역할을 일치시킴 |
| `.agents/skills/ppt-hyperframes-deck/` | 반복 제작 절차 + `references/ppt-checklist.md` | QA 기준 변경 시 수정 |
| `.codex/skills/` | HyperFrames 문법·레이아웃·overview·export 스킬 | **읽기 전용**. 문법의 근거로만 사용 |
| `.codex/skills/skills/` | 위 스킬의 중첩 복사본 | **참조 금지**. 최상위 `.codex/skills/`만 기준으로 사용 |
| `scripts/` | `create_topic.py`, `validate_topic.py`, `validate_codex_port.py` | 수정 시 7절 동기화 표 적용 |
| `shrimp_data/` | shrimp-task-manager `DATA_DIR` | **수동 편집 금지**. shrimp 도구로만 변경 |
| `renders/`, `snapshots/` | 렌더·스냅샷 출력 | gitignore 대상. 커밋하지 않음 |
| `tmp/` | 임시 폴더 | 산출물을 두지 않음. 임시 파일은 세션 scratchpad 사용 |

## 3. topic 폴더 규약

### 3-1. 필수 구성 (`validate_topic.py`가 검사)

- 파일: `index.html`, `overview.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`
- 폴더: `exports/`
- 권장: `BRIEF.md`, `topic.json`, `assets/`, `docs/`(조사 자료·계획서)

### 3-2. `index.html` 규약

- `#root`에 `data-composition-id="main"`, `data-start="0"`, `data-width`, `data-height`, 전체 `data-duration`을 둔다.
- card-news이면 `#root`에 `data-output-type="card-news"`를 둔다. deck은 생략하거나 `data-output-type="deck"`.
- 각 장면은 다음 형태를 따른다. `id`는 **순번 `s-N`** 이다. overview patch의 `## Slide N`이 `id="s-N"`과 `data-slide="N"`에 대응하기 때문이다. 기획 장면 ID는 `data-scene-id`에 둔다.

```html
<section id="s-12" class="scene clip" data-skill="split" data-scene-id="S10" data-start="55" data-duration="5" data-track-index="0">
```

- `<style id="scene-styles">`를 쓰는 topic에서는 `@font-face`·`:root` 토큰·장면 CSS를 모두 그 안에 둔다. html/body/#root 캔버스 규칙은 별도 `<style>`에 둔다.
- 발표자 노트는 장면 안 `<aside class="speaker-note">`에 두고 CSS로 숨긴다. PPTX export가 노트로 복사한다.
- 장면 안에 `<section>`을 중첩하지 않는다.

- 타임라인은 `window.__timelines.main = gsap.timeline({ paused: true })`로 **동기 코드에서** 등록한다.
- 색·폰트·크기는 `:root` CSS 변수로만 정의한다. 장면 CSS에 hex 값을 직접 쓰지 않는다.

### 3-3. 허용 `data-skill` 값

| 출력 타입 | 크기 | 허용 값 |
|---|---|---|
| `deck` | 1920×1080 | `title`, `title-bullets`, `title-image`, `title-tags`, `split`, `stat`, `steps`, `compare`, `evolution-flow`, `quote`, `kindergarten-notice` |
| `card-news` | 1080×1080 (세로 요청 시 1080×1920) | `photo-cover`, `video-cover`, `stat`, `image-feature` |

- deck과 card-news 값을 **섞지 않는다**. `stat`만 양쪽에 존재한다.
- 장면 구현 전 해당 `.codex/skills/hyperframes-slide-work-<skill>/SKILL.md`(deck) 또는 `hyperframes-card-news-work-<skill>/SKILL.md`(card-news)를 읽는다.

### 3-4. `overview.html` 필수 요소 (`validate_topic.py`가 검사)

- `class="edit-btn"` 버튼
- `Aim` 선택 UI 또는 `data-aim`
- `data-editable="true"` 편집 영역
- Done 클릭 시 agent가 읽을 수 있는 patch를 클립보드로 복사. 서버 저장 API 없이 static fallback으로 동작해야 한다.
- PPTX export를 쓸 topic은 각 장면을 `#detail-frame .scene[data-slide="<순번>"]`로 두고, 발표자 노트를 `.speaker-note`에 넣는다 (`hyperframes-overview-pptx-export` 스킬 요구).

### 3-5. 완성형 overview 구조

- 완성형 overview는 iframe이 아니다. **`index.html`의 `:root` 변수·장면 CSS·장면 마크업을 복제**해 담는다. 기반 파일은 `.codex/skills/hyperframes-overview/template.html`이다.
- `create_topic.py`가 만드는 overview는 3장짜리 단순 카드형이다. 완성형으로 교체할 때 이 차이를 인지한다.
- `index.html`에 `<style id="scene-styles">`가 있는 topic은 **`scripts/sync_overview.py`로 overview를 재생성**한다. overview를 손으로 고치지 않는다. `oxxodok_50th`처럼 이 규약이 없는 topic에서는 스크립트가 아무것도 쓰지 않고 실패한다.

```powershell
python scripts\sync_overview.py topics\<slug> --renumber   # 순번 정리 + overview 재생성
python scripts\sync_overview.py topics\<slug> --check      # 최신 여부만 검사
```

## 4. 기능 구현 규칙

### 4-1. 새 topic 생성

- `npm run new-topic -- --name <slug> --title "<제목>" --company "<회사>" --type deck|card-news`를 사용한다.
- 디자인 파일을 직접 지정할 때는 `--design new_md/DESIGN-x.md`를 추가한다.
- `--company` 이름이 들어간 `new_md/DESIGN-*.md`가 없으면 첫 파일이 선택된다. **생성 후 `DESIGN.md`가 의도한 파일인지 반드시 확인**한다.
- 기존 자료 폴더를 topic으로 승격할 때는 3-1 필수 구성을 직접 추가하고, `hyperframes.json`은 루트 파일을 복사한다.

### 4-2. 장면 추가·수정

- 기획 문서의 장면 ID(예: `S10`, `G01`, `A03`)를 `data-scene-id`로 유지한다. HTML `id`는 순번 `s-N`, overview `data-slide`도 같은 순번이다. 매핑표는 `_workspace/ppt_content_plan.md` 상단에 있다.
- 장면을 추가해도 **기획 ID를 재번호하지 않는다**. 새 장면은 새 접두어·번호를 부여한다. 순번 `s-N`은 `sync_overview.py --renumber`가 다시 매긴다.
- `data-start`·`data-duration`·`.page-num`·`#root` 전체 길이는 `--renumber`로 맞춘다. 손으로 계산하지 않는다.

### 4-3. 디자인 적용

- 색·폰트·레이아웃·금지 스타일은 topic의 `DESIGN.md`만 근거로 삼는다.
- 한국어 폰트는 Paperlogy를 우선한다. 폴백 스택에 로컬 한글 폰트를 넣는다.
- PDF가 최종인 topic은 모든 장면을 **정지 상태 한 장**으로 읽히게 만든다. 클릭·호버·순차 강조가 있어야 읽히는 장면을 만들지 않는다.

### 4-4. 자산

- 실제 캡처가 없는 자리는 점선 박스 플레이스홀더와 "실제 화면 교체 예정" 라벨로 둔다. 가짜 스크린샷을 그리지 않는다.
- 개념도는 CSS 도형으로 그리고 "개념 예시"를 표시한다.
- 자산 파일은 `topics/<slug>/assets/`에 둔다.

### 4-5. 문구와 사실 경계

- 근거 없는 성능 수치·절감 시간·이용자 수를 넣지 않는다.
- 사내 모델명·API 주소·API 키·계정·설치 명령을 슬라이드에 넣지 않는다. 역할 이름만 쓴다.
- 개인 사례는 "개인 기록", 공개 Beta 설계는 "개념 예시"로 표시한다.
- 진행 중 topic에 사실 경계 체크리스트가 있으면(예: 계획서 2-6절) 장면마다 대조한다.

## 5. 외부 의존성 규칙

| 대상 | 규칙 |
|---|---|
| HyperFrames CLI | `npx hyperframes ...` 또는 `package.json` 스크립트로만 실행. 전역 설치 가정 금지 |
| HyperFrames 문법 | `.codex/skills/hyperframes/SKILL.md`, `house-style.md`를 따른다. 새 속성·문법을 창작하지 않는다 |
| GSAP | 타임라인은 `paused: true`, 동기 생성, `repeat: -1` 금지. `data-layer`·`data-end` 대신 `data-track-index`·`data-duration` |
| Paperlogy 폰트 | jsdelivr CDN `@font-face`를 사용. 오프라인 렌더를 대비해 폴백 스택 유지 |
| Python 스크립트 | `logging` 모듈 사용(`print` 금지), 타입 힌트, 기존 4칸 들여쓰기 유지 |
| 라이브러리 문서 | 라이브러리·CLI 사용법은 Context7 MCP로 최신 문서를 확인 |

## 6. 워크플로

### 6-1. 기본 파이프라인

```text
new_md/DESIGN-<회사>.md + 사용자 요청
  -> topic_intake_router        -> _workspace/topic_intake.md
  -> ppt_content_planner        -> _workspace/ppt_content_plan.md
  -> ppt_visual_designer        -> _workspace/ppt_visual_plan.md
  -> (선택) 슬라이드 단위 루프  -> 6-2
  -> hyperframes_ppt_builder    -> topics/<slug>/index.html, overview.html
  -> ppt_overview_qa            -> _workspace/ppt_qa_report.md
  -> 사용자 overview Edit/Aim 수정 -> patch 반영 반복
  -> 사용자 최종 확인
  -> PDF/PPTX export            -> topics/<slug>/exports/
```

### 6-2. 슬라이드 단위 루프 (강의·교육 자료)

차수(block) 단위로 반복한다.

```text
slide_content_writer ─┐                        -> _workspace/slide_copy/<차수>.md
                      ├─> lecture_expert (pre)  -> _workspace/lecture_review/<차수>-pre.md
slide_ui_designer ────┘                        -> _workspace/slide_ui/<차수>.md
  -> 수정 요청을 담당 에이전트에 재전달·반영
  -> hyperframes_ppt_builder
  -> validate + lint
  -> lecture_expert (post) + ppt_overview_qa    -> _workspace/lecture_review/<차수>-post.md
```

- `lecture_expert`의 "보류" 항목은 추정하지 말고 사용자에게 모아서 묻는다.
- `slide_ui_designer`는 문구가 넘치면 글자 크기를 줄이지 말고 `slide_content_writer`에게 축소를 요청한다.

### 6-3. Export gate

- 사용자가 "overview 최종 확인"을 말하기 **전에는** PDF/PPTX export를 실행하지 않는다.
- PPTX는 `.codex/skills/hyperframes-overview-pptx-export/scripts/export_overview_to_pptx.mjs`를 사용하고 `--expected-slides`를 실제 장수로 지정한다.
- export 후 전 페이지를 렌더해 장수·순서·한글·편집 UI 제외를 확인한다.

### 6-4. 검증 명령

HTML을 수정할 때마다 다음을 실행한다. lint를 못 돌리면 이유를 보고한다.

```powershell
python scripts\validate_topic.py topics\<slug>
npx hyperframes lint topics\<slug>
```

에이전트·스킬 정의를 수정하면 다음을 실행한다.

```powershell
python scripts\validate_codex_port.py
```

미리보기·스냅샷:

```powershell
npm run preview:port -- topics/<slug>
npm run snapshot -- topics/<slug> -- --at 2.5,8.1
```

## 7. 파일 동기화 규칙

**한쪽만 수정하지 않는다.** 왼쪽을 바꾸면 오른쪽을 같은 작업 안에서 함께 바꾼다.

| 변경 | 함께 수정할 파일 |
|---|---|
| 슬라이드 문구·스타일·장면 추가/삭제 | `topics/<slug>/index.html` **와** `topics/<slug>/overview.html`. scene-styles topic은 index 수정 후 `sync_overview.py --renumber`로 overview 재생성 |
| 사용자 overview patch 반영 | `index.html`, `overview.html` 양쪽(scene-styles topic은 index 반영 후 재생성) → validate + lint → overview 검토 상태로 복귀 |
| 장면 목록·순서 변경 | 위 두 HTML + `_workspace/ppt_content_plan.md` + `_workspace/ppt_visual_plan.md`(ID 매핑표) + topic의 `storyboard.json`이 있으면 동기화 |
| 에이전트 추가·역할 변경 | `.codex/agents/<name>.toml` + (슬라이드 단위면) `.claude/agents/<name>.md` + `AGENTS.md` 에이전트 역할 + `README.md` 파이프라인 + `architecture.md` + `_workspace/orchestration-plan.md` → `validate_codex_port.py` |
| 허용 `data-skill` 변경 | `AGENTS.md` + `scripts/validate_topic.py`(`DECK_SKILLS`/`CARD_NEWS_SKILLS`) + `.agents/skills/ppt-hyperframes-deck/SKILL.md` + `CLAUDE.md` + 이 문서 3-3 |
| topic 필수 파일 변경 | `scripts/validate_topic.py`(`REQUIRED_TOPIC_FILES`/`DIRS`) + `scripts/create_topic.py` + `references/ppt-checklist.md` + `SKILL.md` QA Gates + 이 문서 3-1 |
| workflow·기능 변경 | `README.md`, `architecture.md`, `TASK.md`, `_workspace/orchestration-plan.md` 중 해당 문서 |
| topic의 디자인 교체 | `topics/<slug>/DESIGN.md` + 두 HTML의 `:root` 변수 |

- 저장소 문서(`README.md`, `architecture.md`, `TASK.md`, `orchestration-plan.md`, topic `BRIEF.md`)는 `문제 분석 / 설계 / 구현 / 코드 / 테스트 방법 / 향후 개선사항` 섹션 구조를 유지한다.
- `.codex/agents/*.toml`의 `developer_instructions`에는 `Role:`, `Input:`, `Process:`, `Output:`, `Quality checks:`, `Handoff path:` 마커를 모두 넣는다 (검증기가 요구).
- `.agents/skills/*/SKILL.md`에는 frontmatter `name`, `description`을 넣는다.

## 8. AI 판단 기준

### 8-1. 출력 타입

```text
사용자가 PPT·발표자료·슬라이드덱·강의자료를 말함 -> deck
사용자가 카드뉴스·SNS·인스타그램형을 말함      -> card-news
기존 topic 작업                                  -> index.html의 data-output-type="card-news" 유무로 판별
```

### 8-2. 규칙 충돌

```text
AGENTS.md  >  shrimp-rules.md  >  CLAUDE.md  >  .agents/skills/*  >  .codex/skills/*
진행 중 topic의 계획서(topics/<slug>/docs/*.md)는 해당 topic 범위에서 위 규칙을 구체화한다. 위 규칙을 어기는 결정은 계획서에 있어도 따르지 않고 사용자에게 알린다.
```

### 8-3. 진행 중 topic 작업 전

1. `topics/<slug>/docs/` 아래 계획서(예: `slide-plan-YYYY-MM-DD.md`)의 "확정된 결정" 표를 먼저 읽는다.
2. `_workspace/` 단계 산출물의 최신 상태를 확인한다.
3. 결정 표에 없는 사항만 판단한다.

현재 진행 중 topic 요약 (상세는 계획서가 원본):

| topic | 계획서 | 핵심 결정 |
|---|---|---|
| `sk-hynix-ai-agent-guide-edu` | `docs/slide-plan-2026-09-13.md` | deck, DESIGN-Notion **최소 적용**(오프화이트·근검정·파랑 액센트 1개·헤어라인·그림자 없음·스티커 팔레트 미사용·남색 반전은 S01·G02만), **애니메이션 없음**(빈 paused 타임라인만), 구간 표지 생략, 본문 46장 + 부록 6장 = 52장, 슬라이드 단위 루프 사용 |

### 8-4. 모호한 상황

| 상황 | 행동 |
|---|---|
| 디자인 파일이 여러 개이고 지정 없음 | `--company`와 매칭되는 파일을 쓰고, 없으면 사용자에게 확인 |
| 문구가 레이아웃을 넘침 | 글자 크기 축소보다 문구 축소·장면 분할을 먼저 |
| 실제 자산 없음 | 플레이스홀더로 진행하고 대기 목록에 기록 |
| 사내 환경값·실습 판본 불명 | 추정하지 말고 "미확인"으로 표시해 사용자 확인 목록에 추가 |
| 사용자가 "바로 작업"을 요청 | 요구사항 분석 → 아키텍처 → 구현 계획 → 코드 → QA 순서를 내부 산출물에 반영한 채 진행 |
| 플랜 모드에서 실행으로 전환 직전 | 계획을 `.claude/plans/plan-YYYY-MM-DD-기능명.md`로 남길지 사용자에게 매번 확인 |

## 9. 금지 행동

- ⚠️ 허용 목록 밖의 `data-skill` 값을 쓰지 않는다. deck과 card-news 값을 섞지 않는다.
- ⚠️ 사용자 최종 확인 전에 PDF/PPTX export를 실행하지 않는다.
- ⚠️ 사용자가 영상을 명시적으로 요청하지 않았는데 `npm run render` / `npx hyperframes render`를 실행하지 않는다.
- ⚠️ `index.html`과 `overview.html` 중 한쪽만 수정하지 않는다.
- ⚠️ 문서 갱신 없이 코드·워크플로만 바꾸지 않는다.
- HyperFrames 문법·속성을 새로 만들지 않는다. `.codex/skills/skills/` 중첩 복사본을 기준으로 삼지 않는다.
- `new_md/DESIGN-*.md`, `topics/_template/`, `topics/_card_news_template/`, `topics/oxxodok_50th/`, `.codex/skills/`를 수정하지 않는다.
- 기획 장면 ID를 재번호하지 않는다.
- 근거 없는 수치·가짜 스크린샷·가상의 성공 사례를 실제처럼 넣지 않는다.
- API 키·비밀번호·토큰·사내 주소를 HTML·문서·커밋에 넣지 않는다.
- `shrimp_data/`를 직접 편집하지 않는다.
- 사용자 요청 없이 git commit·push를 하지 않는다. 커밋 메시지는 한국어로 쓴다.
- 타임라인을 `async`·`setTimeout`·Promise 안에서 만들지 않는다. `repeat: -1`을 쓰지 않는다.

### Do / Don't 예시

| Do | Don't |
|---|---|
| S10 문구를 바꾸면 `index.html`의 `data-scene-id="S10"` 장면을 고치고 `sync_overview.py`로 overview 재생성 | `index.html`만 고치고 "overview는 나중에", 또는 overview만 손으로 수정 |
| 새 장면을 G03으로 추가 | S10 뒤에 끼우면서 S11 이후를 S12, S13…으로 재번호 |
| `data-skill="compare"` 사용 | `data-skill="comparison"`, `data-skill="table"` 창작 |
| 캡처 없는 Streamlit 화면을 점선 박스 + "실제 화면 교체 예정"으로 둠 | 그럴듯한 가짜 Streamlit UI를 그려 실제 화면처럼 제시 |
| "사내 추론 서버", "승인된 모델 경로"처럼 역할 이름 사용 | 실제 사내 URL·모델명·키를 슬라이드에 기재 |
| `--color-accent: #0075de`를 `:root`에 두고 변수 참조 | 장면마다 `color: #0075de` 직접 기입 |
| 에이전트 추가 후 `validate_codex_port.py` 실행 | toml만 추가하고 `AGENTS.md`·`orchestration-plan.md` 미갱신 |
| "overview 최종 확인" 발화 후 export | 빌드 직후 "편의상" PDF부터 출력 |
