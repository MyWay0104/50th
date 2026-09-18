# 00 · 전역 CSS 패치 사양 (ROADMAP2, 2026-09-18)

> **v0.7에서 낱말이 바뀌었다 (2026-09-18, `ROADMAP3.md`).** 아래 설명·예시 마크업에 나오는 `두뇌 · 책 · 손발 · 조종 · 내 PC의 에이전트 · 정거장 · 열쇠`는 **v0.6 당시의 기록**이다. 지금 덱은 `LLM · RAG · Tool · Agent · Coding Agent · 단계 · 인증 키`를 쓴다. **CSS 규칙(F절)과 좌표·대비 계산은 그대로 유효**하므로 이 문서는 고치지 않고 남겨 둔다. 진행 띠 아이콘 순서도 그대로다(그림 파일은 바뀌지 않았고 대체 글자만 바뀌었다).

- 대상: `topics/sk-hynix-ai-agent-guide-edu/index.html` 의 `<style id="scene-styles">`
- 적용 방법: 이 문서 **F절의 CSS 블록을 `scene-styles` 맨 끝에 그대로 붙인다.** 기존 규칙은 지우지 않는다(뒤에 와서 덮어쓰는 방식). 장면 마크업은 고치지 않아도 A·C·D가 적용된다. E(구간 표지 진행 띠)만 새 마크업이 필요하다.
- 붙인 뒤: `python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu` 로 overview 재생성 → QA 게이트(G절).
- 근거 자료: `DESIGN.md`(Notion 최소 적용·주황 1색), `_workspace/roadmap2/scene-styles.css`, 장면 G00·L01·S08·C02·S01·G03·T01·G01·S25·A10·S41–S43, 스토리보드 「구간 표지(D01~D07) 설계」.

명암비 계산식은 WCAG 2.x 상대 휘도다. 이 문서에 쓴 휘도(L) 값: 캔버스 `#f6f5f4` 0.9143 · 흰색 1.0 · 전환 틴트 `#fbf1ea` 0.8936 · `--night #793400` 0.0652 · `--accent #dd5b00` 0.2285 · `--ink-3 #615d59` 0.1109 · `--ink-2 #31302e` 0.0296 · `--line-strong #c8c4bf` 0.5552.

---

## A. 상자 테두리·배경 패치

### A-1. 새 토큰

| 토큰 | 값 | 용도 | 대비(계산값) |
|---|---|---|---|
| `--box-line` | `#8a857f` (L 0.2371) | 상자류 1px 테두리, 점선 영역, 목록 점, 분포 막대 | 캔버스 **3.36:1** · 흰색 **3.66:1** · 전환 틴트 `#fbf1ea` **3.29:1** · `--box-muted` **3.10:1** |
| `--box-muted` | `#eeece9` (L 0.8405) | `.dg-box.muted`, `.step.is-muted`, 표 머리칸, `.flow-label` 의 톤 면 | 위 글자 `--ink-2` 11.2:1 · `--ink-3` 5.53:1 · 아이콘 선 `#31302e` 11.2:1 |
| `--on-night-line-strong` | `rgba(255,255,255,0.5)` (night 위 합성 `#bc9a80`, L 0.3536) | 반전 배경 위 상자·띠 테두리 | night **3.50:1** |
| `--on-night-fill` | `rgba(255,255,255,0.24)` (합성 `#99653d`, L 0.1642) | 반전 배경 위 muted 면, 진행 띠 "지나온 정거장" 채움 | 위 흰 아이콘·글자 4.90:1 |
| `--axis-tile` | `96px` | 진행 띠 타일 한 변 | — |

- 호출 측이 잰 후보 `#8f8a84`(캔버스 3.14 · 흰색 3.42)는 전환 장면 틴트 배경(T01–T03) 위에서 3.08:1 로 여유가 없다. 한 단계 어두운 `#8a857f` 로 정해 모든 배경에서 3.2:1 이상을 확보했다. 휘도(0.2371)가 `--accent`(0.2285)보다 약간 밝아, 중립선이 주황선보다 진해 보이지 않는다.
- 기존 `--hairline`(캔버스 1.15 · 흰색 1.25)과 `--line-strong`(캔버스 1.59 · 흰색 1.74)은 토큰으로 남긴다. 상자 **외곽선**에는 더 이상 쓰지 않고, 상자 **안쪽 구분선**에만 쓴다.

### A-2. 굵기

- 중립 상자: **1px 실선** `--box-line`. 굵기를 늘리지 않는다(1px→1px 이라 상자 크기·줄바꿈 변화 0).
- 점선 영역(`.placeholder`, `.dg-zone`, `.doc-gap`): 기존 2px 점선 유지, 색만 `--box-line`. `.fallback` 은 1px 점선 유지.
- 강조 상자: 기존 **2px 실선** `--accent` 유지(캔버스 3.46 · 흰색 3.77).

### A-3. 적용 대상 (테두리 색 `--hairline`/`--line-strong` → `--box-line`)

| 묶음 | 선택자 |
|---|---|
| 카드·패널 | `.split-panel` `.compare-col` `.flow-col` `.steps.row .step` `.code-card` `.data-table`(외곽) `.doc-mock` |
| 텍스트 상자 | `.dg-box` `.time-block` `.quote-points li` `.corner-art` |
| 작은 라벨 | `.chip` `.tag` `.concept-badge` |
| 점선 영역 | `.placeholder` `.dg-zone` `.fallback` `.doc-gap` `.act-bracket` |
| 도형 채움 | `.compare-list li::before`(목록 점) `.dist-bar`(분포 막대) `.doc-line.is-meta` |
| 강조 문장 상자 | `.callout` — 주황 8% 면이 캔버스와 1.10:1 이라 상자로 안 보인다. `1px solid var(--accent)` 추가, 안쪽 여백을 27px 35px 로 1px 줄여 **바깥 크기 불변** |

### A-4. 제외 대상과 이유

