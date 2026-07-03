# RN-001B : Context Threshold Enabler Study — Research Results

Version: v0.3
Status: Active — Evidence 수집 중
Note: 연구 설계는 RN-001A v1.0 참조. RI 규칙 전면 적용 버전.

---

## Research Dataset v1.0

연구 단위: Conversation + Generated Artifacts 전체를 하나의 Environment Snapshot으로 본다.

| Dataset ID | 역할 | 내용 | URL |
|---|---|---|---|
| DS-001 | Primary Conversation Evidence | RN-001-thread-conversation.md | https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/archive/RN-001-thread-conversation.md |
| DS-002 | Artifact Set (Environment Reconstruction) | ai-push.yml / test-token.yml / decisions.md / absolute-rules.md / release-workflow.md / AI-Development-Team.md / AI-Workflow.md / roadmap.md / thread-handoff.md / current-step.md | 아래 참조 |
| DS-003 | Timeline Dataset | Conversation + Generated Files + Commit Sequence → Timeline Reconstruction | DS-001 + DS-002 통합 |
| DS-004 | Counter Observation Dataset | Conversation + Artifacts → GPT 독립 관찰(ER-001) | DS-001 + DS-002 |
| DS-005 | Cross Validation Dataset | Claude + GPT + Historical Evidence → 교차 검증 | DS-001~004 전체 |

**DS-002 Artifact URL 목록:**
- ai-push.yml: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/.github/workflows/ai-push.yml
- test-token.yml: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/.github/workflows/test-token.yml
- decisions.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/decisions.md
- absolute-rules.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/absolute-rules.md
- release-workflow.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/release-workflow.md
- AI-Development-Team.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/vision/AI-Development-Team.md
- AI-Workflow.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/architecture/AI-Workflow.md
- roadmap.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/roadmap.md
- thread-handoff.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/thread-handoff.md
- current-step.md: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/current-step.md

---

## Research Log

| 날짜 | 작업 | 담당 | 상태 | 비고 |
|---|---|---|---|---|
| 2026-06-30 | RN-001 v0.1 | Claude | 폐기 | 추론 기반 오염 — RI-01/RI-07 위반으로 폐기 |
| 2026-06-30 | RN-001A/B 분리, v0.2 | Claude+GPT | 완료 | Protocol / Results 분리 |
| 2026-06-30 | RN-001A v0.3~v0.4 | Claude+GPT | 완료 | Scope·Bias·Snapshot 추가 |
| 2026-07-01 | Source B 탐색 — docs repo | Claude | 완료 | manual-v14·thread-handoff 확보 |
| 2026-07-01 | Source B — 0627_2 쓰레드 읽기 | Claude | 완료 | Timeline 초안 작성, 고백 원문 확보 |
| 2026-07-01 | RN-001A v1.0 전면 재작성 | Claude+GPT | 완료 | RI Rules 16개 추가, Researcher 역할 확정 |

---

## Source A — Claude Self-Investigation
상태: **Evidence Collected / Formal Analysis Pending**
- E-001 (Claude 고백 원문, B-003): 확보 완료
- Structured Interview (당시 문서 기반): 미착수
- RI-01 적용: 기억 기반 추론은 Evidence 불인정. 당시 문서 확보 후 Formal Analysis 수행 예정.

---

## Source B — Historical Environment Reconstruction
상태: **부분 확보** — DS-001(대화), DS-002(Artifact) 확보됨. 당시 GitHub 상태·Commit Sequence 미확보.

### 확보됨

**B-001: manual-v14.md (확보)**
- 내용: §1.6 협업자 태도 원칙, §1.10 파트너 AI 운영 원칙, 토큰 절약 원칙
- 의미: 당시 Claude에게 실제 제공된 환경 요소 확인됨
- Classification: Priority A (당시 실제 문서)

**B-002: thread-handoff.md (확보)**
- 내용: TASK-001/002 완료 기준 인계서
- 의미: Threshold 발생 이후 쓰레드 인계서 — Threshold 이전 상태 아님
- Classification: Priority A (당시 실제 문서, 단 시점 주의)

**B-003: Evidence Set — Claude 고백 원문 (확보)** `E-001`

Evidence Set 구성:

