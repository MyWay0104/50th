# docs/ PDF 세 권 요약 (검토용 · 2026-09-17)

원문 텍스트 추출본은 저작권 때문에 저장소 밖(세션 scratchpad)에만 둔다:
- `C:/Users/swl01/AppData/Local/Temp/claude/C--Users-swl01-workspace-00-sk-hynix-only-50th/1b836274-cf89-4ac4-aad9-a028968a61a5/scratchpad/pdf_4day_agent_framework.md` (215쪽)
- `.../scratchpad/pdf_5day_llm.md` (337쪽)
- `.../scratchpad/pdf_agent_handbook.md` (463쪽)
4일 교안의 페이지별 제목 색인은 `pdf_4day_page_index.md`.

## A. 4일 교안 「AI 에이전트 프레임워크 구현」 (사용자가 원하는 흐름의 원본)

목차: 00 환경설정(VS Code·uv·가상환경, p4–24) → 01 LangChain 기반 Agent 기초(p25–62) → 02 RAG 및 Agent 검색 시스템(p63–96) → 03 LangGraph 워크플로·고급 Agent(p97–178) → 04 멀티에이전트·하네스 설계(p179–214)

01장 순서: 왜 Agent가 필요한가(실패 vs 성공, p25) → LLM이란·다음 토큰 예측·토큰·컨텍스트 윈도우·temperature·환각(p26–27) → 5단계 에이전트·동작 흐름(p28–29) → Deep Agents 첫 체험(p31) → 하네스 = Tools+Memory+Context(p32) → LangChain 3계층·핵심 컴포넌트 4가지(p34–35) → ChatOpenAI·init_chat_model·invoke/stream/batch(p36–41) → Messages 4타입·SystemMessage 페르소나·대화 이력(p42–46) → Tool(@tool, docstring·타입힌트)·create_agent·ReAct 루프·Tool Calling 시각화(p47–51) → Memory·InMemorySaver·thread_id(p52–55) → Middleware(p56–58) → 첫 Agent 결합·실행(p59–61) → 핵심 요약(p62)

02장 순서: RAG란·왜 RAG(환각·최신·도메인, RAG vs 파인튜닝, p64) → 파이프라인(인덱싱: 로딩→분할→임베딩→벡터스토어 / 추론: 질문→검색→컨텍스트→답변, p65–66) → Document Loader(p67–68) → 왜 분할하나(컨텍스트 한계·정밀도·의미 희석, 너무 작으면/크면/경계, p69–72) → 임베딩(뜻이 가까우면 벡터가 가까움, p73–74) → 벡터스토어·유사도 검색·MMR(p75–79) → Retriever→@tool 래핑(p80–82) → Naive RAG 체인·프롬프트 템플릿(p84–88) → Agent 기반 RAG(언제·몇 번 검색할지 LLM이 판단, p89–92) → 검색 품질 평가(적합성·충분성·정밀도, p93) → 한계(p95) → 요약(p96)

03장: create_agent 내부는 LangGraph(p98) → State/Node/Edge·StateGraph 5단계 빌드(p99–105) → 리듀서(p107–109) → 조건부 엣지·LLM 라우팅(p111–117) → 5대 워크플로 패턴(p118–124) → 체크포인터·멀티턴(p125–128) → @tool·bind_tools·ToolMessage 수동 루프(p132–136) → ReAct Agent 직접 구현(p137–140) → HITL interrupt/Command(p141–151) → LangSmith(p152) → Agentic RAG(grade→rewrite→generate, p154–167) → Re-ranking(p168–170) → Context Memory·메모리 3유형(p171–177)

04장: 왜 멀티에이전트(p180) → Supervisor/Handoff/Swarm(p181–195) → 하네스(p196) → write_todos·파일 도구·오프로딩(p197–199) → SKILL.md·Progressive Disclosure(p200–202) → 백엔드(p203–205) → 샌드박스·ACP(p206–208) → 실무 배포 구조·체크리스트(p209–214)

교수법: 매 절이 "왜 필요한가 → 개념 정의(❑/▪ 2~3단계) → 코드 → 시각화 페이지 → 핵심 요약"으로 닫힌다. Tips/주의 박스로 흔한 실수를 코드 옆에 둔다.

## B. 5일 교안 「LLM 활용과 고급화 과정」

| 장 | 절 | 페이지 |
|---|---|---|
| 01 LLM 기초 | LLM 개요(N-gram→Transformer·자기회귀) / 작동원리(GPT-3 시각화) / 토큰·BPE·컨텍스트윈도우·Attention / 학습원리(Pre-training·SFT·RLHF) | p5–46 |
| 02 RAG | LangChain·ChatModel(p48–49) / 프롬프트 엔지니어링(temperature·Top-K/P·zero/few-shot·system/context/role·CoT, p50–71) / LLM 한계·RAG 필요성(p72–76) / Document·Loader·Splitter·Embedding·VectorStore(p77–86) / Naive RAG·FAISS·RAG Agent(p87–106) / LangGraph·Tool·ReAct·Memory·Agentic RAG(p107–125) / Advanced RAG(p126–173) / RAG 구조(p174–198) / 평가(p199–216) | p48–216 |
| 03 Agent | Agent 개요·패턴(p218–239) / Tool & MCP(p240–257) / Deep Agents(p258–303) | p218–303 |
| 04 Fine-tuning | 전략·LoRA·QLoRA·실습 | p305–336 |

