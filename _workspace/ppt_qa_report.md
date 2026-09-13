# QA 보고서 — AI Agent Guide 사내 교육 덱

topic: `topics/sk-hynix-ai-agent-guide-edu/` · 작성: 오케스트레이터(ppt_overview_qa 관점) · 2026-09-14

> **상태: 사용자 overview 검토 대기.** 이 보고서의 검토는 모두 에이전트 내부 검토다. 사용자의 overview Edit/Aim 검토를 대체하지 않는다. PDF/PPTX export는 사용자 최종 확인 전까지 하지 않는다.

## 문제 분석

하루 교육 발표자용 PDF 덱 52장(본문 46: S01, G01, S02–S44, G02 / 부록 6: A01–A06)을 모두 빌드한 뒤 구조·렌더·문구를 점검했다. 오전 22장을 먼저 빌드·검토하고, 그 결과로 CSS와 규칙을 보완한 뒤 오후·부록 30장을 같은 절차로 만들었다.

## 설계

점검 축은 다섯 가지다.

| 축 | 도구 |
|---|---|
| topic 구조 | `scripts/validate_topic.py` |
| HyperFrames 문법 | `npx hyperframes lint` (0.8.36) |
| index ↔ overview 동기화 | `scripts/sync_overview.py --check`, 장면 ID 순서 비교 |
| 넘침·잘림 | Playwright로 overview의 장면별 요소 좌표를 1920×1080 기준으로 측정 |
| 화면 품질 | HyperFrames snapshot PNG 52장 육안 검수 + lecture_expert 사후 검토(오전·오후 각 1회) |
| 사실 경계 | 13항목 체크리스트(작가 대조) + 위험 표현 자동 검색 |

## 구현 — 오전 22장 결과

### 구조와 문법

| 항목 | 결과 |
|---|---|
| validate_topic.py | 통과 |
| hyperframes lint | 오류 0, 경고 2 |
| 경고 내용 | `composition_file_too_large`(727줄), `timeline_track_too_dense`(장면 22개). 모두 권고 수준. 완성 사례 `oxxodok_50th`에도 같은 종류가 있다. overview 변환 규칙이 단일 파일 장면을 전제하므로 sub-composition 분할은 하지 않고 수용한다 |
| 장면 수·순서 | index 22 = overview 22, `data-scene-id` 순서 동일, `--check` 최신 |
| 허용 data-skill | title 1, steps 3, title-tags 1, split 6, compare 7, title-bullets 3, title-image 1 (모두 허용 목록) |
| 카탈로그 밖 클래스 | 0 |
| 인라인 style · hex · `<br>` | 0 · 0 · 0 |
| 발표자 노트 | 22/22, 빈 노트 0 |
| overview 필수 요소 | `edit-btn`, Aim, `data-editable`, 클립보드 patch(템플릿 내장) 확인 |
| 애니메이션 | 트윈 0, paused 타임라인만 등록 |

### 넘침·렌더

| 항목 | 결과 |
|---|---|
| Playwright 넘침 검사 | 22장 0건 (화면 밖, 풋터 침범, 세로·가로 잘림, 상자 밖 넘침) |
| 폰트 로드 | Paperlogy 400–800, JetBrains Mono 400 로드 확인 |
| 스냅샷 | 22장 1920×1080 렌더 |

빌드 중 발견·수정한 문제:

1. **속이 빈 카드:** compare·split 격자가 남은 높이를 채워 카드가 화면 아래까지 늘어나 속이 비어 보였다(S07, S09, S15, S21 등). 격자 기본 높이를 내용에 맞추고 필요한 경우만 `.fill`로 채우게 바꿨다.
2. **코드 괄호 잘림:** 브라우저는 Consolas, HyperFrames 렌더러는 JetBrains Mono로 그려 폭이 달랐다. S12 LangChain 코드 둘째 줄의 `)`가 렌더러에서만 잘렸다. 코드 글꼴을 JetBrains Mono 웹폰트로 고정하고 해당 줄을 두 줄로 나눴다(문구 문서 동기화).
3. **G01 높이 위험:** `.stack` 안 목록이 자기 위 여백을 유지해 7px 넘칠 수 있었다. `.stack` 직계 자식의 위 여백을 없앴다.

