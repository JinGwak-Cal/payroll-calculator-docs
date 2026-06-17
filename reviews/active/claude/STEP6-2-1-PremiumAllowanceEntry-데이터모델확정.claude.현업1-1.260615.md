# STEP6-2-1 — 가산수당 최소 저장 단위 확정

- **문서 종류**: STEP6-2-1 데이터모델 확정 산출물
- **작성**: Claude (현업1-1 협업)
- **기준 시각**: 2606.15
- **상위 참조**: STEP5-4-Drawer-확정안 · manual-v14 §J-1 · §1352~1356 · §1659~1662

> ⚠ 본 문서는 저장 단위 확정 문서이며,
> CalcInput 변환 함수(mapEntriesToCalcInput)는 확정하지 않는다.
> mapEntriesToCalcInput()은 STEP6-2-2 이후 별도 검토한다.

---

## 1. 최소 저장 단위 확정

```typescript
type PremiumAllowanceEntry = {  // 저장 단위: id + selectedAllowances + premiumRate + premiumHours
  id: string                           // 편집/React key/저장/불러오기 식별용
  selectedAllowances: AllowanceType[]  // 수당 종류 배열
  premiumRate: number                  // 실제 가산율 (숫자, 예: 50 / 100 / 30)
  premiumHours: number                 // 가산 적용 시간
}
```

---

## 2. 저장하지 않는 값 (파생 가능)

| 필드 | 이유 |
|---|---|
| `premiumAmount` | 계산값 — §J-1 실시간 계산 원칙, 저장 금지 |
| `premiumType` | `selectedAllowances.length`로 파생 |
| `expectedRate` | `selectedAllowances.length * 50`으로 파생 |
| `isStandard` | `premiumRate === expectedRate`로 파생 |
| `isCustom` | `premiumRate !== expectedRate`로 파생 |
| `allowanceCombo` | `selectedAllowances.join("+")` 로 파생 |
| `mode` | `isStandard/isCustom`으로 파생 — 이중진실 위험 |

---

## 3. 파생값 정의

```typescript
const premiumType    = entry.selectedAllowances.length
// 1 = 단일가산, 2 = 이중가산, 3 = 삼중가산

const expectedRate   = entry.selectedAllowances.length * 50
// 단일 → 50, 이중 → 100, 삼중 → 150

const isStandard     = entry.premiumRate === expectedRate
const isCustom       = entry.premiumRate !== expectedRate
const allowanceCombo = entry.selectedAllowances.join("+")
```

---

## 4. 표준/맞춤 판정 기준 (확정)

**절대값 기준 금지:**
```typescript
// ❌ 잘못된 방식
const STANDARD_RATES = [50, 100, 150]
if (STANDARD_RATES.includes(value)) { ... }
```

**선택개수 기준 사용 (확정):**
```typescript
// ✅ 올바른 방식
const expectedRate = selectedAllowances.length * 50
const isStandard   = premiumRate === expectedRate
```

이유: 단일 수당에서 100%는 맞춤이지만, 이중 수당에서 100%는 표준이다.
절대값으로 판정하면 오분류 발생.

---

## 5. 맞춤가산 입력 차단 규칙 (확정)

```typescript
// 맞춤가산 입력창에서 가산율 입력 시
const expectedRate = selectedAllowances.length * 50
if (value === expectedRate) {
  showGuide(
    `${value}%는 표준가산으로 자동 적용됩니다.\n` +
    `맞춤가산에는 표준과 다른 가산율만 입력해 주세요.`
  )
  rejectValue()
}
```

---

## 6. 동일수당 중복 규칙 (확정)

### 허용 — 소프트 경고
동일 수당이 여러 행에 등장할 수 있다.

> MVP에서는 시간구간 정보(startTime/endTime)를 저장하지 않으므로,
> 시스템은 시간구간 중복 여부를 검증하지 않는다.
> 사용자가 시간구간이 다르다고 판단한 경우, 소프트 경고 후 허용한다.
현실 케이스 근거:
```
행1: [연장] 4시간 50%        (18:00~22:00, 연장 단일)
행2: [연장, 야간] 2시간 100% (22:00~24:00, 연장+야간 이중)
→ 연장이 두 행에 등장하지만 시간구간이 다르므로 정상
```

구현:
```typescript
// 동일 수당 감지 시 소프트 경고 (확인 후 허용)
const overlap = newAllowances.filter(a =>
  entry.selectedAllowances.includes(a)
)
if (overlap.length > 0) {
  showConfirm(
    `${overlap.join("+")} 수당이 이미 포함된 항목이 있어요.\n` +
    `시간구간이 다른 경우에만 추가할 수 있습니다. 계속하시겠어요?`
  )
}
```

### 금지 — 하드 차단
동일 수당에 **표준↔맞춤 동시 적용** 차단.
근거: manual-v14 §1352~1356 "대체관계 원칙: 동일 수당 정형+맞춤 동시 선택 = 이중계산" / §1659~1662 "선택 수당 중복 불가 (v12.0 확정)"

> MVP 저장 단위에는 startTime/endTime이 없으므로, 동일 수당의 표준↔맞춤 동시 입력은 시간구간 구분이 불가능하다.
> 따라서 MVP에서는 기본 하드 차단한다.
> 시간구간 필드가 도입되면 동일 시간구간 기준으로 재검토한다.

```typescript
// 동일 수당 + 표준↔맞춤 충돌 = 하드 차단
const entryIsCustom = entry.premiumRate !== entry.selectedAllowances.length * 50
const newIsCustom   = newRate !== newAllowances.length * 50
const overlap       = newAllowances.filter(a =>
  entry.selectedAllowances.includes(a)
)
if (overlap.length > 0 && entryIsCustom !== newIsCustom) {
  showError(
    `동일 수당에 표준가산과 맞춤가산을 동시에 적용할 수 없습니다.`
  )
  return // 차단
}
```

---

## 7. 저장/불러오기/합산 연결 가능성 확인

| 기능 | 현재 구조로 가능? | 근거 |
|---|---|---|
| 저장 | ✅ | id + selectedAllowances + premiumRate + premiumHours 저장 |
| 불러오기 | ✅ | id 기준 행 식별 후 3개 계산 필드로 상태 복원 |
| 재탭 편집 | ✅ | id로 특정 행 식별, Drawer에 데이터 로드 |
| 요약 표시 | ✅ | selectedAllowances + premiumHours + isStandard로 파생 |
| 근무지합산 | △ 가능성 확보 | selectedAllowances 기준 수당 계열 필터링은 가능. 실제 합산 알고리즘은 STEP6-2-4에서 확정 |
| 시간구간 자동검사 | ❌ MVP 이후 | startTime/endTime 필드 부재 |

---

## 8. 미확정 — 후속 과제

| 항목 | 상태 | 후속 단계 |
|---|---|---|
| `mapEntriesToCalcInput()` | ❌ 미확정 | STEP6-2-2 이후 별도 검토 |
| 이중/삼중 가산율 → 각 수당 배분 방식 | ❌ 미확정 | STEP6-2-2 |
| 행 배열 구조 (`allowanceRows[]`) | ❌ 미확정 | STEP6-2-2 |
| History 저장 구조 검증 | ❌ 미확정 | STEP6-2-3 |
| 근무지합산 알고리즘 | ❌ 미확정 | STEP6-2-4 |
| startTime/endTime 시간구간 필드 | ❌ MVP 이후 | 후속 과제 |

---

*본 문서는 STEP6-2-1 데이터모델 확정 산출물이며, 코드 수정 지시를 포함하지 않는다.*
*CalcInput 변환 함수는 이 문서에서 확정하지 않는다.*
