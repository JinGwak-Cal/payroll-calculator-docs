# Thread Closing Review Checklist

매 쓰레드 종료 전 사용.
Evidence First 원칙에 따라, 여기서 나온 항목은 바로 evidence-log.md에
넣지 않고 Draft로만 남긴 뒤 별도 승인을 거쳐 반영한다.

**목적 구분**: Immediate 경로의 목적은 "안전하게 종료하는 것"이고,
Delayed 경로의 목적은 "현재 상태와 과거 상태를 재동기화(Resync)하는
것"이다. 아래 Baseline Check가 자동으로 둘 중 하나로 분기시킨다.

---

## Baseline Check (최우선, 분기점)

- [ ] 이 쓰레드 시작 시점의 Repository baseline(commit SHA)을
      확인했는가? (없으면 쓰레드 시작 시 기록해두는 절차 필요 —
      research-backlog.md 참조)
- [ ] 지금 origin의 최신 상태와 그 baseline을 비교했을 때, 변화가
      있는가? (`git fetch` 후 `git log <baseline>..origin/main --oneline`)

```
Repository Drift?
├── No  → Immediate Closing (아래 0~F, Persistence, Learning만)
└── Yes → Delayed Closing (아래 전체 + Delayed 전용 항목)
```

Reference Time (Delayed인 경우 반드시 기록):
```
Thread Created: (쓰레드 시작 시각/커밋)
Reviewed:       (지금)
Gap:            (차이)
```

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

---

## Delayed Closing 전용 항목 (Baseline Drift = Yes 인 경우만)

### G. Reality Check
- [ ] 당시 예상했던 결과와 지금 실제 Repository 상태가 같은가?
      (다르면 Missing Artifact Check로)

### H. History Check
- [ ] 그 사이 main/ai/draft 변경, PR Merge, Actions 실행이 있었는가?

### I. Dependency Check
- [ ] 이 쓰레드가 만들려는 문서를, 이미 다른 쓰레드의 작업이
      참조하거나 대체하고 있는가?

### J. Current Step Check
- [ ] 당시 current-step과 지금 current-step이 같은가, 이미 다음
      단계로 넘어갔는가?

### K. Merge Safety
- [ ] 이 쓰레드의 산출물을 그대로 merge하면 현재 상태와 충돌하는가?
      (주의: "merge conflict 없음"과 "release-gate/Actions 검증
      통과"는 다른 개념 — 후자까지 확인)

### L. Missing/Unexpected/Duplicate Artifact Check
- [ ] Expected(당시 예상 산출물) vs Actual(현재 Repository 실제
      상태)을 비교했는가?
- [ ] Missing(있어야 하는데 없는 것)은 없는가?
- [ ] Unexpected(예상에 없던 것이 생겼는가)는 없는가?
- [ ] Duplicate(같은 내용이 파일 안에 중복되어 있는가)는 없는가?
      (실제 사례: thread-closing-checklist.md 전체가 통째로 반복된 사고)

### M. Drift Check
- [ ] 이 쓰레드가 만든 문서가 지금도 최신인가, 이미 이후 작업이
      대체(Superseded)했는가?
      (결과는 여기 적지 않고, 실제 문서(예: direction-hypothesis.md)에
      Historical/Superseded로 표시하러 이동한다 — 체크리스트는
      템플릿으로 유지, 특정 결과값을 담지 않는다)

### N. Identifier Check (Evidence/MH 번호 등)
- [ ] 현재 Repository 기준 마지막 번호를 확인했는가?
- [ ] 번호 충돌 여부를 확인했는가?
- [ ] **Identifier Source**: Repository가 번호의 Source of Truth다.
      쓰레드 안에서 기억하거나 예상한 번호가 아니다.
- [ ] **Identifier Allocation Principle**: 과거 시점에 예상했던
      번호를 쓰지 않는다. 항상 현재 Repository 상태 기준으로 새로
      할당한다. (예: 원래 E-008이 될 예정이었어도, 이미 E-008이
      존재하면 E-011 등으로 재배정. 문서에는 `Date`(사건 발생일)와
      `Recorded`(등록일) 둘 다 기록)

### O. Historical Classification
- [ ] 이번에 확인된 옛 문서에 상태 표시를 남겼는가?
      (상태값: Draft / Current / Historical / Superseded / Rejected
      — 필요한 것만 사용, 전부 강제 아님)

### P. Entry Point Update
- [ ] 후임자가 옛 문서를 최신으로 착각하지 않도록 START-HERE.md나
      관련 문서의 참조를 갱신했는가?

---

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
