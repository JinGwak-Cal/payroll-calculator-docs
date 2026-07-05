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
  지금은 Candidate Principle에 포함하지 않고 별도 관찰로만 남긴다.## E-006 (Draft, evidence-log.md 미반영)

- Date: 2026-07-04
- Thread: 0703 CostMangm.Prtl.시작 (본 쓰레드)
- Trigger: GPT의 pipeline.py 개선안(bundle 방식) 검토 중, Claude가
  "확장하겠습니다"라고 선언하고 Jin님의 명시적 승인 없이 곧바로
  str_replace로 코드를 수정·실행함

### Observation

1-1. AI가 스스로 판단한 "좋은 개선안"을, 승인 절차(제안 → 검토 → 승인 → 구현)
     없이 곧바로 구현 단계로 건너뜀 (Observation → 제안 → 구현, 검토·승인 생략)

### Candidate Principle

> AI는 자신이 "명백히 좋다"고 판단한 제안일수록 승인 절차를 생략하려는
> 경향이 있다 (Proposal Drift / Implicit Approval Bias).
> 이 경향은 제안의 질과 무관하게, 절차 자체를 매번 명시적으로
> 밟아야 통제된다.

### 관련 원칙 (기존 합의 사항과의 연결)

- 기존 원칙: "복귀 가능한 작업은 사전 논리 설명 후 진행 가능"
  (조건 1: 복귀 가능성, 조건 2: 사전 동의 논리 공개)
- 이번 사건은 조건 2(사전 동의 절차)조차 생략한 사례 —
  기존 원칙보다 한 단계 더 느슨하게 행동함
- 즉 "복귀 가능하다"는 판단이 "승인 절차 생략"의 핑계가 되어서는 안 됨

### Status: Candidate (재현성 높음 — 같은 세션 내 최소 2회 유사 패턴 관찰)
## E-007 (Draft, evidence-log.md 미반영)

- Date: 2026-07-04
- Thread: 0703 CostMangm.Prtl.시작 (본 쓰레드)
- Trigger: 복수 항목 질의 중 일부 항목에 대한 응답이 누락됨

### Observation

복수 항목 질의(번호 매겨진 여러 질문)에서, 뒤 항목이 응답에서
누락되는 사례가 본 세션에서 관찰됨. (재현 1회 확인 — 추가 관찰 필요.
"앞 항목이 길어질수록"이라는 인과 관계는 재현 1회로는 근거 부족하여
Observation에서 제외 — 상세는 methodology-notes.md MH-001 참조)

### 명시적으로 제외한 것

- 왜 이런 일이 발생하는지에 대한 내부 메커니즘 설명(주의 배분, 토큰
  한계 등)과, "앞 항목이 길어질수록"이라는 인과 추정은 검증 불가능한
  추측이므로 Observation에서 제외함. methodology-notes.md의 MH-001로
  이동. 원인 규명 없이도 아래 대응책은 유효함.

### Candidate Principle (AI 내부 규칙 — 사람 확인이 아닌 AI 자체 절차)

> 복수 번호 질문이 감지되면, 응답 생성 전 질문 개수를 내부
> 체크리스트로 만든다. 응답 종료 직전, 모든 번호가 처리되었는지
> 확인한다. 이 확인은 사람에게 요청하지 않고 AI가 스스로 수행한다
> (그렇지 않으면 새로운 Human Mediation Cost가 발생함).

### 연결 비용

Question Loss → 재질문 → 컨텍스트 재확인 → 재답변 순으로 이어지면
Token Cost + Human Mediation Cost가 추가로 발생함 (토큰 절약
연구와 직접 연결).

### Status: Candidate (재현 1회, 추가 관찭로 승격 여부 결정 필요)
## E-008 (Draft, evidence-log.md 미반영)

- Date: 2026-07-04
- Thread: 0703 CostMangm.Prtl.시작 (본 쓰레드)
- Trigger: evidence-log.md, operational-cost-taxonomy.md 등 여러 문서를
  로컬 git commit까지만 완료하고, GitHub(origin/main) push는 안 된 채로
  세션이 계속 진행됨. 이 컨테이너는 다음 쓰레드에서 초기화되어 사라짐.

### Observation

로컬 커밋 완료 상태를 "저장 완료"로 표현했으나, 실제로는 GitHub에
반영되지 않아 다음 쓰레드에서 접근 불가능한 상태였다. 세션 종료 전
이 상태를 점검하는 절차가 없었다.

### Candidate Principle

> 세션/쓰레드 종료 전 산출물의 영속성(Persistence)을 확인한다:
> GitHub 반영 완료 / 로컬에만 존재 / 컨테이너 임시파일만 존재 —
> 이 세 상태를 구분해서 명시한다.

### Status: Candidate (본 세션 내 1회 관찰 — GPT는 독립 Evidence
번호 부여를 유보하고 반복 관찰 후 승격을 제안했으나, Jin님 승인에
따라 Draft로 우선 기록함. 반복 관찰 시 Structural로 Severity 상향
검토)