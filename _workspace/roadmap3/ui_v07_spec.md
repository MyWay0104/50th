# v0.7 배치 보정 사양 (T6 · slide_ui_designer · 2026-09-18)

- 대상: `topics/sk-hynix-ai-agent-guide-edu` 66장 (비유→전문용어 치환 적용 직후)
- 측정 근거: `_workspace/roadmap3/measure_v07.md` · `_workspace/roadmap3/measure_v07.json` (Playwright, 1920×1080)
- 산출 CSS: `_workspace/roadmap2/slide_ui/06_v07_fixes.css`
- `index.html` · `overview.html` 은 이 작업에서 고치지 않았다. 메인이 `apply_css_patch.py` 로 붙인다.

## 0. 한 줄 결론

**측정에서 드러난 문제는 4곳뿐이고, 모두 세로 높이를 1px도 늘리지 않고 고쳤다.** 나머지 61장은 조치 불필요다.
24px 미만 5곳은 전부 **v0.6 이전부터 있던 것**이고, 그 가운데 4곳은 v0.6 검수가 "다음 정리 때 올리자"고 남겨 둔 항목이라 이번에 올렸다(높이 증분 0).

## 1. 측정표를 읽을 때 먼저 알아야 할 것 (판정의 전제)

| 측정값 | 실제 의미 | 판정에 쓸 수 있나 |
|---|---|---|
| 하단 여백 **48px**(66장 중 65장) | `.deck-footer { position:absolute; bottom:48px }` 이다. 모든 장면이 같은 값일 수밖에 없다 | ❌ 본문의 세로 여유를 뜻하지 않는다 |
| 상단 여백 **100px**(57장) | `.scene`(padding-top 80) + `.scene-title`(margin-top 20) | ❌ 구조값이라 장면 차이를 못 본다 |
| 좌우 여백 **120/120** | `.scene`(padding 좌우 120) 에 닿는 요소가 있다는 뜻 | ⭕ 좌우 쏠림 1차 판정에는 쓸 수 있다 |
| `overflowY: []` | 넘친 요소가 없다 | ⭕ 다만 **여유가 얼마나 남았는지는 알 수 없다** |
| `tight`(붙음) 목록 | 상자 사이가 0px 인 곳 | ⭕ 단, `.source` 처럼 안쪽 padding 을 가진 상자는 화면 간격과 다르게 읽힌다(2-2 참고) |

**세로 여유를 재는 유일한 단서**는 `.source { margin-top: auto }` 다. 이 값이 0으로 풀린 장면(= `chip-row|source` 가 0px 으로 잡힌 T01)은 **본문이 아래 끝까지 꽉 찬 장면**이다. 그래서 이번 보정의 모든 규칙을 "높이 증감 0"으로 설계했다.

## 2. 장면별 CSS와 근거

### 2-1. G01 (steps · 2번째 장) — 제목과 칩 줄 0px → 24px

| 항목 | 값 |
|---|---|
| 측정 | `tight: scene-title|chip-row = 0px` |
| 원인 | `.scene-title` 에 margin-bottom 이 없고 `.chip-row` 에 margin-top 이 없다(공통 규칙) |
| 위험 | G01 은 흐름의 끝이 `.stack` 이라 남은 세로 여유를 측정으로 알 수 없다 → 24px 을 그냥 더하면 넘칠 수 있다 |

```css
.scene[data-scene-id="G01"] > .chip-row { margin-top: 24px; }
.scene[data-scene-id="G01"] .stack > .dg.is-sep { margin-top: 0; }
```

- **높이 증감 0.** `.dg.is-sep`(index.html 1117줄, G01 한 곳에서만 쓰는 여백 규칙)의 24px 을 제목 아래로 옮겼다.
- 내준 자리 검산: `.panel-title` 아래에는 `.stack` gap 24px + 띠 `margin-top: 108px` 이 남는다. 그 안에 "준비 · 01" 표시(`.axis-prep`, `bottom: calc(100% + 24px)`, 높이 약 60px → 띠 위로 84px)가 들어가고도 **48px** 이 남는다. 새로 붙는 곳이 생기지 않는다.
- 24px 을 고른 이유: DESIGN.md 의 8px 배수이고, 바로 아래 `.thesis`(margin-top 20px)보다 살짝 커서 "제목 → 칩 줄 → 요지" 순서로 읽힌다.

### 2-2. T01 (compare · 15번째 장) — 칩 줄과 출처 0px

