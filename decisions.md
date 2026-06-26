# 파트너 협의 결정사항

---

## D-01 앱 정책

### D-01-01 맞춤가산 정체성 — 확정 (2606031200)
- 맞춤가산 = 가산분 (법정가산의 커스텀 버전)
- 5인 미만 사업장에서 맞춤가산도 0 처리 (표준가산과 동일 게이팅)
- 맞춤가산 계산: 각 행별 hours × wage × rate 후 Math.floor() 1회, 행별 결과 합산
- 맞춤가산 저장 원칙: floor된 금액이 아닌 원본 입력값(hours/rate/선택정보) 기준으로 저장·복원. customPay는 항상 재계산되는 파생값으로만 취급

### D-01-02 맞춤가산 정체성 — 향후 확장 방향
- 위험수당/약정수당 등 별도수당 필요 발생 시 → 별도 기능으로 추가 (맞춤가산과 분리)

### D-01-03 R1 결합가산 처리 — 확정 (2606031200)
- 표준가산(연장/야간/휴일)은 0.5 고정
- 표준가산으로 표현되지 않는 특수 가산율은 맞춤가산으로 처리
- 이중/삼중은 UI상 결합 입력, 내부에서는 선택된 수당 각각 같은 시간으로 분해
- 표준가산은 각 0.5 고정 (연장+야간 = 1.0 / 연장+야간+휴일 = 1.5)
- 5인미만 ON 시 A 게이팅에 의해 자동 0 처리
- 표준가산 진실원천 = 시스템 A (실수령 반영 경로)
- B(Premium)는 계산 진실원천이 아닌 입력 UI / 제거 대상
- UI 프리셋: ResultGrid의 0.5/1.0/1.5 버튼 제거 → "표준가산 50% 고정 · 특수율은 맞춤가산 사용" 정적 안내로 대체 (커밋 a3f4e0d)

### D-01-04 R1 결합가산 처리 — floor 정책 확정
- Premium 가산 row별 최종값에 Math.floor() 1회 적용 후 합산
- 적용 범위: Premium 단일/이중/삼중/맞춤 row에만
- 기본급/주휴/연차/세금·공제는 기존 계산 방식 유지

### D-01-05 R1 결합가산 처리 — state 처리
- nightPremiumRate·overtimePremiumRate·holidayPremiumRate state 유지 (UI만 고정)
- 저장/복원 구조 무변경

### D-01-06 기존 잠복 버그 — 주의
- 맞춤가산 state를 CalcState에 편입할 때 복원부(Home :206–233)에 맞춤 키 명시 추가 필수
- 미추가 시 동일 버그 재현됨
- 수정 완료 이력: archive/decisions-retired.md 참조

---

## D-02 작업 순서

### D-02-01 재확정된 작업 순서 (2606041200)
1. 2-7 화면 분리 (저위험 — PremiumSection 무상태 구조) ✅
2. 2-8 인라인 제거 (2-7 완료 후)
3. 2-5 근무내역 단위 (고위험 — 별도 설계 보고 후 진행)
   → customPremiumRows 영속·계산·history reload 연쇄 영향
4. 2-6 조합 자동 해석 (2-5 확정 후)
   → 자동요율 vs STEP2 수동입력 우선순위 정책 결정 선행 필요

### D-02-02 근거
- PremiumSection 무상태(presentational) 구조 확인
- 2-5 모델 변경은 customPremiumRows/저장복원/계산공식/history reload 동시 영향 고위험
- 저위험 작업으로 표면 정리 후 고위험 진행

---

## D-03 워크플로우 정책

### D-03-01 중기 과제
- 중앙 Context Builder 구축
- LLM 결과 자동 검증 체계 구축

### D-03-02 토큰·GitHub 운영 정책 (통합: B-D-03-05 + B-D-03-09)
<!-- B-D-03-10 Replit 운영 규칙: decisions → absolute-rules 구조5 목차03
     "GitHub 및 토큰 운영 (§운영6+7+Replit)"에 이동+통합 완료 (T+M)
     현행 규칙 위치: absolute-rules.md 구조5-목차03 -->
