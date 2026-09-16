# 사내 반입·적용 안내 (hynix-ingest-handoff)

사외에서 만든 발표자료 제작 방식을 **사내에서 똑같이** 쓰기 위한 인계 문서다. 2026-09-17 기준.

- 이 문서를 사내 Claude Code 에 읽히면 "무엇을 설치하고, 어떤 순서로 만들고, 무엇으로 검증하는지"를 그대로 따라 할 수 있다.
- 사람이 할 일은 **반입 심사·설치·보안 확인** 세 가지다(3·11·12절).
- 방향은 한쪽이다. **규칙과 도구는 밖에서 안으로 가져가고, 사내 자료는 밖으로 내보내지 않는다.**

---

## 0. 먼저 해 보기 (이 순서로 시작한다)

준비물을 미리 다 갖추지 말고, 아래를 그대로 해 본 다음 막히는 곳만 해결한다.

```bash
git clone <사내 Git 주소 또는 사외 저장소> slide-master
cd slide-master
npm ci                                   # 실패하면 3절
pip install -r requirements.txt          # 실패하면 3절 (이미지 작업을 안 하면 건너뛰어도 된다)
npx --no-install hyperframes doctor      # Node·Chrome 만 ✓ 면 충분
npx --no-install hyperframes check topics/sk-hynix-ai-agent-guide-edu --samples 3
```

마지막 명령이 `Check passed` 면 준비 끝이다. 바로 5절로 가서 새 발표자료를 만든다.
막히면 **10절 "자주 나는 문제"** 를 먼저 보고, 그래도 안 되면 3절(오프라인 묶음)로 간다.

---

## 1. 무엇을 가져가나

| 항목 | 내용 | 용량 | 비고 |
|---|---|---|---|
| 저장소(틀) | 스킬 70여 개(`.codex/skills`), 에이전트 정의(`.claude/agents`·`.codex/agents`), 제작 도구(`scripts/`), 템플릿 주제, 디자인 파일(`new_md/`), 지시문 템플릿(`templates/briefs/`), 규칙 문서 | git pack 약 7 MB | 클론 한 번으로 끝 |
| 글꼴·스크립트 | Paperlogy 5종 + JetBrains Mono + GSAP 3.12.5 (`assets/vendor/`) | 약 0.9 MB | 저장소에 포함. **라이선스 확인 필요**(9절) |
| npm 패키지 | `hyperframes` 0.8.41 고정 + 의존성 | 수백 MB(node_modules) | 사내 미러 또는 오프라인 묶음 |
| Python 패키지 | `PyMuPDF`(이미지 작업용, 선택) | 수십 MB | `requirements.txt` |
| 브라우저 | 사내 표준 Chrome | — | 새로 받지 않아도 됨. `doctor` 로 확인 |

가져가지 **않는** 것: Playwright 브라우저(690MB), 외부 MCP 서비스(Context7 등), 사내 자료가 들어간 주제 폴더.

---

## 2. 사외에서 이미 끝난 일 (이 저장소에 반영됨)

- [x] 제작 도구 7종을 `scripts/deck/` 로 승격 (아래 6절)
- [x] 하우스 룰을 `CLAUDE.md` + `topics/<topic>/deck-rules.json` 으로 고정, 자동 검사 가능
- [x] 제작 절차를 `.agents/skills/ppt-hyperframes-deck/SKILL.md` 에 갱신(묶음 루프·치환 표·마지막 검토·운영 원칙)
- [x] 서브에이전트 지시문 템플릿 `templates/briefs/` 3종
- [x] CDN 글꼴·GSAP 를 로컬 파일로 전환(외부 참조 0건 확인)
- [x] `hyperframes` 0.8.41 고정 + `package-lock.json`
- [x] `requirements.txt`

## 3. (선택) 인터넷·미러가 막혔을 때만: 오프라인 묶음

사내에서 `npm ci` 와 `pip install` 이 되면 이 절은 건너뛴다. 막힐 때만 사외에서 아래를 만들어 반입한다.


