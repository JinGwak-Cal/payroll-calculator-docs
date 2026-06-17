# STEP5 — ResultGrid 재설계 검토안 (기존 확정안 재연결본)

- **문서 종류**: STEP5 1차 검토안 — 신규 설계 아님, 기존 확정안 재연결
- **작성**: Claude (현업1-1 협업)
- **기준 시각**: 2606.15
- **상위 참조**: Premium-재설계(01.구조확정) · manual-v14 §1.4.2 · UI-Inventory-STEP4-22건 · UI-Audit-05/06

> ⚠ **본 문서는 신규 설계가 아니다.**
> Premium-재설계(01.구조확정) + manual-v14의 기존 확정 구조를 STEP5(ResultGrid 재설계)에
> 재연결한 문서이며, 새 구조·새 정식 용어를 도입하지 않는다.

---

## 0. 용어 정리

### 0-1. 통칭(비공식 별칭)
**"가산 입력 브릿지"** (통칭)
= §구조-2(입력기 역할 분리) + §구조-3(조합 자동 해석)을 묶어 부르는 실무용 별칭.
정식 변수명·구조를 대체하지 않는다.

### 0-2. 폐기 명칭
"제수당 브릿지 레이어(Allowance Bridge Layer)"는 **명칭만 폐기**한다.
개념 자체는 §구조-2/§구조-3으로 흡수되어 유지된다.

### 0-3. 정식 용어 (manual-v14 §1.4.2 기준, 변경 없음)
| UI문구 | 내부변수 | 설명용어 |
|---|---|---|
| 단일가산/이중가산/삼중가산/맞춤가산 | `premiumType` | 가산유형 |
| 연장/야간/휴일 | `selectedSingleAllowance` | 단일가산 선택수당 |
| 연장/야간/휴일(복수) | `selectedCustomAllowances` | 맞춤가산 선택수당 |
| 연장+야간/야간+휴일/연장+휴일 | `allowanceCombo` | 수당조합 |

---

## 1. STEP4 인벤토리 대조 결과 (RESULT-01~05)

| 항목 | 1차 판단 | 기존 확정안 대조 | 최종 |
|---|---|---|---|
| RESULT-01 컨테이너 | `rounded-2xl`→`rounded-3xl` 통일 후보 (Home 입력카드·안내박스와 정합) | 충돌 없음 | **확정 후보 유지** |
| RESULT-02 실수령액 | ResultGrid 내부 Primary 위계 강화 필요 (`text-base` vs `text-sm` 격차 미미) | 충돌 없음 | **확정 후보 유지** |
| RESULT-03 수당 행 | Row 구조 정식화 타당, `Component=Row` 신규값은 UI-Audit-05 개정 이슈 | 충돌 없음 | **확정 후보 유지** (Row 신규값은 별도 개정 항목으로 표기) |
| RESULT-04 토글(☑/☐) | Indigo Selected 색상 06§2-3 위반 — 제거/이동 검토 | Premium-재설계(01) §구조-6: "체크박스 역할 → **재검토 예정**" (의도적 보류 항목) | **즉시 제거 확정 금지 — 보류 유지** |
| RESULT-05 인라인 펼침 입력(시간/배율) | PremiumScreen 이동 검토 | Premium-재설계(01) §구조-6: "기존 인라인 펼침 입력 UI → **제거**" (이미 확정) | **제거 확정** |
| NightPayCard | Removing 후보 (미사용 dead component) | 무관 (Premium 구조와 별개) | Removing 후보 유지 |
| 시나리오 | A (컨테이너+반복Row 유지) | §구조-6: "ResultGrid는 결과 표시판이자 입력 진입점" — Row 구조 자체는 유지, 입력 책임만 분리 | **A 확정** |

---

## 2. ResultGrid 역할 재정의 (§구조-6/6-1 적용)

- ResultGrid = **결과 표시판 + 입력 진입점**
- 가산수당 영역 터치 → 입력기(하단 입력 Drawer) 열림
- 실수령액/총급여/기본급/주휴수당/연차수당/공제 → 입력 진입 불가 (결과 표시 전용)
- 세부 행 구분(어떤 행이 진입 가능한지)은 §구조-6-1에 따라 "실태조사 후 최종 확정" — STEP5에서 단정하지 않음