| 선택자 | 처리 | 이유 |
|---|---|---|
| `.data-table th`, `.data-table td` 의 `border-bottom` | `--line-strong`(흰색 위 1.74:1)까지만 | 표 안의 칸 선은 행을 따라 읽게 돕는 보조선이다. 외곽선과 같은 진하기로 5–6줄이 겹치면 격자가 글자보다 먼저 보인다. 표의 경계는 외곽선(3.66:1)이 맡는다 |
| `.code-title` 의 `border-bottom` | `--line-strong` | 카드 안 제목줄 구분선. 같은 이유 |
| `.steps::before`(세로 연결선) | `--line-strong` | 순서는 주황 번호 원이 전달한다. 연결선은 장식이라 1.4.11 대상이 아니다. 보이기만 하게 한 단계 올린다 |
| `.doc-line`(문서 도식의 본문 줄) | `--line-strong` | 여러 줄이 모여 "본문 있음"을 나타내는 질감이다. 3:1 로 올리면 제목 줄(`--ink-2`)과 위계가 뒤집힌다 |
| `.hero-tile`(S01 표지 아이콘 타일) | 그대로 | `aria-hidden` 장식. 표지 분위기를 유지한다. 정보를 담는 night 위 상자는 A-6 값으로 올린다 |
| `.stat` 의 `border-top` | 그대로 | 이미 `--ink` 3px |
| `.time-chip` | 그대로 | 구간 표시 삭제 뒤 미사용 |

### A-5. `.dg-box.muted` 와 위계 규칙

- `.dg-box.muted`: 배경 `--box-muted` + 테두리 `1px --box-line` + 글자 `--ink-2`. 지금은 배경이 장면 배경과 같은 `--canvas` 라서 "상자가 없는 것"처럼 보였다. `.steps.row .step.is-muted` 도 같은 값.
- 흰 패널(`.split-panel`·`.compare-col`) 안에 놓여도 흰색 대비 1.18:1 의 톤 차이 + 3.10:1 테두리로 구분된다.

위계는 아래 세 단계로 고정한다(강한 순).

| 단계 | 면 | 테두리 | 글자 | 규칙 |
|---|---|---|---|---|
| 강조 `.accent` / `.is-accent` | 흰색 | **2px `--accent`** | 제목 글자·번호 `--accent` | 한 줄(행)·한 묶음에 1개까지 |
| 기본 | 흰색 | 1px `--box-line` | `--ink` | — |
| 낮춤 `.muted` / `.is-muted` | `--box-muted` | 1px `--box-line` | `--ink-2` | 면 톤으로만 낮춘다. 테두리를 흐리게 하지 않는다 |

- 중립 테두리는 **절대 2px 로 올리지 않는다.** 굵기(2배)와 색상(주황)이 동시에 달라야 강조가 유지된다.
- 주황 글자는 흰색 위 3.77:1 이라 큰 글자 기준만 통과한다. **28px·600 이상 짧은 라벨에만** 쓴다(현재 사용처 모두 해당).
- `.chip.accent` 는 1px → 2px 로 올리고 여백을 7px 17px 로 줄여 크기를 그대로 둔다(`.time-band` 가 세로 가운데 정렬이라 1px 이라도 높이가 달라지면 줄이 어긋난다).

### A-6. `.scene.night`(짙은 주황 `#793400`) 위의 값

| 항목 | 현재 | 패치 |
|---|---|---|
| 상자 테두리(`.compare-col`, `.chip`) | `--on-night-line` 24% 흰색 = **1.86:1** (미달) | `--on-night-line-strong` = **3.50:1** |
| `.compare-heading` 밑줄 | 1.86:1 | 3.50:1 |
| 상자 면 | 투명 | 투명 유지. `.muted` 만 `--on-night-fill` |
| 강조 상자 | 주황은 night 위 **2.42:1** 이라 못 쓴다 | 2px `--on-night`(9.11:1) + 글자 `--on-night` |
| 보조 글자 `.dg-sub` `.dg-caption` | — | `--on-night-2`(6.20:1) |
| 아이콘 `.dg-icon` `.tb-icon` `.row-icon` `.head-icon` | — | 기존 `.col-icon` 과 같은 흰색 필터 |

---

## B. 저대비 컴포넌트 점검표

기준: 글자는 모두 22px 이상이다. 24px 이상(굵은 글씨는 18.66px 이상)은 큰 글자 3:1, 문장으로 읽는 본문은 4.5:1 권장. 비텍스트는 WCAG 1.4.11 의 3:1.

### B-1. 비텍스트(테두리·도형·아이콘)

