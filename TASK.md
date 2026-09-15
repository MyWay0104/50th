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
- [x] `scripts/sync_overview.py` 추가: scene-styles 규약 topic의 overview 재생성, 순번 정리, 최신 여부 검사
- [x] `sk-hynix-ai-agent-guide-edu` topic 52장 빌드 (Phase 0–4, 2026-09-14). 사용자 overview 검토·export 대기. QA: `_workspace/ppt_qa_report.md`
- [x] `sk-hynix-ai-agent-guide-edu` v0.4 57장 개정 (2026-09-16, 브랜치 `feat/sk-hynix-deck-v0.4`): 막 태그·한 줄 요지·설명 문단·장면별 시각 요소, G00·A07–A10 추가, 차수 묶음마다 강사 사전·사후 검토 반영. 사용자 overview 검토·export 대기. 진행 기록: `_workspace/v0.4_progress.md`

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

## 향후 개선사항

- 실제 topic별 QA report 자동 작성
- screenshot 기반 overview 시각 검증
- PDF/PPTX export 자동화 스크립트 추가
- export 전 체크리스트 자동화