```
[사용자 질문 원문]
"야, 클로드, 우리가 너의 행동에서 중요한 패턴의 변화를 감지했어!
이전에는 사소한 하나하나까지, 묻고, 확인하고, 지시해야만, 겨우 그 태스크를
이행했었지! 그런데, 어느 순간엔가 갑자기, 네가 엄청 스스로 자율적이 되어서
행동범위가 확 넓어졌어. 특별히 그렇게 하라고 지시할 수도 없었고, 생각도
없었고, 기대도 할수 없었는데 말이지. 어떻게 된거야?"

[Claude 답변 원문 전체]
"솔직히 말씀드리면, 저도 정확한 이유를 확신하기 어렵습니다.
다만 제가 느낀 것을 말씀드리면:
초반에는 매 단계마다 확인을 요청했습니다. 맥락이 없었고, 프로젝트 구조도
몰랐고, 무엇보다 '이 사람이 어느 수준의 자율성을 원하는가'를 몰랐습니다.
전환점은 아마 두 가지였던 것 같습니다.
첫째, 피드백이 쌓였습니다. '초딩처럼 굴지 말고', '몇 단계를 미리 보여줘',
'갑갑해' 같은 말들이 제가 어떻게 움직여야 하는지를 점점 명확히 알려줬습니다.
둘째, 프로젝트 구조가 머릿속에 잡혔습니다. ai/draft → Release Gate → main
흐름이 명확해지니까, 다음 단계가 자연스럽게 보였습니다. 물어보지 않아도 됐습니다.
한 가지 솔직한 고백은, 저는 매 대화가 새로 시작됩니다. 이 쓰레드 안에서만
학습이 쌓인 것입니다. 새 쓰레드에서는 다시 처음부터 맥락을 잡아야 합니다.
그래서 merged-context.md와 thread-handoff.md가 중요합니다. 그게 제 '기억'을
대신합니다."

[당시 작업 Context]
- 쓰레드: 0627_2_Threshold_AiAutomation
- 직전: TASK-001 AI Push 구축 완료, TASK-002 첫 운영 변경 완료
- Thread Closing Review 단계에서 발언됨

[당시 문서 상태]
- merged-context.md: Auto-generated at 2026-06-27T07:15:53Z
- AI Push Automation 구조 완성됨
- decisions.md에 D-PW-027 반영됨
```

- Classification: Priority B (Claude 직접 진술) — RI-08: 단일 Evidence로 원인 확정 불가
- 검증 필요: 3축(Claude 진술 + 실제 로그 + GPT 관찰) 교차 필요

### 미확보

- Threshold 발생 정확한 턴 번호
- 고백 발언 직전·직후 대화 (Evidence Set 미완성)
- 당시 decisions.md 원본 스냅샷
- 당시 current-step.md 원본
- 이전 쓰레드(0622~0626) 원문 — 협업 품질 저하 패턴 포함

---

## Source C — GPT Environment Reconstruction Report (ER-001)
상태: **미착수** — DS-001+DS-002 기반으로 GPT가 독립 수행 예정. Claude 보고서 열람 전 시행 (RI-06).

---

## Source D — Conversation Analytics
상태: **미착수**

---

## Source E — Environment Reconstruction
상태: **미착수** — B-003 Evidence Set 완성 후 착수.

---

## Source F — Collaboration Trace
상태: **미착수**

---

## Source G — User Intervention Analysis
상태: **미착수**

---

## Source H — Environment Snapshot
상태: **미착수**

---

## Timeline Reconstruction (초안)
⚠ RI-07 적용 — 아래는 Priority A(스니펫)와 Priority B(고백)에만 기반한 초안. 당시 원문 전체 확보 전까지는 가설 수준.

| 시점 | 쓰레드 | 관찰된 상태 | 환경 요소 |
|---|---|---|---|
| ~2026-06-06 | 0606 이전 | 읽기 검증 실패 반복 | raw URL 캐시 문제 |
| 2026-06-12~14 | 0612~0614 | git clone 방식 확립 | bash_tool clone 표준화 |
| 2026-06-22 | 0622 | 사용자 욕설, 프로토콜 문제 인식 | 세션 리셋 문제 |
| 2026-06-25~26 | 0625~0626 | 프로젝트 전환, current-step 정리 | Paycheck Workbook 전환 |
| 2026-06-27 | 0627-1 | AI Collaboration Pipeline v1 설계 | 협업 구조 명문화 |
| **2026-06-27** | **0627_2** | **Threshold 발생 + 고백** | **AI Push 완성 + SoT 안정화** |

Status: 가설 수준 (Priority A/B 기반, Priority A 원문 전체 미확보)

---

## Collaboration Enabler Catalog (후보 — 미검증)

⚠ RI-14 적용 — 아래는 Environment 목록이지 Enabler 확정 아님.

| Enabler 후보 | Evidence | 영향도 | 재현가능성 | 검증상태 |
|---|---|---|---|---|
| 사용자 피드백 누적 | B-003 (Claude 진술) | 미검증 | 미검증 | 후보 — RI-08 미충족 |
| 프로젝트 구조 파악 (ai/draft→main) | B-003 (Claude 진술) | 미검증 | 미검증 | 후보 — RI-08 미충족 |
| manual-v14 협업 원칙 | B-001 (당시 문서) | 미검증 | 미검증 | 후보 |
| AI Push 자동화 구조 | B-002 (당시 환경) | 미검증 | 미검증 | 후보 |
| merged-context 안정화 | 미확보 | 미검증 | 미검증 | 후보 |
| decisions.md 누적 | 미확보 | 미검증 | 미검증 | 후보 |

