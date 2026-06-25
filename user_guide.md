# User Guide

## 문제 분석

이 프로젝트는 새 주제마다 발표자료를 만들기 위한 작업 공간이다. 최종 목표는 기본적으로 `PDF` 또는 `PPTX` 발표자료이며, MP4 영상은 선택 사항이다.

핵심 파일 역할:

- `new_md/DESIGN-회사이름.md`: 새 주제에 적용할 디자인 가이드 원본
- `topics/<topic-name>/DESIGN.md`: 해당 topic에 고정 복사된 디자인 기준
- `topics/<topic-name>/index.html`: 발표자료 원본 슬라이드 소스
- `topics/<topic-name>/overview.html`: 최종 파일화 전 수작업 검토와 Edit/Aim 수정 화면
- `topics/<topic-name>/exports/`: 최종 PDF/PPTX 파일 위치

## 설계

작업 시퀀스는 다음 순서로 이해하면 된다.

```text
1. DESIGN.md 파일을 new_md/에 넣기
2. Codex에게 새 주제 요청하기
3. Codex가 topic 폴더와 HTML 슬라이드 원본 생성
4. overview.html로 전체 슬라이드 검토
5. 사용자가 Edit/Aim으로 최대한 수작업 수정
6. Codex가 수정 patch를 index.html과 overview.html에 반영
7. 최종 확인
8. PDF 또는 PPTX로 export
```

`overview.html`은 최종 파일이 아니다. PDF/PPTX로 만들기 전, 사용자가 직접 수정하고 최종 형태를 확인하는 작업 화면이다.

## 구현

디자인 파일은 아래 폴더에 넣는다.

```text
C:\LSW_Coding\3_slide_master_v2\new_md\DESIGN-airbnb.md
```

다른 회사나 테마라면 파일명만 바꾼다.

```text
C:\LSW_Coding\3_slide_master_v2\new_md\DESIGN-삼성.md
C:\LSW_Coding\3_slide_master_v2\new_md\DESIGN-단기매매.md
C:\LSW_Coding\3_slide_master_v2\new_md\DESIGN-회사이름.md
```

이 디자인 파일은 전역 고정값이 아니다. 새 topic을 만들 때 Codex가 선택해서 읽고, 해당 topic 안에 `DESIGN.md`로 복사해 기준으로 삼는다.

## 코드

### 프롬프트 예시: 주식 단기매매 방법

```text
C:\LSW_Coding\3_slide_master_v2 프로젝트에서 새 발표자료를 만들어줘.

주제: 주식 단기매매 방법
topic 폴더명: stock-short-trading
최종 목표: PDF 또는 PPTX 발표자료
디자인 기준: new_md/DESIGN-airbnb.md
출력 형식: 16:9 발표 슬라이드덱
슬라이드 수: 10장
청중: 주식 초보자
톤: 실전적이지만 과장 없이, 리스크를 명확히 경고하는 교육용

반드시 지킬 것:
1. MP4 영상이 아니라 PDF/PPTX 발표자료 export를 최종 목표로 둘 것
2. 먼저 DESIGN-airbnb.md를 읽고 디자인 토큰과 레이아웃 원칙을 요약할 것
3. topics/stock-short-trading/ 아래에 topic을 만들 것
4. topic 안에 DESIGN.md, index.html, overview.html, meta.json, hyperframes.json, exports/를 둘 것
5. overview.html에는 Edit 버튼과 Aim 선택 기능을 포함할 것
6. PDF/PPTX로 파일화하기 전까지 overview.html에서 내가 수작업으로 수정할 수 있게 할 것
7. 내가 overview를 최종 확인하기 전에는 PDF/PPTX export를 하지 말 것
8. MP4 render는 하지 말 것
9. 투자 수익을 보장하는 표현은 쓰지 말고, 손실 가능성과 리스크 고지를 포함할 것
```

### 프롬프트 예시: overview 수정 반영

`overview.html`에서 `Edit`를 누르고 문구를 수정한 뒤 `Done`을 누르면 patch가 클립보드에 복사된다. 그 내용을 Codex에게 이렇게 전달하면 된다.

```text
방금 overview.html에서 수정한 patch를 붙여넣을게.
이 내용을 topics/stock-short-trading/index.html과 overview.html에 반영해줘.
아직 PDF/PPTX export는 하지 말고, 다시 overview 확인 상태까지만 만들어줘.

<여기에 클립보드 patch 붙여넣기>
```

### 프롬프트 예시: 최종 export 요청

overview를 충분히 수정하고 최종 확인한 뒤에만 요청한다.

```text
topics/stock-short-trading overview 최종 확인 완료.
이제 발표용 PDF와 PPTX로 export해줘.

출력 위치:
topics/stock-short-trading/exports/

파일명:
stock-short-trading.pdf
stock-short-trading.pptx
```

## 테스트 방법

새 topic 생성 후 Codex가 확인해야 할 기본 검증:

```powershell
python scripts\validate_codex_port.py
python scripts\validate_topic.py topics\stock-short-trading
npx hyperframes lint topics\stock-short-trading
```

사용자가 확인할 것:

- `overview.html`에서 전체 흐름이 발표자료처럼 읽히는가
- `Edit` 버튼이 동작하는가
- `Aim` 선택으로 수정 의도가 남는가
- 긴 문장이 슬라이드 안에서 잘리지 않는가
- PDF/PPTX로 만들기 전에 최종 형태가 충분히 다듬어졌는가

## 향후 개선사항

- PDF/PPTX export 자동화 스크립트 추가
- overview patch를 `topics/<topic-name>/feedback.md`에 자동 저장
- topic 생성 시 디자인 md를 더 정교하게 파싱
- export 전 슬라이드별 스크린샷 QA 추가
- PPTX 변환 시 텍스트 박스, 이미지, 폰트 매핑 규칙 표준화
