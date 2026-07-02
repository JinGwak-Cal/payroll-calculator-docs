# C-00023 : 워커-리뷰어-디스패처 권한분리 (Role Separation)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00023 |
| | Coordinate | R-01 |
| **기본** | 이름(한글) | 워커-리뷰어-디스패처 권한분리 |
| | 영문명 / 약어 | Role Separation |
| **정의** | 공식 정의 | Worker(구현), Reviewer(품질 판단 및 거부권), Dispatcher(위임·인계·운영)를 서로 독립된 권한으로 분리하는 운영 규칙 |
| | 목적 | 역할 충돌로 인한 책임 소재 불명확과 권한 남용을 방지한다 |
| | 핵심 질문 | 이 작업에서 누가 결정하고, 누가 만들고, 누가 검사하는가 |
| **분류** | Type | Rule |
| | Status | Repeated *(D-PW-027에서 합의 후 본 쓰레드에서도 반복 적용됨 — 서로 다른 쓰레드 간 재등장 확인)* |
| | Stability | Stable |
| **관계** | 상위 개념 | C-00027 (AI Development OS) *[Forward Reference — 미작성, ID 예약. Role Separation은 Dispatcher보다 먼저 존재하는 원칙이며, Dispatcher 역시 이 규칙을 따르는 하위 존재이므로 더 상위의 아키텍처 개념 아래 위치하는 것이 자연스러움]* |
| | 하위 개념 | C-00024 (오픈딜리게이션), C-00025 (리뷰어우선권), C-00026 (디스패처비구현) |
| | 관련 개념 | C-00005 (디스패처) |
| | Before(전 단계) | 없음 — 출발 원칙 |
| | After(후 단계) | C-00024 (오픈딜리게이션) |
| **비교** | 기존 유사 개념 | Separation of Concerns, RACI Matrix |
| | 차이점 | RACI는 일반적 책임 배분 프레임워크이지만, 본 규칙은 AI 협업이라는 특정 맥락에서 "구현 vs 운영 vs 품질판단"이라는 3분할에 특화되어 있다 |
| | 용어 유형 | 기존용어확장 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | AI Dispatcher 설계 초기 논의에서 GPT/CodeX/Claude/AI Push/사용자의 역할이 뒤섞이는 문제가 반복되어, D-PW-027로 역할 분리가 먼저 확정됨 |
| | Decision Origin | D-PW-027 |
| | Evidence | 없음 |
| | Version | v1.1 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | v1.0(최초 작성) → v1.1(GPT Review 반영: 정의 Authority 중심화, 상위개념을 AI Development OS로 변경, 관련개념에 Dispatcher 추가) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | 정의를 Role 중심에서 Authority 중심으로 수정. 상위 개념을 Dispatcher에서 더 일반적인 AI Development OS(C-00027, Forward Reference)로 변경 — Role Separation이 Dispatcher보다 먼저 존재하는 원칙이라는 판단. 관련 개념에 Dispatcher(C-00005) 추가 |
| | 비고 | Rule군 첫 카드 — 카드당 리뷰 대상. 본 카드의 분류·필드 적용 방식이 R-02~04의 템플릿이 됨. ID 예약 충돌(C-00026 중복) 발견 후 Rule 16에 따라 즉시 정정한 사례이기도 함 |
