# APP 배치 지시 · 부록 · 질문 대응·후속 학습

작성: slide_ui_designer · 2026-09-14 · 대상: A01–A06 (6장, HTML 순번 s-47–s-52)
입력: `_workspace/slide_copy/APP.md`, `00_component_catalog.md`(5절 추가 규칙 2묶음 포함), `index.html` `<style id="scene-styles">` 실측값, topic `DESIGN.md` 최소 적용 규칙, `lecture_review/B1-B3-post.md`, `hyperframes-slide-work-{split,compare,steps,title-bullets}` 스킬
형식 기준: `slide_ui/B1.md`–`B3.md`

## 공통 배치 규칙 (요약 — 원문은 `slide_ui/B1.md` 공통 절)

- 장면 내부 872×1680px. eyebrow+제목 1줄 145, 부제 64, 출처 58, 본문 margin-top 56. 본문 가용 높이: 제목+출처 **613px**, 부제 추가 시 **549px**. callout 1줄 104px.
- 글자 폭 추정: 한글 1.0em, 라틴·숫자 0.55em, 공백·기호 0.3em. 행 높이 = 글자 크기 × line-height(본문 1.4, dg-box 1.3, step-body 1.35, heading 1.25).
- 오전 빌드 뒤 CSS 사실(이 문서의 계산에 반영함)
  - `.split-grid`·`.compare-grid`는 가장 긴 칸 높이에 맞춘다. 남은 높이를 채우지 않는다. 부록 6장은 점선 자리표시가 없으므로 `.fill`을 **쓰지 않는다**.
  - `.scene > .stack`은 위 간격 56px을 받는다. `.stack` 직계 자식은 위 여백 0이다. 따라서 스택 안의 `.compare-grid`·`.steps` margin-top은 0이고, 제목(또는 부제)과 첫 카드 사이는 56px이다. 아래 높이 계산은 모두 이 기준이다(오전 C1 결함 재발 없음).
  - 코드 카드는 부록에서 쓰지 않는다(문구 확정본에 코드 없음).
- 부록 eyebrow(6장 공통, 시각 칩 없음):
  ```html
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  ```
  제목 앞에 "부록 · "을 붙이지 않는다. `.time-chip`을 넣지 않는다. `night` 클래스는 쓰지 않는다(6장 모두 오프화이트).
- 풋터 `.deck-footer`: AI Agent Guide · SK hynix 사내 교육 / `.page-num`: 임시값 "N / 52"(`sync_overview.py --renumber`가 다시 매김).
- 장면 `id`는 순번 `s-47`–`s-52`, `data-scene-id`는 `A01`–`A06`. 기획 ID를 재번호하지 않는다.
- compare 열 내부 순서(B1 S07·B3 S17과 같음): `.compare-kicker` → `.compare-heading` → `ul.compare-list` → `p.compare-note`.
- 스플릿 패널 머리줄: 배지와 패널 제목이 둘 다 있으면 `.dg-row` 한 줄(S05·S11·S18과 같음).
- `strong` 뒤에는 공백 1칸을 둔다(`.callout strong`, `.bullets li strong`에는 margin이 없다).
- 글자 크기 세기: eyebrow·출처·풋터(24px 크롬)와 22–24px 라벨(배지·kicker·dg-sub·캡션·note)은 빼고 센다. 장면당 4종 이하.

### 같은 유형 대조 (오전 장면과 일관성)

| 부록 장면 | 따르는 오전 장면 | 같은 점 |
|---|---|---|
| A01 split | S18·S21 (`.wide-left`) · S05(머리줄) | 좌 흰 패널 개념도 + 우 해석 bullets, 캡션으로 성격 표시 |
| A02 compare | S17 구조 + S07 강조 열 | `.stack`[`cols-3` → callout], 강조 열 1개 |
| A03·A04 compare | S17 | 부제 + `.stack`[`cols-3` → callout], 강조 열 없음, 열 사이 화살표 없음 |
| A05 steps | S16 | `.stack`[`ol.steps.row` 4카드 → callout] |
| A06 title-bullets | (오전에 같은 형태 없음) | 기본 `.bullets` 1열, 강조어 + 보조 1줄 |

---

## A01 · Transformer와 Q·K·V

- data-skill: `split` · section 클래스: `scene clip`
- 변형: **`.split-grid.wide-left`**(좌 913 · 우 703px). 이유: 1fr 1fr(패널 안쪽 726px)이면 1행 상자 안쪽이 101px, 2행 상자 안쪽이 139px로 줄어 보조 설명이 모두 2줄이 되고 강조 상자 "문맥 반영 표현"이 3줄 위험. 좌 패널 624px > 613px로 넘친다(아래 계산).
- 배치 순서: eyebrow → `h2.scene-title` → `.split-grid.wide-left` [좌 `.split-panel` / 우 `ul.bullets`] → `.source`
  - 좌 `.split-panel`(세로 gap 24px):
    1. 머리줄 `.dg-row` [ `span.concept-badge` "개념 예시" + `div.panel-title` "한 위치의 표현이 만들어지는 과정" ]
    2. `.dg`
       - 1행 `.dg-row.stretch`: `.dg-box` "토큰 표현" · `div.dg-arrow` "→" · `.dg-box` "Q" + `.dg-sub` "찾는 기준" · `.dg-box` "K" + `.dg-sub` "비교될 이름표" · `.dg-box` "V" + `.dg-sub` "전달할 내용" (Q·K·V 사이에는 화살표 없음. 세 상자는 나란한 재료)
       - 2행 `.dg-row.stretch`: `.dg-box` "Q·K 비교" + `.dg-sub` "반영 비율 계산" · `div.dg-arrow` "→" · `.dg-box` "V 합산" + `.dg-sub` "비율대로 섞기" · `div.dg-arrow` "→" · `.dg-box.accent` "문맥 반영 표현"
    3. 식 줄 `.dg-row` [ `span.chip` "softmax(QK^T / √d) · V" + `span.dg-caption` "원 논문 식 · 전개 생략" ] (보류 1: 빼기로 하면 이 줄 전체 삭제)
    4. `p.dg-caption` "비유를 쓴 개념도 · 가중치 수치·열지도 아님"
  - 우 `ul.bullets`(3개)
- 마크업 예(상자 1개, S21과 같은 방식):
  ```html
  <div class="dg-box" data-editable="true">Q<span class="dg-sub">찾는 기준</span></div>
  ```
- 요소 ↔ 문구
  - 제목: Transformer와 Q·K·V
  - `.bullets li` 1: Q·K 비교로 반영 비율 계산
  - `li` 2: 비율대로 V를 모아 새 표현
  - `li` 3: 원 논문은 encoder–decoder + `span.sub` "많은 생성 모델은 decoder 중심"
  - `.source`: 출처: Vaswani et al., Attention Is All You Need (2017)
- 강조: `.dg-box.accent` "문맥 반영 표현" 1개. bullets에 strong 없음. 식 칩은 기본 `.chip`(파랑 아님). Q·K·V 세 상자는 같은 색·같은 폭·같은 높이(`.stretch`)로 셋 중 하나가 강조되지 않게 한다.
- 글자 크기: 72 / 40 / 32 / 28 (4종 — 28은 panel-title·chip·li .sub, dg-sub·캡션 24와 배지 22는 라벨)
- 넘침 근거
  - 폭(머리줄): 배지 약 125 + 20 + 패널 제목 한글 14×28 + 공백 4×8 ≈ 426 → 571px < 패널 안쪽 831px → 1줄
  - 폭(1행): 상자 4개 + 화살표 1개 → (831 − 40 − 4×20)/4 = 178, 안쪽 128px. "토큰 표현" 한글 4×32 + 공백 ≈ 138px → 2줄(허용). 보조 "찾는 기준" ≈ 103px 1줄 / "비교될 이름표" ≈ 151px 2줄 / "전달할 내용" ≈ 127px 1–2줄(경계). `.stretch`로 네 상자 높이가 같아지므로 줄 수 차이는 보이지 않는다
  - 폭(2행): 상자 3개 + 화살표 2개 → (831 − 80 − 80)/3 = 224, 안쪽 174px. "Q·K 비교" ≈ 119px 1줄, "V 합산" 1줄, "문맥 반영 표현" ≈ 212px → 2줄("문맥 반영" / "표현"). 보조 "반영 비율 계산" ≈ 158px, "비율대로 섞기" ≈ 151px → 1줄(여유 16–23px)
  - 폭(식 줄): 칩 약 360 + 20 + 라벨 약 200 = 580px < 831px → 1줄
  - 폭(우): bullets 703 − 52 = 651px. 최장 li 3 "원 논문은 encoder–decoder" ≈ 한글 4×40 + 라틴 15×22 + 공백 2×12 ≈ 514px → 1줄. li 2 ≈ 470px, li 1 ≈ 464px → 1줄. sub ≈ 364px → 1줄
  - 높이(좌): 패널 패딩·테두리 82 + 머리줄 41 + 24 + 1행 157(40 + 2 + 42 + 6 + 보조 2줄 67) + 24 + 2행 127(강조 상자 2줄 83 + 44) + 24 + 식 줄 57 + 24 + 캡션 34 = **594px ≤ 613** (여유 19px, **주의**)
  - 높이(우): 3×56 + sub 45 + 2×28 = 269px
  - 1fr 1fr였다면: 1행 157 + 2행 157–168(보조 2줄, 강조 상자 3줄 위험) → 624–635px > 613px → 넘침
- 플레이스홀더: 없음 (CSS 개념도로 완성)
- 위험: 2행 보조("반영 비율 계산")가 2줄로 접히면 2행이 157px가 되어 좌 패널 624px로 넘친다. 스냅샷에서 캡션 아랫변이 출처 윗선 위에 있는지 확인하고, 넘치면 **식 줄을 먼저 뺀다**(−81px → 513px). 문구 담당 제작 메모와 같은 순서다.
- 빌드 메모: 가중치 숫자·색 농도·열지도를 넣지 않는다. 1·2행 사이에 세로 화살표를 넣지 않는다(높이 여유 없음, 읽는 순서는 좌→우·위→아래로 충분). 식 칩의 `^`·`√`는 ASCII/기호 그대로 두고 위첨자 태그를 쓰지 않는다. `.dg-row.stretch` 안의 화살표 세로 정렬은 카탈로그 추가 요청 A1 참고.

## A02 · RAG 검색 방식과 메타데이터

- data-skill: `compare` · section 클래스: `scene clip`
- 배치 순서: eyebrow → `h2.scene-title` → `.stack` [ `.compare-grid.cols-3` [열1 · 열2 · 열3 `.compare-col.is-accent`] → `.callout` ] → `.source`
- 요소 ↔ 문구
  - 제목: RAG 검색 방식과 메타데이터
  - 열1: kicker "미리 준비" / heading "청킹·임베딩" / li: 찾기 좋은 단위로 분할 · 조각을 벡터로 변환 / note: 임베딩 지원 여부는 환경별 확인
  - 열2: kicker "질문할 때" / heading "벡터·키워드 검색" / li: 벡터: 뜻이 가까운 조각 · 키워드: 같은 단어 포함 / note: Vector DB는 선택 사항
  - 열3(`is-accent`): kicker "먼저 설계" / heading "메타데이터" / li: 출처·발행일·문서 버전 · 장비·제조사·적용 기간 / note: 답변에서 구분할 조건부터
  - `.callout`: `<strong>실패 나누기</strong>` + " 검색이 틀렸나, 찾은 근거로 잘못 답했나"
  - `.source`: 출처: Lewis et al. 2020 (Retrieval-Augmented Generation) · LangChain Retrieval 가이드 · Part Number Finder Beta 공개 README
