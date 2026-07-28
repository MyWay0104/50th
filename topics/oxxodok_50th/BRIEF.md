# 품격 있는 대화를 위한 지식 브리핑

## 문제 분석

- 모임: 2026년 7월 제50회 옥쏘독
- 청중: 옥쏘독 회원
- 진행 시간: 총 2시간
- 출력 타입: `deck`
- 최종 목표: PDF
- 현재 단계: 내용 입력 전 구조와 디자인 placeholder
- 현재 슬라이드 수: 14장

## 설계

`심플하게산다-독서토론.pdf`의 흐름을 기준으로 표지, 타임테이블, 각 진행 step의
챕터 전환 표지, 신규 회원 환영, 책 소개, 발제 3개, 회고, 종료 순서의 14장으로 구성한다.

타임테이블은 20분 인사, 10분 책 브리핑, 40분 독서 토론, 30분 운부장 발표,
20분 소감 순서로 운영한다.

## 구현

- `index.html`: 14장 HyperFrames composition
- `overview.html`: 슬라이드 전체 검토 및 Edit/Aim 수정 화면
- `DESIGN.md`: Nintendo.com 2001 기반 디자인 규칙
- `exports/`: 최종 PDF 위치

## 코드

```powershell
python scripts\validate_topic.py topics\oxxodok_50th
npx hyperframes lint topics\oxxodok_50th
```

## 테스트 방법

1. overview에서 14장 흐름을 확인한다.
2. Edit로 placeholder를 실제 내용으로 교체한다.
3. Aim으로 수정할 요소의 셀렉터를 복사한다.
4. 최종 확인 전에는 PDF export를 실행하지 않는다.

## 향후 개선사항

- 책 소개와 저자 정보 입력
- 발제 3개의 인용문, 페이지, 질문 입력
- 최종 소감 문구와 진행자 메모 확정
