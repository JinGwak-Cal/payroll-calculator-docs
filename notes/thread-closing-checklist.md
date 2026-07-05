# Thread Closing Review Checklist

매 쓰레드 종료 전 사용. 5분 이내 완료 목표.
Evidence First 원칙에 따라, 여기서 나온 항목은 바로 evidence-log.md에
넣지 않고 Draft로만 남긴 뒤 별도 승인을 거쳐 반영한다.

---

## 0. Purpose (Goal Drift 점검)
- [ ] 이번 쓰레드 시작 시 목표는 무엇이었는가?
- [ ] 실제로 달성된 것은 무엇인가?
- [ ] 목표가 중간에 바뀌었다면, 명시적 재승인을 거쳤는가?

---

## A. Deliverables
- [ ] 모든 산출물이 실제 생성되었는가?
- [ ] 임시파일만 있고 GitHub에는 없는 것은 없는가?
- [ ] Draft인데 완료라고 말한 것은 없는가?

## B. Delegation
- [ ] 사람이 대신한 기계적 작업이 있었는가?
- [ ] 다른 AI가 할 수 있었던 작업을 사람에게 시켰는가?
- [ ] Delegation Cost 발생 사례는 없는가?

## C. Approval
- [ ] 승인 없이 진행한 구현이 있었는가? (Proposal Drift)
- [ ] 모호한 신호를 승인으로 잘못 해석한 사례가 있었는가?
- [ ] 사람이 내려야 할 결정을 AI가 생략했는가? (Approval Bypass)

## D. Question Coverage
- [ ] 번호 매긴 질문 모두 답했는가?
- [ ] 새 질문이 생기면서 기존 질문이 누락되지 않았는가? (E-007 예방)

## E. Storage
- [ ] 로컬 커밋만 되었는가, GitHub Push까지 되었는가?
- [ ] 다음 쓰레드에서 사라질 것이 있는가?
- [ ] 다음 쓰레드에서 반드시 이어야 할 것은 무엇인가?

## F. Recovery
- [ ] 지금 종료하면 다음 쓰레드에서 복구 비용이 얼마나 드는가?

## Persistence Check
- [ ] GitHub 반영 완료
- [ ] 로컬(컨테이너)에만 존재
- [ ] 컨테이너 임시파일만 존재
- [ ] 다음 쓰레드에서 소멸 예정인 것이 있는가?

## Learning Check
이번 쓰레드에서 새롭게 발견된 것은?
- [ ] 없음
- [ ] Evidence 후보
- [ ] Methodology 수정
- [ ] Cost Taxonomy 수정
- [ ] Pipeline 수정
- [ ] Automation 후보

---

## Closing Review 원시 카운트 (누적 기록용)

※ 현재 Score는 **Experimental**입니다. 가중치는 아직 확정되지 않았으며
실제 운영 데이터를 통해 계속 보정됩니다. 지금 단계의 목적은 정확한
점수가 아니라 "이 측정 체계가 실제로 작동하는지" 테스트하는 것입니다.
가중치가 완성되면 이 문구를 지우고 재측정합니다.

임시 공식 (동일 가중치, 단순 합산): 아래 6개 항목 카운트의 합

| Thread | Human Mediation | Delegation Cost | Proposal Drift | Approval Bypass | Question Loss | Recovery | **Experimental Score (합)** |
|---|---|---|---|---|---|---|---|
| #1 (0703 CostMangm.Prtl.시작, 본 쓰레드) | ~6 | 2 | 3 | 2 | 1 | 2 | **16** |

(본 쓰레드 값은 대화 내용 기반 수기 추정 — 정밀 측정 아님. 다음 쓰레드부터
# Thread Closing Review Checklist

매 쓰레드 종료 전 사용. 5분 이내 완료 목표.
Evidence First 원칙에 따라, 여기서 나온 항목은 바로 evidence-log.md에
넣지 않고 Draft로만 남긴 뒤 별도 승인을 거쳐 반영한다.

---

## 0. Purpose (Goal Drift 점검)
- [ ] 이번 쓰레드 시작 시 목표는 무엇이었는가?
- [ ] 실제로 달성된 것은 무엇인가?
- [ ] 목표가 중간에 바뀌었다면, 명시적 재승인을 거쳤는가?

---

## A. Deliverables
- [ ] 모든 산출물이 실제 생성되었는가?
- [ ] 임시파일만 있고 GitHub에는 없는 것은 없는가?
- [ ] Draft인데 완료라고 말한 것은 없는가?

## B. Delegation
- [ ] 사람이 대신한 기계적 작업이 있었는가?
- [ ] 다른 AI가 할 수 있었던 작업을 사람에게 시켰는가?
- [ ] Delegation Cost 발생 사례는 없는가?

## C. Approval
- [ ] 승인 없이 진행한 구현이 있었는가? (Proposal Drift)
- [ ] 모호한 신호를 승인으로 잘못 해석한 사례가 있었는가?
- [ ] 사람이 내려야 할 결정을 AI가 생략했는가? (Approval Bypass)

## D. Question Coverage
- [ ] 번호 매긴 질문 모두 답했는가?
- [ ] 새 질문이 생기면서 기존 질문이 누락되지 않았는가? (E-007 예방)

## E. Storage
- [ ] 로컬 커밋만 되었는가, GitHub Push까지 되었는가?
- [ ] 다음 쓰레드에서 사라질 것이 있는가?
- [ ] 다음 쓰레드에서 반드시 이어야 할 것은 무엇인가?

## F. Recovery
- [ ] 지금 종료하면 다음 쓰레드에서 복구 비용이 얼마나 드는가?

## Persistence Check
- [ ] GitHub 반영 완료
- [ ] 로컬(컨테이너)에만 존재
- [ ] 컨테이너 임시파일만 존재
- [ ] 다음 쓰레드에서 소멸 예정인 것이 있는가?

## Learning Check
이번 쓰레드에서 새롭게 발견된 것은?
- [ ] 없음
- [ ] Evidence 후보
- [ ] Methodology 수정
- [ ] Cost Taxonomy 수정
- [ ] Pipeline 수정
- [ ] Automation 후보

---

## Closing Review 원시 카운트 (누적 기록용)

※ 현재 Score는 **Experimental**입니다. 가중치는 아직 확정되지 않았으며
실제 운영 데이터를 통해 계속 보정됩니다. 지금 단계의 목적은 정확한
점수가 아니라 "이 측정 체계가 실제로 작동하는지" 테스트하는 것입니다.
가중치가 완성되면 이 문구를 지우고 재측정합니다.

임시 공식 (동일 가중치, 단순 합산): 아래 6개 항목 카운트의 합

| Thread | Human Mediation | Delegation Cost | Proposal Drift | Approval Bypass | Question Loss | Recovery | **Experimental Score (합)** |
|---|---|---|---|---|---|---|---|
| #1 (0703 CostMangm.Prtl.시작, 본 쓰레드) | ~6 | 2 | 3 | 2 | 1 | 2 | **16** |

(본 쓰레드 값은 대화 내용 기반 수기 추정 — 정밀 측정 아님. 다음 쓰레드부터
Closing Review 시점에 실시간으로 채워나가는 것을 목표로 함)
Closing Review 시점에 실시간으로 채워나가는 것을 목표로 함)