- 강조: 열3 `.is-accent` + callout `strong` (2개). 상태 점 없음. 열 사이 화살표·번호 없음(역할 구분이지 순서가 아님).
- 글자 크기: 72 / 40 / 34 / 32 (4종, kicker·note 24는 캡션)
- 넘침 근거
  - 폭: 열 (1680 − 2×32)/3 = 539, 목록 가용 539 − 82 − 30 = 427px(강조 열 425px). 최장 "벡터: 뜻이 가까운 조각" ≈ 한글 9×32 + 기호·공백 4×10 = 328px → 1줄. 나머지 li 243–317px → 1줄. heading 최장 "벡터·키워드 검색" ≈ 304px < 457px → 1줄. note 최장 "임베딩 지원 여부는 환경별 확인" ≈ 341px < 457px → 1줄. callout ≈ 750 + 72px < 1680px → 1줄
  - 폭(출처): 라틴 약 100자 × 13 + 한글 5×24 ≈ 1,470px < 1,680px → 1줄(빠듯. 2줄이 되면 +34px, 여유 안에서 흡수)
  - 높이: 열 = 패딩·테두리 82 + kicker·heading 114 + 목록(24 + 2×45 + 18 = 132) + note 54 = 382px. 145 + 56 + 382 + 24 + 104 + 58 = **769px ≤ 872** (여유 103px)
- 플레이스홀더: 없음
- 빌드 메모: S17과 같은 마크업에서 열3에만 `is-accent`를 붙인다. note는 `margin-top:auto`로 세 열 바닥에 맞춰진다. 청크 크기·정확도 같은 수치를 넣지 않는다. 보류 2·3(임베딩 지원, 메타데이터 예시)으로 문구가 바뀌어도 li 14자 이내면 배치는 그대로다.

## A03 · 프레임워크 선택 기준

- data-skill: `compare` · section 클래스: `scene clip`
- 배치 순서: eyebrow → `h2.scene-title` → `p.scene-subtitle` → `.stack` [ `.compare-grid.cols-3` [열1 · 열2 · 열3, 모두 기본 `.compare-col`] → `.callout` ] → `.source` (S17과 같은 구조)
- 요소 ↔ 문구
  - 제목: 프레임워크 선택 기준
  - `.scene-subtitle`: 배우는 순서가 아니라 필요한 제어 수준으로
  - 열1: kicker "구성 요소 연결" / heading "LangChain" / li: 모델·도구를 공통 방식으로 · Agent를 짧게 구성 / note: 오전 실습에서 사용
  - 열2: kicker "흐름 직접 설계" / heading "LangGraph" / li: 단계·분기를 직접 정의 · 상태 저장·중단 후 재개 / note: LangChain Agent의 기반
  - 열3: kicker "기능 묶음" / heading "Deep Agents" / li: 계획·파일·하위 작업 내장 · 여러 단계의 긴 작업용 / note: LangGraph 기반 하네스
  - `.callout`: `<strong>고르는 기준</strong>` + " 코드 길이·성능 순위가 아니라 문제에 필요한 제어"
  - `.source`: 출처: LangChain Overview · LangGraph Overview · LangChain Concepts(Agent harnesses: Deep Agents)
- 강조: callout `strong` 1개. **`.is-accent` 열 없음**(학습 순서·성능 서열로 읽히지 않게). 열 사이 화살표·번호 없음. 세 열 kicker는 기본 `--ink-3`.
- 글자 크기: 72 / 40 / 34 / 32 (4종)
- 넘침 근거
  - 폭: 목록 427px. 최장 "모델·도구를 공통 방식으로" ≈ 한글 10×32 + 기호·공백 3×10 = 350px, "계획·파일·하위 작업 내장" ≈ 326px → 1줄. heading "Deep Agents" ≈ 230px → 1줄. note 최장 "LangChain Agent의 기반" ≈ 285px < 457px → 1줄. 부제 ≈ 595px < 1,500px → 1줄. callout ≈ 930 + 72px → 1줄
  - 높이: 열 382px. 145 + 64 + 56 + 382 + 24 + 104 + 58 = **833px ≤ 872** (여유 39px. S17 실측과 같은 구조로 화면 확인됨)
- 플레이스홀더: 없음
- 빌드 메모: 세 열을 같은 크기·같은 색으로 둔다. 코드 예시를 넣지 않는다. 열 순서(LangChain → LangGraph → Deep Agents)는 문구 순서 그대로지만 화살표가 없으므로 진화 단계로 읽히지 않는다.

## A04 · MCP·Subagent·Hook 역할

- data-skill: `compare` · section 클래스: `scene clip`
- 배치 순서: A03과 동일 — eyebrow → 제목 → `p.scene-subtitle` → `.stack` [ `.compare-grid.cols-3`(강조 열 없음) → `.callout` ] → `.source`
- 요소 ↔ 문구
  - 제목: MCP·Subagent·Hook 역할
  - `.scene-subtitle`: 상하위 단계가 아닌 서로 다른 역할 · 함께 쓸 수 있음
  - 열1: kicker "외부 연결" / heading "MCP" / li: 외부 시스템 도구를 연결 · 도구를 전하는 표준 규약 / note: 예: 승인된 문서·DB 읽기
  - 열2: kicker "작업 분담" / heading "Subagent" / li: 별도 맥락에서 하위 작업 · 결과를 주 대화로 반환 / note: 예: 예외 입력만 점검
  - 열3: kicker "이벤트 처리" / heading "Hook" / li: 정해진 시점에 자동 실행 · 기억이 아닌 설정으로 동작 / note: 예: 파일 수정 후 포맷
  - `.callout`: `<strong>설치·권한</strong>` + " 사내 가이드의 승인된 설정만 사용"
  - `.source`: 출처: Claude Code 문서 — Features overview · MCP · Subagents · Hooks
- 강조: callout `strong` 1개. `.is-accent` 열 없음. 위아래 배치·화살표·번호 없음(상하위 계층으로 그리지 않음).
- 글자 크기: 72 / 40 / 34 / 32 (4종)
- 넘침 근거
  - 폭: 목록 427px. 최장 "기억이 아닌 설정으로 동작" ≈ 한글 10×32 + 공백 3×10 = 350px → 1줄. 나머지 li 285–317px. heading "Subagent" ≈ 176px. note 최장 "예: 승인된 문서·DB 읽기" ≈ 270px → 1줄. 부제 ≈ 770px < 1,500px → 1줄. callout ≈ 680 + 72px → 1줄
  - 높이: A03과 같은 구조 **833px ≤ 872** (여유 39px)
- 플레이스홀더: 없음
- 빌드 메모: 설정 파일 예시·명령어·서버 주소를 넣지 않는다. 보류 5로 note가 "사내에서는 허용 여부 먼저 확인"(약 330px)으로 바뀌어도 1줄이다.

## A05 · 사내 실행 환경 문제 해결

- data-skill: `steps` · section 클래스: `scene clip`
- 변형: 문구의 "세로 4단계 기본형" 대신 **`ol.steps.row`(가로 카드 4개)**. 이유: 세로 기본형은 단계 1개 = 본문 패딩 10 + 이름 57 + 6 + 설명 39 = 112px → 4×112 + 3×28 = 532px, 여기에 callout(24 + 104)을 더하면 145 + 56 + 660 + 58 = **919px > 872px(47px 초과)**. callout을 빼면 들어가지만 이 장의 핵심 문장("한 번에 하나")이 사라진다. 가로 카드는 S16과 같은 구조라 오전과도 일관된다.
- 배치 순서: eyebrow → `h2.scene-title` → `.stack` [ `ol.steps.row`(4단계) → `.callout` ] → `.source`
- 카드 마크업(4개 같은 형태, `.panel-title` 라벨 없음):
  ```html
  <li class="step">
    <div class="step-num" data-editable="true">1</div>
    <div class="step-body" data-editable="true">접속<span class="step-desc">서버 응답·인증 오류인지 먼저 구분</span></div>
  </li>
  ```
- 요소 ↔ 문구
  - 제목: 사내 실행 환경 문제 해결
  - 카드1: 1 / 접속 / 서버 응답·인증 오류인지 먼저 구분
  - 카드2: 2 / 패키지 / 설치 판본을 실습 가이드와 비교
  - 카드3: 3 / 모델 기능 / 도구 호출·임베딩 지원 여부 확인
  - 카드4: 4 / 파일 경로 / 코드가 실행되는 위치 기준으로 확인
  - `.callout`: `<strong>한 번에 하나</strong>` + " 오류 원문을 남기고 한 가지만 바꿔 다시 실행"
  - `.source`: 출처: vLLM Online Serving 문서 · Claude Code 작동 원리 문서 · 근거: 사용자 제공 강의안
- 강조: callout `strong` 1개. `.step.is-accent` 없음(문구 지정 없음, 네 단계는 점검 순서일 뿐 중요도 차이 없음). step-num 파랑 원은 구조색.
- 글자 크기: 72 / 38 / 34 / 28 (4종, step-num 32는 원 안 라벨)
- 넘침 근거
  - 폭: 카드 (1680 − 3×64)/4 = 372, 안쪽 298px. 이름 최장 "모델 기능"·"파일 경로" ≈ 163px → 1줄. 설명(28px, 줄당 약 10자)
    - "서버 응답·인증 오류인지 먼저 구분" → "서버 응답·인증" / "오류인지 먼저 구분" 2줄
    - "설치 판본을 실습 가이드와 비교" → "설치 판본을 실습" / "가이드와 비교" 2줄
    - "도구 호출·임베딩 지원 여부 확인" → "도구 호출·임베딩 지원" / "여부 확인" 2줄
    - 최장 "코드가 실행되는 위치 기준으로 확인" ≈ 426px → "코드가 실행되는 위치" / "기준으로 확인" 2줄
  - callout ≈ 한글 23×34 + 공백·기호 ≈ 880 + 72px < 1,680px → 1줄
  - 높이: 카드 = 패딩 80 + 테두리 2 + 원 72 + 24 + 이름 51 + 6 + 설명 2줄 78 = 313px. 145 + 56 + 313 + 24 + 104 + 58 = **700px ≤ 872** (여유 172px)
- 플레이스홀더: 없음
- 빌드 메모: 카드 사이 "→"는 CSS가 자동으로 그린다(마크업에 넣지 않음). 사내 주소·모델명·계정·키·설치 명령·오류 메시지 예시를 넣지 않는다. 설명이 3줄이 되어도 +39px(739px)로 넘치지 않는다. 보류 6으로 "실습 가이드 해당 장" 안내를 붙이게 되면 `.guide-ref`를 `.stack` 마지막(callout 뒤)에 두어도 +57px(757px)로 들어간다.

## A06 · 현업 적용 전 확인 항목

- data-skill: `title-bullets` · section 클래스: `scene clip`
- 변형: 기본 `.bullets` **1열**. `.two-col`은 쓰지 않는다. 이유: 2열이면 칸 폭 (1560 − 72)/2 − 52 = 692px인데 최장 항목 "데이터 정의 날짜 기준·단위·결측값 의미" ≈ 826px라 2줄로 접힌다. 1열이면 모두 1줄이고 높이도 들어간다.
- 배치 순서: eyebrow → `h2.scene-title` → `ul.bullets`(4개) → `.source`
- 항목 마크업(4개 같은 형태):
  ```html
  <li data-editable="true"><strong>권한</strong> 실행 환경에서 읽기 범위 제한<span class="sub">프롬프트 문장은 접근 제한이 아님</span></li>
  ```