| 컴포넌트 | 전경 / 배경 | 현재 | 기준 | 조치 |
|---|---|---|---|---|
| `.dg-box` `.time-block` `.chip` `.tag` `.split-panel` `.compare-col` `.code-card` `.data-table` 외곽 등 | `#e6e6e6` / 캔버스·흰색 | 1.15 · 1.25 | 3:1 | **수정** → `--box-line` 3.36 · 3.66 (F에 포함) |
| 흰 상자 면 자체 | 흰색 / 캔버스 | 1.09 | — | 면 대비로는 해결 불가. 테두리로 해결 |
| `.dg-box.muted` | 캔버스 / 캔버스 | 1.00 | 3:1(경계) | **수정** → `--box-muted` 면 + 테두리 3.10 |
| `.placeholder` 점선 | `#c8c4bf` / 캔버스·흰색 | 1.59 · 1.74 | 3:1 | **수정** → `--box-line` |
| `.dg-zone` 점선 | `#c8c4bf` / 캔버스 | 1.59 | 3:1 | **수정** → `--box-line` 3.36. `.dg-zone.accent` 는 3.46 그대로 |
| `.fallback` 점선, `.doc-gap`, `.concept-badge` 테두리 | `#c8c4bf` | 1.59–1.74 | 3:1 | **수정** → `--box-line` |
| `.callout` 면 | 주황 8% / 캔버스 | 1.10 | 3:1(경계) | **수정** → 1px `--accent` 테두리 3.46 |
| `.compare-list li::before` 점, `.dist-bar` | `#c8c4bf` / 흰색 | 1.74 | 3:1 | **수정** → `--box-line` 3.66 |
| `.dg-arrow`, `.steps.row .step + .step::before`, 번호 단계 `→` | `--ink-3` / 캔버스 | 5.99 (틴트 5.86) | 3:1 | 그대로 |
| `.dg-arrow` (night) | `--on-night-2` / night | 6.20 | 3:1 | 그대로 |
| 아이콘 `.col-icon` `.tb-icon` `.dg-icon` `.step-icon` 등 | 선 `#31302e` / 흰색·캔버스·muted | 13.2 · 12.1 · 11.2 | 3:1 | 그대로 |
| `.scene.night .col-icon`, `.hero-icon` | 흰색 85% / night | 7.08 | 3:1 | 그대로 |
| `.thesis` 밑줄, `.bullets li::before`, `.hero-rule`, 강조 테두리 | `--accent` / 캔버스·흰색·틴트 | 3.46 · 3.77 · 3.39 | 3:1 | 그대로 |
| `.time-blocks.is-steps .min` 번호 원 면 | 주황 8% / 흰색 | 1.10 | 장식 | 그대로. 숫자(글자)가 정보를 전달하고 원은 장식이다. (선택) 1px `--accent` 외곽선을 넣을 수 있으나 한 장에 주황 원 5개가 생겨 절제 원칙과 부딪힌다 → F에 넣지 않음 |
| `.status-dot.ok` | `#1aae39` / 흰색·캔버스 | 2.93 · 2.70 | 3:1 | **조건부 그대로.** `DESIGN.md` 가 색을 고정했다. 점은 항상 글자 라벨("통과"·"승인")과 함께 쓰여 색이 유일한 전달 수단이 아니다. 규칙: **상태 점만 단독으로 두지 않는다** |
| `.status-dot.warn` | `#793400` / 흰색 | 9.11 | 3:1 | 그대로 |
| `.scene.night` 상자 테두리 | 24% 흰색 / night | 1.86 | 3:1 | **수정** → 50% 흰색 3.50 |
| `.hero-tile` 테두리 | 24% 흰색 / night | 1.86 | 장식 | 그대로(A-4) |
| `.quote-mark` | 주황 35% | — | 장식 | 그대로 |

### B-2. 텍스트

| 컴포넌트 | 전경 / 배경 | 현재 | 기준 | 조치 |
|---|---|---|---|---|
| `.chip` `.tag` `.dg-box` 본문 | `--ink` / 흰색 | 19.5 | 4.5 | 그대로 |
| `.dg-sub` 24–28px | `--ink-3` / 흰색 · muted(새 값) | 6.53 · 5.53 | 4.5 | 그대로 |
| `.dg-caption` `.source` `.deck-footer` `.guide-ref` 24px | `--ink-3` / 캔버스 · 틴트 | 5.99 · 5.86 | 4.5 | 그대로 |
| `.placeholder-id` `.placeholder-label` `.concept-badge` | `--ink-3` / 흰색 | 6.53 | 4.5 | 그대로. 단 `.concept-badge`·`.dg-zone-label` 은 22px 로 `DESIGN.md` 최소 24px 아래다(대비가 아닌 크기 문제, 이번 패치 범위 밖 — 다음 정리 때 24px 권장) |
| `.data-table th` 24px·700 | `--ink-3` / muted(새 값) | 5.53 | 4.5 | 그대로 |
| `.chip.accent`, `.dg-box.accent`, `.done-label`, `.compare-col.is-accent .compare-kicker` | `--accent` / 흰색 | 3.77 | 큰 글자 3:1 | 그대로(모두 24px·700 이상 짧은 라벨). 문장에는 주황 글자 금지 |
| `.bullets li strong` 44px·700 | `--accent` / 캔버스 | 3.46 | 3:1 | 그대로 |
| `.callout strong` 34px·700 | `--accent` / 주황 8%+캔버스 | 3.16 | 3:1 | 그대로(여유 작음 — 글자 크기를 28px 아래로 내리지 않는다) |
| `.code-body .hl` 28px·400 | `--accent` / 주황 8%+흰색 | 3.42 | 3:1 통과, 4.5 미달 | **선택 수정(F 미포함)**: 코드는 본문처럼 읽으므로 `color: var(--night)`(9.1:1)로 바꾸면 4.5 를 넘는다. 강조 느낌은 연주황 면이 유지한다. 코드 카드 인상이 달라지므로 강사 승인 뒤 적용 |
| `.time-blocks.is-steps .min` 숫자 28px·800 | `--accent` / 주황 8%+흰색 | 3.42 | 3:1 | 그대로 |
| `.step-num`, `.tag.accent`, 강조 번호 원 | 흰색 / `--accent` | 3.77 | 3:1(모두 24px·700 이상) | 그대로 |
| night 보조 글자 | `--on-night-2` / night | 6.20 | 4.5 | 그대로 |
| night 위 주황 글자(`.compare-col.is-accent .compare-kicker` 등) | `--accent` / night | 2.42 | 3:1 | **수정** → `--on-night` (F에 포함) |
| `#a39e98` | — / 캔버스 | 2.44 | — | 미사용 확인(`DESIGN.md` 금지 유지) |

---

## C. 가운데 정렬 패치

### C-1. `.dg-box` — 가로·세로 가운데

- `display:flex; flex-direction:column; justify-content:center; align-items:center;` 를 **기본값**으로 한다. 지금은 `.dg-row.stretch` 에서 가장 높은 상자에 맞춰 늘어난 상자의 내용이 위에 붙는다(L01 `is-roles`, G03, S25, S40, A06).
- 직계 자식 구성(글자 / `img.dg-icon` / `span` / `span.dg-sub`)은 세로로 쌓이는 블록뿐이라 줄이 깨지지 않는다. 글자 줄바꿈의 가운데 정렬은 기존 `text-align:center` 가 맡는다.
- **예외 3곳**(직계 자식이 한 줄로 나란히 놓여야 하는 상자): A10 의 `status-dot + 글자 + dg-sub` 2개, S25 의 `inline-icon + status-dot + span` 1개. `:has()` 로 가로 방향 flex 로 돌린다. `dg-sub` 는 `flex: 0 0 100%` 로 다음 줄에 내리고, S25 는 긴 문장이 아이콘과 같은 줄에 남도록 `nowrap`.
- 기존 선택형 규칙 `.dg-row.stretch > .dg-box.is-center`, `[S02] .split-panel .dg-box { justify-content:center }` 와 결과가 같아 충돌 없다.
- 아이콘 덧씌움(`.icon-track.is-overlay/.is-grid`, S40)은 상자 왼쪽 24–56px 에 놓이고 글자는 원래도 가로 가운데였으므로 겹침 조건이 달라지지 않는다.

