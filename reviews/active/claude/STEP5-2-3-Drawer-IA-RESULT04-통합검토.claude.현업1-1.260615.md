# STEP5-2-3 — Drawer IA + RESULT-04 정체 규명 (통합검토)

- **문서 종류**: STEP5 2-3단계 통합 검토안 — 신규 설계 아님, 현재 코드 기준 구조 설계 질문 정리
- **작성**: Claude (현업1-1 협업)
- **기준 시각**: 2606.15
- **상위 참조**: STEP5-ResultGrid-Review-01.md · Premium-재설계(01.구조확정) · manual-v14

---

## 0. 핵심 전제 — docs↔code 불일치 (필수 선행 인지)

> manual-v14는 Single/Double/Triple/Custom 4구조 완료를 기록하지만,
> 현재 코드상 PremiumScreen은 Custom 전용이며,
> SinglePremiumCard는 미사용 컴포넌트이고,
> Double/Triple/premiumType/allowanceCombo는 존재하지 않는다.
>
> 따라서 STEP5는 현재 코드 기준으로
> ResultGrid 고정3종 입력 제거 여부와
> PremiumScreen/Drawer로의 입력 책임 이전 가능성을 검토한다.

### 0-1. 현재 코드 실제 구조
| 영역 | 실제 상태 |
|---|---|
| ResultGrid | 고정3종(night/overtime/holiday) 입력+결과 혼재 (RESULT-01~05) |
| PremiumScreen → PremiumSection | CustomPremiumCard만 렌더링 — **맞춤가산(Custom) 전용** |
| SinglePremiumCard.tsx | 미사용 (import 0건) — Removing 후보 |
| Double/Triple/premiumType/allowanceCombo | 코드 내 존재하지 않음 — manual-v14 미구현 목표안 |
| "단일/이중/삼중" 표시 | CustomPremiumCard의 `getCustomLabel()` — `selectedCustomAllowances.length` 기반 라벨일 뿐, 별도 데이터구조 아님 |

### 0-2. 지금 하면 안 되는 것
- SinglePremiumCard 즉시 삭제 결정
- manual-v14 4구조가 이미 구현됐다는 가정 하의 설계
- RESULT-04/05 제거를 바로 코드 작업으로 지시

---

## 1. STEP5-2 — Drawer IA (현재 코드 기준 재구성)

### 1-1. 질문 재정의
기존 질문 "ResultGrid → Drawer가 어떻게 열리는가"는 그대로 유효하나,
**"Drawer"가 신규 컴포넌트인지, 기존 PremiumScreen의 확장인지**가 먼저 정해져야 함.

### 1-2. 두 가지 구조 후보
| 후보 | 내용 | 장단점 |
|---|---|---|
| **후보 A — PremiumScreen 확장** | 기존 "가산수당 설정" 화면(PremiumScreen)에 고정3종(night/overtime/holiday) 입력 섹션을 추가. CustomPremiumCard 패턴(칩+`getCustomLabel`)을 고정3종에도 적용 | 화면 전환(screen="premium") 기존 라우팅 재사용. §구조-2 "[연장][야간][휴일][맞춤] 조합 선택 UX 재사용"과 합치 |
| **후보 B — 신규 Drawer 컴포넌트** | ResultGrid 하단에 새로운 Bottom Sheet형 Drawer 신설, 고정3종+맞춤가산 모두 이전 | §구조-7 "상단 ResultGrid + 하단 Drawer" 원문에 더 부합. 단, 신규 컴포넌트 개발 필요 — STEP5 범위를 넘는 구현 작업 |

### 1-3. STEP5에서의 처리
구조 선택(A vs B)은 **STEP6급 구조 설계 결정**으로 분리. STEP5는 "RESULT-04/05의 입력 책임이 ResultGrid 밖으로 이전되어야 한다"는 방향성만 확정하고, 이전 대상(PremiumScreen 확장 vs 신규 Drawer)은 보류.

---

## 2. STEP5-3 — RESULT-04 정체 규명 (현재 코드 기준)

### 2-1. RESULT-04(☑/☐ 토글)의 현재 역할
`allowanceRows`(night/overtime/holiday) 각 행의 좌측 체크 — `includeNight/includeOvertime/includeHoliday`를 직접 토글. 클릭 시 Indigo 색상 사용(06§2-3 위반).

### 2-2. CustomPremiumCard 패턴과의 대조
CustomPremiumCard는 `selectedCustomAllowances`(배열) 칩 선택 + `getCustomLabel()`로 "맞춤 단일/이중/삼중가산" 라벨을 자동 생성. RESULT-04의 ☑/☐ 3개(night/overtime/holiday)를 이 칩 선택 패턴으로 교체하면, **CustomPremiumCard와 동일한 UI 패턴을 고정3종에도 적용 가능** — 단, 이는 "기존 CustomPremiumCard 컴포넌트를 고정3종용으로도 쓸 것인가, 별도 컴포넌트로 복제할 것인가"라는 구현 질문으로 이어짐(STEP6+ 구현 단계 판단).

### 2-3. STEP5 확정 가능 범위
- RESULT-04는 "단순 ON/OFF"가 아니라 "어떤 수당을 포함시킬지 선택하는 칩"으로 재정의 가능 — **방향성만 확정**
- 색상 위반(06§2-3, Indigo Selected) 수정은 RESULT-04 구조 변경과 무관하게 독립적으로 가능 — **이 부분만 즉시 확정 가능**
- "선택 개수→가산유형 자동라벨"은 manual-v14 목표안이며, 현재 CustomPremiumCard에 이미 그 로직(`getCustomLabel`)이 존재 — 고정3종에 재사용할지는 보류

---

## 3. RESULT-05 처리 (현재 코드 기준)

- 인라인 시간 스테퍼(◀◀◀▶▶▶) + 가산율 버튼(+0.5/+1.0/+1.5)
- §구조-6 "기존 인라인 펼침 입력 UI → 제거"는 **방향성 확정**, 이전 대상은 1-2 후보A/B에 의존하므로 보류
- 가산율 버튼 표기(`+0.5/+1.0/+1.5`)는 manual-v14 §G "0.5/1.0/1.5 표기 사용 금지 → 50%추가/100%추가/150%추가 통일" 위반 — **표기 수정은 구조와 무관, 즉시 확정 가능**

---

## 4. STEP5-2-3 종합

### 확정
- RESULT-04 색상(Indigo Selected) 수정 — 06§2-3 적용
- RESULT-05 가산율 표기(`+0.5` → `50%추가`) 수정 — manual-v14 §G 적용
- RESULT-05(인라인 펼침 입력 UI) → ResultGrid 밖으로 이전 방향 확정 (이전 대상은 보류)
- RESULT-04 → "포함 토글"에서 "수당 선택 칩"으로 재정의 방향 확정 (즉시 구조변경 아님)
- SinglePremiumCard → Removing 후보 (즉시 삭제 아님)

### 보류 (STEP6급)
- 이전 대상: PremiumScreen 확장(후보A) vs 신규 Drawer(후보B)
- CustomPremiumCard 패턴을 고정3종에 재사용할지 여부
- "선택개수→가산유형 자동라벨"(premiumType/allowanceCombo류) 고정3종 적용 여부
- Drawer 세부 구현 전반 (기존 문서상 의도적 보류 유지)

---

*본 문서는 STEP5 2-3단계 통합 검토안이며, 코드 수정 지시를 포함하지 않는다.*
