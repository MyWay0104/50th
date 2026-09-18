# TASK

## 문제 분석

`3_slide_master_v2`를 `2_slide_master`의 HyperFrames 방식에 맞춘 반복 사용형 발표자료/카드뉴스 제작 프로젝트로 완성한다. 기본 최종 산출물은 MP4가 아니라 PDF 또는 PPTX 발표자료다.

## 설계

- 기존 HyperFrames skill assets 복사
- Codex Harness 기반 subagent와 reusable skill 구성
- `new_md/DESIGN-회사이름.md` 기반 topic 생성 workflow 구성
- 16:9 deck과 card-news 선택 가능
- `overview.html` 내 Edit/Aim 수정 기능 포함
- 최종 PDF/PPTX export 전 사용자가 overview에서 수작업 수정 가능

## 구현

- [x] `.codex/skills` 이식
- [x] `.codex/agents` 구성
- [x] `.agents/skills/ppt-hyperframes-deck` 구성
- [x] `scripts/create_topic.py` 추가
- [x] `scripts/validate_codex_port.py` 추가
- [x] `scripts/validate_topic.py` 추가
- [x] README/architecture/TASK 문서화
- [x] `user_guide.md`에 새 주제 프롬프트 예시 추가
- [x] topic scaffold에 `exports/` 추가
- [x] PDF/PPTX export gate 중심으로 workflow 문서 수정
- [x] 슬라이드 단위 서브에이전트 3종 추가 (`slide_content_writer`, `slide_ui_designer`, `lecture_expert`)
- [x] LLM·Agent 내용 전문가 서브에이전트 `llm-professional` 추가 (2026-09-17). 교안 3권 제작자 관점의 개념-실습 짝 검토. 첫 사용: `sk-hynix-ai-agent-guide-edu` 재구성 로드맵(`topics/sk-hynix-ai-agent-guide-edu/ROADMAP1.md`)
- [x] `scripts/sync_overview.py` 추가: scene-styles 규약 topic의 overview 재생성, 순번 정리, 최신 여부 검사
- [x] `sk-hynix-ai-agent-guide-edu` topic v0.3 빌드 (Phase 0–4, 2026-09-14). 아래 v0.4로 대체됨. QA: `_workspace/ppt_qa_report.md`
- [x] `sk-hynix-ai-agent-guide-edu` v0.4 57장 개정 (2026-09-16, 브랜치 `feat/sk-hynix-deck-v0.4`): 막 태그·한 줄 요지·설명 문단·장면별 시각 요소, G00·A07–A10 추가, 차수 묶음마다 강사 사전·사후 검토 반영. 사용자 overview 검토·export 대기. 진행 기록: `_workspace/v0.4_progress.md`
- [x] `sk-hynix-ai-agent-guide-edu` v0.5 재구성 (2026-09-17 밤): 사내 실습 흐름에 맞춰 50장으로 재편, `ROADMAP1.md` 기준. 신규 서브에이전트 `llm-professional`과 `lecture_expert`로 빌드 전·후 검토. QA 게이트 통과. 사용자 overview 검토·export 대기. 기록: `_workspace/roadmap1/`
- [x] `sk-hynix-ai-agent-guide-edu` final-touch (2026-09-17, 브랜치 `final-touch` → main): 사용자 수정 12건(주황 테마, 구간 표시·쪽번호·시간 정보 삭제, 존댓말, 제목 간결화, 공식 출처만, 로고·아이콘). 기록: `_workspace/final_touch.md`
- [x] 교육설계 서브에이전트 `llm-edu-designer` 등록 (2026-09-18): 사용자가 만든 정의서를 저장소 현실(v0.5 55장, 원본 html·실습 코드 부재, 하우스 룰)에 맞게 보정, `.codex/agents/llm-edu-designer.toml` 계약 추가. 원본 백업 `_workspace/roadmap2/`
- [x] `sk-hynix-ai-agent-guide-edu` v0.6 실습자료 정합 (2026-09-18 새벽, `topics/sk-hynix-ai-agent-guide-edu/ROADMAP2.md`): 실제 실습자료 요약본(Part 4·실습 9개)에 맞춰 55장 → 66장(본문 49 + 구간 표지 7 + 부록 10). 확정 사실 R2-1~R2-21 → `llm-edu-designer`의 검수·스토리라인·콘티(`docs/edu-*.md`) → `llm-professional`·`lecture_expert` 교차 검수 → shrimp 작업 T1~T8(UI 사양·콘티 확정·CSS 패치·빌더 4명·조립·빌드 후 검수·반영). 전역 UI 패치(상자 테두리 대비 3:1·가운데 정렬·썸네일 모서리), 비유 축과 구간 표지, 실습 번호 일치. QA 게이트 통과. 사용자 overview 검토·export 대기. 의사결정 이력과 사내 코드 확인 요청서: `docs/handoff-inhouse-claude-lab-check.md`, 강사 진행표: `docs/instructor-runsheet.md`, 기록: `_workspace/roadmap2/`
- [ ] v0.6 후속: 사내 Claude 코드 확인 답안 반영(R2-11 장비 메모리, 검색 개수·점수 방향, 환경 파일 읽기 차단 등) · 캡처 자리표시 교체 · A10 승인 카드 그림 재캡처 · 사용자 overview patch 반영 · export