### 사실 경계

| 항목 | 결과 |
|---|---|
| 13항목 대조 | 22장 모두 작가가 대조 결과 기록. 표현 14곳 수정 |
| 위험 표현 자동 검색(화면·노트) | 3건 검출, 모두 오해를 막는 부정·질문 문장(S04 "재학습될까요?", S10 "다시 학습시키지 않음" 등). 위반 0 |
| 사내 URL·모델명·키 | 0 |
| 근거 없는 수치·성과 | 0. 가상 데이터는 "가상 데이터" 표기(S15, S18) |
| 성격 표시 | 개념 예시·개인 기록·공개 Beta 설계 기반 개념 예시 배지 사용 |

### 강사 검토

- 사전 검토: `_workspace/lecture_review/B1-B3-pre.md` — 수정 필요 B1 3·B2 0·B3 4, 요청 W1–W10·U1 반영 완료, W11은 오후로 이월.
- 사후 검토: `_workspace/lecture_review/B1-B3-post.md` — 결과는 아래 "사후 검토 반영" 절에 기록.

## 구현 — 오후·부록 30장과 전체 52장 결과

### 구조와 문법 (전체 52장)

| 항목 | 결과 |
|---|---|
| validate_topic.py | 통과 |
| hyperframes lint | 오류 0, 경고 2 (`composition_file_too_large` 1606줄, `timeline_track_too_dense` 장면 52개 — 오전과 같은 권고, 수용) |
| 장면 수·순서 | index 52 = overview 52, 매핑표 순서와 동일, `--check` 최신 |
| 전체 길이 | `#root` 260초 = 52장 × 5초 |
| data-skill 분포 | compare 16, title-bullets 14, split 12, steps 6, title 1, title-tags 1, title-image 1, quote 1 (매핑표와 일치, 모두 허용 목록) |
| 남색 반전 | S01, G02만 |
| 구간 시각 칩 | S01, S09, S15, S22, S28, S34, S41 (구간 첫 장면 7곳) |
| 카탈로그 밖 클래스 · style · hex · `<br>` | 0 · 0 · 0 · 0 |
| 발표자 노트 | 52/52 |

### 넘침·렌더 (전체 52장)

| 항목 | 결과 |
|---|---|
| Playwright 넘침 검사 | 52장 0건 (UI 담당이 여유 19px로 경고한 A01 포함) |
| 스냅샷 | 52장 1920×1080 렌더, 오후·부록 30장 육안 검수 결함 없음 |

오후 제작 중 CSS·카탈로그 추가: `.dg-row.stretch > .dg-arrow` 세로 가운데 정렬(부록 UI 요청, S21에도 적용), `night` 장면의 `.bullets li .sub` 색(G02 보조 줄 가독성).

### 사실 경계 (전체 52장)

| 항목 | 결과 |
|---|---|
| 위험 표현 자동 검색(화면·노트, 14개 패턴) | 9건 검출, 모두 오해를 막는 부정 문장. 예: S23 "모든 일을 할 수 있다는 뜻은 아니어서", S34 "똑같이 판단하는 분신이 아니라", S36·A04 "CLAUDE.md는 권한을 강제하지 않는다". 위반 0 |
| 사내 URL·모델명·키·설치 명령 | 0 |
| 근거 없는 수치 | 0 |

### 강사 검토 (오후·부록)

- 사전 검토: `_workspace/lecture_review/B4-B7-pre.md` — 수정 필요 B4 2·B5 2·B6 3·B7 1, 부록 2. 요청 W21–W30과 UI 문구 축소 4건(S39 넘침 필수 포함) 반영 완료. B7 마무리에 중심 메시지가 없던 문제를 G02 노트로 해결.
- 사후 검토: `_workspace/lecture_review/B4-B7-post.md` — 결과는 아래 "사후 검토 반영 (오후·부록)" 절에 기록.

## 코드

```powershell
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --renumber
python scripts\sync_overview.py topics\sk-hynix-ai-agent-guide-edu --check
python scripts\validate_topic.py topics\sk-hynix-ai-agent-guide-edu
npx hyperframes lint topics\sk-hynix-ai-agent-guide-edu
npx hyperframes snapshot topics\sk-hynix-ai-agent-guide-edu --at 2.5,7.5,12.5 --no-end
```

