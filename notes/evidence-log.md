# Evidence Log

이 문서는 merged-context 자동 포함 대상이 아니다.
CMP/ER/TM/TCA 등 Methodology 작성 시점에만 참조한다.

---

## Evidence Model — L0 Hypothesis

### Candidate Entry Criteria
Candidate가 되려면 아래를 모두 충족해야 한다:
- 실제 운영에서 발생한 사건이어야 한다
- 관찰 가능한 사실이어야 한다
- 재현 가능성을 가져야 한다
- 향후 판단에 영향을 줄 가능성이 있어야 한다

### Candidate → Accepted Promotion Criteria
동일한 Hypothesis를 지지하는 독립적인 운영 Evidence가 축적되어,
Evidence가 우연을 설명하기보다 Hypothesis를 더 잘 설명하게 되는 순간 Accepted로 전환한다.
(N회 등 숫자 기준은 정의하지 않음 — Threshold는 Count가 아니라 Confidence의 질적 변화)

### Lifecycle
Candidate → Accepted → Supporting → Archived

Accepted 이후 단계(Supporting/Archived) 전환 기준은 아직 미정의.
(Accepted 사례가 실제로 나온 뒤 역으로 설계 예정 — Evidence First 원칙)

---

## E-001

- Date: 2026-07-03
- Trigger: CMP→ER→TM 순서 변경 제안, current-step.md 갱신 여부 논의
- Observation: current-step 갱신 제안이 있었다. Partner Review와 Human Review를 거친 후, 갱신하지 않기로 결정했다.
- Hypothesis: Review와 Decision 사이에 Operational Confirmation이라는 별도 Gate가 없으면 State 문서가 검증 안 된 상태로 갱신될 수 있다.
- Derived Hypothesis: "Model First, Storage Second" — Model/기준을 먼저 정의하지 않고 Storage/Implementation을 먼저 제안하면 재작업 위험이 생긴다.
- Status: Candidate

---

## Cost Model (Observation Framework)

Taxonomy는 관찰을 위한 Frame이며 Evidence 없이도 설계 가능하다.
각 Category 자체는 분류이고, Category 아래 붙는 Principle만 Evidence를 요구한다.

Governance Cost      — Evidence 있음 (E-001)
Resource Cost        — Evidence 없음
Interaction Cost      — Evidence 없음
Communication Cost    — Evidence 없음
Recovery Cost         — Evidence 없음

빈 Category는 삭제하지 않고, 확정하지도 않는다. Evidence가 들어오면서 채워진다.