## 코드

검증 명령:

```powershell
python scripts\validate_codex_port.py
python scripts\validate_topic.py topics\_template
```

## 테스트 방법

새 topic 생성 후:

```powershell
npm run new-topic -- --name test-topic --title "테스트 발표" --company "테스트회사" --type deck
python scripts\validate_topic.py topics\test-topic
npx hyperframes lint topics\test-topic
```

## 테스트 방법 — 덱 대규모 수정 (2026-09-18 v0.7에서 자리잡은 절차)

낱말·표기를 덱 전체에서 바꿀 때는 아래 순서를 쓴다. `sk-hynix-ai-agent-guide-edu` v0.7(비유 → 전문용어 359곳)에서 검증했다.

1. **치환 표**(JSONL)를 장면 단위로 쓰고, 적용 전에 `_workspace/roadmap3/check_tables.py` 방식으로 "원문이 그 장면에 정확히 한 번 나오는지"를 센다. `apply_table.py --dry`보다 먼저 돌리면 어디가 어긋났는지까지 나온다.
2. 표로 못 덮는 자리(아이콘 `alt`·띠 라벨·`aria-label`·CSS 주석)는 **일괄 치환 스크립트**로 따로 처리한다. 반드시 표를 적용한 **뒤에** 돌린다(먼저 돌리면 표의 원문이 어긋난다). 그림 파일 개수를 치환 전후로 비교해 다르면 저장을 거부하는 안전장치를 넣는다.
3. **QA 게이트 5단계** 뒤에 **Playwright 실측**을 더한다(`browser_evaluate`로 66장의 넘침·장면밖·형제 간격·작은 글자·좌우 여백을 한 번에). `hyperframes check`는 기본 9장만 보므로 `--samples <장수>`를 준다.
4. **눈 검수를 반드시 넣는다.** 기계 지표가 전부 0이어도 세로 무게 중심·고아 줄바꿈·빈 칸은 남는다. 스냅샷을 `NN_장면ID.png`로 뽑아 UI 서브에이전트가 한 장씩 보게 한다.
5. **글자 총량과 핵심 흐름 개수**를 이전 판과 대조한다. 총량이 줄고 핵심 흐름 개수가 같으면, "지우면 안 되는 것"을 건드리지 않았다는 근거가 된다.

## 향후 개선사항

- 실제 topic별 QA report 자동 작성
- ~~screenshot 기반 overview 시각 검증~~ → v0.7에서 Playwright 실측 + 눈 검수 2갈래로 자리잡음. 스크립트화는 남음
- 치환 표 사전 검사(`check_tables.py`)를 `scripts/deck/`로 옮겨 상시 도구화
- PDF/PPTX export 자동화 스크립트 추가
- export 전 체크리스트 자동화
