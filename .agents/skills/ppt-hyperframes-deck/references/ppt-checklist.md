# PPT HyperFrames Checklist

## 문제 분석

- 사용자 요청이 `deck`인지 `card-news`인지 확인했다.
- DESIGN markdown 위치와 회사명을 확인했다.
- topic slug와 산출물 경로를 확인했다.

## 설계

- `deck`은 1920x1080, 16:9로 구성했다.
- `card-news`는 1080x1080 기본 규격으로 구성했다.
- 선택한 `data-skill` 값이 `AGENTS.md` 허용 목록에 있다.

## 구현

- `topics/<topic-name>/index.html` 존재
- `topics/<topic-name>/overview.html` 존재
- `topics/<topic-name>/DESIGN.md` 존재
- `topics/<topic-name>/exports/` 존재
- `meta.json`, `hyperframes.json` 존재
- `overview.html`에 `class="edit-btn"` 포함
- `overview.html`에 `Aim` 또는 `data-aim` 포함
- Done 클릭 시 클립보드 patch 복사 가능
- PDF/PPTX export 전 사용자의 overview 최종 확인 완료

## 코드

- 하드코딩된 API KEY, PASSWORD, TOKEN 없음
- 불필요한 외부 API 호출 없음
- CSS는 카드/슬라이드 텍스트가 컨테이너를 벗어나지 않도록 구성

## 테스트 방법

```powershell
python scripts\validate_topic.py topics\<topic-name>
npx hyperframes lint topics\<topic-name>
```

## 향후 개선사항

- overview screenshot 검증
- export 전 snapshot 자동 비교
