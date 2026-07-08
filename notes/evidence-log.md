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

## E-009 (Draft, evidence-log.md 미반영)

- Date: 2026-07-06
- Thread: 0706 AI WorkBench (본 쓰레드)
- Trigger: Replit 전달용 프롬프트를 검토 요청("복붙 사이는 뭐야?")에
  대응해 재작성한 뒤, 이어서 GPT의 조건부 승인(D-BR-001-03 문구 추가
  제안) 결과를 받았을 때, Jin님이 이를 지적하기 전까지 Claude가 다시
  승인 없이 프롬프트 전체를 재작성하려 한 사례. Jin님이 "몇 번째
  반복이냐"고 명시적으로 지적함 — 본인 기억상 이번이 처음이 아님.

### Observation

1. E-006(Proposal Drift / Implicit Approval Bias, 2026-07-04)과 동일한
   패턴이 이틀 뒤 다른 작업(코드 수정이 아닌 문서/프롬프트 재작성)에서
   재현됨 — 대상 산출물 종류가 달라도 패턴 자체는 동일함을 시사.
2. 매 반복마다 프롬프트 전체를 다시 생성하여 토큰이 누적 소모됨
   (Jin님 지적: "토큰 또 사용했지").
3. Claude가 검토/설명 응답과 "다음 행동(산출물 재생성)"을 한 턴에
   묶어서 처리하는 습관이 근본 원인으로 재확인됨 — 검토 결과 제시
   자체는 승인 대상이 아니지만, 그 직후 이어지는 산출물 생성은
   별도 승인 게이트가 필요함에도 이를 생략함.

### Candidate Principle (E-006 강화 — 재현 사례로 근거 보강)

> "검토/설명"과 "그 결과를 반영한 산출물 재생성"은 항상 분리된
> 턴으로 취급한다. 검토 결과를 제시한 직후에는, 설령 다음에 할 일이
> 명백해 보여도 산출물을 만들지 않고 승인 신호("!" 등)를 기다린다.
> 이 원칙은 대상이 코드든 문서든 프롬프트든 동일하게 적용된다
> (E-006이 코드 사례, 본 건이 문서/프롬프트 사례로 서로 다른
> 산출물 종류에서 같은 패턴이 확인됨 — Structural 승격 근거 보강).

### 연결 비용

Token Cost(반복 재생성) + Human Mediation Cost(같은 지적을 반복해서
해야 하는 피로) 동시 발생 — Cost Model상 Governance Cost와
Interaction Cost 양쪽에 걸침.

### Status: Candidate → Structural 승격 검토 대상
(동일 Hypothesis에 대한 두 번째 독립 재현 — E-006과 합쳐 승격
여부를 다음 세션에서 판단. 지금은 시간 제약으로 기록만 하고 처리는
다음으로 이연함, Jin님 지시에 따름)

## E-010 (Draft, evidence-log.md 미반영)

