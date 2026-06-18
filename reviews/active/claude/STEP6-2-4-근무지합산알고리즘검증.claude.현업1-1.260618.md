# STEP6-2-4 — 근무지합산 알고리즘 검증

> 작성일: 2026-06-18
> 상태: 확정

---

## STEP6-2-4 결론

calc-engine 입력 구조와 충돌 없음.
allowanceRows 동일 수당별 hours 누적 합산 후 각 필드에 분배하는 방식으로 확정.
표준/맞춤 혼재 시 customPay 필드로 분리 처리 가능.
History 복원값 → 근무지합산 연결 가능.
5인 미만 게이팅은 calc-engine 내부가 아니라 변환 계층에서 처리한다.

---

## §1. 동일 수당별 합산 방식

calc-engine은 nightHours / overtimeHours / holidayHours를 독립 필드로 수신.
mapEntriesToCalcInput()에서 동일 수당 여러 행의 hours를 누적 합산 후 각 필드에 분배.

예시:
| allowanceRows | CalcInput 분배 |
|---|---|
| 연장 2h + 연장 3h | overtimeHoursManual = 5 |
| 야간 1h + 야간 2h | nightHoursPerDay = 3 |

---

## §2. 표준/맞춤 혼재 처리

- 표준가산: nightHoursPerDay / overtimeHoursManual / holidayHoursPerDay 각 필드
- 맞춤가산: customPay 필드 (계산 결과값 직접 전달)
- 두 경로 독립적으로 합산 — 충돌 없음

---

## §3. 5인 미만 사업장 게이팅

- isSmallBiz는 CalcInput에 포함되지 않음
- calc-engine 내부에는 5인 미만 가산 제한 로직이 없음
- STEP6 설계 기준으로 게이팅은 mapEntriesToCalcInput() 등 변환 계층에서 처리
- 5인 미만 토글은 주휴·연차 OFF가 아니라 연장·야간·휴일의 가산분만 제거하는 의미로 적용
- 엔진 수정 없이 구현 가능 확인

---

## §4. History 복원값 연결

- handleHistoryReload에서 inputs.customPremiumRows 복원 패턴 존재
- STEP6 구현 시 inputs.allowanceRows도 동일 패턴으로 복원 가능
- 연결 가능 확인

---

## §5. 구현 전 필요 작업

| 항목 | 내용 |
|------|------|
| 구현 원칙 | mapEntriesToCalcInput()에서 합산 처리, 엔진 직접 수정 금지 |
| 5인 미만 처리 | 변환 계층에서 isSmallBiz 참조하여 가산분 0 처리 |
| 다음 단계 | STEP6-1 — 연차 개선 (선행조건 충족) |

---

*본 문서는 STEP6-2-4 산출물이며, 코드 수정 지시를 포함하지 않는다.*
