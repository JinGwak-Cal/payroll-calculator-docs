# C-00014 : merged-context 운영체계 (merged-context Operating Structure)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00014 |
| | Coordinate | A-07 |
| **기본** | 이름(한글) | merged-context 운영체계 |
| | 영문명 / 약어 | merged-context Operating Structure |
| **정의** | 공식 정의 | 프로젝트 핵심 운영 정보를 하나의 구조화된 Context로 통합하여 AI가 일관된 작업 상태를 이어받을 수 있도록 하는 운영 구조 |
| | 목적 | 쓰레드 전환 시 AI가 매번 전체 이력을 재학습하지 않고, 압축된 Context 하나로 이전 작업을 이어받을 수 있게 한다 |
| | 핵심 질문 | AI가 새 쓰레드에서 프로젝트 Context를 가장 효율적으로 이어받으려면 어떤 구조가 필요한가 |
| **분류** | Type | Architecture |
| | Status | Repeated *(본 프로젝트에서 매 쓰레드 시작마다 읽기 검증 프로토콜로 반복 사용됨)* |
| | Stability | Stable *(실제 운영에서 검증된 구조)* |
| **관계** | 상위 개념 | C-00013 (AI Company Concept System) |
| | 하위 개념 | 없음 *(absolute-rules·current-step·decisions는 본 카드의 구성 문서이나 별도 Concept 카드 아님)* |
| | 관련 개념 | C-00012 (Context Layer — merged-context가 실현하는 Context 관리 계층), C-00016 (컨텍스트 쓰레시홀드 — merged-context 성숙이 Threshold 도달의 전제조건) |
| | Before(전 단계) | 없음 *(쓰레드 시작 시 첫 번째로 읽히는 구조 — 선행 개념 없음)* |
| | After(후 단계) | C-00019 (개념 파이프라인 — merged-context 확보 후 파이프라인 운영 시작) |
| **비교** | 기존 유사 개념 | Context Window Management, System Prompt, Memory Module |
| | 차이점 | System Prompt는 단일 지시문이고 Memory Module은 외부 저장소 연동이지만, merged-context는 프로젝트의 절대 규칙·현재 단계·핵심 결정을 하나의 구조화된 문서로 압축해 AI가 읽는 방식이다 — 외부 의존 없이 문서 자체가 Context 전달 수단이 된다 |
| | 용어 유형 | 기존용어조합+신개념 |
| | Semantic Boundary | merged-context는 Context 자체가 아니라 Context를 전달하는 운영 구조다. Context Layer(C-00012)는 개념 계층(프로젝트의 목표·결정·규칙·워크플로우를 관리하는 계층)이고, merged-context는 그 계층을 실제 문서 형태로 구현한 운영 메커니즘이다 |
| **근거** | Origin Thread | Research Thread #001 (이전 쓰레드부터 운영 중) |
| | Discovery Context | 쓰레드 전환 시 AI가 이전 Context를 잃어버리는 문제를 해결하기 위해 핵심 운영 정보를 단일 파일로 통합하는 방식이 반복 검증을 거쳐 표준 운영 방식으로 확립됨 |
| | Decision Origin | 없음 |
| | Evidence | C-00018 (Claude 자율성 관찰 사례 — merged-context 운영 후 자율성 향상이 관찰됨) |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음6-2) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | ①정의를 구현 방식(세 문서 병합)→운영 목적(핵심 운영 정보 통합) 중심으로 일반화. ②Semantic Boundary 추가 — Context Layer(개념 계층)와 merged-context(구현 메커니즘) 역할 분리 명시. ③Discovery Context를 "자연 발생적 정착"→"반복 검증을 거쳐 표준 운영 방식으로 확립"으로 개선. Backlog: Architecture Diagram 문서화 여부 — Sprint-1 완료 후 검토 |
| | 비고 | 본 운영체계는 이미 운영 중인 실체이므로 Status=Repeated, Stability=Stable이 가장 낮은 신뢰 등급이 아님에 주목 — Pilot 단계 이전부터 사용된 유일한 카드. 구성 문서(absolute-rules·current-step·decisions) 중 어느 하나라도 누락되면 읽기 검증 실패로 처리한다 |