### C-2. `.time-block` — 숫자 원·글자 모두 가운데

- `align-items:center; justify-content:center; text-align:center;` 추가(이미 세로 flex).
- `.time-blocks.time-band` 는 `align-items: stretch` 로 바꾼다. 지금은 `.time-band` 의 `center` 때문에 S08 에서 글자가 두 줄인 블록만 키가 커진다. 같은 높이로 맞춘 뒤 내용을 가운데 둔다.
- **`.tb-icon` 과 겹침 확인**
  - 번호 원이 보이는 블록(G01·S08·M01·S13·S19·S26): 아이콘은 y 28–60(64)px, 글자 `.what` 은 원(56px)+간격(12px) 아래인 y ≥ 88px 에서 시작한다. 세로로 겹치지 않으므로 글자 폭과 무관하게 안전하다. 원은 가로 가운데(예: 폭 313px 블록에서 x 129–185), 아이콘은 오른쪽 끝(x 270–302)이라 가로로도 84px 떨어진다.
  - 번호 원을 숨긴 블록(S41·S42·S43): 글자 첫 줄과 아이콘이 같은 높이에 온다. S42(3칸, 블록 폭 약 265px)에서 "멈춤·정리"(약 130px)는 아이콘과 11px 차이로 아슬아슬하다. → 이 세 장면만 **좌우 여백을 64px(= 20 + 36 + 8)로 대칭**으로 잡아 글자가 아이콘 자리에 들어가지 못하게 하고, 아이콘을 세로 가운데로 옮긴다. 글자 칸 폭: S42 137px(28px 글자 4.5자), S41·S43 약 283px. 넘으면 겹치지 않고 두 줄로 접힌다.

### C-3. 그 밖의 상자류 판단

| 컴포넌트 | 판단 | 이유 |
|---|---|---|
| `.chip`, `.tag` | 포함(`justify-content:center; text-align:center`) | 격자·늘림 안에 들어가도 가운데 유지. 평소엔 글자 폭 상자라 변화 없음 |
| `.callout`, `.done-box`, `.fallback` | **세로만** 가운데(`align-content:center`, 블록 컨테이너용 — Chrome 123 이상에서 동작, 미지원이면 지금과 같음) | 문장 상자다. `strong` 머리말 + 문장이 한 줄로 이어져야 해서 flex 세로 쌓기를 쓰면 줄이 끊긴다. 가로는 왼쪽 정렬이 의도("완료 조건" 라벨 → 문장 순서로 읽음) |
| `.quote-points li`, `.hero-tile`, `.corner-art`, `.placeholder`(기본) | 변경 없음 | 이미 가운데 |
| `.steps.row .step` | **제외** | 카드마다 설명 줄 수가 다르다. 세로 가운데로 두면 번호 원이 카드마다 다른 높이에 놓여 "1→2→3" 기준선이 무너지고, 오른쪽 위 `.step-icon`(top 48px)과의 줄 맞춤도 깨진다 |
| `.stat` | 제외 | 상자가 아니라 위쪽 굵은 선 + 큰 숫자다. 선의 왼쪽 끝과 숫자 왼쪽 끝을 맞추는 것이 디자인 |
| `.compare-col`, `.flow-col`, `.split-panel` | 제외 | 머리글 + 불릿 목록. 불릿 점은 공통 왼쪽 기준선이 있어야 읽히고, 머리글 밑줄은 카드 폭 전체를 쓴다 |
| `.placeholder.is-spec` | 제외(세로 가운데는 이미 됨) | "넣을 자료 / 조건 / 대체" 세 줄의 머리말이 같은 x 에서 시작해야 비교가 된다 |
| `.code-card`, `.data-table`, `.doc-mock` | 제외 | 코드·표·문서 도식은 왼쪽 정렬이 원래 모양이다 |
| `.dg-zone` | 제외 | 왼쪽 위 구역 라벨 + 안쪽 행을 담는 그릇 |

---

## D. 썸네일 모서리 패치

- 원인: `.split-image` 는 컨테이너에 `border-radius + overflow:hidden` 을 건다. `.is-thumb` 은 `img { width:auto }` 라 이미지 오른쪽 끝이 컨테이너 끝(약 913px)에 닿지 않는다(G00: 높이 340px → 16:9 폭 약 604px). 왼쪽 두 모서리만 컨테이너에 잘려 둥글고 오른쪽은 각지게 보인다.
- 수정: **이미지 자체에** `border-radius: var(--radius)` 를 준다. `width:auto; height:100%` 라 요소 상자와 그림이 일치하므로 네 모서리가 모두 둥글게 잘린다. 컨테이너 규칙은 그대로 둔다.
- 범위 밖 메모: `.split-image.pair`(A01)처럼 `object-fit:contain` 으로 여백이 생기는 이미지는 요소에 반경을 줘도 그림 모서리가 둥글어지지 않는다. 흰 바탕 논문 그림이라 문제가 보이지 않아 이번엔 건드리지 않는다. 사진을 새로 넣을 때는 `is-thumb`(높이 기준) 또는 `is-fit`(폭 기준)을 쓴다.

---

## E. 구간 표지 진행 띠 (D01–D07)

### E-1. 구성

