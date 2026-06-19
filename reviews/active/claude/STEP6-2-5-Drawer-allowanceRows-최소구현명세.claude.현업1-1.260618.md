# STEP6-2-5 — Drawer/allowanceRows 최소구현명세

> 작성일: 2026-06-18
> 상태: 확정
> 목표: 코딩 가능한 최소 UX 계약서 (스타일/토큰/애니메이션 제외)

---

## 결론

아래 항목만 확정하면 STEP6-2 구현 진입 가능.
스타일·색상·여백·애니메이션은 UI-Audit/분류매뉴얼 단계에서 별도 확정.

---

## 0. 입력 진입점 단일화

기존 "가산수당 설정" 버튼은 제거한다.
PremiumScreen 전체화면 입력 경로는 STEP6-2 MVP에서 사용하지 않는다.
가산수당 입력의 단일 진입점은 ResultGrid 가산수당 영역 Row → Drawer로 통일한다.

흡수 대상은 수당 타입, 칩 선택, rate/hours 입력, 완료 조건, id 기반 row 관리 로직으로 한정한다.
PremiumScreen 화면 구조와 CustomPremiumCard UI는 흡수 대상이 아니다.

흡수 대상 (use-premium.tsx 로직 기준):
- 칩 선택 토글 로직
- 가산율/가산시간 입력 핸들러
- 완료 조건 판정 로직 (selectedAllowances.length > 0 && rate !== null && hours !== null)
- 금액 계산 로직 (Math.floor(hours × wage × rate/100), D-01-01 floor 원칙 준수)

흡수 안 함 (구조가 다름):
- 고정 3행 visible/hidden 구조 (showNextCustomRow) — allowanceRows는 자유 추가/삭제 구조
- resetCustomRows — allowanceRows 전용 reset 별도 구현
- screen="premium" 라우팅 — 본 §0에 따라 제거

처리 순서:
1. 위 흡수 대상 로직 확인
2. 흡수 대상 로직만 Drawer / allowanceRows 구조로 이전
3. ResultGrid → Drawer 단일 진입점 구현
4. "가산수당 설정" 버튼 제거
5. PremiumScreen 경로 제거
6. 더 이상 참조되지 않으면 PremiumScreen / CustomPremiumCard를 dead component로 확인 후 삭제

선삭제 금지 — 흡수 → 참조 제거 확인 → 삭제 순서 준수.

---

## 1. Drawer가 언제 열리는가

- ResultGrid 가산수당 영역 Row 전체 탭 → 하단 Drawer 열림
- 대상: 연장·야간·휴일 (+ 필요시 맞춤가산 분기)
- 맞춤가산은 별도 입력영역이 아니라 Drawer 내부 [맞춤 가산율로 변경 →] 분기로 진입
- 비대상: 주휴 / 연차 / 공제차감

---

## 2. 행 1개가 무엇을 의미하는가

- 행 = 근무상황 1건
- 수당 총합 입력기 아님
- 동일 수당이 여러 행에 등장 가능 (시간구간이 다른 경우)

---

## 3. 사용자 입력 순서

1. 수당 선택:
   - 표준가산: [연장][야간][휴일] 복수 선택 가능
   - 맞춤가산: [맞춤 가산율로 변경 →] 탭 후 단일 수당만 허용 (MVP)
2. 시간 입력: 스테퍼 또는 숫자 탭 → 키패드
3. 가산율 확인: 표준=안내문구 자동 / 맞춤=직접 입력
4. 즉시 결과 표시
5. [이 수당 추가하기] 탭 → 행 저장

---

## 4. 완료 조건

- selectedAllowances.length > 0
- premiumHours > 0
- premiumRate > 0 (표준: 자동 / 맞춤: 직접입력)
- 위 3개 충족 시 [이 수당 추가하기] 활성화

---

## 5. 추가/수정/삭제

- 추가: [다른 수당 추가] 탭 → 새 Drawer 열림
- 수정: 행 요약 탭 → Drawer에 기존 값 로드 → 전부 수정 가능
- 삭제: 별도 삭제 동작 (수정 화면 내 삭제 버튼)
- 칩: 완료 전 비선택 칩 유지 / 완료 후 비선택 칩 제거

---

## 6. 표준/맞춤 구분

| 구분 | 조건 | UI |
|------|------|-----|
| 표준 | premiumRate === selectedAllowances.length * 50 | 안내문구만 |
| 맞춤 | 그 외 | [맞춤 가산율로 변경 →] 탭 후 입력 필드 노출 |

- 동일 수당 표준↔맞춤 동시 적용: 하드 차단 (MVP)
- 동일 수당 여러 행 (다른 시간구간): 소프트 경고 후 허용
- isStandard는 저장하지 않고 계산 시 파생한다.
  판정식: premiumRate === selectedAllowances.length * 50

---

## 7. allowanceRows 저장값 구조

타입 정의:
```ts
type AllowanceType = 'overtime' | 'night' | 'holiday'
type PremiumAllowanceEntry = {
  id: string
  selectedAllowances: AllowanceType[]
  premiumRate: number
  premiumHours: number
}
```

저장값 예시:
```json
{
  "allowanceRows": [
    {
      "id": "row-1",
      "selectedAllowances": ["night"],
      "premiumRate": 50,
      "premiumHours": 4
    }
  ]
}
```

저장 금지: premiumAmount / premiumType / isStandard / allowanceCombo / mode

---

## 8. Drawer 닫은 후 표시

ResultGrid Row는 기존 표시 형식을 그대로 사용한다.
예시 형식: "야간수당 (12시간 × 50%가산) +61,920원"
allowanceRows 계산 결과가 기존 Row 포맷(수당명 · 시간·가산율 상세 · 금액)에 그대로 반영된다.
체크박스만 제거되고(RESULT-04), 표시 포맷 자체는 변경 없음.

---

## 9. 5인 미만 사업장 처리

- isSmallBiz는 calc-engine에 전달하지 않는다.
- mapEntriesToCalcInput() 또는 직전 변환 계층에서 처리한다.
- 5인 미만 ON 시 연장·야간·휴일 가산분만 0 처리한다.
- 주휴·연차는 이 게이팅 대상이 아니다.

---

## 10. 기존 customPremiumRows 처리

- 기존 History의 customPremiumRows는 allowanceRows로 변환 가능해야 한다.
- 신규 저장은 allowanceRows 기준으로 한다.
- 기존 customPremiumRows를 그대로 유지하지 않는다.

---

## 구현 범위 (MVP)

| 항목 | 포함 여부 |
|------|----------|
| 가산수당 설정 버튼 / PremiumScreen 제거(흡수 후) | ✅ |
| Drawer 열기/닫기 | ✅ |
| 칩 선택/완료 | ✅ |
| 시간 입력 (스테퍼+키패드) | ✅ |
| 표준가산 안내문구 | ✅ |
| 맞춤가산 입력 (단일) | ✅ |
| 행 추가/수정/삭제 | ✅ |
| allowanceRows 저장/복원 | ✅ |
| customPremiumRows → allowanceRows 변환 | ✅ |
| mapEntriesToCalcInput() 연결 | ✅ |
| 5인 미만 가산분 게이팅 | ✅ |
| ResultGrid 기존 표시 포맷 유지 | ✅ |
| 색상/여백/애니메이션 | ❌ (UI-Audit 단계) |
| 최대 행 수 제한 | ❌ (STEP6+ 보류) |
| 시간구간 자동검사 | ❌ (STEP6+ 보류) |

---

*본 문서는 STEP6-2-5 산출물이며, 코드 수정 지시를 포함하지 않는다.*
