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
