# C-00013 : AI Company 개념체계 (AI Company Concept System)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00013 |
| | Coordinate | A-06 |
| **기본** | 이름(한글) | AI Company 개념체계 |
| | 영문명 / 약어 | AI Company Concept System |
| **정의** | 공식 정의 | Threshold Foundry(AI Company의 운영 대상)를 구성하는 개념들을 발견·명명·정의·분류·관계화하고 생명주기까지 관리하는 메타 구조 |
| | 목적 | Threshold Foundry 운영에 필요한 모든 개념을 일관된 구조로 기술하여, 개념 혼용 없이 시스템이 성장할 수 있는 지식 기반을 제공한다 |
| | 핵심 질문 | Threshold Foundry를 구성하는 개념들이 어떻게 정의되고, 서로 어떻게 연결되며, 어떻게 진화하는가 |
| **분류** | Type | Architecture *(단일 운영 절차나 규칙이 아니라 전체 개념 구조를 조직하는 메타 아키텍처 — Meta Card)* |
| | Status | Candidate |
| | Stability | Emerging *(Sprint-1을 통해 구조가 검증되었으나 외부 적용 사례 미확인)* |
| **관계** | 상위 개념 | 없음 *(최상위 메타 구조)* |
| | 하위 개념 | *(대표 구성요소)* C-00001 (개념수확), C-00004 (후보등록부), C-00019 (개념 파이프라인), C-00020 (Review System), C-00021 (Registry System), C-00027 (AI Development OS) — 실제 구성요소는 지속 확장됨 |
| | 관련 개념 | C-00040 (Threshold Foundry) *[Forward Reference — 미작성, ID 예약. 본 Concept System이 기술하는 대상(Subject)]* |
| | Before(전 단계) | 없음 |
| | After(후 단계) | 없음 *(최상위 구조 — 다음 단계가 아닌 모든 카드를 수용하는 구조)* |
| **비교** | 기존 유사 개념 | Ontology, Domain Model, Knowledge Model |
| | 차이점 | Ontology는 형식논리·추론까지 포함하는 시맨틱웹 표준이고, Domain Model은 주로 소프트웨어 엔티티 관계를 모델링한다. 본 개념은 AI Company 운영 개념의 발견·정의·생명주기 관리까지 포함하는 운영적 지식 모델이다 |
| | 용어 유형 | 기존용어조합+도메인한정 |
| | Semantic Boundary | Threshold Foundry는 AI Company가 운영하는 실체(Subject)이고, AI Company Concept System은 그 실체를 기술하는 메타 구조(Meta Structure)다 — 둘은 동일하지 않다. Foundry가 "무엇을 하는가"라면, Concept System은 "그것을 어떻게 이해하고 기술하는가"이다. Concept System은 Foundry를 변경하지 않고 기술한다 |
| | Official Name 후보 | 없음 — 확정 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | AI Dispatcher 설계 중 개념 혼용이 반복되면서 용어를 체계화할 필요가 생겼고, Thread Closing Pipeline 논의에서 "개념을 관리하는 메타 구조"로 발전함 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음6-1) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | ①하위 개념에 "대표 구성요소" 명시(확장 가능성 표현). ②Semantic Boundary에 "Concept System은 Foundry를 변경하지 않고 기술한다" 추가. ③비고 계층명을 Concept Dictionary 공식 용어가 확정될 때까지 잠정 표기로 유지 — Dictionary 상위 분류(운영계층/설명계층) 확정 시 동기화 |
| | 비고 | **Meta Card**: 본 카드는 Concept System 자체를 기술하는 카드 — 자기 자신이 관리하는 체계의 구성원이기도 함. **계층 구조(잠정)**: 운영계층(Rule·Workflow·Business·Architecture)과 설명계층(Theory·Hypothesis·Metric·Case Study)을 모두 수용하는 최상위 구조 — 공식 계층명은 Sprint-1 Backlog의 "Type Dictionary 상위 분류 검토" 확정 후 동기화 예정. **Threshold Foundry와의 관계**: Foundry = Subject(운영 대상), Concept System = Meta Structure(기술 도구) — 혼동 금지. Concept System은 Foundry를 변경하지 않고 기술한다 |
