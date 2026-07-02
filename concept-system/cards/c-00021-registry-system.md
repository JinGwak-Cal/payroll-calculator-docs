# C-00021 : 등록부 시스템 (Registry System)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00021 |
| | Coordinate | A-05 |
| **기본** | 이름(한글) | 등록부 시스템 |
| | 영문명 / 약어 | Registry System |
| **정의** | 공식 정의 | Concept ID의 예약·후보·승격·보관 상태를 각각 관리하는 여러 등록부(Registry)의 집합 |
| | 목적 | 단일 Candidate Registry로는 ID 예약, 후보, 승격, 보관의 서로 다른 생명주기 단계를 구분해 관리할 수 없으므로 역할별로 분리한다 |
| | 핵심 질문 | 이 Concept ID는 지금 어떤 등록부에 속해 있는가 |
| **분류** | Type | Architecture |
| | Status | Candidate |
| | Stability | Experimental *(아직 실제 운영 전, Pilot 단계에서는 텍스트 기반으로만 관리됨)* |
| **관계** | 상위 개념 | C-00019 (개념 파이프라인) |
| | 하위 개념 | 없음 *(하위 4종 Registry는 본 카드의 내부 구성요소로 관리, Manual Rule 12 적용 사례와 동일하게 별도 카드화하지 않음)* |
| | 관련 개념 | C-00020 (Review System) |
| | Before(전 단계) | 없음 |
| | After(후 단계) | 없음 |
| **비교** | 기존 유사 개념 | Database Schema Registry, Service Registry (마이크로서비스), Package Registry (npm 등) |
| | 차이점 | 일반적 Registry는 단일 목적(서비스 위치, 패키지 버전 등)을 관리하지만, 본 시스템은 하나의 Concept ID가 생명주기에 따라 서로 다른 Registry로 이동하는 **상태 기반 다중 Registry** 구조다 |
| | 용어 유형 | 기존용어확장 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Pilot 진행 중 Forward Reference(예약 ID)가 누적되면서 Manual Rule 16(Registry Consistency)이 신설됨. Alpha Review에서 단일 Candidate Registry로는 부족하다는 점이 확인되어 4종 구성으로 식별됨 |
| | Decision Origin | Manual Rule 16 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 — Alpha Review 결과로 신설 |
| | Review Result | 검토 대기 |
| | Review Notes | — |
| | 비고 | 구성: Reserved Registry(예약된 ID, 아직 카드 미작성) / Candidate Registry(Status=Candidate~Repeated 카드) / Asset Registry(Status=Promoted 카드만) / Archived Registry(Status=Deprecated·Archived 카드). Promotion Queue는 Candidate→Asset 전환 대기열로, 별도 Registry가 아니라 Promotion Review(승격심사) 절차의 일부로 본다 |