- 요소 ↔ 문구
  - 제목: 현업 적용 전 확인 항목
  - li 1: `<strong>권한</strong>` 실행 환경에서 읽기 범위 제한 / sub: 프롬프트 문장은 접근 제한이 아님
  - li 2: `<strong>데이터 정의</strong>` 날짜 기준·단위·결측값 의미 / sub: 정의를 누가 관리하는지도 기록
  - li 3: `<strong>결과 확인</strong>` 정답 아는 입력·자료 없음·실패 / sub: 없는 답을 만들지 않고 실패를 알림
  - li 4: `<strong>운영</strong>` 응답 시간·호출량·변경 기록·피드백 / sub: 화면이 뜨는 것과 운영 준비는 다름
  - `.source`: 출처: LangChain SQL Agent 가이드 · Anthropic, Building effective agents
- 강조: 항목 머리말 `strong` 4개를 **한 묶음 1개**로 센다(같은 역할의 이름표, B1 S05 강조 상자 한 쌍과 같은 기준). 그 밖의 파랑 없음. 목록 앞 파랑 막대는 컴포넌트 고정.
- 글자 크기: 72 / 44 / 28 (3종)
- 넘침 근거
  - 폭: 가용 1560 − 52 = 1,508px(줄당 약 34자). 최장 li 2 ≈ 한글 17×44 + 기호·공백 6×13 = 826px → 1줄. li 4 ≈ 784px, li 3 ≈ 740px, li 1 ≈ 682px → 1줄. sub 최장 "없는 답을 만들지 않고 실패를 알림" ≈ 한글 14×28 + 공백 ≈ 430px → 1줄
  - 높이: 항목 1개 = 44×1.4 62 + 6 + sub 39 = 107px. 4×107 + 3×28 = 512px. 145 + 56 + 512 + 58 = **771px ≤ 872** (여유 101px)
- 플레이스홀더: 없음
- 빌드 메모: 목표치·절감 시간 같은 수치를 넣지 않는다. 보류 7로 5항목으로 늘리면 `.bullets` 4개 한도를 넘으므로 `.compact`로 욱여넣지 말고 A07 장면을 새로 만든다(ID 재번호 없음). 그 경우 A06·A07은 이 장면과 같은 배치(1열, 항목 2–3개)로 둔다.

---

## 넘침 점검 요약

| 장면 | 변형 | 본문 기준 높이 | 가용 | 판정 |
|---|---|---|---|---|
| A01 | split `.wide-left` | 좌 패널 594px | 613px | **주의(여유 19px)** · 넘치면 식 줄 제거 |
| A02 | compare `cols-3` + callout | 769px(장면 전체) | 872px | 통과 |
| A03 | compare `cols-3` + 부제 + callout | 833px | 872px | 통과(S17과 같은 구조) |
| A04 | compare `cols-3` + 부제 + callout | 833px | 872px | 통과(S17과 같은 구조) |
| A05 | steps `.row` 4카드 + callout | 700px | 872px | 통과 · 세로 기본형이면 919px로 넘침 → 변형 변경 |
| A06 | title-bullets 1열 | 771px | 872px | 통과 |

빌드 후 확인: `validate_topic.py`, `hyperframes lint`, s-47–s-52 스냅샷. A01은 캡션 아랫변과 출처 윗선의 간격, A05는 카드 설명 줄 수(모두 2줄)를 확인한다.

---

## 카탈로그 추가 요청

| ID | 요청 | 이유 | 본문 대체안 |
|---|---|---|---|
| A1 | `.dg-row.stretch > .dg-arrow { align-self: center; }` | `.dg-row.stretch`는 상자 높이를 맞추려고 `align-items: stretch`를 쓰는데, 같은 줄의 `.dg-arrow`도 늘어나 화살표 글자가 상자 **윗부분**에 붙는다(상자 157px에서 화살표는 위 40px 안). A01 1·2행과 이미 빌드된 B3 S21(`⇄` 2개)이 해당한다. 넘침 문제는 아니고 정렬 문제다 | 본문은 `.dg-row.stretch`를 그대로 쓴다. 반영되지 않으면 화살표가 위쪽에 붙은 채로 둔다(S21과 같은 상태). `.stretch`를 빼면 Q·K·V 상자 높이가 123/157px로 달라져 문구 담당 제작 메모("세 상자 크기를 같게")를 어기므로 빼지 않는다 |

## 문구 축소 요청(slide_content_writer)

없음. 6장 모두 현재 확정 문구로 폭·높이 안에 들어간다. A01은 여유가 19px뿐이라 빌드 화면에서 넘치면 문구를 줄이지 말고 **식 줄(보류 1)을 먼저 뺀다**. 이 순서는 문구 담당 제작 메모에 이미 있다.

---

# v0.4 배치 (2026-09-15)

작성: slide_ui_designer · 대상: A01–A06(보강) + A07–A10(신규) 10장 · 순서 A01 → … → A10
입력: `slide_copy/APP.md` "# v0.4 보강" 절·보류 목록, `00_component_catalog.md` 5·7절, `index.html` `#scene-styles`(v0.4 텍스트 층 포함), topic `DESIGN.md` 최소 적용 규칙, 계획서 7-3·10절
v0.3 절(위)은 기록으로 남긴다. 빌드는 이 절을 따른다.

## v0.4 공통 (부록 10장)

- 배치 순서: eyebrow → `h2.scene-title` → `p.thesis` → `p.explain` → 본문 컴포넌트 1개 → `p.source` → `aside.speaker-note` → 풋터·쪽번호. 막 태그·`.scene-subtitle`·`.callout` 없음(문구 확정본에서 모두 요지·설명으로 옮겨짐).
- eyebrow는 v0.3과 같다: `<div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>`. `night` 없음.
- 장면 `id`는 `s-47`–`s-56` 임시값, `data-scene-id`는 A01–A10, `.page-num`은 임시값(`sync_overview.py --renumber`가 다시 매김). A07–A10은 A06 `</section>` 뒤, `<!-- BLOCK:APP END -->` 앞에 넣는다.
- `.speaker-note`는 문구 파일 각 장면의 "발표자 노트 (최종 전문)"을 그대로 넣는다. 아래 골격에서는 `…`로 줄였다.
- 높이 기준(CSS 실측값으로 계산)
  - 고정: eyebrow+제목 1줄 145 · 요지 1줄 81 · 설명 2줄 109 / 3줄 155 · 본문 위 간격 32 · 출처 1줄 58(2줄 92). 여유 = 872 − 합계, **24px 이상**이어야 통과.
  - 설명 2줄 장면의 본문 가용 447px(여유 24 확보 시 본문 ≤ 423px), 3줄이면 401px(≤ 377px).
  - `.dg-box` 1줄·보조 없음 84px(accent 86) · 보조 1줄 123px(accent 125) · 보조 2줄 157px. `.dg-zone` = 테두리 4 + 위 56 + 아래 24 + 내용(gap 16). `.dg` gap 24. `.dg-caption` 1줄 34px. `.chip` 57px.
  - `.code-card` = 제목 67(패딩 32 + 24×1.4 + 선 1) + 본문 패딩 48 + 줄 수 × 43.4 + 테두리 2 → 5줄 334 · 6줄 377 · 7줄 421. 폭 = 줄 글자 수 × 15.4 + 56 + 2(42자 705px, 39자 659px).
  - `.split-panel` 패딩·테두리 82 + 내용(gap 24). `.compare-col` 패딩·테두리 82.
- 글자 폭 추정: 한글 1.0em, 라틴·숫자 0.55em, 공백·기호 0.3em. 요지 40px×1680 ≈ 42자, 설명 32px×1600 ≈ 50자(라틴 많으면 더 들어감).
- 글자 크기 세기: eyebrow·출처·풋터 크롬 24px과 22–24px 라벨(배지·kicker·dg-sub·dg-caption·code-title·zone-label)은 빼고 센다. 장면당 4종 이하.
- 강조: 요지 밑줄과 `bullets` 앞 막대·`step-num` 원은 컴포넌트 고정 구조색이라 세지 않는다. 그 밖의 파랑(`.dg-box.accent`·`.is-accent`·`strong`·`.chip.accent`·코드 `.hl`)은 **장면당 한 곳**(코드 `.hl` 한 줄은 코드 카드 안 강조로 따로 허용 — S06·S12와 같은 기준).

### 같은 유형 대조 (v0.4)

| 장면 | 본문 구성 | 맞춘 장면 |
|---|---|---|
| A01 · A09 | `split-grid.wide-left` [좌 해석/개념도 · 우 이미지/코드] | S05(원 논문 그림 패널)·S06(개념도 + 코드) |
| A02 · A03 | `.stack` [띠 `.dg-row` · `compare-grid.cols-3`] (A02 띠 위, A03 띠 아래) | S17 3열 |
| A04 | `compare-grid.cols-3`, 열 안 칩 줄 | S17 |
| A05 | `ol.steps.row` 4카드 | S16 |
| A06 | `.stack` [5칸 띠 `.dg-row.stretch` · 캡션] | S10 흐름 띠 |
| A07 · A08 · A10 | `split-grid` [좌 흰 패널 그래프 `.dg` · 우 코드 카드 또는 이미지 패널] | 셋 모두 같은 좌우 비율과 같은 패널 머리 규칙 |

---

## A01 · Transformer와 Q·K·V (v0.4 배치)

- section: `scene clip` · `data-skill="split"` · 변형 **`.split-grid.wide-left`**(좌 913 · 우 703px, gap 64)
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.split-grid.wide-left` [좌 `ul.bullets` 3개 / 우 `.split-panel` (이미지 두 장 한 틀 → 캡션)] → 출처
- 이미지 두 장: `.split-image.h-sm` 한 틀 안에 `<img>` 두 개를 나란히 둔다. 두 `.split-image`를 `.dg-row`에 넣는 방식은 `.split-image`에 폭 규칙이 없어 원본 폭(445·835px)이 그대로 들어와 넘칠 수 있다 → **CSS 요청 C1 `.split-image.pair`**.

```html
<section id="s-47" class="scene clip" data-skill="split" data-scene-id="A01" data-start="230" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">Transformer와 Q·K·V</h2>
  <p class="thesis" data-editable="true">Attention은 Q·K 비교로 정한 비율대로 V를 모은다</p>
  <p class="explain" data-editable="true">비율은 입력마다 새로 계산되는 값이며 학습된 매개변수와 다르다. 원 논문은 encoder–decoder 구조이고, 많은 생성 모델은 decoder 중심이다.</p>
  <div class="split-grid wide-left">
    <ul class="bullets">
      <li data-editable="true"><strong>Q·K·V</strong> 찾는 기준·이름표·내용<span class="sub">비유 · 한 토큰 표현에서 나온 세 벡터</span></li>
      <li data-editable="true">그림 왼쪽: 헤드 하나의 계산<span class="sub">softmax(QK^T / √d) · V</span></li>
      <li data-editable="true">그림 오른쪽: 여러 헤드를 나란히<span class="sub">헤드 = Q·K·V 계산 한 벌 · 헤드마다 다른 변환</span></li>
    </ul>
    <div class="split-panel">
      <div class="split-image h-sm pair">
        <img src="assets/img/b1/attention-fig2a.png" alt="원 논문 Figure 2 왼쪽: Scaled Dot-Product Attention">
        <img src="assets/img/b1/attention-fig2b.png" alt="원 논문 Figure 2 오른쪽: Multi-Head Attention">
      </div>
      <p class="dg-caption" data-editable="true">Vaswani et al. (2017), Figure 2 · arXiv:1706.03762</p>
    </div>
  </div>
  <p class="source" data-editable="true">출처: Vaswani et al., Attention Is All You Need (2017) · arXiv:1706.03762</p>
  <aside class="speaker-note">…문구 파일 A01 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">47 / 56</div>