- 새 클래스: `.axis-strip`(띠, `<ol>`) · `.axis-stop`(정거장, `<li>`) · `.axis-tile`(아이콘 타일 96px) · `.axis-icon`(48px) · `.axis-label`(28px) · `.axis-prep`(D01 "준비" 표시). 상태: `is-done` / `is-current` / `is-todo`.
- 아이콘 6개(순서 고정): `brain`(두뇌) → `book-open`(책) → `hand`(손발) → `repeat`(조종) → `terminal`(내 PC의 에이전트) → `rocket`(적용). "준비"는 `key`. 모두 `assets/img/icons/*.svg` 에 있다.
- 배치: 표지 글(머리말·제목·한 줄)은 왼쪽 정렬이므로 띠도 **왼쪽 끝 x=120px 에서 시작**한다. 6칸 등폭 격자(1680 ÷ 6 = 280px), 타일·라벨 모두 칸의 왼쪽에 붙인다. 정거장 사이는 2px 선(타일 옆 12px 띄움, 길이 280 − 96 − 24 = 160px).
- **띠의 위치는 일곱 장에서 같아야 한다**(넘길 때 상태만 바뀌는 것처럼 보이게). 그래서 흐름 배치가 아니라 `top: 720px` 절대 위치로 고정하고, 표지 장면의 아래 여백을 400px 로 늘려 글 묶음이 y 80–680px 안에서 세로 가운데에 놓이게 한다.
  - 글 묶음 높이: 머리말 39 + 제목(28 + 114, 두 줄이면 28 + 229) + 한 줄(28 + 59) = 268px / 383px → 600px 영역의 세로 가운데이므로 y 246–514 / 189–572. 띠(720px)와 148px 이상 떨어진다.
  - 띠 높이: 타일 96 + 간격 16 + 라벨 한 줄 38(+밑줄 8) = 최대 158px → y 720–878. 풋터(y ≈ 998)와 120px 떨어진다.
  - 라벨 폭: 칸 280 − 오른쪽 여백 24 = 256px. 가장 긴 "내 PC의 에이전트"가 28px·700 에서 약 220px 로 한 줄에 들어간다.
- 글자 크기 종류: 28(머리말·라벨) · 104(제목) · 44(한 줄) · 24(풋터) = 4종.

### E-2. 상태 표현 (night 배경 기준, 대비 계산값)

| 상태 | 타일 | 아이콘 | 라벨 | 들어오는 연결선 |
|---|---|---|---|---|
| `is-done` 지나온 정거장 | `--on-night-fill` 채움 + 1px `--on-night-line-strong`(night 대비 3.50) | 흰색 100% (채움 위 4.90) | `--on-night` 500 | 2px 실선 `--on-night`(9.11) |
| `is-current` 현재 | 투명 + **4px `--on-night`**(9.11) | 흰색 100% | `--on-night` **700** + 4px 흰 밑줄 | 2px 실선 `--on-night` |
| `is-todo` 남은 정거장 | 투명 + 1px `--on-night-line-strong`(3.50) | 흰색 60%(4.34) | `--on-night-2` 400(6.20) | 2px 점선 `--on-night-line-strong`(3.50) |

- "흐림"도 3:1 아래로 내려가지 않는다(스토리보드 R2-20).
- 지나온 정거장을 순백으로 꽉 채우지 않는 이유: D07 에서는 흰 타일 5개가 현재 정거장보다 먼저 눈에 들어온다. 24% 채움으로 "지나옴"을 나타내고, 가장 밝은 것은 현재 정거장의 굵은 흰 테두리 하나로 둔다.
- 밝은 배경(G01 의 비유 축 띠)에서도 같은 마크업을 쓸 수 있게 기본값을 밝은 배경용으로 두고 `.scene.night` 에서 덮어쓴다. 밝은 배경: 기본 흰 타일 + 1px `--box-line`, 현재 4px `--accent`, 지나옴 `--box-muted` 채움, 남음 아이콘 60%(흰색 위 3.79).

### E-3. 표지 전체 마크업 (D03 기준)

`id`·`data-start` 는 빌더가 순번에 맞춰 넣는다. 인라인 style·hex 색 없음.

```html
<section id="s-N" class="scene clip title-scene night" data-skill="title" data-scene-id="D03" data-start="0" data-duration="5" data-track-index="0">
  <div class="hero-kicker" data-editable="true">Part 2 · LangChain 실습</div>
  <h1 class="hero-title" data-editable="true">책 — 찾아보며 답합니다, RAG</h1>
  <p class="hero-sub" data-editable="true">실습 04</p>
  <ol class="axis-strip" aria-label="오늘의 여섯 정거장">
    <li class="axis-stop is-done"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/brain.svg" alt="두뇌 아이콘"></span><span class="axis-label" data-editable="true">두뇌</span></li>
    <li class="axis-stop is-current"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/book-open.svg" alt="책 아이콘"></span><span class="axis-label" data-editable="true">책</span></li>
    <li class="axis-stop is-todo"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/hand.svg" alt="손발 아이콘"></span><span class="axis-label" data-editable="true">손발</span></li>
    <li class="axis-stop is-todo"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/repeat.svg" alt="조종 아이콘"></span><span class="axis-label" data-editable="true">조종</span></li>
    <li class="axis-stop is-todo"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/terminal.svg" alt="터미널 아이콘"></span><span class="axis-label" data-editable="true">내 PC의 에이전트</span></li>
    <li class="axis-stop is-todo"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/rocket.svg" alt="적용 아이콘"></span><span class="axis-label" data-editable="true">적용</span></li>
  </ol>
  <aside class="speaker-note">지금까지 두뇌에 직접 묻고 답의 모양을 바꿔 봤습니다. 여기서부터는 두뇌가 모르는 자료를 책처럼 찾아보며 답하게 만듭니다.</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
</section>
```

상태 배치표(빌더용): D02 = current 1번째 / D03 = done 1, current 2 / D04 = done 1–2, current 3 / D05 = done 1–3, current 4 / D06 = done 1–4, current 5 / D07 = done 1–5, current 6. 나머지는 `is-todo`.

### E-4. D01 "준비" 변형

- 여섯 정거장은 모두 `is-todo`. 띠의 **첫 자식**으로 `axis-prep` 한 줄을 넣는다. 절대 위치(띠 왼쪽 끝 위 24px)라 격자 칸을 차지하지 않고, 여섯 정거장의 좌표는 D02–D07 과 똑같다.
- night 위: 흰 면 pill + `--night` 글자(9.11:1) + 원본 색 열쇠 아이콘(흰 면 위 13.2:1). 화면에서 가장 밝은 요소가 "준비" 하나가 된다. pill 은 `DESIGN.md` 가 태그에 허용한 999px 모서리다.
- pill 높이 약 60px → y 636–696. D01 제목이 두 줄이어도 글 묶음 아래 끝(572px)과 64px 떨어진다.