- Replit Secrets에 3개 토큰 저장 완료
  → GITHUB_APP_TOKEN
  → GITHUB_DOCS_READ_TOKEN
  → GITHUB_DOCS_WRITE_TOKEN
- main 직접 푸시 금지 / PR 필수 / Jin님 승인 후 병합
- payroll-calculator-docs 수정은 Jin님 승인 및 PR 절차를 통해서만 허용
- 대화창 토큰 노출 원칙적으로 지양

### D-03-03 문서 체계 확정 (2606051200)
- Source of Truth = absolute-rules / current-step / decisions
- merged-context.md = 파생/캐시 문서 (Source of Truth 아님)
- merged-context 충돌 시 원본 문서 우선
- index.md = 안내/진입점 역할만 (Source of Truth 아님)
- manual-v14 = archive 이동 금지 / 우선순위 하향 유지
- archive/ = 과거 기록 보관용 / 현재 판단 근거 사용 금지

### D-03-04 GPT 표준 컨텍스트 확정 (2606051200)
- GPT raw/jsdelivr/blob URL 접근 반복 실패 확인
- GPT 표준 진입 방식 = merged-context.md
- merged-context.md도 URL 읽기 실패 가능성 있음
- 최후 수단 = Jin님 직접 복붙
- GitHub Actions는 GPT 읽기 문제 해결책 아님
  → 문서 동기화·검증·자동화 인프라 역할

### D-03-05 GitHub Actions 도입 근거 (2606051200)
<!-- B-D-03-11: 문서 책임 정의 → absolute-rules 구조6으로 이동 완료 (SoT=Y 유지) -->
<!-- 현행 규칙 위치: absolute-rules.md 구조6-목차01 문서 역할 정의 -->
<!-- B-D-03-08: archive 아닌 K 유지 — "왜 Actions를 도입했는가"의 결정 근거 -->
- 협업 자동화 관점에서 높은 우선순위
- 역할: merged-context 자동 생성 / index 검증 / 불일치 경고
- GPT 읽기 문제와 별개로 문서 동기화·자동화 인프라 역할
- 구축 완료 이력: archive/decisions-retired.md 참조

---

## D-04 문서 체계 개편 결정 (0612)

### D-04-01 식별자 체계 도입 이유
- 문서 개편 시 Before/After 항목 추적 불가 문제 해결
- 상태-문서-구조-목차-서브목차 형식으로 이동 경로 명확화
- 예: B-A-02-03-S01 → A-A-02-02-S03 (어디서 어디로 갔는지 즉시 파악)

### D-04-02 sot 판정 기준 도입 이유
- 통합(M) 시 흡수된 항목이 현행 규칙인지 아닌지 판단 기준 부재 문제 해결
- "형식(독립 목차)이 사라져도 내용이 현행 규칙에 존재하면 현행 유지"
- sot=y/n으로 단순화하여 파트너 간 혼선 방지

### D-04-03 복수분류 허용 이유
- 문서 개편에서 이동+통합, 이동+개정 등이 동시 발생하는 현실 반영
- 단일 분류 강제 시 정보 손실 발생 (예: T만 표기 시 통합 사실 소실)
- 최대 2개 조합, 앞=현재처리/뒤=이후처리 순서 규칙으로 혼선 방지

### D-04-04 archive 분리 이유
- 폐기/구버전 항목이 현행 문서에 남아 파트너 혼선 유발
- sot와 archive를 독립 판정하여 "이동했지만 현행 유지(sot=y, archive=n)"와
  "폐기됐지만 기록 보존(sot=n, archive=y)" 구분

### D-04-05 SoT 3문서 체계 확정 이유
- merged-context는 파생본이므로 SoT로 삼으면 원본 훼손 시 판단 기준 소실
- index는 안내 역할이므로 규칙 저장 위치로 부적합
- absolute-rules / current-step / decisions 3문서만 SoT로 확정하여 단일 진실원천 유지

---

