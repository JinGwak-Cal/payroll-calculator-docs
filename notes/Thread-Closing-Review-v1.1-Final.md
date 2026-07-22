# Thread Closing Review (통합 클로징 리뷰) v1.1 Final

> Status: STANDARD / Maturity: Verified / Change Policy: Frozen
> (실제 검증된 개선이 발생했을 때만 개정 — v1.2 임의생성 금지)
> Origin: v1.0 + Operational Review Pilot(OR-0000/0001) + Search
> Contract(GPT 제안)

> 목적: 이번 쓰레드에서 생성된 모든 지식이 유실 없이 적절한 귀속점을
> 갖고, 종료된 판단과 보류된 판단이 명확히 구분된 상태로 다음
> 쓰레드에 전달되도록 한다.

---

## STEP 0-A. Search Contract (검색 계약, 2026-07-22 개정)

Closing Review에서 사용할 Evidence의 확보 계약을 원문 확보 및
검증 수행 **전에** 먼저 선언한다. 추정을 방지하고 정확한
실측(Evidence Verification)을 수행하기 위함이다.

각 검색 목적마다 아래 5요소를 선언한다:

1. **Question** — 이번 Closing에서 확인하려는 질문
2. **Primary Source** — 판단의 주 근거가 되는 Source
3. **Secondary Source (Optional)** — Primary Source에 없는 범위만
   보완, Primary Source를 대체하지 않는다
4. **Tool** — grep / find / view·cat / git / 기타
5. **Expected Artifact** — 확보해야 하는 결과물(원문/파일/Git
   상태/로그/Evidence 등)
6. **Expected Evidence (2026-07-22 추가)** — Artifact 안에서
   구체적으로 무엇이 확인되어야 판단 근거로 인정하는지(예:
   Artifact="git diff", Evidence="ID 14개 모두 존재"). Artifact
   확보와 Evidence 판정을 분리한다

검색 목적별 기본 매핑(참조용):

| 목적 | 질문 예시 | Primary Source | Tool |
|---|---|---|---|
| 대화에서 언제 논의됐는가 | 누가 무슨 말을 했는가? | 대화 원문(Conversation) | `grep` |
| 실제 파일이 존재하는가 | 산출물이 생성되었는가? | 저장소(Repository) | `find`, `ls` |
| 파일 내용이 무엇인가 | 내용이 정확히 반영되었는가? | 파일 자체 | `cat`, `view` |
| 최신 상태인가 | 어느 것이 기준(SoT)인가? | Git / Metadata | `git log`, `git status`, `stat` |

**실행 규칙**: 작업을 시작하기 전, 위 5요소에 따라 검색 대상을
명확히 정의하고 도구를 선택해야 한다. "grep으로는 못 찾았지만
find에서는 찾을 수 있는" 상황을 방지하기 위함이다.

> **Gate(2026-07-22 추가)**: STEP0-A/0-B(Search Contract·원문
> 확보·읽기검증)가 완료되기 전에는 STEP1 이하를 시작하지 않는다.
> (하단 "실행 전제조건" 절의 What/How/Interpretation Evidence/
> 성공검증기준/Source Coverage와 동일 원칙 — 여기서는 STEP0
> 경계에 다시 한번 명시)

---

## STEP 0-B. 원문 확보 및 실측 (Source of Truth & Evidence Verification)
□ Claude 원문을 로컬 PC에 저장했다.
□ 이번 작업과 관련된 GPT 원문이 존재하는지 확인했다.
□ 존재하면 Claude 원문과 동일한 Source of Truth로 확보하여 로컬 PC에
  저장했다.
□ 존재하지 않으면 "GPT 원문 없음"을 명시적으로 확인했다.
□ Claude 원문과 GPT 원문을 동일한 Source of Truth로 취급한다.
□ **이번 리뷰는 반드시 원문을 기준으로 수행한다** (완독이 아니라, 각
  Event가 인용하는 구간을 실제로 열어 확인 — 0711 GPT 원문 줄번호
  오인용 사례 참고. 기억이나 요약이 아니라 원문 Evidence를 기준으로
  한다)
□ **STEP 0-A에서 정의한 매핑에 따라 실측(grep, find, git status 등)을 완료했다.**

**읽기 검증 프로토콜(2026-07-22 추가, 확보≠읽음 구분)**
□ 원문의 Auto Timestamp/생성시각을 확인했다
□ Source 라인(어느 파일들의 합본인지)을 확인했다
□ 최근 Decision 1건 이상을 원문에서 실제로 인용했다
□ Current Step 최신 항목을 원문에서 실제로 인용했다
□ "파일이 있다"가 아니라 "실제로 열어서 내용을 확인했다"임을
  구분한다(예: JSON/PNG/ZIP이 첨부목록에 있어도 실제 열어보지
  않았다면 "확보"이지 "읽음"이 아니다)