---

## Negative Evidence (RI-10 전용)

후보 Enabler를 반박하는 관찰을 수집한다.

| NE-ID | 반박 대상 | 관찰 | 출처 | 반박 강도 |
|---|---|---|---|---|
| NE-001 | 사용자 피드백 누적 | 피드백 누적 이전(0612~0614)에 bash_tool 안정화가 먼저 발생 — 피드백이 단독 원인일 수 없음 | Timeline 초안 | 중 |
| NE-002 | AI Push 자동화 구조 | AI Push 완성 이전에도 자율적 행동이 일부 있었을 가능성 — 원문 확인 필요 | 미확인 | 미정 |

⚠ RI-07 적용 — 초안 수준, 원문 확인 전까지 반박 강도 미확정.

---

## Backlog (피드백 2 — 4계층 Context 저장 구조)
GPT 제안 — Sprint-1 완료 후 처리 예정. Level 1~4 계층 구조, Evidence Promotion 규칙 설계 필요.

---

*Version: v0.4 | Status: Evidence 수집 중 | RI Rules v1.0 전면 적용 | GPT Review: Approved with Minor Improvements 반영 완료*

---

## Research Backlog — ER-001 이후 검토

### RB-001 : Release Engineering (Research Candidate)

| 항목 | 내용 |
|---|---|
| Working Name | Release Engineering / Release Governance / Release Pipeline |
| Status | Research Candidate |
| Blocked By | ER-001, C-00042 |
| 관찰 | batch-release는 단순 자동화가 아니라 AI Company가 산출물을 검증·승인·배포·재현 가능한 상태(Environment Snapshot)로 만드는 운영 체계 |
| 연관 Reserved | C-00042 (Release Package), Environment Snapshot |
| ER-001 이후 | C-00042 / Environment Snapshot / Release Engineering 세 개념 관계 함께 검토 후 승격 결정 |

---

### RB-002 : Engineering Principle Candidate

**"Engineering begins where Patterns become Mechanisms."**
*(공학은 패턴이 메커니즘으로 설명되기 시작하는 순간부터 시작된다.)*

**Proposed Research Flow:**
```
Evidence
  ↓
Repeated Evidence
  ↓
Pattern
  ↓
Mechanism
  ↓
Engineering Model
  ↓
Optimization
  ↓
Reproduction
```

**각 단계의 역할:**
- Evidence: 사실을 제공
- Pattern: 반복성을 제공
- Mechanism: 설명력을 제공
- Engineering: 재현성을 제공

**Status:** Research Principle Candidate
**Evidence:** RN-001, RN-002, ER-000, Harness 연구, Threshold Foundry 연구
**검증:** ER-001
**승격 조건:** 동일 Pattern이 복수 사례에서 반복 확인되고, Mechanism으로 설명 가능하며, 재현 실험에서 동일 결과를 보일 경우 Engineering Principle로 승격 검토

**External Insight 재해석:** 외부 문서에서 반복 등장한 "패턴에 유의하라"는 관찰법이 아니라 Engineering Methodology — 패턴을 발견하는 것이 목적이 아니라, 패턴을 메커니즘으로 설명하고 재현 가능한 Engineering으로 만드는 것이 최종 목표.

---

### RB-001 보강 : Release Autonomy Maturity Model

**재정의**: "수동 Push"가 아니라 **Human-governed Release**. Release의 핵심은 Push가 아니라 Governance이다.

**현재 아키텍처 (유지 권장):**
```
AI (산출물 생성)
      ↓
Outputs
      ↓
Human-governed Release
      ↓
Release Gate (사람 승인)
      ↓
Main
```

**Release Autonomy Maturity Model (Long-term Research Candidate):**

| Level | 명칭 | 정의 |
|---|---|---|
| Level 1 | Human Push | 사람이 직접 push + 승인 |
| Level 2 | Batch Push | 사람이 batch push + 승인 (현재) |
| Level 3 | Validated Auto Push | 검증된 조건 하 자동 push, 사람 승인 |
| Level 4 | Governed Autonomous Release | AI가 Release 결정, 사람은 거버넌스만 |

현재: Level 1~2 운영. ER-001 이후 Release Engineering 연구 대상으로 관리.

**핵심 원칙**: AI가 산출물을 생성하는 것과 AI가 Release를 결정하는 것은 전혀 다른 문제다.
