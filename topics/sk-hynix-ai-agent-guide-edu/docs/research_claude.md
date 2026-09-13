# Claude Code 오후 강의용 공식자료 조사

확인일: 2026-09-13. 아래 링크의 Anthropic 공식 문서를 실제 열어 확인했다. **공식 기능**, **강의 설계 제안**, **사내 미검증 사항**을 구분한다. 이 문서는 조사 메모이며 최종 발표자료가 아니다.

## 1. 강의에 넣을 핵심 포인트 12개

| 우선순위 | 주제 | 강의에서 전달할 핵심 | 오전 실습과 연결 / 발표 소재 |
|---|---|---|---|
| 필수 | 1. 내가 만든 Agent와 내가 쓰는 Coding Agent | Claude Code는 모델 자체가 아니라, 모델에 파일·명령 실행 도구와 맥락 관리·실행환경을 제공하는 프로그램이다. 맥락 수집→행동→결과 확인을 반복한다. | 오전에는 Python으로 Agent의 구성 요소를 직접 연결했다. 오후에는 이미 구성된 Agent를 사용해 그 Python 프로젝트를 발전시킨다. [작동 원리](https://code.claude.com/docs/en/how-claude-code-works) |
| 필수 | 2. 왜 이번 실습에서 Claude Code인가 | 파일 탐색·여러 파일 수정·명령 실행·개발도구 연동을 한 작업 흐름에서 수행할 수 있어서 선택한다. 특정 제품이 항상 최고라는 비교 주장보다, 교육 목표에 맞는 이유를 제시한다. | 복사한 오류에 답변만 받는 장면과, 실제 파일을 읽고 수정 후 실행 결과까지 확인하는 장면을 보여준다. [개요](https://code.claude.com/docs/en/overview) |
| 필수 | 3. 로컬 실행·모델 처리·권한은 서로 다른 개념 | 로컬 세션에서는 파일/명령 작업이 내 PC에서 실행되지만, LLM 처리를 위해 네트워크로 데이터가 전송된다. 실행 가능 범위는 도구·권한·네트워크·사내 정책에 달려 있다. | `내 PC 파일 → Claude Code → 승인된 모델 경로 → 도구 결과 → 다음 행동` 그림. 계정/계약/경로에 따라 데이터 정책이 달라진다. [데이터 사용](https://code.claude.com/docs/en/data-usage), [권한](https://code.claude.com/docs/en/permissions) |
| 필수 | 4. 탐색→계획→구현→검증 | 접근법이 불확실하거나 여러 파일을 바꾸는 작업은 먼저 구조를 탐색하고 계획한다. 작은 수정까지 모든 작업을 거대한 계획으로 만들 필요는 없다. | Part Finder 경험을 ‘처음부터 완벽한 설계’보다 ‘변경하기 쉬운 경계와 작은 검증’의 교훈으로 바꾼다. [공식 모범사례](https://code.claude.com/docs/en/best-practices) |
| 필수 | 5. 좋은 요청에는 완료 조건이 있다 | 무엇을 만들지뿐 아니라 입력·기대 출력·변경 범위·확인 방법을 준다. 오류 없는 실행, 정확한 결과, 사용자의 목적 충족은 각각 확인한다. | ‘대시보드 만들어줘’→‘제공 CSV에서 장비별 건수를 보여주고 빈 파일을 안내하며 예제 입력의 합계가 12인지 확인해줘’. [공식 모범사례](https://code.claude.com/docs/en/best-practices) |
| 필수 | 6. CLAUDE.md는 반복 설명을 줄이는 프로젝트 안내서 | 실행/테스트 방법, 사내 API 이용 원칙, 프로젝트 구조, 공통 규칙을 간결하게 기록한다. 모델이 읽는 지침이며 강제 권한 설정은 아니다. | ‘숫자는 Python/SQL로 계산하고 결과 근거를 표시’, ‘테스트 데이터 위치’, ‘주요 파일의 역할’처럼 이 실습에 필요한 사실만 넣는다. [프로젝트 기억](https://code.claude.com/docs/en/memory) |
| 필수 | 7. 긴 대화가 영구 기억은 아니다 | 맥락에는 대화·파일·도구 출력이 들어간다. 길어지면 요약되며 세부 정보가 소실될 수 있다. 관련 없는 일을 분리하고 결정·미해결 사항·검증 명령을 파일로 남긴다. | `/context`, `/compact`, 새 작업으로 분리하는 원리를 소개한다. 명령 UI·동작은 교육 환경에서 재확인한다. [맥락 설명](https://code.claude.com/docs/en/context-window), [작동 원리](https://code.claude.com/docs/en/how-claude-code-works) |
| 필수(짧게) | 8. Skill은 재사용할 업무 절차 | SKILL.md에 반복 절차와 참고자료/스크립트를 묶는다. 필요할 때 읽어 사용하는 방식이다. 모델 가중치를 학습시키는 기능으로 설명하지 않는다. | ‘회의록에서 결정·근거·후속행동을 분리’, ‘CSV 품질 점검’ 같은 좁은 절차 하나가 좋다. [Skills](https://code.claude.com/docs/en/skills) |
| 선택 | 9. MCP는 외부 도구를 연결하는 표준 | DB·문서·이슈시스템 등의 기능을 Claude Code에 제공하는 연결 방식이다. 모든 업무에 필수는 아니며 기존 파일/명령 도구로 충분하면 추가하지 않는다. | 오전 SQL 함수 도구를 직접 붙인 경험과 연결한다. 도구 자체와 도구를 전달하는 연결 규약을 구분한다. 신뢰할 수 있는 사내 승인 서버, 읽기 범위, 인증을 확인한다. [MCP](https://code.claude.com/docs/en/mcp) |
| 선택 | 10. Hooks는 특정 시점에 실행하는 자동 처리 | 파일 수정 후 포맷, 작업 종료 알림 등 반복 동작을 이벤트에 연결한다. 명령 기반 hook은 모델이 기억해 실행하기를 기대하지 않고 설정된 시점에 실행한다. 모델 판단을 쓰는 hook 유형도 있다. | ‘지침에 써두기’와 ‘실제 자동 실행 설정’의 차이를 1장으로 설명한다. 설치/설정 전체 실습은 시간 여유가 있을 때. [Hooks 가이드](https://code.claude.com/docs/en/hooks-guide) |
| 선택/부록 | 11. Subagent는 범위를 나눠 맡기는 보조 작업자 | 별도 맥락에서 구체적인 하위 작업을 처리하고 결과를 돌려준다. 조사 로그가 주 대화를 채우는 것을 줄일 수 있다. 여러 개를 쓰면 비용·조정 작업도 생기므로 간단한 문제의 기본값으로 두지 않는다. | ‘이 함수의 예외 입력만 점검’, ‘이 폴더의 설정 위치만 조사’처럼 독립적인 일에 한정한다. [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 필수 | 12. 되돌릴 수 있는 작업과 운영 작업의 차이 | 변경 전후 비교와 실제 결과 확인을 습관으로 만든다. 파일 체크포인트가 DB 변경·배포·외부 API 작업까지 되돌리지는 못한다. | SQL Tool은 테스트 데이터와 읽기 권한으로 시작한다. UI가 뜨는 것은 사내 서비스 운영 준비 완료와 다르다는 점을 Part Finder 운영 경험으로 설명한다. [작동 원리의 체크포인트](https://code.claude.com/docs/en/how-claude-code-works), [보안](https://code.claude.com/docs/en/security) |

**우선순위 해석은 강의 설계 제안이다.** 제품 문서가 필수/선택을 지정한 것이 아니다. 오후 시간이 짧으면 CLAUDE.md와 Skill 하나를 실제 체험하고, MCP·Hooks·Subagent는 ‘필요할 때 찾을 지도’ 수준으로 제시한다.

## 2. 초안에서 바꿀 표현

| 기존 표현 | 권장 표현 | 구분/근거 |
|---|---|---|
| 내 로컬에 접근할 수 있다 = 내가 컴퓨터로 할 수 있는 모든 작업을 할 수 있다 | ‘허용된 파일과 명령 실행 도구를 사용해 내 PC의 많은 작업을 수행할 수 있습니다. 앱 화면 조작과 사내 시스템 접근은 별도 도구·연결·권한이 필요할 수 있습니다.’ | 공식 기능 범위. [작동 원리](https://code.claude.com/docs/en/how-claude-code-works), [권한](https://code.claude.com/docs/en/permissions) |
| 로컬에서 돌아가므로 자료가 외부로 나가지 않는다 | ‘실행 위치와 모델 처리 위치는 다릅니다. 사내에서 허용한 모델 경로와 전송 가능한 자료 범위를 먼저 이해해야 합니다.’ | 공식 로컬 데이터 흐름. [데이터 사용](https://code.claude.com/docs/en/data-usage) |
| Skill·MCP 내재화 | ‘반복 업무 절차는 Skill로 재사용하고, 다른 시스템의 기능이 필요할 때 MCP로 연결합니다.’ | 서로 다른 기능이며 모델 학습과 구별. [Skills](https://code.claude.com/docs/en/skills), [MCP](https://code.claude.com/docs/en/mcp) |
| Obsidian을 연계하면 나와 동일한 수준으로 판단하는 twin agent | ‘메모에 판단의 근거·전제·결과를 축적해 내 업무 맥락을 참고하는 보조자를 만드는 것이 장기 목표입니다. 같은 판단을 한다는 것은 별도 평가가 필요한 목표입니다.’ | 강사의 비전/추론으로 표시. Claude Code 기능이 동일 의사결정을 보장하지는 않는다. [프로젝트 기억](https://code.claude.com/docs/en/memory) |
| 기술스택 공부는 필수이고 누구나 풀스택 개발 가능 | ‘문법을 모두 외우지 않아도 작은 도구부터 만들 수 있습니다. 요구사항, 입력과 출력, 데이터 흐름, 오류, 검증, 배포의 기본을 배우면 AI가 만든 결과를 더 잘 판단할 수 있습니다.’ | 강의 설계 제안. 누구나 완성·운영을 보장하는 표현은 피한다. |
| 아키텍처를 처음부터 견고하게 짜야 한다 | ‘변하기 쉬운 부분의 경계를 먼저 나누고, 작은 기능을 검증하면서 설계를 보완하겠습니다.’ | Part Finder 경험을 일반화하는 권장 표현. 공식 모범사례는 큰/불확실한 변경의 계획을 권하며 작은 작업은 직접 수행 가능하다고 한다. [모범사례](https://code.claude.com/docs/en/best-practices) |
| Claude Code가 결과를 검증하므로 믿어도 된다 | ‘Agent에게 검증 방법을 제공하고 실제 확인 결과를 받습니다. 중요한 결과는 사람이 목적·근거·영향까지 검토합니다.’ | ‘자체 검증 가능’과 ‘정확성 보장’ 구별. [모범사례](https://code.claude.com/docs/en/best-practices), [보안](https://code.claude.com/docs/en/security) |
| 오전 vLLM API를 오후 Claude Code에서도 그대로 사용 | ‘오전의 사내 LLM API와 오후 Claude Code의 지원 모델·인증·게이트웨이는 별도 확인 대상입니다.’ | **현재 공식 문서는 게이트웨이를 통한 non-Claude 모델 라우팅을 지원하지 않는다고 명시.** 사내 비공식 호환/변환 프록시가 있는지는 미검증. [LLM 게이트웨이](https://code.claude.com/docs/en/llm-gateway) |

## 3. 현실적인 자유 실습 3가지

아래는 공식 기능에 기초한 **교육 제안**이며, 사내 환경에서 실행 검증한 완성 실습이 아니다. 예상 시간은 기본 환경 준비 후 기준이다.

### A. 가장 쉬운 트랙: CSV 업무 집계 도구 (30~45분)

- 입력: 비식별/합성 장비별 작업 기록 CSV, 미리 정한 기대 집계표.
- 과제: 장비별 건수·시간 합계·중복·누락을 점검하는 작은 Python 프로그램을 만들고 결과 CSV/HTML 보고서를 생성한다.
- 핵심 경험: 요청→파일 확인→실행→결과 비교. 수치는 Python으로 계산하고 Agent는 코드 작성과 오류 수정에 활용한다.
- 완료 기준: 기준 예제의 합계 일치, 빈 파일·잘못된 날짜·중복 행 처리, 재실행 방법 README.
- 확장: 자주 쓰는 점검 절차를 ‘데이터 품질 점검’ Skill로 정리한다.

### B. 지식자산 트랙: Obsidian용 결정 기록 정리 (30~45분)

- 입력: 공개/합성 회의 메모 Markdown 5개. Obsidian이 없어도 폴더와 Markdown 파일로 진행할 수 있다.
- 과제: 결정·근거·가정·보류사항을 일정한 양식으로 정리하고, 각 항목에 원본 파일 링크를 남긴다.
- 핵심 경험: CLAUDE.md에 작업 범위와 기록 원칙을 적고 동일 절차를 Skill로 재사용한다.
- 완료 기준: 근거 없는 새 사실을 추가하지 않음, 원본을 찾아갈 수 있음, 상충하는 내용은 확인 필요로 표시, 원본 파일 보존.
- 확장: 새로운 메모 1개를 넣어 같은 방식으로 처리되는지 확인한다. ‘나처럼 판단’보다 ‘내 판단 근거를 추적’하는 성취로 평가한다.

### C. 오전 연계 트랙: 뉴스/SQL Streamlit 앱에 기능 하나 추가 (45~60분)

- 입력: 오전에 제공한 소스코드와 합성 CSV 또는 테스트 DB.
- 과제: 출처 표시·빈 검색 결과 안내·오류 메시지 개선·CSV 다운로드 중 한 가지만 선택해 추가한다.
- 핵심 경험: 먼저 기존 파일 구조와 데이터 흐름을 설명하게 하고, 변경할 파일과 확인 방법을 계획한 뒤 구현한다.
- 완료 기준: 기존 기능 정상, 선택 기능 정상, 정상/빈 결과/연결 실패 사례 확인, 실제 화면 확인, 변경 이유 설명.
- 확장: 화면 코드는 Streamlit에, 데이터 접근과 LLM 호출은 별도 함수에 두는 작은 구조 개선. 초기 수업에서는 여러 프레임워크나 별도 프론트엔드를 추가하지 않는다.

공통 제출물은 ‘실행되는 결과 + 실행 방법 + 확인한 사례 3개 + 남은 한계’면 충분하다. 자유 주제라도 결과 범위를 작게 정해야 수강생마다 성공 경험을 만들기 쉽다.

## 4. PDF·HTML·ZIP에 배치할 정보

- **PDF**: Agent 작동 원리, 오전/오후 연결, 로컬 실행과 모델 처리의 구분, 계획/검증, Part Finder의 실제 시행착오, 확장 기능 비교표. 기능별 설치 명령 나열은 최소화한다.
- **HTML**: 설치/로그인/사내 네트워크 가이드, 교육 환경에서 확인한 버전과 검증일, 복사할 프롬프트, 오류별 확인 순서, 공식문서 링크, 선택 실습.
- **ZIP**: 작동하는 최소 예제, 합성 입력과 기대 결과, 환경설정 예시, 실행 방법, 간단한 확인용 테스트. API 키·실제 DB 계정·민감한 자료는 포함하지 않는다.

**사내에서 아직 검증하지 않은 항목**: 승인된 설치 경로, 계정 종류, 실제 모델·게이트웨이, 외부 접속/인증서/프록시, 사용 가능한 기능, MCP 허용 목록, 데이터 처리 조건. 공개 문서만으로 이를 확인했다고 말하면 안 된다.

현재 공식 개요의 Windows 설치 방식·자동 업데이트 동작은 실제 열어 확인했지만, 강의용 명령은 사내 설치 가이드와 일치하는지 확인한 뒤 HTML에 넣는 것이 좋다. [설치 개요](https://code.claude.com/docs/en/overview), [사내 네트워크 구성](https://code.claude.com/docs/en/network-config)

## 5. 공식 링크 목록

1. [Claude Code 개요](https://code.claude.com/docs/en/overview)
2. [작동 원리: 모델·도구·실행환경·체크포인트](https://code.claude.com/docs/en/how-claude-code-works)
3. [공식 모범사례: 계획·검증·맥락 관리](https://code.claude.com/docs/en/best-practices)
4. [확장 기능 비교](https://code.claude.com/docs/en/features-overview)
5. [CLAUDE.md와 auto memory](https://code.claude.com/docs/en/memory)
6. [맥락 창 설명](https://code.claude.com/docs/en/context-window)
7. [Skills](https://code.claude.com/docs/en/skills)
8. [MCP](https://code.claude.com/docs/en/mcp)
9. [Hooks 가이드](https://code.claude.com/docs/en/hooks-guide)
10. [Hooks 상세 참조](https://code.claude.com/docs/en/hooks)
11. [Subagents](https://code.claude.com/docs/en/sub-agents)
12. [권한](https://code.claude.com/docs/en/permissions)
13. [보안](https://code.claude.com/docs/en/security)
14. [데이터 사용 및 로컬/클라우드 데이터 흐름](https://code.claude.com/docs/en/data-usage)
15. [LLM 게이트웨이](https://code.claude.com/docs/en/llm-gateway)
16. [사내 네트워크 구성](https://code.claude.com/docs/en/network-config)
