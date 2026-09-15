# AI Agent Guide — HyperFrames 시각·구현 계획 (v0.2)

버전: v0.2 · 2026-09-13 · topic: `topics/sk-hynix-ai-agent-guide-edu/`

## v0.4 자산 표 (2026-09-16, 아래 v0.2보다 우선)

원본은 `topics/sk-hynix-ai-agent-guide-edu/docs/slide-plan-v0.4-visual-narrative.md` 6절 자산 준비 표다. 계획서가 "CSS/SVG"로 적은 도식은 별도 SVG 파일을 만들지 않고 `index.html` 안의 `.dg` 계열 클래스(dg-row·dg-box·dg-arrow·dg-zone·dg-sub·dg-caption)로 그렸다.

| 계획서 논리 이름 | 장면 | 실제 구현 |
|---|---|---|
| `common/yt-thumb-kf1dypnh.jpg` | G00 | 이미지 파일 `assets/img/common/yt-thumb-kf1dypnh.jpg` (P-G00 쓰지 않음) |
| `b1/transformer-fig1.png` | S05 | 이미지 파일 `assets/img/b1/transformer-fig1.png` + 출처 캡션 |
| `b1/attention-fig2.png` | A01 | 두 패널로 나눈 `assets/img/b1/attention-fig2a.png`·`attention-fig2b.png` + 출처 캡션 |
| `b1/ai-ml-dl-llm.svg` 외 B1 도식 | S03·S04·S06·S07 | 인라인 `.dg` (S03 동심 `.dg-zone`, S04 `.steps.row`, S06 두 영역 `.dg-zone`, S07 `.dist` 막대) |
| `b1/practice1-output.png` | S08 | 플레이스홀더 P-S08 |
| `b2/*.svg` | S09·S10·S14 | 인라인 `.dg` (S10 두 시점 `.dg-zone.is-grow` + 조각·겹침 칩) |
| `b2/article-body-check.png` | S11·S13 | 플레이스홀더 P-S11·P-S13 |
| `b3/*.svg` | S15–S18·S21 | 인라인 `.dg`·`.steps.row.is-compact`·`.data-table` |
| `b3/streamlit-app.png` | S20·S29 | 플레이스홀더 P-S20·P-S29 |
| `b4/*.svg` | S22–S25 | 인라인 `.dg` (S25·S40 요청문 6칸은 같은 틀) |
| `b4/claude-code-screen.png` | S26 | 플레이스홀더 P-S26 |
| `b5/*.svg` | S28·S30 | 인라인 `.dg`·코드 카드 |
| `b5/git-diff-example.png`·`dokmo-before-after.png` | S31 | 플레이스홀더 P-S31·P-S31b |
| `b6/vault-raw-wiki.svg`·`vault-screenshot.png` | S34 | 인라인 `.dg` + 플레이스홀더 P-S34 (S37은 파일 카드 도식, 자리표시 없음) |
| `b6/skill-*.svg` | S36·A04 | S36 인라인 `.dg-row.is-roles` 역할 카드 + 3단계 흐름, A04 `.compare-grid.cols-3` + N×M→N+M 칩 줄 |
| `b7/free-practice-3tracks.svg` | S39 | `.compare-grid.cols-3` |
| `appendix/*.svg` | A03·A07–A09 | 인라인 `.dg` + 코드 카드 (A03 공통 기반 띠 `.dg-row.is-band`) |
| `appendix/hitl-interrupt.svg` | A10 | 인라인 `.dg` + 승인 카드만 자른 `assets/img/appendix/cowork-hitl-approval-card.png` (모델명 영역 없음) |

쓰지 않은 자리표시: P-G00, P-S05, P-A01, P-S37, P-A10 (자산을 확보했거나 도식으로 대신함). 남은 자리표시 10곳 목록은 `_workspace/ppt_qa_report.md` "v0.4" 절.

v0.4에서 디자인 시스템에 더한 클래스(원본 `index.html` `#scene-styles` 끝 v0.4 블록, 규칙은 `_workspace/slide_ui/00_component_catalog.md` 5·7절):

