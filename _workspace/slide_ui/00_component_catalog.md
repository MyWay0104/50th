# 컴포넌트 카탈로그 — AI Agent Guide 덱

기준 파일: `topics/sk-hynix-ai-agent-guide-edu/index.html`의 `<style id="scene-styles">`
이 문서에 없는 클래스는 쓰지 않는다. 새 클래스가 필요하면 오케스트레이터에게 요청한다.

## 1. 공통 규칙

- 인라인 `style` 속성과 hex 색상을 쓰지 않는다. 색은 토큰 클래스로만 표현한다.
- 화면에 보이는 텍스트 leaf 요소마다 `data-editable="true"`를 붙인다. 장식 요소(화살표, 규칙선)는 `aria-hidden="true"`.
- `<br>`을 쓰지 않는다. 줄바꿈은 요소 폭(`max-width`)과 자연 줄바꿈에 맡긴다.
- 장면 안에 `<section>`을 중첩하지 않는다. `sync_overview.py`가 장면을 `section`으로 찾기 때문이다.
- 애니메이션용 클래스·id·스크립트를 추가하지 않는다.

## 2. 레이아웃 예산 (1920×1080)

| 영역 | 크기 |
|---|---|
| 장면 안쪽 여백 | 상 80 · 좌우 120 · 하 128 (풋터 자리) |
| 사용 가능 폭 | 1680px |
| eyebrow + 제목 1줄 | 약 140px |
| 본문 영역 높이 | 약 620px (제목 1줄, 출처 1줄 기준) |
| 제목 2줄이면 | 본문 약 540px |

한글 한 글자 폭은 대략 글자 크기와 같다. 한 줄 글자 수 ≈ 폭 ÷ 글자 크기.

| 요소 | 크기 | 1680px 기준 한 줄 | 반폭(약 800px) 한 줄 |
|---|---|---|---|
| `.scene-title` | 72px | 약 22자 | — |
| `.bullets li` | 44px | 약 35자 | 약 17자 |
| `.split-grid .bullets li` | 40px | — | 약 18자 |
| `.compare-list li` (2열) | 32px | — | 약 22자 |
| `.compare-list li` (3열, 약 520px) | 32px | — | 약 14자 |
| `.callout` | 34px | 약 46자 | 약 21자 |
| `.source` | 24px | 약 68자 | — |

## 3. 장면 뼈대

```html
<section id="s-N" class="scene clip" data-skill="split" data-scene-id="S10" data-start="0" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">B2</span><span data-editable="true">외부 근거와 기사 RAG</span></div>
  <h2 class="scene-title" data-editable="true">RAG의 기본 구조</h2>
  <!-- 본문 컴포넌트 1개 (아래 4절) -->
  <p class="source" data-editable="true">출처: Lewis et al. 2020 · LangChain Retrieval 가이드</p>
  <aside class="speaker-note">발표자 노트 3–6문장</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">N / 52</div>
</section>
```

- `id`, `data-start`, `page-num` 숫자는 `sync_overview.py --renumber`가 다시 매기므로 임시값이어도 된다.
- 구간 첫 장면(S01, S09, S15, S22, S28, S34, S41)만 eyebrow에 `<span class="time-chip" data-editable="true">10:00–10:40</span>`을 추가한다.
- 부록은 `block-chip`에 `부록`, 제목 앞에 "부록 · "을 붙이지 않고 eyebrow에 표시한다.
- `.source`는 항상 본문 뒤, `.speaker-note` 앞에 둔다. 출처가 없으면 "근거: 사용자 제공 시간표·강의안"처럼 성격을 적는다.

## 4. 본문 컴포넌트

### 4-1. `title` — 표지·마무리

```html
<section ... class="scene clip title-scene night" data-skill="title" ...>
  <div class="eyebrow">…</div>
  <div class="hero-rule" aria-hidden="true"></div>
  <div class="hero-kicker" data-editable="true">SK hynix 사내 교육 · 하루 과정</div>
  <h1 class="hero-title" data-editable="true">AI Agent Guide</h1>
  <p class="hero-sub" data-editable="true">부제 한 줄</p>
  <div class="hero-meta"><span data-editable="true">[강사명]</span><span data-editable="true">[교육일]</span></div>
```

`night`는 S01·G02만. G02는 `title-bullets`에 `night`를 붙여 `.bullets`를 쓴다.

### 4-2. `title-bullets`

