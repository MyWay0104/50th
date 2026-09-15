# final-touch 시각 보강 명세 (slide_ui_designer)

대상: `topics/sk-hynix-ai-agent-guide-edu/index.html` 57장 · 기준 스크린샷 `shots3/slide-01…57.png`
적용 단위: `_workspace/final_touch/visual_spec.jsonl` (142줄, 장면 51곳) + 아래 CSS 블록 1개(`#scene-styles` 맨 끝에 붙임) + CSS만으로 처리하는 장면 4곳(S05·A01·A10·G00 일부)

## 1. 적용 순서

1. 아래 CSS 블록 전체를 `index.html`의 `<style id="scene-styles">` 맨 끝(`.act-group { display: block; }` 다음)에 붙인다. `sync_overview.py`가 overview로 복사한다.
2. `visual_spec.jsonl`을 한 줄씩 적용한다. 각 줄의 `old`는 해당 `data-scene-id` 장면 안에서 정확히 한 번 나온다.
   - old에 들어간 기존 글자는 new에 그대로 있다(글자 변경 0).
   - 제목·출처·발표자 노트는 old에 넣지 않았다.
   - 시각이 곧 지워질 S41–S43 시간 블록은 old를 시각 **앞부분**까지만 잡았다. 예: `<div class="what" data-editable="true">목표·범위`. 시각이 지워지기 전과 후 모두 맞는다.
3. `python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --renumber` → `validate_topic.py` → `npx hyperframes lint`.

## 2. 새 CSS 블록