## 테스트 방법 — 아침 사용자 검토

1. `topics/sk-hynix-ai-agent-guide-edu/overview.html`을 브라우저로 연다(이미지 자산이 없어 파일로 열어도 된다).
2. 좌측 썸네일로 장면을 넘기며 문구·순서를 확인한다.
3. 고칠 문구는 `Edit` → 수정 → `Done`으로 patch를 복사해 agent에 전달한다.
4. 특정 요소 지적은 `Aim`으로 셀렉터를 복사해 전달한다.

## 사용자 확인 목록 (오전)

| ID | 내용 | 영향 장면 |
|---|---|---|
| P1 | 실습 1의 "최신 자료 질문"을 B2 실습 기사와 같은 주제로 준비할 수 있는지 | S08, S09 |
| P2 | 기사 실습이 코드가 정한 순서로만 동작하는지, SQL 실습에서 모델이 도구 호출 여부를 고르는지 | S17, S22 |
| P3 | 사내 환경의 임베딩 지원과 실습의 임베딩 검색 사용 여부 | S10 |
| P4 | Streamlit 실습 화면 캡처(입력·처리 중·결과 영역 크롭) | S20 |
| P5 | 수업 전 필수 확인: S08 준비 출력, 질문별 검색 단계 유무, 저장 본문, DB 읽기 권한·교육용 DB, 모델 tool calling 지원, 오후 Claude Code 모델 경로 | S08, S13, S19, S21, S22 |
| — | `[강사명]`, `[교육일]` 자리표시 | S01 |
| — | 실습 가이드 실제 장 이름·앵커 ("실습 가이드 해당 장"으로 표기 중) | S08, S13, S19, S20 |
| — | S04 실제 토크나이저 결과, S07 실측 출력, S06·S12 실제 실습 코드로 교체할지 | S04, S06, S07, S12 |

작가 보류 목록 원문: `_workspace/slide_copy/B1.md`, `B2.md`, `B3.md` 각 파일 끝.

## 사용자 확인 목록 (오후·부록)

| ID | 내용 | 영향 장면 |
|---|---|---|
| Q1 | 수강생 PC에 Claude Code가 미리 설치·로그인됐는지, Python 실행 허용, 화면 조작 도구 연결, 파일 수정·명령 실행 전 승인 설정 | S23, S26, S32 |
| Q2 | "검색 결과 없음 안내"가 오전 앱에 이미 구현됐는지, 대체 과제 시작 코드와 "준비된 결과"가 있는지 | S24, S25, S28, S32 |
| Q3 | 실습 폴더가 Git 저장소이고 diff를 볼 수 있는지 (아니면 S31 "Git diff" → "바뀐 줄 비교") | S31, S32 |
| Q4 | 준비된 Skill·짧은 원문·대체 요청문·검토 전후 예시가 실습 가이드에 있고 미리 실행해 봤는지 | S37, S38 |
| Q5 | 16:00–16:20 휴식 없이 자유 실습을 시작하는 안을 확정하는지 (두면 S41–S43과 G01 시각 수정) | G01, S41–S43 |
| Q6 | 자유 실습에 실제 사내 데이터를 쓸 수 있는지, 가상 CSV와 정답표가 있는지 | S39, S41 |
| Q7 | 실제 실습 코드의 화면·조회·모델 호출 구조 (별도 백엔드가 있는 판본이면 S29 수정) | S29 |
| P2·P5 | 오전 항목과 같음: 모델의 도구 호출 선택 여부, 오후 Claude Code 모델 경로 | S22, S23, S26, A03, A05 |
| N1 확장 | 자리표시 "실습 가이드 해당 장/자유 실습 장"이 오후 6곳(S26, S32, S37, S41–S43)에도 있음 | 오후 안내판 |
| N2 확장 | G02 eyebrow "B7 · 자유 실습과 Q&A"를 그대로 둘지 (G01의 "B1"과 같은 방식으로 결정) | G02 |