---

## STEP 1. 원문 검토 (Evidence Review)

**Source Capability Mapping (2026-07-22 추가)**
원문 검토 전, 각 정보 유형이 어느 Source에서 판단 가능한지 선언한다.
| 정보 유형 | 판단 가능 Source |
|---|---|
| Discussion / 의도 | 대화 원문 |
| 파일 존재 여부 | Repository |
| 최신본 여부 | Git |
| 구현 완료 여부 | Repository (코드) |

원문과 실측된 Evidence를 근거로 다음 사항을 추출한다.
□ Event
□ Discussion (중요 논의 — 결론이 나오기까지의 과정, "왜 그런
  결론이 나왔는가"를 보존. 예: Public/Private 논의, Corpus 생성
  여부 논의 등이 Discussion → Decision → Event로 이어짐)
□ Decision
□ Rule
□ Current Step 변경사항
□ Default Correction 후보
□ Handbook 반영사항
□ Review
□ 구현 Task
□ Deferred 후보
□ 장기 보존 가치가 있는 내용
□ Claude 원문과 GPT 원문 내용이 서로 다르면, 어느 한쪽만으로 결론
  내리지 않고 통합 후 판단한다.

**Cross Validation Gate (2026-07-22 추가)**: 양 원문이 충돌하면
아래 순서로 대조하고, 대조 근거를 기록한다.
1. Discussion(논의 과정) 대조
2. Decision(결론) 대조
3. Event(실행 결과) 대조
이 순서로 판단 근거를 남겨 "통합"이 검토자마다 달라지지 않게 한다.

---

## STEP 2. 귀속 (Disposition)
**귀속이 필요한 모든 결과가 빠짐없이 귀속되었는가? (귀속 누락 없음)**

**Disposition 유형 (2026-07-22 추가, Reconciliation 용이성 위해)**
각 귀속 항목마다 아래 중 하나로 표시한다.
□ 신규 생성 □ 기존 수정 □ 귀속 안 함(사유 기록)

□ Event History
□ decisions.md
□ current-step.md
□ absolute-rules.md
□ Handbook
□ Default Correction Table
□ Review
□ 구현 Task
□ Deferred
□ 귀속하지 않기로 결정한 사항도 이유를 기록했다.
※ 어느 곳에도 귀속되지 않은 결과가 남아 있으면 안 된다.

---

## STEP 3. 문서 반영 (Integration)
□ Event History 반영
□ decisions.md 반영
□ current-step.md 반영
□ absolute-rules.md 반영
□ Handbook 반영
□ Default Correction Table 반영
□ Review 반영
□ 기타 필요 문서 반영

---

## STEP 4. 판단 종료 확인 (Decision Closure)
□ 이번 쓰레드에서 결정된 사항이 명확하다.
□ 보류된 사항이 명확하다.
□ 귀속되지 않은 판단이 없다.
□ 같은 논의를 다음 쓰레드에서 반복하지 않아도 된다.
□ 판단 종료 근거(Evidence)를 확인할 수 있다.

---

## STEP 5. Deferred 및 Not Assessable 확정 (2026-07-22 개정)
판단이 보류되거나 검증 불가능한 항목은 명확히 구분하여 기록한다.

**판단 상태 구분**
□ Deferred (조건부 보류: 나중에 다시 판단함)
□ Not Assessable (검증 불가: 현재 Evidence로는 판단 자체가 불가능함)

**Deferred (보류) 항목 기록 필수 사항**
□ Decision (이번에 무엇을 결정했는가)
□ Reason (왜 지금 하지 않는가)
□ Evidence Trigger (어떤 Evidence가 생기면 재검토하는가)
□ Next Review (언제 다시 판단하는가)

Deferred는 단순한 보류가 아니라, **판단을 종료한 상태**이다.
재검토 조건(Evidence Trigger)이 발생하기 전까지 동일한 논의를
반복하지 않는다.

