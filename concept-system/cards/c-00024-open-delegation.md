# C-00024 : 오픈 딜리게이션 (Open Delegation)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00024 |
| | Coordinate | R-02 |
| **기본** | 이름(한글) | 오픈 딜리게이션 |
| | 영문명 / 약어 | Open Delegation |
| **정의** | 공식 정의 | 디스패처가 특정 Worker를 지정 강제하지 않고, 적합한 Worker가 스스로 작업을 수락하도록 위임하는 권한 행사 방식 |
| | 목적 | Worker의 자율성을 보장하고 디스패처가 작업 배정 권한을 과도하게 행사하지 않도록 제한한다 |
| | 핵심 질문 | 디스패처는 작업을 누구에게, 어떻게 위임하는가 |
| **분류** | Type | Rule |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00023 (역할분리) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00005 (디스패처) |
| | Before(전 단계) | C-00023 (역할분리) |
| | After(후 단계) | C-00028 (Dispatcher Report) *[Forward Reference — 미작성, ID 예약]* |
| **비교** | 기존 유사 개념 | Pull-based Task Assignment, Self-assignment (애자일/칸반에서 흔함) |
| | 차이점 | 일반적 Pull 방식은 사람 팀원이 자발적으로 작업을 가져가는 것을 의미하지만, 본 개념은 AI Worker 간 위임에서 디스패처가 **강제 배정을 하지 않는다는 권한 제약**으로서 정의된다 |
| | 용어 유형 | 기존용어조합+신개념 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Dispatcher 설계 논의 중 "Dispatcher는 평가하지 않는다"는 원칙과 함께, 위임 방식 자체도 강제가 아니어야 한다는 방향으로 발전 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음1-2) |
| | Review Result | Approved |
| | Review Notes | 묶음1(Rule군) 일괄 승인. 정의를 "응답"에서 "수락"으로 일반화(GPT 권고 반영) |
| | 비고 | C-00023 템플릿 적용 — Rule군 묶음 리뷰 대상 |