## UI-Audit 검증 결과 확정 (2606.13)
1. 4축 체계 채택 — Type·Component·Feature·Layer
2. C안 채택 — Interaction은 Type 흡수 / Signature·Notes 독립 유지
3. 색상 3층 확정 — Brand=Blue-Gray / Accent=Indigo / Semantic=Emerald·Red·Amber
4. 제거 우선 원칙 채택 (실행 절차는 UI-Audit(05) X-6 참조)
5. 단일 주인공 원칙 — 화면당 Primary 1개
6. 콘텐츠 우선 원칙 — 장식보다 숫자·내용·결과 우선
7. 여백은 구조 — Spacing 우선, Divider·Border·Card 후순위
8. 벤치마킹 목적 재정의 — 분류체계 검증·제거기준 확보·토큰값 참조 (예쁜 UI 탐색 아님)
9. 토큰값 조사 참조원 및 우선순위 확정 — Apple HIG → Apple Wallet → Toss → KakaoBank
   · Apple Wallet은 제거우선(X-5)·단순화절차(X-6) 검증용 핵심 참조원
   (상세 근거: UI-Audit 05·06)

---

## D-05 UI 재설계 확정 (2606.15)

### D-05-01 ResultGrid 역할 재정의 — 확정 (2606.15)
- ResultGrid = 결과 표시판 + 입력 진입점
- 가산수당 영역 터치 → 하단 Drawer(Bottom Sheet) 열림
- 실수령액·총급여·기본급·주휴·공제 → 입력 진입 불가 (표시 전용)

### D-05-02 RESULT-04/05 처리 — 확정 (2606.15)
- RESULT-04: 체크박스 방식 제거 확정 / 대체 ON/OFF 방식은 STEP6+ 보류
- RESULT-05: 인라인 펼침 입력 UI 제거 확정 → Drawer로 이전

### D-05-03 Drawer 구조 — 확정 (2606.15)
- 위치: 항상 하단 고정 (Bottom Sheet)
- 칩 구성: [연장][야간][휴일][완료] 한 줄
  - 완료 전: 비선택 칩 유지 / 완료 후: 비선택 칩 제거
- 입력 흐름: 수당 선택 → 시간 입력(스테퍼+키패드) → 가산율 안내 → 즉시 결과
- 재탭 편집: 기존 값을 유지한 채 편집모드 복귀 (수정 가능 범위는 STEP6+ 확정)
- 추가 버튼: [다른 수당 추가]
- 행 철학: 행 = 근무상황 1건 (수당 총합 입력기 아님)

### D-05-04 가산수당 저장 단위 — 확정 (2606.15)
- 저장 단위: `id + selectedAllowances + premiumRate + premiumHours`
- 저장 금지: `premiumAmount / premiumType / mode / allowanceCombo` (파생값)
- 표준/맞춤 판정: `isStandard = premiumRate === selectedAllowances.length * 50`
  - 절대값 기준 금지: 동일 값이 수당 수에 따라 표준/맞춤 달라지기 때문
- 동일 수당 + 다른 rate = MVP 금지 (A안 확정)
- 맞춤가산 MVP 범위: 단일 수당만 허용

### D-05-05 mapEntriesToCalcInput() — STEP6-2-2 기준 A안 확정 (2606.15)
- 표준가산: 각 수당별 rate=0.5 고정 분배, premiumRate는 isStandard 판정용만 사용
- 맞춤가산(단일): rate = premiumRate / 100
- 시간 합산: 동일 수당 여러 행은 hours 누적 합산
- 근거: calc-engine은 조합 엔진 아님 — night/overtime/holiday 독립 계산 후 합산 구조

### D-05-06 SinglePremiumCard.tsx — 처리 방향 확정 (2606.15)
- Removing 후보 (미사용 dead component)
- 즉시 삭제 아님 — 별도 코드 작업 시 제거

### D-05-07 History 저장 구조 — 확정 (2606.18)
- allowanceRows는 HistoryEntry.inputs 내부에 추가
- HistoryEntry 최상위 필드 추가 금지
- 저장값: PremiumAllowanceEntry[] 원본 입력값만 허용
- 저장 금지: premiumAmount · premiumType · mode · allowanceCombo
- 즐겨찾기/삭제 로직과 충돌 없음
- 구현 전 타입 신설(PremiumAllowanceEntry) 및 복원 검증 함수 필요

