# C-00031 : 리워크 오더 (Rework Order)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00031 |
| | Coordinate | WF-03 |
| **기본** | 이름(한글) | 리워크 오더 |
| | 영문명 / 약어 | Rework Order |
| **정의** | 공식 정의 | Reviewer가 품질 거부권을 행사했을 때 재작업을 지시하는 표준 양식 |
| | 목적 | 품질 미달 시 재작업 절차를 표준화하여 즉흥적 재지시로 인한 혼선을 막는다 |
| | 핵심 질문 | 무엇이 부족했고, 무엇을 다시 해야 하는가 |
| **분류** | Type | Workflow |
| | Status | Candidate |
| | Stability | Experimental |
| **관계** | 상위 개념 | C-00005 (디스패처) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00025 (리뷰어우선권) |
| | Before(전 단계) | C-00025 (리뷰어우선권 행사) |
| | After(후 단계) | 없음 *(완료 또는 재반복 — 단일 다음 개념으로 특정 안 됨)* |
| **비교** | 기존 유사 개념 | Bug Report, Change Request, Revision Request |
| | 차이점 | 일반 Bug Report는 결과물의 결함을 기록하는 데 그치지만, 본 개념은 Reviewer Quality Veto(C-00025) 권한 행사의 직접적 결과물로서 디스패처-Worker 간 공식 재위임 문서라는 점이 다르다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Dispatcher 운영 구조를 설계하는 과정에서 Constitution → Workflow → Report → Work Order → Handoff의 흐름이 정리되며 Workflow 산출물로 정의되었다 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음2-3) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | Workflow군 묶음 승인. 발행 주체(Reviewer=Trigger, Dispatcher=Issuer 가능성)는 Dispatcher Constitution 작성 시 정리 — 정의 변경은 보류 |
| | 비고 | C-00028 템플릿 적용 — Workflow군 묶음 리뷰 대상. **추후과제**: 발행 주체 명확화(Constitution 단계) |
