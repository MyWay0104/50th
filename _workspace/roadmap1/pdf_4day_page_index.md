p1: AI 에이전트프레임워크구현 | Deep Agents · LangChain · LangGraph | 2026 | SK하이닉스
p2: 본교안은＂AI 에이전트프레임워크구현" 참여자만을위해제공되는교육용목적자료이며, | 본자료의전체또는일부를무단복제, 배포, 전송, 수정, 대여등일체의행위는 | 저작권법, 부정경쟁방지및영업비밀보호법등에의거하여엄격히금지되며 | 이를위반하는경우관련법령에따른처벌이수반될수있습니다.
p3: 목차 | 01. LangChain 기반Agent 기초 | ❑환경설정 | ❑ChatModel / Messages 구조이해
p4: 환경설정 | 00
p5: 환경설정 | ❑Visual Studio Code | ▪Visual Studio Code(줄여서VS Code)는Microsoft가만든무료코드편집기 | - 코드자동완성, 문법하이라이팅, 디버깅등개발에필요한기능을지원
p6: 환경설정 | ❑공식웹사이트에서다운로드 | ▪웹브라우저에서code.visualstudio.com에접속 | - 페이지중앙에있는“Download for Windows” 버튼을클릭하여설치파일을다운로드
p7: 환경설정 | ❑다운로드확인 | ▪버튼을클릭하면자동으로다운로드가시작되고, “Thanks for downloading VS Code!” 페이지가표시 | - 브라우저상단또는하단에다운로드진행상태가표시됩니다. 다운로드가완료되면설치파일을클릭하여실행
p8: 환경설정 | ❑라이선스동의 | ▪설치프로그램이실행되면사용권계약화면이표시 | - 화면아래쪽에서“동의합니다(A)”를선택한후다음(N) 버튼을클릭
p9: 환경설정 | ❑설치경로선택 | ▪VS Code가설치될폴더를지정하는화면 | - 기본경로(보통C:\Users\사용자이름\AppData\Local\Programs\Microsoft VS Code)를그대로사용
p10: 환경설정 | ❑시작메뉴폴더선택 | ▪Windows 시작메뉴에VS Code 바로가기를만들폴더이름을정하는화면 | - 기본값“Visual Studio Code”를그대로두고다음(N) 버튼을클릭
p11: 환경설정 | ❑추가작업선택 | ▪VS Code 설치시함께설정할추가옵션들을선택하는화면 | - 이설정들은나중에VS Code를더편리하게사용할수있게해줌
p12: 환경설정 | ❑설치준비완료확인 | ▪지금까지선택한설치설정의요약정보가표시 | ▪내용을확인한후설치(I) 버튼을클릭하여설치를시작
p13: 환경설정 | ❑설치진행 | ▪파일이추출되면서설치가진행
p14: 환경설정 | ❑설치완료 | ▪설치가완료되면“Visual Studio Code 설치마법사완료” 화면이표시 | ▪“Visual Studio Code 실행” 체크박스가체크된상태에서종료(F) 버튼을클릭하면VS Code가바로실행
p15: 환경설정 | ❑첫실행및초기설정 | ▪VS Code가처음실행되면“Get started with VS Code” 안내 화면이표시 | - 워크스루를따라설정하거나, “Mark Done”을클릭하여건너뛸수있음
p16: 환경설정 | ❑첫실행및초기설정 | ▪새파일만들기, 폴더열기, Git 저장소복제등의작업을시작할수있음
p17: 환경설정 | ❑uv | ▪uv는Python 프로젝트를관리하는데필요한거의모든기능을하나로모아놓은도구 | ▪웹브라우저에서docs.astral.sh/uv에접속하여공식문서를확인할수있음
p18: 환경설정 | ❑PowerShell 열기 | ▪키보드에서Windows 키를누르고“PowerShell”을입력한후Windows PowerShell을클릭하여실행 | ❑설치명령어실행하기
p19: 환경설정 | ❑설치완료확인하기 | ▪화면에PATH(경로) 설정을위한추가명령어가안내됨 | ▪안내된대로아래명령어를실행
p20: 환경설정 | ❑uv가정상적으로설치되었는지확인 | ▪새PowerShell 창을열고다음명령어를입력 | ▪uv help
p21: 환경설정 | ❑Python 프로젝트만들고가상환경생성하기 | ▪다음두가지명령어를차례대로입력 | uv init --python 3.13
p22: 환경설정 | ❑가상환경활성화시오류가발생하는경우 | ▪가상환경을활성화하기위해아래명령어를입력 | ▪이때빨간색오류메시지(PSSecurityException)가나타날수있음
p23: 환경설정 | ❑PowerShell 실행정책변경하기(관리자권한필요) | ▪Windows PowerShell을오른쪽클릭하고“관리자권한으로실행”을선택 | ▪확인메시지가나타나면A (모두예)를입력하고Enter를입력
p24: 환경설정 | ❑PowerShell 실행정책변경하기(관리자권한필요) | ▪Windows PowerShell을오른쪽클릭하고“관리자권한으로실행”을선택 | ▪확인메시지가나타나면A (모두예)를입력하고Enter를입력
p25: 왜Agent가필요한가? — 실패vs 성공비교
p26: LLM이란? — 에이전트의두뇌 | ❑대규모언어모델(Large Language Model) | ▪방대한텍스트로학습한, "다음토큰"을예측하는확률모델 | - 입력(프롬프트)을받아가장그럴듯한다음토큰을차례로생성→ 문장·코드·요약등자연어출력
p27: LLM 작동원리 | ❑Next Token Prediction | ▪앞토큰들을보고다음토큰확률을예측, 그걸반복해문장생성 | - 즉, LLM은"정답을안다"기보다"확률적으로자연스러운이어쓰기"를한다.
p28: 5단계로이해하는AI 에이전트
p29: AI 에이전트동작흐름
p30: LangChain 기반Agent 기초 | 01
p31: Deep Agents로Agent 첫체험 | ❑Deep Agents — 한줄로AI 에이전트를생성하는고수준API | ▪도구, 메모리, 프롬프트를조합한에이전트를즉시생성 | ❑create_deep_agent()가하는일
p32: 하네스(Harness) | ❑하네스(Harness)란? | ▪에이전트의도구·메모리·컨텍스트를하나로묶는실행틀 | ❑하네스3대구성요소
p33: 환경설정 | ❑필수패키지설치 | ▪LangChain 생태계핵심라이브러리 | ❑API Key 관리원칙
p34: LangChain | ❑LangChain이란? | ▪LLM 기반에이전트개발프레임워크 | ❑3계층구조로에이전트시스템을구성
p35: 핵심컴포넌트4가지 | ❑Model | ▪LLM, 에이전트의"두뇌" 역할 | - ChatOpenAI, initchatmodel()로초기화
p36: ChatOpenAI | ❑ChatOpenAI | ▪OpenAI 호환LLM을래핑하는LangChain 클래스 | - 환경변수의OPENAI_API_KEY를자동으로읽어옴
p37: init_chat_model — 프로바이더통합초기화 | ❑문자열하나로다양한프로바이더모델초기화 | ▪＂프로바이더:모델명＂ 형식으로지정 | ❑지원프로바이더목록
p38: invoke() — 단일호출 | ❑invoke() | ▪가장기본적인호출방식 | - 전체응답을한번에반환
p39: stream() — 토큰단위스트리밍 | ❑stream() | ▪토큰이생성되는대로실시간출력 | - 사용자체감응답속도를크게향상
p40: batch() — 여러입력동시처리 | ❑batch() | ▪여러요청을병렬로처리 | - 개별invoke() 반복보다효율적
p41: invoke / stream / batch 3가지호출패턴
p42: Messages 타입개요— 역할기반메시지시스템 | ❑LLM은메시지리스트를입력으로받음 | ▪각메시지에는역할(role)이부여 | ❑4가지메시지타입
p43: Messages 타입구조— 시각화
p44: SystemMessage — 모델의페르소나설정 | ❑SystemMessage로역할을부여하면같은질문에다른응답 | ▪설계포인트 | - SystemMessage는리스트맨앞에배치
p45: 딕셔너리형식과대화이력관리 | ❑딕셔너리형식 | ▪OpenAI API와동일한구조 | - 마이그레이션에유리한형식
p46: AIMessage 응답객체상세분석 | ❑AIMessage 내부구조 | ▪텍스트(content) 외에메타데이터포함 | - usage_metadata 활용
p47: Tool이란? — LLM이호출할수있는함수 | ❑Tool(도구) | ▪ 에이전트가호출할수있는외부함수인터페이스 | - LLM이"언제, 어떤인자로" 도구를호출할지자율판단
p48: from langchain.tools import tool | @tool | def add(a: int, b: int) -> int: | """두수를더합니다."""
p49: 도구를에이전트에연결하여실행 | ❑create_agent()에tools 리스트전달 | ▪에이전트가자동으로적절한도구를선택 | ❑에이전트의ReAct 루프
p50: Tool Calling 흐름— 시각화
p51: 복합도구호출— 멀티스텝계산 | ❑하나의질문에서여러도구를순차호출 | ❑메시지흐름관찰 | ▪1. HumanMessage: 사용자질문
p52: Memory — 대화상태유지메커니즘 | ❑Memory란? | ▪에이전트가이전대화를기억하는메커니즘 | ❑InMemorySaver
p53: Memory 동작흐름— 시각화
p54: InMemorySaver로멀티턴대화구현 | ❑체크포인터를에이전트에연결 | from langgraph.checkpoint.memory import InMemorySaver | memory_agent = create_agent(
p55: thread_id — 세션독립성 | ❑서로다른thread_id는완전히독립된대화 | ❑실무활용패턴 | ▪사용자별고유thread_id 부여→ 개인화대화
p56: Middleware — 에이전트파이프라인훅시스템 | ❑Middleware란? | ▪에이전트실행각단계에훅을추가하는메커니즘 | - 실행흐름중간에개입해서동작을추가/수정하는지점
p57: Middleware 구현예시— 로깅 | ❑@before_model | ▪입력로깅 | ❑미들웨어를에이전트에적용
p58: from langchain.agents.middleware import dynamic_prompt | from datetime import datetime | @dynamic_prompt | def add_datetime_context(request):
p59: 첫번째Agent — Tool + Memory + Middleware 결합 | ❑핵심구성요소정리 | ▪Model: ChatOpenAI | - 에이전트의두뇌
p60: ReAct 에이전트패턴— 시각화
p61: 에이전트실행— invoke & stream | ❑invoke로기본호출 | ❑stream으로실시간진행상황확인 | config = {"configurable": {"thread_id": "agent-1"}}
p62: 핵심요약 | ❑모델호출 | ▪ChatOpenAI 또는init_chat_model()로시작 | ❑메시지구조
p63: RAG 및Agent 검색시스템 | 02
p64: RAG란? | ❑검색증강생성(Retrieval-Augmented Generation) | ▪외부문서를검색하여LLM 응답의근거로활용하는기법 | ❑왜RAG인가?
p65: RAG 파이프라인전체흐름 | ❑Naive RAG 인덱싱단계 | ▪문서를검색가능한형태로변환 | - 문서(PDF/Excel/Word) → 로딩→ 텍스트분할→ 임베딩→ 벡터스토어
p66: 문서파이프라인전체흐름— 시각화
p67: Document Loader — 다양한포맷통합처리 | ❑RAG의첫단계 | ▪ 원본문서를Document 객체로변환 | ❑포맷별로더
p68: 문서로딩 | ❑PDF 로딩 | ▪ 페이지별Document 생성 | ❑Excel / Word 로딩
p69: 왜텍스트를분할하는가? | ❑LLM의컨텍스트윈도우한계 | ▪전체문서를한번에넣을수없다 | ❑검색정밀도향상
p70: 텍스트분할전략— 시각화
p71: RecursiveCharacterTextSplitter — 범용분할기 | ❑가장범용적인분할기 | ▪구분자우선순위를따라자연스럽게분할 | - 분할순서: "\\n\\n" → "\\n" → " " → "" (단락→ 줄→ 단어→ 글자)
p72: chunk_size에따른분할결과비교 | ❑chunk_size 변경실험 | ▪도메인에맞는최적값탐색 | ❑도메인별권장크기
p73: 임베딩이란? — 텍스트를벡터로변환 | ❑텍스트의의미를고차원벡터(숫자배열)로표현 | ▪의미적으로유사한텍스트→ 벡터공간에서가까이위치 | ❑벡터유사도예시
p74: OpenAI Embeddings 사용 | ❑OpenAI 임베딩모델 | ▪ text-embedding-3-small | ▪ text-embedding-3-large
p75: 벡터스토어란? — 벡터저장+ 유사도검색 | ❑벡터스토어 | ▪임베딩벡터를저장하고유사도검색을수행하는DB | ❑벡터스토어비교
p76: 임베딩과벡터스토어구조— 시각화
p77: ChromaDB | ❑from_documents() | ▪분할·임베딩·저장을한줄로 | from langchain_chroma import Chroma
p78: 유사도검색— similarity_search | ❑코사인유사도기반top-k 검색 | ❑점수포함검색 | ▪검색품질판단
p79: 검색방식비교— similarity vs MMR | ❑유사도검색(Similarity) | ▪관련성만고려 | - 가장유사한k개를반환
p80: Retriever 인터페이스— 체인연결의핵심 | ❑Retriever란? | ▪LangChain 체인/에이전트에연결가능한검색인터페이스 | - as_retriever()로벡터스토어를Retriever로변환
p81: Retriever → Agent의검색Tool — @tool 래핑 | ❑Retriever를@tool로래핑하면에이전트가자율호출가능 | ❑content_and_artifact 패턴 | ▪content — 에이전트에게전달되는텍스트요약
p82: Retriever 파라미터튜닝
p83: 미들웨어로Agent 행동제어— 하네스미들웨어스택 | ❑미들웨어스택 | ▪에이전트의모든동작에훅을추가하는구조 | ▪하네스관점
p84: Naive RAG 파이프라인구조 | ❑Naive RAG — 가장기본적인RAG 구조 | ▪질의→ Retrieve(검색) → Augment(보강) → Generate(생성) | ❑4단계동작흐름
p85: Naive RAG 아키텍처
p86: RAG 프롬프트템플릿설계 | ❑ChatPromptTemplate | ▪컨텍스트+ 질문을구조화 | ❑프롬프트설계핵심
p87: Naive RAG 체인구성— LCEL 파이프라인 | ❑RunnablePassthrough로질문전달 | ▪Retriever로컨텍스트병렬주입 | ❑데이터흐름
p88: Naive RAG 실행및테스트 | ❑invoke()로전체파이프라인실행 | ❑다양한질문으로테스트 | ▪도메인내질문: 문서에답이있는경우확인
p89: Agent 기반RAG — 자율검색호출구조 | ❑Agent 기반RAG | ▪ 에이전트가검색Tool을자율적으로호출 | - 언제검색할지, 몇번검색할지를LLM이판단
p90: LCEL 체인vs 에이전트RAG 비교 | ❑LCEL 체인(Naive) | ▪고정된단일검색+ 단일생성 | - 항상1회검색, 검색횟수고정, 도구조합불가
p91: RAG 방식비교— 시각화
p92: 검색도구정의및에이전트RAG 구현 | ❑@tool로검색도구정의 | ❑create_agent로RAG 에이전트생성 | @tool(response_format="content_and_artifact")
p93: 검색품질평가관점 | ❑적합성(Relevance) | ▪검색된문서가질문과관련있는가? | - 유사도점수로판단— 점수가낮을수록(L2) 유사
p94: 프롬프트튜닝전략 | ❑기본프롬프트vs 개선프롬프트비교 | ▪기본: "컨텍스트: {context}\n질문: {question}\n답변:“ | ❑개선전략4가지
p95: Naive RAG의한계점 | ❑질의변환부재 | ▪사용자질문을그대로검색에사용 | - 의도파악실패가능→ Query Rewriting, HyDE로개선
p96: 핵심요약 | ❑문서파이프라인 | ▪로딩→ 분할→ 임베딩→ 벡터스토어저장 | ❑분할품질
p97: LangGraph 워크플로우및고급 | Agent | 03
p98: Agent 내부원리 | ❑create_agent()는내부적으로LangGraph 그래프를구성 | ▪자동으로ReAct 패턴의StateGraph를생성 | ❑내부동작흐름
p99: LangGraph란 | ❑LangGraph | ▪ LangChain 생태계의저수준오케스트레이션프레임워크 | ▪상태기반그래프구조로에이전트워크플로를정의
p100: LangGraph 상태머신개념— 시각화
p101: LangGraph 핵심특징5가지 | ❑상태관리 | ▪TypedDict 기반상태정의및리듀서 | - 워크플로전체에서공유하는데이터스키마
p102: 두가지API | ❑Graph API | ▪선언적(노드+ 엣지) | - 명시적State + 리듀서로상태관리
p103: 상태(State) 정의— TypedDict 기반스키마 | ❑State란? | ▪워크플로실행중관리되는공유데이터 | - TypedDict로스키마를정의
p104: StateGraph 빌드패턴 | ❑5단계빌드패턴 | ▪1. StateGraph(State) | - 상태스키마로그래프빌더생성
p105: StateGraph 구조— 시각화
p106: 입출력스키마분리— 내부상태보호 | ❑내부상태보호 | ▪문제 | - 내부중간처리용필드가외부에노출됨
p107: 상태리듀서란? | ❑리듀서(Reducer) | ▪상태필드가어떻게업데이트되는지결정하는함수 | ❑4가지리듀서타입
p108: operator.add 리듀서 | ❑Annotated[list, operator.add] | ▪반환한리스트를기존에append | ❑핵심차이
p109: from langgraph.graph import MessagesState | def chatbot(state: MessagesState) -> dict: | response = llm.invoke(state["messages"]) | return {"messages": [respons
p110: 멀티노드그래프 | ❑여러노드를엣지로연결→ 순차파이프라인 | class TextState(TypedDict): | text: str
p111: 조건부엣지— 상태에따라동적분기 | ❑add_conditional_edges | ▪라우팅함수의반환값에따라다음노드결정 | ❑핵심규칙
p112: 조건부라우팅흐름— 시각화
p113: LLM 기반조건부라우팅 | ❑Pydantic 모델+ with_structured_output | ▪LLM이직접분류 | ❑장점
p114: 그래프시각화— Mermaid 다이어그램 | ❑get_graph().draw_mermaid() — 그래프구조를텍스트다이어그램으로확인 | class DemoState(TypedDict): | input: str
p115: stream() — 실행과정실시간관찰 | ❑stream()은각노드완료시상태변경분을yield | ▪yield는값을하나반환하고, 함수상태를유지한채멈췄다가다음호출때이어서실행 | ❑invoke() vs stream() 차이
p116: class RouterState(TypedDict): | query: str | category: str | result: str
p117: LLM structured output을활용한라우팅 | ❑Pydantic 모델로LLM 분류결과를스키마화 | ❑장점 | ▪키워드매칭보다유연— 문맥이해기반분류
p118: 5대워크플로패턴 | ❑LangGraph로구현하는5가지핵심워크플로패턴 | ▪Prompt Chaining — A → B → C (순차) | - 단계별변환: 초안→ 개선→ 최종
p119: 5대워크플로패턴
p120: Routing 패턴— 조건분기라우팅상세 | ❑Routing | ▪입력특성에따라전문노드로분기 | ❑Routing 패턴의핵심
p121: Orchestrator-Worker 패턴— Send()로동적작업분배 | ❑Orchestrator-Worker | ▪하나의오케스트레이터가서브태스크를동적생성 | ❑Send()의역할
p122: Prompt Chaining — 순차적LLM 호출파이프라인 | ❑각단계의출력이다음단계의입력 | class ChainState(TypedDict): | topic: str
p123: Parallelization — 병렬실행후결과합산 | ❑START에서여러노드로엣지→ 자동병렬실행 | ❑핵심 | ▪Annotated[list, operator.add] 리듀서로결과누적
p124: Evaluator-Optimizer — 자동품질개선루프 | ❑generate → evaluate → 품질미달시다시generate | ❑무한루프방지필수 | ▪iterations 카운터로최대반복제한
p125: 체크포인터와멀티턴대화 | ❑체크포인터(Checkpointer) | ▪invoke() 호출사이에상태자동저장 | - InMemorySaver — 메모리기반(개발/테스트용)
p126: Persistence 메커니즘— 시각화
p127: 멀티스텝대화흐름— 단계별정보수집 | ❑커스텀상태로대화단계(phase)를관리 | ❑상태머신의핵심패턴 | ▪각노드가phase를업데이트→ 다음동작자동결정
p128: 통합예제— 라우팅+ 멀티턴+ 상태관리 | ❑MessagesState 확장 | ▪커스텀필드추가 | ❑실전구조: 분류→ 전문가라우팅→ 응답
p129: 핵심요약 | ❑State | ▪TypedDict로스키마를정의하고리듀서로업데이트를병합 | ❑Node
p130: 조건분기복습— 감성분석라우터예시 | ❑add_conditional_edges()로상태기반동적분기 | ❑분기대상 | ▪라우팅함수반환값→ 노드이름매핑
p131: LLM 기반라우팅— structured output 활용 | ❑Pydantic + with_structured_output — LLM이직접분기결정 | ❑키워드매칭vs LLM 라우팅 | ▪키워드: 빠르지만경직적— 새패턴대응어려움
p132: Tool 정의— @tool 데코레이터 | ❑@tool — Python 함수를LLM이호출할수있는도구로변환 | ❑필수요소— docstring(도구설명) + 타입힌트(파라미터스키마) | from langchain_core.tools import tool
p133: bind_tools — LLM에도구바인딩 | ❑bind_tools() — 도구스키마를LLM에전달 | ▪바인딩후LLM은응답에tool_calls를포함시킴 | ❑핵심포인트
p134: ToolMessage — 도구실행결과전달 | ❑tool_calls를수동으로실행하고결과를ToolMessage로구성 | ▪tool_call_id가핵심— LLM이어떤호출의결과인지매핑 | ❑전체흐름
p135: 다양한종류의도구정의— 검색, 계산, API | ❑실전에서자주사용하는도구패턴 | ❑docstring이LLM의도구선택기준 | ▪모호하면LLM이잘못된도구를선택할수있음
p136: 복합도구바인딩및테스트 | ❑여러도구를한번에바인딩 | ▪LLM이자동선택 | all_tools = [search_knowledge, add, multiply, get_exchange_rate]
p137: ReAct Agent — Tool-calling 루프의핵심패턴 | ❑ReAct(Reasoning + Acting) | ▪추론과행동을번갈아수행 | ❑루프구조
p138: ReAct Agent 구현코드 | ❑StateGraph로tool-calling 루프구현 | class AgentState(TypedDict): | messages: Annotated[list[AnyMessage], operator.add]
p139: ReAct Agent 그래프— 시각화
p140: ReAct Agent 실행— stream으로추적 | ❑stream_mode="updates"로각노드실행을단계별추적 | ❑복합질문— 여러도구를순차적으로호출 | ▪ReAct 패턴이도구결과를보고추가도구호출을자동결정
p141: HITL (Human-in-the-Loop) — 사람의개입이필요한워크플로 | ❑HITL이란? | ▪에이전트가위험하거나중요한작업전에사람의승인을받는패턴 | ❑핵심API 2가지
p142: HITL (Human-in-the-Loop)
p143: HITL 워크플로우구현— 승인노드패턴 | ❑승인노드에서interrupt()로사람의판단을받는구현 | ❑재개코드 | from langgraph.types import interrupt, Command
p144: Deep Agents의interrupt_on — 선언적HITL | ❑Deep Agents는HITL을선언적으로지원 | ▪interrupt_on 파라미터로중단조건을간결하게지정 | ❑LangGraph 직접구현vs Deep Agents 선언적HITL
p145: 체크포인터기반에러핸들링 | ❑프로덕션핵심원칙 | ▪ 에러발생해도처음부터다시시작하지않음 | ❑InMemorySaver 체크포인터
p146: 멀티턴대화에이전트구현 | ❑같은thread_id → 이전대화유지 | ❑스레드독립성— 다른thread_id는완전히독립된상태 | config = {"configurable": {"thread_id": "session-01"}}
p147: get_state() — 현재상태조회 | ❑체크포인터가저장한상태를조회하여디버깅 | ❑get_state_history() | ▪전체상태이력조회
p148: interrupt() — Human-in-the-Loop 패턴 | ❑민감한작업전사람의승인을받는패턴 | ❑실행흐름 | ▪1. interrupt() 호출시그래프실행이중단됨
p149: Command(resume) — 중단된실행재개 | ❑resume 값이interrupt()의반환값이됨 | ❑중단된스레드와동일한config 사용필수 | # 1단계: 그래프실행→ interrupt에서중단
p150: update_state() — 외부에서상태직접수정 | ❑디버깅또는수동개입시상태를프로그래밍방식으로변경 | ❑update_state()는새체크포인트를생성 | ▪기존이력은보존됨— 타임트래블가능
p151: 타임트래블— 이전체크포인트로되돌아가기 | ❑get_state_history()에서원하는시점의config를가져와재개 | ❑핵심— 타임트래블후새대화는분기(fork)를생성 | ▪기존이력은보존— 비파괴적디버깅
p152: Agent 디버깅— LangSmith 트레이싱& 스트리밍디버그 | ❑LangSmith 트레이싱 | ▪에이전트실행의전체흐름을시각적으로추적 | - 각노드의입력/출력, 토큰사용량, 실행시간기록
p153: 핵심요약 | ❑조건분기 | ▪라우팅함수와LLM structured output으로동적분기 | ❑Tool 연동
p154: Naive RAG의한계점분석 | ❑Naive RAG 파이프라인 | ▪질문→ 검색(top-k) → LLM 생성 | - 가장기본적인검색증강생성구조
p155: Naive RAG → Agentic RAG 전환 | ❑Naive RAG의근본문제— 검색전략이고정 | ▪항상동일한파이프라인: 검색→ 생성 | ▪검색결과품질과무관하게진행
p156: Agentic RAG
p157: Naive RAG vs Agentic RAG — 시각화
p158: Agentic RAG 아키텍처흐름 | ❑전체그래프구조 | ▪질문→ retrieve → grade_documents → 분기 | ▪관련문서있음→ generate 노드로답변생성
p159: Agentic RAG 아키텍처흐름
p160: create_agent 기반Agentic RAG | ❑가장간단한구현— create_agent + retrieve 도구 | ❑특성 | ▪구현: 한줄(create_agent)
p161: Query Decomposition — 복합질문분해전략 | ❑문제— 여러정보를요구하는복합질문은단일검색으로불충분 | ▪예: "SK하이닉스HBM 매출·경쟁사점유율·향후전략은?" → 한번의top-k로는세영역을다덮기어려움 | ❑핵심아이디어— LLM이원질문을서브질문으로분해→ 각각검색→ 통합
p162: Query Decomposition — 흐름시각화
p163: Query Decomposition 구현패턴 | ❑Structured Output으로서브질문리스트생성 | ❑서브질문별검색+ 통합 | from pydantic import BaseModel, Field
p164: GradeDocuments — 문서관련성이진판정 | ❑핵심아이디어 | ▪검색결과를무조건사용하지않고관련성을평가 | - Naive RAG: 검색결과를그대로LLM에전달
p165: grade_documents 노드구현 | ❑노드함수 | ▪검색문서를하나씩평가 | ❑동작원리
p166: 조건분기— generate vs rewrite | ❑라우팅함수 | ▪필터링결과에따라분기 | ❑rewrite_query 노드— 쿼리재작성
p167: Agentic RAG 전체그래프조립 | ❑StateGraph 구성 | ▪흐름요약 | - START → retrieve → grade → (yes) → generate → END
p168: Re-ranking 개요 | ❑Re-ranking이란? | ▪ 검색된문서를질문과의관련성기준으로재정렬 | - 1차검색(Bi-Encoder)은빠르지만정밀도가낮을수있음
p169: Re-ranking 개요
p170: LLM 기반Re-ranker 구현 | ❑with_structured_output 활용 | ▪구조화된관련성점수수신 | from pydantic import BaseModel, Field
p171: Context Memory — 대화맥락을유지하는RAG | ❑문제— 기본RAG는대화맥락을기억하지못함 | ▪"아까검색한문서에서..." → 이전대화참조불가 | ▪매턴마다독립적검색→ 연속대화에서품질저하
p172: Context Memory 2차원매트릭스— 시각화
p173: 메모리3유형— Semantic / Episodic / Procedural | ❑Semantic Memory — 사실과지식 | ▪예: "사용자는반도체공정PM 담당" | ▪사용자프로필, 도메인지식, 환경설정
p174: InMemoryStore — 장기메모리구현 | ❑InMemoryStore + namespace 패턴 | ❑검색— 시맨틱유사도기반 | ❑namespace 설계
p175: Context Memory + Agent 통합 | ❑Tool에서Store 접근 | ❑Hot Path vs Background | ▪Hot Path: 동기— 응답전에메모리저장(정확하지만느림)
p176: Agentic RAG + Context Memory 통합아키텍처 | ❑통합파이프라인 | ▪1. 사용자질문수신 | ▪2. Context Memory에서관련기억검색(remember 도구)
p177: 통합구현예시 | ❑create_agent로통합 | ❑실행 | from langchain.agents import create_agent
p178: 핵심요약 | ❑한계인식 | ▪Naive RAG의검색품질한계와개선포인트이해 | ❑Agentic RAG
p179: 멀티에이전트및하네스설계 | 04
p180: 왜멀티에이전트인가? | ❑단일에이전트의한계— 복잡한작업에서역할과부하발생 | ▪하나의에이전트에너무많은도구와역할→ 성능저하 | ▪도메인별전문성확보가어려움
p181: 3대멀티에이전트패턴 | ❑Supervisor 패턴— 감독자가서브에이전트를도구로호출 | ▪중앙집중제어, 컨텍스트격리, 병렬처리에적합 | ▪감독자가작업분해→ 위임→ 결과집계
p182: 3대멀티에이전트패턴
p183: 패턴선택가이드 | ❑패턴선택의사결정흐름 | ▪1. 에이전트간전체대화이력을공유해야하는가? | - 예→ Handoff 패턴
p184: Supervisor 패턴— 3계층아키텍처 | ❑3계층구조 | ▪저수준도구: 외부서비스직접호출(단순함수래퍼) | ▪서브에이전트: 도메인별추론+ 도구조합(전문시스템프롬프트)
p185: Supervisor 패턴— 3계층아키텍처
p186: Handoff 패턴— 에이전트간상태전환 | ❑Handoff 패턴이란? — Command(goto=...)로에이전트간직접전환 | ▪Supervisor가중앙집중형이라면, Handoff는분산형제어흐름 | ❑전환메커니즘
p187: Handoff 패턴— 에이전트간상태전환
p188: SubAgent 패턴— 서브에이전트를도구로래핑 | ❑핵심아이디어— 서브에이전트를@tool로래핑하여감독자에노출 | ❑핵심포인트 | ▪래핑함수에서마지막메시지의content만반환→ 컨텍스트격리
p189: 에이전트레지스트리— 단일디스패치도구 | ❑에이전트레지스트리— 서브에이전트를딕셔너리로관리 | ▪서브에이전트추가/제거가레지스트리수정만으로완료 | ▪Literal 타입으로유효한에이전트이름을제한→ 잘못된호출방지
p190: CompiledSubAgent — Deep Agents 방식 | ❑Deep Agents의SubAgent 추상화 | ▪CompiledSubAgent의역할 | - sub_agents dict → 자동으로@tool 래핑+ 레지스트리구성
p191: CompiledSubAgent — Deep Agents 방식
p192: 상태공유+ 서브그래프모듈화 | ❑에이전트간상태공유방식 | ▪공유키: 부모-서브그래프간동일키로매핑(스키마동일시) | ▪래퍼노드: 래퍼함수에서상태를변환하여전달(스키마다를시)
p193: 상태공유+ 서브그래프모듈화
p194: 래퍼노드패턴— 스키마변환 | ❑부모상태와서브그래프상태가다를때 | ❑핵심포인트 | ▪래퍼함수가상태변환의핵심— 매핑을명확히정의
p195: 핵심요약 | ❑패턴이해 | ▪Supervisor / Handoff / Swarm의특성과사용시점 | ❑SubAgent 정의
p196: Agent 하네스란? | ❑하네스(Harness) — 에이전트의실행환경을감싸는프레임워크 | ▪LLM + 도구+ 상태관리+ 보안경계를하나로통합 | ▪에이전트가"무엇을할수있고, 무엇을할수없는지" 정의
p197: write_todos — 에이전트의작업계획 | ❑TodoList 패턴— 에이전트가작업을계획하고추적 | ❑동작흐름 | ▪1. 사용자요청수신→ 에이전트가작업분해
p198: 파일시스템도구— 읽기/쓰기/편집 | ❑에이전트에파일접근능력부여 | ❑기본도구세트 | ▪read_file: 파일내용읽기(경로제한적용)
p199: 컨텍스트오프로딩— 긴출력관리 | ❑문제— 도구출력이길면LLM 컨텍스트윈도우낭비 | ▪검색결과수십개, 로그파일수천줄→ 토큰폭증 | ❑해결— 긴출력을파일로저장하고요약만컨텍스트에유지
p200: SKILL.md — 에이전트의지식모듈 | ❑SKILL.md란? — 에이전트가참조하는구조화된지식파일 | ▪도메인지식, 작업절차, 제약조건을Markdown으로정의 | ▪에이전트의system_prompt에선택적으로주입
p201: Progressive Disclosure — 선택적지식로딩 | ❑문제— 모든지식을항상로딩하면토큰낭비 | ▪10개SKILL.md를모두system_prompt에넣으면수만토큰소모 | ❑Progressive Disclosure 패턴
p202: SKILL.md 작성실습가이드 | ❑좋은SKILL.md의요건 | ▪명확한역할정의: 이Skill이무엇을하는지한줄로설명 | ▪도구목록: 사용가능한도구와각도구의용도
p203: 스토리지백엔드— 4가지유형 | ❑왜스토리지백엔드가필요한가? | ▪InMemoryStore는프로세스종료시소멸 | ▪프로덕션에이전트는상태를영구저장해야함
p204: StateBackend vs StoreBackend | ❑StateBackend — 세션내임시상태 | ❑StoreBackend — 교차세션영구저장 | ❑선택기준
p205: CompositeBackend — 데이터별라우팅 | ❑CompositeBackend란? — 여러백엔드를조합하여데이터별최적저장 | ❑라우팅규칙 | ▪대화상태, 작업목록→ state (빠른접근, 임시)
p206: 샌드박스— 에이전트의안전한실행환경 | ❑왜샌드박스가필요한가? | ▪에이전트가코드를생성하고실행하는경우→ 보안위험 | ▪파일시스템접근, 네트워크요청, 시스템명령실행가능
p207: 샌드박스구현옵션 | ❑경량샌드박스— 프로세스격리 | ▪subprocess + 리소스제한(ulimit) | ▪빠른시작, 간단한구현, 보안수준보통
p208: ACP — Agent Communication Protocol | ❑ACP란? — 에이전트간통신을표준화하는프로토콜 | ▪서로다른프레임워크로구현된에이전트간통신 | ▪HTTP 기반RESTful API 표준
p209: 실무배포구조— 전체아키텍처 | ❑프로덕션에이전트의구성요소 | ▪1. Agent 하네스: 실행환경+ 도구+ 보안경계 | ▪2. SKILL.md: Progressive Disclosure로지식관리
p210: 실무배포구조— 전체아키텍처
p211: Putting it all together — 통합예시 | ❑반도체기술분석에이전트시스템 — 이에이전트가할수있는것 | ▪작업계획수립(write_todos) → 서브에이전트위임 | ▪파일읽기/쓰기→ 컨텍스트오프로딩→ 보고서생성
p212: 프로덕션체크리스트 | ❑보안 | ▪파일시스템경로제한(allowed_paths) | ▪코드실행샌드박스(timeout, memory, network)
p213: 에이전트디버그및최적화
p214: 핵심요약 | ❑하네스 | ▪도구, 메모리, 컨텍스트가조합된Agent의인프라 | ❑SKILL.md
p215: End
