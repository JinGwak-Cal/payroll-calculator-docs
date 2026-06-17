# STEP6-2-2 — 행 배열 구조 + CalcInput 변환 검토

- **문서 종류**: STEP6-2-2 산출물
- **작성**: Claude (현업1-1 협업)
- **기준 시각**: 2606.15
- **참조**: STEP6-2-1 · calc-engine.ts 분석

---

## §1. 엔진 구조 확인

calc-engine은 조합가산 엔진이 아님. night/overtime/holiday 독립 계산 후 단순 합산:

```
grossPay = basePay + nightPay + overtimePay + holidayPay + customPay
```

- "이중/삼중가산" 개념은 엔진에 없음 — UI 라벨 수준의 표현일 뿐
- 각 수당 배율은 독립 필드: `nightPremiumRate` / `overtimePremiumRate` / `holidayPremiumRate`
- 조합 판별·배율 중첩·시간 중복 조정 로직 없음

---

## §2. 표준가산 CalcInput 분해 규칙 (확정)

표준가산 행의 `premiumRate = n × 50`은 각 수당에 **50%씩 분배**:

| 행 저장값 | 엔진 분해 |
|---|---|
| 야간 단일 50% 4h | `nightPremiumRate=0.5`, `nightHours=4` |
| 연장+야간 100% 2h | `overtimePremiumRate=0.5` `overtimeHours=2` + `nightPremiumRate=0.5` `nightHours=2` |
| 연장+야간+휴일 150% 1h | 세 수당 각각 `premiumRate=0.5`, `hours=1` |

규칙: 각 수당 배율 = **0.5 고정**. `premiumRate`는 isStandard 판정용으로만 사용.

---

## §3. 맞춤가산 MVP 범위 확정

- MVP: **맞춤가산은 단일 수당만 허용**
- 맞춤 이중/삼중 조합: 직접 지원 안 함
- 필요 시 안내문구로 단일 행 여러 개 추가 유도:

> "맞춤가산은 수당별로 따로 입력합니다.
> 연장+야간처럼 여러 수당의 맞춤가산이 필요하면,
> 연장 맞춤가산과 야간 맞춤가산을 각각 추가해 주세요."

맞춤 단일 CalcInput 분해:
```
{ selectedAllowances: ["야간"], premiumRate: 30, premiumHours: 2 }
→ nightPremiumRate=0.3, nightHours=2
```

---

## §4. mapEntriesToCalcInput() 구조 (A안 기반 확정)

**전제 (A안 확정):**
- 동일 수당 + 서로 다른 premiumRate = MVP 금지
- 동일 수당은 여러 행에 존재할 수 있으나 premiumRate는 동일해야 한다.
- 따라서 `nightPremiumRate` / `overtimePremiumRate` / `holidayPremiumRate`는 항상 단일값
- UI 하드 차단: "야간수당은 이미 입력되어 있습니다. 동일 수당은 하나의 가산율만 적용할 수 있습니다."

```typescript
function mapEntriesToCalcInput(
  entries: PremiumAllowanceEntry[]
): Partial<CalcInput> {
  const result: Partial<CalcInput> = {}

  for (const entry of entries) {
    const isCustom = entry.premiumRate !== entry.selectedAllowances.length * 50
    const perRate = 0.5  // 표준가산은 항상 수당별 50%

    for (const allowance of entry.selectedAllowances) {
      const rate = isCustom ? entry.premiumRate / 100 : perRate

      if (allowance === "야간") {
        result.includeNight = true
        result.nightHoursPerDay = (result.nightHoursPerDay ?? 0) + entry.premiumHours
        result.nightPremiumRate = rate
      }
      if (allowance === "연장") {
        result.includeOvertime = true
        result.overtimeHoursManual = (result.overtimeHoursManual ?? 0) + entry.premiumHours
        result.overtimePremiumRate = rate
      }
      if (allowance === "휴일") {
        result.includeHoliday = true
        result.holidayHoursPerDay = (result.holidayHoursPerDay ?? 0) + entry.premiumHours
        result.holidayPremiumRate = rate
      }
    }
  }
  return result
}
```

---

## §5. 미확정 — 후속 과제

| 항목 | 상태 | 후속 |
|---|---|---|
| 동일 수당 + 다른 rate | MVP 금지 확정 (A안) | — |
| 맞춤 이중/삼중 지원 | MVP 제외 | STEP6+ 별도 엔진 검토 |
| History 저장 구조 검증 | 미확정 | STEP6-2-3 |
| 근무지합산 알고리즘 | 미확정 | STEP6-2-4 |

---

*본 문서는 STEP6-2-2 산출물이며, 코드 수정 지시를 포함하지 않는다.*
