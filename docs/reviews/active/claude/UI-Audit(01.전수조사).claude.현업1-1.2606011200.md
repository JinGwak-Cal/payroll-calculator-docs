# UI-Audit (01. 전수조사)

- **문서 종류**: UI 전수조사 (현황 보고용 / 코드 수정 없음)
- **작성**: Claude (현업1-1)
- **기준 시각**: 2606.01 12:00
- **대상 앱**: 리플렛급여계산기 (`artifacts/salary-calculator`)
- **목표 이미지**: "새롭고 · 신선하고 · 깔끔하고 · 잘 정돈된" — UI 통일 작업의 기준점(baseline) 탐색

> 점수: 각 항목 1~5점 (5=우수). 평가 8축 = 가독성 / 일관성 / 단순성 / 신뢰성 / 현대성 / 모바일우선성 / 접근성 / 정보밀도
> 크게 보여야 할 것 = 계산 결과 금액 · 입력 숫자 / 작아도 되는 것 = 설명문 · 보조정보 · 참고문구

---

## 0. 전체 요약 (Executive Summary)

앱 전반은 "soft card + 큰 입력값" 기조로 **입력 영역의 완성도는 높지만**, 결과 영역에서 **디자인 토큰(둥근 모서리·색 의미·글자 크기 스케일)이 분산**되어 통일감이 약합니다. 특히 **가장 중요한 '최종 금액'이 시각적으로 가장 약하게(작게) 표현**되는 구조적 역전이 핵심 결함입니다.

### 발견된 3대 시스템 이슈
1. **둥근 모서리 비일관**: 최상위 카드가 `rounded-3xl`(NightPayCard·PaySimulator·CompanySizeScreen)와 `rounded-2xl`(ResultGrid·PremiumSection·ActionButtons·HistoryScreen)로 갈림.
2. **색 의미 분산**: 실수령=emerald / 가산수당=blue / 활성상태=indigo·blue 혼재 / 공제=red / 시뮬차액=green·rose / 경고=amber. 동일 의미(활성)에 다른 색.
3. **타이포 위계 역전**: 메인 결과(ResultGrid) `text-base`(~16px) < 상세(NightPayCard) `text-[1.6rem]`(~25.6px) < 시뮬레이터(PaySimulator) `text-3xl`(~30px). **핵심 결과가 가장 작음.**

### 결론 (기준점/정리 후보)
- **기준점(baseline) 후보**: **NightPayCard** (라벨↔값 대비 명확, `rounded-3xl`, 큰 값) + **PaySimulator** (현대성·임팩트).
- **가장 정리 필요**: **ResultGrid** (메인 총액 약함 + 토글·입력·요약·총액 과밀 + radius/색 분산).

---

## 1. Home 입력 영역
**대상 파일**: `Home.tsx`(레이아웃), `WageInput`, `UniformInput`, `PerDayInput`, `OptionsSection`, `ModeToggle`, `TabSelector`, `InputSummary`, `StickyHeader`

### 1) 사용 중인 스타일
- **배경**: 화면 `bg-background`, 카드 `bg-white`, 입력 행 `bg-gray-50` → `focus-within:bg-white`
- **테두리**: 카드 `border-gray-100`, 포커스 `ring-indigo-500/20`, 빈 상태 `border-dashed`
- **모서리**: 외곽 카드 `rounded-3xl`, 입력 행 `rounded-2xl`, (이탈) PerDayInput 내부·StickyHeader 박스 `rounded-xl`
- **폰트**: 입력값 `text-xl font-black`, 라벨 `text-base/sm font-semibold`, 단위(원/시간/일) `text-base font-semibold text-gray-400`
- **여백**: 표준 행 높이 `h-14`, 카드 `px-4 py-4`, 섹션 간 `space-y-3` (이탈) PerDayInput `h-12/h-10`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 |