```css
/* ===== final-touch 시각 보강 (2026-09-17): 로고·아이콘·이미지 확대 =====
   색·크기는 :root 토큰만 참조. 로고는 정사각 원본이라 가로=세로로만 지정(비율·색 변형 없음). */

/* 로고 */
.logo { display: block; flex-shrink: 0; width: 48px; height: 48px; object-fit: contain; }
.logo-inline { display: inline-block; flex-shrink: 0; width: 32px; height: 32px; object-fit: contain; vertical-align: middle; }
.logo-row { display: flex; align-items: center; gap: 24px; }
.compare-heading > .logo-inline { width: 40px; height: 40px; margin-right: 14px; vertical-align: -6px; }
.dg-row > .logo-inline, .dg-row > .row-icon, .chip-row > .row-icon { align-self: center; }

/* 아이콘 공통 (Lucide 선 아이콘, 원본 짙은 회색) */
.dg-icon { display: block; width: 40px; height: 40px; margin: 0 auto 12px; object-fit: contain; }
.head-icon { display: block; flex-shrink: 0; width: 40px; height: 40px; object-fit: contain; }
.row-icon { flex-shrink: 0; width: 36px; height: 36px; object-fit: contain; }
.inline-icon { display: inline-block; width: 32px; height: 32px; margin-right: 12px; vertical-align: -6px; object-fit: contain; }

/* 단계 아이콘: 세로 시간표(G01)는 번호 원 옆, 가로 카드(S04·S16·S28·A05)는 오른쪽 위 */
.step-icon { flex-shrink: 0; width: 40px; height: 40px; object-fit: contain; }
.steps.row .step-icon { position: absolute; top: 48px; right: 36px; width: 56px; height: 56px; }
.steps.row.is-compact .step-icon { top: 24px; width: 40px; height: 40px; }

/* 비교 카드 머리 아이콘: 오른쪽 위 고정, 높이 증가 없음 */
.compare-col:has(.col-icon), .compare-col:has(.col-icons) { position: relative; }
.col-icon { position: absolute; top: 36px; right: 36px; width: 40px; height: 40px; object-fit: contain; }
.col-icons { position: absolute; top: 36px; right: 36px; display: flex; gap: 12px; }
.compare-grid.cols-4 .col-icon { top: 28px; right: 24px; }

/* 점선 구역 머리 아이콘: 구역 라벨 줄 오른쪽 */
.zone-icon { position: absolute; top: 12px; right: 20px; width: 32px; height: 32px; object-fit: contain; }

/* 코드 카드 제목줄 오른쪽 로고 (제목 없는 카드는 첫 줄 오른쪽 빈 곳) */
.code-card.has-logos, .code-card:has(> .code-logos) { position: relative; }
.code-logos { position: absolute; top: 17px; right: 28px; display: flex; gap: 16px; }

/* 패널 모서리 로고 (S21·S34) */
.split-panel:has(> .corner-logos) { position: relative; }
.corner-logos { position: absolute; top: 40px; right: 40px; display: flex; gap: 16px; }

/* 인용 장면 모서리 원형 배지 (S44) */
.corner-art { position: absolute; top: 96px; right: 120px; display: flex; align-items: center; justify-content: center; width: 128px; height: 128px; border: 1px solid var(--hairline); border-radius: 50%; background: var(--surface); }
.corner-icon { width: 56px; height: 56px; object-fit: contain; }

/* 표지 아이콘 타일 (S01, 반전 장면) */
.hero-art { position: absolute; top: 50%; right: 120px; transform: translateY(-50%); display: grid; grid-template-columns: repeat(3, 144px); gap: 24px; }
.hero-tile { display: flex; align-items: center; justify-content: center; width: 144px; height: 144px; border: 1px solid var(--on-night-line); border-radius: var(--radius); }
.hero-tile.is-core { border-color: var(--on-night); background: var(--on-night); }
.hero-icon { width: 56px; height: 56px; object-fit: contain; filter: brightness(0) invert(1); opacity: 0.85; }
.hero-tile.is-core .hero-icon { width: 72px; height: 72px; filter: none; opacity: 1; }
.scene.night .col-icon { filter: brightness(0) invert(1); opacity: 0.85; }

/* 편집 상자 위 아이콘 줄: 상자·화살표와 같은 flex 구성이라 가운데가 맞는다 (S33·S34·S37·A06) */
.icon-track { gap: 20px; }
.icon-track > .track-cell { flex: 1; min-width: 0; display: flex; justify-content: center; }
.icon-track > .dg-arrow.is-ghost { visibility: hidden; }
/* 높이가 빠듯한 장면은 상자 왼쪽 안쪽에 겹쳐 올린다 (S36 줄 · S40 3×2 격자) */
.dg-row.has-overlay, .dg.has-overlay { position: relative; }
.icon-track.is-overlay, .icon-track.is-grid { position: absolute; inset: 0; pointer-events: none; }
.icon-track.is-overlay { display: flex; align-items: stretch; }
.icon-track.is-grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 1fr); gap: 24px 20px; }
.icon-track.is-overlay > .track-cell, .icon-track.is-grid > .track-cell { align-items: center; justify-content: flex-start; padding-left: 24px; }
.icon-track.is-overlay .head-icon, .icon-track.is-grid .head-icon { width: 32px; height: 32px; }

/* 문서 모양 도식: 제목만 남은 문서 vs 본문 있는 문서 (S11) */
.doc-pair { display: flex; gap: 24px; }
.doc-mock { flex: 1; display: flex; flex-direction: column; gap: 8px; min-height: 120px; padding: 16px 24px; border: 1px solid var(--hairline); border-radius: var(--radius); background: var(--surface); }
.doc-line { display: block; height: 10px; border-radius: 5px; background: var(--hairline); }
.doc-line.is-title { width: 60%; height: 14px; background: var(--ink-2); }
.doc-line.is-meta { width: 40%; background: var(--line-strong); }
.doc-line.is-short { width: 70%; }
.doc-gap { flex: 1; display: flex; align-items: center; justify-content: center; border: 2px dashed var(--line-strong); border-radius: var(--radius); }
.doc-gap > .status-dot { margin: 0; }

/* 실습 안내판 시간 블록 아이콘 (블록 오른쪽 위) */
.time-block:has(> .tb-icon) { position: relative; }
.tb-icon { position: absolute; top: 28px; right: 20px; width: 36px; height: 36px; object-fit: contain; }
.time-blocks.row .tb-icon { right: 12px; width: 32px; height: 32px; }

/* 실습 안내판: 시간 → 번호 단계 (오케스트레이터가 .time-blocks에 is-steps, .min에는 순서 번호만) */
.time-blocks.is-steps { column-gap: 28px; }
.time-blocks.is-steps .time-block { position: relative; gap: 12px; padding: 20px 24px; }
.time-blocks.is-steps.row .time-block { padding: 20px 12px; }
.time-blocks.is-steps .min { display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); font-size: var(--fs-small); letter-spacing: 0; }
.time-blocks.is-steps .time-block.is-accent .min { background: var(--accent); color: var(--on-accent); }
.time-blocks.is-steps.row .time-block + .time-block::before,
.time-blocks.is-steps.cols-3 .time-block + .time-block::before,
.time-blocks.is-steps:not(.row):not(.cols-3) .time-block:nth-child(even)::before {
  content: "→"; position: absolute; left: -24px; top: 50%; transform: translateY(-50%);
  font-size: var(--fs-small); color: var(--ink-3);
}
/* 진행 띠(S41–S43): 시각을 지운 칩 앞에 순서 번호 원 */
.time-band { counter-reset: tb; }
.time-band > .chip { counter-increment: tb; }
.time-band > .chip::before { content: counter(tb); display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; margin-right: 10px; border-radius: 50%; background: var(--canvas); color: var(--ink-3); font-size: var(--fs-caption); font-weight: 700; }
.time-band > .chip.accent::before { background: var(--accent); color: var(--on-accent); }

/* 이미지 확대 */
.split-image.is-thumb { gap: 24px; align-items: flex-end; }
.split-image.is-thumb > img:first-child { width: auto; }
.split-image.is-thumb > .logo { width: 48px; height: 48px; }
[data-scene-id="G00"] .split-image.h-sm { height: 340px; }
[data-scene-id="G00"] .split-image.is-left + .dg-caption { max-width: none; }
[data-scene-id="S05"] .split-image.h-lg { height: 380px; }
[data-scene-id="A01"] .split-panel { padding: 24px; gap: 12px; }
[data-scene-id="A01"] .split-image.h-sm { height: 360px; }
[data-scene-id="A10"] > .split-grid { grid-template-columns: 600px 1fr; gap: 48px; }
[data-scene-id="A10"] .dg-row { gap: 12px; }
[data-scene-id="A10"] .dg-box { padding-left: 16px; padding-right: 16px; }
[data-scene-id="A10"] .dg > .dg-arrow.is-end { margin-right: 68px; }
```