| 항목 | 값 |
|---|---|
| 측정 | `tight: chip-row|source = 0px` |
| 사실 1 | `.source` 는 공통 규칙에 `padding-top: 24px` 이 있다 → **화면에 보이는 글자 사이 간격은 이미 24px** 이고, 이는 출처 줄이 있는 60여 장면 모두와 같은 기준값이다. 측정이 0으로 읽은 것은 상자(border-box) 기준이기 때문이다 |
| 사실 2 | `.source { margin-top: auto }` 가 **0으로 풀렸다** → 이 장면의 세로 여유는 0px 이다. 간격을 더하면 그대로 넘침이 된다 |

```css
.scene[data-scene-id="T01"] > .stack { margin-bottom: 24px; }
.scene[data-scene-id="T01"] > .source { padding-top: 0; }
```

- **높이 증감 0 · 화면 변화 0.** 같은 24px 을 상자 안쪽(padding)에서 상자 사이(margin)로 옮기기만 했다. `margin-top: auto` 는 그대로 두어 나중에 글이 줄면 출처가 아래에 남는 성질을 유지한다.
- 이렇게 한 이유: 이 장면은 진짜로 붙어 있는 것이 아니라 **상자 모델 때문에 붙어 보이는 것**이다. 여유가 0px 인 장면에 간격을 더하는 것은 "넘침 0" 기준과 정면으로 부딪힌다. 대신 측정과 화면이 같은 값(24px)을 말하게 만들어, 앞으로의 자동 검사에서도 같은 지적이 반복되지 않게 했다.
- 만약 검수자가 T01 에 **24px 보다 넓은** 간격을 원하면 CSS 로는 풀 수 없다. 글을 한 줄 줄이는 일(`compare-note` 또는 `compare-list` 한 항목)이 먼저이고, 그때 다시 측정해야 한다. → `llm-edu-designer` 몫으로 남긴다.

### 2-3. S23 · A07 · A09 — `.dg-zone-label` 22px → 24px

```css
.scene[data-scene-id="S23"] .dg-zone-label,
.scene[data-scene-id="A07"] .dg-zone-label,
.scene[data-scene-id="A09"] .dg-zone-label { font-size: 24px; }
```

**이 22px 이 어디서 왔는지 (요청하신 확인)**

| 후보 | 확인 결과 |
|---|---|
| v0.7 치환 때문인가 | **아니다.** `_workspace/roadmap3/backup_v0.6/index.html` 905·909줄에 같은 `font-size: 22px` 이 있고, 마크업(2992 · 3824 · 3901 · 3910줄)도 같다 |
| 01~05 의 장면 전용 축소인가 | **아니다.** 01~05 어디에도 `.dg-zone-label` 이 없다. 그 파일들의 축소 규칙(LAB01 칩 26px, LAB04 24px, N03 26px, T0x 34px 등)은 **24px 아래로 내린 곳이 하나도 없다** |
| 그럼 무엇인가 | `index.html` 905줄, **기본 컴포넌트 정의값**(v0.4 때부터의 값)이다. `00_global_css_patch.md` B-2 표가 "`.concept-badge`·`.dg-zone-label` 은 22px 로 DESIGN.md 최소 24px 아래다 … 다음 정리 때 24px 권장" 이라고 적어 두고 미뤘다. 쌍둥이인 `.concept-badge` 는 `04_review_fixes.css` 가 이미 24px 로 올렸고 **`.dg-zone-label` 만 남았다** |

→ **일부러 줄인 것이 아니라 남겨 둔 것**이므로 올린다. 올려도 안전하다는 근거:

- 세로 증분 **0**: 이 라벨은 `position: absolute` 라 흐름 높이에 기여하지 않는다.
- 세로 겹침 없음: `top: 14px` + 24px 한 줄(약 33px) = **47px** < 구역 `padding-top: 56px`. 안쪽 첫 줄과 닿지 않는다.
- 가로 한 줄 유지(가장 빡빡한 A07 기준): 라벨 「State · messages · category를 모든 노드가 공유」 = 라틴 21자(11.1em) + 한글 8자(8em) + 가운뎃점 2 + 공백 7 + 자간 1px×38자 → 24px 에서 **약 565px**.
  쓸 수 있는 폭 = 구역 864px(`split-grid` 1fr: (1800−64)/2 − 테두리) − 왼쪽 24 − 오른쪽 `.zone-icon` 자리 52 − 여유 8 = **780px**. 여유 215px(38%).
  S23 「내 PC」 약 85px, A09 「하네스 · 모델을 둘러싼 실행 틀」 약 340px · 「Deep Agents가 미리 묶은 것」 약 330px — 열 폭이 981px(`wide-left`)이라 더 여유롭다.
- 대비: 색은 `--ink-3`(캔버스 5.99:1) 그대로라 명암비 영향 없다.

### 2-4. A01 — 전치 기호 `<sup>` 23.3px → 24px

