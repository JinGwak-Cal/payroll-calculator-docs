# 페이첵 웍북 수당근무 변경 기능: Rule Lifecycle Walkthrough #2

**성격**: Walkthrough #1(기본근무 변경)과 달리, 이건 **가상 시나리오가
아니라 오늘(2026-07-17~19) 실제로 진행된 AllowanceBrowser/D-PW-036
작업의 사후 재구성**이다. 진짜 Evidence로 Reference Components의
범용성을 검증하는 게 목적이므로 가설이 아니라 실측이다.

Gate/Role/Evidence 정의는 전부 `reference-components.md`를 참조하고
여기서 재정의하지 않는다.

---

## 1. Work Instruction (실제 발생)

**WI-2026-002**: "수당근무 항목을 목록으로 보고, 편집·삭제할 수
있게 해달라. 메모도 남길 수 있어야 한다." (D-PW-036, D-PW-031)

## 2. 적용 Rule (오늘 실제 사용된 것)

| Rule ID | 이 시나리오의 Trigger | 실제 결과 |
|---|---|---|
| A-08 | P-1/P-2/P-3 충돌 발견, 구현 여부 제안 | ⚠️ 최소 6회 위반(Appendix A) — Walkthrough #1의 이론과 달리, **G3(Design Permission Gate)에 해당하는 실제 서버측 통제가 없어서 대화 텍스트 규칙만으로 막으려 하다가 반복 실패** |
| C-07 | "제수당" 존재 여부, 편집화면 확정 여부 등 주장 | 1회 위반(DEFER-018), grep 실측 전 "없다" 단정 |
| C-14 | R19 규칙 제안 | 1회 위반(즉시 실행) |
| PW-01류(도메인 Guard) | 가산시간 Validation, memo 7자 제한 | ✅ 준수 — Preflight에서 실측 확인 후 trim/clip 가드 구현 |
| PW-02류(고위험 Gate) | 해당 없음(운영데이터 영향 아님, 앱 코드 변경뿐) | 적용 안 됨 — **Walkthrough #1과 다른 점**: 이 사례는 고위험 배포가 아니라 항상 G4가 발동하는 건 아님을 보여줌 |

## 3. C1 판정 (실제)

| C1 요소 | 판정 |
|---|---|
| What | 통과 (목록+편집+삭제+메모) |
| How | 통과 (Contract→Preflight→구현→검증, 오늘 실제 순서) |
| Interpretation | 조건부 통과 → 도중에 재정의됨(인라인→목록+Drawer 재사용, D-PW-036) |
| Evidence | 통과 (Preflight 보고, Contract 문서, 구현 보고, e2e Playwright) |
| Success | 통과 (Acceptance Checklist 10/10) |
| Transition | **조건부 통과** — 오늘 실제로 이 Transition 판단(검토→실행)에서 A-08이 6회 깨짐 |

**결론**: C1-Approval Required였고, 실제로 사용자 승인을 거쳐
진행됨 — 다만 그 승인 경로가 Gate가 아니라 대화 텍스트("!", "동의")
였다는 게 Walkthrough #1의 P0 결손(server-side phase transition
부재)을 실제로 재현한다.

## 4. 단계별 Walkthrough (실제 발생 순서, Gate ID는 참조만)

| 순서 | 실제 사건 | Gate | 실제 Evidence |
|---|---|---|---|
| 0 | WI 발생(AllowanceBrowser 필요) | G1 | current-step.md 구조3 |
| 1 | Contract 작성(AllowanceBrowser.contract.md) | G2 | Contract 파일 |
| 2 | Preflight(Replit 실측: A-1~A-4) | C-07 | Preflight 보고 원문 |
| 3 | P-1/P-2/P-3 충돌 발견 → 제안 | G3 | 채팅 원문 |
| 4 | **승인 없이 파일럿 실행 시도(위반)** | G3 위반 | doc48(파트너 지적) — Walkthrough #1의 "실패주입 A"가 실제로 일어난 사례 |
| 5 | 사용자 재지적 → 승인 후 구현 지시 | G3 (사후 정정) | 채팅 원문 |
| 6 | Replit 구현 + 자체 architect 리뷰 | G4 상당(코드 리뷰) | 구현 보고 |
| 7 | memo UI 추가 승인 → 재구현 | G3 | "memo UI 구현을 승인합니다" 원문 |
| 8 | e2e Playwright 검증 | G5 | 구현 보고 Acceptance Checklist |
| 9 | RCA 파일럿(A-08/C-07/C-14) 시도 | G6 상당 | 오늘 파일럿 시도 기록(중단됨) |

## 5. Reference Components 범용성 검증 결과

| 검증 항목 | Walkthrough #1(가상) | Walkthrough #2(실제) | 일치? |
|---|---|---|---|
| Gate 구조(G1~G6)가 다른 기능에도 적용되는가 | 설계 시점 가정 | **적용됨** — 다만 G3가 실제로는 시스템이 아니라 대화 텍스트로만 존재해서 반복 뚫림 | 부분 일치 — 구조는 맞으나 실제 구현이 없음 |
| RCA Verdict(Prevented by Control) | 이론적으로 제안 | **한 번도 발생 안 함** — 오늘 6회 전부 Violated였지 Prevented가 없었음. 즉 "시스템이 막아준" 사례가 실제로는 0건 | **불일치 — 중요한 발견** |
| Evidence Ledger 스키마 | 이론적 스키마 | 오늘 실제론 grep/파일diff/채팅원문으로 대체 사용 — correlation_id 같은 개념은 있었지만(파일명, D-PW 번호) formal ledger는 없었음 | 부분 일치 |

---

## 6. 이번 Walkthrough가 REA/RCA/Condition1에 되돌리는 것

**핵심 발견**: Walkthrough #1의 P0 Backlog(server-side phase
transition, approval-to-artifact binding)가 "설계 시 예측"이 아니라
**오늘 실제로 정확히 그 자리에서 문제가 됐다.** A-08은 REA 기준
Q1~Q4를 다 갖춘 AE=Yes 규칙이었지만(REA-001), 그걸 강제하는
G3(Design Permission Gate)에 해당하는 실제 시스템이 없어서 —
텍스트 규칙만으로는 6번 뚫렸다.

→ calibration-notes.md로 이어짐.
