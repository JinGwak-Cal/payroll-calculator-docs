# UI-Audit (01. 전수조사)

- **문서 종류**: UI 전수조사 (현황 보고용 / 코드 수정 없음)
- **작성**: Replit (현업1-1)
- **기준 시각**: 2606.01
- **대상 앱**: 리플렛급여계산기 (`artifacts/salary-calculator`)
- **목표 이미지**: "새롭고 · 신선하고 · 깔끔하고 · 잘 정돈된" — UI 통일 작업의 기준점(baseline) 탐색

> 점수: 각 항목 1~5점 (5=우수). 평가 8축 = 가독성 / 일관성 / 단순성 / 신뢰성 / 현대성 / 모바일우선성 / 접근성 / 정보밀도
> 크게 보여야 할 것 = 계산 결과 금액 · 입력 숫자 / 작아도 되는 것 = 설명문 · 보조정보 · 참고문구

---

## 0. 전체 요약 (Executive Summary)

앱 전반은 "soft card + 큰 입력값" 기조로 **입력 영역의 완성도는 높지만**, 결과 영역에서 **디자인 토큰(둥근 모서리·색 의미·글자 크기 스케일)이 분산**되어 통일감이 약합니다. 특히 **가장 중요한 '최종 금액'이 시각적으로 가장 약하게(작게) 표현**되는 구조적 역전이 핵심 결함입니다.

### 발견된 3대 시스템 이슈
1. **둥근 모서리 비일관**: 최상위 카드가 `rounded-3xl`(NightPayCard·PaySimulator·CompanySizeScreen)와 `rounded-2xl`(ResultGrid·PremiumSection·ActionButtons·HistoryScreen)로 갈림.
2. **색 의미 분산**: 실수령=emerald / 가산수당=blue / 활성상태=indigo·blue 혼재 / 공제=red / 시뮬차액=green·rose / 경고=amber.
3. **타이포 위계 역전**: 메인 결과(ResultGrid) `text-base`(~16px) < 상세(NightPayCard) `text-[1.6rem]`(~25.6px) < 시뮬레이터(PaySimulator) `text-3xl`(~30px). **핵심 결과가 가장 작음.**

### 결론 (기준점/정리 후보)
- **기준점(baseline) 후보**: **NightPayCard** (라벨↔값 대비 명확, `rounded-3xl`, 큰 값) + **PaySimulator** (현대성·임팩트).
- **가장 정리 필요**: **ResultGrid** (메인 총액 약함 + 토글·입력·요약·총액 과밀 + radius/색 분산).

---

## 1. Home 입력 영역

### 1) 사용 중인 스타일
- **배경**: 화면 `bg-background`, 카드 `bg-white`, 입력 행 `bg-gray-50` → `focus-within:bg-white`
- **테두리**: 카드 `border-gray-100`, 포커스 `ring-indigo-500/20`, 빈 상태 `border-dashed`
- **모서리**: 외곽 카드 `rounded-3xl`, 입력 행 `rounded-2xl`, (이탈) PerDayInput 내부·StickyHeader 박스 `rounded-xl`
- **폰트**: 입력값 `text-xl font-black`, 라벨 `text-base/sm font-semibold`, 단위 `text-base font-semibold text-gray-400`
- **여백**: 표준 행 높이 `h-14`, 카드 `px-4 py-4`, 섹션 간 `space-y-3`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 |

### 3) 문제점
- PerDayInput 이탈: 모서리·행 높이·주말색 등이 다른 입력과 달라 "다른 컴포넌트"처럼 보임.
- StickyHeader 자체 토큰 사용 → 본문 카드와 불일치.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점**: WageInput · ModeToggle
- **정리 필요**: PerDayInput

---

## 2. 결과 카드 (ResultGrid)

### 1) 사용 중인 스타일
- **배경**: `bg-white`, 행 `bg-gray-50`, 활성 `bg-indigo-50`
- **테두리**: `border-gray-100`, `rounded-2xl / xl / lg` 혼용
- **폰트**: 총액 `text-base font-black text-gray-900`, 실수령 `text-base font-black text-emerald-600`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 |

