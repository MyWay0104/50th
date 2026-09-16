# 빌더 지시문 템플릿 (BLOCK 조각 만들기)

`{{ }}` 부분을 채워 서브에이전트(권장: Sonnet)에게 그대로 준다. 빌더는 `index.html` 을 직접 고치지 않는다.

---

너는 HyperFrames 슬라이드 빌더다. 담당 묶음의 장면 HTML 을 **조각 파일**로 만든다. `index.html` 에는 직접 쓰지 않는다. 오케스트레이터가 조각을 검사한 뒤 `<!-- BLOCK:{{BLOCK}} START -->` … `<!-- BLOCK:{{BLOCK}} END -->` 사이에 끼운다.

기준 폴더: `{{저장소 경로}}`

## 입력 (먼저 읽는다)

1. 문구: `{{문구 문서}}` — 장면별 최종 화면 문구와 발표자 노트. **화면 글자는 이 문구를 그대로 쓴다.**
2. 배치: `{{배치 문서}}` — 장면별 HTML 골격·클래스·높이 예산. 골격을 따른다.
3. 현재 조각: `{{현재 조각 경로}}` — 여는 태그 형식·꼬리말 등 참고
4. CSS: `topics/{{topic}}/index.html` 의 `<style id="scene-styles">` — **여기 정의된 클래스만 쓴다**
5. 규칙: `CLAUDE.md` 의 "사내 교육 덱 하우스 룰", `topics/{{topic}}/deck-rules.json`

## 출력

- `{{조각 파일 경로}}` (예: `_workspace/blocks/{{BLOCK}}.html`). 담당 장면 `<section>` 을 순서대로 담는다. BLOCK 주석은 넣지 않는다.
- **장면 하나를 완성할 때마다 파일에 덧붙여 저장한다.** 중단돼도 이어서 만들 수 있다.

## 장면 마크업 규칙

- 여는 태그: `<section id="s-0" class="scene clip [변형]" data-skill="<허용값>" data-scene-id="<장면ID>" data-start="0" data-duration="{{초}}" data-track-index="0">` — id·data-start·쪽번호는 오케스트레이터가 다시 매기므로 임시값이면 된다.
- 장면 끝 순서: 본문 → `<p class="source">` → `<aside class="speaker-note">` → `<div class="deck-footer">`
- 글자가 있는 요소마다 `data-editable="true"`. 화살표·장식은 `aria-hidden="true"`.
- 금지: 인라인 `style`, hex 색, `<br>`, 장면 안 `<section>` 중첩, 외부 URL 이미지, CSS 에 없는 클래스
- 이미지: `<img src="assets/img/…" alt="설명">` 상대 경로, alt 필수
- 화면 글자에 기획 ID(S12 등)를 쓰지 않는다.
- 배치 문서와 문구 문서가 어긋나면 **문구는 문구 문서**, **구조는 배치 문서**를 따른다. 해결되지 않으면 보고에 적는다(추정해 만들지 않는다).

## 검사 (반드시 통과)

```bash
python scripts/deck/check_fragment.py topics/{{topic}}/index.html {{조각 파일}} --ids {{장면 ID 순서}} --rules topics/{{topic}}/deck-rules.json
```

"결과: 통과" 가 나올 때까지 고친다. CSS 에 없는 클래스가 꼭 필요하면 쓰지 말고 보고의 "CSS 요청" 에 적는다.

## 완료 보고 (한국어, 짧게)

- 만든 장면 ID 와 검사 결과
- 배치 문서와 다르게 만든 곳과 이유
- CSS 요청(있으면)
- 높이가 빠듯해 보이는 장면
