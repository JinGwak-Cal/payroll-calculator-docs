# UI Inventory (STEP4 산출물)

- **문서 종류**: UI 인벤토리 — STEP4 산출물 (UI-Audit 01·05·06 기반, STEP 5-B 별도 커밋 대상)
- **기준 시각**: 2606.14
- **근거 문서**:
  - UI-Audit(01. 전수조사) — 9개 영역 전수조사 원본 (재사용, 재조사 없음)
  - UI-Audit(05. 분류체계확정-검증반영) — 4축·C안·색상3층·X-5/X-6 정본
  - UI-Audit(06. 디자인언어-벤치마킹실행) — 색상3층·검증 근거
- **전제**:
  - UI-Audit(01~04) 원본 수정 없음. 본 인벤토리는 별도 산출물.
  - Interaction은 Type에 흡수 (C안, 별도 칸 없음)
  - Status는 단일값만 사용 (Default·Selected·Disabled·Loading·Error·Success)
  - ResultGrid·Premium = Lifecycle=Redesign 표시만, STEP4에서 재설계 없음
  - 디자인 변경·토큰값 결정·색상 변경·컴포넌트 통합·코드 수정 없음
- **산출 결과**:
  - Inventory 22건
  - Source Gap 4건
  - UI-Audit(01) §1~9 전수 매핑 완료, 누락 없음

---

## 1. 인벤토리 (22건)