## 3. 이미지 확대 값

| 장면 | 전 | 후 | 방법 · 높이 근거 |
|---|---|---|---|
| G00 썸네일 | 498×280 | 604×340 (+21%) | 칸을 `wide-left`로 넓힘(913px). 캡션 max-width를 풀어 3줄→2줄(−33px). 결과 +27px, 콘텐츠 끝 약 y 832 |
| S05 원 논문 Figure 1 | 230×340 | 257×380 (+12%) | 높이만 늘림. 캡션 끝 약 y 864. 400px이면 y 884로 여유가 없어 380으로 멈춤 |
| A01 Figure 2 두 장 | 높이 280 | 높이 360 (+29%) | 패널 안쪽 여백 40→24px, 간격 24→12px로 80px를 확보. 패널 끝 약 y 859 |
| A10 승인 카드 | 913×250 | 1032×283 (+13%) | 왼쪽 도식 칸을 600px로 고정하고 간격 64→48. 도식 상자 좌우 여백 24→16, 줄 간격 20→12. 상자 폭 165px ≥ "도구 호출" 글자 폭 120+32. 왼쪽 캡션이 2줄이 되어 끝 약 y 839 |

모든 장면이 출처 줄(글자 윗선 약 y 918, padding 24 포함 약 y 894) 위에서 끝난다.

## 4. 장면별 요약