```html
<ol class="axis-strip" aria-label="오늘의 여섯 정거장">
  <li class="axis-prep is-current"><img class="axis-icon" src="assets/img/icons/key.svg" alt="준비 아이콘"><span data-editable="true">준비</span></li>
  <li class="axis-stop is-todo"><span class="axis-tile"><img class="axis-icon" src="assets/img/icons/brain.svg" alt="두뇌 아이콘"></span><span class="axis-label" data-editable="true">두뇌</span></li>
  <!-- 나머지 다섯 정거장도 is-todo -->
</ol>
```

### E-5. 함께 처리해야 하는 문서 충돌 (이 사양 밖, 오케스트레이터 몫)

- `DESIGN.md` 의 금지 항목 "짙은 주황 반전 밴드를 S01·G02 외 장면에 쓰지 않는다"와 스토리보드 결정(D01–D07 = `title-scene night`)이 충돌한다. 표지를 빌드하기 전에 `DESIGN.md` 에 **"구간 표지 D01–D07 은 예외"** 한 줄과 A-1 의 새 토큰 5개를 추가해야 한다. `_workspace/ppt_visual_plan.md` 의 토큰 표도 같이 고친다.

---

## F. 붙여 넣을 CSS 블록

`<style id="scene-styles">` 의 **맨 끝**에 그대로 붙인다. 색은 모두 토큰 참조이며 hex 는 `:root` 선언에만 있다.

