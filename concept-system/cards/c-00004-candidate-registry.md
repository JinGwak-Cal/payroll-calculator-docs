# C-00004 : 후보등록부 (Candidate Registry)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00004 |
| | Coordinate | WF-04 |
| **기본** | 이름(한글) | 후보등록부 |
| | 영문명 / 약어 | Candidate Registry |
| **정의** | 공식 정의 | Concept Harvest를 거쳐 발견된 개념이 Status=Candidate~Repeated 상태로 머무르며 반복 검증을 기다리는 등록부 |
| | 목적 | 검증되지 않은 개념이 곧바로 SoT에 반영되는 것을 막고, 단계적 검증 과정을 거치게 한다 |
| | 핵심 질문 | 이 개념은 충분히 반복 등장했는가 |
| **분류** | Type | Workflow |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00021 (Registry System) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00001 (개념수확), C-00019 (개념 파이프라인) |
| | Before(전 단계) | C-00001 (개념수확) |
| | After(후 단계) | C-00032 (Promotion Review) |
| **비교** | 기존 유사 개념 | Backlog (애자일), Draft Registry, Staging Area (Git) |
| | 차이점 | 일반 Backlog는 우선순위로 정렬된 작업 목록이지만, 본 등록부는 "개념"이라는 비정형 지식 단위가 Status 전이(Candidate→Repeated)를 거치는 곳이라는 점이 다르다 |
| | 용어 유형 | 기존용어조합 |
| | Official Name 후보 | 없음 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | "Promotion Log"라는 초기 명칭에서 출발해, 승격 전 단계임을 명확히 하기 위해 "Candidate Registry"로 재정의됨 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 — Sprint-1 묶음2-4. C-00004는 Concept System 설계 초기 단계에서 이미 예약된 ID를 그대로 사용 |
| | Review Result | Approved |
| | Review Notes | Workflow군 묶음 중 최고 평가. "저장소"가 아닌 "상태 공간"으로서의 정의가 명확하다는 평가 |
| | 비고 | C-00028 템플릿 적용 — Workflow군 묶음 리뷰 대상. Reserved Registry / Asset Registry / Archived Registry와 함께 Registry System(C-00021)의 구성요소 중 하나 |
