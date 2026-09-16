# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

HyperFrames(HTML + GSAP 기반 composition) 방식으로 **16:9 발표 슬라이드덱** 또는 **카드뉴스**를 topic 단위로 제작하는 작업 공간이다. 일반 애플리케이션이 아니며 빌드 산출물·테스트 프레임워크·npm 의존성이 없다 (`npx hyperframes`가 CLI를 그때그때 받아 실행).

- **기본 최종 산출물은 PDF/PPTX**다. MP4는 사용자가 명시적으로 영상을 요청할 때만 만든다.
- 저장소 전체 작업 규칙의 원본은 `AGENTS.md`다 (Codex용으로 작성됐지만 이 저장소의 규칙이다). 규칙이 충돌하면 `AGENTS.md`를 따른다.
- 새 제작 요청 프롬프트 예시와 사용자 관점 흐름은 `user_guide.md`에 있다.

## 명령어

Windows/PowerShell 환경 기준. Python 3.11+ 필요 (`validate_codex_port.py`가 `tomllib` 사용), Node 20+.

```powershell
# 새 topic 생성 (new_md/DESIGN-*.md 중 --company 이름이 포함된 파일을 찾아 복사, 없으면 첫 파일 사용)
npm run new-topic -- --name <slug> --title "<제목>" --company "<회사>" --type deck        # 또는 --type card-news
npm run new-topic -- --name <slug> --title "<제목>" --company "<회사>" --design new_md/DESIGN-x.md  # 디자인 파일 직접 지정

# 검증 (이 저장소의 "테스트"에 해당)
python scripts\validate_codex_port.py              # harness 구조 검증 (.codex/agents/*.toml, .agents/skills/*/SKILL.md)
python scripts\validate_topic.py topics\<slug>     # 단일 topic 검증
npx hyperframes lint topics\<slug>                 # HyperFrames lint (npm run lint -- topics/<slug> 도 동일)

# 미리보기 / 스냅샷
npm run preview:port -- topics/<slug>              # port 3000 preview 서버
npm run snapshot -- topics/<slug> -- --at 2.5,8.1,13.7

# MP4 — 사용자가 영상을 명시적으로 요청한 경우에만
npm run render -- topics/<slug>
```

HTML을 수정한 뒤에는 `validate_topic.py`와 `hyperframes lint`를 실행하고, lint를 못 돌렸다면 그 이유를 보고한다.

## 아키텍처

### 제작 파이프라인 (Generate-Review)

```text
new_md/DESIGN-<회사>.md + 사용자 요청
  -> intake -> content plan -> visual plan -> HyperFrames build -> overview QA
  -> 사용자가 overview.html에서 Edit/Aim 수정 -> patch 반영 반복
  -> 사용자 최종 확인 후에만 PDF/PPTX export -> topics/<slug>/exports/
```

- 각 단계의 역할 정의는 `.codex/agents/*.toml`(topic_intake_router, ppt_content_planner, ppt_visual_designer, hyperframes_ppt_builder, ppt_overview_qa), 반복 절차는 `.agents/skills/ppt-hyperframes-deck/SKILL.md`, 단계별 산출 문서 경로는 `_workspace/orchestration-plan.md`에 있다. 큰 작업의 중간 산출물은 `_workspace/topic_intake.md`, `ppt_content_plan.md`, `ppt_visual_plan.md`, `ppt_qa_report.md`에 기록한다.
- **Export gate**: 사용자가 overview 최종 확인을 말하기 전에는 PDF/PPTX export를 실행하지 않는다.

### topic 구조

`topics/<slug>/`는 독립 HyperFrames 프로젝트다. `_template`(deck)과 `_card_news_template`(card-news)는 참고용 scaffold이며, `oxxodok_50th`가 실제 완성 사례다.