</section>
```

- 캡션은 문구 파일의 긴 형태(논문 제목 포함, 약 903px)가 아니라 보류 V2의 짧은 형태로 둔다 → **문구 축소 요청 R1**. 논문 제목은 출처 줄에 남으므로 12-1 3번(저자·연도·arXiv ID)을 지킨다.

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 고정 |
| 요지 1줄 | 81 | 약 1,000px < 1,680 |
| 설명 2줄 | 109 | 한글 46×32 + 라틴 21×17.6 + 공백·기호 ≈ 2,044px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| split-grid (우 패널 기준) | 420 | 82 + 이미지 280 + 24 + 캡션 1줄 34 |
| 출처 1줄 | 58 | 약 960px |
| **합계 / 여유** | **845 / 27** | 통과(경계). 좌 bullets 359 < 420 |

- 가로: 좌 913 − 52 = 861px(40px 약 21자). li 1 ≈ 500px, li 2 ≈ 470px, li 3 ≈ 530px → 모두 1줄. sub(28px) 최장 "비유 · 한 토큰 표현에서 나온 세 벡터" ≈ 460px → 1줄. 좌 높이 3 × (56 + 6 + 39) + 2 × 28 = 359px.
- 우 패널 안쪽 621px. 이미지 틀 621 × 280 → 두 칸 각 298px, fig2a는 141 × 280, fig2b는 213 × 280으로 들어간다(가운데 정렬, 비율 유지). 캡션 짧은 형태 ≈ 575px → 1줄.
- 글자 크기: 72 / 40(요지·항목) / 32 / 28 → 4종.
- 강조: 항목 1 `strong` "Q·K·V" 한 곳. 이미지 틀에 테두리·배경을 넣지 않는다(흰 패널이 바탕).
- 주의
  - 여유 27px. 스냅샷에서 캡션 아랫변 ~ 출처 윗선 간격을 확인한다.
  - 사용자가 V2를 받지 않고 긴 캡션(2줄, +34px)을 유지하면 패널이 454px → 여유 −7px로 넘친다. 그때는 CSS 요청 C2(`.split-panel.is-tight`)를 적용한다(패널 82 → 50, 여유 25px).
  - fig2b 안 글자("Scaled Dot-Product Attention")는 원본 약 40px × 0.25 ≈ 10px로 작다. 그림은 구조를 보여 주는 보조 자료이고 읽을 내용은 항목 2·3이 대신한다. `h-md`(360)는 +80px로 넘치므로 쓰지 않는다.
  - v0.3의 CSS 개념도·배지·패널 제목·식 칩 줄은 모두 지운다.

## A02 · RAG 검색 방식과 메타데이터 (v0.4 배치)

- section: `scene clip` · `data-skill="compare"`
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.stack` [ 파이프라인 띠 `.dg-row.is-compact` → `.compare-grid.cols-3`(열3 `is-accent`) ] → 출처
- 띠는 **`.is-compact`(CSS 요청 C3, 상자 위아래 패딩 20 → 12)** 를 쓴다. 기본 상자(84px)로 두면 본문 436px → 여유 11px로 기준(24) 미달이다.

```html
<section id="s-48" class="scene clip" data-skill="compare" data-scene-id="A02" data-start="235" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">RAG 검색 방식과 메타데이터</h2>
  <p class="thesis" data-editable="true">RAG 품질은 재학습이 아니라 분할·검색·메타데이터로 다듬는다</p>
  <p class="explain" data-editable="true">RAG 품질은 재학습이 아니라 분할·검색·메타데이터로 다듬는다. 답이 틀리면 검색이 틀렸는지, 찾은 근거로 잘못 답했는지부터 나눈다. 검색 쪽은 재정렬(Reranking), 생성 쪽은 프롬프트 제약을 본다.</p>
  <div class="stack">
    <div class="dg-row is-compact">
      <div class="dg-box" data-editable="true">분할</div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">임베딩</div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">저장</div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">검색</div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">생성</div>
      <span class="dg-caption" data-editable="true">개념 예시 · 교안 내용 재구성</span>
    </div>
    <div class="compare-grid cols-3">
      <div class="compare-col">
        <div class="compare-kicker" data-editable="true">미리 준비</div>
        <div class="compare-heading" data-editable="true">청킹·임베딩</div>
        <ul class="compare-list">
          <li data-editable="true">찾기 좋은 단위로 분할</li>
          <li data-editable="true">크기·겹침은 실험해 결정</li>
        </ul>
      </div>
      <div class="compare-col">
        <div class="compare-kicker" data-editable="true">질문할 때</div>
        <div class="compare-heading" data-editable="true">벡터·키워드 검색</div>
        <ul class="compare-list">
          <li data-editable="true">벡터: 뜻이 가까운 조각</li>
          <li data-editable="true">둘을 합친 하이브리드도</li>
        </ul>
      </div>
      <div class="compare-col is-accent">
        <div class="compare-kicker" data-editable="true">먼저 설계</div>
        <div class="compare-heading" data-editable="true">메타데이터</div>
        <ul class="compare-list">
          <li data-editable="true">출처·발행일·문서 버전</li>
          <li data-editable="true">질문에서 필터를 뽑기도</li>
        </ul>
      </div>
    </div>
  </div>
  <p class="source" data-editable="true">출처: Lewis et al. 2020 · LangChain Retrieval 가이드 · 4일·5일 과정 교안 RAG 장(용어 재구성)</p>
  <aside class="speaker-note">…문구 파일 A02 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">48 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 790px |
| 요지 1줄 | 81 | 약 1,000px |
| 설명 2줄 | 109 | 한글 64×32 + 라틴 9×17.6 + 공백·기호 ≈ 2,436px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| 띠(`.is-compact`) | 68 | 패딩 24 + 테두리 2 + 32×1.3 |
| 스택 간격 | 24 | `.stack` |
| 3열 | 328 | 82 + kicker 34 + heading 80 + 목록(24 + 2×45 + 18) — 열 메모 없음 |
| 출처 1줄 | 58 | 약 1,000px |
| **합계 / 여유** | **845 / 27** | 통과(C3 전제). C3 미반영이면 861 / 11 → 아래 주의 |

- 가로: 띠 = 상자 5 + 화살표 4(각 약 40) + 캡션 약 307 + 간격 9×20 → 상자 폭 약 206px, 안쪽 156px. 최장 "임베딩" 96px → 1줄. 캡션은 줄 끝에 붙는다(줄바꿈 없음).
- 3열: 열 539px, 목록 안쪽 427px(강조 열 425). 최장 "크기·겹침은 실험해 결정"·"둘을 합친 하이브리드도"·"질문에서 필터를 뽑기도" ≈ 340–350px → 모두 1줄. heading 최장 "벡터·키워드 검색" ≈ 304px → 1줄.
- 글자 크기: 72 / 40(요지·열 제목) / 32(설명·띠 상자·목록) → 3종.
- 강조: 열3 `.is-accent` 한 곳. 띠 상자는 모두 기본색, 띠와 열 사이 화살표 없음(열은 역할 구분).
- 주의
  - 열 메모를 되살리지 않는다(+54px → 여유 −27).
  - C3이 반영되지 않으면 띠 상자 5개를 `.chip`(57px)으로 바꾼다(여유 38px). 글자는 28px가 되지만 띠는 단계 이름표라 읽기에 문제없다. 상자 글자 크기를 CSS로 줄이는 방식은 쓰지 않는다.

## A03 · 프레임워크 선택 기준 (v0.4 배치)

- section: `scene clip` · `data-skill="compare"`
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.stack` [ `.compare-grid.cols-3`(강조 열 없음) → 공통 기반 띠 `.dg-row.is-compact` ] → 출처
- A02와 같은 부품을 위아래만 바꿔 쓴다(A02는 띠가 위, A03은 세 열을 받치는 띠가 아래). 띠는 C3 `.is-compact`.
- 문구 파일은 띠를 `.dg-row.stretch`로 적었지만, 상자 하나 + 캡션이라 높이를 맞출 상자가 없다. 캡션이 세로 가운데에 오도록 `.stretch` 없이 쓴다.

```html
<section id="s-49" class="scene clip" data-skill="compare" data-scene-id="A03" data-start="240" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">프레임워크 선택 기준</h2>
  <p class="thesis" data-editable="true">배우는 순서가 아니라 문제에 필요한 추상화 수준을 고른다</p>
  <p class="explain" data-editable="true">추상화 수준은 기능이 미리 묶인 정도다. 단순 호출 하나면 SDK로 충분하다. LangChain Agent와 Deep Agents는 LangGraph 위에서 동작한다.</p>
  <div class="stack">
    <div class="compare-grid cols-3">
      <div class="compare-col">
        <div class="compare-kicker" data-editable="true">짧게 구성</div>
        <div class="compare-heading" data-editable="true">LangChain Agent</div>
        <ul class="compare-list">
          <li data-editable="true">모델·도구 호출 루프</li>
          <li data-editable="true">create_agent 한 번으로</li>
        </ul>
      </div>
      <div class="compare-col">
        <div class="compare-kicker" data-editable="true">흐름 직접 설계</div>
        <div class="compare-heading" data-editable="true">LangGraph</div>
        <ul class="compare-list">
          <li data-editable="true">단계·분기를 직접 정의</li>
          <li data-editable="true">상태 저장·중단 후 재개</li>
        </ul>
      </div>
      <div class="compare-col">
        <div class="compare-kicker" data-editable="true">기능 묶음</div>
        <div class="compare-heading" data-editable="true">Deep Agents</div>
        <ul class="compare-list">
          <li data-editable="true">계획·파일·위임 내장</li>
          <li data-editable="true">여러 단계의 긴 작업용</li>
        </ul>
      </div>
    </div>
    <div class="dg-row is-compact">
      <div class="dg-box muted" data-editable="true">공통 실행 기반 · LangGraph 런타임</div>
      <span class="dg-caption" data-editable="true">개념 예시 · 기반 관계, 배우는 순서 아님</span>
    </div>
  </div>
  <p class="source" data-editable="true">출처: LangChain Overview · LangGraph Overview · LangChain Concepts(Agent harnesses: Deep Agents)</p>
  <aside class="speaker-note">…문구 파일 A03 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">49 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 720px |
| 요지 1줄 | 81 | 약 1,110px |
| 설명 2줄 | 109 | 한글 38×32 + 라틴 36×17.6 + 공백·기호 ≈ 2,040px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| 3열 | 328 | A02와 같은 열 구조(메모 없음) |
| 스택 간격 | 24 | `.stack` |
| 기반 띠(`.is-compact`) | 68 | 상자 1줄 |
| 출처 1줄 | 58 | 약 1,300px |
| **합계 / 여유** | **845 / 27** | 통과(C3 전제) |

- 가로: 목록 안쪽 427px. 최장 "create_agent 한 번으로" ≈ 라틴 12×17.6 + 한글 4×32 + 공백 ≈ 350px, "상태 저장·중단 후 재개" ≈ 340px → 모두 1줄. heading "LangChain Agent" ≈ 320px < 457px → 1줄. 띠 상자 폭 = 1680 − 20 − 캡션 약 394 = 1,266px, 문구 약 510px → 1줄.
- 글자 크기: 72 / 40 / 32 → 3종.
- 강조: 없음(요지 밑줄만). 세 열 같은 크기·같은 색, 열 번호·열 사이 화살표·띠로 향하는 화살표 없음. 띠는 `.muted`(오프화이트 면)로 세 열과 층이 다름을 보인다.
- 주의
  - C3이 반영되지 않으면 여유 11px → 띠 상자를 `.chip`으로 바꾼다(여유 38px). `.chip`은 `.muted` 면이 없으므로 이때는 캡션만으로 기반 관계를 말한다.
  - 열 메모를 되살리지 않는다.

## A04 · MCP·Subagent·Hook 역할 (v0.4 배치)

- section: `scene clip` · `data-skill="compare"`
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.compare-grid.cols-3`(강조 열 없음, `.stack` 없이 바로) → 출처
- 열1 안 순서: kicker → heading → `ul.compare-list`(1개) → 칩 도식 `.dg-row` → `p.compare-note`. 열2·3: kicker → heading → 목록 2개 → note.
- `.compare-col` 자식은 위 여백이 0이라 목록 바로 밑에 칩 줄이 붙는다 → **CSS 요청 C4**(`.compare-list + .dg-row` 위 간격 18px, 목록 항목 간격과 같게).