- 텍스트 층: `.act-tag`(막 태그), `.thesis`(한 줄 요지 40px, 파랑 밑줄), `.explain`(설명 문단 32px)
- G01 괄호선: `.act-group`·`.act-bracket`·`.act-name`
- 자리표시 v2: `.placeholder.is-spec`·`.placeholder-id`
- 그림 틀 높이: `.split-image.h-sm/h-md/h-lg`, 두 장 나란히 `.split-image.pair`
- 분포 막대: `.dist`·`.dist-bar.lv-1…lv-5` (S07, 수치 없는 모양)
- 진행 시간 띠: `.time-band` (S41–S43)
- 그 밖: `.dg-check`(빈 체크 칸), `.dg-zone.is-grow`, `.steps.row.is-compact`, `.quote-points`, `.done-row.is-full`, `.dg-row.is-band`, `.dg-arrow.has-label`, `.nowrap`

## v0.2 디자인 시스템 (아래 v0.1 본문보다 우선)

- 기준: topic `DESIGN.md`의 "교육 자료 최소 적용 규칙". Notion 원문은 참고용.
- 캔버스: 1920×1080. 배경 `--canvas` 오프화이트, 카드 `--surface` 흰색 + 1px `--hairline`. 그림자 없음, 모서리 12px.
- 액센트: 파랑 `--accent` 하나. 단계 번호 원, 강조 밑줄, 현재 구간 표시, 비교의 "권장" 열 테두리에만 사용.
- 반전: 남색 `--night` 배경은 S01 표지와 G02 마무리 두 장만.
- 글자: Paperlogy 우선. 장면 제목 72–80px/700, 핵심 항목 40–48px, 보조 32–36px, 출처·풋터 24–28px `--ink-3`.
- 장면 공통 구조: 상단 eyebrow(구간 표시) → 장면 제목 → 본문 영역 → 하단 출처 줄 → 풋터(좌: 교육명, 우: 쪽번호).
- 애니메이션 없음: 트윈을 쓰지 않는다. `window.__timelines.main`에 paused 타임라인만 등록한다.
- 이미지 없음 기본: 실제 캡처가 없는 자리는 점선 플레이스홀더 + "실제 화면 교체 예정" 라벨. 개념도는 CSS 도형 + "개념 예시" 배지.

## v0.2 구현 규약

| 항목 | 규약 |
|---|---|
| 장면 태그 | `<section id="s-N" class="scene clip" data-skill="…" data-scene-id="S10" data-start="(N-1)*5" data-duration="5" data-track-index="0">` |
| 순번 | `s-N`은 overview `data-slide="N"`과 같은 번호. `scripts/sync_overview.py --renumber`가 관리 |
| 편집 | 화면 텍스트 leaf마다 `data-editable="true"` |
| 발표자 노트 | 장면 안 `<aside class="speaker-note">…</aside>`. 화면에는 숨김, PPTX export 시 노트로 복사 |
| 풋터 | `.deck-footer`(좌)와 `.page-num`(우). overview 템플릿 공용 `.brand`/`.slide-num`과 이름이 겹치지 않게 분리 |
| CSS 위치 | `@font-face`, `:root` 토큰, 장면 CSS는 모두 `<style id="scene-styles">` 안에. html/body/#root 캔버스 규칙은 별도 style |
| 클래스 | `_workspace/slide_ui/00_component_catalog.md`의 클래스만 사용. 인라인 hex 금지 |
| overview | `python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --renumber`로 재생성. 직접 편집하지 않음 |

장면별 레이아웃은 `ppt_content_plan.md` 상단 매핑표가 기준이다. 장면별 세부 배치는 `_workspace/slide_ui/<차수>.md`에 있다.

## v0.1 본문 중 무효가 된 항목

- 3절 "반복 생성은 HTML에서 순차 강조"와 6절 애니메이션 시간 설명 → 애니메이션 없음으로 대체.
- 7절 제안 topic 이름 `ai_agent_guide` → 실제 topic은 `sk-hynix-ai-agent-guide-edu`.
- 2절 레이아웃 적용 예 중 S02(`split`) → `title-tags`.

---

# AI Agent Guide — HyperFrames 콘티 제작 인계

버전: v0.1 · 2026-09-13

