# C-00022 : 컨텍스트 쓰레시홀드 검증 (Context Threshold Verification)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00022 |
| | Coordinate | H-02 |
| **기본** | 이름(한글) | 컨텍스트 쓰레시홀드 검증 |
| | 영문명 / 약어 | Context Threshold Verification |
| **정의** | 공식 정의 | Context Threshold(C-00016) 가설이 다른 프로젝트·다른 AI에서도 재현되는지 확인하는 연구 과제 |
| | 목적 | C-00016을 단일 관찰 기반 가설에서 반복 검증된 이론으로 격상하기 위한 증거를 수집한다 |
| | 핵심 질문 | 이 가설은 본 프로젝트 외에서도 재현되는가 |
| **분류** | Type | Hypothesis *(C-00016이 가설이라면, 본 카드는 그 가설을 검증하는 연구 과제 자체를 개념화한 것 — Theory/Hypothesis 구분에서 "검증 활동"은 Theory가 될 수 없으므로 Hypothesis로 분류)* |
| | Status | Candidate |
| | Stability | Experimental |
| **관계** | 상위 개념 | C-00016 (컨텍스트 쓰레시홀드 — 검증 대상 가설) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00018 (Claude 관찰 사례 — 검증의 출발점), C-00017 (CTI — 검증에 사용할 측정 도구 후보) |
| | Before(전 단계) | C-00018 (단일 관찰) |
| | After(후 단계) | C-00016 *(검증 성공 시 C-00016이 Theory로 승격될 수 있음)* |
| **비교** | 기존 유사 개념 | Replication Study (과학 연구), A/B Test, Validation Study |
| | 차이점 | 일반 Replication Study는 기존 실험을 동일 조건으로 반복하지만, 본 검증은 "운영 Context 성숙도"라는 비정형 변수를 다루므로 측정 프로토콜 자체가 아직 미확정이다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Claude 자율성 관찰(C-00018)이 단일 사례에 그치지 않으려면 재현 검증이 필요하다는 판단에서 별도 개념으로 분리됨 |
| | Decision Origin | 없음 |
| | Evidence | C-00018 (검증의 출발 근거) |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음4-3). ※당초 C-00019로 예약되었으나 Concept Pipeline에 배정되어 Rule 16에 따라 C-00022로 재배정됨 |
| | Review Result | Approved (조건부→승인 전환) |
| | Review Notes | Hypothesis 분류는 현 시점 최선 — Dictionary에 Validation Type 없으므로 유지. Review Backlog: ①Validation Type 독립 필요성(검증 활동 vs 가설의 성격 차이), ②Type Dictionary 상위 분류(운영 계층/설명 계층) — Sprint-1 이후 검토 |
| | 비고 | Theory/Hypothesis 구분: C-00016(가설)→본 카드(검증 활동)→C-00035/C-00036(검증 후 이론으로 흡수 또는 독립) 순서. After가 C-00016(상위 개념)과 동일 대상 — Rule 15 예외: 검증 성공 시 C-00016 자체가 Theory로 승격하는 논리적 귀결이므로 의식적 허용 |
