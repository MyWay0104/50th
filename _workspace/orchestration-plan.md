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

### 4. HyperFrames Build

담당: `hyperframes_ppt_builder`

출력:

- `topics/<topic-name>/index.html`
- `topics/<topic-name>/overview.html`
- `topics/<topic-name>/DESIGN.md`
- `topics/<topic-name>/meta.json`
- `topics/<topic-name>/hyperframes.json`
- `topics/<topic-name>/exports/`

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