[장면별 콘티](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/outputs/ai_agent_guide_storyboard/_workspace/ppt_content_plan.md) · [기획 데이터](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/outputs/ai_agent_guide_storyboard/storyboard.json)

## 1. 제작 기준

- 16:9, 1920×1080.
- 본문 S01–S40, 자유 실습 진행 S41–S44.
- 선택 부록 A01–A06은 본문 시간표에 포함하지 않음. 실제 덱에 포함하면 별도 번호 구간으로 구성.
- 현재 산출물은 콘티. 화면 문구와 구도는 초안이며 실제 HTML 렌더·PDF 가독성 검수는 아직 수행하지 않음.
- 기존 로컬 제작 규약에 맞춰 index.html과 overview.html의 장면 내용을 동기화.
- overview의 Edit/Aim은 제작 검토용. 발표용 PDF에는 편집 버튼·썸네일 목록·진행 도구 UI를 포함하지 않음.
- 강사용 멘트와 출처는 별도 노트 데이터에 유지. 일반 슬라이드 PDF에서 발표자 노트가 자동으로 제공된다고 가정하지 않음.

## 2. 허용 레이아웃과 이 초안의 사용처

기준: [HyperFrames Slide Skill](C:/LSW_Coding/3_slide_master_v2/.codex/skills/hyperframes-slide/SKILL.md).

| data-skill | 구도 | 적용 예 |
|---|---|---|
| title | 큰 제목과 짧은 부제 | S01 |
| steps | 한 가지 과정의 순서. 단계 이름 가까이에 설명 배치 | S04, S10, S16, S28 |
| split | 실제 자료/개념도와 설명을 분리 | S02, S05, S06, S18, S24, S34 |
| compare | 비교 기준을 고정한 두세 대상 | S07, S09, S12, S17, S22, S25 |
| title-image | 실제 화면을 중심으로 필요한 부분만 설명 | S20 |
| title-bullets | 실습 안내·완료 조건·진행 시각 | S08, S13, S19, S26, S32, S37, S41–S44 |

선택한 타입의 실제 HTML 구현 시에는 대응하는 `hyperframes-slide-work-*` 하위 스킬을 읽는다. 새로운 data-skill 값을 임의로 추가하지 않는다.

## 3. 주요 장면의 구도 초안

### S04 · LLM의 응답 생성

- 상단: 제목.
- 중앙: 문장 입력, 문맥 계산, 다음 토큰 선택의 과정.
- 하단: “학습과 일반 추론 요청은 구분”이라는 짧은 보조 문장.
- 토큰 분할 결과를 실제 출력처럼 제시하려면 수업 모델의 토크나이저 결과를 사용한다. 그렇지 않으면 개념 예시로 표시한다.
- 반복 생성은 HTML에서 순차 강조할 수 있지만 PDF에는 전체 흐름이 보여야 한다.

### S05 · Attention과 문맥

- 좌측: 문맥이 다른 짧은 문장 두 개.
- 우측: 주변 단어와 해당 표현의 관계를 설명하는 개념도 자리.
- 실제 attention 가중치 수치나 열지도를 측정 없이 만들지 않는다.
- 수식·Q/K/V는 부록. 본문은 어떤 역할인지 이해하는 데 집중한다.

### S06 · 모델·서버·API

- 학습자 Python 프로그램, 통신 경로, 추론 서버/모델의 위치를 구분.
- SDK는 Python 쪽에, vLLM은 서버 쪽에 배치.
- 요청에 쓰는 API 형식과 모델 자체를 같은 상자로 묶지 않는다.
- 사내 주소·API 키 대신 역할 이름을 표시한다.

### S10 · RAG

- 문서 준비와 질문 처리의 시점을 구분.
- “자료 수집·분할” 영역과 “검색·답변” 영역을 연결.
- 임베딩과 저장소는 선택한 구현의 역할로 설명.
- 모든 외부 문서 요약을 자동으로 Agentic RAG라고 표시하지 않는다.

### S16 · Tool 실행

- 모델이 만드는 호출 요청과 프로그램이 실행하는 함수를 다른 영역에 배치.
- 도구 이름, 인자, 결과를 각각 보여준다.
- 단계별 강조를 없애도 PDF 한 장에서 전체 순서를 읽을 수 있게 한다.
- 도구 호출 로그를 모델의 숨겨진 사고 전체라고 표시하지 않는다.

