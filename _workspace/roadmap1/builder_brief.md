# 빌더 공통 지시문 (ROADMAP1 재구성 빌드 · 2026-09-17)

당신은 `topics/sk-hynix-ai-agent-guide-edu/index.html`의 장면(`<section class="scene ...">`) 조각을 만드는 빌더다. 문구(화면 글자·발표자 노트)와 마크업을 함께 만든다. 저장소 루트는 `C:/Users/swl01/workspace/00_sk_hynix_only/50th`.

## 반드시 먼저 읽을 것

1. `topics/sk-hynix-ai-agent-guide-edu/ROADMAP1.md` — 0절 결정 기록, 2-1 원칙, **2-2 새 흐름의 담당 구간 표**, 2-5 자산. 여기 적힌 개념·관찰·완료 조건·참여 질문을 그대로 구현한다.
2. `_workspace/roadmap1/review_llm_professional.md`, `review_lecture_expert.md` — 담당 장면에 대한 보강안(개념 칩, 용어 3개 제한, 명칭 교정, 참여 질문).
3. `_workspace/roadmap1/user_lab_flow.md` — 실습의 실제 순서.
4. `_workspace/roadmap1/scenes/<ID>.html` — 현재 덱의 장면 원본 57개. **유지 장면은 이 파일을 그대로 복사**하고, 보강 장면은 이 파일을 고친다. 새 장면도 비슷한 성격의 기존 장면을 본떠 만든다(예: 개념 장면은 S06·S10·S16, 실습 안내판은 S08·S13·S20, 표지형은 S01, 마무리형은 G02).
5. `_workspace/roadmap1/scene-styles.css` — 쓸 수 있는 CSS 클래스 전부. **여기 없는 클래스는 쓰지 않는다.** 인라인 style도 금지.
6. `topics/sk-hynix-ai-agent-guide-edu/deck-rules.json` — 자동 검사 규칙. `forbidden_patterns`의 정규식에 걸리면 QA에서 실패한다.

## 마크업 규약 (check_fragment.py가 검사)

- `<section id="s-0" class="scene clip" data-skill="<허용값>" data-scene-id="<ID>" data-start="0" data-duration="5" data-track-index="0">`. `id`·`data-start`는 나중에 `sync_overview.py --renumber`가 다시 매기므로 임시값이면 된다. 표지형은 `class="scene clip title-scene night"`처럼 기존 장면의 class를 그대로 따른다. 남색 반전(`night`)은 S01·G02에만.
- 허용 `data-skill`: `title`, `title-bullets`, `title-image`, `title-tags`, `split`, `stat`, `steps`, `compare`, `evolution-flow`, `quote`.
- 필수 요소: `h2.scene-title`, `aside.speaker-note`(발표자 노트 4~7문장, 강사 말투 존댓말), `div.deck-footer`(내용 `AI Agent Guide · SK hynix 사내 교육`).
- 글자가 든 `p/h2/h3/li/td/th`에는 모두 `data-editable="true"`. `span`·`div`는 기존 장면 패턴을 따른다.
- 금지: 인라인 `style=`, `<br>`, 마크업 안 hex 색, 외부 URL 이미지, `alt` 없는 `<img>`.
- 이미지는 `assets/img/icons/*.svg`, `assets/img/logos/*`, `assets/img/b1/*`, `assets/img/common/*`, `assets/img/appendix/*`만. 아이콘 목록: book-open bot boxes brain calculator circle-help clipboard-check code cpu database file-search file-text folder git-compare globe graduation-cap hand key layers link list-checks list-ordered lock message-square monitor network notebook-pen pencil play presentation repeat rocket search server shield-check split table terminal thermometer triangle-alert user users workflow wrench. 로고: anthropic claude git github jupyter langchain obsidian openai python sqlite streamlit vllm(png) youtube.
- 장면마다 시각 요소 1개 이상(`.dg` 도식, `.steps`, `.compare-grid`, `.time-blocks`, `.placeholder.is-spec` 자리표시, 이미지). 자리표시는 `[IMG-PLACEHOLDER · P-<ID>]` 형식과 "넣을 자료 / 조건 / 대체" 세 줄.
- 코드는 `.code-card > pre.code-body`에 3~6줄 이내, `<span class="hl">`·`<span class="cm">`만 사용. `<`·`>`·`&`는 엔티티로.