- `index.html` — 원본 슬라이드 소스. `#root`에 `data-output-type`, `data-composition-id="main"`, `data-width/height`, 전체 `data-duration`을 둔다. 각 슬라이드는 `<section class="scene clip" data-skill=... data-start=... data-duration=... data-track-index="0">`이고, 애니메이션은 paused GSAP timeline을 `window.__timelines.main`에 등록한다.
- `overview.html` — 사용자 검토·수정 화면. 필수: `class="edit-btn"` 버튼, Aim UI 또는 `data-aim`, `data-editable="true"` 영역, Done 시 agent가 읽을 수 있는 patch를 클립보드로 복사 (서버 저장 API 없이도 동작해야 함).
- `DESIGN.md` — 생성 시 `new_md/`에서 복사해 고정한 디자인 기준. 색·폰트·레이아웃·금지 스타일의 근거로 사용한다.
- `topic.json`, `BRIEF.md`, `meta.json`, `hyperframes.json`(루트 파일 복사본), `assets/`, `exports/`(필수), `renders/`·`snapshots/`(gitignore).

### index.html ↔ overview.html 동기화

완성형 overview(`oxxodok_50th`, `.codex/skills/hyperframes-overview/template.html` 기반)는 iframe이 아니라 **index.html의 `:root` 변수·씬 CSS·슬라이드 마크업을 복제**해 담는다. 따라서 슬라이드 내용이나 스타일을 바꾸면 두 파일을 모두 수정해야 하고, 사용자가 붙여넣은 overview patch도 양쪽에 반영한 뒤 다시 overview 검토 상태로 돌려준다.

`index.html`에 `<style id="scene-styles">`가 있는 topic(예: `sk-hynix-ai-agent-guide-edu`)은 index만 고치고 `python scripts\sync_overview.py topics\<slug> --renumber`로 overview를 재생성한다. 장면 id는 순번 `s-N`(patch의 `## Slide N`과 대응), 기획 장면 ID는 `data-scene-id`, 발표자 노트는 `.speaker-note`다. (`create_topic.py`가 만드는 overview는 3장짜리 단순 카드형이라 완성형과 구조가 다르다.)

### 허용 `data-skill` 값 (`validate_topic.py`가 검사)

- `deck` (1920x1080): `title`, `title-bullets`, `title-image`, `title-tags`, `split`, `stat`, `steps`, `compare`, `evolution-flow`, `quote`, `kindergarten-notice`
- `card-news` (기본 1080x1080, 세로형 요청 시 1080x1920): `photo-cover`, `video-cover`, `stat`, `image-feature`

deck/card-news 값을 섞지 않는다. 출력 타입 판별은 `index.html`의 `data-output-type="card-news"` 유무로 한다.

### HyperFrames 스킬 레퍼런스

`.codex/skills/`에 HyperFrames 문법·레이아웃·전환 효과 스킬이 있다 (Claude Code 스킬로 자동 로드되지 않으므로 필요한 `SKILL.md`를 직접 읽는다). HyperFrames 문법을 새로 만들지 말고 이 스킬들을 따른다.

- `hyperframes/` (핵심 문법, `house-style.md`, `palettes/`), `hyperframes-slide*/` (deck 레이아웃별), `hyperframes-card-news*/`, `hyperframes-overview*/` (overview 템플릿·live 편집), `hyperframes-overview-pptx-export/` (overview → PPTX 변환 스크립트), `hyperframes-fx-*/`, `gsap/`
- `.codex/skills/skills/`는 같은 스킬의 중첩 복사본이다. `.codex/skills/` 최상위를 기준으로 본다.

## 덱 제작 도구 (`scripts/deck/`)

묶음(차수) 단위 제작과 덱 전체 수정에 쓰는 도구다. 모두 `python scripts/deck/<파일> --help` 로 사용법을 볼 수 있다.