```html
<ul class="bullets">
  <li data-editable="true"><strong>강조어</strong> 설명 한 줄</li>
  <li data-editable="true">항목<span class="sub">보조 설명 한 줄</span></li>
</ul>
```

변형: `.bullets.two-col`(4개, 2열), `.bullets.compact`(38px). 4개 이하.

### 4-3. 실습 안내판 (`title-bullets` + 보조)

```html
<p class="board-meta" data-editable="true">09:24–09:40 · 16분 · 실습 가이드 1장</p>
<div class="practice-grid">
  <div>
    <ul class="bullets">…단계 3개…</ul>
    <div class="done-box"><div class="done-label" data-editable="true">완료 조건</div><div class="done-text" data-editable="true">바꾼 값과 관찰 결과를 한 문장으로 설명</div></div>
    <div class="fallback" data-editable="true"><strong>막히면</strong>준비된 출력으로 비교를 계속합니다</div>
  </div>
  <div class="time-blocks">
    <div class="time-block"><div class="min" data-editable="true">4<small>분</small></div><div class="what" data-editable="true">첫 호출</div></div>
    …
  </div>
</div>
```

`time-blocks` 변형: 기본 2열, `.row` 4열 한 줄, `.cols-3`. 강조할 칸은 `.time-block.is-accent`.

### 4-4. `split`

```html
<div class="split-grid">            <!-- 변형: .wide-left / .wide-right -->
  <div class="split-panel">          <!-- 시각 자료 쪽: dg, code-card, data-table, placeholder 중 하나 -->
    <span class="concept-badge" data-editable="true">개념 예시</span>
    …
  </div>
  <ul class="bullets">…해석 2–3개…</ul>
</div>
```

실제 이미지는 `<div class="split-image"><img src="assets/…" alt="…"></div>`.

### 4-5. `compare`

```html
<div class="compare-grid">           <!-- .cols-3 / .cols-4 -->
  <div class="compare-col">
    <div class="compare-kicker" data-editable="true">작은 라벨</div>
    <div class="compare-heading" data-editable="true">열 제목</div>
    <ul class="compare-list"><li data-editable="true">항목</li></ul>
    <p class="compare-note" data-editable="true">열 하단 메모(선택)</p>
  </div>
  <div class="compare-col is-accent">…권장·핵심 열 1개만…</div>
</div>
```

상태 점: `<span class="status-dot ok" aria-hidden="true"></span>` / `.warn`. 글자색으로 쓰지 않는다.

### 4-6. `steps`

```html
<ol class="steps">                   <!-- 세로 기본 / .row 가로 카드 3–4개 / .timeline 시간표 -->
  <li class="step">
    <div class="step-num" data-editable="true">1</div>
    <div class="step-body" data-editable="true">단계 이름<span class="step-desc">설명 한 줄</span></div>
  </li>
</ol>
```

`.timeline`은 `<div class="step-time" data-editable="true">09:00</div>`를 `step-num` 앞에 둔다. `.row`에서 강조 카드는 `.step.is-accent`.

### 4-7. `title-image`

```html
<section ... class="scene clip title-image" data-skill="title-image" ...>
  …eyebrow, scene-title, scene-subtitle…
  <div class="image-frame">
    <div class="placeholder"><div class="placeholder-label" data-editable="true">실제 화면 교체 예정</div><div class="placeholder-desc" data-editable="true">Streamlit 실습 앱: 입력·처리 중·결과 영역</div></div>
  </div>
```

### 4-8. `title-tags`

```html
<p class="scene-subtitle" data-editable="true">보조 설명</p>
<div class="tags"><span class="tag" data-editable="true">태그</span><span class="tag accent" data-editable="true">강조 1개</span></div>
```

### 4-9. `quote`

```html
<section ... class="scene clip quote" data-skill="quote" ...>
  <div class="eyebrow">…</div>
  <div class="quote-mark" aria-hidden="true">“</div>
  <p class="quote-body" data-editable="true">핵심 문장 <em>강조</em></p>
  <p class="quote-attrib" data-editable="true">— 출처(선택)</p>
  <ol class="quote-points"><li data-editable="true">질문 1</li></ol>   <!-- 선택, 3개 이하 -->
```

### 4-10. `stat`, `evolution-flow`

`.stats`(.cols-2/.cols-4) > `.stat`(.accent) > `.num` + `.label`. 근거 있는 수치만 쓴다.
`.flow` > `.flow-col` + `.flow-arrow`(aria-hidden) + `.flow-col.after`, 안에 `.flow-label` `.flow-heading` `.flow-list`.