| 쪽 | 장면 | 넣은 요소 | 이미지/인포그래픽 |
|---|---|---|---|
| 1 | S01 | 오른쪽 3×3 아이콘 타일(가운데 bot 흰 타일, 반전 배경용 흰 아이콘) | ✓ |
| 2 | G01 | 7구간 아이콘(brain·file-search·database·list-ordered·wrench·book-open·rocket) | ✓ |
| 3 | G00 | 썸네일 340px + YouTube 로고 | ✓ |
| 4 | S02 | 카드 머리 search·monitor + Obsidian 로고 | ✓ |
| 5 | S03 | 흐름 상자 link·list-ordered·network | ✓ |
| 6 | S04 | 단계 카드 split·calculator·repeat | ✓ |
| 7 | S05 | Figure 1 380px (CSS만) | ✓ |
| 8 | S06 | Python·vLLM 로고(도식), LangChain·OpenAI 로고(코드 제목줄) | ✓ |
| 9 | S07 | thermometer×2·clipboard-check (+기존 막대 분포) | ✓ |
| 10 | S08 | 단계 아이콘 play·repeat·globe·clipboard-check | ✓ |
| 11 | S09 | bot·file-text | ✓ |
| 12 | S10 | 구역 database·search, 조각 띠 앞 file-text | ✓ |
| 13 | S11 | 표 아래 CSS 문서 도식(본문 빈 문서/본문 있는 문서) | ✓ |
| 14 | S12 | 코드 카드 OpenAI·LangChain 로고 | ✓ |
| 15 | S13 | file-text·search·message-square·circle-help | ✓ |
| 16 | S14 | file-search·wrench | ✓ |
| 17 | S15 | bot / database+Python 로고 | ✓ |
| 18 | S16 | 행위자 code·bot 교대 + LangChain·Python 로고 | ✓ |
| 19 | S17 | terminal·workflow·bot | ✓ |
| 20 | S18 | GitHub 로고(공개 README) + 기존 흐름도 | ✓ |
| 21 | S19 | table·database·pencil·message-square | ✓ |
| 22 | S20 | Streamlit 로고 줄 | ✓ |
| 23 | S21 | 패널 모서리 Streamlit 로고, layers·wrench | ✓ |
| 24 | S22 | Claude 로고(제목), monitor | ✓ |
| 25 | S23 | 구역 monitor·server, lock | ✓ |
| 26 | S24 | 구역 pencil, database | ✓ |
| 27 | S25 | 요청 줄 message-square (+기존 6칸 양식) | ✓ |
| 28 | S26 | Claude 로고·folder·file-search | ✓ |
| 29 | S27 | file-text·play·notebook-pen, hand | ✓ |
| 30 | S28 | search·notebook-pen·code·clipboard-check | ✓ |
| 31 | S29 | Streamlit·Python 로고 | ✓ |
| 32 | S30 | Claude 로고(CLAUDE.md), notebook-pen | ✓ |
| 33 | S31 | Git 로고(바뀐 줄 비교) | ✓ |
| 34 | S32 | hand(승인 카드), search·notebook-pen·code·clipboard-check | ✓ |
| 35 | S33 | 아이콘 줄 brain·play·message-square | ✓ |
| 36 | S34 | 모서리 Obsidian 로고, 아이콘 줄 file-text·pencil·book-open | ✓ |
| 37 | S35 | bot·user | ✓ |
| 38 | S36 | 겹침 아이콘 file-text·link·users·workflow / list-ordered·file-search·play, Claude 로고 | ✓ |
| 39 | S37 | 아이콘 줄 file-text·Claude 로고·Obsidian 로고, 단계 아이콘 4 | ✓ |
| 40 | S38 | file-search·circle-help·user | ✓ |
| 41 | S39 | table·book-open·wrench | ✓ |
| 42 | S40 | 6칸 겹침 격자 rocket·folder·file-text·boxes·lock·list-checks | ✓ |
| 43 | S41 | notebook-pen·search + 진행 띠 번호 | ✓ |
| 44 | S42 | play·pencil·hand + 진행 띠 번호 | ✓ |
| 45 | S43 | clipboard-check·notebook-pen + 진행 띠 번호 | ✓ |
| 46 | S44 | 모서리 원형 배지 presentation | ✓ |
| 47 | G02 | message-square·split·notebook-pen·shield-check(흰색) | ✓ |
| 48 | A01 | Figure 2 두 장 360px (CSS만) | ✓ |
| 49 | A02 | split·search·table | ✓ |
| 50 | A03 | LangChain 로고·network·boxes | ✓ |
| 51 | A04 | link·users·workflow | ✓ |
| 52 | A05 | server·boxes·cpu·folder | ✓ |
| 53 | A06 | 아이콘 줄 lock·table·list-checks·workflow·git-compare | ✓ |
| 54 | A07 | 구역 database, 코드 network+Python 로고 | ✓ |
| 55 | A08 | LangChain·Python 로고 (+기존 흐름도) | ✓ |
| 56 | A09 | 구역 layers·boxes, LangChain·Python 로고 | ✓ |
| 57 | A10 | 승인 카드 1032px (CSS만) | ✓ |