```bash
# 1) 오프라인 npm 묶음 — 사내와 같은 OS/아키텍처(Windows x64)에서 실행
npm ci                      # node_modules 생성(네이티브 바이너리 포함)
tar -czf node_modules.tgz node_modules

# 2) 오프라인 pip 묶음
pip download -r requirements.txt -d wheels

# 3) 저장소 묶음 (사내 Git 이 없을 때)
git bundle create slide-master.bundle --all
```

반입할 파일: `slide-master.bundle`(또는 사내 Git push), `node_modules.tgz`, `wheels/`.
사내 npm 미러가 있으면 1번은 생략하고 사내에서 `npm ci` 를 바로 돌려도 된다.

---

## 4. 사내 설치 순서

```bash
# 1) 저장소
git clone <사내 Git 주소> slide-master        # 또는: git clone slide-master.bundle slide-master
cd slide-master

# 2) Node 패키지 (둘 중 하나)
npm ci                                        # 사내 미러가 있을 때
tar -xzf ../node_modules.tgz                  # 오프라인 묶음을 가져왔을 때

# 3) Python 패키지
pip install --no-index --find-links ../wheels -r requirements.txt

# 4) 환경 점검
npx --no-install hyperframes doctor
```

`doctor` 에서 이것만 확인하면 된다.

- ✓ Node.js 20 이상, ✓ Chrome 발견
- ✗ FFmpeg·Docker·whisper·TTS 는 **없어도 된다**(MP4 를 만들 때만 필요)

### 설치 검증 (이 4개가 통과하면 준비 끝)

```bash
python scripts/validate_topic.py topics/<topic>
npx --no-install hyperframes check topics/<topic> --samples 3
python scripts/deck/qa_rules.py topics/<topic> --rules topics/<topic>/deck-rules.json
python scripts/sync_overview.py topics/<topic> --check
```

기대 결과(사외에서 확인한 값): `Topic validation passed` · `Check passed`(레이아웃 0건, 명암비 54/54 AA) · `위반 0건` · `최신 상태`.

---

## 5. 새 발표자료 만드는 순서

```bash
# 1) 주제 만들기
npm run new-topic -- --name <slug> --title "<제목>" --company "<회사>" --type deck

# 2) 인터넷이 막힌 환경이면 자산 로컬화 (글꼴이 바뀌면 줄바꿈·넘침이 전부 달라진다)
python scripts/deck/localize_assets.py topics/<slug>
python scripts/deck/localize_assets.py topics/<slug> --check   # 외부 참조 0 확인

# 3) 하우스 룰 파일 복사
cp topics/sk-hynix-ai-agent-guide-edu/deck-rules.json topics/<slug>/deck-rules.json
```

그다음은 `.agents/skills/ppt-hyperframes-deck/SKILL.md` 의 절차를 따른다. 요약하면 이렇다.

```text
계획 → (묶음마다) 문구 → 배치 → 강사 사전 검토 → 조각 빌드 → 조립 → QA 게이트 → 강사 사후 검토
     → 전체 QA → 마지막 검토(시각 2 + 내용 1) → 문서 정리 → 사용자 overview 검토 → export
```

덱 전체를 한 번에 고칠 때(존댓말 전환, 시간 정보 삭제처럼 가로 방향 작업)는 장면을 다시 만들지 말고 **치환 표**를 쓴다.

---

## 6. 제작 도구 (`scripts/deck/`)

| 스크립트 | 하는 일 | 예시 |
|---|---|---|
| `check_fragment.py` | 조각을 index 에 끼우기 전 검사 | `python scripts/deck/check_fragment.py topics/<t>/index.html blocks/B2.html --ids S09 S10 --rules topics/<t>/deck-rules.json` |
| `splice_blocks.py` | BLOCK 구간 교체·추출 | `python scripts/deck/splice_blocks.py topics/<t>/index.html blocks B2 B3` |
| `apply_table.py` | 치환 표 적용(**항상 `--dry` 먼저**) | `python scripts/deck/apply_table.py topics/<t>/index.html copy_B1.jsonl --kind copy --dry` |
| `qa_rules.py` | 하우스 룰 검사 | `python scripts/deck/qa_rules.py topics/<t> --rules topics/<t>/deck-rules.json` |
| `dump_deck_text.py` | 검토용 본문·노트 추출 | `python scripts/deck/dump_deck_text.py topics/<t> -o _workspace/<t>-text.md` |
| `scene_map.py` | 장면 매핑표 생성 | `python scripts/deck/scene_map.py topics/<t> -o _workspace/scene-map.md` |
| `localize_assets.py` | CDN 자산 로컬화 | `python scripts/deck/localize_assets.py topics/<t>` |