| 스크립트 | 언제 쓰나 |
|---|---|
| `check_fragment.py` | 빌더가 만든 BLOCK 조각을 `index.html`에 끼우기 전 검사(장면 ID·data-skill·금지 마크업·CSS 없는 클래스) |
| `splice_blocks.py` | `<!-- BLOCK:X START -->` 구간 교체(`--extract` 로 추출) |
| `apply_table.py` | 문구·배치 치환 표(JSONL) 적용. **항상 `--dry` 로 먼저 확인** |
| `qa_rules.py` | topic 의 `deck-rules.json` 으로 하우스 룰 검사 |
| `dump_deck_text.py` | 검토 서브에이전트용 화면 글자·노트 추출 |
| `scene_map.py` | 장면 ID ↔ 순번 매핑표 생성(기획 문서 갱신용) |
| `localize_assets.py` | CDN 글꼴·스크립트를 topic 안 로컬 파일로 바꿈(인터넷 없는 환경 필수) |

서브에이전트 지시문 템플릿은 `templates/briefs/` 에 있다.

## QA 게이트 (HTML 을 고친 뒤 이 순서로)

```powershell
python scripts\sync_overview.py topics\<topic>            # 장면을 더하거나 뺐으면 --renumber
python scripts\validate_topic.py topics\<topic>
npx hyperframes check topics\<topic>                      # lint·런타임·레이아웃 겹침·명암비를 한 번에
python scripts\deck\qa_rules.py topics\<topic> --rules topics\<topic>\deck-rules.json
python scripts\sync_overview.py topics\<topic> --check
```

`hyperframes check` 가 레이아웃 겹침·넘침과 WCAG 명암비를 보므로 별도 브라우저 스크립트는 필요 없다. `qa_rules.py` 는 `check` 가 모르는 우리 교육 규칙(시간 표기·존댓말·출처 등)만 본다.

## 사내 교육 덱 하우스 룰 (`sk-hynix-ai-agent-guide-edu`)

`deck-rules.json` 이 자동으로 검사하는 규칙이다. 새 사내 교육 덱도 이 규칙을 복사해 쓴다.

- **실습 자료는 사내 전용**이다. 현업 가이드(`skh_llm_guide`)의 파일명·함수명·장 이름을 실습 코드처럼 쓰지 않는다. 코드 위치는 역할 이름 + "실습 가이드 해당 장"으로만 적는다.
- **시간 정보는 첫 시간표(G01) 한 장에만** 둔다. 실습 시간은 실제와 달라 수강생에게 압박이 된다. 나머지는 순서 표현(먼저·이어서·다음 구간)으로 쓴다.
- **화면 문장은 존댓말**(…합니다/…입니다)로 쓴다. 명사형 라벨·칩·표 칸은 그대로 둔다.
- **출처 줄은 공식 문서와 논문만** 남긴다. "근거:", 교안, 개인 기록, 사내 가이드는 적지 않는다(수강생이 볼 수 없는 자료).
- **사내 주소·모델명·키를 화면에 쓰지 않는다.** 역할 이름으로 표시한다.
- **구간 코드(B1–B7)·쪽번호·기승전결 표현을 화면에 두지 않는다.**
- **장면마다 이미지 또는 인포그래픽이 하나 이상** 있어야 한다. 자리표시(`[IMG-PLACEHOLDER · P-…]`)는 캡처가 들어올 자리이므로 지우지 않는다.
- 강조색은 주황 `--accent: #dd5b00`, 반전 배경은 `--night: #793400` 이다(`DESIGN.md` 참고).
- **PDF/PPTX export 는 사용자가 overview 최종 확인을 말한 뒤에만** 실행한다.

## 문서화 규칙

기능이나 workflow를 바꾸면 `README.md`, `architecture.md`, `TASK.md`, `_workspace/orchestration-plan.md` 중 해당 문서를 함께 갱신한다 (`AGENTS.md`: 문서 없이 코드만 수정하지 않는다). 이 문서들은 `문제 분석 / 설계 / 구현 / 코드 / 테스트 방법 / 향후 개선사항` 섹션 구조를 공통으로 쓴다.