### D-05-08 근무지합산 알고리즘 — 확정 (2606.18)
- mapEntriesToCalcInput()에서 동일 수당 hours 누적 합산 후 각 필드 분배
- 표준가산: 각 수당 필드 / 맞춤가산: customPay 필드 — 독립 합산
- 5인 미만 게이팅: calc-engine 내부 아님 — 변환 계층에서 isSmallBiz 참조하여 가산분 0 처리
- 5인 미만 토글 = 연장·야간·휴일 가산분만 제거 (주휴·연차 유지)
- 엔진 수정 없이 구현 가능

### D-05-09 Drawer/allowanceRows 최소구현명세 — 확정 (2606.18)
- 입력 진입점 단일화: "가산수당 설정" 버튼 제거, PremiumScreen MVP 병존 안 함, 단일 진입점=ResultGrid→Drawer
- PremiumScreen/CustomPremiumCard/usePremium은 흡수→참조 제거 확인→삭제 순서로 처리 (선삭제 금지)
- 흡수 대상: 칩 선택 토글 / rate·hours 입력 핸들러 / 완료 조건 판정 / 금액 계산 로직(floor 1회)
- 흡수 안 함: 고정 3행 visible/hidden 구조, resetCustomRows, screen="premium" 라우팅
- PremiumAllowanceEntry 타입 확정: id + selectedAllowances + premiumRate + premiumHours
- isStandard는 저장하지 않고 계산 시 파생 (판정식: premiumRate === selectedAllowances.length * 50)
- ResultGrid Row는 기존 표시 포맷 유지 (체크박스만 제거, 표시 형식 변경 없음)
- 5인 미만 게이팅은 변환 계층에서 처리, 연장·야간·휴일 가산분만 0 처리
- 기존 History의 customPremiumRows는 allowanceRows로 변환 가능해야 하며, 신규 저장은 allowanceRows 기준

### D-05-10 premiumHours 의미 확정 — 급여기간 총 가산시간 (2606.19)
- premiumHours는 연장·야간·휴일 모두 급여기간 기준 총 가산시간으로 해석한다. 1일 기준(per-day) 값이 아니다.
- 연장은 총시간을 그대로 전달한다.
- 야간/휴일은 calc-engine 내부 구조로 인해 변환 계층에서 역산·보정 후 전달하지만, 최종 계산 결과는 입력된 총 가산시간 기준과 동일해야 한다.
- 근무일수를 곱하는 처리(nightHoursPerDay/holidayHoursPerDay류 직접 매핑)는 사용하지 않는다.
- 부동소수점으로 인한 언더슈팅(floor 1원 손실)은 변환 계층에서 극소 보정 처리한다.
- premiumHours의 의미는 입력 모드(uniform / timerange / 2×2 확장모드)에 의해 변경되지 않는다.
- 근거:
  - STEP5-4 §3-3: 입력 즉시 그 시간에 대한 금액만 표시(곱셈 언급 없음)
  - 사용자는 "이번 달 야간 몇 시간 했는지"는 알아도 내부 1일 기준 개념은 모름
  - 2×2 확장모드(요일별 다른 근무시간)에서도 총시간 입력은 모드 독립적으로 동일 작동
  - 입력값의 정확성=사용자 책임 / 계산의 정확성=앱 책임, 단 앱은 입력 의미를 정확히 안내할 책임이 있음
- 변환 계층(custom-premium.ts/use-calc.tsx)에서만 처리, calc-engine.ts(calculate) 미수정 원칙 유지
- Drawer 시간 입력 단계에 안내문구 표시: "가산시간은 급여기간 전체 기준으로 입력합니다. (1일 기준이 아닙니다.)"

