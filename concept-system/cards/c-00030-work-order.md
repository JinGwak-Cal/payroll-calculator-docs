# C-00030 : 워크 오더 (Work Order)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00030 |
| | Coordinate | WF-02 |
| **기본** | 이름(한글) | 워크 오더 |
| | 영문명 / 약어 | Work Order |
| **정의** | 공식 정의 | 디스패처가 Worker(또는 Worker Group)에게 구체적 작업을 위임할 때 사용하는 표준 지시서 |
| | 목적 | 위임 과정의 모호함을 제거하고 Worker가 즉시 착수할 수 있게 한다 |
| | 핵심 질문 | 누가, 무엇을, 어떤 기준으로 완료해야 하는가 |
| **분류** | Type | Workflow |
| | Status | Candidate |
| | Stability | Experimental |
| **관계** | 상위 개념 | C-00005 (디스패처) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00024 (오픈딜리게이션) |
| | Before(전 단계) | C-00028 (Dispatcher Report) |
| | After(후 단계) | C-00031 (Rework Order) *[Forward Reference — 미작성, ID 예약]* |
| **비교** | 기존 유사 개념 | Task Ticket, Work Order (제조업/IT 서비스 관리에서 표준 용어) |
| | 차이점 | 제조업의 Work Order는 보통 사람 작업자에게 발급되지만, 본 개념은 AI Worker에게 발급되며 Open Delegation 원칙(강제 배정 아님)과 결합된다는 점이 다르다 |
| | 용어 유형 | 기존용어 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Dispatcher 운영 구조를 설계하는 과정에서 Constitution → Workflow → Report → Work Order → Handoff의 흐름이 정리되며 Workflow 산출물로 정의되었다 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.1 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | v1.0 → v1.1(Worker를 Worker(또는 Worker Group)로 확장) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | Workflow군 묶음 승인. 향후 다수 Worker 동시작업 구조 대비해 표현 확장 |
| | 비고 | C-00028 템플릿 적용 — Workflow군 묶음 리뷰 대상 |