(예시: D-TF-002 Corpus 보류 — "쓰레드 수백 개 누적, AI분석 병목
시점"이라는 구체적 재검토 조건까지 기록된 사례)

---

## STEP 6. 최종 검증 (Final Verification)
□ Claude 원문 로컬 저장 완료
□ GPT 원문 로컬 저장 완료 (존재하는 경우)
□ Event History 반영 완료
□ Decision 반영 완료
□ Current Step 반영 완료
□ Rule 반영 완료
□ 귀속 누락 없음
□ Deferred에 Evidence Trigger 기록 완료
□ 다음 쓰레드가 이번 쓰레드를 다시 열지 않고도 작업을 시작할 수
  있다. (작업 관점 — 개발을 이어갈 수 있는가)
□ 이번 쓰레드를 다시 열어야 하는 미해결 판단이 남아있지 않다.
  (판단 관점 — 결정이 끝났는가. 개발 재개 가능 여부와는 별개로,
  판단 자체가 끝났는지 독립적으로 확인)
□ **Decision Rationale (2026-07-22 추가, 2026-07-22 개정으로 세분화)**:
  - **Evidence**: 이번 판단의 핵심 근거
  - **Reason**: 위 Evidence를 근거로 이러한 Closing 결론에 도달한 이유
  - **Alternative (선택, 2026-07-22 추가)**: 왜 다른 판단을 하지
    않았는가 — 필수 아님, 재현성이 특히 중요한 판단에서만 기록
  (예: "Evidence — 모든 산출물이 Repository에 push되었으며 커밋
  SHA로 확인됨. Reason — Deferred 항목은 Evidence Trigger가
  명확히 기록되어 재논의 없이 다음 쓰레드로 이월 가능하기 때문.")

### 3단 파이프라인 Trigger (2026-07-13 추가)

STEP3(문서 반영)에서 "반영 완료"를 선언하기 **직전**, 아래를 순서대로
실행한다. 하나라도 통과 못 하면 STEP6 "완료" 선언을 하지 않는다.

1. **Local Preflight** — 이 시점에 즉시 실행. `preflight_validator.py`
   (repo notes/tools/ 또는 매 쓰레드 재생성)를 반영 대상 zip에 대해
   실행 → Package/Exclusion/Destination-A/B/Content/Diff 검사
2. **PR Gate** — PR 생성 시 자동 실행 (`.github/workflows/`). Actual
   PR Changed Path Set == Expected Path Set
3. **Post-Merge Gate** — merge 완료 시 자동 실행. origin/main에서
   Sentinel·경로 재확인

Diff 검사에서 REVIEW_REQUIRED/FAIL이 나오면, 자동판정으로 끝내지
않고 수동 의미검토(재배치인지 실손실인지) 후 Evidence를 남긴다.

---

## 실행 전제조건 (Execution Precondition, 2026-07-13 추가 —
Gate가 실행을 막지 못하고 사후 해명 양식이 된 실패 사례 보완)

**발견된 문제**: Gate(What/How/Interpretation Evidence/성공검증
기준)를 제시하는 규칙이 있었음에도, 실행 후에야 뒤늦게 제시하는
사례가 발생함(2026-07-13, PART D 실행 후 Gate 사후 작성).

**규칙**: 아래 4개가 실제로 제시·확인되기 전에는 추출·분류·문서
수정·완료선언을 시작하지 않는다.
1. What (무엇을 할 것인가)
2. How (어떻게 할 것인가)
3. Interpretation Evidence (왜 이렇게 해석했는가, Mapping 포함)
4. 성공검증 기준 (무엇이 확인되어야 완료인가)

원문 기반 작업이면 추가로 확인한다.
5. Source Coverage — 대상 구간의 시작점·끝점이 확보 원문에
   존재하는가, 필요한 병행 원문(GPT/Claude 등)이 확보되었는가

하나라도 미충족이면 `BLOCKED` 또는 `SOURCE INCOMPLETE`로 표시하고
작업을 실행하지 않는다.

## 종료 게이트 (Completion Gate, 2026-07-13 추가)

**발견된 문제**: 사용자의 "이 정도로 진행하라"는 실행 허용을,
애초에 정한 성공검증 기준이 충족된 것으로 확대 해석하여 "전체
완료"를 선언한 사례 발생(2026-07-13, PART D).

**규칙**: 실행 승인 ≠ 성공검증 통과. 사용자가 불완전한 Evidence
상태에서 진행을 허용해도, 미충족 성공검증 기준을 임의로 PASS로
바꾸지 않는다.

사용 가능한 종료 상태:
- VERIFIED / CLOSED — 성공검증 기준이 실제 Evidence로 전건 충족
- **PARTIAL VERIFIED (2026-07-22 추가)** — 일부 항목(예: Decision/
  Rule)은 완료됐으나 다른 항목(예: Event History)은 미완료인 경우.
  EXECUTED와 구분 — 부분적으로는 실제 검증까지 끝났다는 뜻
- EXECUTED / VERIFICATION INCOMPLETE — 실행은 됐으나 검증 미완료
- BLOCKED — Source Coverage 등 전제조건 미충족으로 착수 자체 불가
- ABORTED — 중단

"완료"·"닫음"이라는 표현은 VERIFIED/CLOSED 상태에서만 사용한다.

## 검증 보고 형식 (2026-07-13 확정 — 실행 실패로 발견된 구조적 결함 보완)

**발견된 문제**: STEP6에서 "[x] 반영 완료", "[x] 귀속 누락 없음"
같은 체크박스만으로 완료를 선언하면, 그 판정이 무엇으로 증명됐는지
추적되지 않아 실제 내용 유실을 놓치는 사례가 발생함(2026-07-13,
`git status`만으로 반영 완료를 선언했다가 `git diff`에서 실제
내용 유실 발견). 검사 항목만 늘리는 것으로는 부족하며, 모든 검증
주장에 직접 실측 근거를 강제해야 함.

**제안 규칙**: 이 절차의 모든 완료·통과·반영 주장은 아래 6단
형식으로 제시한다. 직접 Evidence가 없으면 통과·완료로 판정하지
않고 "미검증" 또는 "미측정"으로 남긴다.

```
[검증 주장]  무엇이 완료/통과했다고 주장하는가 (Claim)
[검증 대상]  실제로 무엇을 검사했는가 (Target)
[측정 방법]  어떤 방법·명령·대조표로 검사했는가 (Method)
[실측 근거]  실제 diff, ID 검색 결과, 인용 구간, 개수 대조 등 (Evidence)
[판정]      통과 / 실패 / 부분통과 / 미검증 / 미측정 (Verdict)
[한계]      이 근거로 무엇까지 증명되고 무엇은 증명 안 되는가 (Scope/Limit)
```

Evidence가 증명하는 범위를 넘어서는 판정을 금지한다:
- `git status` → "파일이 변경됨"까지만 증명
- `git diff` → "무엇이 변경됐는지"까지만 증명
- ID 검색 → "ID가 존재하는지"까지만 증명
- Reconciliation → "추출 항목이 빠짐없이 귀속·반영됐는지"까지만 증명
- 원문 대조 → "반영 내용이 원문에 충실한지"까지만 증명
- 이들은 서로 대체할 수 없다

**"확인했다"는 서술만으로 끝내지 않는다** — 예: "current-step.md에
특정 문구가 없다"를 확인했다면, 검색어·검색 결과·비교 대상(로컬/
origin)까지 명시하고, "다른 브랜치·과거 커밋에도 없다"까지는
확대하지 않는다(그 부분은 이 검증의 한계로 명시).