### 3) 문제점
- **PerDayInput 이탈**: 모서리(`rounded-xl`)·행 높이(`h-12/10`)·주말색(`bg-rose-50/50`) 등이 다른 입력과 달라 "다른 컴포넌트"처럼 보임. time-range 모드의 `divide-y`와 grid 모드 혼합으로 밀도 과다.
- **StickyHeader** `gap-2.5`·`rounded-xl`·`text-[10px]` 등 자체 토큰 사용 → 본문 카드와 불일치.
- UniformInput(`bg-rose-50`) vs PerDayInput(`bg-rose-50/50`) 주말색 농도 불일치.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점**: **WageInput · ModeToggle** (`focus-within` 전환, 큰 값, 명확한 위계 — 가장 "premium").
- **정리 필요**: **PerDayInput** (밀도·토큰 이탈로 입력부 통일성을 깨는 주범).

---

## 2. 결과 카드 (ResultGrid)
**대상 파일**: `ResultGrid.tsx`

### 1) 사용 중인 스타일
- **배경**: `bg-white`, 행 `bg-gray-50`, 활성 `bg-indigo-50`
- **테두리**: `border-gray-100`, 구분선 `border-t border-gray-50`, 빈 `border-dashed`
- **모서리**: `rounded-2xl / xl / lg` 혼용
- **폰트**: 총액(gross) `text-base font-black text-gray-900`, 실수령(net) `text-base font-black text-emerald-600`, 수당 행 라벨 `text-sm font-semibold text-gray-700`, 금액 `text-sm font-black` (emerald/gray-400)
- **여백**: 컨테이너 `space-y-2`, 행 `py-1.5 px-1` (조밀)

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 |

### 3) 문제점 (핵심)
- **메인 결과가 가장 약함**: 실수령/총액이 `text-base`(~16px)에 불과 → 상세카드(NightPayCard `1.6rem`)·시뮬레이터(`text-3xl`)보다 작다. "계산 결과가 중심"이라는 신뢰성 기준에 정면 배치.
- **과밀**: 토글·입력·요약문·수당행·총액을 한 카드에 `py-1.5`로 욱여넣어 cramped.
- **모서리/색 분산**: 형제 카드가 `rounded-3xl`인데 여기만 `rounded-2xl`. 색 의미(emerald/red/indigo)가 한 카드에 혼재.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점**: 부적합.
- **정리 필요**: ⭐ **앱 전체에서 1순위 정리 대상.** 최소한 최종 금액을 `text-2xl`↑로 승격 + 여백 확대 필요.

---

## 3. 주휴수당
**대상 파일**: `JuhuPanel.tsx`(요약 카드), `JuhuSection.tsx`(주차 탭 + 결과 패널)

### 1) 사용 중인 스타일
- **JuhuPanel**: `rounded-3xl bg-white border-gray-100 shadow-sm`, 주휴수당 값 `text-xl font-black text-emerald-700`, 보조 `text-[11px] text-emerald-400`, 미충족 경고 `bg-amber-50`
- **JuhuSection**: 주차 탭 strip(`flex-1` 균등분할), 2색 체계(발생=파랑 `#3b82f6` / 미발생=회색 `#9ca3af`), per-week 토글 스위치, 결과 패널 `border-2`, 결과문구 `✔ 주휴 발생 (개근·주간 N시간)`
- **여백**: 안내 div `px-3 py-2 text-xs text-gray-500`, 패널 `p-3`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### 3) 문제점
- **두 컴포넌트 색 체계 불일치**: JuhuPanel은 emerald 기반, JuhuSection은 blue/gray 2색. 같은 "주휴" 영역인데 색 언어가 다름.
- **다주차 시 탭 좁아짐**: `flex-1` 균등분할이라 6주↑에서 탭 폭·라벨 가독성 급락(별도 감사 S-1-3 확인). 캡/스크롤 없음.
- 결과 금액 강조 약함(`text-xl`은 양호하나 패널 결과문구는 텍스트 위주).

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점 후보**: JuhuPanel 금액 카드(emerald, 큰 값)는 양호.
- **정리 필요**: JuhuSection 탭 strip(다주차 대응 + 색 통일).

---

## 4. 연차수당
**대상 파일**: `AnnualLeaveSection.tsx`

