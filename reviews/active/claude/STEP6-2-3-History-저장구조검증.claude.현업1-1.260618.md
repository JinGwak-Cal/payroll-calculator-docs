# STEP6-2-3 — History 저장 구조 검증

> 작성일: 2026-06-18
> 상태: 확정

---

## STEP6-2-3 결론

History 저장 구조는 변경하지 않는다.
allowanceRows는 HistoryEntry.inputs 내부에 추가한다.
저장값은 PremiumAllowanceEntry[] 원본 입력값만 허용한다.
premiumAmount 등 파생값 저장은 금지한다.
즐겨찾기/삭제 로직과 충돌 없음.
단, 코드에는 PremiumAllowanceEntry 타입이 아직 없으므로 구현 전 타입 신설 및 복원 검증 함수가 필요하다.

---

## §1. allowanceRows 저장 위치

```
HistoryEntry.inputs.allowanceRows: PremiumAllowanceEntry[]
```

- HistoryEntry 본체 = 요약값 (mainPay, netPay, label 등)
- 상세 입력 복원값 = inputs: Record<string, unknown> 에 저장 (기존 구조 활용)
- 별도 필드 추가 불필요

---

## §2. 저장/복원 구조

저장값:
```
{
  id,
  selectedAllowances,
  premiumRate,
  premiumHours
}
```

복원 흐름:
```
inputs.allowanceRows → mapEntriesToCalcInput() → 계산 엔진 재계산
```

금액은 저장하지 않고 불러온 뒤 재계산.

---

## §3. premiumAmount 저장 금지

| 구분 | 필드 |
|------|------|
| 저장 허용 | id · selectedAllowances · premiumRate · premiumHours |
| 저장 금지 | premiumAmount · premiumType · mode · allowanceCombo |

근거: D-05-04 (파생값 저장 금지 원칙)

---

## §4. 즐겨찾기/삭제/불러오기 충돌 없음

- 즐겨찾기: isFavorite 플래그 토글 — inputs 내부와 무관
- 삭제: id 기준 제거 — 충돌 없음
- 일반 저장 7개 제한: non-favorite 기준 — 충돌 없음
- 즐겨찾기 저장: 별도 제한 없음 — 충돌 없음

---

## §5. 구현 전 필요 작업

| 항목 | 내용 |
|------|------|
| 구현 원칙 | HistoryEntry 최상위 필드 추가 금지, inputs 내부에만 allowanceRows 추가 |
| 타입 신설 | PremiumAllowanceEntry (현재 코드 미존재, 대응물은 CustomPremiumRow) |
| 복원 검증 함수 | 저장값 → PremiumAllowanceEntry[] 캐스팅 및 유효성 검증 |
| 확인 필요 파일 | Home.tsx · CustomPremiumCard.tsx · use-premium.tsx · history.ts |
| 다음 단계 | STEP6-2-4 — 근무지합산 알고리즘 |

---

*본 문서는 STEP6-2-3 산출물이며, 코드 수정 지시를 포함하지 않는다.*
