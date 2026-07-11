# Thread Closing Review (통합 클로징 리뷰) v1.0

> 목적: 이번 쓰레드에서 생성된 모든 지식이 유실 없이 적절한 귀속점을
> 갖고, 종료된 판단과 보류된 판단이 명확히 구분된 상태로 다음
> 쓰레드에 전달되도록 한다.

---

## STEP 0. 원문 확보 (Source of Truth)
□ Claude 원문을 로컬 PC에 저장했다.
□ 이번 작업과 관련된 GPT 원문이 존재하는지 확인했다.
□ 존재하면 Claude 원문과 동일한 Source of Truth로 확보하여 로컬 PC에
  저장했다.
□ 존재하지 않으면 "GPT 원문 없음"을 명시적으로 확인했다.
□ Claude 원문과 GPT 원문을 동일한 Source of Truth로 취급한다.
□ 이번 리뷰는 반드시 원문을 기준으로 수행한다 (완독이 아니라, 각
  Event가 인용하는 구간을 실제로 열어 확인 — 0711 GPT 원문 줄번호
  오인용 사례 참고. 기억이나 요약이 아니라 원문 Evidence를 기준으로
  한다)

---

## STEP 1. 원문 검토 (Evidence Review)
원문을 근거로 다음 사항을 추출한다.
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

---

## STEP 2. 귀속 (Disposition)
**귀속이 필요한 모든 결과가 빠짐없이 귀속되었는가? (귀속 누락 없음)**
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

## STEP 5. Deferred 확정
보류 항목마다 반드시 아래 항목을 함께 기록한다.
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

---

## 특수 종료

TCA(6-Domain Audit)는 일반 Thread Closing Review 대상이 아니다.
Release, Sprint 종료, 대규모 구조 변경 등 특별한 종료 시점에만
별도로 수행한다.

---

## 변경 이력
- v1.0 (2026-07-11): 최초 확정. GPT/Claude 원문 동일 SoT, 귀속
  (Disposition) 개념 도입, Deferred 4필드 확정.