## 특수 종료

TCA(6-Domain Audit)는 일반 Thread Closing Review 대상이 아니다.
Release, Sprint 종료, 대규모 구조 변경 등 특별한 종료 시점에만
별도로 수행한다.

---

## 변경 이력
- **v1.1 Final (2026-07-22, 2차 보완)**: 파트너(doc52) 피드백
  7건 반영 — ①STEP0-B 읽기검증 프로토콜(확보≠읽음 구분) ②STEP0
  경계 Gate 명문화(조건1 완료 전 STEP1+ 시작 금지) ③STEP1 Cross
  Validation Gate(Discussion→Decision→Event 순 대조) ④STEP2
  Disposition 유형(신규/수정/귀속안함) ⑤STEP6 Alternative(선택
  필드) ⑥Completion Gate에 PARTIAL VERIFIED 추가 ⑦Search
  Contract에 Expected Evidence 필드(Artifact와 Evidence 판정
  분리). 최소증분 원칙 유지 — 기존 조항 삭제 없음
- **v1.1 Final (2026-07-22, 1차)**: 최소증분 병합 확정. 기준=완전판
  v1.1(모든 기존 조항 100% 보존: STEP1 11개 추출항목/3단 Pipeline
  Trigger/실행전제조건/종료Gate/6단 검증보고/TCA조항). 그 위에
  GPT 제안 2건만 반영 — ① STEP0-A를 Search Contract 5요소
  (Question/Primary Source/Secondary Source/Tool/Expected
  Artifact)로 구조화 ② STEP6 Decision Rationale를 Evidence/Reason
  으로 분리. Status=STANDARD, Frozen(실증된 실패 재발 시에만 개정)
- v1.1 draft (2026-07-22): OR 파일럿 검증 요소 증분 반영. STEP 0-A(Search Target Classification) 신설, STEP 1에 Source Capability Mapping 추가, STEP 5에 Not Assessable 상태 구분 추가, STEP 6에 Decision Rationale 기록 요건 추가.
- v1.0 (2026-07-11): 최초 확정. GPT/Claude 원문 동일 SoT, 귀속
  (Disposition) 개념 도입, Deferred 4필드 확정.