개념 설명 방식: 일상 비유 한 장에 하나(숫자→수학→숫자→단어, 96명 전문가 릴레이, 시험→오답노트→재시험). temperature는 용도 대비(낮음=사실·분류, 높음=창작) + 같은 질문 3회 호출 코드(p56, p58–59). 프롬프트는 같은 과제(표어)에 system→context→role을 한 줄씩 덧붙이는 누적 실험(p66–68). RAG는 반드시 "LLM 3대 제약 표"를 먼저(p74–75), 파이프라인은 Load→Split→Store→Retrieve→Generate(p88, p100). 청킹 이유를 먼저 쓰고(p80) 임베딩은 numpy 코사인 직접 계산으로 체감(p83). Tool은 "LLM은 계산·최신·DB·파일에 약하다 → LLM+Tool=Agent" 한 줄 공식(p112). ReAct는 라우터 그래프에서 엣지 하나만 바꾸면 루프가 된다는 코드 diff(p114 vs p117). docstring에 "언제 사용/언제 사용하지 말 것"(p241, p253). MCP는 USB-C·N×M→N+M(p254).

하루 교육에 가져올 후보: 다음 토큰 확률표(p12) · temperature 3회 비교(p56·58–59) · system→context→role 누적 실험(p66–68, 긍정봇으로 변형) · zero/few-shot 리뷰 분류(p61–64) · 3대 제약→RAG 해결표(p74–75) · Load→Split→Store→Retrieve→Generate(p88·100) · 청킹 이유+Splitter(p80–81·91) · 코사인 유사도 3문장(p83)+FAISS score(p96·98) · LLM+Tool=Agent·tool_calls(p112·241·253) · MCP USB-C·하네스·SKILL.md·HITL(p254·258·295–301) · 평가→병목→개선 루프(p216)

## C. agent-handbook (배기민 강사 자료)

| 파트 | 내용(쪽) |
|---|---|
| I 입문 (p7–35) | 환경 · LLM 기초 · LangChain 입문 · 멀티턴 메모리 · LangGraph 입문 · Deep Agents 입문 · 세 프레임워크 비교 · 미니 프로젝트 |
| II LangChain (p36–124) | 첫 에이전트 · 모델·메시지 · 도구·구조화 출력 · 메모리·스트리밍 · 미들웨어 · HITL · 멀티에이전트 · RAG · 프로덕션 · MCP · 가드레일 |
| III LangGraph (p125–214) | Graph/Functional API · 워크플로 패턴 · 지속성 · 스트리밍 · 인터럽트 · 서브그래프 · 프로덕션 |
| IV Deep Agents (p215–308) | 첫 에이전트 · 백엔드 · 서브에이전트 · 장기 메모리·스킬 · 하네스 · 샌드박스 |
| V 고급 (p309–424) | 미들웨어 · Subagents · Handoffs · 컨텍스트 엔지니어링 · Agentic RAG · SQL 에이전트 · 데이터 분석 · 배포 |
| VI 실전 (p425–458) | RAG · SQL · 데이터 분석 · ML · 딥 리서치 |

교수법: 학습 목표 → 이론 → 코드(+실행 결과) → 요약표 고정. **결핍→해결 서사**(메모리 없는 에이전트가 이름을 못 기억하는 장면을 먼저 실행으로 보여준 뒤 InMemorySaver 도입, p18). 매 장 도입에 "핵심 질문 · 한눈에 보는 핵심 · 언제 쓰고 언제 멈출까". 다이어그램마다 "그림 읽는 법" 한 단락. 개념은 표로 대비.

하루 교육에 가져올 후보: 메시지 4역할+도구 호출 4단계(p13) · ReAct 7단계·model/tools 두 노드(p16, p40–41) · "docstring은 동료에게 설명하듯"(p16, p56) · RAG 오프라인 인덱싱/온라인 질의 도식·chunk_size 권장(p368–372) · RAG 3아키텍처 비교(2-Step/Agentic/Hybrid, p370–371) · SQL 에이전트 트레이스·"DML 금지는 프롬프트가 아니라 DB 권한으로"(p383–384) · HITL 3옵션은 분기점(p386) · 컨텍스트=RAM·파일=디스크, 서브에이전트=팀장→팀원 위임(p220–221) · 하네스=말의 마구, AGENTS.md·SKILL.md·Progressive Disclosure(p260–267, p279) · 컨텍스트 엔지니어링 3줄 규칙·"실패 원인은 모델보다 컨텍스트 부족"(p353–354)

주의: 세 교안 모두 화면 출처로 쓰지 않는다(수강생이 볼 수 없는 자료). 개념·도식·비유의 아이디어만 가져오고, 출처 줄에는 공식 문서·논문만 적는다.