---

## 3. 입력 책임 이전 — 하단 입력 Drawer (§구조-7)

- 상단: ResultGrid (결과 + 진입점)
- 하단: 입력 Drawer (칩 + 시간 입력 + 내역 목록) — §구조-4/5/5-1 형식
- RESULT-05(시간/배율 인라인 입력)는 이 Drawer로 입력 책임 이전 — **이전 방향만 확정**
- **Drawer 세부 구현은 기존 문서상 의도적 보류 항목 — STEP5에서 확정하지 않음**

### 4종 매핑표 (코드 레벨 검증 결과, §구조-2와 합치)
| 분류 | 항목 | 내부 변환(state, use-calc) | calculate 입력 | 비고 |
|---|---|---|---|---|
| 단일가산 대상 | 연장 | `includeOvertime`, `overtimeHoursManual`, `overtimePremiumRate` | 동일 필드 → `overtimePay/overtimeHours` | §구조-2: "선택 결과는 A state로 전달" |
| 단일가산 대상 | 야간 | `includeNight`, `nightHoursPerDay`, `nightPremiumRate` | 동일 필드 → `nightPay/nightHours` | 〃 |
| 단일가산 대상 | 휴일 | `includeHoliday`, `holidayHoursPerDay`, `holidayPremiumRate` | 동일 필드 → `holidayPay/holidayHours` | 〃 |
| 맞춤가산 | customPremiumRows | `selectedCustomAllowances`(게이트)+`premiumRate`+`premiumHours`+`isCustomRowCompleted` | `customPremiumTotal()` → `grossPay` | 화면표시(use-premium.tsx)와 총급여반영(custom-premium.ts) 계산식 동일 확인됨 |

**검증 결론**: 엔진(`calculate()`) 변경 불필요. §구조-2/3의 "선택 결과는 기존 A state로 전달"이 코드 레벨에서 그대로 성립함.

---

## 4. 06 벤치마킹 재연결 (신규 조사 불필요)

manual-v14 §1.4.2 "[F. 맞춤가산]" 구간의 "칩 선택 → 가산유형 자동 해석(단일/이중/삼중)" 패턴은
UI-Audit-06 §4의 **"5. 네이버 임금계산기 — 도메인 매핑 참조"** 항목과 동일 패턴
(사용자 체크 → 내부 공제코드/가산유형 변환).
→ 별도 신규 벤치마킹 불필요, 06 §4 기존 항목 인용으로 충분.

---

## 5. STEP5 확정/보류 종합

### 확정
- 시나리오 A (컨테이너+반복Row 구조 유지)
- RESULT-01: `rounded-3xl` 통일 후보
- RESULT-02: 내부 Primary 위계 강화 필요
- RESULT-03: Row 구조 정식화 (Component=Row 신규값은 UI-Audit-05 개정 항목으로 별도 처리)
- RESULT-05: 제거 확정 (§구조-6 기존 확정사항)
- ResultGrid 역할: 결과 표시판 + 입력 진입점 (§구조-6/6-1)
- "가산 입력 브릿지"는 통칭으로만 사용, 정식 변수명은 premiumType/allowanceCombo/selectedSingleAllowance/selectedCustomAllowances 사용
- NightPayCard: Removing 후보

### 보류
- RESULT-04 (토글 ☑/☐): 즉시 제거 확정 금지 — "재검토 예정"(보류) 유지
- 입력 Drawer 세부 구현 (§구조-7/8): 의도적 보류 항목, STEP5에서 확정하지 않음
- ResultGrid 세부 행 구분(어떤 행이 입력 진입 가능한지): §구조-6-1, "실태조사 후 최종 확정"
- PremiumScreen 재구성의 구체 레이아웃: STEP6+ 검토

---

*본 문서는 STEP5 1차 검토안이며, 코드 수정 지시를 포함하지 않는다.*
