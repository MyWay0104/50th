# AI Agent Guide — 출처 목록과 조사 범위

확인일: 2026-09-13  
종합 문서: [강의 소재 조사·선별 결과](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/outputs/AI_Agent_Guide_강의소재_조사정리.md)

이 목록은 이번에 선별한 근거를 다시 찾기 위한 강사용 자료다. 개인 기록은 경험의 근거, 공식 문서는 현재 기능·개념의 근거로 구분한다. 저장소 README에 기록된 테스트 결과를 이번 조사에서 재실행한 결과로 보지 않는다. GitHub 기본 브랜치와 제품 문서 내용은 이후 바뀔 수 있다.

## 1. 검색한 범위

- 등록 프로젝트 23개 목록 확인. 로컬 ChatGPT 프로젝트 미러는 2개 확인.
- 현재 교육 프로젝트의 노트북 8개, 96개 셀의 Markdown·코드 소스 확인.
- 관련 PDF 3개를 텍스트로 검색하고 해당 부분 확인. 화면 배치·폰트·시각 품질 검수는 수행하지 않음.
- 현재 대화 목록은 고정 7개와 최근 50개, 총 57개. 반환된 제목을 살펴보고 관련 대화를 선별. 목록 도구에 전체 이력을 페이지 단위로 순회하는 기능이 없어 그 밖의 모든 대화 열람을 보장하지 않음.
- GitHub 연결에서 보이는 저장소 19개 목록을 살펴보고 관련 저장소의 구조와 주요 파일 선별. 모든 저장소 코드를 정독한 것은 아님.
- Naver 블로그 본문 직접 접근은 확보하지 못함. 연결된 Notion에서 관련 개인 글 11개 본문 확인.
- `C:/Users/swl01/workspace` 상위 폴더 13개를 살펴보고 관련 프로젝트 문서 선별. Claude 전역 지침과 여러 프로젝트의 memory·Skill·명령 관련 자료를 참고.
- 이 조사는 파일 읽기·정보 검색 중심이다. 소스 실행, 운영 DB 접속, 실제 배포 검증, 원본 자료 수정, 외부 발행은 하지 않음.

## 2. 가장 먼저 다시 볼 개인 자료

