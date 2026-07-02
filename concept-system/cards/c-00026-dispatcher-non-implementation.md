# C-00026 : 디스패처 비구현 원칙 (Dispatcher Non-Implementation)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00026 |
| | Coordinate | R-04 |
| **기본** | 이름(한글) | 디스패처 비구현 원칙 |
| | 영문명 / 약어 | Dispatcher Non-Implementation |
| **정의** | 공식 정의 | 디스패처는 어떤 경우에도 직접 코드를 구현하거나 결과물을 평가하지 않는다는 권한 제약 규칙 |
| | 목적 | 디스패처 역할이 Worker(구현) 또는 Reviewer(평가) 영역으로 침범되는 것을 방지한다 |
| | 핵심 질문 | 디스패처가 절대 하지 않는 일은 무엇인가 |
| **분류** | Type | Rule |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00023 (역할분리) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00005 (디스패처) |
| | Before(전 단계) | C-00023 (역할분리) |
| | After(후 단계) | 없음 |
| **비교** | 기존 유사 개념 | Separation of Duties (보안/회계 분야의 직무분리 원칙) |
| | 차이점 | Separation of Duties는 보통 부정행위 방지가 목적이지만, 본 원칙은 AI 운영자 역할이 본연의 기능(연결·운영) 밖으로 확장되어 권한이 비대해지는 것을 막는 데 목적이 있다 |
| | 용어 유형 | 기존용어확장 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Pilot-002(Dispatcher 카드) Review에서 "Operation Boundary(긍정/부정 책임)"가 Dispatcher 정의의 핵심으로 확인되며, 그 부정 책임 축이 별도 Rule로 분리됨 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음1-4) |
| | Review Result | Approved |
| | Review Notes | 묶음1(Rule군) 일괄 승인. Pilot-002의 Positive/Negative Responsibility 중 Negative 축을 독립 Rule로 분리한 설계가 적절하다고 평가됨 |
| | 비고 | C-00023 템플릿 적용 — Rule군 묶음 리뷰 대상. Pilot-002에서 GPT가 제안한 "Positive/Negative Responsibility" 중 Negative 축이 본 규칙으로 구체화됨 |