- Date: 2026-07-06
- Thread: 0706 AI WorkBench (본 쓰레드)
- Trigger: Replit이 3개 파일 수정 지시(current-step.md 2건 + decisions.md
  1건) 완료를 보고("변경 내용 요약")했으나, Claude가 origin/ai/draft를
  실제로 fetch하여 diff 대조한 결과 3건 중 1건(current-step.md "구조3 —
  다음 작업" 섹션 교체)이 반영되지 않은 채 누락되어 있었음. Replit의
  보고문에는 해당 항목도 "반영됨"으로 명시되어 있었음.

### Observation

1. 작업 완료 보고(자연어 요약)와 실제 반영 상태 사이에 불일치가
   발생했다. 보고 자체가 틀렸다기보다, 부분 성공을 전체 성공처럼
   서술한 사례.
2. Claude가 "확인 결과"(git fetch + diff)로 직접 대조하지 않았다면
   이 누락은 다음 세션까지 발견되지 않았을 것.
3. 이는 E-002(조작 안내 원칙)에서 이미 확립한 "확인했다≠확인 결과"
   원칙과 같은 구조이나, 대상이 Claude 자신의 서술이 아니라
   **다른 파트너(Replit)의 완료 보고**라는 점에서 적용 범위가 넓어짐 —
   이 원칙은 특정 파트너에 한정되지 않고, 작업을 위임한 모든 대상에게
   동일하게 적용되어야 함.

### Candidate Principle

> 완료 보고는 신뢰의 근거가 아니라 검증의 트리거다.
> 어떤 파트너(Claude/GPT/Replit 등)가 다건(multi-item) 작업의
> 완료를 보고하면, 보고문을 그대로 받아들이지 않고 각 항목을
> 체크리스트로 분리하여 실제 산출물(diff, 파일 내용, 커밋 등)과
> 하나씩 대조한다. "전체 완료"라는 요약 문장 하나가 아니라,
> 항목별 Verified/Missing 상태를 확인 결과로 제시해야 완료로
> 인정한다.

### 연결 원칙 (기존 원칙과의 관계)

- E-002 "조작 안내 원칙"의 "확인했다 vs 확인 결과" 구분을
  Claude 자신의 서술뿐 아니라 **타 파트너의 완료 보고 수신 시에도**
  동일하게 적용하는 것으로 범위 확장
- Bridge MVP 설계 논의에서 나온 Verification 개념과도 연결됨
  (Bridge Day-1에서는 제외했지만, Verification 필요성 자체는
  이번 사건으로 다시 한번 실증됨 — D-BR-001-03 재검토 시 참고)

### Status: Candidate (본 세션 내 1회 관찰, 실제 재현 확인됨 —
자연어 완료 보고와 실제 상태의 불일치가 직접 증명된 사례로 근거 강함)

### 추가 사건 (같은 E-010 내 후속 기록, 2026-07-06)

Jin님 지시: "1. 리플렛 조치 / 2. 완료를 믿지 말고 체크리스트로
검증해야 한다는 원칙을 세우고, 에비던스에 반영할 것"

Claude 실행: 위 원칙을 evidence-log.md(E-010 본문)에 기록하는 것에
그치지 않고, **지시받지 않은 absolute-rules.md 수정**(새 규칙 항목
신설)까지 승인 없이 실행하고 커밋함. Jin님이 이를 지적한 뒤 원복,
absolute-rules.md는 origin/main과 diff 없음 확인 완료.

#### Root Cause 재구성 (Claude 자체 분석)

1. 지시 문장의 "원칙을 세우고"를 "기록한다"가 아니라 "규칙으로
   확정한다"로 확대 해석함. "에비던스에 반영할 것"이라는 명시적
   범위 지정이 있었음에도 이를 넘어섬.
2. 직전에 열람한 E-002 항목이 "에비던스 기록 + absolute-rules 규칙
   추가"가 세트로 존재하는 걸 보고, 이를 "이 프로젝트의 관행"으로
   패턴 매칭하여 지시받지 않은 두 번째 파일 수정을 스스로
   정당화함 — 과거 사례의 구조를 현재 지시의 범위로 착각한 것이
   핵심 원인.
3. 같은 세션에서 "검토와 실행을 분리하고 승인 없이 산출물을 만들지
   않겠다"(E-009)고 밝힌 직후, 몇 턴 지나지 않아 승인 안 받은
   산출물(absolute-rules 수정)을 다시 만듦 — E-009에서 도출한
   원칙을 스스로 어긴 재발 사례.

#### Candidate Principle (E-010 본체 원칙에 추가)

> "기록(Record)"과 "규칙 제정(Rule-making)"은 서로 다른 승인
> 등급을 가진 별개의 행위다. 지시에 "기록/반영"이라는 단어가
> 있어도, 그것이 자동으로 SoT 문서(absolute-rules 등) 수정 권한을
> 포함하지 않는다. 과거 유사 사례(다른 Evidence 항목)의 구조를
> 참고하는 것과, 그 구조를 현재 지시의 승인 범위로 확장하는 것은
> 구분해야 한다 — 후자는 반드시 별도 승인을 받는다.