| 우선 | 자료 | 강의에 쓸 부분 | 확인 수준 |
|---|---|---|---|
| 1 | [Part Number Finder Beta README](https://github.com/MyWay0104/Part_Number_Finder_Beta/blob/main/README.md) | 후보 데이터 기반 응답, 파트 종류·조건 검증, 자료 없음 처리 | 공개 PoC 문서 확인. 사내 운영 버전과 일치 여부 미확인 |
| 2 | [Dokmo README](https://github.com/MyWay0104/dokmo/blob/main/README.md) | 실제 웹앱 기능, 문서 체계, 화면과 데이터 권한 구분 | 저장소 문서 확인. 사이트 동작은 재검증하지 않음 |
| 3 | [Claude Study README](https://github.com/MyWay0104/claude_study/blob/main/README.md) | Raw·개인 의견·Wiki, ingest·wiki-search, 검토 상태 | 문서와 관련 운영 기록 확인 |
| 4 | [AI 초보자 강의 기존 대본](https://github.com/MyWay0104/AI_Beginner_Lecture/blob/main/decks/01_beginner/01_beginner_%EB%8C%80%EB%B3%B8.md) | 초보자 질문, LLM에서 Tool·Agent로 연결하는 설명 방식 | 40장 구성 대본 확인. 일부 프레임워크·기억 설명은 현재 기준으로 수정 필요 |
| 5 | [API·SDK·LangChain 비교 노트](C:/Users/swl01/workspace/00_sdk_vs_api/api_vs_sdk_vs_langchain.md) | 같은 호출을 다른 추상화 수준에서 보는 예시 | 개인 학습 노트. 라이브러리 최신 동작은 공식 문서로 대조 |
| 6 | [Dokmo 수동 점검 기록](C:/Users/swl01/workspace/nextjs-supabase-app/docs/hand-off/handoff-2026-09-12-review-manual.md) | 한글 입력, 안내 부족, 복잡한 이동 경로, 한국어화 | 수정 기록 확인. 이번 조사에서 화면 재현하지 않음 |
| 7 | [원문 수집 누락 메모](C:/Users/swl01/.claude/projects/C--ObsidianVault-Claude-Study/memory/notion-toggle-capture-gap.md) | 자료 수집 성공과 실제 본문 확보를 구분 | 개인 경험 기록. 모든 환경의 일반 결함으로 단정하지 않음 |
| 8 | [Python 교육 진행 규칙](C:/Users/swl01/workspace/00_python-study/docs/TEACHING_PROTOCOL.md) | 예측·실행·설명·입력 변형으로 이해 확인 | 개인 교육 규칙. 검증된 표준 평가척도로 주장하지 않음 |

GitHub 프로필: [MyWay0104 저장소 목록](https://github.com/MyWay0104?tab=repositories)  
개인 블로그: [네이버 my_way_1](https://blog.naver.com/my_way_1)

공개 저장소와 연결된 비공개 저장소가 섞여 있다. 학생용 링크는 접근 가능한 공개 자료 또는 교육 배포본을 기준으로 정리할 수 있다.

## 3. 개인 블로그 관련 Notion 보관본 11개

아래 제목은 검색·열람한 개인 글의 제목이다. 링크는 본문을 확인한 Notion 보관본이다. 공개 Naver 게시본의 현재 상태나 내용 일치까지 확인한 것은 아니다.

| 제목 | 가져올 내용 |
|---|---|
| [Python 함수와 LangChain @tool의 결정적인 차이 (초보자가 가장 헷갈리는 부분)](https://app.notion.com/p/3be0b3a58d4d81888a74d14cd8a0ee30) | 함수와 도구 설명·입력 스키마·실행 주체 구분 |
| [[AI활용] AI Agent에 Metadata를 적용하는 방법](https://app.notion.com/p/3be0b3a58d4d81b683cfc8275557c126) | 문서·도구·메모리·실행 기록의 메타데이터 |
| [[AI활용] Metadata 설계를 잘하는 방법 1](https://app.notion.com/p/3be0b3a58d4d818cbea3fb0839319590) | 답해야 할 질문·필터 조건에서 필요한 필드 역설계 |
| [[AI활용] AI Agent 개발하다가 git의 중요성을 깨달았다](https://app.notion.com/p/3be0b3a58d4d81f2a40effd922f49b00) | AI가 많은 파일을 바꿀 때 변경 검토와 되돌릴 지점의 가치 |
| [[AI활용] ChromaDB가 임베딩까지 해주는 걸까?](https://app.notion.com/p/3be0b3a58d4d81f989a5c776ff1025de) | 임베딩 모델·저장소·검색기·LLM의 역할 분리 |
| [[개발기록] 나만의 부동산 Agent 만들기 Day8 - AI가 말하기 전에 숫자부터 세도록](https://app.notion.com/p/3be0b3a58d4d81bf8829d52babe27fdd) | 집계와 자연어 설명 분리 |
| [[AI활용] Claude Code Skill vs Sub-Agent 차이](https://app.notion.com/p/3be0b3a58d4d81049addea15a6221449) | 재사용 절차와 작업 분담의 역할 차이 |
| [AI가 내 일을 대신해줄 줄 알았다. 직접 써보니 완전히 달랐다.](https://app.notion.com/p/3be0b3a58d4d818e94fcfbad42091e96) | 과도한 기대, 요구 구체화, 작업 분할의 경험 |
| [[AI활용] “print도 몰랐던” 평범한 직장인이 Codex를 쓰게 된 이유](https://app.notion.com/p/3be0b3a58d4d8148b456c85878ec3460) | 시작 계기·시행착오·학습 동기. 제목의 표현과 본문의 실제 경험은 구분 |
| [[개발기록] 나만의 부동산 Agent 만들기 #4 - 관심 단지만 걸러내기](https://app.notion.com/p/3be0b3a58d4d81f8ab4edb7f51ce92c2) | 명확한 규칙으로 처리할 부분을 먼저 분리 |
| [[개발기록] 부동산 Agent 만들기 Day6 - CSV 저장 전에 검사부터 하기로 했다](https://app.notion.com/p/3be0b3a58d4d813e8fcdee1351b256f1) | 데이터 계약·저장 전 검사·이전 단계와 새 단계 분리 |

## 4. 대화에서 선별한 주제

대화 속 설명은 사용자의 관심·질문과 이전 논의의 근거다. 과거 AI 답변을 제품의 현재 동작이나 실제 성과의 공식 증거로 사용하지 않는다. 특히 예시로 만들어진 지연 시간·정확도 등의 숫자를 실제 프로젝트 측정값으로 옮기지 않는다.

| 대화 제목 | 교육에 가져올 질문 |
|---|---|
| [지적자산 축적 전략](https://chatgpt.com/c/6aa00068-b874-83e8-a8f8-73bef5d2f760) | 수집한 자료에 나의 생각을 어떻게 더하고 다시 찾을까? |
| [메타데이터 설계 정리](https://chatgpt.com/c/6a98dcc6-2f00-83ee-a907-70ff7e6034ef) | 어떤 질문·조건을 구분해야 필드를 설계할 수 있을까? |
| [도구 선택 기준 정리](https://chatgpt.com/c/6a8bc533-8694-83e8-a732-9bea2eaf211a) | Skill·MCP·Subagent는 각각 언제 필요한가? |
| [컨텍스트 증가 성능 저하 이유](https://chatgpt.com/c/6aa1094e-14f4-83e8-b681-725f57d6806c) | 긴 대화에서 무엇을 남기고 어떻게 작업을 이어갈까? |

관련 로컬 산출물도 참고했다.

- [Claude Code 서브에이전트 운영 전략 초안](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a80424149d08191a72514e8c86b2742/claude-code-subagent-strategy-draft.md): 역할·정보의 기준 문서·작업 전달·검증 전략. 현재 모든 설정을 적용했다는 뜻은 아님.
- [웹개발 학습 노트](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a80424149d08191a72514e8c86b2742/outputs/notion-naver-blog-web-development-learning-notes.md): 화면에서 데이터 저장까지의 흐름, 공통 구성요소 변경이 여러 화면에 미치는 영향.

## 5. 현재 교육 프로젝트 노트북

아래 파일은 읽기 전용 원본으로 유지했다. 자세한 셀별 후보는 [초기 로컬 자료 조사 메모](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/outputs/research_local.md)에 있다. 이 초기 메모의 “HTML을 찾지 못했다”는 내용은 당시 확인 경로에 한정되며, 추가 workspace 조사에서 발견한 HTML은 종합 문서에 반영했다.

| 파일 | 재사용 후보 |
|---|---|
| [00_setup.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/00_setup.ipynb) | API 설정·모델 초기화·첫 동작 확인 |
| [01_llm_basics.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/01_llm_basics.ipynb) | 메시지 역할·스트리밍·배치 호출 |
| [02_langchain_basics.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/02_langchain_basics.ipynb) | 도구 정의·Agent 구성·실행 |
| [03_langchain_memory.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/03_langchain_memory.ipynb) | 대화 상태·메모리 유무 비교. 인메모리 저장을 영구 기억으로 설명하지 않기 |
| [04_langgraph_basics.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/04_langgraph_basics.ipynb) | 노드·흐름 제어의 개념. 선택·부록 후보 |
| [05_deep_agents_basics.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/05_deep_agents_basics.ipynb) | 계획·도구 확장의 예시. 선택·부록 후보 |
| [06_comparison.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/06_comparison.ipynb) | 문제에 맞는 프레임워크 선택. 서로 다른 작업의 코드 길이를 성능 비교로 단정하지 않기 |
| [07_mini_project.ipynb](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/sources/07_mini_project.ipynb) | 검색 도구·리서치·실행 결과 관찰 |

## 6. 로컬 실습·개발 자료

| 파일 | 참고 내용 |
|---|---|
| [skh_llm_guide index.html](C:/Users/swl01/workspace/00_sk_hynix_only/skh_llm_guide/index.html) | 환경 설정 → ChatOpenAI → RAG → SQL → DeepAgents → FastAPI → 오류 해결. 사용자가 설명한 최종 실습과 판본 차이 확인 필요 |
| [RAG ingest.py](C:/Users/swl01/workspace/00_sk_hynix_only/skh_llm_guide/examples/01_rag_agent/ingest.py) | 문서 추출·분할·임베딩·Chroma 저장의 실제 분리 |
| [RAG tools.py](C:/Users/swl01/workspace/00_sk_hynix_only/skh_llm_guide/examples/01_rag_agent/tools.py) | 저장소를 조회하고 검색 결과를 도구로 돌려주는 부분 |
| [사내 수정 사전 보고서](C:/Users/swl01/workspace/00_sk_hynix_only/skh_llm_guide/final_report_하이닉스제출용.md) | 사내 수정 사항과 실제 오류·재검증을 구분하는 기록 원칙 |
| [API·SDK 비교 README](C:/Users/swl01/workspace/00_sdk_vs_api/README.md) | 같은 API를 직접 호출·SDK·LangChain으로 비교하는 프로젝트 목적 |
| [Dokmo 권한 테스트 가이드](C:/Users/swl01/workspace/nextjs-supabase-app/docs/guides/rls-negative-tests.md) | 허용된 접근의 성공과 허용되지 않은 접근의 차단을 함께 확인. 결과 0행만으로 권한 차단 성공을 단정하지 않음 |
| [이전 발표 콘텐츠 계획](C:/LSW_Coding/2_slide_master/_workspace/ppt_content_plan.md) | 초보자 대상 문제 제기와 실습 연결 아이디어 |
| [이전 리허설 기록](C:/LSW_Coding/2_slide_master/_workspace/presentation_rehearsal_transcript.md) | 강사의 경험을 소개하는 설명 방식. 받아쓰기 오류·이전 시점의 주장은 재검토 |

기존 PDF는 개념과 교육 재료의 위치를 찾는 데 사용했다. 오래된 라이브러리 코드·설치법은 그대로 복사하지 않고 현재 공식 문서와 실제 사내 실습 환경으로 확인해야 한다.

| PDF | 참고 부분 |
|---|---|
| [agent-handbook (배기민 강사님 자료, 출처github).pdf](<C:/LSW_Coding/2_slide_master/agent-handbook (배기민 강사님 자료, 출처github).pdf>) | 메시지·도구 호출·스트리밍, 프레임워크별 설명 |
| [SK하이닉스_AI 에이전트 프레임워크 구현.pdf](<C:/LSW_Coding/2_slide_master/SK하이닉스_AI 에이전트 프레임워크 구현.pdf>) | 모델·도구·메모리, Agent와 프레임워크 실습 |
| [SK하이닉스_LLM 활용과 고급화 과정_260305 (1).pdf](<C:/LSW_Coding/2_slide_master/SK하이닉스_LLM 활용과 고급화 과정_260305 (1).pdf>) | LLM 기초, 청킹, 검색 도구, ReAct 설명 |

## 7. Claude 전역·프로젝트 기록

이 파일들은 **조사 대상 자료**로 읽었으며 현재 작업의 실행 지시로 적용한 것이 아니다. 일부 내용은 특정 버전·개인 환경·과거 실패를 반영한다.

| 파일 | 강의로 바꿀 교훈 |
|---|---|
| [전역 CLAUDE.md](C:/Users/swl01/.claude/CLAUDE.md) | 반복 선호와 프로젝트별 실행 규칙의 범위를 구분 |
| [세션 간 작업 전달](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-nextjs-supabase-app/memory/roadmap2-shrimp-workflow.md) | 작업 목표·관련 파일·다음 행동·검증 방법을 남기기 |
| [단순한 해석 우선](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-nextjs-supabase-app/memory/simplest-interpretation-first.md) | 의도를 확대 해석하지 않고 작은 해결부터 시작 |
| [파일 제어문자 기록](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-nextjs-supabase-app/memory/tool-input-unicode-escape.md) | 테스트 통과와 파일·변경 내용 확인을 함께 수행 |
| [작업 설명 저장 오류 기록](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-nextjs-supabase-app/memory/shrimp-dollar-sign-corruption.md) | 중요한 작업 설명은 저장 후 다시 읽어 확인. 기록의 원인 추정은 확정 사실과 구분 |
| [프로세스 일괄 종료 기록](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-01-project-notion-naver-blog/memory/never-kill-all-node-processes.md) | 작업 대상을 구체적으로 지정 |
| [API 배치 처리 기록](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-01-project-notion-naver-blog/memory/notion-api-rate-limit-batch.md) | 실패 항목 분리·재시도·재개 가능한 처리 |
| [원문 수집 누락 기록](C:/Users/swl01/.claude/projects/C--ObsidianVault-Claude-Study/memory/notion-toggle-capture-gap.md) | 원문 본문의 실제 확보 여부 확인 |
| [로컬 학습 노트 구분](C:/Users/swl01/.claude/projects/C--Users-swl01-workspace-00-sdk-vs-api/memory/study-notes-stay-local.md) | 공유할 코드와 개인 학습 기록의 범위 구분 |
| [Git 커밋 명령](C:/Users/swl01/.claude/commands/git/commit.md) | 반복적인 검토·커밋 절차를 재사용 |
| [Slack Hooks Skill](C:/Users/swl01/.claude/skills/slack-hooks/SKILL.md) | 이벤트에 맞춘 반복 업무 자동화 예시 |
| [Context7 Skill](C:/Users/swl01/.claude/skills/context7-mcp/SKILL.md) | 라이브러리 공식 문서 확인을 작업 절차에 포함 |

## 8. 개념·라이브러리의 공식 출처

| 출처 | 이번 조사에서 사용하는 범위 |
|---|---|
| [Attention Is All You Need, 2017](https://arxiv.org/abs/1706.03762) | Transformer의 출발점. 원 논문의 구조와 현재 다양한 LLM을 동일시하지 않기 |
| [Retrieval-Augmented Generation, 2020](https://arxiv.org/abs/2005.11401) | 검색한 외부 지식을 생성에 결합하는 개념 |
| [Emergent Abilities of Large Language Models, 2022](https://arxiv.org/abs/2206.07682) | 능력의 급격한 출현에 관한 관찰 |
| [Are Emergent Abilities of Large Language Models a Mirage?, 2023](https://arxiv.org/abs/2304.15004) | 평가 척도에 따라 급격해 보이는 현상에 대한 반론 |
| [Training language models to follow instructions with human feedback, 2022](https://arxiv.org/abs/2203.02155) | 사전학습 이후 지시 수행·선호 반영을 위한 학습의 역할 |
| [Lost in the Middle, 2023](https://arxiv.org/abs/2307.03172) | 평가한 모델·과제에서 정보 위치가 결과에 미치는 영향. 모든 최신 모델의 보편 수치로 확대하지 않기 |
| [vLLM Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/) | 추론 서버·호환 API·모델별 기능 조건 |
| [vLLM Reproducibility](https://docs.vllm.ai/en/latest/usage/reproducibility/) | 재현성은 temperature 하나만으로 보장되지 않음 |
| [OpenAI Function calling](https://developers.openai.com/api/docs/guides/function-calling) | 모델의 도구 요청과 애플리케이션의 실제 실행 구분 |
| [LangChain Overview](https://docs.langchain.com/oss/python/langchain/overview) | 프레임워크 역할, LangGraph와의 관계 |
| [LangChain Models](https://docs.langchain.com/oss/python/langchain/models) | 모델 인터페이스·응답·도구 호출 |
| [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools) | 함수 정의, 도구 설명, 입력 형식 |
| [LangChain SQL Agent](https://docs.langchain.com/oss/python/langchain/sql-agent) | SQL 조회 흐름, 권한·실행 범위 고려 |
| [LangChain 문서의 Retrieval 가이드](https://docs.langchain.com/oss/python/deepagents/retrieval) | 정해진 검색 후 생성과 Agent가 검색을 선택하는 방식 구분 |
| [Streamlit Architecture](https://docs.streamlit.io/develop/concepts/architecture/architecture) | Python 서버와 브라우저 화면의 역할 |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | 단순한 방법부터 시작, 정해진 작업 흐름과 Agent의 차이 |

LangChain의 Tool·검색·SQL 자료는 Context7의 공식 문서 검색 결과와 웹 공식 페이지로 대조했다. 설치 버전과 사내 서버에 대한 실행 검증은 별도다.

## 9. Claude Code 공식 출처

더 자세한 오후 강의 후보는 [Claude Code 공식자료 조사 메모](C:/Users/swl01/.codex/.chatgpt-projects/g-p-6a620d47fab081918f3c35b34836fc62/outputs/research_claude.md)에 있다.

| 공식 문서 | 강의 활용 |
|---|---|
| [Overview](https://code.claude.com/docs/en/overview) | 코딩 Agent를 사용하는 이유 |
| [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works) | 맥락 수집·행동·결과 확인, 도구·실행 환경 |
| [Best practices](https://code.claude.com/docs/en/best-practices) | 탐색·계획·구현·검증, 명확한 작업 요청 |
| [Memory](https://code.claude.com/docs/en/memory) | 프로젝트 지침과 기억 |
| [Context window](https://code.claude.com/docs/en/context-window) | 맥락 사용과 요약 |
| [Features overview](https://code.claude.com/docs/en/features-overview) | 지침·Skill·Subagent·MCP·Hook 역할 구분 |
| [Skills](https://code.claude.com/docs/en/skills) | 반복 절차와 참고자료의 재사용 |
| [MCP](https://code.claude.com/docs/en/mcp) | 외부 도구·데이터 연결 |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | 범위를 나눈 하위 작업과 별도 맥락 |
| [Hooks guide](https://code.claude.com/docs/en/hooks-guide) | 이벤트에 자동 동작 연결 |
| [Hooks reference](https://code.claude.com/docs/en/hooks) | Hook 유형과 설정의 세부 조건 |
| [Permissions](https://code.claude.com/docs/en/permissions) | 실행 범위와 권한 |
| [Security](https://code.claude.com/docs/en/security) | 로컬 실행과 작업 경계 |
| [Data usage](https://code.claude.com/docs/en/data-usage) | 요청 처리 경로·데이터 사용 조건 |
| [Network configuration](https://code.claude.com/docs/en/network-config) | 사내 네트워크 설정 시 확인할 내용 |
| [LLM gateway](https://code.claude.com/docs/en/llm-gateway) | Anthropic이 지원하는 Gateway 구성 범위 |
| [vLLM의 Claude Code 연결 가이드](https://docs.vllm.ai/en/latest/serving/integrations/claude_code/) | vLLM의 기술적 호환 안내. Anthropic 지원 정책과 사내 승인 여부는 별도 |

## 10. 확인되지 않은 자료·주장

- [사용자가 제시한 학습법 영상](https://youtu.be/Kf1dYpnH-N4): 제목·페이지 정보까지만 확인. 전체 자막·원 인터뷰·기간 단축 주장은 미확인.
- Naver 블로그 전체 공개 게시물: 직접 본문 접근을 확보하지 못해 Notion 관련 보관본으로 보완.
- Naver 기사·Streamlit 실습의 최종 HTML과 배포용 Python/ZIP: 발견한 skh_llm_guide와 동일 판본인지 미확인.
- Part Finder의 사내 운영 시작 시점과 강사 경력: 사용자가 제공한 소개 정보. 공개 Beta 저장소만으로 실제 운영 현황·성과를 독립 검증한 것은 아님.
- 현재 사내 모델명·API 주소·허용 기능·설치 경로·동시 호출 정책: 강의 환경에서 확인할 사항. 개인 자료의 이전 값으로 확정하지 않음.

종합 문서는 이런 미확인 부분을 성과나 기능으로 단정하지 않고, 로드맵을 확정할 때 확인할 항목으로 남겼다.
