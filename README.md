# slide-master-v2-hyperframes

## 문제 분석

이 프로젝트는 `C:\LSW_Coding\2_slide_master`의 HyperFrames 기반 제작 방식을 유지하면서, 새 주제마다 독립된 topic 프로젝트로 16:9 발표자료 또는 카드형 뉴스를 생성하기 위한 작업 공간이다.

사용자는 새 topic을 만들 때 `new_md/DESIGN-회사이름.md`를 넣고, Codex는 해당 디자인 파일을 읽어 테마와 레이아웃 방향을 잡는다. 최종 검토는 항상 `overview.html`에서 먼저 진행하며, 사용자는 HTML 안의 `Edit`/`Aim` 기능으로 원하는 디자인 수정 사항을 바로 남길 수 있다.

기본 최종 산출물은 MP4가 아니라 발표용 `PDF` 또는 `PPTX`다. `index.html`은 PDF/PPTX export 전의 원본 슬라이드 소스이고, `overview.html`은 최종 파일화 전 수작업 검토 화면이다.

## 설계

워크플로우는 Codex Harness 방식의 Generate-Review 파이프라인이다.

```text
사용자 요청
  -> topic_intake_router
  -> ppt_content_planner
  -> ppt_visual_designer
  -> (선택) slide_content_writer / slide_ui_designer -> lecture_expert 검토
  -> hyperframes_ppt_builder
  -> ppt_overview_qa
  -> 사용자 overview 검토
  -> 사용자 Edit/Aim 수작업 수정
  -> 최종 확인
  -> PDF/PPTX export
```

`index.html`에 `<style id="scene-styles">`를 두는 topic은 `overview.html`을 손으로 복제하지 않고 `scripts/sync_overview.py`로 재생성한다. 장면 id는 순번 `s-N`, 기획 장면 ID는 `data-scene-id`, 발표자 노트는 `.speaker-note`에 둔다.

```powershell
python scripts\sync_overview.py topics\<topic-name> --renumber
python scripts\sync_overview.py topics\<topic-name> --check
```

핵심 디렉터리:

- `.codex/skills/`: `2_slide_master`에서 가져온 HyperFrames 스킬
- `.codex/agents/`: PPT/카드뉴스 제작용 Codex subagent 정의
- `.agents/skills/ppt-hyperframes-deck/`: 반복 제작 절차
- `new_md/`: 사용자가 배치하는 `DESIGN-회사이름.md`
- `topics/<topic-name>/`: topic별 HyperFrames 산출물
- `_workspace/`: 기획, 디자인, QA, harness 참조 자료
- `user_guide.md`: 새 주제 요청 프롬프트 예시와 작업 순서
- `scripts/deck/`: 묶음 단위 제작·덱 전체 수정 도구(조각 검사·조립, 치환 표 적용, 하우스 룰 검사, 본문 추출, 매핑표, 자산 로컬화)
- `templates/briefs/`: 서브에이전트 지시문 템플릿(빌더·사전 검토·마지막 검토)
- `assets/vendor/`: 글꼴·GSAP 원본. 인터넷이 막힌 환경에서 `scripts/deck/localize_assets.py` 가 topic 으로 복사한다
- `hynix-ingest-handoff.md`: 사내 반입·설치·적용 안내

## 구현

새 topic 생성:

```powershell
npm run new-topic -- --name sk-ai-agent --title "SK AI Agent" --company "SK" --type deck
```

카드뉴스 생성:

```powershell
npm run new-topic -- --name sk-card-news --title "AI 활용 뉴스" --company "SK" --type card-news
```

생성 스크립트는 `new_md/DESIGN-*.md`를 찾아 topic 폴더에 복사하고, `index.html`, `overview.html`, `meta.json`, `hyperframes.json`, `BRIEF.md`, `exports/`를 만든다.

## 코드

자주 쓰는 명령:

```powershell
npm run preview:port -- topics/<topic-name>
npm run lint -- topics/<topic-name>
npm run snapshot -- topics/<topic-name> -- --at 2.5,8.1,13.7
python scripts\validate_codex_port.py
python scripts\validate_topic.py topics\<topic-name>
```

MP4가 필요할 때만 별도로 실행한다.

```powershell
npm run render -- topics/<topic-name>
```

## 테스트 방법

1. `python scripts\validate_codex_port.py`
2. `npm run new-topic -- --name sample-deck --title "Sample Deck" --company "Sample" --type deck`
3. `python scripts\validate_topic.py topics\sample-deck`
4. `npx hyperframes lint topics\sample-deck`
5. `npx hyperframes preview topics\sample-deck --port 3000`
6. 브라우저에서 `overview.html`의 `Edit`, `Aim`, `Done` 동작 확인
7. 사용자가 최종 확인한 뒤 PDF/PPTX export 진행

## 향후 개선사항

- PDF/PPTX export 파이프라인 표준화
- overview 수정 patch를 파일로 저장하는 local helper 서버
- CI에서 harness validation과 HyperFrames lint 자동 실행
- topic별 이미지 asset 수집 자동화