```css
.scene[data-scene-id="A01"] .bullets li .sub sup { font-size: 24px; }
```

- 출처: 덱 규칙이 아니라 **브라우저 기본값** `sup { font-size: smaller }`(0.833 × 부모 `--fs-small` 28px = 23.3px)다. v0.6 백업 3616줄에도 같은 마크업이 있어 v0.7 치환과 무관하다.
- 올려도 위첨자로 읽힌다: 부모 28px 대비 0.86배 + `vertical-align: super` 의 올림이 남는다(수식 `softmax(QK^T / √d) · V`).
- 넘침 없음: 글자 폭 +0.7px, 줄 상자 높이 +0.5px 수준. A01 은 `tight` 목록이 비어 있다 = `.source` 앞에 여유가 남아 있는 장면이다.
- 대안(채택 안 함): 수학 위첨자를 24px 규칙의 예외로 두는 것. 올리는 비용이 사실상 0이라 검증 기준을 그대로 통과시키는 쪽을 택했다.

## 3. 사용자 배치 기준 4가지 판정 (ROADMAP3 5-5절)

| # | 기준 | 측정 근거 | 판정 |
|---|---|---|---|
| ① | **텍스트가 한쪽으로 몰리지 않는다** | 좌우 여백 66장 중 **65장이 120/120 완전 대칭**. S44(인용)만 120/156(차 36px < 기준 40px) — `.quote-body`·`.explain` 의 줄 길이 때문이고 열 구조가 기운 것이 아니다. 좌우 차 40px 초과 **0장** | **통과 · 조치 불필요** |
| ② | **균형 잡힌 중앙 정렬** | 상자 안 내용의 상하좌우 가운데 정렬은 `00_global_css_patch.md` C절이 v0.6에서 전역 적용했고 이번에 바꾼 것이 없다. 장면 전체의 세로 무게 중심은 **이번 측정으로는 판정할 수 없다**(1절: 하단 48px 은 풋터, 상단 100px 은 제목이라 본문 여유가 안 잡힌다). 다만 "글을 지워 위로 쏠린 장면"이 있었다면 `.source { margin-top:auto }` 가 크게 벌어져 나타나는데, 붙음 목록에 T01 하나만 잡혔고 넘침이 0인 것으로 보아 본문이 여전히 아래까지 차 있다 | **CSS 조치 불필요 · 눈 검토로 이월**(T8 Playwright 66장) |
| ③ | **컴포넌트끼리 다닥다닥 붙지 않는다** | 0px 2곳(G01 · T01). G01 은 24px 확보(2-1), T01 은 화면 간격이 이미 24px 임을 확인하고 측정값을 화면과 일치시킴(2-2). 나머지 64장에 0px 없음 | **조치 완료** |
| ④ | **넘침·겹침 없다** | `overflowX 0 · overflowY 0 · outside 0`. 이번 CSS 의 세로 높이 증감 **0**, 가로 증감은 절대 위치 라벨 +43px(여유 215px 안) 뿐 | **통과 · 유지** |

## 4. 24px 미만 5곳 — 처리 결정 요약

| 장면 | 요소 | 값 | 출처 | 결정 | 넘침 위험 |
|---|---|---|---|---|---|
| S23 | `.dg-zone-label` 「내 PC」 | 22px | v0.4 기본 정의값 (v0.6 백업에 동일) | **24px 로 올림** | 없음(absolute · 폭 85px) |
| A07 | `.dg-zone-label` 「State · messages · category를 …」 | 22px | 〃 | **24px 로 올림** | 없음(약 565px < 780px) |
| A09 | `.dg-zone-label` 「하네스 · …」 | 22px | 〃 | **24px 로 올림** | 없음(약 340px < 900px) |
| A09 | `.dg-zone-label` 「Deep Agents가 …」 | 22px | 〃 | **24px 로 올림** | 없음 |
| A01 | `<sup>` 「T」 | 23.3px | 브라우저 기본 `font-size: smaller` | **24px 로 올림** | 없음(+0.7px) |

- **일부러 줄인 규칙 때문에 남은 것은 하나도 없었다.** 01~05 의 장면 전용 축소는 전부 24px 이상에서 멈춰 있다(LAB04 `.what` 24px, LAB04b `.code-body` 24px, S17 `.chip` 24px 등). 이번에 올린 5곳은 그 축소와 겹치지 않으므로 **되살아나는 넘침이 없다.**
- 글을 지워 생긴 여유를 글자 키우는 데 쓰지 않았다. 올린 것은 "24px 미만 없음" 기준을 채우기 위한 **바닥값 보정**이고, 본문 글자 크기는 한 곳도 키우지 않았다.

## 5. 기존 CSS(00~05)와의 충돌 점검