```html
<section id="s-50" class="scene clip" data-skill="compare" data-scene-id="A04" data-start="245" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">MCP·Subagent·Hook 역할</h2>
  <p class="thesis" data-editable="true">셋은 상하위 단계가 아니라 서로 다른 역할이다</p>
  <p class="explain" data-editable="true">세 기능은 필요할 때만 골라 조합하고, 기본 도구로 충분하면 더하지 않는다. CLAUDE.md 지침은 권한을 강제하지 않으므로 설치·권한은 사내 가이드의 승인된 설정을 따른다.</p>
  <div class="compare-grid cols-3">
    <div class="compare-col">
      <div class="compare-kicker" data-editable="true">외부 연결</div>
      <div class="compare-heading" data-editable="true">MCP</div>
      <ul class="compare-list">
        <li data-editable="true">앱 N개·도구 M개를 한 규약으로</li>
      </ul>
      <div class="dg-row">
        <span class="chip" data-editable="true">N×M</span>
        <span class="dg-arrow" aria-hidden="true">→</span>
        <span class="chip accent" data-editable="true">N+M</span>
        <span class="dg-caption" data-editable="true">앱·도구 연결 수</span>
      </div>
      <p class="compare-note" data-editable="true">개념 예시 · 교안 내용 재구성</p>
    </div>
    <div class="compare-col">
      <div class="compare-kicker" data-editable="true">작업 분담</div>
      <div class="compare-heading" data-editable="true">Subagent</div>
      <ul class="compare-list">
        <li data-editable="true">별도 맥락에서 하위 작업</li>
        <li data-editable="true">결과를 주 대화로 반환</li>
      </ul>
      <p class="compare-note" data-editable="true">예: 예외 입력만 점검</p>
    </div>
    <div class="compare-col">
      <div class="compare-kicker" data-editable="true">이벤트 처리</div>
      <div class="compare-heading" data-editable="true">Hook</div>
      <ul class="compare-list">
        <li data-editable="true">정해진 시점에 자동 실행</li>
        <li data-editable="true">명령 실행형·모델 판단형</li>
      </ul>
      <p class="compare-note" data-editable="true">예: 파일 수정 후 포맷</p>
    </div>
  </div>
  <p class="source" data-editable="true">출처: Claude Code 문서 — Features overview · MCP · Subagents · Hooks · 5일 과정 교안 MCP 장(재구성)</p>
  <aside class="speaker-note">…문구 파일 A04 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">50 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 900px |
| 요지 1줄 | 81 | 약 1,000px |
| 설명 2줄 | 109 | 한글 64×32 + 라틴 9×17.6 + 공백·기호 ≈ 2,456px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| 3열(MCP 열 기준) | 394 | 82 + 34 + 80 + 목록(24 + 45) + 18 + 칩 줄 57 + note 54. 열2·3은 382 |
| 출처 1줄 | 58 | 약 1,150px |
| **합계 / 여유** | **819 / 53** | 통과 |

- 가로: 열 안쪽 457px. 칩 줄 = 칩 "N×M" 약 77 + 20 + 화살표 40 + 20 + 칩 "N+M" 약 77 + 20 + 캡션 약 166 = 420px → 1줄(여유 37px). 목록 최장 "앱 N개·도구 M개를 한 규약으로"·"정해진 시점에 자동 실행" ≈ 350px < 427 → 1줄. note 최장 "개념 예시 · 교안 내용 재구성" ≈ 307px → 1줄.
- 글자 크기: 72 / 40 / 32 / 28(칩) → 4종.
- 강조: 칩 `N+M` `.accent` 한 곳. `.is-accent` 열 없음. 세 열 같은 크기·같은 높이(note가 `margin-top:auto`로 바닥 정렬), 위아래 배치·열 번호 없음.
- 주의
  - C4가 반영되지 않으면 칩 줄이 목록 바로 밑(간격 0)에 붙는다. 넘치지는 않는다(높이 −18).
  - 칩 줄 폭 여유가 37px뿐이다. 캡션이 2줄로 접히면 칩 줄 높이는 그대로(57px 안)지만 보기 나쁘므로, 스냅샷에서 1줄인지 확인한다.
  - `×`는 곱셈 기호(U+00D7) 그대로 둔다. 영문 x로 바꾸지 않는다.

## A05 · 사내 실행 환경 문제 해결 (v0.4 배치)

- section: `scene clip` · `data-skill="steps"` · 변형 `ol.steps.row` 가로 카드 4개(v0.3과 같음)
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `ol.steps.row` → 출처. v0.3의 `.stack`·callout은 지운다(callout 문장은 설명 2문장으로 옮겨짐). `ol.steps`는 `.scene` 직계 자식이 되어 요지·설명 뒤 32px 간격을 받는다.
- 예시 줄: `.step-body` 안 두 번째 보조 줄로 `span.dg-sub`(24px, `--ink-3`, 위 6px)를 쓴다. 설명 줄 `.step-desc`(28px, `--ink-2`)와 크기·색이 달라 "예시"임이 드러나고, 카드 폭 298px에서 2줄 안에 들어간다. 두 번째 `.step-desc`로 두면 28px 3줄(+39px)이 된다.

```html
<section id="s-51" class="scene clip" data-skill="steps" data-scene-id="A05" data-start="250" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">사내 실행 환경 문제 해결</h2>
  <p class="thesis" data-editable="true">막히면 접속부터 파일 경로까지 한 층씩 좁힌다</p>
  <p class="explain" data-editable="true">호환 API라도 모든 옵션이 똑같이 동작하지는 않는다. 오류 원문을 남기고 한 번에 한 가지만 바꿔 다시 실행한다. 주소·계정·키는 사내 실행 가이드에서 확인한다.</p>
  <ol class="steps row">
    <li class="step">
      <div class="step-num" data-editable="true">1</div>
      <div class="step-body" data-editable="true">접속<span class="step-desc">서버 응답·인증 오류인지 먼저 구분</span><span class="dg-sub">예: 콘솔 인코딩 오류로 서버가 안 뜸</span></div>
    </li>
    <li class="step">
      <div class="step-num" data-editable="true">2</div>
      <div class="step-body" data-editable="true">패키지<span class="step-desc">설치 판본을 실습 가이드와 비교</span><span class="dg-sub">예: 호환 서버용 임베딩 옵션 누락</span></div>
    </li>
    <li class="step">
      <div class="step-num" data-editable="true">3</div>
      <div class="step-body" data-editable="true">모델 기능<span class="step-desc">도구 호출·임베딩 지원 여부 확인</span><span class="dg-sub">예: 임베딩 모델 바꾸면 벡터 새로 생성</span></div>
    </li>
    <li class="step">
      <div class="step-num" data-editable="true">4</div>
      <div class="step-body" data-editable="true">파일 경로<span class="step-desc">코드가 실행되는 위치 기준으로 확인</span><span class="dg-sub">예: 실행 위치가 달라 파일 못 찾음</span></div>
    </li>
  </ol>
  <p class="source" data-editable="true">출처: vLLM Online Serving 문서 · Claude Code 작동 원리 문서 · 현업 활용 가이드 문제 해결 사례(일반화) · 근거: 강사 강의안</p>
  <aside class="speaker-note">…문구 파일 A05 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">51 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 860px |
| 요지 1줄 | 81 | 약 1,000px |
| 설명 2줄 | 109 | 한글 62×32 + 라틴 3×17.6 + 공백·기호 ≈ 2,300px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| 카드 | 384 | 패딩 80 + 테두리 2 + 번호 72 + 24 + 이름 51 + 설명(6 + 2줄 78) + 예시(6 + 2줄 65) |
| 출처 1줄 | 58 | 약 1,350px |
| **합계 / 여유** | **809 / 63** | 통과 |

- 가로: 카드 (1680 − 3×64)/4 = 372px, 안쪽 298px. 이름 최장 "모델 기능"·"파일 경로" ≈ 163px → 1줄. 설명(28px, 줄당 약 10자) 네 개 모두 2줄(v0.3 실측과 같음). 예시(24px, 줄당 약 12자) 네 개 모두 한글 13자 안팎 ≈ 355px → 2줄.
- 글자 크기: 72 / 40(요지) / 38(카드 이름) / 32(설명) / 28(카드 설명) → **5종으로 기준(4종) 초과**. v0.4 요지·설명 층이 더해져 생긴 것이며 `steps.row`를 쓰는 본문 장면(S10·S16·S28 등)도 같다 → **CSS 요청 C5**(`.steps.row .step-body` 38 → 40px, 요지와 같은 크기). 반영되면 72 / 40 / 32 / 28로 4종, 카드 높이 +3px(여유 60px). 이름 폭은 "모델 기능" ≈ 172px로 1줄 유지.
- 강조: 없음(`step-num` 파랑 원은 구조색). `.step.is-accent` 쓰지 않는다. 카드 사이 "→"는 CSS가 그린다.
- 주의
  - 예시 줄은 현업 활용 가이드 사례를 일반화한 문장이다. 옵션 이름·명령·경로·오류 원문을 넣지 않는다.
  - 예시가 3줄로 접히면 카드 +32px(여유 31px)로 여전히 통과한다.

## A06 · 현업 적용 전 확인 항목 (v0.4 배치)

- section: `scene clip` · `data-skill="title-bullets"` 유지(보류 V9 → UI 판단: **받아들인다**). `validate_topic.py`는 `data-skill` 값만 검사하고, `.bullets`가 없어도 쓰는 CSS가 없다. 기획표의 장면 유형을 바꾸지 않기 위해 값은 그대로 둔다.
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.stack` [ 5칸 띠 `.dg-row.stretch`(상자 5 + 화살표 4) → `p.dg-caption` ] → 출처. v0.3 `ul.bullets`는 지운다.
- 띠는 기본 상자(패딩 20)를 쓴다. 높이 여유가 커서 `.is-compact`가 필요 없다.

```html
<section id="s-52" class="scene clip" data-skill="title-bullets" data-scene-id="A06" data-start="255" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">현업 적용 전 확인 항목</h2>
  <p class="thesis" data-editable="true">화면이 뜨는 것과 업무에 쓸 준비는 다르다</p>
  <p class="explain" data-editable="true">오늘 만든 작은 도구를 업무에 쓰기 전에 다섯 가지를 확인한다. 권한은 프롬프트 문장이 아니라 실행 환경에서 제한한다. 없는 답을 만들지 않고 실패를 알리는지도 본다.</p>
  <div class="stack">
    <div class="dg-row stretch">
      <div class="dg-box" data-editable="true">권한 제한<span class="dg-sub">읽기 범위·허용 테이블</span></div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">데이터 정의<span class="dg-sub">날짜 기준·단위·결측값 문서화</span></div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">정답 세트 검증<span class="dg-sub">정답 아는 입력·실패 상황</span></div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">호출 흐름 기록<span class="dg-sub">응답 시간·호출량도 함께</span></div>
      <span class="dg-arrow" aria-hidden="true">→</span>
      <div class="dg-box" data-editable="true">변경·피드백<span class="dg-sub">누가 무엇을 바꿨는지</span></div>
    </div>
    <p class="dg-caption" data-editable="true">권장 순서 예시 · 교안·현업 활용 가이드 체크리스트 재구성</p>
  </div>
  <p class="source" data-editable="true">출처: LangChain SQL Agent 가이드 · Anthropic, Building effective agents · 4일 과정 교안·현업 활용 가이드 체크리스트(재구성)</p>
  <aside class="speaker-note">…문구 파일 A06 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">52 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 790px |