### 치환 표 형식 (JSON Lines, 한 줄이 한 장면)

```json
{"sid": "S09", "title": "새 제목", "source": "출처: Anthropic, Building effective agents", "replace": [{"where": "screen", "old": "원문 그대로", "new": "새 문구"}, {"where": "note", "old": "…", "new": "…"}]}
```

- `title`·`source` 는 생략하거나 `null` 이면 그대로, `source` 가 `""` 면 출처 줄을 지운다.
- `old` 는 **그 장면 안에서 정확히 한 번** 나와야 한다. HTML 태그를 가로지르면 안 된다.
- 배치 표는 `{"sid": "...", "old": "<div …>", "new": "<div …>"}` 형식에 `--kind visual` 로 적용한다.
- `--dry` 결과의 "못 찾음"은 **이미 적용됐거나 원문이 다르다**는 뜻이다. 표는 한 번만 적용한다.

---

## 7. 서브에이전트 구성

| 역할 | 정의 파일 | 지시문 템플릿 |
|---|---|---|
| 문구 담당 | `.claude/agents/slide_content_writer.md` | `templates/briefs/review-pre.md` 참고 |
| 배치 담당 | `.claude/agents/slide_ui_designer.md` | — |
| 강사 검토 | `.claude/agents/lecture_expert.md` | `templates/briefs/review-pre.md`, `review-final.md` |
| 조각 빌더 | 일반 에이전트(Sonnet 권장) | `templates/briefs/builder.md` |

운영 원칙(사용 한도 대비): 동시 실행 3–4개, 장면마다 결과 파일에 덧붙여 저장, 위험한 작업 전 커밋, 진행 상태는 `_workspace/<주제>_progress.md` 표로.

---

## 8. MCP 판단

| MCP | 사내에서 | 대체 |
|---|---|---|
| Playwright | 선택 | `hyperframes check`(레이아웃·명암비) + `hyperframes snapshot`(스크린샷) |
| 작업 관리(shrimp) | 선택 | `_workspace/<주제>_progress.md` 진행 표 |
| Context7 | **쓰지 않음** | 외부 서비스라 사내 정보 유출 위험. 공식 문서 확인은 사외에서 미리 |
| supabase·shadcn 등 | 불필요 | 사내 `.mcp.json` 에서 제외 |

---

## 9. 보안·라이선스 확인 (사람이 판단)

- **저장소 분리**: 틀(규칙·도구)은 사외, **사내 자료가 들어간 주제는 사내 저장소에만** 둔다. 현재 사외 저장소에는 `topics/sk-hynix-ai-agent-guide-edu` 가 있고 그 안에 사내 배포 패키지 승인 카드 그림이 있다. 공개 여부를 확인하고, 필요하면 사내로 옮긴다.
- **글꼴 라이선스**: Paperlogy·JetBrains Mono 를 사내 배포 자료에 쓸 수 있는지 확인한다. 쓸 수 없으면 `assets/vendor/fonts/` 를 사내 승인 글꼴로 바꾸고 `index.html` 의 `@font-face` 이름만 맞춘다.
- **로고·아이콘**: 출처와 라이선스는 `topics/<topic>/assets/img/LICENSES.md` 에 정리돼 있다(Simple Icons CC0, Lucide ISC, 상표는 각 회사 소유).
- **외부 전송 금지**: 사내 문구·캡처를 외부 서비스(웹 검색, 외부 MCP)로 보내지 않는다.
- **export 게이트**: PDF/PPTX 는 사용자가 overview 최종 확인을 말한 뒤에만 만든다.

