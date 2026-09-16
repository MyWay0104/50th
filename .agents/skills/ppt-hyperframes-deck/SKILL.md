---
name: ppt-hyperframes-deck
description: Use when creating, revising, or QA-checking HyperFrames 16:9 decks or card-news topics in this workspace.
---

# PPT HyperFrames Deck

이 저장소에서 발표자료(16:9 덱)와 카드형 뉴스를 반복 제작할 때 쓰는 절차다. `AGENTS.md`·`CLAUDE.md` 와 함께 읽는다. 실제 제작에서 검증된 순서이며, 57장 규모 덱을 두 차례 개정한 기록이 `_workspace/final_touch.md` 와 `_workspace/v0.4_progress.md` 에 있다.

## 1. 시작 전에 받아야 할 것

- 목적·대상·시간(또는 읽는 상황), 출처로 쓸 자료와 사실 경계
- 회사/브랜드와 디자인 입력 `new_md/DESIGN-<회사>.md`
- 출력 종류: `deck` 또는 `card-news`, topic 폴더 이름
- 최종 산출물은 PDF/PPTX. **export 는 사용자가 overview 최종 확인을 말한 뒤에만** 한다. MP4 는 명시 요청이 있을 때만.

## 2. 전체 흐름

```text
intake → 콘텐츠 계획 → 시각 계획 → (묶음 루프) → 전체 QA → 마지막 검토 → 문서 동기화 → 사용자 overview 검토 → export
```

장면이 20장을 넘으면 **묶음(차수) 단위**로 나눠 아래 루프를 돌린다.

```text
문구(slide_content_writer) → 배치(slide_ui_designer) → 강사 사전 검토(lecture_expert)
  → 조각 빌드(빌더, templates/briefs/builder.md) → check_fragment → splice_blocks
  → QA 게이트 → 강사 사후 검토(lecture_expert)
```

덱 전체에 걸친 수정(존댓말 전환, 시간 정보 삭제 같은 가로 방향 작업)은 장면을 다시 만들지 말고 **치환 표 방식**을 쓴다.

```text
서브에이전트가 장면별 치환 표(JSONL)를 만든다
  → apply_table.py --dry 로 원문 일치 확인(못 찾음 0)
  → apply_table.py 적용 → QA 게이트 → 마지막 검토
```

## 3. 마지막 검토 (사용자 확인 직전)

`hyperframes snapshot` 으로 장면별 PNG 를 만들고 세 갈래로 나눠 본다.

1. 시각 검토 A: 앞 절반 (정렬·치우침·잘림·오탈자·로고 위치)
2. 시각 검토 B: 뒤 절반
3. 내용 검토: `dump_deck_text.py` 결과로 사실·흐름·하우스 룰 위반

지시문은 `templates/briefs/review-final.md`, 사전 검토는 `templates/briefs/review-pre.md` 를 쓴다. 높음·중간 항목은 반영하고, 보류는 이유와 함께 QA 보고서의 사용자 확인 목록에 남긴다.

## 4. QA 게이트 (HTML 을 고칠 때마다)

```bash
python scripts/sync_overview.py topics/<topic>        # 장면 수가 바뀌면 --renumber
python scripts/validate_topic.py topics/<topic>
npx hyperframes check topics/<topic>                  # lint·런타임·레이아웃 겹침·명암비
python scripts/deck/qa_rules.py topics/<topic> --rules topics/<topic>/deck-rules.json
python scripts/sync_overview.py topics/<topic> --check
```

- `hyperframes check` 는 레이아웃 겹침·넘침과 WCAG 명암비까지 본다. 별도 브라우저 스크립트를 만들지 않는다.
- `qa_rules.py` 는 `check` 가 모르는 하우스 룰(시간 표기·존댓말·출처·사내 정보)을 본다.
- 인터넷이 막힌 환경에서는 `scripts/deck/localize_assets.py` 로 CDN 글꼴·스크립트를 먼저 로컬화한다.

## 5. 허용 출력 종류

- 덱(1920×1080): `title`, `title-bullets`, `title-image`, `title-tags`, `split`, `stat`, `steps`, `compare`, `evolution-flow`, `quote`, `kindergarten-notice`
- 카드뉴스(기본 1080×1080): `photo-cover`, `video-cover`, `stat`, `image-feature`

## 6. 운영 원칙 (사용 한도·중단 대비)

- 서브에이전트 동시 실행은 3–4개로 제한한다.
- 서브에이전트는 **한 장면을 끝낼 때마다 결과 파일에 덧붙여 저장**한다. 중단돼도 이어서 할 수 있다.
- 되돌리기 어려운 작업(조립·일괄 치환) 전에는 커밋한다.
- 진행 상태는 `_workspace/<주제>_progress.md` 표로 남긴다. 작업 관리 MCP 가 없어도 이 표로 재개한다.
- 작은 문구 수정은 멈춘 서브에이전트를 깨우지 말고 오케스트레이터가 직접 고친다.

## 7. 완료 보고 전 확인

- topic 폴더에 `index.html`·`overview.html`·`meta.json`·`hyperframes.json`·`DESIGN.md`·`exports/` 가 있다
- `overview.html` 에 `class="edit-btn"` 과 Aim UI(또는 `data-aim`)가 있다
- QA 게이트 5단계를 모두 통과했다(못 돌린 것이 있으면 이유를 적는다)
- 사용자 최종 확인 전에는 export 를 하지 않았다
- 문서(`BRIEF.md`·기획·QA 보고서·매핑표)를 실제 결과와 맞췄다

자세한 체크리스트는 `references/ppt-checklist.md` 에 있다.
