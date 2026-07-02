# C-00027 : AI Development OS

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00027 |
| | Coordinate | B-01 |
| **기본** | 이름(한글) | AI 개발 운영체계 |
| | 영문명 / 약어 | AI Development OS |
| **정의** | 공식 정의 | Dispatcher·Worker·Reviewer가 역할분리 원칙과 표준 절차(Work Order, Dispatcher Report)에 따라 협업하는 AI 운영체계 |
| | 목적 | 역할분리와 표준 절차를 기반으로 AI 협업이 지속 가능하게 운영될 수 있는 구조를 정의한다 |
| | 핵심 질문 | AI 협업이 사람 중계 없이 작동하려면 어떤 운영 구조가 필요한가 |
| **분류** | Type | Business *(Business인 이유: 단순 Architecture 설계가 아니라 "누가 어떤 역할로 참여해 어떤 가치를 만드는가"라는 운영 모델을 정의하기 때문 — AI Company의 핵심 운영 자산)* |
| | Status | Candidate |
| | Stability | Emerging *(D-PW-027에서 역할 분리가 합의·운영 중이나, 자동화는 아직 Stage 1)* |
| **관계** | 상위 개념 | C-00038 (AI Company Concept System) *[Forward Reference — 미작성, ID 예약]* |
| | 하위 개념 | C-00005 (디스패처), C-00023 (역할분리), C-00028 (Dispatcher Report), C-00030 (Work Order) |
| | 관련 개념 | C-00011 (Dispatcher Roadmap — AI Development OS가 Stage 7에 도달하는 경로) |
| | Before(전 단계) | C-00023 (역할분리 규칙 확립) |
| | After(후 단계) | C-00011 (Dispatcher Roadmap — Stage 1부터 단계적 자동화) |
| **비교** | 기존 유사 개념 | DevOps, MLOps, AI Workflow Automation |
| | 차이점 | DevOps·MLOps는 소프트웨어 빌드·배포 파이프라인 자동화를 다루지만, 본 개념은 AI가 서로의 역할을 인식하고 Context Layer 위에서 자율적으로 협업하는 운영체계를 다룬다 — 코드 파이프라인이 아니라 판단·위임·보고의 협업 파이프라인이다 |
| | 용어 유형 | 기존용어조합+신개념 |
| | Semantic Boundary | 일반적 "Operating System"은 하드웨어 자원을 관리하는 시스템 소프트웨어를 의미한다. 본 개념에서 "OS"는 그 은유를 빌려 AI 협업 자원(역할·절차·Context)을 관리하는 운영 구조를 표현한다 — 실제 소프트웨어 OS와는 무관하다 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Role Separation·Work Order·Dispatcher Report 등 개별 규칙과 절차가 축적되면서, 이를 하나의 일관된 운영체계로 통합할 필요가 생겨 정의됨 |
| | Decision Origin | D-PW-027 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음5-1) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | 정의를 특정 AI 제품명→역할(Dispatcher·Worker·Reviewer) 중심으로 일반화. 목적을 "사람 중계 제거"→"지속 가능한 AI 협업 운영체계 구축"으로. Discovery Context를 개별 규칙의 통합 필요성 중심으로. Review Backlog: Threshold Foundry ↔ AI Development OS ↔ AI Company Concept System 계층 관계 — Sprint-1 완료 후 Architecture군과 함께 재정의 검토 |
| | 비고 | Business군 첫 카드 — 카드당 리뷰 대상. Role Separation(C-00023)을 헌법으로, Work Order·Dispatcher Report를 절차로 갖추면 이 OS가 실제로 작동한다. 현재 Stage 0(사람 중계) 거의 완료, Stage 1(운영규칙 확립) 진행 중 |