---

## 10. 자주 나는 문제

| 증상 | 원인·해결 |
|---|---|
| 글꼴이 달라 보이고 줄바꿈·넘침이 사외와 다르다 | 자산 로컬화를 안 했다. `localize_assets.py` 실행 후 `--check` 로 외부 참조 0 확인 |
| `npm ci` 가 실패한다 | `sharp`·`onnxruntime-node` 같은 네이티브 패키지를 미러가 막는다. 오프라인 `node_modules.tgz` 를 쓴다 |
| `hyperframes` 명령을 못 찾는다 | `npm ci` 를 먼저 하거나 `npx --no-install hyperframes …` 로 부른다 |
| `check` 가 경고 9건을 낸다 | 같은 아이콘을 한 장면에서 여러 번 쓴 경우와 파일 길이 경고다. **영상 렌더용 권고라 덱 출력에는 영향이 없다** |
| 치환 표에서 "못 찾음"이 많다 | 이미 적용된 표를 다시 돌렸거나 원문이 바뀌었다. `--dry` 로 확인하고 표를 다시 만든다 |
| 장면을 더하거나 뺐다 | `sync_overview.py --renumber` 로 순번·쪽번호를 다시 매긴다 |
| Chrome 을 못 찾는다 | 사내 표준 Chrome 설치 경로를 확인하고 `hyperframes doctor` 로 다시 본다 |

---

## 11. 반입 심사용 목록

| 소프트웨어 | 버전 | 출처 | 라이선스 | 용도 |
|---|---|---|---|---|
| hyperframes | 0.8.41 | npm | 패키지 라이선스 확인 | 덱 lint·검사·미리보기·스냅샷 |
| Node.js | 20 이상 | 사내 표준 | — | 위 CLI 실행 |
| Python | 3.11 이상 | 사내 표준 | — | 제작·검사 스크립트 |
| PyMuPDF | 1.24 이상 | PyPI | AGPL/상용 | 논문 그림 추출 등 이미지 작업(선택) |
| Paperlogy / JetBrains Mono | — | 글꼴 배포처 | **확인 필요** | 덱 글꼴 |
| GSAP | 3.12.5 | cdnjs | 표준 무료 라이선스 확인 | 장면 타임라인 |
| Simple Icons / Lucide | 13 / 0.460.0 | npm | CC0 / ISC | 로고·아이콘 |

---

## 12. 완료 기준

사내 PC에서 **인터넷을 끊고** 아래가 모두 통과하면 사외와 같은 품질로 만들 수 있다.

- [ ] `npx --no-install hyperframes doctor` — Node·Chrome ✓
- [ ] `python scripts/validate_topic.py topics/<topic>` — passed
- [ ] `npx --no-install hyperframes check topics/<topic>` — Check passed
- [ ] `python scripts/deck/qa_rules.py topics/<topic> --rules topics/<topic>/deck-rules.json` — 위반 0건
- [ ] `python scripts/sync_overview.py topics/<topic> --check` — 최신 상태
- [ ] `npx --no-install hyperframes snapshot topics/<topic> --at 4,9,14 -o snapshots/test` — PNG 생성
- [ ] `overview.html` 을 브라우저로 열어 Edit/Aim 동작 확인

## 13. 참고 문서

| 문서 | 내용 |
|---|---|
| `CLAUDE.md` | 저장소 규칙, 제작 도구, QA 게이트, 사내 교육 덱 하우스 룰 |
| `AGENTS.md` | 저장소 작업 규칙 원본 |
| `.agents/skills/ppt-hyperframes-deck/SKILL.md` | 제작 절차(묶음 루프·치환 표·마지막 검토) |
| `_workspace/final_touch.md` | 실제 개정 사례: 요청 12건을 57장에 반영한 기록 |
| `_workspace/ppt_qa_report.md` | QA 결과와 사용자 확인 목록 |
| `topics/sk-hynix-ai-agent-guide-edu/` | 완성된 예시 덱 57장(사내 이관 여부는 9절 참고) |