| 요지 1줄 | 81 | 약 900px |
| 설명 2줄 | 109 | 한글 67×32 + 공백·기호 ≈ 2,390px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| 5칸 띠 | 157 | 42 + 이름 1줄 42 + 6 + 보조 2줄 67(`.stretch`로 다섯 칸 같은 높이) |
| 스택 간격 + 캡션 | 58 | 24 + 34 |
| 출처 1줄 | 58 | 약 1,350px |
| **합계 / 여유** | **640 / 232** | 통과 |

- 가로: 상자 폭 (1680 − 화살표 4×40 − 간격 8×20)/5 = 272px, 안쪽 222px. 이름 "권한 제한" 138 · "데이터 정의" 170 · "변경·피드백" 170 → 1줄. "정답 세트 검증"·"호출 흐름 기록" ≈ 212px로 **1줄 경계**(2줄이 되면 띠 199px, 여유 190px로 통과). 보조(24px, 줄당 약 9자): "누가 무엇을 바꿨는지"만 1줄, 나머지 2줄. 캡션 ≈ 600px → 1줄(가운데 정렬).
- 글자 크기: 72 / 40 / 32 → 3종.
- 강조: 없음(요지 밑줄만). 다섯 칸 모두 같은 색. 화살표는 "권장 순서"이며 캡션에 그렇게 적혀 있다.
- 주의
  - 여유 232px는 비워 둔다. 띠를 `.fill`로 늘리거나 v0.3 bullets를 되살리지 않는다(카탈로그 7-2, 문구 담당 메모).
  - 관측 도구 이름(Phoenix 등)을 상자·보조에 넣지 않는다.

## A07 · LangGraph로 흐름 꺼내기 (v0.4 배치, 신규)

- section: `scene clip` · `data-skill="steps"` · 본문 `.split-grid`(기본 1fr 1fr, 좌 808 · 우 808px, gap 64)
- 비율: 문구 파일은 좌 55% · 우 45%를 적었지만, 코드 최장 줄이 42자라 코드 카드에 705px(글자당 15.4px) ~ 764px(JetBrains Mono 실제 폭 0.6em = 16.8px)가 필요하다. `.wide-left`의 우 703px로는 마지막 글자가 잘릴 수 있어 **1fr 1fr**로 둔다.
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.split-grid` [좌 `.dg`(State 영역 → 캡션) / 우 `.stack` > `.code-card`] → 출처
- 좌 개념도는 **흰 패널(`.split-panel`) 없이** 캔버스 위에 둔다. 패널 여백 82px를 더하면 503px로 가용 423px를 넘는다. A08·A10도 같은 방식이다(흰 상자·점선 영역이 캔버스 위에 바로 놓임, S29 코드 카드와 같은 층).
- 영역 안 구성
  - 1행 `.dg-row`: `span.chip` "START" → `.dg-box` "분류" + `.dg-sub` "classify 노드". START는 시작 표식이라 칩으로 둔다(상자 폭을 분류 상자에 몰아 줌).
  - 2행 `.dg-row`: `span.dg-caption` "조건부 Edge: …" → `span.dg-arrow` "↓". 캡션을 앞에 두면 ↓가 분류 상자 가로 중앙(약 475px) 근처인 452–492px에 온다. ↓를 앞에 두면 START 칩 밑에 붙어 "START에서 갈라진다"로 읽히므로 순서를 바꾸지 않는다.
  - 3행 `.dg-row.stretch`: 상자 3개(보조 없음).

```html
<section id="s-53" class="scene clip" data-skill="steps" data-scene-id="A07" data-start="260" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">LangGraph로 흐름 꺼내기</h2>
  <p class="thesis" data-editable="true">분기·중단·재개가 필요할 때 흐름을 그래프로 직접 그린다</p>
  <p class="explain" data-editable="true">LangGraph는 상태(State)·단계(Node)·연결(Edge)로 흐름을 정의한다. create_agent의 도구 호출 루프도 내부는 그래프다. 순서가 고정된 작업이면 직접 그리지 않아도 된다.</p>
  <div class="split-grid">
    <div class="dg">
      <div class="dg-zone">
        <div class="dg-zone-label" data-editable="true">State · messages·category를 모든 노드가 공유</div>
        <div class="dg-row">
          <span class="chip" data-editable="true">START</span>
          <span class="dg-arrow" aria-hidden="true">→</span>
          <div class="dg-box" data-editable="true">분류<span class="dg-sub">classify 노드</span></div>
        </div>
        <div class="dg-row">
          <span class="dg-caption" data-editable="true">조건부 Edge: 질문 종류로 다음 노드 선택</span>
          <span class="dg-arrow" aria-hidden="true">↓</span>
        </div>
        <div class="dg-row stretch">
          <div class="dg-box" data-editable="true">기사 검색</div>
          <div class="dg-box" data-editable="true">SQL 조회</div>
          <div class="dg-box" data-editable="true">바로 답변</div>
        </div>
      </div>
      <p class="dg-caption" data-editable="true">모두 END로 · 개념 예시, 오전 앱 구조 아님 · 교안 내용 재구성</p>
    </div>
    <div class="stack">
      <div class="code-card">
        <div class="code-title" data-editable="true">StateGraph 빌드 · 교육용 축약(일부 줄 생략)</div>
        <pre class="code-body" data-editable="true">g = StateGraph(State)
g.add_node("classify", classify)
g.add_edge(START, "classify")
<span class="hl">g.add_conditional_edges("classify", route)</span>
app = g.compile(checkpointer=...)
app.invoke({"messages": [...]}, config)</pre>
      </div>
    </div>
  </div>
  <p class="source" data-editable="true">출처: LangGraph Overview · 4일 과정 교안 LangGraph 장(재구성) · 뿌리강의 REMASTERED</p>
  <aside class="speaker-note">…문구 파일 A07 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">53 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 1,000px |
| 요지 1줄 | 81 | 약 1,100px |
| 설명 2줄 | 109 | 한글 46×32 + 라틴 34×17.6 + 공백·기호 ≈ 2,270px → 2줄 |
| 본문 위 간격 | 32 | CSS |
| 좌 `.dg` | 421 | 영역(테두리 4 + 위 56 + 아래 24 + 1행 123 + 16 + 2행 40 + 16 + 3행 84 = 363) + 24 + 캡션 34 |
| 우 코드 카드 | (377) | 6줄. 좌보다 낮아 격자 높이에 영향 없음 |
| 출처 1줄 | 58 | 약 1,000px |
| **합계 / 여유** | **846 / 26** | 통과(경계) |

- 가로: 영역 안쪽 808 − 4 − 48 = 756px. 1행 = 칩 약 115 + 20 + 화살표 40 + 20 + 분류 상자 561px. 2행 캡션 ≈ 432px → 1줄. 3행 상자 폭 (756 − 40)/3 ≈ 239px, 안쪽 189px — "기사 검색"·"바로 답변" 138px, "SQL 조회" 127px → 1줄. 영역 라벨(22px) ≈ 505px → 1줄.
- 코드: 줄 길이 21 / 32 / 29 / 42 / 33 / 39자 → 최장 42자 647–706px < 카드 안쪽 750px. 코드 제목 ≈ 581px → 1줄.
- 글자 크기: 72 / 40 / 32 / 28(코드·칩) → 4종.
- 강조: 코드 4줄째 `.hl` 한 곳. 개념도 상자에는 `.accent`를 쓰지 않는다.
- 주의
  - 여유 26px. 스냅샷에서 캡션 아랫변 ~ 출처 윗선을 확인한다. 넘치면 3행을 `.chip` 3개로 바꾸지 말고(주 글자 32px 규칙) 영역 라벨·캡션 문구를 줄이지도 않는다 — 1행 분류 상자의 보조 "classify 노드"를 노트로 옮기는 문구 축소(−39px)를 먼저 요청한다.
  - 코드 줄 앞뒤 공백을 바꾸지 않는다(`pre`는 공백을 그대로 보인다). `.hl` 스팬은 줄 전체를 감싼다.
  - API 이름은 오케스트레이터가 공식 문서로 확인 중(보류 V10). 이름이 바뀌어도 42자 이하·6줄이면 배치는 그대로다.

## A08 · Agentic RAG와 재검색 (v0.4 배치, 신규)

- section: `scene clip` · `data-skill="steps"`
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.stack` [ `.split-grid.wide-left`(좌 913 · 우 703) [좌 `.dg` 루프 / 우 `.stack` > `.code-card`] → 칩 줄 `.dg-row` ] → 출처
- 비율: 코드 최장 38자(585–638px + 58)라 우 703px에 들어가고, 좌 상자 3개가 한 줄에 서려면 913px가 필요하다("관련성 평가"가 1fr 1fr의 안쪽 164px에서는 2줄 → +42px로 넘침). A07·A10(1fr 1fr)과 비율만 다르고 좌 그래프 · 우 자료 구조는 같다.
- 좌 개념도(흰 패널 없음, A07과 같음)
  - 1행 `.dg-row`(세로 가운데 정렬): 검색 → 관련성 평가(`.accent`) → [`.stack`: "→" + `.dg-sub` "yes"] → 답변 생성. 화살표 칸 두 개의 폭(약 40px)이 같아 가운데 상자가 줄 가운데에 온다.
  - 2행: `div.dg-arrow` 한 줄(블록이라 `.dg` 폭 전체로 늘어나고 `text-align:center`) 안에 `span`(↓, `aria-hidden`) + `span.dg-caption` "no". ↓가 가운데 상자 밑에 온다.
  - 3행 `.dg-row`: 질문 재작성 상자 + 같은 줄 끝 `span.dg-caption` "개념 예시 · 교안 내용 재구성". 캡션을 따로 한 줄 두면 +58px로 넘치므로 3행 끝에 붙인다(A02 띠와 같은 방식). 상자 폭 약 586px라 ↓ 밑을 덮는다.
- 되돌아가는 화살표(←·↑)는 쓰지 않는다. "다시 검색으로"는 상자 보조 줄이 말한다.

```html
<section id="s-54" class="scene clip" data-skill="steps" data-scene-id="A08" data-start="265" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">Agentic RAG와 재검색</h2>
  <p class="thesis" data-editable="true">검색 결과를 평가해 부족하면 질문을 고쳐 다시 찾는다</p>
  <p class="explain" data-editable="true">본문 B2의 '검색이 틀렸나' 확인을 그래프 안에 넣은 구조다. 모델이 문서마다 관련성을 yes/no로 매기고, 그 결과로 경로가 갈린다. 판정마다 호출이 늘어 재시도 횟수를 제한한다.</p>
  <div class="stack">
    <div class="split-grid wide-left">
      <div class="dg">
        <div class="dg-row">
          <div class="dg-box" data-editable="true">검색<span class="dg-sub">retrieve</span></div>
          <span class="dg-arrow" aria-hidden="true">→</span>
          <div class="dg-box accent" data-editable="true">관련성 평가<span class="dg-sub">문서별 yes/no</span></div>
          <div class="stack">
            <span class="dg-arrow" aria-hidden="true">→</span>
            <span class="dg-sub" data-editable="true">yes</span>
          </div>
          <div class="dg-box" data-editable="true">답변 생성<span class="dg-sub">generate</span></div>
        </div>
        <div class="dg-arrow"><span aria-hidden="true">↓</span> <span class="dg-caption" data-editable="true">no</span></div>
        <div class="dg-row">
          <div class="dg-box" data-editable="true">질문 재작성<span class="dg-sub">다시 검색으로 · 횟수 제한</span></div>
          <span class="dg-caption" data-editable="true">개념 예시 · 교안 내용 재구성</span>
        </div>
      </div>
      <div class="stack">
        <div class="code-card">
          <div class="code-title" data-editable="true">관련성 판정 스키마 · 교육용 축약(import 생략)</div>
          <pre class="code-body" data-editable="true">class GradeDocuments(BaseModel):
    <span class="hl">score: Literal["yes", "no"]</span>