| 새 규칙 | 겹치는 기존 규칙 | 결과 |
|---|---|---|
| `[G01] > .chip-row { margin-top: 24px }` | `.scene.title-scene .chip-row { margin-top:40px }`(G01은 title-scene 아님) · `.compare-note + .chip-row { margin-top:16px }`(해당 없음) | 충돌 없음. 특이도 (0,3,0) + 맨 뒤 |
| `[G01] .stack > .dg.is-sep { margin-top:0 }` | `.stack > .dg.is-sep { margin-top:24px }`(index 1117줄, **G01 한 곳에서만 쓰임**) | 특이도 (0,5,0) 로 이김. 다른 장면 영향 0 |
| `[T01] > .stack { margin-bottom:24px }` · `> .source { padding-top:0 }` | `.source { margin-top:auto; padding-top:24px }` · `[T0x]` 전환 장면 규칙 6개(색·카드 padding·칩 줄) | 충돌 없음. `margin-top:auto` 유지 |
| `[S23·A07·A09] .dg-zone-label { font-size:24px }` | `.dg-zone-label { font-size:22px }`(index 905줄) · `.dg-zone.accent .dg-zone-label`(색만) | 특이도 (0,3,0) 로 이김. `.dg-zone-label` 은 덱 전체에 이 4개뿐이라 남는 22px 이 없다 |
| `[A01] .bullets li .sub sup { font-size:24px }` | 브라우저 기본값만 | 충돌 없음. `<sup>` 은 덱 전체에 이 1곳뿐 |

## 6. 적용과 검증

```powershell
# 1) 06 을 패치 구간에 포함해 다시 붙인다 (기존 인자 뒤에 추가)
python _workspace\roadmap2\apply_css_patch.py topics\sk-hynix-ai-agent-guide-edu\index.html `
  _workspace\roadmap2\slide_ui\00_global_css_patch.md `
  _workspace\roadmap2\slide_ui\01_conti_css_requests.css `
  _workspace\roadmap2\slide_ui\03_builder_requests.css `
  _workspace\roadmap2\slide_ui\04_review_fixes.css `
  _workspace\roadmap2\slide_ui\05_fix_pass.css `
  _workspace\roadmap2\slide_ui\06_v07_fixes.css

# 2) QA 게이트 (CLAUDE.md 순서 그대로)
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu
python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu
npx hyperframes check topics\sk-hynix-ai-agent-guide-edu
python scripts\deck\qa_rules.py topics\sk-hynix-ai-agent-guide-edu --rules topics\sk-hynix-ai-agent-guide-edu\deck-rules.json
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --check
```

**재측정으로 확인할 값**(같은 Playwright 스크립트를 다시 돌린다)

| 확인 항목 | 기대값 |
|---|---|
| 붙음 | **0** (G01 24px · T01 24px 으로 잡혀야 한다) |
| 24px 미만 | **0** |
| 가로넘침 · 세로넘침 · 장면밖 | **0 유지** (특히 G01 · T01 · A07) |
| G01 새 간격 | `panel-title|dg` 24px, 화면상 "준비" 표시까지 48px |

## 7. 남은 위험과 T8(눈 검토)로 넘기는 것

| # | 내용 | 등급 |
|---|---|---|
| 1 | **A07 라벨 폭은 계산값**(약 565px/780px)이다. 글꼴이 Paperlogy 대신 폴백으로 잡히면 폭이 달라질 수 있다 → 재측정에서 A07 `overflowX 0` 과 라벨이 한 줄인지 확인 | 중간 |
| 2 | **G01 은 세로 여유를 잴 수 없었다.** 높이 증감 0으로 설계했으므로 새 넘침은 없어야 하지만, 재측정에서 G01 `overflowY 0` 을 반드시 본다 | 중간 |
| 3 | **T01 은 여유 0px 장면**이다. 앞으로 이 장면에 한 글자라도 더하면 바로 넘친다. 문구 수정 금지 구간으로 표시해 둔다 | 중간 |
| 4 | **세로 무게 중심(기준 ②)은 기계로 못 본다.** T8 Playwright 66장 검토에서 "글을 지운 뒤 위로 쏠린 장면"이 있는지 눈으로 본다. 특히 치환으로 글자가 가장 많이 준 S22 · LAB05 · N03 | 중간 |
| 5 | ROADMAP3 9절 ④(G01 띠 부제 길이) · ⑤(LAB04 칩 줄 접힘) · ⑬(LAB05 캡션 복원)은 **이번 측정에서 문제로 잡히지 않았다**(세 장면 모두 넘침·붙음 0). 조치하지 않았다. 되살릴지는 문구 담당 판단 | 낮음 |