### 1) 사용 중인 스타일
- **모드 탭**: `매월 발생/퇴사 정산` — 활성 `bg-indigo-50 text-indigo-600 border-indigo-200`
- **개근 토글**: 개근 `bg-blue-500 text-white` / 결근 `bg-red-400 text-white`
- **입력**: `rounded-lg border-gray-200 bg-white text-sm`
- **결과**: valid `text-sm font-bold text-emerald-600` / unmet `text-amber-600` / zero `text-gray-500`
- **참고문구**: `text-[11px] text-gray-400`
- **모서리**: `rounded-xl / lg` 혼용

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 |

### 3) 문제점
- **단일 컴포넌트에 5색**: indigo(모드)·blue(개근)·red(결근)·emerald(결과)·amber(경고). 색 과다로 시선 분산 → 일관성 최저.
- 개근 토글 색(blue/red)이 JuhuSection의 발생/미발생 색 언어와도 다름.
- 결과 금액 `text-sm`로 작음(접근성: 중년 사용자에 불리).

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점**: 부적합.
- **정리 필요**: 색 팔레트 축소 + 결과 금액 승격 대상.

---

## 5. 야간수당
**대상 파일**: `NightPayCard.tsx` (+ ResultGrid 수당행)

### 1) 사용 중인 스타일
- **모서리**: `rounded-3xl`(외곽), `rounded-2xl/xl`(내부)
- **배경**: `bg-white`, 데이터부 `bg-slate-50`
- **금액**: `text-[1.6rem] font-black tracking-tight` (앱 내 상세 중 최대급)
- **라벨**: `text-sm font-semibold text-slate-500`, 강조색 `text-indigo-500`
- **구조**: `grid-cols-2` "card-within-a-card"

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 |

### 3) 문제점
- **slate 계열 색이 단독 사용**(타 카드 gray 계열) → 미세한 색 이탈.
- 그 외 구조·위계는 모범적.

### 4) 기준점 후보 / 5) 정리 필요 후보
- ⭐ **앱 전체 기준점(baseline) 1순위.** 라벨↔값 대비, 큰 금액, `rounded-3xl`, 그리드 정렬이 목표 이미지("깔끔·정돈")에 가장 부합. slate→gray만 통일하면 표준.

---

## 6. 연장수당
**대상 파일**: `PremiumSection.tsx`, `Single/Double/Triple/CustomPremiumCard.tsx`, `PremiumRateCard.tsx` (+ ResultGrid 수당행)

### 1) 사용 중인 스타일
- **카드 패턴**: `rounded-2xl border-gray-100 bg-white shadow-sm` (일관)
- **헤더**: 제목 `text-sm font-medium text-gray-800`, 가산액 `text-sm font-semibold text-blue-600`
- **여백**: 헤더 `px-4 py-3`, 내용 `px-4 pb-4`
- **PremiumRateCard**: 비율 버튼 `rounded-xl border text-base font-black`, 활성 `ring-2 ring-indigo-500/20`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 3 | 4 | 3 | 4 | 4 | 3 | 3 |

### 3) 문제점
- **활성 색 이탈**: PremiumRateCard는 indigo ring, 나머지 Premium 카드는 blue → 활성 의미색 불일치.
- 가산 금액이 `text-sm`로 작음(신뢰성/접근성).
- Premium 카드들끼리는 일관성 양호(앱 내 모듈 일관성 모범 사례).

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점 후보**: PremiumCard 군의 통일된 카드 패턴(모듈 일관성)은 참고할 만함.
- **정리 필요**: PremiumRateCard 활성색(indigo→blue 통일) + 금액 크기.

---

## 7. 휴일수당
**대상**: `ResultGrid.tsx` 수당행 + Premium 가산 경로

### 1) 사용 중인 스타일
- 독립 카드 없음. ResultGrid 수당행으로만 표현: 라벨 `text-sm font-semibold text-gray-700`, 금액 `text-sm font-black` (emerald/gray-400), 행 `py-1.5`
- 가산 입력은 Premium 카드 경로 공유

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### 3) 문제점
- **전용 표현 부재**: 야간(NightPayCard)과 달리 휴일수당은 ResultGrid 행에 종속 → 위계가 낮고, 사용자 인지 약함.
- ResultGrid의 과밀/작은 금액 문제를 그대로 상속.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점**: 없음(전용 UI 없음).
- **정리 필요**: 야간수당 카드와 동급의 표현 일관성 검토 대상.