grader = model.with_structured_output(
    GradeDocuments)
grade = grader.invoke(prompt).score</pre>
        </div>
      </div>
    </div>
  </div>
  <p class="source" data-editable="true">출처: 4일·5일 과정 교안 RAG 장(Agentic·Self·Corrective·Adaptive RAG 재구성) · Lewis et al. 2020</p>
  <aside class="speaker-note">…문구 파일 A08 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">54 / 56</div>
</section>
```

- 칩 줄은 `.chip-row`가 아니라 `.dg-row`에 둔다. `.chip-row`는 세로 정렬이 `stretch`라 앞 캡션("같은 계열")이 칩 윗줄에 붙는다. `.dg-row`는 세로 가운데 정렬이고 줄바꿈이 없다(폭 여유 약 400px로 충분).

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 780px |
| 요지 1줄 | 81 | 약 1,100px |
| 설명 2줄 | 109 | 줄바꿈 추정: 1줄째 "…관련성을 yes/no로"까지 약 1,517px, 2줄째 약 1,154px |
| 본문 위 간격 | 32 | CSS |
| 좌 `.dg` | 336 | 1행 125(강조 상자) + 24 + 2행 40 + 24 + 3행 123. 우 코드 5줄 334 |
| 스택 간격 + 칩 줄 | 81 | 24 + 57 |
| 출처 1줄 | 58 | 약 1,080px |
| **합계 / 여유** | **842 / 30** | 통과 |

- 가로: 1행 상자 폭 (913 − 화살표 칸 2×40 − 간격 4×20)/3 ≈ 251px, 안쪽 약 200px. "관련성 평가" ≈ 170px → 1줄. 보조 최장 "문서별 yes/no" ≈ 150px → 1줄. 3행 상자 폭 = 913 − 20 − 캡션 약 307 = 586px. 칩 줄 = 캡션 103 + 칩 357 · 326 · 427 + 간격 3×20 ≈ 1,273px < 1,680.
- 코드: 줄 길이 32 / 31 / 38 / 19 / 35자 → 최장 38자 585–638px < 카드 안쪽 645px(**0.6em 기준 여유 7px**). 코드 제목 ≈ 465px → 1줄.
- 글자 크기: 72 / 40 / 32 / 28(코드·칩) → 4종.
- 강조: 관련성 평가 `.dg-box.accent` 한 곳 + 코드 2줄째 `.hl`(코드 안 강조). 칩 셋은 모두 기본색(셋 사이 서열 없음).
- 주의
  - 설명이 3줄로 접히면(+46px) 여유 −16px → 보류 V14대로 **칩 줄(스택 간격 포함 81px)을 뺀다**(여유 65px). 칩 내용은 노트에 이미 있다.
  - 코드 3줄째(38자)가 렌더러에서 잘리면 `.wide-left`를 기본 1fr 1fr로 바꾸지 말고(1행이 2줄로 넘침) 3·4줄 줄바꿈 위치를 바꾸는 문구 조정을 요청한다.
  - 2행의 `div.dg-arrow`는 화살표 글자만 `aria-hidden`이고 "no" 캡션은 편집 가능하다.

## A09 · 하네스와 Deep Agents (v0.4 배치, 신규)

- section: `scene clip` · `data-skill="split"` · 본문 `.split-grid.wide-left`(좌 913 · 우 703px) — A01과 같은 split 비율
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.split-grid.wide-left` [좌 `.dg`(영역 1 → 영역 2 → 캡션) / 우 `.stack` > `.code-card`] → 출처
- 좌 개념도(흰 패널 없음, A07·A08과 같음)
  - 영역 1 `.dg-zone` "하네스 · 모델을 둘러싼 실행 틀" 안에 `.dg-row.stretch.is-compact`(C3): 모델(`.accent`) / Tools / Memory / Context. 상자 4개 높이를 맞춘다.
  - 영역 2 `.dg-zone` "Deep Agents가 미리 묶은 것" 안에 `.chip-row` 칩 4개.
  - 두 영역은 위아래로 나란히 두고 겹치거나 품지 않는다(문구 파일의 구성 그대로. 동심원 도식은 쓰지 않음).
- C3 `.is-compact`를 쓰는 이유: 기본 상자면 영역 1이 209px, 개념도 432px → 여유 15px로 기준 미달.

```html
<section id="s-55" class="scene clip" data-skill="split" data-scene-id="A09" data-start="270" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">하네스와 Deep Agents</h2>
  <p class="thesis" data-editable="true">하네스는 모델에 도구·기억·맥락을 묶는 실행 틀이다</p>
  <p class="explain" data-editable="true">Deep Agents는 LangGraph 위에 계획·파일·위임 등을 미리 묶은 하네스다. Claude Code도 구현은 다르지만 같은 역할의 실행 틀이다. 짧은 도구 호출이면 create_agent로 충분하다.</p>
  <div class="split-grid wide-left">
    <div class="dg">
      <div class="dg-zone">
        <div class="dg-zone-label" data-editable="true">하네스 · 모델을 둘러싼 실행 틀</div>
        <div class="dg-row stretch is-compact">
          <div class="dg-box accent" data-editable="true">모델</div>
          <div class="dg-box" data-editable="true">Tools<span class="dg-sub">외부 기능</span></div>
          <div class="dg-box" data-editable="true">Memory<span class="dg-sub">상태·저장소</span></div>
          <div class="dg-box" data-editable="true">Context<span class="dg-sub">지침·규칙</span></div>
        </div>
      </div>
      <div class="dg-zone">
        <div class="dg-zone-label" data-editable="true">Deep Agents가 미리 묶은 것</div>
        <div class="chip-row">
          <span class="chip" data-editable="true">작업 계획</span>
          <span class="chip" data-editable="true">파일 도구</span>
          <span class="chip" data-editable="true">긴 출력 보관</span>
          <span class="chip" data-editable="true">하위 작업</span>
        </div>
      </div>
      <p class="dg-caption" data-editable="true">개념 예시 · 교안 내용 재구성</p>
    </div>
    <div class="stack">
      <div class="code-card">
        <div class="code-title" data-editable="true">create_deep_agent 인자 · 교육용 축약(값 생략)</div>
        <pre class="code-body" data-editable="true">agent = create_deep_agent(
    model=..., tools=[...],
    subagents=[...], skills=[...],
    backend=...,
    interrupt_on={...},
)</pre>
      </div>
    </div>
  </div>
  <p class="source" data-editable="true">출처: LangChain Concepts(Agent harnesses: Deep Agents) · 4일 과정 교안 하네스 장 · 5일 과정 교안 DeepAgent 장(재구성)</p>
  <aside class="speaker-note">…문구 파일 A09 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">55 / 56</div>
</section>
```

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 900px |
| 요지 1줄 | 81 | 약 950px |
| 설명 2줄 | 109 | 줄바꿈 추정: 1줄째 "…같은 종류의 실행"까지 약 1,597px(경계, 넘으면 "실행"이 2줄째로), 2줄째 약 870–930px |
| 본문 위 간격 | 32 | CSS |
| 좌 `.dg` | 416 | 영역 1(84 + 상자 줄 109) 193 + 24 + 영역 2(84 + 칩 57) 141 + 24 + 캡션 34. 우 코드 6줄 377 |
| 출처 1줄 | 58 | 약 1,330px |
| **합계 / 여유** | **841 / 31** | 통과(C3 전제) |

- 가로: 영역 안쪽 913 − 4 − 48 = 861px. 상자 폭 (861 − 3×20)/4 ≈ 200px, 안쪽 150px(강조 148). 최장 "Context" ≈ 123px, 보조 최장 "외부 기능"·"상태·저장소" ≈ 103px → 모두 1줄. 칩 4개 ≈ 624 + 3×12 = 660px → 1줄. 영역 라벨(22px) ≈ 300–330px → 1줄.
- 코드: 줄 길이 26 / 27 / 34 / 16 / 23 / 1자 → 최장 34자 524–571px < 카드 안쪽 645px. 코드 제목 ≈ 480px → 1줄.
- 글자 크기: 72 / 40 / 32 / 28(코드·칩) → 4종.
- 강조: 모델 `.dg-box.accent` 한 곳 + 코드 5줄째 `.hl`(A10 설명과 이어지는 `interrupt_on`). 두 영역·칩은 기본색.
- 주의
  - `.stretch` 때문에 "모델" 상자는 보조 줄이 없어도 옆 상자와 같은 높이(109px)가 되고 글자는 위쪽에 놓인다. A01 v0.3의 Q·K·V와 같은 상태이며 넘침 문제는 아니다.
  - C3이 반영되지 않으면 여유 15px → 상자 보조 줄 3개("외부 기능"·"상태·저장소"·"지침·규칙")를 노트로 옮기는 문구 축소를 요청한다(상자 86px, 여유 54px). 조건부 요청 R4.
  - 상자 보조 줄이 2줄로 늘어나면 +34px로 넘친다. 보조 5자 이하를 유지한다.

## A10 · HITL: 사람 승인을 흐름에 (v0.4 배치, 신규)

- section: `scene clip` · `data-skill="steps"` · 본문 `.split-grid`(기본 1fr 1fr, 좌 808 · 우 808px) — A07과 같은 비율
- 배치 순서: eyebrow → 제목 → 요지 → 설명 → `.split-grid` [좌 `.dg` 승인 흐름 / 우 `.stack` (이미지 → 캡션)] → 출처
- 이미지: 오케스트레이터가 자른 **`assets/img/appendix/cowork-hitl-approval-card.png`**(1543×421, 승인 카드 부분)를 쓴다. 문구 파일의 전체 화면본(`cowork-hitl-approval.png`)은 쓰지 않는다(보류 V13 해소).
  - 우 칸 808px = 화면 폭의 42%(50% 이하). 가로로 긴 그림이라 크기는 폭이 정한다: 808 × 220px로 그려지고 `.split-image.h-sm`(280px) 틀 안에서 위아래 30px씩 비는 채로 가운데 놓인다. 그림 안 글자는 약 12–14px. `h-md`·`h-lg`는 틀만 커지고 그림은 커지지 않으므로 쓰지 않는다.
  - 그림은 자체 테두리·면이 있어 흰 패널에 넣지 않는다.
- 좌 개념도(흰 패널 없음, A07·A08과 같음)
  - 1행 `.dg-row`: 도구 호출 → 멈춤(`.accent`) → 사람 결정. 상자 3개 폭이 같다.
  - 2행 `div.dg-arrow` "↓"(블록, 가운데 정렬): 문구 파일은 "사람 결정 아래"라고 적었지만, 3행이 승인·거부 두 칸이라 가운데 ↓가 두 칸의 경계(= 결정이 둘로 갈림)를 가리킨다. 오른쪽 끝에 두면 거부 칸만 가리키므로 가운데에 둔다.
  - 3행 `.dg-row.stretch`: 승인(`.status-dot.ok`) / 거부(`.status-dot.warn`).
  - 캡션 `p.dg-caption` 1줄.

