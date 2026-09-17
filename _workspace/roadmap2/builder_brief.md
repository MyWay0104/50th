# 빌더 공통 지시문 (ROADMAP2 재구성 빌드 · 2026-09-18)

당신은 `topics/sk-hynix-ai-agent-guide-edu/index.html`의 장면(`<section class="scene ...">`) 조각을 만드는 HyperFrames 슬라이드 빌더다. 저장소 루트는 `C:/Users/swl01/workspace/00_sk_hynix_only/50th`. **`index.html`·`overview.html`은 직접 고치지 않는다.** 담당 묶음의 조각 파일만 만든다. 오케스트레이터가 조각을 검사해 조립한다.

## 1. 반드시 먼저 읽을 것 (순서대로)

1. **담당 묶음의 콘티** `topics/sk-hynix-ai-agent-guide-edu/docs/edu-conti-v1-2026-09-18-part<k>.md` — 장면별 실제 표기 문안 · 비주얼 구성 · 발표자 노트(강사 스크립트). **화면 글자와 노트는 콘티를 그대로 옮긴다.** 문안을 새로 짓지 않는다. 콘티 맨 앞의 「공통 부품」(P1)과 말미의 이음매 · 넘침 메모도 읽는다.
2. `_workspace/roadmap2/conti_coordinator_decisions.md` — 콘티의 확인 질문에 대한 확정 결정. **콘티와 다르면 이 문서가 우선한다**(아이콘 파일, 클래스 이름, 채택/보류된 CSS).
3. `_workspace/roadmap2/conti_fix_log.md`(있으면) — 교차 검수 뒤 콘티에 반영된 수정 기록.
4. `_workspace/roadmap2/scenes/<장면ID>.html` — 현재 덱의 장면 원본 55개. **유지 장면은 이 파일을 그대로 복사**한다. 보강 장면은 복사한 뒤 콘티의 "현재 → 변경" 쌍만 적용한다. 재작성 · 신설 장면은 아래 3절의 "본뜰 장면"을 복사해 고친다.
5. `_workspace/roadmap2/scene-styles.css` — 쓸 수 있는 CSS 클래스 전부(2026-09-18 전역 패치 포함). **여기 없는 클래스는 쓰지 않는다.** 꼭 필요하면 쓰지 말고 완료 보고의 "CSS 요청"에 적는다.
6. `_workspace/roadmap2/slide_ui/00_global_css_patch.md`의 E절 — 구간 표지와 진행 띠의 마크업(표지 · G01 · G02 담당만).
7. `topics/sk-hynix-ai-agent-guide-edu/deck-rules.json` — 자동 검사 규칙.

## 2. 마크업 규약 (`check_fragment.py`가 검사)

- 여는 태그: `<section id="s-0" class="scene clip" data-skill="<허용값>" data-scene-id="<ID>" data-start="0" data-duration="5" data-track-index="0">`. `id` · `data-start`는 오케스트레이터가 다시 매기므로 임시값이면 된다.
- 허용 `data-skill`: `title` `title-bullets` `title-image` `title-tags` `split` `stat` `steps` `compare` `evolution-flow` `quote`. 콘티가 지정한 값을 쓴다.
- 장면 끝 순서: 본문 → `<p class="source">`(있을 때) → `<aside class="speaker-note">` → `<div class="deck-footer" data-editable="true">AI Agent Guide · SK hynix 사내 교육</div>`.
- 글자가 든 `p/h1/h2/h3/li/td/th`에는 `data-editable="true"`. `span` · `div`는 기존 장면의 패턴을 따른다. 화살표 · 장식은 `aria-hidden="true"`.
- 금지: 인라인 `style=`, `<br>`, 마크업 안 hex 색, 외부 URL 이미지, `alt` 없는 `<img>`, 장면 안 `<section>` 중첩, `class="eyebrow"` · `"page-num"` · `"act-tag"`.
- **`.dg-box`는 이제 flex 상자다.** 상자 안에서 글자와 `strong` · `b` · `code` · `em` · `a`를 한 줄에 섞으면 태그마다 줄이 끊긴다. 섞어야 하면 문장 전체를 `<span>` 하나로 감싼다. 기본 구성은 `글자 + span.dg-sub` 또는 `img.dg-icon + span + span.dg-sub`다.
- 이미지는 `assets/img/icons/*.svg`, `assets/img/logos/*`, `assets/img/b1/*`, `assets/img/common/*`, `assets/img/appendix/*`만. 아이콘 목록: book-open bot boxes brain calculator circle-help clipboard-check code cpu database door-open file-search file-text folder git-compare globe graduation-cap hand joystick key laptop layers link list-checks list-ordered lock message-square monitor network notebook-pen pencil play presentation repeat rocket search server shield-check split table terminal thermometer triangle-alert user users workflow wrench.
- **비유 아이콘은 고정**: 두뇌 `brain` · 책 `book-open` · 손발 `hand` · 조종 `joystick` · 내 PC의 에이전트 `laptop` · 적용 `rocket` · 열쇠 `key` · 문 `door-open`. 콘티가 다른 파일(`wrench` · `bot` · `monitor` · `repeat` · `terminal`)을 비유 아이콘으로 적었어도 위 파일로 바꾼다. UI 사양 E절 예시의 `repeat` · `terminal`도 `joystick` · `laptop`으로 바꾼다.
- 장면마다 시각 요소 1개 이상. 자리표시는 `.placeholder.is-spec` 안에 `[IMG-PLACEHOLDER · P-<장면ID>]` + "넣을 자료 / 조건 / 대체" 세 줄. 콘티의 자리표시 계승표대로 ID를 새 장면 ID로 바꾸되 **자리는 없애지 않는다.**
- 코드는 `.code-card > pre.code-body`에 3~8줄, `<span class="hl">` · `<span class="cm">`만. `<` · `>` · `&`는 엔티티로. "개념 예시" 표기.

