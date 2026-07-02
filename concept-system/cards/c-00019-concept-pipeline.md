# C-00019 : 개념 파이프라인 (Concept Pipeline)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00019 |
| | Coordinate | WF-05 |
| **기본** | 이름(한글) | 개념 파이프라인 |
| | 영문명 / 약어 | Concept Pipeline |
| **정의** | 공식 정의 | Thread에서 발견된 개념이 후보 등록과 반복 검증을 거쳐 자산으로 승격되고 운영 기준 문서에 반영되기까지의 전체 흐름 |
| | 목적 | 개념이 1회성 아이디어로 휘발되지 않고 검증된 자산으로 정착하는 경로를 표준화한다 |
| | 핵심 질문 | 하나의 개념이 발견부터 SoT 반영까지 어떤 단계를 거치는가 |
| **분류** | Type | Workflow |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00013 (AI Company Concept System) *[Forward Reference — 미작성, ID 예약]* |
| | 하위 개념 | C-00001 (개념수확), C-00020 (Review System), C-00021 (Registry System) |
| | 관련 개념 | 없음 |
| | Before(전 단계) | 없음 — Thread 종료가 트리거 |
| | After(후 단계) | 없음 — SoT 반영이 종착점, 다음 개념으로 이어지지 않음 |
| **비교** | 기존 유사 개념 | CI/CD Pipeline, Knowledge Management Pipeline |
| | 차이점 | CI/CD가 코드의 빌드·배포 흐름을 다루는 것과 같은 구조를, 우리는 "개념(Concept)"이라는 비정형 지식 단위에 적용한다. 코드가 아니라 정의·분류·관계를 검증 대상으로 삼는다는 점이 다르다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Pilot 5장을 작성하는 과정에서 개별 카드보다 상위의 흐름(Thread→Harvest→Registry→Review→Asset→SoT)이 반복적으로 드러나 Alpha Review에서 별도 개념으로 식별됨 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 — Alpha Review 결과로 신설 |
| | Review Result | 검토 대기 |
| | Review Notes | — |
| | 비고 | 흐름: Thread → Concept Harvest(C-00001) → Candidate Registry → Promotion Review → Asset Registry → SoT 반영. 각 단계는 Registry System(C-00021), Review System(C-00020)이 구체적으로 관리 |