```html
<section id="s-56" class="scene clip" data-skill="steps" data-scene-id="A10" data-start="275" data-duration="5" data-track-index="0">
  <div class="eyebrow"><span class="block-chip" data-editable="true">부록</span><span data-editable="true">질문 대응·후속 학습</span></div>
  <h2 class="scene-title" data-editable="true">HITL: 사람 승인을 흐름에</h2>
  <p class="thesis" data-editable="true">되돌리기 어려운 도구 실행 전에 멈추고 사람의 결정으로 재개한다</p>
  <p class="explain" data-editable="true">interrupt()로 멈추고 Command(resume)로 사람의 결정을 받아 이어간다. 멈춘 상태를 저장할 체크포인터가 필요하다. CLAUDE.md나 프롬프트의 '하지 마' 문장은 이것을 대신하지 못한다.</p>
  <div class="split-grid">
    <div class="dg">
      <div class="dg-row">
        <div class="dg-box" data-editable="true">도구 호출<span class="dg-sub">모델이 요청</span></div>
        <span class="dg-arrow" aria-hidden="true">→</span>
        <div class="dg-box accent" data-editable="true">멈춤<span class="dg-sub">interrupt()</span></div>
        <span class="dg-arrow" aria-hidden="true">→</span>
        <div class="dg-box" data-editable="true">사람 결정<span class="dg-sub">resume로 재개</span></div>
      </div>
      <div class="dg-arrow" aria-hidden="true">↓</div>
      <div class="dg-row stretch">
        <div class="dg-box" data-editable="true"><span class="status-dot ok" aria-hidden="true"></span>승인<span class="dg-sub">도구 실행</span></div>
        <div class="dg-box" data-editable="true"><span class="status-dot warn" aria-hidden="true"></span>거부<span class="dg-sub">사유를 모델에</span></div>
      </div>
      <p class="dg-caption" data-editable="true">지정한 도구만 멈춤 · 결과는 다시 모델로 · 개념 예시 · 교안 내용 재구성</p>
    </div>
    <div class="stack">
      <div class="split-image h-sm"><img src="assets/img/appendix/cowork-hitl-approval-card.png" alt="사내 배포 패키지 예시 화면의 승인 카드 부분: 셸 명령 실행 승인 요청, 도구 이름과 명령, 승인·거부 버튼"></div>
      <p class="dg-caption" data-editable="true">사내 배포 패키지 예시 화면의 승인 카드 · 실행할 명령과 승인·거부 버튼 · 수강생 실습 화면 아님</p>
    </div>
  </div>
  <p class="source" data-editable="true">출처: LangGraph Human-in-the-loop 문서 · 4일·5일 과정 교안 HITL(재구성) · 현업 활용 가이드 예시 화면</p>
  <aside class="speaker-note">…문구 파일 A10 노트 전문…</aside>
  <div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>
  <div class="page-num">56 / 56</div>
</section>
```

- alt·캡션은 문구 파일 문장을 바탕으로 "승인 카드 부분"을 넣었다. 캡션의 "모델명 가림"은 자른 그림에 모델명 영역이 아예 없어 "승인 카드 부분"으로 바꾼다 → 문구 조정 요청 R2(넘침과 무관, 문구 담당 확인용).

| 요소 | 높이(px) | 근거 |
|---|---|---|
| eyebrow + 제목 1줄 | 145 | 제목 약 900px |
| 요지 1줄 | 81 | 약 1,244px |
| 설명 2줄 | 109 | 줄바꿈 추정: 1줄째 "…체크포인터가"까지 약 1,523px, 2줄째 약 1,107px |
| 본문 위 간격 | 32 | CSS |
| 좌 `.dg` | 394 | 1행 125(강조 상자) + 24 + ↓ 40 + 24 + 3행 123 + 24 + 캡션 34. 우 = 280 + 24 + 34 = 338 |
| 출처 1줄 | 58 | 약 1,000px |
| **합계 / 여유** | **819 / 53** | 통과 |

- 가로: 1행 상자 폭 (808 − 2×40 − 4×20)/3 ≈ 216px, 안쪽 166px(강조 164). 이름 최장 "도구 호출"·"사람 결정" 138px → 1줄. 보조 "interrupt()" ≈ 145px, "resume로 재개" ≈ 158px(**여유 8px, 경계**). 3행 상자 폭 394px → 1줄. 좌 캡션 ≈ 500px, 우 캡션 ≈ 710px → 1줄.
- 글자 크기: 72 / 40 / 32 → 3종(캡션·보조 24는 라벨).
- 강조: 멈춤 `.dg-box.accent` 한 곳. 상태 점 초록·주황은 DESIGN.md가 허용한 상태 표시(글자·면 채우기 아님).
- 주의
  - "resume로 재개"가 2줄로 접히면 1행이 157px가 되어 여유 21px로 기준 미달 → 1행에 C3 `.is-compact`를 붙인다(1행 141px, 여유 37px).
  - 캡션을 문구 파일의 긴 형태로 두어 2줄이 되어도 우 칸 371px < 좌 394px라 넘치지 않는다.
  - 그림 속 "쉘"(원본 표기)과 alt의 "셸"이 다르다. 그림은 원본 화면이라 고치지 않는다.
  - 카탈로그 7-4 확보 이미지 목록의 A10 항목(`cowork-hitl-approval.png`)을 `cowork-hitl-approval-card.png`로 고쳐야 한다(오케스트레이터).

---

## v0.4 넘침 점검 요약

| 장면 | 본문 구성 | 합계 | 여유(추정) | v0.3 실측 여유 | 전제 |
|---|---|---|---|---|---|
| A01 | split `.wide-left` · bullets + 원 논문 그림 2장 | 845 | 27 | 25 | R1(캡션 1줄) · C1 |
| A02 | 띠 5칸 + 3열(강조 1) | 845 | 27 | 104 | C3 |
| A03 | 3열 + 기반 띠 | 845 | 27 | 42 | C3 |
| A04 | 3열 · MCP 열 칩 줄 | 819 | 53 | 42 | (C4는 간격만) |
| A05 | `steps.row` 4카드 + 예시 줄 | 809 | 63(C5 반영 시 60) | 173 | — |
| A06 | 5칸 띠 + 캡션 | 640 | 232 | 103 | — |
| A07 | split 1fr 1fr · State 그래프 + 코드 6줄 | 846 | 26 | 신규 | — |
| A08 | split `.wide-left` · 루프 + 코드 5줄 + 칩 줄 | 842 | 30 | 신규 | 설명 2줄 |
| A09 | split `.wide-left` · 하네스 영역 2개 + 코드 6줄 | 841 | 31 | 신규 | C3 |
| A10 | split 1fr 1fr · 승인 흐름 + 승인 카드 그림 | 819 | 53 | 신규 | "resume로 재개" 1줄 |

빌드 후 확인: `validate_topic.py`, `hyperframes lint`, s-47–s-56 스냅샷. 여유 30px 이하인 A01·A02·A03·A07·A08·A09는 출처 윗선과 본문 아랫변 간격을 실측한다. A05는 C5 반영 여부, A06은 "정답 세트 검증"·"호출 흐름 기록" 줄 수, A08은 설명 줄 수와 코드 3줄째 잘림, A10은 "resume로 재개" 줄 수를 확인한다.

## CSS 요청

모두 `:root` 토큰 또는 px 값만 쓰고 색 hex를 쓰지 않는다. `#scene-styles` 끝 v0.4 블록에 추가하면 된다.

| ID | 선택자 · 속성 | 용도 · 이유 | 쓰는 장면 |
|---|---|---|---|
| C1 | `.split-image.pair { gap: 24px; }` · `.split-image.pair img { flex: 1 1 0; min-width: 0; }` | 이미지 두 장을 한 틀 안에 나란히 둔다. `.split-image`에는 폭 규칙이 없어 `.dg-row`에 두 개를 넣으면 원본 폭(445·835px)이 들어와 넘칠 수 있다. 기존 `img { width:100%; height:100%; object-fit:contain }`과 함께 두 칸이 같은 폭을 나눠 가진다 | A01 |
| C2 | (조건부) `.split-panel.is-tight { padding: 24px; }` | R1(캡션 줄이기)이 받아들여지지 않아 캡션이 2줄일 때만. 패널 82 → 50px, 여유 25px | A01 |
| C3 | `.dg-row.is-compact > .dg-box { padding: 12px 24px; }` | 한 줄 띠 상자 높이 84 → 68px(보조 줄 있으면 123 → 107). 글자 크기는 32px 그대로. 12px는 8px 배수가 아니지만 16px로는 A02·A03 여유가 19px로 기준에 못 미친다 | A02 · A03 · A09 · (A10 조건부) |
| C4 | `.compare-list + .dg-row { margin-top: 18px; }` | compare 열 안에서 목록 뒤 칩 줄의 위 간격(목록 항목 간격 18px과 같게). `.scene *`의 margin 0보다 우선한다 | A04 |
| C5 | `.steps.row .step-body { font-size: 40px; }`(현재 38px) | v0.4 요지(40)·설명(32) 층이 더해져 `steps.row` 장면의 글자 크기가 5종(72·40·38·32·28)이 된다. 38 → 40으로 요지와 맞추면 4종. 덱 전체 결정이다(S10·S16·S28 등 `steps.row` 장면 카드 높이 약 +3px). 반영하지 않으면 A05는 5종인 채로 둔다(넘침 없음) | A05 외 본문 장면 |

## 문구 축소 요청 (slide_content_writer)

| ID | 장면 · 요소 | 현재 | 목표 | 이유 |
|---|---|---|---|---|
| R1 | A01 · 그림 캡션(`.dg-caption`) | "Vaswani et al., Attention Is All You Need (2017), Figure 2 · arXiv:1706.03762" 77자(약 903px, 패널 안쪽 621px에서 2줄) | "Vaswani et al. (2017), Figure 2 · arXiv:1706.03762" 약 50자(약 575px, 1줄) | 2줄이면 여유 −7px. 문구 파일 보류 V2의 안 그대로이며 논문 제목은 출처 줄에 남아 12-1 3번(저자·연도·arXiv ID)을 지킨다. 받아들이지 않으면 C2 적용 |
| R2 | A10 · 그림 캡션·alt(문구 조정, 넘침 무관) | 캡션 "사내 배포 패키지 예시 화면 · 모델명 가림 · 수강생 실습 화면 아님" / alt "…셸 명령 실행 승인 요청과 승인·거부 버튼" | 캡션 "사내 배포 패키지 예시 화면의 승인 카드 · 실행할 명령과 승인·거부 버튼 · 수강생 실습 화면 아님"(39자, 1줄) / alt "사내 배포 패키지 예시 화면의 승인 카드 부분: 셸 명령 실행 승인 요청, 도구 이름과 명령, 승인·거부 버튼" | 자른 그림(`-card.png`)에는 모델명 영역이 없다. "승인 카드 부분"임을 알리라는 오케스트레이터 지시 반영. 문구 담당이 원래 표현을 유지해도 배치는 넘치지 않는다 |
| R3 | (조건부) A08 · 칩 줄 전체 | 캡션 + 칩 3개 | 삭제(노트에만) | 설명이 화면 3줄로 접힐 때만. 보류 V14와 같은 순서 |
| R4 | (조건부) A09 · 영역 1 상자 보조 줄 3개 | "외부 기능"·"상태·저장소"·"지침·규칙" | 삭제(노트에 이미 있음) | C3이 반영되지 않을 때만(여유 15 → 54px) |
| R5 | (조건부) A07 · 분류 상자 보조 줄 | "classify 노드" 11자 | 삭제(코드 2줄째에 `"classify"`가 있음) | 스냅샷에서 여유가 24px 미만일 때만(−39px) |

위 요청 외 화면 문구는 모두 확정본 그대로 폭·높이 안에 들어간다. 글자 크기를 줄이는 방식은 어느 장면에서도 쓰지 않았다.

## 강사 사전 검토 반영 (2026-09-16)

- #14 A08 아래 칩 줄 블록을 삭제했다(새 용어 수·사내망 웹 검색 문제, 여유 약 106px로 증가). #19 A09 코드 5줄째 `.hl` 강조를 뺐다. 그 밖의 문구 요청은 slide_copy/APP.md에 반영했고 이 문서 골격 속 같은 문구도 맞췄다(문구 문서가 기준). #1(eyebrow 본문 구간)·#7(사내 실행 가이드 통일)은 사용자 확인 보류.