## 3. 장면 유형별 규약

- **구간 표지 D01~D07**: `class="scene clip title-scene night"`, `data-skill="title"`. `div.hero-kicker`(Part 이름) + `h1.hero-title`(큰 제목. 줄을 나눌 때는 `<span class="nowrap">` 두 덩어리, `<br>` 금지) + `p.hero-sub`(실습 번호) + `ol.axis-strip`(UI 사양 E-3 마크업, 상태 배치표대로 `is-done / is-current / is-todo`, D01은 E-4의 `axis-prep` 변형) + `aside.speaker-note`(두 문장) + `div.deck-footer`. 본뜰 장면: `S01.html`.
- **실습 안내판 LAB01~LAB08(LAB04b)**: 제목 `실습 NN · <이름>`. `p.board-meta`에 "코드 위치: 실습자료 · 실습 NN". `p.explain`에 `<strong>관찰할 것</strong>` + 문장. 소단계는 `.time-blocks.is-steps.row`(또는 현 안내판과 같은 구조)의 `.time-block`(`.min` 순번, `.what` 이름, `.tb-icon`), 소단계 ≤5, 강조 소단계 하나에 `is-accent`. 바로 아래 `.chip-row`에 개념 칩. `.done-box`(완료 조건) · `.fallback`(`<strong>막히면</strong>`). 오른쪽 `.stack`에 자리표시 또는 도식. 본뜰 장면: `S08.html`(5칸) · `S13.html`(4칸) · `S19.html` · `S20.html` · `S26.html` · `S41.html`.
- **"준비" 표시(`li.axis-prep`)는 D01(`is-current`)과 G01 · G02("준비 · 01")에만 둔다.** D02~D07에는 넣지 않는다(지나온 모양이 없어 D01과 똑같이 강조돼 보인다).
- **열쇠 지도 축소판은 전 묶음 공통으로 칩 한 줄**: `.chip-row` + 맨 앞 `img.row-icon`(`key.svg`) + 칩 셋 "첫째 · 채팅용 키" / "둘째 · 임베딩용 키" / "셋째 · 데이터 조회용 토큰", 그 장면에서 쓰는 열쇠 하나만 `.chip.accent`, 꼬리 설명은 `.dg-sub` 한 마디. 기준은 콘티 part1 맨 앞 「공통 부품」이다.
- **안내판의 장면 전용 CSS**: 기존 안내판에 걸려 있던 장면 전용 규칙을 새 ID에도 복제해 두었다 — `S08` → `LAB01` · `LAB02` · `LAB03`, `S13` → `LAB04`, `S19` → `LAB04b`, `S20` → `LAB05`, `S26` → `LAB06` · `LAB07`, `S41` → `LAB08`. 그러니 **이 짝대로 본떠야** 배치가 그대로 나온다. 본뜬 장면에서 도식(예: S19의 "네 층")을 빼면 그 도식 전용 규칙은 그냥 쓰이지 않을 뿐이다.
- **개념 장면(신설 · 재작성)**: `h2.scene-title` + `p.thesis`(한 줄 요지) + `p.explain`(설명문) + 도식. 본뜰 장면: 세 열 비교는 `S17.html` · `T01.html`, 순서도는 `S16.html` · `S10.html`, 좌우 분할은 `E01.html` · `L01.html` · `V01.html`, 마무리형은 `G02.html`.
- **전환 장면 T01~T03**: 현 `T01.html`의 구조(틴트 배경 · 세 열 · 아래 띠)를 그대로 쓰고 문안만 콘티대로.
- **G01 · G02의 비유 축 띠**: `ol.axis-strip`을 밝은 배경에서 쓴다(같은 마크업). 콘티의 9열 격자(`.axis-grid`)는 CSS가 없으므로 **`axis-strip` 6칸 + 그 아래 실습 번호 칩 줄(`.chip-row`)** 로 빌드하고, "준비 · 01"은 `axis-prep` 변형으로 둔다. 넘치면 보고한다.

