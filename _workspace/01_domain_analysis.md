# Domain Analysis

## 문제 분석

사용자는 앞으로 새 주제마다 별도 프로젝트처럼 발표자료 또는 카드뉴스를 만들 예정이다. 디자인 기준은 매번 `new_md/DESIGN-회사이름.md`로 제공되며, 산출물은 HyperFrames 방식으로 preview, overview edit, 최종 PDF/PPTX export까지 이어져야 한다.

성공 기준:

- `2_slide_master`의 HyperFrames skill 구조를 유지한다.
- 16:9 deck과 card-news를 사용자가 선택할 수 있다.
- topic별 스타일, 테마, 내용, 주제를 분리한다.
- `overview.html`에서 `Edit`/`Aim`으로 수정 의도를 남길 수 있다.
- 최종 파일화 전까지 사용자가 overview에서 수작업으로 충분히 수정할 수 있다.
- 기본 최종 산출물은 MP4가 아니라 PDF/PPTX 발표자료다.
- Codex Harness 방식으로 역할과 QA를 분리한다.

## 설계

선택한 패턴은 Generate-Review 파이프라인이다.

이유:

- topic마다 입력과 디자인이 달라 기획과 구현을 분리해야 한다.
- overview 검토 후 export하는 발표자료 workflow와 맞다.
- QA gate를 PDF/PPTX export 이전에 둘 수 있어 반복 수정 비용을 줄인다.

## 구현

역할:

- `topic_intake_router`: 요청, 디자인 md, 출력 타입 정리
- `ppt_content_planner`: 메시지 구조화
- `ppt_visual_designer`: 디자인 md 기반 시각 체계 수립
- `hyperframes_ppt_builder`: HyperFrames HTML 구현
- `ppt_overview_qa`: 검증과 PDF/PPTX export gate

위험:

- DESIGN markdown 누락
- deck/card-news `data-skill` 혼용
- overview edit 기능 누락
- 사용자가 preview를 확인하기 전에 PDF/PPTX export 실행
- MP4 render를 기본 최종 산출물로 오해
- 과도한 텍스트로 인한 슬라이드 overflow

## 코드

검증:

```powershell
python scripts\validate_codex_port.py
python scripts\validate_topic.py topics\<topic-name>
npx hyperframes lint topics\<topic-name>
```

## 테스트 방법

샘플 topic을 만들고 `overview.html`의 edit/aim patch 복사를 확인한다.

## 향후 개선사항

- visual regression screenshot 체크
- DESIGN markdown schema 정규화
- topic별 작업 ledger 자동 생성
- PDF/PPTX export 파이프라인 표준화
