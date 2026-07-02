# Pilot-002 : 디스패처 (Dispatcher)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00005 |
| | Coordinate | A-01 |
| **기본** | 이름(한글) | 디스패처 |
| | 영문명 / 약어 | Dispatcher |
| **정의** | 공식 정의 | Worker에게 작업을 위임하고 작업 흐름을 유지하는 운영자 역할. 구현과 품질 판단은 담당하지 않는다 |
| | 목적 | GPT→CodeX→Claude 간 사람의 수동 중계(Relay)를 자동화하기 위한 첫 단계 |
| | 핵심 질문 | 누가 다음 작업을 누구에게 넘길 것인가 |
| **분류** | Type | Architecture |
| | Status | Candidate |
| | Stability | Stable *(역할 정의 자체는 이미 D-PW-027에서 합의·반복 사용 중)* |
| **관계** | 상위 개념 | C-00006 (AI Development OS) *[Forward Reference — 미작성, ID 예약]* |
| | 하위 개념 | C-00007 (역할분리 규칙), C-00008 (Dispatcher Report), C-00009 (Work Order), C-00010 (Rework Order) *[전부 Forward Reference — 미작성, ID 예약]* |
| | 관련 개념 | C-00001 (개념수확 — 동일 쓰레드 내 다른 Architecture 사례) / C-00012 (컨텍스트 레이어) *[Rule 14: Pilot-003에서 본 카드를 하위 개념으로 역참조함]* |
| | Before(전 단계) | C-00007 (역할분리 합의) *[Forward Reference]* |
| | After(후 단계) | C-00011 (Dispatcher Roadmap) |
| **비교** | 기존 유사 개념 | Workflow Orchestrator, Agent Orchestrator, Task Dispatcher |
| | 차이점 | 업계의 Orchestrator/Dispatcher는 대개 작업 스케줄링·라우팅 기능을 가리킨다. 본 개념은 그 기능에 더해 **운영 경계(Operation Boundary)** — 무엇을 하는가(Positive Responsibility: 위임·인계·상태보고)와 무엇을 하지 않는가(Negative Responsibility: 구현·품질평가·승인)를 모두 명시한다는 점이 다르다 |
| | 용어 유형 | 기존용어 *(이름 자체는 업계 표준 용어 그대로 채택. 새로 만든 것은 역할의 경계 정의)* |
| | Official Name 후보 | 없음 — 기존용어 채택 확정 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | "AI Dispatcher를 만들자"는 최초 목표에서 출발했으나, 논의가 진행되며 "AI가 자율적으로 협업할 수 있는 운영 환경을 만들자"는 상위 목표로 확장되는 과정에서 Dispatcher의 역할이 재정의됨 |
| | Decision Origin | D-PW-027 (AI 역할 분리 확정) |
| | Evidence | 없음 *(Type=Architecture, 선택 필드)* |
| **관리** | Version | v1.1 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | v1.0(최초 작성) → v1.1(GPT Review 반영: 정의에 부정책임 포함, After를 C-00011 ID참조로 수정) |
| | Review Result | Approved with Recommendations |
| | Review Notes | "After는 반드시 Concept을 가리켜야 한다"는 원칙 확인 — 로드맵을 별도 카드(C-00011)로 분리. Operation Boundary(긍정/부정 책임) 개념이 Dispatcher 정의의 핵심으로 확인됨 |
| | 비고 | 현재 Dispatcher Stage는 0(사람이 수행) 거의 완료, Stage 1(운영 규칙 확립) 진행 시작 단계 |

---

## Pilot 검증 메모 (Review 반영 완료)

- **"After는 반드시 Concept을 가리켜야 한다"** 원칙 확인. 카드화되지 않은 대상(로드맵 등)을 관계 필드에 텍스트로 적는 것은 금지 — 반드시 먼저 카드(Forward Reference 포함)로 만든 뒤 ID로 참조한다. 이 원칙은 02. Concept Manual에 규칙으로 추가 검토 필요.
- **Dispatcher Roadmap**을 C-00011로 Architecture 카드 신규 작성 완료 (별도 파일).
- Review Notes의 자유텍스트 형식은 유지하되, 패턴이 반복되면(Standard개선/Manual개선/Dictionary개선/Naming개선/System개선) Review Type 분류 도입을 후보로 남김 — 지금은 보류.