## 5. 보조 요소

| 클래스 | 용도 |
|---|---|
| `.scene-subtitle` | 제목 아래 보조 문장 1줄 |
| `.callout` (+`strong`) | 핵심 한 줄 강조, 파랑 틴트 배경 |
| `.chip`, `.chip.accent`, `.chip-row` | 토큰·파일명·값 같은 작은 상자 |
| `.concept-badge` | "개념 예시", "개인 기록", "공개 Beta 설계 기반 개념 예시" |
| `.placeholder` > `.placeholder-label` + `.placeholder-desc` | 실제 화면 교체 자리 |
| `.panel-title` | split-panel 안의 작은 제목 |
| `.guide-ref` | 실습 가이드 장 이름 안내 |
| `.code-card` > `.code-title` + `pre.code-body` (`.hl`, `.cm`) | 코드 5–7줄 |
| `.data-table` (`td.is-match`, `tr.is-dim`) | 가상 데이터 3–5행 |
| `.dg` > `.dg-row`(.stretch) > `.dg-box`(.accent/.muted) + `.dg-arrow` | 개념도 상자와 화살표 |
| `.dg-sub` | 상자 안 보조 설명 |
| `.dg-zone`(.accent) > `.dg-zone-label` | 점선 영역(예: "모델 영역", "프로그램 영역") |
| `.dg-caption`, `.dg-caption.is-left` | 개념도 하단 캡션 (기본 가운데, `is-left` 왼쪽) |
| `.stack` | 세로 쌓기 래퍼(gap 24px). callout·done-box·code-card·chip-row를 그리드 뒤나 칸 안에서 간격 두고 쌓을 때. UI 문서의 "스택 `.dg` 래퍼" 지시는 `.stack`으로 쓴다 |

| `.done-row` > `.done-box` + `.fallback` | 완료 조건과 막히면 상자를 가로 2칸으로 나란히(최대 1400px, 위 간격 24px, 두 상자 윗변 정렬). `title-image` 실습 안내판용 |

| `.split-grid.fill`, `.compare-grid.fill` | 격자가 남은 높이를 모두 채움. 기본은 가장 긴 칸 높이에 맞춰 카드 속이 비지 않는다. 점선 자리표시처럼 큰 면이 필요할 때만 `.fill` |

추가 규칙 (2026-09-14, 부록 UI 담당 요청 반영):
- `.dg-row.stretch` 안의 `.dg-arrow`는 CSS가 세로 가운데로 정렬한다. 높이를 맞춘 상자 줄에서 화살표가 위에 붙지 않는다.
- `night` 장면(G02) 안의 `.bullets li .sub`는 CSS가 흰색 계열(`--on-night-2`)로 바꾼다. 보조 줄을 그대로 써도 된다.

추가 규칙 (2026-09-14, 오전 빌드 검수 반영):
- `split-grid`·`compare-grid`는 기본적으로 남은 높이를 채우지 않는다. 오전 검수에서 카드가 화면 아래까지 늘어나 속이 비어 보였기 때문이다.
- 코드 줄은 42자 이하로 쓴다. 브라우저와 HyperFrames 렌더러의 고정폭 글꼴 폭이 달라 한쪽에서만 잘릴 수 있다.

추가 규칙 (2026-09-14, UI 담당 요청 반영):
- `title-scene`·`quote` 장면의 `.source`는 CSS가 하단 좌측에 고정한다. S01에도 출처 줄을 넣어도 가운데 정렬이 깨지지 않는다.
- `title-image` 장면에서 `.image-frame` 뒤 `.done-box`는 CSS가 위 간격 24px을 준다.

`dg-arrow` 문자는 `→`, `↓`, `⇄`만 쓴다.

## 6. 금지 예시

| 하지 말 것 | 대신 |
|---|---|
| `<div style="color:#0075de">` | `<strong>` 또는 `.chip.accent` |
| 카탈로그에 없는 `.card`, `.box`, `.grid-3` | `.compare-col`, `.split-panel`, `.compare-grid.cols-3` |
| 가짜 앱 화면을 CSS로 그림 | `.placeholder` + 설명 |
| `<br>`으로 줄 맞춤 | 문구 축소 또는 `max-width` 조정 요청 |
| 사내 URL·모델명·키 | "사내 추론 서버", "승인된 모델 경로" |