| UI ID | 기능정의 | Type | Component | Feature | Layer | Emphasis | Status | Signature | Notes | Lifecycle |
|---|---|---|---|---|---|---|---|---|---|---|
| HOME-01 | Home 입력 영역 컨테이너 카드 | Display | Card | WorkInput | Input | Secondary | Default | 입력 영역 전체를 담는 카드 | rounded-3xl. PerDayInput·StickyHeader가 이 카드의 토큰과 불일치(01 문제점) | Built |
| HOME-02 | 시급 입력(WageInput) | Input | Input | WorkInput | Input | Primary | Default | 가장 먼저 입력하는 핵심 값 | 01 "기준점 후보" — text-xl font-black, focus 시 ring-indigo-500/20 | Built |
| HOME-03 | 근무모드 선택(ModeToggle) | Input | Toggle | WorkInput | Input | Secondary | Default | 모드 선택 | 01 "기준점 후보" | Built |
| HOME-04 | 일별 근무시간 입력(PerDayInput) | Input | Input | WorkInput | Input | Secondary | Default | 요일별 시간 입력 | 모서리(rounded-xl)·행 높이·주말색이 타 입력과 달라 "다른 컴포넌트"처럼 보임(01 "정리 필요 1순위") | Built |
| RESULT-01 | ResultGrid 컨테이너 카드 | Display | Card | Global | Result | Primary | Default | 결과 화면 전체를 담는 최상위 카드 | rounded-2xl/xl/lg 혼용(01 문제점). 다른 카드(NightPayCard 등)는 rounded-3xl — 모서리 불일치 | Redesign |
| RESULT-02 | 총급여/실수령액 금액 표시 | Display | Amount | Global | Result | Primary | Default | 앱 전체에서 가장 중요한 숫자 | 현재 text-base — 01 문제점("메인 결과가 가장 약함"), SIM-02·NightPayCard보다 작음(위계 역전) | Redesign |
| RESULT-03 | 수당 항목별 행(연장/야간/휴일 등) | Display | Card | Global | Result | Secondary | Default | 각 수당 행의 라벨+값 | bg-gray-50, py-1.5로 과밀(01 문제점). 휴일수당은 전용 카드 없이 이 행에 종속됨(01 §7, 야간수당 NightPayCard와 대비) | Redesign |
| RESULT-04 | 결과화면 내 토글(표준가산 등) | Input | Toggle | Global | Result | Secondary | Default | 토글 ON/OFF | 활성 시 bg-indigo-50 — 06 색상3층상 Accent층 사용, Result Layer에서의 Accent 적정성은 재설계 시 판단 | Redesign |
| RESULT-05 | 결과화면 내 입력 요소 | Input | Input | Global | Result | Secondary | Default | 값 직접 입력 | 결과 화면에 입력 요소 혼재 — 01 "과밀" 문제의 일부 | Redesign |
| JUHU-01 | 주휴수당 결과 표시 패널(JuhuPanel) 컨테이너 | Display | Card | WeeklyHoliday | Result | Primary | Default | 큰 금액(주휴수당 값) | rounded-3xl, 색상 emerald 계열 — 06 색상3층 적용 시 검토 대상 | Built |
| JUHU-02 | 주휴수당 금액 표시 | Display | Amount | WeeklyHoliday | Result | Primary | Default | 금액 자체의 크기·굵기 (text-xl font-black) | - | Built |
| JUHU-03 | 주차 선택 탭(발생/미발생 2색 포함) | Input | Tab | WeeklyHoliday | Input | Secondary | Default | 탭 자체 색상으로 발생/미발생 구분 (현재 blue/gray) | 다주차 시 flex-1 균등분할로 탭 좁아짐(01 문제점). JuhuPanel(emerald)과 색 체계 불일치 존재 | Built |
| ANNUAL-01 | 연차 산정모드 선택 탭 | Input | Tab | AnnualLeave | Input | Secondary | Default | 활성 모드 표시(현재 indigo) | 활성 탭에 indigo 사용 — 06 §2-3 기준 Accent층 용도와 충돌 여부 검토 대상 | Built |
| ANNUAL-02 | 개근/결근 토글 | Input | Toggle | AnnualLeave | Input | Secondary | Default | 개근/결근 상태 구분(현재 blue/red) | 개근=blue는 06 색상3층 어디에도 속하지 않음 — 정리 대상 | Built |
| ANNUAL-03 | 연차수당 결과 금액 표시 | Display | Amount | AnnualLeave | Result | Primary | Default | 금액 자체 (valid/unmet/zero 3분기) | 현재 text-sm으로 작음 — 01 문제점("결과 금액이 작음"), Emphasis=Primary와 현재 크기 간 위계 역전 | Built |
| ANNUAL-04 | 연차수당 산정조건 안내문 | Display | Note | AnnualLeave | Result | Tertiary | Default | 보조 설명 텍스트 | - | Built |
| NIGHT-01 | 야간수당 카드(NightPayCard) 컨테이너 | Display | Card | Global | Result | Primary | Default | 카드 표준 baseline(01 "기준점 후보 1순위") | rounded-3xl. 01에서 앱 전체 카드 모서리 통일 기준으로 지목됨 | Built |
| NIGHT-02 | 야간수당 금액 표시 | Display | Amount | Global | Result | Primary | Default | 큰 금액(text-[1.6rem], 라벨 대비 명확) | slate 계열 단독 사용 — 타 카드 gray 계열과 색 이탈(01 문제점) | Built |
| OT-01 | 연장수당 카드 컨테이너 | Display | Card | Global | Result | Secondary | Default | 카드 패턴(rounded-2xl, shadow-sm) | 01 정보량이 적어 다른 카드와의 모서리 비교는 RESULT-01에 이미 기록된 전체 혼재 문제의 일부로 처리 | Built |
| OT-02 | 연장수당 가산액 표시 | Display | Amount | Global | Result | Secondary | Default | 가산액 강조(text-sm, blue) | blue 색상 — 06 색상3층 어디에도 명시적으로 속하지 않음, 색 체계 검토 대상 | Built |
| SIM-01 | 시뮬레이터 결과 카드 컨테이너 | Display | Card | Simulator | Result | Primary | Default | gradient(indigo) 배경 + 큰 결과 | rounded-3xl. 06 색상3층 기준 indigo=Accent층 — 강조 카드 용도와 부합 | Built |
| SIM-02 | 시뮬레이터 결과 금액 표시 | Display | Amount | Simulator | Result | Primary | Default | 매우 큰 금액(text-3xl, white) | ResultGrid(text-base)보다 커서 위계 역전(01 문제점) — ResultGrid는 Redesign 대상이므로 이 역전은 ResultGrid 쪽에서 정리될 사안 | Built |

---

## 2. Source Gap (4건)