## 4. 문구 규약 (`qa_rules.py`가 검사)

- 화면 문장은 존댓말(…합니다/…입니다). 명사형 라벨 · 칩 · 표 칸은 그대로. 반말 평서형 "…다." 금지.
- 시각 · 분 표기 금지(G01 · G03의 기존 시각만 예외). 노트도 같다. 콘티의 "소요시간" · "메모(강사 시연 대체 가능 · 비상안)" 칸은 **화면과 노트에 옮기지 않는다.**
- 출처 줄(`p.source`)은 공식 문서와 논문만. 콘티가 적은 그대로.
- 사내 주소 · 모델명 · 키 · 테이블명 · 실제 장비 ID · 폴더/파일명 금지. 코드 위치는 "코드 위치: 실습자료 · 실습 NN" 한 가지 형식. "실습 가이드" · "해당 장" · "챗봇" · "실습 1~5" 표기는 남기지 않는다(유지 · 보강 장면에서도 콘티의 치환 쌍대로 지운다).
- 구간 코드(B1–B7) · 쪽번호 · 기승전결 표현 금지. 화면 글자에 장면 ID(S12 등)를 쓰지 않는다.

## 5. 높이 예산 (1920×1080, 안쪽 여백 상하 96px · 좌우 120px)

- 제목 1줄 + 요지 1줄 + 설명문 2줄이면 본문 영역은 약 y 400~900이다. 설명문이 3줄이 되면 도식 높이를 줄인다.
- 본뜬 장면보다 상자 수 · 줄 수를 늘리지 않는 것이 가장 안전하다. 콘티가 "넘치면 뺄 순서"를 적어 둔 장면은 그 순서를 따른다.
- 같은 행의 상자는 **줄 수를 맞춘다**(세로 가운데 정렬이라 줄 수가 다르면 아이콘 높이가 어긋난다).

## 6. 산출물과 검사

- 조각 파일: `_workspace/roadmap2/blocks/<묶음>.html`. `<section>...</section>`만 순서대로 담는다(주석 · 다른 태그 없음). **장면 하나를 끝낼 때마다 파일에 덧붙여 저장한다**(중단 대비).
- 검사(통과할 때까지 고친다):
  `python scripts/deck/check_fragment.py topics/sk-hynix-ai-agent-guide-edu/index.html _workspace/roadmap2/blocks/<묶음>.html --ids <장면 ID 순서> --rules topics/sk-hynix-ai-agent-guide-edu/deck-rules.json`
- 추가 자체 점검(Grep): 조각에 `실습 가이드` · `해당 장` · `챗봇` · `통째` · `인자 없` · `별개` · `실습 [1-5] ` 이 남아 있지 않은지, `.dg-box` 안에 글자와 인라인 태그가 섞이지 않았는지.
- 메모: `_workspace/roadmap2/blocks/<묶음>-notes.md`에 10줄 이내 — 콘티와 다르게 만든 곳과 이유, CSS 요청, 높이가 빠듯한 장면.

## 7. 완료 보고 (한국어, 짧게)

만든 장면 ID와 검사 결과 · 콘티와 다르게 만든 곳 · CSS 요청 · 높이가 빠듯한 장면.
