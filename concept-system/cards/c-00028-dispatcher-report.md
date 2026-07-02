# C-00028 : 디스패처 리포트 (Dispatcher Report)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00028 |
| | Coordinate | WF-01 |
| **기본** | 이름(한글) | 디스패처 리포트 |
| | 영문명 / 약어 | Dispatcher Report |
| **정의** | 공식 정의 | 디스패처가 현재 작업 흐름의 상태를 공유하기 위한 표준 보고 형식 |
| | 목적 | 사람이 매 순간 개입하지 않아도 전체 진행 상황을 한눈에 파악할 수 있게 한다 |
| | 핵심 질문 | 지금 무엇이 진행 중이고, 무엇이 막혀 있는가 |
| **분류** | Type | Workflow |
| | Status | Candidate |
| | Stability | Experimental *(아직 실제 자동 생성 전 — Dispatcher Roadmap Stage 4 이후 산출물)* |
| **관계** | 상위 개념 | C-00005 (디스패처) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00024 (오픈딜리게이션) |
| | Before(전 단계) | C-00024 (오픈딜리게이션) |
| | After(후 단계) | C-00030 (Work Order) *[Forward Reference — 미작성, ID 예약]* |
| **비교** | 기존 유사 개념 | Standup Report, Status Report, CI/CD Pipeline Dashboard |
| | 차이점 | 일반 Status Report는 사람이 작성하지만, 본 개념은 디스패처(AI 운영자 역할)가 작성 주체라는 점에서 다르다. 또한 단순 현황 나열이 아니라 "다음 위임이 필요한 지점"을 포함하는 운영 도구다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Dispatcher 운영 구조를 설계하는 과정에서 Constitution → Workflow → Report → Work Order → Handoff의 흐름이 정리되며 Workflow 산출물로 정의되었다 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.1 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | v1.0(최초 작성) → v1.1(GPT Review 반영: 정의를 사람+AI 포괄하도록 일반화, Discovery Context를 설계과정 중심으로 수정) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | Dispatcher Report를 "표준 인터페이스"로 보는 관점이 좋게 평가됨. Workflow 전용 Input/Output 필드는 후보로 남기되, 카드 10~20장 누적 후 Manual 개선 검토 |
| | 비고 | Workflow군 첫 카드 — 카드당 리뷰 완료. WF-02~05는 이 템플릿으로 묶음 리뷰 진행 |
