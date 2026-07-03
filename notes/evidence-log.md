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
---

## E-002

- Date: 2026-07-03
- Trigger: GitHub 웹 UI/CLI 조작 안내가 동일 세션 내 3회 이상 반복 실패
  (백틱 형식, 커밋 메시지란 위치, notes/notes 경로 중복)
- Observation: 각 실패마다 Claude가 현재 상태를 확인하지 않고 조작을 제안했고,
  실패 후에도 원인 진단 없이 같은 접근을 재시도했으며,
  이전에 이미 성공한 방법(CLI)이 있었음에도 검증 안 된 방법(웹 UI 추측)을 먼저 제시했다.

- Derived Principle (Candidate):

  1. Context First, Instruction Second
     명령이나 조작 방법을 생성하기 전에 현재 상태(Context)를 먼저 확인한다.

  2. Diagnose Before Retry (Diagnosis Gate)
     반복 실패가 발생하면 즉시 재시도하지 않는다. 먼저 Diagnosis Gate를 통과한다.
     Diagnosis Gate:
       1) Context를 다시 확인한다
       2) 실패의 Root Cause를 규명한다
       3) 가능한 대안들을 기회비용(Opportunity Cost) 기준으로 비교한다
       4) 그중 이전에 뚜렷한 성공 경험이 있는 방법을 우선하여 다음 시도를 결정한다
       5) 성공 경험이 있는 방법이 없는 경우, 기존 절약 원칙(R8~R17)을 따라 제안한다 —
          전체 재출력 금지, 변경분만 제시

- Status: Candidate (같은 세션 내 3회 이상 재현 — 일반적 기준보다 근거가 강함)

- Note: "Diagnosis Gate를 Run Mode/Thinking Mode 전환 임계점으로 볼 수 있다"는 아이디어가 논의됨.
  다만 이미 정의된 Threshold(Evidence→Confidence 전환) 개념과 의미가 겹치므로,
  지금은 Candidate Principle에 포함하지 않고 별도 관찰로만 남긴다.