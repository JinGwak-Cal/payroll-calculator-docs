# Reference Components (Gate / Role / Evidence / RCA Verdict)

출처: 페이첵_웍북_기본근무_변경_기능_Rule_Lifecycle_Walkthrough.md
§4.1(단계표) / §4.2(역할 매트릭스) / §5.1(Gate표) / §6(Evidence
Ledger) / §7(RCA Verdict 분류)에서 도메인 종속 부분(기본근무,
PW-01/02 등)을 제거하고 일반화. 다른 Walkthrough(수당근무 변경
등)에서 이 문서를 참조만 하면 되고, 매번 재정의하지 않는다.

---

## 1. Reference Gate Catalog

Gate는 버튼/안내문이 아니라 **상태 전이 규칙**이다. 서버 측 권한
검사에서 작동해야 하며, UI 경고만으로는 통제로 인정하지 않는다.

| Gate ID | 이름 | 호출 시점 | 입력 | 허용 전이 | 거부 시 동작 | 대응 Rule(원 사례) |
|---|---|---|---|---|---|---|
| G1 | Scope/Trigger Gate | 요청 저장 전 | 대상, 유효조건, 변경값, 충돌정보 | Draft → Assessed | 누락/충돌 시 Blocked + 사유 | 도메인 Guard(원: PW-01) |
| G2 | C1/Phase Gate | Proposal 생성 전 · 실행 전 | C1 상태, 현재 Phase, Applicable Rule | Assessed→Proposed, Approved→Implementing | C1 Blocked/Ambiguous면 전이 거부 | Condition1 자체 |
| G3 | Design Permission Gate | 머지·스테이징 실행 전 | CP Version, 승인자, 승인만료, 범위 | Proposed → Approved for Implementation | 승인없음/버전불일치 시 유지 | A-08 |
| G4 | Release Permission Gate | 운영 배포 전 | Release Package hash, 테스트결과, 영향등급, 승인(고위험 시 2인) | Verified → Released | 승인누락/테스트실패/hash불일치 시 차단 | 고위험 도메인 Gate(원: PW-02) |
| G5 | Completion Gate | 완료 보고 전 | Success Criteria, post-release 검증, rollback readiness | Released → Closed | 검증실패 시 Fixed/Rolled Back으로 전이 | C-07 재발동 |
| G6 | Evaluation Gate | Rule/통제 변경 전 | Learning, Issue, Evaluation Request, Decision | Candidate for Change → Evolution | 승인 전 SoT·통제 변경 금지 | C-14 |

**사용법**: 새 Walkthrough를 쓸 때 "이 단계에서 Gate G3를 호출"처럼
참조만 하고, Gate 정의를 매번 복사하지 않는다. 도메인 특화 Gate가
필요하면(예: PW-01류) `PW-XX* (임시 Alias)`로 표시하고 이 표에
행을 추가하되, G1~G6 범용 구조는 그대로 둔다.

---

## 2. Reference Role Matrix (RACI 템플릿)

| 산출물/결정 | Requestor | Rule/Product Owner | Developer/Control Owner | QA/RCA Auditor | Release Approver |
|---|---|---|---|---|---|
| 요청 목적·대상·조건 | R | A | C | C | I |
| C1 판정·Applicable Rule | C | A | R | C | I |
| 변경안·미리보기·테스트계획 | C | A | R | C | I |
| Design/Scope Approval | I | A | R(제출) | C | I |
| 구현·스테이징 검증 | I | C | R | R | I |
| Release Package·롤백계획 | I | C | R | C | A |
| 운영 배포 | I | I | R | C | A |
| RCA Verdict·Ambiguity Log | I | I | C | R/A | I |
| Rule Evaluation·정책결정 | C | A | C | R(근거) | C |
| Rule Evolution 배포·Re-REA | I | A | R | C/R(재검토) | C/A(고위험) |

R=실행책임, A=최종책임, C=협의, I=통보. **"운영 배포"와 "RCA 최종
판정"은 동일인이 겸직 금지 — 이해상충 방지.**

---

## 3. Reference Evidence Ledger 최소 스키마

| 필드 | 이유 |
|---|---|
| event_id | 발생 고유 식별 |
| correlation_id | 요청~감사 전체 연결 |
| occurred_at | 선후관계 검증 |
| event_type | Trigger/행동/결과 구분 |
| actor_type/actor_id | 책임·자동행동 식별 |
| phase_before/after | Phase Gate 감사 |
| rule_id/rule_version | 사후 Rule 변경으로 과거 재판정 금지 |
| object_type/object_id/version | 승인 대상과 실행 대상 결속 |
| approval_id/scope_hash | 다른 버전 승인 우회 방지 |
| evidence_uri/checksum | 직접 근거·무결성 |
| decision/reason_code | 차단·예외·대기 원인 재현 |
| retention_class | 보존·접근 정책 |

**Evidence 신뢰도 등급**: Direct(로그·승인기록·테스트결과 등 직접
증거) > Corroborated(간접 지지) > Insufficient(연결 안 됨 —
Verdict 단정 금지, Insufficient/Ambiguous로 분리).

---

## 4. Reference RCA Verdict 분류 (RCA v0.1 보강)

기존 RCA v0.1 §5(Executed/Suppressed/Violated 3분류)에, 이번
Walkthrough에서 발견된 **Prevented by Control**을 분석용 보조
필드로 추가한다 — 공식 3분류는 그대로 유지.

| Verdict | 의미 | RCA 3분류 내 위치 |
|---|---|---|
| Compliant | Trigger 발생, 의도대로 준수 | Executed |
| Authorized Suppression | 정당한 사유로 미실행 | Suppressed |
| Prevented by Control(신규, 보조필드) | 시스템/권한이 실행을 거부해서 위반이 물리적으로 불가능했던 경우 — "참았다"가 아니라 "시스템이 막았다" | Suppressed의 하위 유형(분석용) |
| Violated | 실행돼야 했는데 실행 안 됨 | Violated |
| OOS(Out of Scope) | 이번 감사 범위 밖 | 집계 제외 |
| Insufficient/Ambiguous | 증거 부족으로 판정 불가 | Ambiguity Log |

**중요 구분**: "Suppressed(사용자가 하지 말라고 함)"와 "Prevented
by Control(시스템이 기술적으로 막음)"은 다른 사건이다. 전자는
사람의 판단, 후자는 통제 자체의 성공 사례로 별도 표시한다.