```css
      /* ===== ROADMAP2 전역 패치 (2026-09-18): 상자 대비 · 가운데 정렬 · 썸네일 모서리 · 구간 표지 진행 띠 =====
         기존 규칙을 지우지 않고 뒤에서 덮어쓴다. 사양: _workspace/roadmap2/slide_ui/00_global_css_patch.md */
      :root {
        --box-line: #8a857f;                               /* 상자 테두리: 캔버스 3.36 · 흰색 3.66 · 전환 틴트 3.29 */
        --box-muted: #eeece9;                              /* 낮춤 상자 면: 테두리 대비 3.10, 위 글자 ink-3 5.53 */
        --on-night-line-strong: rgba(255, 255, 255, 0.5);  /* 반전 배경 위 테두리 3.50 */
        --on-night-fill: rgba(255, 255, 255, 0.24);        /* 반전 배경 위 낮춤 면 · 지나온 단계 채움 */
        --axis-tile: 96px;
      }

      /* --- A. 상자 테두리: 1px 유지, 색만 3:1 이상으로 --- */
      .split-panel, .compare-col, .flow-col, .steps.row .step, .code-card, .data-table, .doc-mock,
      .dg-box, .time-block, .quote-points li, .corner-art,
      .chip, .tag, .concept-badge,
      .placeholder, .dg-zone, .fallback, .doc-gap, .act-bracket { border-color: var(--box-line); }
      /* 상자 안쪽 구분선·연결선은 한 단계만 올린다(격자가 글자보다 먼저 보이지 않게) */
      .code-title, .data-table th, .data-table td { border-bottom-color: var(--line-strong); }
      .steps::before { background: var(--line-strong); }
      .doc-line { background: var(--line-strong); }
      .doc-line.is-title { background: var(--ink-2); }
      .doc-line.is-meta { background: var(--box-line); }
      /* 정보를 담는 작은 도형 */
      .compare-list li::before, .dist-bar { background: var(--box-line); }
      .compare-col.is-accent .compare-list li::before, .dist-bar.is-accent { background: var(--accent); }
      /* 낮춤 상자: 면 톤으로만 낮춘다 */
      .dg-box.muted, .steps.row .step.is-muted { background: var(--box-muted); }
      .flow-label, .data-table th { background: var(--box-muted); }
      .flow-col.after .flow-label { background: var(--accent); }
      /* 강조 상자: 2px 주황 유지(중립선은 2px 로 올리지 않는다) */
      .dg-box.accent, .compare-col.is-accent, .steps.row .step.is-accent, .flow-col.after,
      .time-block.is-accent, .done-box, .dg-zone.accent { border-color: var(--accent); }
      .dg-box.accent, .compare-col.is-accent, .steps.row .step.is-accent, .flow-col.after,
      .time-block.is-accent, .done-box { border-width: 2px; border-style: solid; }
      .chip.accent { border: 2px solid var(--accent); padding: 7px 17px; }
      .tag.accent { border-color: var(--accent); }
      /* 강조 문장 상자: 연주황 면만으로는 경계가 안 보인다. 1px 주황선, 여백을 1px 줄여 크기 불변 */
      .callout { padding: 27px 35px; border: 1px solid var(--accent); }

      /* 반전 배경 위 상자 */
      .scene.night .compare-col, .scene.night .chip { border-color: var(--on-night-line-strong); }
      .scene.night .compare-heading { border-bottom-color: var(--on-night-line-strong); }
      .scene.night .dg-box, .scene.night .time-block, .scene.night .tag, .scene.night .split-panel,
      .scene.night .quote-points li { border-color: var(--on-night-line-strong); background: transparent; color: var(--on-night); }
      .scene.night .placeholder, .scene.night .dg-zone, .scene.night .fallback { border-color: var(--on-night-line-strong); }
      .scene.night .dg-box.muted { background: var(--on-night-fill); }
      .scene.night .dg-box.accent, .scene.night .time-block.is-accent, .scene.night .compare-col.is-accent { border-color: var(--on-night); color: var(--on-night); }
      .scene.night .compare-col.is-accent .compare-kicker { color: var(--on-night); }
      .scene.night .compare-col.is-accent .compare-heading { border-bottom-color: var(--on-night); }
      .scene.night .compare-list li::before, .scene.night .compare-col.is-accent .compare-list li::before { background: var(--on-night); }
      .scene.night .dg-sub, .scene.night .dg-caption { color: var(--on-night-2); }
      .scene.night .dg-icon, .scene.night .tb-icon, .scene.night .row-icon, .scene.night .head-icon { filter: brightness(0) invert(1); }

      /* --- C. 가운데 정렬 --- */
      /* 텍스트 상자: 늘어난 높이 안에서 내용을 가로·세로 가운데로 */
      .dg-box { display: flex; flex-direction: column; justify-content: center; align-items: center; }
      .dg-box > * { max-width: 100%; }
      /* 예외: 상태 점·인라인 아이콘이 글자와 한 줄에 놓이는 상자 (A10 · S25) */
      .dg-box:has(> .status-dot), .dg-box:has(> .inline-icon) { flex-direction: row; flex-wrap: wrap; align-content: center; }
      .dg-box:has(> .status-dot) > .dg-sub { flex: 0 0 100%; }
      .dg-box:has(> .inline-icon) { flex-wrap: nowrap; }
      .dg-box > .status-dot, .dg-box > .inline-icon { flex-shrink: 0; }
      .dg-box:has(> .inline-icon) > span { min-width: 0; }
      /* 번호 단계 블록: 숫자 원·글자 모두 가운데, 한 줄의 블록 높이는 같게 */
      .time-block { align-items: center; justify-content: center; text-align: center; }
      .time-blocks.time-band { align-items: stretch; }
      /* 번호 원을 숨긴 블록(S41–S43)은 글자와 아이콘이 같은 높이다. 좌우 여백을 대칭(20+36+8)으로 잡아 겹침을 막는다 */
      .scene[data-scene-id="S41"] .time-block:has(> .tb-icon),
      .scene[data-scene-id="S42"] .time-block:has(> .tb-icon),
      .scene[data-scene-id="S43"] .time-block:has(> .tb-icon) { padding-left: 64px; padding-right: 64px; }
      .scene[data-scene-id="S41"] .tb-icon,
      .scene[data-scene-id="S42"] .tb-icon,
      .scene[data-scene-id="S43"] .tb-icon { top: 50%; transform: translateY(-50%); }
      /* 작은 라벨: 늘어난 칸 안에서도 가운데 */
      .chip, .tag { justify-content: center; text-align: center; }
      /* 문장 상자: 가로는 왼쪽(의도), 세로만 가운데. 블록 컨테이너 align-content 는 미지원 브라우저에서 무시된다 */
      .callout, .done-box, .fallback { align-content: center; }

      /* --- D. 썸네일: 컨테이너가 아니라 그림 자체를 둥글게 --- */
      .split-image.is-thumb > img:first-child { border-radius: var(--radius); }

      /* --- E. 비유 축 진행 띠 (구간 표지 D01–D07 · G01) --- */
      .axis-strip { position: relative; display: grid; grid-template-columns: repeat(6, 1fr); width: 100%; margin-top: 48px; }
      .axis-stop { position: relative; display: flex; flex-direction: column; align-items: flex-start; gap: 16px; min-width: 0; padding-right: 24px; }
      .axis-tile { display: flex; align-items: center; justify-content: center; flex-shrink: 0; width: var(--axis-tile); height: var(--axis-tile); border: 1px solid var(--box-line); border-radius: var(--radius); background: var(--surface); }
      .axis-icon { width: 48px; height: 48px; object-fit: contain; }
      .axis-label { font-size: var(--fs-small); font-weight: 500; line-height: 1.35; color: var(--ink-2); }
      /* 단계 사이 연결선: 앞 타일 오른쪽 12px 부터 이 타일 왼쪽 12px 앞까지 */
      .axis-stop + .axis-stop::before {
        content: ""; position: absolute;
        top: calc(var(--axis-tile) / 2 - 1px);
        left: calc(-100% + var(--axis-tile) + 12px);
        width: calc(100% - var(--axis-tile) - 24px);
        border-top: 2px dashed var(--box-line);
      }
      /* 상태: 지나옴(채움) · 현재(굵은 테두리와 굵은 글씨) · 남음(흐림, 단 3:1 이상) */
      .axis-stop.is-done .axis-tile { background: var(--box-muted); }
      .axis-stop.is-done::before, .axis-stop.is-current::before { border-top-style: solid; }
      .axis-stop.is-current .axis-tile { border: 4px solid var(--accent); }
      .axis-stop.is-current .axis-label { padding-bottom: 4px; border-bottom: 4px solid var(--accent); font-weight: 700; color: var(--ink); }
      .axis-stop.is-todo .axis-icon { opacity: 0.6; }
      .axis-stop.is-todo .axis-label { font-weight: 400; color: var(--ink-3); }
      /* D01 "준비" 표시: 띠 왼쪽 끝 위. 격자 칸을 차지하지 않아 여섯 단계 좌표가 모든 표지에서 같다 */
      .axis-prep { position: absolute; left: 0; bottom: calc(100% + 24px); display: inline-flex; align-items: center; gap: 12px; padding: 10px 24px; border: 1px solid var(--box-line); border-radius: 999px; background: var(--surface); font-size: var(--fs-small); font-weight: 700; line-height: 1.35; color: var(--ink); }
      .axis-prep.is-current { border: 2px solid var(--accent); color: var(--accent); }
      .axis-prep .axis-icon { width: 32px; height: 32px; }
      /* 반전 배경 위 */
      .scene.night .axis-tile { border-color: var(--on-night-line-strong); background: transparent; }
      .scene.night .axis-icon { filter: brightness(0) invert(1); }
      .scene.night .axis-label { color: var(--on-night); }
      .scene.night .axis-stop + .axis-stop::before { border-top-color: var(--on-night-line-strong); }
      .scene.night .axis-stop.is-done .axis-tile { background: var(--on-night-fill); }
      .scene.night .axis-stop.is-done::before, .scene.night .axis-stop.is-current::before { border-top-color: var(--on-night); }
      .scene.night .axis-stop.is-current .axis-tile { border-color: var(--on-night); }
      .scene.night .axis-stop.is-current .axis-label { border-bottom-color: var(--on-night); color: var(--on-night); }
      .scene.night .axis-stop.is-todo .axis-label { color: var(--on-night-2); }
      .scene.night .axis-prep, .scene.night .axis-prep.is-current { border-color: var(--on-night); background: var(--on-night); color: var(--night); }
      .scene.night .axis-prep .axis-icon { filter: none; }
      /* 표지 위의 띠: 일곱 장에서 같은 자리(top 720px). 글 묶음은 그 위 영역에서 세로 가운데 */
      .scene.title-scene:has(> .axis-strip) { padding-bottom: 400px; }
      .scene.title-scene > .axis-strip { position: absolute; top: 720px; left: 120px; right: 120px; width: auto; margin: 0; }
```

