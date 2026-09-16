# AM1 빌드 노트 (S01 G01 G00 S02 E01 S04 S07 L01 S08)

- G01·S08: 소단계 5개를 한 줄에 두려고 `.time-blocks.is-steps.row`에 `.time-band`(flex 한 줄)를 함께 썼다. 4열 grid로는 5번째 블록이 다음 줄로 밀리고, 2행이면 S08 높이(1080)를 넘기 때문. 새 CSS 없이 기존 클래스 조합으로만 해결.
- G01: 좌우 두 열 대신 오전 띠·오후 띠 두 줄 전폭으로 배치(3열 grid에서 2행째 첫 블록 앞에 화살표가 남는 문제 회피). 번호는 하루 순서 1–8 연속.
- S08: `p.source`(vLLM Reproducibility)는 높이 때문에 생략(브리프 허용). `.what` 라벨은 한 줄 유지를 위해 "환경·첫 호출 / system 바꾸기 / temperature 3회 / 럭키비키 긍정봇 / 최신 자료 질문"으로 줄였다.
- E01: 도식 상자 글자를 3층 이름 중심으로 줄였고(코드 카드는 S06의 model/base_url 두 줄 재사용, LangChain 로고는 뺌), 참여 질문·API·SDK·LangChain·사전 과제·content+토큰 언급은 노트에만 두었다.
- 검사: check_fragment 통과, deck-rules 정규식(시간·반말·출처·사내 정보) 자체 스캔 0건, 1920×1080 렌더에서 넘침·출처 겹침 없음(로컬 미리보기로 확인).
