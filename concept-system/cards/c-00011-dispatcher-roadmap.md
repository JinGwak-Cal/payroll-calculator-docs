# C-00011 : 디스패처 로드맵 (Dispatcher Roadmap)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00011 |
| | Coordinate | A-02 |
| **기본** | 이름(한글) | 디스패처 로드맵 |
| | 영문명 / 약어 | Dispatcher Roadmap (또는 Dispatcher Maturity Roadmap) |
| **정의** | 공식 정의 | 디스패처가 사람 수행(Stage 0)에서 완전 자율 운영(Stage 7)까지 성장하는 8단계 구조 |
| | 목적 | Dispatcher 역할이 어떤 순서로 자동화·성숙되는지 추적 가능하게 한다 |
| | 핵심 질문 | Dispatcher는 지금 어느 성숙 단계에 있는가 |
| **분류** | Type | Architecture *(작업 순서가 아니라 시스템의 성장 구조이므로 Workflow가 아닌 Architecture로 분류)* |
| | Status | Candidate |
| | Stability | Experimental |
| **관계** | 상위 개념 | C-00005 (디스패처) |
| | 하위 개념 | 없음 *(Stage 0~7 자체는 카드가 아니라 본 카드 내부 속성으로 관리)* |
| | 관련 개념 | 없음 |
| | Before(전 단계) | C-00005 (디스패처) |
| | After(후 단계) | 없음 *(현재 최상위 — Stage 7 도달 후 후속 개념 미정)* |
| **비교** | 기존 유사 개념 | Product Roadmap, Maturity Model (예: CMMI) |
| | 차이점 | 일반 Maturity Model은 조직·프로세스 성숙도를 측정하지만, 본 로드맵은 단일 역할(Dispatcher)이 사람 개입에서 완전 자율로 옮겨가는 경로에 한정된다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | Dispatcher Roadmap / Dispatcher Maturity Roadmap *(미확정)* |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Pilot-002(Dispatcher 카드 작성) 중 "After가 Concept이 아닌 텍스트를 가리켜서는 안 된다"는 검토 결과로 분리 신설됨 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 — Pilot-002 Review 결과로 신설 |
| | Review Result | 검토 대기 |
| | Review Notes | — |
| | 비고 | Stage 구성 개요: 0(사람 수행) → 1(운영규칙 확립) → 2(Task Type 표준화) → 3(Worker Registry) → 4(Report 자동생성) → 5(Work Order 자동생성) → 6(자율추천) → 7(완전자율, 장기목표). 상세는 아래 Stage 상세 표 참조 |

---

## Stage 상세 (Goal / Activation Condition / Exit Condition)

| Stage | Goal | Activation Condition | Exit Condition | Deliverable |
|---|---|---|---|---|
| 0 | 사람이 Dispatcher 역할 수행 | 프로젝트 시작 | 운영 패턴이 반복되어 규칙화 가능해짐 | (사람 운영, 산출물 없음) |
| 1 | Dispatcher 운영 규칙 확립 (Constitution, 권한, Report, Work Order, Boundary) | Stage 0 종료 | 운영 규칙 문서 확정 | Dispatcher Constitution v1.0 |
| 2 | Task Type 표준화 (Design/Implementation/Bug/Review/Research/Release) | Stage 1 종료 | Task Type 분류 기준 확정 | Task Dictionary v1.0 |
| 3 | Worker Registry 완성 (GPT/Claude/CodeX/Reviewer/Dispatcher 역할 확정) | Task Type이 표준화됨 | Worker Registry 운영 시작 | Worker Registry v1.0 |
| 4 | Dispatcher Report 자동 생성 | Worker Registry 운영 중 | Report 자동 생성 안정화 | Dispatcher Report Generator |
| 5 | Work Order 자동 생성 | Report 자동화 안정화 | Work Order 자동 생성 안정화 | Work Order Generator |
| 6 | Task를 보고 자동으로 Worker 추천 | Work Order 자동화 안정화 | 추천 정확도 검증 완료 | Worker Recommendation Engine |
| 7 | Context Threshold 도달 시 Dispatcher 스스로 운영 (장기 목표) | Stage 6 안정화 + CTI 측정 가능 | — (장기 목표, Exit 미정의) | Autonomous Dispatcher |
