# Architecture

## 문제 분석

이 저장소는 일반 Python 백엔드가 아니라 HyperFrames HTML composition 제작 workspace다. 핵심 문제는 매번 다른 주제와 회사 디자인 문서를 받아도 동일한 절차로 16:9 발표자료를 만들고, 최종적으로 PDF 또는 PPTX로 파일화할 수 있게 만드는 것이다.

## 설계

아키텍처는 project-local Codex Harness와 HyperFrames topic 구조로 나뉜다.

```text
new_md/DESIGN-*.md
        |
        v
topic_intake_router
        |
        v
content plan -> visual plan -> topic build -> overview QA -> manual edit -> export
        |
        v
topics/<topic-name>/
```

구성 요소:

- `AGENTS.md`: 저장소 전체 작업 규칙과 허용 HyperFrames 타입
- `.codex/agents/*.toml`: 역할별 subagent 계약
- `.agents/skills/ppt-hyperframes-deck/SKILL.md`: 반복 제작 절차
- `.codex/skills/hyperframes*`: 기존 `2_slide_master` 방식의 HyperFrames 스킬
- `scripts/create_topic.py`: topic scaffold 생성
- `scripts/validate_codex_port.py`: harness 구조 검증
- `scripts/validate_topic.py`: topic 산출물 검증

## 구현

각 topic은 독립 프로젝트처럼 관리한다.

```text
topics/<topic-name>/
  BRIEF.md
  DESIGN.md
  hyperframes.json
  meta.json
  index.html
  overview.html
  assets/
  exports/
  renders/
  snapshots/
```

출력 타입별 루트 크기:

- `deck`: 1920x1080, 16:9, PDF/PPTX export 대상
- `card-news`: 1080x1080 기본, 필요 시 1080x1920

## 코드

topic 생성 스크립트는 표준 라이브러리만 사용한다. LLM 호출, API KEY, 외부 서비스 호출을 포함하지 않아 운영 위험이 낮다.

HyperFrames preview는 npm script를 통해 호출한다. MP4 render는 선택 사항이며 기본 최종 산출물이 아니다. PDF/PPTX export 전에는 사용자가 `overview.html`의 Edit/Aim으로 최종 형태를 충분히 수정할 수 있어야 한다.

## 테스트 방법

- harness: `python scripts\validate_codex_port.py`
- topic: `python scripts\validate_topic.py topics\<topic-name>`
- HyperFrames: `npx hyperframes lint topics\<topic-name>`
- review: `overview.html`의 `Edit`, `Aim`, `Done` 동작 확인

## 향후 개선사항

- PDF/PPTX export 파이프라인 표준화
- 디자인 md 파서 고도화
- overview patch를 `topics/<topic-name>/feedback.md`로 자동 저장
- card-news 세로형 scaffold 옵션 추가
