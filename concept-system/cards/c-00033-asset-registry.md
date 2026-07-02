# C-00033 : 자산 등록부 (Asset Registry)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00033 |
| | Coordinate | B-02 |
| **기본** | 이름(한글) | 자산 등록부 |
| | 영문명 / 약어 | Asset Registry |
| **정의** | 공식 정의 | 승격 심사(C-00032)를 통과한 Concept만 등재되는 최종 등록부 |
| | 목적 | Candidate Registry(C-00004)와 분리하여 "검증된 자산"과 "검증 중인 후보"를 명확히 구분하고, SoT 반영 대상을 단일 진실원천으로 관리한다 |
| | 핵심 질문 | 이 개념은 공식 운영 자산으로 인정받았는가 |
| **분류** | Type | Business *(검증·승격 절차의 산출물이자 AI Company의 공식 운영 자산(Official Operational Assets) 집합체 — 운영 가치를 직접 실현하는 Business 개념)* |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00021 (Registry System) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00004 (Candidate Registry — 선행 단계), C-00032 (Promotion Review — 진입 조건) |
| | Before(전 단계) | C-00032 (Promotion Review) |
| | After(후 단계) | C-00039 (SoT Integration) *[Forward Reference — 미작성, ID 예약. Architecture군 또는 Sprint-2 이후 카드화 검토]* |
| **비교** | 기존 유사 개념 | Master Data Registry, Configuration Management Database (CMDB), Knowledge Base |
| | 차이점 | CMDB는 IT 인프라 구성 요소를 관리하고, Knowledge Base는 정보를 수집·저장한다. 본 등록부는 "반복 검증을 통과한 개념"만 등재한다는 점에서 엄격한 진입 기준을 갖는다 — 품질 보증된 지식 자산만의 목록이다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | 검증을 통과한 개념과 아직 검증 중인 후보를 분리해 관리할 필요가 명확해지면서, "운영 자산(Operational Asset)"이라는 개념이 정립되고 그 최종 목록으로 정의됨 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음5-2) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | ①Business에 Official Operational Assets 표현 보강. ②After를 텍스트→C-00039(SoT Integration, Forward Reference)로 변경. ③Discovery Context를 운영 자산 관리 관점으로 일반화. Review Backlog: SoT Integration 카드화 여부(Architecture군 검토), Registry Lifecycle 시각화 |
| | 비고 | Registry System(C-00021) 구성: Reserved→Candidate→**Asset**→Archived 4단계 중 3번째. C-00039(SoT Integration)는 Architecture군 또는 Sprint-2에서 카드화 결정 예정 |
