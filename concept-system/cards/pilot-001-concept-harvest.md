# Pilot-001 : Concept Harvest (개념수확)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00001 |
| | Coordinate | WF-01 |
| **기본** | 이름(한글) | 개념수확 |
| | 영문명 / 약어 | Concept Harvest (CH) |
| **정의** | 공식 정의 | 쓰레드에서 새로 등장한 개념을 발견하고, 이름을 붙이고, 정의하고, 좌표를 부여하는 과정 |
| | 목적 | 정의되지 않은 용어가 혼용되어 같은 단어를 다르게 이해하는 것을 방지한다 |
| | 핵심 질문 | 이 쓰레드에서 무엇이 새로 발견되었고, 그것을 무엇이라 부를 것인가 |
| **분류** | Type | Workflow |
| | Status | Candidate *(동일 Thread 내 반복은 Repeated 불인정 — 타 Thread 재등장 시 승격)* |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00002 (쓰레드 클로징 파이프라인) *[Forward Reference — 미작성, ID 예약]* |
| | 하위 개념 | C-00003 (Concept Card) *[Forward Reference — 미작성, ID 예약]* |
| | 관련 개념 | C-00004 (후보등록부) *[Forward Reference — 미작성, ID 예약]* / C-00012 (컨텍스트 레이어) *[Rule 14: Pilot-003에서 본 카드를 하위 개념으로 역참조함]* |
| | Before(전 단계) | 없음 — Thread 종료가 트리거, 별도 선행 개념 카드 없음 |
| | After(후 단계) | C-00004 (후보등록부 등록) |
| **비교** | 기존 유사 개념 | Concept Extraction, Knowledge Extraction, Ontology Building |
| | 차이점 | 기존 개념들은 주로 "추출(Extraction)"에 그치지만, 개념수확은 발견 → 명명 → 정의 → 좌표화까지 포함한다. 단순 추출보다 범위가 넓다 |
| | 용어 유형 | 기존용어조합+신개념 *(Concept·Harvest 모두 기존 용어이나, 이 의미 조합으로 쓰는 것은 신규 — Context Threshold와 동일 패턴)* |
| | Official Name 후보 | 없음 — 이미 확정되어 사용 중 |
| **근거** | Origin Thread | Research Thread #001 (AI Dispatcher 설계 → Context Threshold 발견 쓰레드) |
| | Discovery Context | AI Dispatcher 설계 논의 중, 쓰레드 전체를 문서화할지 여부를 고민하다가 "승격된 자산만 넘기면 된다"는 결론에 도달하며 그 사전 단계로 발견됨 |
| | Decision Origin | 없음 (아직 정식 Decision 미등록) |
| | Evidence | 없음 *(Type=Workflow, 선택 필드 — 02. Concept Manual 규칙 11 참조)* |
| **관리** | Version | v1.1 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | v0.x(초안) → v1.0(Standard v1.0 전체 필드 작성) → v1.1(Pilot Review 반영: Status 정정, 용어유형 정정, Discovery Context·Review 필드 추가) |
| | Review Result | Approved with Minor Improvements |
| | Review Notes | Pilot-001 결과 Standard는 안정적으로 작동함을 확인. 보완은 Manual에 집중됨(Forward Reference Rule, Evidence 선택규칙, Repeated 판단기준 신설). 본 카드는 그 발견을 직접 적용한 첫 사례 |
| | 비고 | 본 카드 자체가 Pilot 1호이자, 동시에 "개념수확"이라는 절차를 거쳐 만들어진 첫 산출물 — 메타적으로 자기 자신을 증명하는 카드 |

---

## Pilot 검증 메모 (Review 반영 완료)

작성 과정에서 발견되어 Manual v1.0에 반영된 사항:

- **Forward Reference Rule** 신설 — 미작성 개념을 ID 예약 후 선참조 가능
- **Evidence 필드 선택(Optional)** 규칙 신설 — Type별 권장 기준 명시
- **Repeated 판단 기준** 신설 — 동일 Thread 내 반복은 불인정, 타 Thread 재등장만 인정

결론: Pilot-001을 통해 **Standard 구조 자체는 안정적**이며, 발견된 보완점은 전부 **Manual(운영 규칙)** 영역이었다.