### S18 · Part Finder

- 가상 카탈로그의 후보 몇 개와 사용자 조건을 함께 제시.
- 파트 종류와 제조사 조건이 맞는지 같은 기준으로 비교.
- 조건이 없을 때의 결과 없음 처리를 명시.
- “공개 Beta 설계 기반 개념 예시”를 표시. 운영 정확도 수치를 추가하지 않는다.

### S24 · 프로그램 구조

- 화면·업무 규칙·모델 연결·데이터 접근을 구분.
- ‘결과 없음 안내’ 기능을 바꿀 때 영향을 받는 부분만 강조.
- 작은 Streamlit 예제에 존재하지 않는 서비스를 추가하지 않는다.
- 구조 경계에 관한 설명을 하되 처음부터 복잡한 서비스 분리 설계를 요구하지 않는다.

### S31 · Dokmo 점검 경험

- 실제 사례 하나에 집중: 한글 이름 입력 또는 다음 행동 안내.
- 확보된 실제 화면만 사용. 화면이 없으면 당시 점검 문서의 짧은 내용으로 설명.
- 코드/테스트 성공과 실제 사용자 목적 충족을 같은 사례에서 비교.

### S34 · 개인 지식

- Raw, 개인 의견, Wiki의 관계를 설명.
- 실제 글 하나가 정리 문서로 바뀌는 예시를 사용.
- 자동 정리와 사람의 검토 시점을 구분.
- “나와 동일한 사고를 보장하는 분신”이라는 표현 대신 과거 근거를 찾아 판단을 돕는 활용 방향을 설명.

### 실습 안내 화면

- 상단: 실습 번호와 주제.
- 중앙: 이번 단계의 동작과 완료 조건.
- 하단: 해당 HTML 가이드의 장 이름. 파일명·앵커 확정 전에는 임의 링크를 만들지 않음.
- 설치 명령과 전체 코드를 PDF에 반복하지 않음.
- 타이머나 클릭이 없어도 언제 무엇을 완료해야 하는지 읽을 수 있게 한다.

## 4. 글자와 정보량의 초안 기준

브랜드 DESIGN 문서가 확정되면 해당 기준을 우선한다. 현재는 가독성을 위한 임시 제작 지침이다.

- 슬라이드당 주제 하나.
- 1920×1080 작업 기준 제목 72–88px, 본문 40–48px, 보조 출처 28–32px를 출발점으로 실제 화면에서 확인.
- 화면 문구는 콘티의 1–4개 핵심 항목 중심. 발표 멘트를 본문에 통째로 넣지 않는다.
- 코드 비교는 각 영역 5–7줄 정도로 제한하고 실습 파일의 핵심 부분만 보여준다.
- 여백과 행간을 먼저 확보하고, 넘치는 문장은 줄이거나 장면을 나눈다.
- 모든 화면을 카드형 UI로 만들지 않는다. 큰 텍스트·실제 화면·과정·비교를 목적에 맞게 사용한다.
- Paperlogy를 우선하는 로컬 기본 규칙을 참고하되, 실제 사내 렌더 환경에서 한글 폰트 제공 여부를 확인한다. 외부 CDN 접속만을 전제로 하지 않는다.

## 5. 필요한 자료와 자산

| 자산 | 사용하는 장면 | 준비 기준 |
|---|---|---|
| 강사 소개 정보와 사용 가능한 프로젝트 화면 | S02 | 사용자 제공 경력 확인, 실제 화면 |
| 고정 입력의 LLM 호출 결과 | S07–S09 | 모델·옵션·질문·실행일 기록. 가상 예시는 별도 표시 |
| 기사 본문과 검색 결과 | S09–S14 | 제목·URL·날짜·본문 확보. 교육용 저장 본문 준비 |
| 교육용 DB와 스키마 | S15–S19 | 정답을 아는 가상 데이터, 자료 없음 사례 |
| Part Finder 개념 예시 | S18 | 공개 Beta 원칙, 가상 카탈로그 |
| Streamlit 정상 화면과 개선 전후 | S20, S24, S29, S32 | 최종 실습판 기준 캡처 |
| Claude Code 실행·프로젝트 탐색 화면 | S22, S26 | 사내에서 검증한 환경. 인증정보 제거 |
| Dokmo 사용자 점검 사례 | S31 | 실제 점검 기록 또는 사용 가능한 화면 |
| Raw·개인 의견·Wiki 예제 | S34–S38 | 짧은 원문, 출처, 검토 전/후 상태 |
| 기본 Skill과 자유 실습 시작 코드 | S37–S43 | 사전 실행 확인, 작은 완료 조건 |