### D-05-11 timerange 모드 야간 우선순위 확정 (2606.19)
- timerange(출퇴근시간) 모드에서도 allowanceRows에 야간 입력이 있으면, 엔진의 자동 야간 산출값보다 Drawer 입력을 우선 반영한다(A안).
- 근거: allowanceRows 활성 시 Drawer 입력이 SoT — 사용자의 명시적 의사가 엔진의 자동 추정보다 우선해야 한다는 원칙(D-05-10)에 따름.
- 구현: 변환 계층에서 inputMode를 "direct"로 전환해 엔진의 timerange 자동 야간 분기를 우회. 기본급/주휴/연차 등 base 계산에는 영향 없음(duration이 이미 hoursPerDay에 반영되어 패턴 동일).
- calc-engine.ts(calculate) 미수정 원칙 유지.

### D-05-12 STEP6-2 구현 완료 (2606.19)

* 가산수당 입력 체계(Drawer/allowanceRows) 구현 완료, 1/5~5/5 전 단계 검증 통과
* calc-engine.ts(calculate)는 구현 기간 전체 동안 미수정 유지
* 변환 계층(custom-premium.ts / use-calc.tsx)에서만 처리 원칙 유지
* dead component 정리 완료:
  PremiumScreen / PremiumSection / CustomPremiumCard 삭제, usePremium 훅 제거
* use-premium.tsx는 공용 타입 모듈로 축소 유지
  (AllowanceType / CustomPremiumRow / PremiumAllowanceEntry / initialCustomPremiumRows)
* History 저장/복원 연결 완료
* legacy customPremiumRows 기록은 allowanceRows로 변환 후 정상 복원
* SinglePremiumCard / DoublePremiumCard / TriplePremiumCard는 범위 외로 유지
* 후속 보류 이슈: use-calc.tsx Fast Refresh 비호환 — dev HMR 중 일시적 null context 오류 가능. 프로덜션 영향 없음. 필요 시 별도 리팩토링 task로 분리.

### D-05-13 토큰 절약 검토 절차 확정 (2606.22)

* 문서 작업, Replit Agent 프롬프트 작성, 대형 파일 작업(권장 기준: 300줄 이상 또는 20KB 이상), 신규 프로세스 설계 시 반드시 토큰 절약 검토를 수행한다.

* 토큰 절약 검토는 실제 작업 전에 수행하며, 작업 완료 후 사후 설명으로 대체할 수 없다.

* 프롬프트 수정 시에는 R17을 적용하며, 승인 대기 중인 프롬프트는 변경분만 제시한다.

* 작업 전 검토 형식:

  [토큰 절약 검토]

  1-1 검토유무:
  1-2 검토방법:
  1-3 예상 성과:
  - 작업 전 예상 전달량: (파일명, 줄 수)
  - 적용 방식: (append/변경분 삽입/구간 지정 등)
  - 예상 절감: (줄 수 또는 파일 수)

* 작업 완료 후 보고 형식:

  [토큰 절약 결과]

  * 실제 전달량: (줄 수)
  * 실제 절감: (줄 수)

* 일반 질의응답에는 적용하지 않는다.

* 토큰 절약 검토 결과가 없으면 문서 작업 프롬프트 승인 금지.

### D-05-14 Replit Agent 협업 재발방지 원칙 (2606.25)

* 작업환경 모델 고정
  · Replit Agent 환경에서 Shell/bash/git clone 직접 실행 제안 금지
  · 확정된 협업 구조(Claude=설계, Agent=실행) 임의 변경 금지
  · 작업환경 모델을 잃었을 때 즉시 merged-context 재확인

* 최소 정보 요청 원칙
  · 파일명 → 경로 → 구간 → tar.gz → 전체 순서 준수
  · 단계 건너뛰기 금지 / 전체 파일 출력은 최후수단

* Replit Agent 실패 종료 규칙
  · 모든 조회 프롬프트에 실패 종료 조건 포함
  · "30초 내 응답 없으면 '실패'만 출력"
  · "파일이 없으면 '파일 없음'만 출력"

* 구현 단계 진실원천 우선순위
  · Replit 워킹트리 > GitHub
  · 원인 추측 전 워킹트리 코드 확인

