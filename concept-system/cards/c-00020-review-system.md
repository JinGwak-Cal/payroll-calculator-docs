# C-00020 : 리뷰 시스템 (Review System)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00020 |
| | Coordinate | A-04 |
| **기본** | 이름(한글) | 리뷰 시스템 |
| | 영문명 / 약어 | Review System |
| **정의** | 공식 정의 | 개별 Concept Card뿐 아니라 Standard·Manual·Naming·Dictionary 같은 기준 문서 자체를 검토하고 진화시키는 체계 |
| | 목적 | Review가 단순 품질 검사가 아니라 시스템 전체를 발전시키는 엔진임을 명시한다 |
| | 핵심 질문 | 이번 검토에서 무엇이 바뀌어야 하는가 — 카드인가, 운영규칙인가, 시스템 자체인가 |
| **분류** | Type | Architecture |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00019 (개념 파이프라인) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00021 (Registry System) |
| | Before(전 단계) | 없음 |
| | After(후 단계) | 없음 |
| **비교** | 기존 유사 개념 | Code Review, Peer Review, Design Review |
| | 차이점 | 일반 Code/Design Review는 결과물(코드·설계)의 품질을 검사하는 데 그치지만, 본 개념은 검토 대상이 카드 자체일 수도, 카드를 만드는 규격(Standard)일 수도, 운영규칙(Manual)일 수도 있다 — Pilot에서 실제로 후자 둘이 더 자주 바뀌었다 |
| | 용어 유형 | 기존용어확장 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Pilot-001~005를 거치며 "카드는 거의 안 바뀌고 운영규칙만 진화했다"는 패턴이 반복 확인되어, Review 자체가 하나의 독립된 시스템 구성요소임이 Alpha Review에서 식별됨 |
| | Decision Origin | 없음 |
| | Evidence | C-00018 (Pilot 시리즈 자체가 근거 — Manual Rule 11~16이 전부 Review에서 발생) |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 — Alpha Review 결과로 신설 |
| | Review Result | 검토 대기 |
| | Review Notes | — |
| | 비고 | Review 결과가 영향을 줄 수 있는 대상 4종: 개별 Card / Standard / Manual / Naming·Dictionary. 영향 범위에 따라 Review의 무게가 다르다는 점은 아직 별도 필드화하지 않음 — 운영하며 필요성 확인 시 도입 검토 |