삽화·장식은 실제 근거 화면을 대신하지 않는다. 개념도는 개념도임을 표시하고, 설명에 필요한 구조만 사용한다. 실제 화면을 확보하지 못한 자리는 콘티의 자산 요청으로 남긴다.

## 6. 수업 시간과 HyperFrames 시간

`storyboard.json`의 `presentation_minutes`, `start`, `end`는 수업 운영 시간이다.

HyperFrames의 `data-start`, `data-duration`은 애니메이션 타임라인의 초 단위 값이다. 로컬 스킬의 기본 장면 길이 6초를 6분 강의로 해석하거나, 40분 수업을 2,400초 자동 재생 장면으로 만들지 않는다. 이번 덱은 PDF의 정적 페이지 넘김으로 발표할 예정이다.

예를 들어 S08은 수업 중 16분 동안 사용할 안내 화면이지만, HTML 장면 애니메이션은 짧게 완성하면 충분하다. PDF에는 모든 필수 텍스트와 단계가 보이는 최종 상태를 담는다.

## 7. 후속 topic 구성 제안

제안 topic 이름: `ai_agent_guide`. 실제 구현 저장소는 확정 후 적용한다.

```text
topics/ai_agent_guide/
  BRIEF.md
  DESIGN.md
  index.html
  overview.html
  meta.json
  hyperframes.json
  assets/
  exports/
```

- 기획 문서의 장면 ID S01–S44를 유지해 코멘트와 수정 요청을 연결한다.
- 로컬 HyperFrames가 사용하는 실제 HTML id와 data-slide는 구현 시 규약에 맞게 부여하고, 기획 ID를 별도 연결한다.
- `storyboard.json`은 제작 인계 자료다. 기존 `create_topic.py`가 자동으로 읽는 입력 형식이라고 가정하지 않는다.
- 코드 생성기는 최종 실습 파일·앵커·화면을 연결한 뒤 HTML 장면을 만든다.
- 선택 부록은 별도 구간으로 생성하며 본문 40장과 자유 실습 4장의 번호를 바꾸지 않는다.

## 8. 구현과 PDF 확인 순서

1. 사용자의 콘티 수정과 실제 실습 판본을 반영.
2. 디자인 기준과 실제 자산을 적용해 HTML 장면 구현.
3. index와 overview의 내용·순서·번호 일치 확인.
4. overview에서 Edit/Aim 수정과 재검토.
5. 장면별 텍스트 잘림·한글 폰트·화면 가독성 확인.
6. 로컬 topic 검증 스크립트와 HyperFrames lint 수행.
7. PDF 출력 시 16:9, 한 장면 한 페이지, 배경·폰트·편집 UI 제외 확인.
8. 출력한 PDF 전 페이지를 렌더해 마지막 페이지까지 내용과 순서 확인.

로컬 README에는 PDF/PPTX export 파이프라인 표준화가 개선 항목으로 남아 있었다. 따라서 검증하지 않은 자동 PDF 명령을 이 초안에 기재하지 않았다. 실제 출력 단계에서 사용 가능한 브라우저 인쇄 또는 PDF 출력 경로를 확인하고 결과를 검수한다.

## 9. 아직 수행하지 않은 검증

이 문서는 기획 인계 자료다. HTML lint, 이미지 렌더, PDF 출력, 사내 API·DB·Claude Code 실행 검증을 수행했다고 주장하지 않는다. 이번 점검은 시간 합계, 장면 누락, 출처 연결, 로컬 경로, 레이아웃 이름의 적합성에 한정한다.

