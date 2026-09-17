# Orchestration Plan

## 문제 분석

새 주제의 발표자료 또는 카드뉴스를 빠르게 만들되, 기존 `2_slide_master`의 HyperFrames 구성과 review-first 원칙을 깨지 않아야 한다.

## 설계

```text
1. Intake
2. Content Plan
3. Visual Plan
4. HyperFrames Build
5. Overview QA
6. User Review
7. PDF/PPTX Export
```

## 구현

### 1. Intake

담당: `topic_intake_router`

입력:

- 사용자 요청
- `new_md/DESIGN-회사이름.md`
- 출력 타입: `deck` 또는 `card-news`

출력:

- `_workspace/topic_intake.md`

### 2. Content Plan

담당: `ppt_content_planner`

출력:

- `_workspace/ppt_content_plan.md`

### 3. Visual Plan

담당: `ppt_visual_designer`

출력:

- `_workspace/ppt_visual_plan.md`

### 3-0. Instructional Design (선택, 실습이 있는 교육 덱)

실습자료와 덱을 맞춰야 할 때 `llm-edu-designer`가 설계 문서를 먼저 만든다. 덱 HTML은 고치지 않는다.

```text
실습자료 요약본 + ROADMAP2 확정 사실 + 현재 덱 추출본
  -> llm-edu-designer review (짜임새 검수)
  -> llm-edu-designer storyboard (스토리라인)
  -> llm-edu-designer conti (슬라이드별 내용과 콘티)
  -> llm-professional + lecture_expert 교차 검수
  -> (사용자 승인 후) 3-1 Slide-level Refinement
```

출력:

- `topics/<topic-name>/docs/edu-review-v<N>-<날짜>.md`
- `topics/<topic-name>/docs/edu-storyboard-v<N>-<날짜>.md`
- `topics/<topic-name>/docs/edu-conti-v<N>-<날짜>.md`

### 3-1. Slide-level Refinement (선택)

강의 자료처럼 장면별 정밀도가 필요할 때 차수(block) 단위로 반복한다.

```text
slide_content_writer ─┐
                      ├─> lecture_expert (pre) ─> 수정 반영 ─> hyperframes_ppt_builder
slide_ui_designer ────┘                                              │
                                                                     v
                                lecture_expert (post) + ppt_overview_qa ─> 사용자 검토
```

출력:

- `_workspace/slide_copy/<차수>.md`
- `_workspace/slide_ui/<차수>.md`
- `_workspace/lecture_review/<차수>-pre.md`, `<차수>-post.md`

### 4. HyperFrames Build

담당: `hyperframes_ppt_builder`

출력:

- `topics/<topic-name>/index.html`
- `topics/<topic-name>/overview.html`
- `topics/<topic-name>/DESIGN.md`
- `topics/<topic-name>/meta.json`
- `topics/<topic-name>/hyperframes.json`
- `topics/<topic-name>/exports/`

`index.html`에 `<style id="scene-styles">`를 둔 topic은 장면을 index에만 작성하고 다음 명령으로 overview를 재생성한다. 장면 id는 순번 `s-N`, 기획 ID는 `data-scene-id`.

```powershell
python scripts\sync_overview.py topics\<topic-name> --renumber
```

### 5. Overview QA

담당: `ppt_overview_qa`

검증:

- topic 구조
- allowed `data-skill`
- `class="edit-btn"`
- `Aim` 또는 `data-aim`
- HyperFrames lint

출력:

- `_workspace/ppt_qa_report.md`

### 6. User Review

사용자는 `overview.html`에서 다음을 수행한다.

- `Edit` 클릭
- 텍스트 직접 수정
- `Aim` 선택
- `Done` 클릭
- 클립보드 patch를 Codex에 전달
- Codex는 patch를 반영해 `index.html`과 `overview.html`을 갱신
- 사용자는 최종 파일화 전까지 같은 방식으로 반복 수정

### 7. PDF/PPTX Export

사용자가 overview를 최종 확인한 뒤에만 발표자료 파일화를 진행한다.

기본 목표:

- `topics/<topic-name>/exports/<topic-name>.pdf`
- `topics/<topic-name>/exports/<topic-name>.pptx`

### Optional MP4 Render

MP4 영상은 기본 최종 산출물이 아니다. 사용자가 명시적으로 영상 render를 요청한 뒤에만 실행한다.

```powershell
npx hyperframes render topics\<topic-name>
```

## 코드

topic 생성:

```powershell
npm run new-topic -- --name <topic-name> --title "<title>" --company "<company>" --type deck
npm run new-topic -- --name <topic-name> --title "<title>" --company "<company>" --type card-news
```

## 테스트 방법

```powershell
python scripts\validate_codex_port.py
python scripts\validate_topic.py topics\<topic-name>
npx hyperframes lint topics\<topic-name>
```

## 향후 개선사항

- QA 결과를 `_workspace/ppt_qa_report.md`에 자동 기록
- feedback patch를 topic에 저장하는 helper 추가
- PDF/PPTX export 자동화 스크립트 추가