UI-Audit(01) 원문에 4축 부여를 위한 컴포넌트 단위 정보가 없는 영역. 미분류 큐(X-4, UI 존재+4축 미확정)와는 성격이 다름 — UI 식별 정보 자체가 부족하거나 01 작성 시점에 존재하지 않았던 영역.

| 영역 | 유형 | 사유 |
|---|---|---|
| History (저장/기록) | Source Gap | UI-Audit(01) §8에 8축 점수표만 존재, 컴포넌트 단위 기술 없음 |
| Premium (PremiumScreen) | Source Gap | UI-Audit(01, 2606.01) 작성 이후(2606.04 Phase 2-7) 신설 — 원문 작성 시점에 존재할 수 없었음 |
| CompanySizeScreen | Source Gap | UI-Audit(01) §9 제목에만 언급, 컴포넌트 단위 기술 없음 |
| StickyHeader | Source Gap | UI-Audit(01) §1에 "본문과 토큰 불일치"라는 문제만 기술, 컴포넌트 구성 정보 없음 (HOME-01 Notes에 연계) |

---

## 3. 영역별 매핑 검산 (UI-Audit(01) §1~9 전수 대응)

| 01 § | 영역 | 처리 결과 |
|---|---|---|
| §1 | Home 입력 | HOME-01~04 (4건) |
| §2 | 결과 카드(ResultGrid) | RESULT-01~05 (5건, Redesign) |
| §3 | 주휴수당 | JUHU-01~03 (3건) |
| §4 | 연차수당 | ANNUAL-01~04 (4건) |
| §5 | 야간수당 | NIGHT-01~02 (2건) |
| §6 | 연장수당 | OT-01~02 (2건) |
| §7 | 휴일수당 | RESULT-03 Notes 종속 처리 (0건, 신규 UI ID 없음) |
| §8 | 저장/기록 화면 | Source Gap |
| §9 | 기타(PaySimulator·CompanySizeScreen·StickyHeader) | SIM-01~02 (2건) + CompanySizeScreen·StickyHeader Source Gap |

**합계**: 인벤토리 22건 + Source Gap 4건. 9개 영역 전수 매핑 확인, 누락 없음.

---

## 4. 작성 과정 중 확정된 규칙 (참고용 기록)

- Status는 단일값만 사용. 계산 결과의 의미 분기(예: valid/unmet/zero)는 Status로 매핑하지 않고 Signature/Notes에 기록 (ANNUAL-03)
- Feature 전용값 없는 영역(연장/야간/휴일수당)은 Feature=Global로 처리, 새 Feature 생성 안 함 (Premium은 별개 Source Gap 항목이라 개념 혼동 방지)
- Notes는 "문제 사실 기록"까지만, 해결책·토큰값·디자인 방향 결정은 기재하지 않음
- 기존 작성 항목에 대한 사실 보강(RESULT-03 — 휴일수당 종속 정보)은 좌표·태그·설계·관리 컬럼 불변 조건 하에 1건 허용

---

## 5. STEP4 종료 메모 — RESULT-03 Component 분류 검토사항

현재 RESULT-03(수당 항목별 행)은 의미상 Row에 가까우나,
UI-Audit-05 Component 목록에 Row 값이 존재하지 않아 Card로 분류하였다.

다만 본 판단은 STEP4의 "현재 구현 기준 분류"에 따른 임시 결정이며,
STEP5 ResultGrid 재설계 방향에 따라 재검토가 필요하다.

검토 시나리오:
- 시나리오 A: ResultGrid가 "컨테이너 카드 + 반복 행" 구조를 유지하는 경우
  → Component=Row 도입 가치 존재, RESULT-03 계열을 Row로 재분류 검토
- 시나리오 B: ResultGrid가 "수당별 독립 카드" 구조로 재설계되는 경우
  → RESULT-03 자체가 분해 또는 소멸 가능, Row 도입 필요성 낮음

Row 도입 여부는 STEP4 인벤토리 단계가 아닌
STEP5 ResultGrid 재설계 방향 확정 이후 판단한다.

본 메모는 Component 체계 개정 제안이 아니라,
STEP5 ResultGrid 재설계 시 확인해야 할 설계 관찰사항이다.
