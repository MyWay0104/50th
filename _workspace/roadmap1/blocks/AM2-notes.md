# AM2 블록 빌드 메모 (S09 S10 R01 S13 S14 S15 S16 S19 S17 S29 S20 S21 G03)

- 검사: `check_fragment.py` 통과(13장, ID 순서 일치). `deck-rules.json`의 forbidden_patterns(시간 표기·반말·출처·사내 정보)도 조각에 직접 적용해 0건 확인.
- G03: 지시의 `hero-tile`은 CSS가 night 전용(흰색 아이콘·night 테두리)이라 밝은 배경에서 보이지 않아, `.stats.cols-2`(11:40 / 13:20 큰 숫자) + `.dg-box`·`.dg-icon` 타일 3개 + 준비물 `.chip-row`로 대체했다. class는 `scene clip`(title-scene 아님, night 아님).
- S16: 코드 카드의 `->`는 브리프 규약대로 `-&gt;` 엔티티로 썼다(원본 S16은 raw `->`). 4번째 카드 아이콘을 bot → repeat로 바꿔 루프를 보이게 했다.
- S15: 노트의 개인 기록 문장에 "Part Finder" 이름만 덧붙였다(화면 변경 없음). S21: 데이터 상자 부제를 "기사·교육용 DB" → "기사·장비 테이블"(역할 이름)로, 출처에 Anthropic 글 추가(하네스 라벨 근거).
- S13·S19: 막힘 대체 경로는 지시대로 한 가지("준비된 저장 본문" / "준비된 조회 결과")만 두되 S19는 원본의 "옆 사람 화면" 절을 이어 붙여 유지했다.