작가 보류 목록 원문: `_workspace/slide_copy/B4.md`–`B7.md`, `APP.md` 각 파일 끝. 부록 보류(식 칩 표시, 메타데이터 예시, 사내 MCP·Hook 허용 등)는 `APP.md` 끝.



## 향후 개선사항

- 넘침 검사 코드를 저장소 스크립트로 옮겨 반복 실행할 수 있게 한다.
- 실제 화면 자산이 들어오면 스냅샷과 넘침 검사를 다시 한다.

## 사후 검토 반영 (오전)

lecture_expert가 스냅샷 PNG 22장을 모두 열어 판정했다. 파일: `_workspace/lecture_review/B1-B3-post.md`.

| 차수 | 수정 필요 | 내용 |
|---|---|---|
| B1 | 1 | 9번 가독성: S06 라벨 2줄 접힘(T1), G01 세로선 위치(C2), S04 제목–카드 간격(C1) |
| B2 | 1 | 9번 가독성: S10·S14 제목–카드 간격(C1) |
| B3 | 2 | 5번 실습 전환: S20 가이드 표기 누락(T2) / 9번 가독성: S16·S17 간격(C1) |

4건(T1, T2, C1, C2) 모두 반영하고 재검증했다. 사전 검토 요청 W1–W10·U1이 화면에 반영된 것도 사후 검토에서 확인됐다. 빌드 중 변경(카드 높이, JetBrains Mono, S12 줄 나눔)은 교육적으로 문제없다고 판정됐다.

반영 후: validate 통과, lint 오류 0, 넘침 22장 0건.

사용자 확인 목록 추가:

| ID | 내용 |
|---|---|
| N1 | export 전에 반드시 채울 자리표시: S01 `[강사명]`·`[교육일]`, 실습 안내판 4장의 "실습 가이드 해당 장", S20 이미지 자리 |
| N2 | G01 하루 시간표 위의 eyebrow "B1"을 그대로 둘지 |

## 사후 검토 반영 (오후·부록)

lecture_expert가 오후·부록 30장과 S21(오전 연결)의 스냅샷 PNG를 모두 열어 판정했다. 파일: `_workspace/lecture_review/B4-B7-post.md`.

| 대상 | 수정 필요 | 내용 |
|---|---|---|
| B4 | 0 | — |
| B5 | 0 | — |
| B6 | 0 | — |
| B7 | 1 | G02 "고른다" 보조 줄 "정해진 작업 흐름"이 S17 용어 "Workflow"와 다름(T21) |
| 부록 | 0 | A03 사전 검토 지적(W30)이 화면에 해소됨 |

화면으로 확인된 사항:

- 사전 검토 요청 W21–W30과 UI 문구 축소 4건이 화면 또는 발표자 노트에 반영됨.
- 빌드 확인 항목 통과: S26 단계 3은 1줄, S32·S37 막히면 상자는 각 2줄.
- 오후 실습 안내판(S26, S32, S37, S41–S43)이 오전 안내판(S08, S13, S19, S20)과 같은 구조. S41–S43의 다음 단계 시각은 파랑 큰 숫자 칸으로 멀리서도 읽힘.
- 오전의 제목–카드 간격 결함(C1)이 재발하지 않음. 사전 검토에서 빠듯하다던 S24·S34·S39·S42도 여유 있게 들어감.
- S44 → G02가 하루를 닫고, 중심 메시지 문장(W28)이 G02 발표자 노트에 있음.

T21을 반영하고 재검증했다: validate 통과, lint 오류 0, `sync_overview.py --check` 최신, 넘침 52장 재검사.

## 최종 상태 요약

| 항목 | 상태 |
|---|---|
| 장수 | 52장 (본문 46 + 부록 6) |
| 구조·문법 | validate 통과, lint 오류 0 (권고 경고 2) |
| 동기화 | index·overview 52장 일치, `--check` 최신 |
| 넘침 | 52장 0건 |
| 사실 경계 | 자동 검색 위반 0, 13항목 대조 완료 |
| 강사 검토 | 오전·오후 각각 사전·사후 검토 완료, 수정 요청 전부 반영 |
| 남은 일 | 사용자 overview 검토 → 사용자 확인 목록 답변·자리표시 교체 → 실제 화면 자산 교체 → 최종 확인 후 PDF/PPTX export |