---

## 8. 저장/기록 관련 화면
**대상 파일**: `HistoryScreen.tsx`, `ActionButtons.tsx`

### 1) 사용 중인 스타일
- **ActionButtons**: `rounded-2xl`, `bg-indigo-50`/`bg-amber-50`, 텍스트 `text-sm/xs font-bold` (indigo/amber/gray)
- **HistoryScreen**: `rounded-2xl` 카드 기반 리스트

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 |

### 3) 문제점
- 기능 영역으로서 일관성 양호. 다만 `rounded-2xl`로 통일돼 있어, 앱 표준을 `rounded-3xl`로 잡을 경우 함께 조정 필요.
- amber/indigo 액션색이 다른 영역의 의미색과 충돌하지 않도록 정리 권장.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점 후보**: 보조 영역 일관성은 무난.
- **정리 필요**: 표준 radius 확정 시 동반 조정.

---

## 9. 기타 사용자 노출 UI
**대상 파일**: `PaySimulator.tsx`, `CompanySizeScreen.tsx`, `StickyHeader.tsx`

### 1) 사용 중인 스타일
- **PaySimulator**: `bg-gradient-to-br from-indigo-600 to-indigo-700`, 결과 `text-3xl font-black text-white`(앱 내 최대), 차액 `text-green-300/text-rose-300`, 슬라이더 `accent-indigo-500`, `rounded-3xl`
- **CompanySizeScreen**: `rounded-3xl`
- **StickyHeader**: `bg-gray-100` 바, 항목 `bg-white rounded-xl`, 값 `text-base font-black`

### 2) 8축 점수
| 가독성 | 일관성 | 단순성 | 신뢰성 | 현대성 | 모바일 | 접근성 | 정보밀도 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | 3 | 4 | 4 | 5 | 4 | 4 | 4 |

### 3) 문제점
- **위계 역전 주범**: PaySimulator 결과(`text-3xl`)가 메인 결과(ResultGrid `text-base`)보다 크다 → 보조 화면이 본 화면보다 강조됨.
- gradient·차액색(green/rose)이 앱 표준 팔레트와 별개로 작동.

### 4) 기준점 후보 / 5) 정리 필요 후보
- **기준점 후보(현대성)**: ⭐ **PaySimulator** — "새롭고 신선한" 목표 이미지에 가장 부합. 다만 위계는 메인 결과를 넘지 않도록 조정 전제.
- **정리 필요**: StickyHeader 토큰(radius/gap)을 앱 표준에 맞추기.

---

## 10. 종합 — 기준점 / 정리 우선순위

### 가장 기준점으로 삼기 좋은 UI (Top)
1. **NightPayCard** — 구조·위계·여백의 모범 (깔끔·정돈). → **카드 표준 baseline**
2. **PaySimulator** — 현대성·임팩트 (새로움·신선함). → **강조 표현 baseline**
3. **WageInput / ModeToggle** — 입력부 표준.

### 가장 정리가 필요한 UI (Top)
1. **ResultGrid** — 메인 금액 약함 + 과밀 + 토큰 분산 (최우선).
2. **AnnualLeaveSection** — 단일 컴포넌트 5색, 색 언어 정리.
3. **PerDayInput** — 입력부 토큰 이탈.
4. **JuhuSection 탭** — 색 통일 + 다주차 대응.

### 통일 작업 시 우선 확정 권장 토큰 (관찰 기반, 제안 아님 / 결정 보류)
- **Radius 표준**: 최상위 카드 단일화 (현재 3xl ↔ 2xl 혼재).
- **타이포 스케일**: 최종 결과 금액 > 상세 금액 > 보조정보 순으로 **위계 정상화** (현재 역전).
- **색 의미 사전**: 활성/실수령/가산/공제/경고 색을 1:1 고정 (현재 indigo·blue·emerald·red·amber 혼선).

---

*본 문서는 현황 전수조사이며 코드 수정·구현 방향 확정을 포함하지 않습니다.*
