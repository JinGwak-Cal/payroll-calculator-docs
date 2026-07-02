# Pilot-003 : 컨텍스트 레이어 (Context Layer)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00012 |
| | Coordinate | A-03 |
| **기본** | 이름(한글) | 컨텍스트 레이어 |
| | 영문명 / 약어 | Context Layer |
| **정의** | 공식 정의 | GitHub가 코드를 관리하는 것과 별개로, 프로젝트의 목표·결정·규칙·워크플로우·리뷰·운영 자산(Asset)·학습을 관리하는 계층 |
| | 목적 | "GitHub=Code Layer, AI Company=Context Layer"로 역할을 분리해 운영 맥락을 코드와 독립적으로 관리한다 |
| | 핵심 질문 | 코드가 아닌, 프로젝트의 운영 맥락은 어디서 관리되는가 |
| **분류** | Type | Architecture |
| | Status | Candidate |
| | Stability | Emerging *(D-010으로 한 차례 재정의된 바 있어 아직 표현이 다듬어지는 중)* |
| **관계** | 상위 개념 | C-00013 (AI Company Concept System) *[Forward Reference — 미작성, ID 예약]* |
| | 하위 개념 | C-00001 (개념수확), C-00005 (디스패처) *— 둘 다 Context Layer 안에서 운영되는 절차/역할* |
| | 관련 개념 | C-00014 (merged-context 운영 체계) *[Forward Reference — 미작성, ID 예약]* |
| | Before(전 단계) | 없음 *(Context Layer는 시간/절차상 전후 관계가 아니라 구조 관계 — Rule 15 적용)* |
| | After(후 단계) | 없음 *(상위 개념 C-00013로 구조적 연결, Before/After와 중복 표기하지 않음 — Rule 15)* |
| **비교** | 기존 유사 개념 | Knowledge Layer, Context Management, Context Engineering |
| | 차이점 | 일반적 Context Layer/Knowledge Layer는 AI 모델 입력에 들어가는 정보 자체를 가리키는 경우가 많다. 본 개념은 "코드 위에서 목표·결정·리뷰·학습을 관리하는 계층"이라는 **프로젝트 운영 메타구조**를 가리킨다는 점에서 다르다 — Context Window/Context Engineering과 같은 모델 내부 개념과 혼동 금지 |
| | 용어 유형 | 기존용어확장 |
| | Official Name 후보 | 없음 — 이미 확정되어 사용 중 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | GitHub Layer와 비교되며 D-010("GitHub는 Code Layer, AI Company는 Context Layer")으로 처음 정식화됨. 이후 Concept Harvest 단계에서 추가 보강됨 |
| | Decision Origin | D-010 |
| | Evidence | 없음 |
| **관리** | Version | v1.1 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | v1.0(최초 작성) → v1.1(GPT Review 반영: Before/After를 Rule 15에 따라 제거, 구조관계는 상위/관련 개념으로만 표현) |
| | Review Result | Approved with System Improvements |
| | Review Notes | Before/After는 시간·절차 관계, 상위/하위는 포함 관계 — Context Layer는 Concept System과 시간 선후가 아닌 구조 관계이므로 Before/After를 비움 (Rule 15 첫 적용 사례) |
| | 비고 | 하위 개념으로 Concept Harvest와 Dispatcher를 명시함으로써, 이 둘이 "Context Layer 안에서 운영된다"는 GPT의 Pilot 순서 제안 근거가 카드 구조에도 그대로 반영됨 |

---

## Pilot 검증 메모 (Review 반영 완료)

- Forward Reference 3건(C-00013, C-00014, C-00015) 발생 — Context Layer가 다른 카드들의 공통 기반이라는 위치상 자연스러운 결과.
- **상호 참조 갱신 문제 → Manual Rule 14(Link Consistency Rule)로 해결.** "강제 자동 갱신"이 아니라 "검토" 원칙으로 명문화됨.
- **Before/After와 상위/하위 중복 문제 → Manual Rule 15(Relation Type Consistency)로 해결.** 본 카드가 그 첫 적용 사례 — Before/After를 비우고 상위 개념으로만 연결.