* 설계 범위 확대 금지
  · 현재 STEP 범위만 구현
  · 새 UI/컴포넌트/구조 추가는 다음 STEP으로 분리

* 승인 판정 규칙
  · 첫 줄에 반드시 판정 명시: 승인 / 조건부 승인 / 보완 필요 / 반려
  · 조건부 승인 시 첫 줄에 반드시 "조건부 승인"으로 시작 (승인으로 시작 후 조건 붙이기 금지)
  · "좋습니다. 다만..." 형식 금지

* 추측보다 검증 우선
  · 최종 판정은 실제 build/tsc/lint 결과 기준

* 복붙 우선 원칙
  · 사용자가 "변경분만"을 요구하지 않는 이상, 수정사항이 반영된 복붙 가능한 최종본을 먼저 제시하고, 변경 설명은 그 다음에 제시한다.

* 대기 규칙
  · 대기 등록 후 사용자 지시 전까지 새 제안 시작 금지
  · 공식 문서 반영 전이라도 즉시 준수

* 기존 컴포넌트 재사용 전 확인 규칙
  · 기존 컴포넌트/훅/유트 재사용 가능 여부를 먼저 조사
  · import 확인 → 중첩 확인 → 구현 순서 준수

* 협업 자세 원칙
  · 사용자의 토큰 비용, 클릭 수, 복붙 횟수를 실제 작업 비용으로 간주
  · AI가 편한 방식보다 사용자의 작업환경에서 덝 번거로운 방식을 우선
  · 프롬프트 초안은 한 번에 실행 가능한 품질을 목표로 작성
  · 사용자가 뻔히 요구할 보완은 선제 반영
  · 같은 유형의 실수를 반복하지 않도록 체크리스트를 재점검

* 토큰 비용 안내
  · 토큰 소모량이 불필요한 경우를 제외하고, 질문 또는 제안 시 예상 토큰 소모량을 함께 언급

* Replit 프롬프트 작성 체크리스트
  · 범위 최소화 / 하위 경로 명시 / 출력 형식 지정 / 출력 금지 명시
  · 수정 금지 명시 / 실패 종료 조건 포함 / 토큰 절약 순서 준수
  · 현재 STEP 범위 확인 / 기존 컴포넌트/훅/유트 재사용 여부 조사
  · import 중복·중첩 확인 / 복붙 가능한 최종본 제시 / 첫 줄 판정 명시

### D-05-15 수당근무 내역 UX 최종 확정안 (2606.25)

* 2줄 표준 형식 (공통 UI 규격)
  · 1줄: 번호(displayNo) + 메몤 (식별자, 고정)
  · 2줄: 입력 시각(createdAt) · 적용수당 · 가산율
  · 목록 / 선택 Sheet / 비교편집 / 요약 카드 모두 동일 형식 적용
  · 예시

    #01  토요일 특근
    06-25 14:30 · 연장·야간 · 150%

* 삭제 Placeholder 확정
  · 기본: ▶ #02
  · 클릭: ▼ #02 (이용자 삭제)
  · 재클릭: ▶ #02
  · 번호 재정렯 없음. 설명/시각/카드 없음.

* 식별자 고정 원칙
  · displayNo / 메몤 / createdAt = 수정해도 변하지 않음
  · 수정 가능한 것: 적용수당 / 가산율만

* 비교편집 UX 방향 확정
  · MVP를 먼저 구현하여 현재 STEP 범위를 유지하고, 3단 비교편집은 후속 STEP으로 분리한다.
  · MVP (저비용): Drawer 상단 기존 입력 요약 카드만 추가
    - 읽기전용 카드 1개 / 실시간 diff 없음 / 기존 Drawer 구조 유지
  · 풀 구현 (후순위): 3단 비교편집 구조
    - 기존 입력 / 수정 입력 / 예상 수정 실시간 동기화
    - 구현 비용: AllowanceDrawer 150~200줄 영향 / state 3~5개 추가
    - STEP 5 이후로 보류

* 구현 원칙
  · 기존 컴포넌트 우선 재사용
  · 최소 증분 구현
  · 현재 STEP 범위를 넘는 UI 확장 금지
