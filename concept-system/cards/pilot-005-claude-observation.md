# Pilot-005 : 클로드 컨텍스트 쓰레시홀드 관찰 사례 (Claude Context Threshold Observation)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00018 |
| | Coordinate | CS-01 |
| **기본** | 이름(한글) | 클로드 컨텍스트 쓰레시홀드 관찰 사례 |
| | 영문명 / 약어 | Claude Context Threshold Observation (CS-01) |
| **정의** | 공식 정의 | 본 프로젝트에서 Claude가 특정 시점 이후 사람에게 묻는 질문 빈도가 줄고 자율적 판단을 내리는 비중이 늘어난 단일 관찰 사례 |
| | 목적 | Context Threshold(C-00016) 가설의 최초 경험적 근거를 기록한다 |
| | 핵심 질문 | 실제로 어떤 시점에, 무엇이 바뀌었는가 |
| **분류** | Type | Case Study |
| | Status | Candidate |
| | Stability | Experimental *(단일 사례, 재현 검증 전)* |
| **관계** | 상위 개념 | C-00016 (컨텍스트 쓰레시홀드) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00022 (컨텍스트 쓰레시홀드 검증) *[Forward Reference — 미작성, ID 예약. 본 사례의 재현 검증을 위한 후속 연구. ※당초 C-00019로 예약되었으나 Concept Pipeline에 배정되어 Rule 16에 따라 C-00022로 재배정]* |
| | Before(전 단계) | 없음 *(관찰 시작점 — 선행 개념 없음)* |
| | After(후 단계) | C-00022 (컨텍스트 쓰레시홀드 검증) |
| **비교** | 기존 유사 개념 | (학술) Case Study, Anecdotal Evidence |
| | 차이점 | 일반적 Case Study 방법론과 동일하나, 본 사례는 **단일 관찰**이며 통제군이나 반복 실험 없이 기록된 1차 관찰이라는 점에서 엄밀한 학술 Case Study보다 신뢰도가 낮다. 이 한계를 명시적으로 인정하고 일반화하지 않는다 |
| | 용어 유형 | 기존용어 |
| | Official Name 후보 | 없음 — 비공식 별칭으로 "Claude Threshold" 사용 가능하나 공식 채택 보류. 공식 용어는 Context Threshold(C-00016) 유지 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | "왜 Claude는 어느 순간 갑자기 자율적으로 변했을까?"라는 질문에서 직접 관찰된 현상. 이 질문을 끝까지 추적한 결과가 Context Threshold(C-00016) 가설로 이어짐 — 즉 본 사례가 가설보다 시간상 먼저 존재함 |
| | Decision Origin | 없음 |
| | Evidence | 없음 *(Type=Case Study이므로 Manual Rule 12상 Evidence 필드는 필수이나, 본 카드 자체가 다른 카드의 Evidence 역할을 하는 최하단 노드 — 추가 근거 카드 없음, 관찰 기록 자체가 근거)* |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Pilot-005, Pilot 시리즈 마지막 카드) |
| | Review Result | 검토 대기 |
| | Review Notes | — |
| | 비고 | Pilot 5장 중 유일한 Case Study. 일반화 금지 원칙(Manual에 명문화되어 있지 않음 — 검토 포인트)을 카드 차이점 필드에서 직접 경고함 |

---

## Pilot 검증 메모 — 시리즈 종합

- **Evidence 필수 규칙(Rule 12)이 처음으로 한계에 부딪힘.** Case Study는 Evidence가 필수라는 규칙이지만, 본 카드 자체가 "최하단 1차 관찰"이라 더 근거할 카드가 없다. **Evidence 필드가 "다른 카드를 가리키는 것"만 의미하는지, 아니면 "관찰 기록 자체"도 Evidence로 인정되는지 Manual에 명시 필요.**
- **"일반화 금지" 원칙이 카드 텍스트로만 존재하고 Manual 규칙으로는 없음.** Case Study Type 카드 전반에 적용될 공통 원칙이라면 Manual에 명문화하는 게 일관적일 것으로 보임.
- Before가 비어 있고 상위 개념(C-00016)과 시간순으로는 오히려 본 카드가 더 먼저인 역설적 구조 — "발견 순서(시간)"와 "개념체계상 포함관계(상위/하위)"가 반대 방향일 수 있다는 사실이 처음 드러남. Rule 15 적용 범위를 한 번 더 점검할 가치 있음.

---

## Pilot 시리즈 종합 (001~005)

5개 카드 모두 작성 완료. Standard/Manual은 Pilot을 거치며 Rule 11~16까지 6개 규칙이 신설되었고, 그중 3건(11,12,15)은 Pilot-001~004 단계에서, 1건(16)은 Review 단계에서, 이번 005에서 2건의 추가 검토 포인트(Evidence의 "기록 자체" 인정 여부, 일반화 금지 원칙의 명문화 여부)가 새로 발견되었다.

확인된 사항: **Standard(카드 규격) 자체는 5개 카드 전체에서 구조적으로 무너진 적이 없다.** 모든 보완은 Manual(운영 규칙) 또는 카드 내 개별 처리로 흡수되었다.