## 5. 판단 메모

- **편집 상자 안에는 넣지 않았다.** 흐름 상자 대부분은 상자 자체가 `data-editable`이다. 안에 img를 끼우면 편집 영역의 내용이 바뀌므로 대신 두 방식을 썼다.
  - 위에 같은 폭의 아이콘 줄(`.icon-track`)을 둔다. 보이지 않는 화살표로 칸 폭을 맞춘다.
  - 높이가 빠듯한 S36·S40은 상자 왼쪽 안쪽 여백에 겹쳐 올린다(`.is-overlay`·`.is-grid`).
- **높이가 늘지 않는 배치를 우선했다.** 비교 카드·단계 카드·시간 블록·구역·코드 카드의 아이콘은 모두 절대 위치다. 존댓말 전환으로 설명 문단이 한 줄 늘어도 버틴다.
- 높이가 늘어나는 곳과 늘어난 뒤 콘텐츠 끝 위치:

  | 장면 | 늘어난 높이 | 콘텐츠 끝 |
  |---|---|---|
  | S02 | +52 | y≈782 |
  | S03 | +52 | 세로 가운데 정렬 |
  | S06 | +52 | 왼쪽 도식, y≈812 |
  | S11 | +144 | y≈831 |
  | S20 | +72 | y≈855 |
  | S27 | +52 | 세로 가운데 정렬 |
  | S33 | +64 | y≈784 |
  | S34 | +64 | y≈795 |
  | S37 | +64 | y≈792 |
  | A06 | +64 | 세로 가운데 정렬 |

  가장 빠듯한 곳은 S20(y≈855)이다.
- **로고는 제품을 직접 가리킬 때만 넣었다.**
  - S32 승인 카드는 "실제 화면과 다름" 개념 예시라서 Claude 로고 대신 hand 아이콘을 썼다.
  - S39 지식 정리는 "Obsidian 없이도" 과제라서 로고를 넣지 않았다.
  - LangGraph·MCP는 로고가 없어 network·link 아이콘으로 대신했다.
  - SK hynix 로고는 쓰지 않았다.
- **반전 장면(S01·G02) 아이콘**은 `filter: brightness(0) invert(1)`로 흰색 선이 된다. 로고에는 필터를 쓰지 않는다.
- **실습 안내판 번호 단계**
  - 번호는 56px 주황 옅은 원에 담는다. 강조 블록은 주황 원에 흰 숫자다.
  - 블록 사이 간격은 28px로 넓히고 가운데에 → 를 둔다. 2열 배치는 같은 줄 안에서만 둔다.
  - 단계마다 오른쪽 위에 아이콘을 붙인다. 원(왼쪽)과 아이콘(오른쪽)이 같은 높이에 온다.
  - 가로 4칸(`row`)의 좌우 여백은 12px로 줄였다. "검색 결과 확인"(약 160px)이 한 줄로 남는다.
  - 진행 띠 칩 7개에는 CSS 카운터 번호 원을 붙인다. 시각을 지우면 칩마다 약 75px가 줄고 번호 원이 36px를 더하므로 한 줄에 들어간다.
- **애매한 곳**
  1. S21 오른쪽 "13:20 · 이 앱이…" 줄. 시각을 지울 수 있어 old에 글자를 넣지 않았다. 여는 태그 조각 `<div class="dg-row"><div class="dg-box" data-editable="true">`만 잡았다.
  2. S31 Git 로고. 세 확인 상자 줄 맨 앞에 두었다. 근거는 발표자 노트의 "Git diff"라서, 화면 글자로는 연결이 약하다.
  3. S44 인용 장면. 가운데 정렬을 흔들지 않으려고 모서리 배지 하나만 두었다. 시각 요소로는 가장 약하다.
  4. A10. 왼쪽 도식 칸을 600px로 고정해서 상자 글자 여유가 약 17px밖에 없다. 글꼴 폭이 달라지면 "사람 결정"이 두 줄이 될 수 있다. 확인이 필요하다.
  5. S26의 `callout`("수정은 14:20부터"), S27의 thesis·callout, S38의 callout("6분")은 시각 삭제 대상이라 건드리지 않았다.