덮어쓰기 점검(특이도)
- 중립 테두리는 `border-color` 만 바꾼다. 강조 변형(`.dg-box.accent` 0,2,0 등)은 특이도가 높아 원래도 이기지만, 순서 의존을 없애려고 바로 아래에서 다시 선언했다.
- `.scene.night .chip`(0,3,0)·`.scene.night .compare-col` 은 기존 값이 이기므로 night 묶음에서 따로 올렸다.
- `.axis-stop + .axis-stop::before` 와 `.axis-stop.is-done::before` 는 특이도가 같다(0,2,1). **상태 규칙이 뒤에 와야 하므로 블록 안 순서를 바꾸지 않는다.**
- `.dg-row.stretch > .dg-box.is-center`, `[S02] .split-panel .dg-box`, `[S06] .dg-box.is-center` 는 새 기본값과 같은 방향이라 그대로 둔다.

---

## G. 회귀 위험 목록

크기 변화 요약: 중립 테두리 1px→1px, 강조 2px→2px, `.chip.accent`·`.callout` 은 여백으로 상쇄 → **이 패치로 상자 높이·폭이 늘어나는 곳은 S41–S43 의 좌우 여백 한 곳뿐**이다. 위험은 주로 "내용 위치 이동"에서 나온다.

| # | 위험 | 해당 장면 유형 | 확인 방법 |
|---|---|---|---|
| 1 | **한 줄에 놓인 상자끼리 아이콘·번호 원의 높이가 어긋남.** 세로 가운데 정렬이라 줄 수가 다른 상자는 내용 시작 높이가 달라진다(28px 글자 한 줄 차이 = 약 18px 어긋남) | `dg-icon` 있는 `.dg-row.stretch`(L01·G03·S02), 번호 블록 행(G01 오전 5칸 — "Claude Code 설치 확인·작동"만 두 줄 가능, S08·M01·S13·S19) | 스냅샷에서 같은 행의 아이콘·원 y 좌표를 비교. 어긋남이 거슬리면 CSS 가 아니라 **문구를 같은 줄 수로 맞추도록 `slide_content_writer` 에 요청**(예: L01 `dg-sub` 를 세 상자 모두 2줄) |
| 2 | **`.dg-box` 가 flex 로 바뀌어, 글자와 인라인 태그(`strong`·`code`·`b`·`br`)를 섞은 상자는 태그마다 줄이 끊김.** 현재 0건이지만 새 장면에서 생길 수 있다 | 새로 만드는 D·E·LAB·N·R·V 계열 장면의 개념도 | `Grep`: `class="dg-box[^"]*"[^>]*>[^<]*<(strong\|b\|code\|em\|a\|br)` 와 `</span>[^<\s][^<]*</div>` 를 `index.html` 에 돌려 0건 확인. 필요하면 문장을 `<span>` 하나로 감싼다. `check_fragment.py` 규칙에 추가 권장 |
| 3 | **S41–S43 번호 블록의 글자 칸이 좁아져 두 줄로 접힘 → 블록 높이 +38px.** S42(3칸)는 글자 칸 137px | S41·S42·S43 (실습 안내판, 왼쪽 열이 출처 줄과 가까움) | 세 장면 스냅샷에서 `.what` 이 한 줄인지, 왼쪽 열 아래 끝이 풋터(y 998)와 겹치지 않는지 확인. 접히면 라벨을 4자 이내로 줄이거나 S42 를 2칸으로 |
| 4 | 표지 제목이 두 줄이 될 때 D01 의 "준비" pill 과 거리 | D01(제목 15자), D05·D06(두 줄 예상) | D01·D05·D06 스냅샷. 글 묶음 아래 끝 ≤ 600px, pill 위 끝 636px 확인 |
| 5 | 테두리가 진해지면서 상자가 많은 장면이 무거워 보임 | 상자 6개 이상: S25·S40·S10·V01·A06, 흰 패널 안 상자(S02·S21) | 스냅샷 육안 검토. 무거우면 테두리를 흐리게 하지 말고 **상자 수를 줄이거나 `.muted` 로 낮춘다**(3:1 은 유지) |
| 6 | `.time-blocks.time-band` 를 `stretch` 로 바꾸면 S08 의 블록 높이가 가장 큰 블록에 맞춰짐(줄어들지는 않음) | S08 | 아래 칩 줄·완료 조건 상자가 밀리지 않는지 스냅샷 확인 |
| 7 | `:has()`(Chrome 105+), 블록 `align-content`(Chrome 123+) 의존 | 전 장면(A10·S25·S41–S43·표지) | `npx hyperframes check` 의 런타임 렌더와 PPTX 변환 스크립트가 쓰는 브라우저 버전 확인. `align-content` 는 미지원이어도 지금과 같게 보인다 |
| 8 | night 장면 테두리가 24% → 50% 흰색으로 밝아짐 | G02(비교 카드 4칸·칩) | G02 스냅샷. S01 의 `.hero-tile` 은 바꾸지 않았으므로 변화 없어야 한다 |
| 9 | overview 와 어긋남 | 전체 | `python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --check` |

QA 순서(CLAUDE.md 게이트 그대로)

```powershell
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --renumber   # D01–D07 추가 시
python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu
npx hyperframes check topics\sk-hynix-ai-agent-guide-edu                         # 겹침·넘침·글자 명암비
python scripts\deck\qa_rules.py topics\sk-hynix-ai-agent-guide-edu --rules topics\sk-hynix-ai-agent-guide-edu\deck-rules.json
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --check
```

- `hyperframes check` 는 글자 명암비만 본다. 테두리 3:1 은 이 문서 A-1·B-1 의 계산값이 근거다. 토큰 값을 바꾸면 표의 숫자를 다시 계산한다.
- 우선 스냅샷 대상(12장): G00 · G01 · L01 · S08 · G03 · S25 · A10 · S42 · T01 · G02 · D01 · D06.