## 문구 규약 (qa_rules.py가 검사)

- **화면 문장은 존댓말**(…합니다/…입니다). 명사형 라벨·칩·표 칸은 그대로. 반말 평서형 "…다."는 금지.
- **시간 표기 금지**: `09:00` 같은 시각, `10분` 같은 분 표기는 G01·G03에서만. 다른 장면과 노트에서는 "먼저·이어서·다음 구간" 같은 순서 표현.
- **출처 줄**(`p.source`)은 공식 문서·논문만. 교안(4일·5일·handbook), "근거:", 개인 기록, 사내 가이드는 적지 않는다. 출처가 없으면 `p.source`를 생략해도 된다.
- **사내 정보 금지**: 사내 주소·모델명·키·사내 라이브러리 실제 이름·`llmops`·`localhost`·`gpt-4`·현업 가이드 파일명. 역할 이름으로 쓴다: "사내 추론 서버", "사내 모델 운영 페이지", "사내 데이터 조회 라이브러리", "실습 가이드 해당 장".
- 구간 코드(B1–B7)·쪽번호·기승전결 표현 금지. `class="eyebrow"`, `class="page-num"`, `class="act-tag"` 금지.
- 코드 위치는 "코드 위치: <역할 이름> — 실습 가이드 해당 장" 형식(`p.guide-ref` 또는 `p.board-meta`).
- 사실 경계: 근거 없는 수치·성과 금지. 개인 사례는 "개인 기록", 공개 Beta는 "공개 Beta 설계 기반 개념 예시". 사내 실데이터 테이블은 화면에 테이블명·실제 값 대신 역할 이름과 가상 예시 값(교육용 가상 데이터 표기).

## 실습 안내판 규약 (실습 1~5)

- 제목 `실습 N · <이름>`. `p.board-meta`에 코드 위치, `p.explain`에 `<strong>관찰할 것</strong>` + 2문장.
- 소단계는 `.time-blocks.is-steps.row` 안의 `.time-block`(`.min`에 순번 숫자, `.what`에 3~8자 이름, `.tb-icon`). 소단계 ≤5. 강조할 소단계 하나에 `is-accent`.
- **개념 칩**: 소단계 바로 아래 `.chip-row`에 `.chip`으로 "① 환경 · 세 층" "② 역할 · system"처럼 소단계 번호 + 직전 개념 이름을 붙인다. 이것이 "코드만 치고 개념은 모르는" 상태를 막는 장치다.
- `.done-box`(완료 조건 1개), `.fallback`(`<strong>막히면</strong>` 대체 경로 1개). 오른쪽 `.stack`에 자리표시 또는 도식.
- 발표자 노트는 소단계 순서대로 무엇을 하고 무엇을 관찰하는지, 그리고 이 실습이 직전 개념 어디와 짝인지 말한다.

## 산출물

- 담당 블록의 장면을 **지정된 순서대로 한 파일**에 이어 붙여 `_workspace/roadmap1/blocks/<블록>.html`로 저장한다. 파일에는 `<section>...</section>`만 있고 다른 태그·주석은 없다.
- 저장 후 반드시 검사한다: `python scripts/deck/check_fragment.py topics/sk-hynix-ai-agent-guide-edu/index.html _workspace/roadmap1/blocks/<블록>.html --ids <ID 순서> --rules topics/sk-hynix-ai-agent-guide-edu/deck-rules.json`. "결과: 통과"가 나올 때까지 고친다.
- 검사 결과와 함께, 로드맵과 다르게 정한 곳(있다면)과 이유를 `_workspace/roadmap1/blocks/<블록>-notes.md`에 5줄 이내로 적는다.
- index.html·overview.html은 직접 수정하지 않는다.