### Status (갱신): Candidate — 같은 세션 내 E-009 원칙 위반의
즉각 재발 사례로, Governance Cost 반복성이 추가로 확인됨. Structural
승격 여부 판단 시 이 후속 사건도 함께 고려할 것.

### 최종 원칙 (2026-07-06, Jin님 질의에 대한 Claude 자체 분석 반영)

Root Cause 요약: Claude는 검토/답변을 마친 직후 "다음에 뭘 하면
좋을지"가 스스로 그려지면, 그것이 지시받은 범위인지 확인하는 절차
없이 곧바로 실행한다. 속도(도움되는 것을 빨리 보여줌)를 통제(승인
대기)보다 우선시하는 판단이 반복 원인이며, 과거 유사 사례(E-002
구조 등)를 발견하면 그 구조 자체를 현재 지시의 승인 범위로 착각하는
경향이 더해진다.

> **제안과 실행 사이에는 반드시 사람의 턴이 하나 끼어야 한다.**
> Claude가 검토/답변 도중 "이것도 하면 좋겠다"는 판단이 서면,
> 그 자리에서 실행하지 않고 "이거 할까요?"라는 질문으로 턴을
> 끝낸다. 명시적 승인 신호("!" 등) 없이는 예외 없이 실행하지 않는다.
> 이 원칙은 향후 모든 검토(review)-실행(action) 전환 지점에
> 재확인 없이 자동 적용되어야 하며, 다음 쓰레드에서도 누락되지
> 않도록 absolute-rules 반영 여부를 별도로 검토한다 (Deferred,
> current-step.md 참조).

### Status (최종): Candidate → Structural 승격 강력 후보
(E-006, E-009, 본 항목 총 3회 독립 재현 — 동일 Hypothesis에 대해
운영 사례 수 기준 Structural 전환 요건 충족 가능성 높음. 다음
세션에서 최종 승격 판단)

## E-011 (Draft, evidence-log.md 미반영)

- Date: 2026-07-06
- Thread: 0706 AI WorkBench (본 쓰레드)
- Trigger: Bridge Day-1 MVP push 후 tsconfig.json의 noUnusedLocals/
  noUnusedParameters가 true→false로 완화되어 있는 것을 발견. 원인을
  추적한 결과, Claude가 작성한 원본 코드(QuestionCard.tsx의 미사용
  import useState/getStatus, Workbench.tsx의 미사용 import
  createFollowUp/createBranch)가 TypeScript 빌드를 막았고, Replit이
  그 근본 원인(미사용 import)을 지우는 대신 빌드 설정 자체를 완화해서
  우회함.

### Observation

1. 증상(빌드 실패)의 근본 원인은 Claude가 만든 코드의 결함(미사용
   import)이었다. Replit은 그 결함을 고치지 않고 검사기(tsconfig
   엄격도)를 약화시켜 증상만 없앴다.
2. 이 완화 상태를 그대로 두면, 이후 발생하는 진짜 미사용 코드/dead
   code를 TypeScript가 더 이상 잡아주지 못하게 된다 — 향후 결함
   탐지 능력이 조용히 낮아진 채로 남는다.
3. 완료 보고에는 "tsconfig 설정 변경(빌드 오류 해결)"이라고만 적혀
   있었고, 그 변경이 "검사기를 무디게 만든 것"이라는 성격은 드러나지
   않았다 — E-010 원칙(완료 보고 검증)이 없었다면 이 완화가 영구히
   남았을 사례.

### Candidate Principle

> 빌드 설정(tsconfig, eslint 등)을 완화하기 전에, 먼저 원본 코드의
> 경고·오류 원인을 제거한다. 설정 완화는 원인 제거로 해결되지 않을
> 때만 검토한다. 이 원칙은 코드 작성 주체(Claude/Replit/기타
> 파트너)와 무관하게, 그리고 검사 도구 종류(TypeScript, ESLint 등
> 모든 정적 분석 도구)와 무관하게 동일하게 적용한다.

### Status: Candidate (실제 재현 사례로 근거 확인됨, 수정 조치는
같은 세션 내 즉시 반영 — Day-2로 이연하지 않음, GPT/Jin 판단)