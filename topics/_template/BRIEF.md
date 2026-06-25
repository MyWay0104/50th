# HyperFrames v2 Template

## 문제 분석

- 출력 타입: `deck`
- 회사/브랜드: `SAMPLE`
- 디자인 원본: `C:\LSW_Coding\3_slide_master_v2\new_md\DESIGN-SAMPLE.md`
- topic 경로: `C:\LSW_Coding\3_slide_master_v2\topics\_template`

## 설계

이 topic은 `2_slide_master` 방식의 HyperFrames 구성과 v2 harness workflow를 따른다.

## 구현

- `index.html`: HyperFrames composition
- `overview.html`: 사용자 검토 및 Edit/Aim 수정 화면
- `DESIGN.md`: topic에 고정된 디자인 기준 문서

## 코드

```powershell
python scripts\validate_topic.py topics\_template
npx hyperframes lint topics\_template
```

## 테스트 방법

1. `overview.html`을 브라우저 또는 preview 서버에서 확인한다.
2. `Edit`를 누르고 수정한다.
3. `Aim`을 선택한다.
4. `Done`을 눌러 patch를 클립보드로 복사한다.

## 향후 개선사항

- 실제 발표 내용과 자료를 반영해 slide/card copy를 확정한다.
- 필요한 이미지와 도표 asset을 `assets/`에 추가한다.