### 3) 문제점 (핵심)
- 메인 결과가 가장 약함: 실수령/총액이 `text-base`(~16px) → 상세카드보다 작음.
- 과밀: 토글·입력·요약문·수당행·총액을 한 카드에 `py-1.5`로 욱여넣음.
- 모서리/색 분산.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점**: 부적합.
- **정리 필요**: ⭐ 앱 전체에서 1순위.

---

## 3. 주휴수당

### 1) 사용 중인 스타일
- JuhuPanel: `rounded-3xl bg-white border-gray-100 shadow-sm`, 주휴수당 값 `text-xl font-black text-emerald-700`
- JuhuSection: 주차 탭 `flex-1` 균등분할, 2색 체계(발생=파랑/미발생=회색)

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### 3) 문제점
- JuhuPanel은 emerald, JuhuSection은 blue/gray — 같은 주휴 영역인데 색 언어 다름.
- 다주차 시 탭 좁아짐.

---

## 4. 연차수당

### 1) 사용 중인 스타일
- 모드 탭: 활성 `bg-indigo-50 text-indigo-600 border-indigo-200`
- 개근 토글: 개근 `bg-blue-500` / 결근 `bg-red-400`
- 결과: valid `text-emerald-600` / unmet `text-amber-600` / zero `text-gray-500`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 |

### 3) 문제점
- 단일 컴포넌트에 5색: indigo·blue·red·emerald·amber.
- 결과 금액 `text-sm`으로 작음.

---

## 5. 야간수당

### 1) 사용 중인 스타일
- 모서리: `rounded-3xl`(외곽)
- 금액: `text-[1.6rem] font-black tracking-tight`
- 라벨: `text-sm font-semibold text-slate-500`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 |

### 3) 문제점
- slate 계열 색이 단독 사용(타 카드 gray 계열) → 미세한 색 이탈.

### 4) 기준점 후보
- ⭐ 앱 전체 기준점 1순위. slate→gray만 통일하면 표준.

---

## 6. 연장수당

### 1) 사용 중인 스타일
- 카드 패턴: `rounded-2xl border-gray-100 bg-white shadow-sm`
- 헤더: 가산액 `text-sm font-semibold text-blue-600`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 3 | 4 | 3 | 4 | 4 | 3 | 3 |

---

## 7. 휴일수당

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### 3) 문제점
- 전용 표현 부재: 야간(NightPayCard)과 달리 ResultGrid 행에 종속.

---

## 8. 저장/기록 관련 화면

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 |

---

## 9. 기타 (PaySimulator·CompanySizeScreen·StickyHeader)

### 1) 사용 중인 스타일
- PaySimulator: `bg-gradient-to-br from-indigo-600 to-indigo-700`, 결과 `text-3xl font-black text-white`
- 모서리: `rounded-3xl`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | 3 | 4 | 4 | 5 | 4 | 4 | 4 |

### 3) 문제점
- PaySimulator 결과(`text-3xl`)가 메인 결과(ResultGrid `text-base`)보다 큼 → 위계 역전.

---

## 10. 종합 — 기준점 / 정리 우선순위

### 기준점으로 삼기 좋은 UI (Top)
1. **NightPayCard** — 카드 표준 baseline (깔끔·정돈)
2. **PaySimulator** — 강조 표현 baseline (새로움·신선함)
3. **WageInput / ModeToggle** — 입력부 표준

### 가장 정리가 필요한 UI (Top)
1. **ResultGrid** — 메인 금액 약함 + 과밀 + 토큰 분산 (최우선)
2. **AnnualLeaveSection** — 단일 컴포넌트 5색
3. **PerDayInput** — 입력부 토큰 이탈
4. **JuhuSection 탭** — 색 통일 + 다주차 대응

### 통일 작업 시 우선 확정 권장 토큰
- **Radius 표준**: 최상위 카드 단일화 (현재 3xl ↔ 2xl 혼재)
- **타이포 스케일**: 최종 결과 금액 > 상세 금액 > 보조정보 순으로 위계 정상화
- **색 의미 사전**: 활성/실수령/가산/공제/경고 색을 1:1 고정

---

*본 문서는 현황 전수조사이며 코드 수정·구현 방향 확정을 포함하지 않습니다.*
