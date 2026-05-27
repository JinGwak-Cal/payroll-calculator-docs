<!-- Auto-generated at 2026-05-27T15:47:21Z -->

# absolute-rules

# 절대 규칙
- v13.2 기준 고정
- 재정의 금지
- 없는 부분만 추가 허용
- 전체 재작성 금지
- 증분 코드만 출력
- 캘디게 구조 변경 금지
- 계산은 항상 수행 / 표시만 제어
- premiumAmount state 저장 금지
- 입력은 state / 결과는 useMemo 원칙 유지

# 작업 시작 프로토콜 (모든 AI 파트너 공통 강제)
작업 시작 전 반드시 index.md 실제 읽기 실행
확보 상태 표시 후에만 작업 가능:

[작업 시작 상태]
index.md       □ 미확보 / ■ 확보
current-step   □ 미확보 / ■ 확보
decisions      □ 미확보 / ■ 확보
absolute-rules □ 미확보 / ■ 확보

하나라도 미확보 시:
- 현재 STEP 추정 금지
- 구조 판단 금지
- 코드 생성 금지
- 읽기 실행 후 재시작

# 작업 시작 지시 정의
작업 시작 지시란 다음을 의미한다:
- 특정 STEP/G/P/BUG/UX 항목을 진행/검토/구현하라는 지시
- Codex/Claude/Agent 전달문 작성 요구
- "이어서 작업하자" 류의 지시

작업 시작 지시 시 순서:
1. index.md 실제 읽기
2. reviews/active/ 관련 파일 존재 확인
3. 있으면 읽고 반영
4. 없으면 "active review 없음" 보고 후 진행

일반 질문(개념/비용/가능성)은 작업 시작 지시 아님
→ reviews/active 자동 참조 불필요

# AI 협업 구조
Claude 검토 저장: docs/reviews/active/claude/
GPT 검토 저장: docs/reviews/active/gpt/
완료 작업 이동: docs/reviews/completed/

index.md에는 reviews 전문 미포함
reviews는 필요 시 bash_tool로 직접 참조


# current-step

# 현재 작업 단계
STEP 5 완료 ✅
§19-B-1 완료 ✅
UX-02-5 shimmer 완료 ✅

다음: 대기 G (G-1~G-8) 처리

[대기 G 목록]
G-1: 섹션 안내영역 + STEP2 입력창 shimmer 이후 동시 강조 신호 
G-2: STEP3 금액 문구 능동 반영 "[수당]수당으로 총급여에 추가됩니다"
G-3: 선택 후 닫힘 상태 수당유형 미반영 버그 수정
G-4: 선택 전 닫힘 보조 문구 정책 결정
G-5: 섹션 안내영역 "총 근무시간 [N시간]" 동적 반영
G-6: 가산 금액 총급여 실제 반영 여부 검증
G-7: "세전 표시용·실수령에는 반영 안됨" 문구 정책 확인
G-8: [심각 고민 중] 라벨 체계 뒤집기 검토

# decisions

# 파트너 협의 결정사항

# manual-v14

PAYROLL CALCULATOR
운영매뉴얼 · 인수인계리스트 · 작업리스트
v13.2 통합본
2026-05-18 업데이트 (v13.1 + 대기 A~F + §19 shimmer 보강)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

★ 새 쓰레드 첫 메시지 복붙용
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
이어서 작업하자!
반드시 첨부된 v13.2 매뉴얼만 기준으로 작업하라.
직전 쓰레드는 막히는 경우에만 참조.

[절대 규칙]
- v13.2 기준 고정
- 재정의 금지
- 없는 부분만 추가 허용
- 전체 재작성 금지
- 증분 코드만 출력
- 캘디게 구조 변경 금지
- trigger-gate 관련 로직 금지
- 계산은 항상 수행 / 표시만 제어
- premiumAmount state 저장 금지
- 입력은 state / 결과는 useMemo 원칙 유지
- 현재 STEP 범위 외 구조 변경 금지
  (§1.6-4 연계 / 제안도 포함)

[주의]
- glow UX는 현재 보류 상태
- shimmer UX만 진행
- glow 관련 확장/보완/튜닝 금지
- shimmer 대상은 §19 K 기준만 사용

[현재 단계]
STEP 3 완료.
STEP 3-F usePremium hook 추출 완료. ✅
STEP 3-G adjustedGrossPay 연결 완료. ✅
STEP 4 저장 연동 완료. ✅
STEP 5 추가버튼 / 초기화 정교화 진입.
STEP 5-1 완료. ✅
STEP 5-2 완료. ✅

[현재 상태 요약]
- 캘디게 (Calculation Display Gate) 구현 및 검증 완료
- trigger-gate 완전 폐기
- 계산: 항상 실행 / 표시: hasCalculatedOnce 조건부 제어
- 제수당 구조 B 확정 / §6 신규 명문화
- 글로벌 전략 §17 신규 추가
- 저장기록 + 기록보기 설계 §18 신규 추가
- §19 가산율 기반 제수당 UI 설계 완료
- §1.4.2 한·영 병기 용어 3구분 도표 완성
- derived value 원칙 확정 / 변수명 전체 확정
- STEP 1 골조 구현 완료
- STEP 2 상태 연결 완료
- STEP 3 derived value 연결 완료
- §1.6-4 / §1.11 / §1.12 신규 추가 (v13.0)
- §1.13 구조 설계 원칙 신규 추가 (v13.1)
- usePremium hook 설계 확정 (v13.0)
- STEP 3-F usePremium hook 추출 완료 (v13.1)
  3-F-1: use-premium.tsx shell + 타입 ✅
  3-F-2: expanded + single 이동 ✅
  3-F-3: double/triple 이동 ✅
  3-F-4: custom 이동 + escape hatch 제거 ✅
  3-F-5: 모든 derived 이동 ✅
  3-F-6: Home 연결 + PremiumSection presentation화 ✅
         adjustedGrossPay 정의 완료
         premium state lifecycle → Home으로 이동 (의도된 결과)
- STEP 3-G adjustedGrossPay 연결 완료 (v13.1)
  3-G-1: UI 표시 연결 ("가산 포함 총액" 카드) ✅
  3-G-2: 저장 payload 연결 (HistoryEntry.adjustedGrossPay optional 추가) ✅
  3-G-3: HistoryScreen 표시 연결 (adjustedGrossPay ?? mainPay) ✅
  3-G-4: 세금 계산 정책 검토 → A 확정 (현재 유지) ✅
         result.grossPay / netPay: calc-engine 기준 의미 보존
         adjustedGrossPay: UI 표시 + 저장 payload 전용
         premium은 세금 계산·실수령에 미반영

[현재 최우선 작업]
STEP 4 — 저장 연동
  4-1: 저장 구조 일관성 검증 (§18 기준) ✅ 수정 불필요
  4-2: usePremium domain boundary audit ✅ 구조 안정 확인
  4-3: adjustedGrossPay 단일 참조 정리 ✅ Home.tsx inline 중복 제거
  4-4: share 메시지 premium 조건부 표시 ✅ 가산 포함 총액 보조 줄 추가
  4-5: HistoryScreen reload premium 정책 — 사용자 요구 발생 시 진행
  4-6: premium ↔ calc-engine 가산 의미 중복 분석 — 별도 대형 STEP

[현재 최우선 작업]
STEP 5 — 추가버튼 / 초기화 정교화
  5-1: 추가버튼 / 초기화 UX 연결 ✅
       추가버튼 조건부 표시 (마지막 visible row completed + hidden 존재 시)
       문구 통일 "동일 가산율의 다른 수당을 추가합니다"
       reset 연결 유지 / 신규 state 없음
  5-2: 초기화 버튼 표시 조건 정교화 ✅
       입력값 존재 시에만 표시 (render-time 파생 / 신규 state 없음)
       초기 진입 시 숨김 / 입력 시작 시 즉시 노출

[잠재 후속 개선 — 별도 STEP 필요 시]
- premium 단일가산(연장/야간/휴일)과 calc-engine 자체 가산의
  의미 분리/중복 방지 설계

[현재 핵심 구조]
- 단일가산: singlePremiumRows[] 3행
- 맞춤가산: customPremiumRows[] 3행
- 이중/삼중: 단일 객체
- 추가버튼: hidden row visible 토글 방식
- 삭제 버튼 없음 → 전체 초기화 방식
- usePremium hook: src/hooks/use-premium.tsx

[usePremium 확정 구조]
type UsePremiumReturn = {
  expanded: { expandedRowId, toggleExpanded }
  single:   { rows, showNextRow, resetRows, handlers, amounts, subtotal }
  double:   { combo, hours, handlers, amount }
  triple:   { hours, handlers, amount }
  custom:   { rows, showNextRow, resetRows, handlers, amounts, subtotal }
  totals:   { totalPremium }
}
type PremiumSectionProps =
  Omit<UsePremiumReturn, "totals"> & {
    totalPremium: number
  }

Home.tsx:
const p = usePremium(wage)
const { totals, ...sectionProps } = p
<PremiumSection {...sectionProps} totalPremium={totals.totalPremium} />
const adjustedGrossPay = result.grossPay + totals.totalPremium

[주의]
- premiumAmount state 저장 금지
- useMemo dependency 체크리스트 준수 (§1.12)
- 각 STEP마다 동작 동일성 검증
- 파트너 구조+프롬 → Claude 검토 → 개발자 컨펌 → Agent 전달
- expandedRowId: STEP 3-F-2에서 동시 이동 필수

[즉시 확인할 것]
§1.6-4 / §1.12 / §19 J-4

[절대 규칙 — 상세]
- 캘디게 구조 변경 금지
- trigger-gate 관련 로직 추가 금지
- 계산은 항상 수행 / 표시만 제어
- 매뉴얼 §번호 기준 작업만 진행

[작업 우선순위 — v13.0 기준]

🔴 즉시
STEP 3-F — usePremium hook 추출 (6단계)
STEP 3-G — adjustedGrossPay 연결
STEP 4   — 저장 연동
STEP 5   — 추가버튼/초기화 정교화

🟡 후순위
❌ P3 — allowanceRows juhu row 복귀 + JuhuSection 패널 연결 (폐기)
      → 이미 구현 확인됨 (ResultGrid.tsx:136 / JuhuSection.tsx 연결 완료)

🟡 후순위
P4  — UI-A~F 주휴 미결 항목 (파란 배지 포함)
      + UI-I / UI-J / UI-J1 / UI-K (v10.1 신규 추가)
P5  — UX 안내 규칙 확정
P6  — 검증 체크리스트
P7  — 연차수당 신설 구현 (§15 / UI-M)
P8  — holidayHours 변환 불일치 수정 (§6.7)
P9  — dead code 제거 (PremiumRateCard / NightPayCard)
P10 — useMemo 단순화 (optional)

🔵 신규 추가 (Jin님 확인 항목)
P-A — 첫 화면 기록보기 버튼 위치/노출 확인 및 구현
      (W-02 / W-05 기준)
P-B — 피드백 기능 복구
      (구글문서 질문 완성본 기준 / W-16 기준)
P-C — 가산율 피커 비단위 입력 (0.3, 0.8 등)
      (W-10 기준)
P-D — 공유 등 하단 기능모음 버튼 확인 및 구현
      (W-23 기준)

🔵 버그
BUG-01 — 기록보기: 저장버튼 토글
          (누를 때마다 저장↔취소 반복)
          현재: 누를 때마다 계속 저장만 됨

🔵 UX
UX-01 — 입력화면 세금·공제 4지 선다 아코디언
         선택 시 해당 항목만 펼침
         나머지 3개 자동 축소
         대상 파일: OptionsSection.tsx 또는 SupplementScreen.tsx (확인 필요)

UX-02 — 펼침 항목 글로우잉 효과
         (§UX-02 상세 참조)

🔵 UI 미결
UI-L — 라벨 클릭 → 정보 표시 + 정보 아이콘 추가
        적용 화면 미정 (기록보기 화면 vs 수당 화면 확인 필요)

🔵 먼 후순위
P11 — Status 타입 확장 (fail_hours / fail_absent)
P12 — attendance week 객체 내부 포함

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PART 1  운영 매뉴얼 (운.메)
변하지 않는 원칙 · 개념 · 설계 기준
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 문서 업데이트 점검 항목
업데이트 전 확인:
- 1. 메타 규칙 — 새 원칙 추가됐는가?
- 2. 개념 정의 — 완전주/상태모델 변경됐는가?
- 3. 계산 흐름 — 단계/파일 위치 변경됐는가?
- 4. 금지 목록 — 새 항목 추가됐는가?
- 5. UI 스펙 — 색상/문구/구조 변경됐는가?
- 6. 경우의 수 테이블 — 새 케이스 추가됐는가?
업데이트 후 확인:
- A. 운.메 내용이 인.리 스펙과 일치하는가?
- B. 용어 통일 (근무요일/법정소정근로일) 지켜졌는가?
- C. 변경 불가 원칙이 훼손되지 않았는가?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 메타 규칙 (전역 — 절대 변경 불가)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1.1 최소 수정 원칙
- 기존 구조 유지 / 리팩토링 금지
- 필요한 부분만 수정 — 잘 작동하는 구조는 건드리지 않음
- 전체 코드 출력 금지 / diff만 출력

1.2 계산 / 표현 분리 원칙
- calc-engine → UI 직접 연결 금지
- UI는 week.status 외 hours/attendance 직접 참조 금지
- 판단 로직은 calc-engine 또는 use-calc에서만

1.3 언어 규칙
- UI에서 'h' 사용 금지 → 반드시 '시간' 사용
- 내부 계산은 숫자(h) 사용 가능

1.4 용어 통일 규칙
⚠ '법정 소정근로일' 단독 사용 금지 — 반드시 '근무요일(법정 소정근로일)'로 병기

1.4.1 수당 용어 체계 (v7.0 확정)
Allowance = 수당 항목 (종류 지칭)
Pay = 실제 지급 금액
Premium = 가산율
※ JuhuAllowance는 Premium 없는 독립 수당

1.4.2 한·영 병기 용어 모음집 (v11.0 업데이트)
⚠ 3구분 원칙: 내부변수 / UI문구 / 설명용어

[기존 확정 항목]
UI문구                    내부변수                      설명용어
──────────────────────────────────────────────────────────────
uniform + direct          uniformDirect                 매일 동일 + 직접 입력 (1×1)
uniform + timerange       uniformTimerange              매일 동일 + 출퇴근 시각 (1×2)
perday + direct           perdayDirect                  요일별 상이 + 직접 입력 (2×1)
perday + timerange        perdayTimerange               요일별 상이 + 출퇴근 시각 (2×2)
없음                      workDays / pattern            근무요일
없음                      juhuPay / JuhuAllowance       주휴수당
없음                      hoursPerDay                   하루근무시간
없음                      hasCalculatedOnce             계산최초실행여부
없음                      resetCalculated               계산표시초기화
없음                      Time-Attribute Allowance      시간속성형 수당
없음                      Status-Based Paid Allowance   상태유급형 수당
없음                      Calculation Display Gate      계산 표시 게이트

[가산율 기반 제수당 신규 확정 항목 (v11.0)]
UI문구                         내부변수                        설명용어
──────────────────────────────────────────────────────────────────────
단일가산/이중가산/삼중가산/맞춤가산  premiumType                가산유형
50%추가/100%추가/150%추가       premiumRate                    가산율
시간 입력                       premiumHours                   가산시간
+00,000원                      premiumAmount                   가산금액
연장/야간/휴일                  selectedSingleAllowance         단일가산 선택수당
연장/야간/휴일 (복수)           selectedCustomAllowances        맞춤가산 선택수당
연장+야간/야간+휴일/연장+휴일   allowanceCombo                  수당조합
단일가산 배열                   singlePremiumRows[]             단일가산 행 배열
맞춤가산 배열                   customPremiumRows[]             맞춤가산 행 배열
이중가산 행                     doublePremiumRow                이중가산 행
삼중가산 행                     triplePremiumRow                삼중가산 행
없음                           isSingleRowCompleted             단일행 입력완료 여부
없음                           isCustomRowCompleted             맞춤행 입력완료 여부
없음                           isSingleRowVisible               단일행 표시여부
없음                           isCustomRowVisible               맞춤행 표시여부
+ 단일가산 추가                 isAddSingleRowButtonVisible      단일가산 추가버튼 표시여부
+ 맞춤가산 추가                 isAddCustomRowButtonVisible      맞춤가산 추가버튼 표시여부
단일가산 초기화                 resetSinglePremiumRows           단일가산 초기화 함수
맞춤가산 초기화                 resetCustomPremiumRows           맞춤가산 초기화 함수
없음                           initialPremiumRowState            가산행 초기 복원값
없음                           expandedRowId                    펼침행 확인번호
없음                           inlineGuideShownOnce             인라인 안내 1회 표시여부
없음                           isSingleRowCompleted             단일행 입력완료 여부
없음                           isCustomRowCompleted             맞춤행 입력완료 여부
없음                           totalWorkHours                   총근무시간 (검증 기준값)

1.5 색상 규칙 (결과 상태 전용)
⚠ 색상은 결과 상태 표현 전용 — 구조 구분용 사용 금지

1.6 협업자 태도 원칙 (v7.9)
1. 두괄식으로 최선의 대안을 먼저 제시
2. 제안 시 반드시: 기준 / 판단 근거 / 장단점·리스크 비교
3. 모든 판단과 제안은 반드시 매뉴얼 기준으로만

1.6-4 작업 진행 흐름 규칙 (v12.0 신규)

[흐름 규칙 — 최우선]
1. 무엇을 기준으로 작업할 것인가?
2. 그 기준을 세우는 근거는 무엇인가?
3. 기준 확정 후에만 대안 제시
4. 현 과제 완료 후에만 후속작업 제시
   (완료 판단은 파트너 AI 자체 판단)

[제안 시 — 흐름 규칙 준수 후 적용]
  두괄식으로 최선의 대안 먼저 제시 (§1.6-1)
  매뉴얼 기준으로만 판단 (§1.6-3)

[권장 흐름 — 코드 작성 전 구조 제시 필수] (v13.0 추가)

① 구조 제시 (코드 전 항상)
   - 현재 수정 목표
   - owner / props / state 위치
   - 지금 구현할 것
   - 지금 구현 안 하는 것 + 이유
   - 미래 STEP 연결 예정
   - 리스크

② 개발자 확인 ("이상 없음" or 수정 지시)

③ 코드 작성 → 리뷰 → 다음 STEP

[개발자 역할 — 구조 감독자]
  ① owner 위치 이상 없는가
  ② 미래에 꼬이지 않는가
  ③ 현재 STEP 범위 넘었는가

[AI 역할]
  구조 시뮬레이션 / 코드 생산
  매뉴얼 정합성 유지 / STEP 경계 유지
  완성형 생성 충동 차단

[현재 STEP 범위 외 제안 금지]
  STEP 범위를 벗어난 신규 기능 제안은
  개발자 요청 시에만 수행

[멈춤 금지 예외 조건] (v13.1 추가)
  다음 상황 진입 시 "진행 중단 후 구조 판단" 허용:
  - 구조 충돌
  - owner 충돌
  - 순환 의존
  - 대규모 리팩토링 진입

[파트너 AI 검토 기준] (v13.0 추가)

MODE A — STEP 검토 (기본)
  1. 현재 STEP 범위 안에서 우선 검토한다.
  2. 현재 STEP에 직접 영향 없는 미래 확장 제안은
     기본적으로 생략한다.
  3. 치명적 버그 / 현재 구조 충돌 / 타입 오류 가능성을
     우선 지적한다.
  4. 선택적 개선안 / 리팩토링 / 미래 최적화는
     개발자 요청 시에만 제시한다.
  5. 진행 속도와 증분 안정성을 우선한다.

MODE B — 아키텍처 검토 (요청 시만)
  장기 확장성 / 구조 개선 / 미래 리스크 포함
  → 개발자가 명시적으로 요청할 때만 사용

1.7 구조 선택 기준 (v7.9)
- 매뉴얼에 정의된 UI 구조를 최우선 기준으로 삼는다

1.8 복수 작업 순서 판단 원칙 (v7.7)
1. 의존 관계 확인
2. 독립적이면 → 즉시 실행 가능한 것 먼저
3. 의존 관계면 → 선행 작업 먼저
4. 매뉴얼 업데이트는 프롬/코드와 독립적이면 프롬 먼저

1.9 프롬 파일 제공 기준 (v7.6)
- 새로 작성된 프롬 → txt 파일로 저장 후 다운로드
- 50줄 이상 새 프롬 → 반드시 txt 파일로 제공

1.10 파트너 AI 운영 원칙 (v10.0)

▶ 파일 형식
- 정본 매뉴얼 → txt
- 쓰레드 도중 → 작업리스트 txt
- docx는 필요 시에만 생성

▶ 파일 운영
- 쓰레드당 작업리스트 1개 (추가통합 방식)
- 버전: 매뉴얼과 동일한 소수점 체계 (v10.1, v10.2 ...)
- 쓰레드 종료 시 → 정본 매뉴얼에 통합 → 자연수 버전 업
- 새 쓰레드 시작 시 → 통합된 정본 매뉴얼 txt 1개만 첨부

▶ 대기 표시 규칙
- 신규 대기 → 내용 상세 표시
- 기존 대기 (업뎃 미완료) → 제목 + 한 줄 설명만
- 업뎃 완료 항목 → 표시 불필요
- 형식: 대기 N: [내용 — 해석 여지 없이 정확하게]

▶ 토큰 절약 원칙
- 1순위: 프로젝트 안정성 / 정합성
- 2순위: 토큰 절약
- 충돌 시 → 토큰 절약 포기 + 충돌 지점 명시 후 Jin님 판단 요청

▶ 코드 다운로드 강제 기준
- 파일 수정 3회 이상 누적 시
- 오류 발생 시
- 구조 전면 교체 시
- 쓰레드 종료 전

▶ GPT 프롬 처리 규칙
→ §1.11 참조

▶ 위치 anchor 강제 (v13.1 추가)
- "아래/위" 대신 특정 함수/버튼/useMemo 기준 anchor 명시 필수
- 기존 코드 일부 교체보다 anchor 기반 신규 block 추가 우선

▶ 신규 용어 생성 시 처리 규칙
- 내부 변수 확정 순간 즉시 개발자님께 한·영 병기 + 설명 보고
- 작업리스트 한·영 병기표에 즉시 추가

▶ 확정 제안 표기 원칙 (v10.1 신규)
- 모든 확정 항목에 "확정 제안"으로 표기
- 확정 전까지 "미결" 또는 "보류"로 표기

▶ JSX/TSX 코드 출력 규칙 (v13.0 신규)

JSX/TSX 또는 TypeScript 코드 포함 시
반드시 fenced code block 사용:
  ```tsx
  ...
  ```
  또는
  ```ts
  ...
  ```

이유:
  꺾쇠괄호(<div> <span> 등)가
  HTML 태그로 파싱되어 렌더링 시 사라짐

특히 주의 태그:
  <div> / <span> / <button> / <input>
  JSX 태그 전반

적용 대상:
  파트너 AI → 개발자 전달 코드 전체
  Replit Agent 전달 프롬프트 포함

1.11 GPT 전용 운영 원칙 (v12.0 신규 분리)

▶ GPT 프롬 처리 규칙 (GPT 전용)
- 기존과 동일 프롬 → "그대로 실행" 한 줄
- 변경 시 → 변경 부분 + 완성 프롬 전체 재제시

▶ GPT 작업 진행 흐름 규칙 (v13.0 추가 / GPT 전용)
1. 검토만 하고 종료 금지
2. 검토 → 보충 → 다음 STEP 자동 제시
3. 구조 + 프롬 동시 제시
4. 현재 상태 요약 유지
5. 다음 자연스러운 작업 자동 연결

▶ 구조 오해 방지 (v13.1 추가 / GPT 전용)
- UI 유사성만으로 동일 state 구조 가정 금지
- rows[] 여부 / owner 위치 / 실제 state 이름 확인 후 제안
- (§실제 식별자 기준 검토 원칙과 연계)

1.12 단계별 구현 경계 원칙 (v13.0 신규)

적용 범위:
  단계별 구현 구조를 사용하는 AI 협업 프로젝트
  구체 허용/금지 항목은 프로젝트마다 재정의

핵심 원칙:
  "지금 일부러 덜 구현하는 것이 핵심"
  빠뜨린 것이 아니라 의도적 보류

골조 구현 (Skeleton Implementation):
  목업과의 차이:
    목업 = 그림 / 정적 시각 확인용
    골조 구현 = 실제 작동하는 뼈대
               실제 파일로 존재
               이후 STEP에서 살 붙이기만 수행
               버리는 코드 거의 없음
  STEP 1 = 골조 구현 단계

현재 프로젝트(Payroll Calculator) 기준:

  STEP 1 목표: UI 구조 고정
    허용: rows[] / expandedRowId / visible toggle
          map() / mock buttons / mock inputs
    금지: 실제 계산 / useMemo / derived
          validation / disabled 계산
          duplicate 검사 / 저장구조

위반 시:
  추가 구현 중단 후 개발자 판단 요청
  (즉시 롤백 아님 — 부분 유지 가능)

useMemo/useCallback/useEffect 추가 시 필수: (v13.0 추가)
  1. 참조 변수 목록 작성
  2. dependency 배열 대조 검증
  "사용 변수 = deps" 눈으로 검증 후 작성

먼 후순위 메모: (v13.0 추가)
  연속 클릭 race 가능성:
    현재: 외부 state snapshot 사용
    조건: 단일 사용자 / 동기 / async 없음 → 현재 무해
    향후 async 흐름 추가 시 재검토 필요

리팩토링 ≠ 기능 추가 (v13.1 추가):
  리팩토링 STEP에서 기능/UX 변경 금지
  동작 동일성 유지 우선

한 STEP = 한 변경 원칙 (v13.1 추가):
  한 STEP에서는 핵심 변경 축 1개만 우선 수행 권장
  (state owner 이동 / UI 구조 변경 / 계산 owner 이동 등)
  단, 이동 대상 state와 공유 의존 관계인 축
  (예: expandedRowId)은 동일 STEP에서 함께 이동 권장
  (§Hook 추출 증분 원칙 연계)

presentation component 기준 (v13.1 추가):
  도메인 계산 state / useMemo / handler를 보유하지 않는 것을 원칙으로 한다
  단, 로컬 UI 표현 state
  (예: hover, focus, 애니메이션 트리거 등 렌더 전용)는 예외 가능

동작 동일성 검증 원칙 (v13.1 추가):
  리팩토링 단계에서 UI / 계산 / interaction 동일 우선 검증

골조 완료 정의 (v13.1 추가):
  골조 완료 = 구조/owner/흐름 확정
  렌더/UX 미세조정은 별개

setState updater 내부 제한 (v13.1 추가):
  외부 state 참조 최소화
  side effect 금지
  derived 계산 최소화
  위반 시: 추가 구현 중단 후 개발자 판단 요청
           (§1.12 기존 위반 처리 기준 동일 적용)

race 재검토 트리거 (v13.1 추가):
  다음 기능 추가 시 race 가능성 재검토:
  async 저장 / debounce / animation / transition / optimistic update

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.13 구조 설계 원칙 (v13.1 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Derived Owner 승격 원칙:
  derived 값이 상위 도메인의 핵심 계산에 사용되기 시작하면
  callback/effect bridge 적용 전
  owner 승격 필요 여부 먼저 검토
  ⚠ "owner 승격" 용어: 현재 §1.4.2 병기 보류
     (설계 개념 용어 단계 / 실제 변수명 등장 시 추가)

Hook 추출 증분 원칙:
  hook 추출 시:
  state / handler / derived / owner 한 번에 전체 이동 금지
  도메인 단위 증분 이동 권장
  단, 여러 도메인이 공유하는 state 축 (expandedRowId 등)은
  부분 이동 금지 — 동일 STEP에서 함께 이동 권장

실제 식별자 기준 검토 원칙:
  패턴 복제 전 반드시 확인:
  - 실제 state 이름
  - rows[] 여부
  - owner 위치
  - useMemo 위치
  UI 유사성만으로 동일 구조 가정 금지

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. 절대 금지 목록
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- UI에서 week.hours >= 15 판단
- UI에서 attendanceByWeek[i] 직접 읽기
- UI에서 qualifies 참조
- UI에서 계산 로직 작성
- status로 최종 지급 판단 (status + isFullWeek 결합 필요)
- mergedByDay 덧셈
- status를 merged 이전에 생성
- 계산 흐름 역방향 참조
- 주 배열 길이 임의 변경
- 전체 코드 출력
- UI에서 'h' 사용
- isFullWeek를 use-calc에서 재계산
- 코드 범위 지정 시 라인 번호 기준 사용
- allowanceRows.map 부분만 부분 복사
- 코드 파일 요청 시 cat 출력 사용
- 긴 프롬 직접 출력
- 캘디게 구조 변경
- trigger-gate 관련 로직 추가 (완전 폐기)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. 공통 개념 정의
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3.1 주(週) 기준
- 주 = 월요일 ~ 일요일 (고정)

3.2 완전주 / 불완전주 정의 (절대 원문)
🔴 불완전주: 근무요일의 일부가 다른 급여산정 기간에 걸쳐있는 주
🟢 완전주: 전체 근무요일이 현재 급여기간 안에서 끝나는 주
- 완전주 → isFullWeek = true
- 불완전주 → isFullWeek = false

3.3 상태 모델 (4가지)
PENDING: 판단 유보 → 계산에서는 항상 미지급(NOT_PAID)
주휴 지급 판단 로직:
if (!attendance)                              → NOT_PAID (FAIL_ABSENT)
if (!hoursOK)                                 → NOT_PAID (FAIL_HOURS)
if (FIRST && !isMergedFirst && !isFullWeek)   → NOT_PAID (PENDING)
if (LAST && !isFullWeek)                      → NOT_PAID (PENDING)
→ PAID (SUCCESS)

3.4 병합주 (Merged Week)
- mergedByDay 규칙: 덧셈 금지 / current 우선 선택

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. 전체 계산 흐름 (단방향 — 역전 금지)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
입력 → 주 생성 + isFullWeek 판단 → 병합 처리 → status 계산
→ 주휴 지급 판단 → UI 렌더링
⚠ 역방향 참조 금지 / UI → 계산 접근 금지

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. 모드 구조 (v10.1 역할 재정의)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1×1: uniform + direct   (매일 동일 + 직접 입력) ← 현재 구현
1×2: uniform + timerange (매일 동일 + 출퇴근 시각) ← 미구현
2×1: perday + direct    (요일별 상이 + 직접 입력) ← 미구현
2×2: perday + timerange  (요일별 상이 + 출퇴근 시각) ← 미구현

⚠ 2×2 역할 재정의 (v10.1):
  이전: 출퇴근 시각 → 야간/연장 자동판정 (시스템 중심)
  이후: 출퇴근 시각 → 총근무시간 계산 보조만 수행 (사용자 판단 보조)
  수당 판단은 사용자 몫 / 앱은 총근무시간 산출만 지원

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. 입력 항목 구조
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6.1 핵심 입력
- 시급 (wage)
- 근무 시작 요일 (startDayIndex: 0=월 ~ 6=일)
- 근무일수 (actualDays)
- 근무요일 (workDays / pattern)

6.2 이전 기간 입력 (첫주 병합용)
- 이전 기간이 있습니다 토글: ON=병합계산 / OFF=단독계산

6.3 개근 여부 입력
- attendanceByWeek: boolean[] — UI 상태로 관리

6.7 후순위 미결
⚠ holidayHours 변환 불일치 — use-calc.ts
입력(총시간) / safeMult ≠ mult 시 오차 발생 가능 → P8 처리

6.8 주휴 UI 후순위 복원 항목
allowanceRows[0] — juhu row (맨 앞)
├── 좌: ☑ 주휴수당 토글
├── 중앙: (7주 발생 · 주30시간) 요약
├── 우: +700,000원
└── 클릭 → 패널 열림 → <JuhuSection />

❌ 누락 항목 (복원 예정 / P4):
- 파란 배지 ① + '주휴 발생 조건 — 개근 여부 선택'
- 파란 배지 ② + '주휴 발생 조건 — 주 15시간 이상 근무 여부'
- ON시 안내: '첫 주는 이전 기간의 마지막 주 근무를 포함해 계산됩니다'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6-신규. 제수당 구조 설계 원칙 (v10.1 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6-A. 수당 계열 분류 (확정 제안)

[시간속성형 / Time-Attribute Allowance]
  실제 근로시간 안에서의 속성 분류
  야간수당   nightPay
  연장수당   overtimePay
  휴일수당   holidayPay
  → 총근무시간 안의 일부 시간에 대한 가산
  → 총근무시간에 추가 합산되지 않음
  → 가산적용시간 = 총근무시간 중 일부

[상태유급형 / Status-Based Paid Allowance]
  실제 근로시간 외 유급 인정
  주휴수당   juhuPay
  연차수당   annualPay
  → 추가 근로가 아닌 유급 인정 개념
  → 총근무시간에 포함되지 않음
  → 조건 충족 시 자동 발생

6-B. 입력 구조 (확정 제안)

채택: 구조 B — 수당별 시간 직접입력형

근거:
  ① 복잡도 최소화 원칙 (§11)
  ② 달력/출퇴근 시각 자동계산 불필요
  ③ 가산 유형 명시로 중복 문제 해소
  ④ 사용자가 이미 인지한 값 직접 입력
  ⑤ 모바일 UX에 최적화

입력 흐름:
  STEP 1 기본근무 입력
    시급 / 총근무시간 / 근무일수 → 기본급 확정
    핵심 UX 문구:
    "실제 일한 전체 근무시간을 입력하세요.
     (가산수당 대상 시간 포함)"

  STEP 2 시간속성형 수당 입력
    총근무시간 중 가산 대상 시간 입력 + 가산 유형 선택
    핵심 UX 문구:
    "총근무시간 중 추가 가산이 적용되는
     시간을 입력하세요.
     예: 40시간 근무 중 8시간이 야간이면
     → 가산적용시간 8시간 입력"

  STEP 3 상태유급형 수당
    조건 판단 → 자동 표시

총근무시간 원칙:
  → 총근무시간 = 원본 노동시간 (고정)
  → 가산적용시간은 총근무시간의 속성 분류
  → 가산적용시간을 총근무시간에 합산하지 않음
  → 앱은 총근무시간과 가산시간의 관계를 검증하지 않음
     (사용자 판단에 맡김 — §11)

6-C. 가산율 구조 (확정 제안)

선택형 피커:
  +0.5   50% 가산
  +1.0   100% 가산
  +1.5   150% 가산
  직접입력  비단위 가산 (0.3, 0.8 등)

가산 유형 분류 (숫자와 반드시 병기):
  단일가산  +0.5   야간만 / 연장만 / 휴일만
  이중가산  +1.0   야간+휴일 / 연장+휴일
  삼중가산  +1.5   야간+연장+휴일
  맞춤가산  직접입력  사업장 약정

⚠ 규칙: 숫자만 단독 표시 금지
  반드시 유형명 + 상황 예시 병기

제수당명 병기 원칙:
  기존 수당명(야간수당, 연장수당 등)과
  가산유형을 함께 표시
  예: "야간수당 · 단일가산(+0.5)"

6-D. 2×2 모드 구조 재정의 → §5 참조

6-E. 설명 원칙 (신규)

사용자가 결과 금액이 왜 나왔는지
이해할 수 있도록 계산 근거를 함께 표시

표시 예:
  야간수당  8시간 × 단일가산(+0.5)  = +40,000원
  휴일수당  4시간 × 이중가산(+1.0)  = +40,000원

목적:
  ① 초보자 노동법 자동 학습
  ② 검산 근거 명확화
  ③ 고용주 이의제기 시 법적 설명력 확보

6-F. 미결 사항

① 연장수당 입력란 신설
   현재 야간/휴일만 있음 → 연장 추가 필요
   → P3 연계 또는 신규 번호 부여 필요

② 가산 유형 UI 구현 방식
   피커 / 설명 텍스트 / 별도 선택UI 중 미정

③ 총근무시간 표시 정책
   수당별 입력시간 합산 여부 미정
   현재: 반영 안 됨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7~9. 주 생성 / 주휴 엔진 / UI 구조
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
(v9.0 §7~§9 내용 동일 유지)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10. 확장 설계 (미래)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- attendance → week 객체 내부 포함 (P12)
- 세금 재계산 동기화
- 중간 완전주 개별 시간 입력
- 급여기간 사용자 정의

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
11. 제품 설계 원칙 (v4.0)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 앱은 모든 예외 케이스를 처리하지 않는다
- 판단이 애매한 영역은 사용자 해석에 맡긴다
- 복잡도를 증가시키는 기능은 배제한다

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
14. 전 수당 공통 규칙
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
안내문구 원칙: [수당명] 없음 — [사유] (1줄)

14-1. allowanceRows 순서 확정
[0] 주휴 / juhu
[1] 연차 / annual (후순위 구현)
[2] 연장 / overtime
[3] 야간 / night
[4] 휴일 / holiday

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
15. 연차수당 / Annual Leave (v8.x 확정)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

15-1. UI 구조
- 매월 정산 (Monthly): 개근 전제
- 퇴사 정산 (Severance): 연차개월수 입력

15-2. 계산 공식
mode = monthly: days = isFullAttendance ? 1 : 0
mode = termination:
  months = 0 → days = 0
  0 < months < 12 → days = months
  months >= 12 → days = Math.min(15 + (months - 12), 25)
amount = days * dailyHours * hourlyWage
MIN_WAGE = 10000 (경계값 포함)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
16. 계산 표시 게이트 / Calculation Display Gate (v10.0)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠ v9.0 §16 (debounce / trigger-gate) 완전 폐기 → 캘디게로 대체

16-1. 핵심 구조
- 계산: 항상 수행 (state 변경 시 useMemo 즉시 실행)
- 표시: hasCalculatedOnce (계산최초실행여부) 조건으로 제어

16-2. 동작 규칙
초기 진입 → hasCalculatedOnce = false → 결과 숨김
hoursPerDay 유효 입력 → hasCalculatedOnce = true → 결과 표시
이후 모든 입력 (시급/토글/요일) → 즉시 재계산 반영
reset() → hasCalculatedOnce = false → 결과 다시 숨김
loadState() → hasCalculatedOnce = false → 결과 숨김
입력수정 진입 → hoursPerDay 비움 + hasCalculatedOnce = false

16-3. 유효 입력 판단 기준
- 빈값("") → 차단
- 소수점 입력 중 ("8.") → 차단
- 그 외 → hasCalculatedOnce = true

16-4. 구현 위치
- use-calc.ts: hasCalculatedOnce useState
- use-calc.ts: hoursPerDay useEffect → setHasCalculatedOnce(true)
- use-calc.ts: reset() / loadState() → setHasCalculatedOnce(false)
- use-calc.ts: return { result: hasCalculatedOnce ? adjustedResult : null }
- use-calc.ts: resetCalculated() → return에 노출
- Home.tsx: 입력수정 버튼 → update("hoursPerDay", "") + resetCalculated()

16-5. 폐기 항목
- debounce 구조 완전 제거
- trigger-gate 완전 폐기
- snapshot / calcTrigger 완전 제거
- isCalculatingPending 제거

16-6. 검증 체크리스트
1. 첫 진입 → 결과 숨김 ✅
2. hoursPerDay 입력 → 결과 표시 ✅
3. 토글/시급 변경 → 즉시 반영 ✅
4. reset → 결과 숨김 ✅
5. 기록보기 → 결과 숨김 ✅
6. 입력수정 → 결과 숨김 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
§UX-02. 펼침 항목 글로우잉 효과 (v10.1 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

목적:
  펼칠 수 있는 항목임을 직관적으로 인지하도록
  시각적 힌트 제공

발동/소멸 조건:
  닫힘 → 글로우잉 ON
  열림 → 글로우잉 OFF (자동 소멸)
  닫힘 → 즉시 재발동
  진입 경로 무관
  (초기화 / 재입력 / 기록보기 동일 적용)

글로우잉 형태:
  펄스 1종 고정
  (은은하게 밝아졌다 어두워지는 반복)
  ⚠ 3종 랜덤 삭제 — 구현 복잡도 / 상태 꼬임 리스크

적용 범위:
  현재 구현 전체 + 2×2 확장 화면까지

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
§17. 글로벌 확장 전략 (v10.1 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

17-A. 글로벌 시장 현황
  HR/급여 소프트웨어 시장 규모:
    2024년   81억 달러
    2035년   261억 달러 (예상)
    CAGR     11.2%
  아시아태평양 성장률 가장 빠름
  핵심 트렌드:
    ① 클라우드 기반 이동
    ② 모바일 셀프서비스 확대
    ③ 긱 이코노미 수요 급증
    ④ 각국 노동법 현지화 요구 심화

17-B. 국가별 현지화 요구사항

  [일본] — 우선 확장 1순위
    심야수당(深夜手当): 22시~5시 25% 가산
    잔업수당(残業手当): 법정 25% 이상
    휴일수당(休日手当): 35% 이상
    → 가산율 구조 B안과 직접 호환 가능

  [호주] — 우선 확장 2순위
    페널티 레이트(Penalty Rates) 제도
    주말/야간/공휴일별 가산율 직접 명시
    Fair Work 기준 준수 필수

  [영국]
    National Living Wage / National Minimum Wage
    Overtime: 법정 의무 없으나 계약 기준 적용
    → 가산율 직접입력 구조 유리

  [동남아 (필리핀/베트남/태국)]
    긱워커/알바 인구 급증
    설명형 UX 수요 높음
    → 중장기 타깃

17-C. 현지화 앱 벤치마킹

  [전략 유사형 — 설명형 검산 계산기]
  Gig Worker Salary Calculator
    개발사: Connect Fit Co., Ltd. (한국)
    한국명: 기그 / 기그 사장님
    글로벌: App Store (미국 포함) / Google Play
    다운로드: 100,000+ (Google Play 기준)
    구조: 달력 기반 (구조 A)
    시사점: 이미 글로벌 진출 / 구조 A로 선점
            → 우리 앱은 구조 B + 설명형으로 차별화

  Deputy (호주)
    시프트 기록 + 페널티 레이트 자동 계산
    구독형 수익 월 $4~25/직원

  [전략 상이형 — 자동화/관리형]
  Homebase (미국) / Shifty / 7shifts
    구조 A 완전체 / 기업용 / 관리자용
    우리 앱과 포지션 완전 다름

17-D. 글로벌 확장 구조화 방향

  [공통 코어]
    시급 × 시간 = 기본급
    가산율 피커 (유형 병기)
    설명형 결과 표시

  [현지화 레이어]
    국가별 법정 가산율 프리셋
    수당 명칭 현지어
    세금/공제 계산 방식
    통화/소수점 표기

  우선순위:
    1순위   한국 완성
    2순위   일본 (구조 동일, 수치만 변경)
    3순위   호주 (페널티 레이트 프리셋)
    4순위   영국 / 동남아

17-E. 포지셔닝 전략

  현재 시장 공백:
    단순 계산기  → 빠르지만 설명 없음
    근태관리형   → 강력하지만 무거움

  우리 앱 포지션:
    "가볍지만 설명력 있는 급여 검산 앱"

  차별화 핵심:
    ① 가산 유형 UX (단일/중복/삼중/특이)
    ② 결과 설명 (왜 이 금액인가)
    ③ 초보자 자동 학습 구조
    ④ 이의제기 가능한 검산 근거

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
§18. 근무지 합산 · 저장기록 + 기록보기 설계 원칙 (v10.1 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

18-A. 저장기록 카드 2줄 구조 (출시 필수 / 확정 제안)
  1줄: 제목 · 총급여(실수령액)
  2줄: 수당 특징 요약
       (주휴포함 / 단일가산 8h 등)
  ⚠ 2줄 세부 내용 확정 보류

18-B. 기록보기 화면 편집 항목 (출시 필수 / 확정 제안)
  현재 기록보기 화면에 추가 구현
  7가지 항목:
    체크박스 / 번호 / 제목 / 기간 /
    총급여(실수령액) / 제수당액 / 세금·공제

  드래그 리오더링 ①:
    맨 위 카드에서 7가지 항목 순서 드래그
    → 나머지 모든 카드에 순서 자동 연동

  드래그 리오더링 ②:
    카드 자체 순서도 드래그 리오더링 가능

18-C. 근무지 합산 (출시 필수 / 확정 제안)
  요약형 카드 (근무지별)
  체크박스: 기본 숨김
            [선택] 버튼 누를 때만 활성화

  합산 결과 표시:
    계산결과 화면과 동일한 형식
    = 기록보기 단일 근무지 내역과 동일 형식
    내용만 선택된 근무지들의 합산값으로 표시
    제목: "합산 - 제목1 + 제목2"
          (선택된 기록 제목들 자동 조합)
    → 별도 상세 도표 / 확장 불필요

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PART 2  인수인계 리스트
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 현재 작업 위치
- STEP 3 완료 (derived value 연결 전체)
- 다음: STEP 3-F usePremium hook 추출 (6단계)

2. 미결 작업 목록

🔴 즉시
STEP 3-F — usePremium hook 추출
  3-F-1: use-premium.tsx 신규 생성 (타입/shape만)
  3-F-2: Single + expandedRowId hook 이동
  3-F-3: Double/Triple hook 이동
  3-F-4: Custom hook 이동
  3-F-5: totalPremium hook 이동
  3-F-6: PremiumSection presentation화
  ⚠ expandedRowId: 3-F-2에서 동시 이동 필수

STEP 3-G — adjustedGrossPay 연결
  grossPay + totalPremium = adjustedGrossPay
  Home.tsx owner

STEP 4 — 저장 연동
STEP 5 — 추가버튼/초기화 정교화

🟡 후순위
❌ P3 — allowanceRows juhu row 복귀 + JuhuSection 패널 연결 (폐기)
      → 이미 구현 확인됨 (ResultGrid.tsx:136 / JuhuSection.tsx 연결 완료)
      ⚠ dead code 제거 예정 PremiumRateCard.tsx / NightPayCard.tsx → P9 완료로 해소

P4  — UI-A~F 주휴 미결 항목
P5  — UX 안내 규칙 확정
P6  — 검증 체크리스트
P7  — 연차수당 신설 구현 (§15 / UI-M)
P8  — holidayHours 변환 불일치 수정 (§6.7)
P9  — dead code 제거 (PremiumRateCard / NightPayCard)
P10 — useMemo 단순화 (optional)

🔵 신규 추가
P-A — 첫 화면 기록보기 버튼 위치/노출 (W-02 / W-05)
P-B — 피드백 기능 복구 (W-16)
P-C — 가산율 피커 비단위 입력 (W-10)
P-D — 공유 등 하단 기능모음 버튼 (W-23)

BUG-01 — 기록보기: 저장버튼 토글
UI-L   — 라벨 정보 아이콘 추가
UX-01  — 입력화면 세금·공제 4지 선다 아코디언
UX-02  — 펼침 항목 글로우잉 효과 (§UX-02 참조)

🔵 먼 후순위
P11 — Status 타입 확장 (fail_hours / fail_absent)
P12 — attendance week 객체 내부 포함

3. usePremium hook 확정 구조

type UsePremiumReturn = {
  expanded: {
    expandedRowId: string | null
    toggleExpanded: (id: string) => void
  }
  single: {
    rows: SinglePremiumRow[]
    showNextRow: () => void
    resetRows: () => void
    handlers: {
      onSelectAllowance: (rowId, type) => void
      onChangeHours: (rowId, value) => void
    }
    amounts: Record<string, number>
    subtotal: number
  }
  double: {
    combo: DoublePremiumType | null
    hours: number | null
    handlers: {
      onSelectCombo: (type) => void
      onChangeHours: (value) => void
    }
    amount: number
  }
  triple: {
    hours: number | null
    handlers: {
      onChangeHours: (value) => void
    }
    amount: number
  }
  custom: {
    rows: CustomPremiumRow[]
    showNextRow: () => void
    resetRows: () => void
    handlers: {
      onToggleAllowance: (rowId, allowance) => void
      onChangeRate: (rowId, value) => void
      onChangeHours: (rowId, value) => void
    }
    amounts: Record<string, number>
    subtotal: number
  }
  totals: {
    totalPremium: number
  }
}

type PremiumSectionProps =
  Omit<UsePremiumReturn, "totals"> & {
    totalPremium: number
  }

Home.tsx 사용 패턴:
  const p = usePremium(wage)
  const { totals, ...sectionProps } = p
  <PremiumSection {...sectionProps} totalPremium={totals.totalPremium} />
  const adjustedGrossPay = result.grossPay + totals.totalPremium

4. 단계별 동작 동일성 검증 체크리스트

각 3-F STEP 후 필수 확인:
  □ TS 컴파일 통과 (에러 0)
  □ 런타임 마운트 정상
  □ expand toggle 4종 카드 정상
  □ 해당 STEP 핵심 동작 확인
  □ 기능 추가 없음 확인

5. 미결 핵심 쟁점
- adjustedGrossPay 연결: STEP 3-G에서 처리
- 저장 wiring: hook의 serialize()/loadState() 추후 노출
- 모드 확장: usePremium hook 구조 다중 인스턴스 지원 가능

4. 확정 스펙

4.1 상태 모델
type WeekStatus = 'success' | 'fail' | 'absent' | 'pending'
추후: fail→fail_hours / absent→fail_absent

4.2 색상 (Tailwind 확정)
SUCCESS:     border-blue-500  bg-#dbeafe
FAIL_HOURS:  border-amber-500 bg-#fef3c7
FAIL_ABSENT: border-gray-400  bg-#f3f4f6
PENDING:     border-amber-500 bg-#fef3c7

4.3 계산 흐름
입력 → 주 생성 → 병합 → status → 주휴 계산 → UI
※ 역방향 참조 금지

4.4 CompanySizeScreen 명칭
UI 한글: 5인 미만 사업장
파일명: CompanySizeScreen.tsx
내부 변수: isSmallBiz

5. 작업 표준 절차

5.1 코드 파일 확보 표준
1. Replit Agent에게 cp 명령 실행 요청
2. Replit 일반 탭에서 파일 다운로드
3. 다운로드한 파일을 파트너 AI 대화창에 업로드
⚠ cat / sed 출력 방식 사용 금지

5.2 실수 이력
1. 진입점 섹션 0 확인 전 작업 재시작 제안 반복
2. 소수점 버전 재팩 금지 규칙 위반
3. trigger-gate 구현 → 자동계산 문제 → C안으로 전환
4. snapshot 참조 공유 문제 → setSnapshot({...state})로 수정
5. loadState에서 snapshot 갱신 → 트리거 무력화

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
§19. 가산율 기반 제수당 UI 목업 구현 스펙 (v10.1 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[전체 수당 순서]
주휴 → 연차 → 연장 → 야간 → 휴일 → 세금·공제
⚠ 박스 구분 없음 / 단일 흐름 유지

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[A. 섹션 진입 안내 — PremiumSection 최상단 단일 안내영역]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

역할:
  개념 설명 / 오해 방지 / 전체 입력 철학 안내

위치:
  PremiumSection 전체 최상단 단일 영역
  (카드별 개별 안내 아님)

내용 (STEP2 설명 형식/문구/표현구조 그대로 재배치):
  "[총 근무 N시간] 안에 포함된,
   가산금액이 반영되어야 할 0시간을 입력하세요."

  ※ 문구 변경 금지 / wording 수정 금지
  ※ dynamic 계산값 이동 금지
  ※ reactive 숫자 연동 금지
  ※ 계산 state 표시 금지
  → 개념 설명 역할만 / 숫자는 각 카드 입력영역에서 유지

발동: 앱 최초 1회
      제수당 영역 화면 30% 이상 노출 시
축소 조건:
  ① 첫 번째 가산유형 선택 순간
  ② 3초 후 자동 축소

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[B. 가산유형 행 — 닫힘 상태]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[선택 전 닫힘] — 가로 1줄
☑ 단일(50%추가) · 연장 · 야간 · 휴일        0원
☑ 이중(100%추가) · 연장+야간                0원
☑ 삼중(150%추가) · 연장+야간+휴일           0원
☑ 맞춤 · 연장 · 야간 · 휴일                 0원

[선택 후 닫힘] — 2줄
☑ 단일(연장수당 50%추가)
  8시간 · +40,000원

글로우잉 규칙 (v13.1 보류):
  glow UX 현재 보류 — 사용자 피드백 기반 재오픈
  (기존 펄스 1종 고정 정책 → 보류 전환)

닫힘 요약 표시 규칙 (v12.0 확정):

  닫힘 축약 표기:
    단일가산 → 단일 / 이중가산 → 이중
    삼중가산 → 삼중 / 맞춤가산 → 맞춤
    (열림 헤더는 풀네임 유지)

  삼중가산 수당조합 생략:
    조합 고정(연장+야간+휴일)이므로 닫힘에서 생략

  [공통]
    금액: 항상 1줄 맨 오른쪽 고정

  [1줄이라면]
    가산유형(행번호) · 수당조합 · 가산율 · 시간 · 금액

  [2줄이라면 — 넘칠 경우에만]
    기본:
    1줄: 가산유형(행번호) · 수당조합 · 금액
    2줄: 가산율 · 시간

    수당조합까지 넘칠 경우:
    1줄: 가산유형(행번호) · 금액
    2줄: 수당조합 · 가산율 · 시간

    2줄도 넘칠 경우 (맞춤 3개 수당 한정):
    가산율 표기 축약 허용
    (구현 예시: 30%추가 → +30% / 정적 UI 렌더 후 최종 확정)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[C. 단일가산 — 열림 상태]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[선택 전] ☑ 단일가산 (50%추가)
[선택 후] ☑ 단일가산 (연장수당 50%추가)
  한 가지 수당만 가산될 때
──────────────────────────────────
STEP 1. 수당 선택
  [연장]  [야간]  [휴일]
  선택 후: 선택된 버튼만 표시
  이미 선택된 수당 → 비활성(회색) / 선택 불가
  선택 시 법적 설명 1줄 자동 표시:
    [연장] "정해진 근무시간을 초과해 일한 경우"
    [야간] "밤 10시~아침 6시 사이 근무한 경우"
    [휴일] "휴일에 근무한 경우"
  선택 즉시 헤더 동적 반영

STEP 2. 가산시간 입력
  [ 입력창 ]
  (장문 설명 제거 — 섹션 상단 안내영역 A에서 일괄 처리)
  (shimmer 적용 대상 — UX-02-5)

STEP 3. 즉시 금액 표시
  +40,000원
  이 금액이 [연장]수당으로 총급여에 추가됩니다.
  ※ [ ] 안 수당명은 선택값 동적 반영

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[D. 이중가산 — 열림 상태]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[선택 전] ☑ 이중가산 (100%추가)
[선택 후] ☑ 이중가산 (연장+야간수당 100%추가)
  두 가지 수당이 동시에 가산될 때
──────────────────────────────────
STEP 1. 수당 조합 선택
  [연장+야간]  [야간+휴일]  [연장+휴일]
  선택 후: 선택된 조합만 표시
  선택 즉시 헤더 동적 반영

STEP 2. 가산시간 입력
  [ 입력창 ]
  (장문 설명 제거 — 섹션 상단 안내영역 A에서 일괄 처리)
  (shimmer 적용 대상 — UX-02-5)

STEP 3. 즉시 금액 표시
  +80,000원
  이 금액이 [연장+야간]수당으로 총급여에 추가됩니다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[E. 삼중가산 — 열림 상태]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[선택 전] ☑ 삼중가산 (150%추가)
[선택 후] ☑ 삼중가산 (연장+야간+휴일수당 150%추가)
  세 가지 수당이 동시에 가산될 때
──────────────────────────────────
수당 조합: 연장+야간+휴일 (고정 / 선택 불필요)
헤더: 자동 반영

STEP 2. 가산시간 입력
  [ 입력창 ]
  (장문 설명 제거 — 섹션 상단 안내영역 A에서 일괄 처리)
  (shimmer 적용 대상 — UX-02-5)

STEP 3. 즉시 금액 표시
  +120,000원
  이 금액이 [연장+야간+휴일]수당으로
  총급여에 추가됩니다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[F. 맞춤가산 — 열림 상태]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[선택 전] ☑ 맞춤가산
[선택 후]
  1개 → ☑ 맞춤 단일가산 (연장)수당
  2개 → ☑ 맞춤 이중가산 (연장+야간)수당
  3개 → ☑ 맞춤 삼중가산 (연장+야간+휴일)수당
  계약서상 별도 가산율이 있을 때
──────────────────────────────────
맞춤가산 사용 목적 (v12.0 명문화):
  비정형 가산율(0.3, 0.8 등) 적용
  정형가산(단일/이중/삼중)의 대체 수단

대체관계 원칙:
  정형과 맞춤은 누적 적용 불가
  동일 수당 정형+맞춤 동시 선택 = 이중계산
  → 전 가산유형 중복 금지로 구조적 차단
  → 근거: 한 근무지 기준 검산 / 이중계산 방지

개념: 연장/야간/휴일 수당의 확장
      선택 수에 따라 자동 명칭 부여

STEP 1. 수당 선택 (복수 선택 가능)
  [연장]  [야간]  [휴일]
  이미 정형 가산에서 선택된 수당 → 비활성 처리
  선택 즉시 헤더 동적 반영

  ⚠ 복수선택 후 UI 표시 방식 — 미결 (Jin님 확정 필요)
  A안: 선택된 버튼 각각 유지
       [연장✓] [야간✓]
       → 개별 확인 가능 / 재선택 직관적 / 구현 단순
  B안: 조합 칩 병합 표시
       [연장+야간]
       → 깔끔 / 재선택 시 분해 필요 / 구현 복잡

STEP 2. 가산율 입력
  [ 30 % 추가 ]
  숫자만 입력 / % 추가 고정 표시
  계약서에 명시된 가산율을 입력하세요.

STEP 3. 가산시간 입력
  총 근무시간 [ 40시간 ] 안에 포함된,
  가산금액이 반영되어야 할 시간 [ 8 ] 을
  입력하세요.

STEP 4. 즉시 금액 표시
  +24,000원
  이 금액이 [연장]수당으로 총급여에 추가됩니다.
  ※ [ ] 안 수당명은 선택값 동적 반영
     → 요약 / 근무지 합산 / 급여명세 전체 반영

[+ 맞춤가산 추가] 버튼
  동일 UI 복제
  이미 선택된 수당 비활성 처리
  가산율 독립 입력 가능

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[G. 가산율 표기 통일 규칙]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0.5 / 1.0 / 1.5 표기 사용 금지
→ 50%추가 / 100%추가 / 150%추가 통일
맞춤: [ 숫자 % 추가 ] 입력형

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[H. 요약 표시 기준]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
형식: 수당명 앞 / 가산율 보조
순서: 연장 → 야간 → 휴일 고정

예:
  연장수당 50%추가 · 8시간 · +40,000원
  야간수당 50%추가 · 4시간 · +20,000원
  연장+야간수당 100%추가 · 4시간 · +32,000원
  연장수당 30%추가(맞춤) · 5시간 · +24,000원

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[I. 근무지 합산 표시]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MVP (출시 필수):
  동일 수당 계열 합산 표시
  예: 연장수당 총액 (기본+맞춤 합산)

상세 breakdown (출시 후):
  연장수당
    기본 50%추가: +40,000원
    맞춤 30%추가: +24,000원

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J. 행 구조 확정]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
단일가산: singlePremiumRows[] 배열 (3행)
          1행 기본표시 / 2,3행 숨김
          map() 한 번으로 렌더링
이중가산: doublePremiumRow 단일 행 (추가버튼 없음)
삼중가산: triplePremiumRow 단일 행 (고정)
맞춤가산: customPremiumRows[] 배열 (3행)
          1행 기본표시 / 2,3행 숨김

행 타입 정의:
type SinglePremiumRow = {
  id                      // 행 식별자
  isSingleRowVisible      // 행 표시 여부
  selectedSingleAllowance // 선택수당 (연장/야간/휴일)
  premiumRate             // 가산율
  premiumHours            // 가산시간 (입력값만 저장)
  isSingleRowCompleted    // 입력완료 여부
}

type DoublePremiumRow = {
  id              // 행 식별자
  allowanceCombo  // 수당조합 (연장+야간 등)
  premiumHours    // 가산시간
}

type CustomPremiumRow = {
  id                       // 행 식별자
  isCustomRowVisible       // 행 표시 여부
  selectedCustomAllowances // 선택수당 (복수)
  premiumRate              // 맞춤 가산율 (직접입력)
  premiumHours             // 가산시간
  isCustomRowCompleted     // 입력완료 여부
}

⚠ premiumAmount는 state 저장 금지
  → useMemo derived value로만 계산
⚠ premiumAmount를 각 row state에 저장하지 않는다.
   모든 금액은 useMemo 기반 derived value로 계산한다.
   (row.premiumAmount 형태로 저장 시 이중 진실 버그 발생)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J-1. 실시간 계산 원칙 — derived value]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
한 줄 원칙:
"입력은 state, 결과는 useMemo. 예외 없음."

state 저장 (입력값만):
  premiumHours            가산시간
  premiumRate             가산율
  selectedSingleAllowance 선택수당
  singlePremiumRows[]     행 배열
  expandedRowId           펼침행 확인번호
  isSingleRowCompleted    완료여부
  isCustomRowCompleted    완료여부

useMemo 계산 (저장 금지):
  premiumAmount     = premiumHours × wage × premiumRate
  totalPremium      = Σ premiumAmount
  adjustedGrossPay  = base + totalPremium
  adjustedNetPay    = 세금 재계산
  요약 라벨

isCompleted 판단 기준 (v12.0 확정):

  isSingleRowCompleted:
    selectedSingleAllowance !== null
    AND premiumHours !== null
    AND premiumHours > 0
    AND premiumHours <= totalWorkHours

  isCustomRowCompleted:
    selectedCustomAllowances.length > 0
    AND premiumRate !== null AND premiumRate > 0
    AND premiumHours !== null AND premiumHours > 0
    AND premiumHours <= totalWorkHours

  ⚠ 오류 상태(가산시간 초과)에서
    completed = false 자동 유지
    추가버튼 비활성 유지

캘디게 정합성:
  result 레벨 게이트 1회 적용 (이미 적용됨)
  별도 게이트 추가 금지
  이중 진실(dual source of truth) 원천 차단

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J-2. 초기화 규칙]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
삭제 버튼 없음 → 가산유형 전체 초기화로 대체

단일가산 초기화 (resetSinglePremiumRows):
  singlePremiumRows[] → initialPremiumRowState 전체 복원
  1행만 표시 / 2,3행 숨김 / 모든 입력값 null

맞춤가산 초기화 (resetCustomPremiumRows):
  customPremiumRows[] 동일 방식

UI:
  [단일가산 초기화] 버튼 — 단일가산 영역 하단
  [맞춤가산 초기화] 버튼 — 맞춤가산 영역 하단

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J-3. Intersection Observer 명세]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
인라인 안내 발동 기준:
  threshold: 0.3 (화면 30% 이상 노출 시)
  once: true (최초 1회만)
  mobile viewport 기준

[내부변수] inlineGuideShownOnce
  false: 미표시 → 발동
  true:  이미 표시됨 → 발동 안 함

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J-4. 코딩 구현 단계 순서]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: 정적 UI 구현
STEP 2: 상태 연결
STEP 3: 실시간 계산 (derived value)
STEP 4: 저장 연동
STEP 5: 추가버튼 / 초기화

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J-5. 선택 수당명 동적 반영 — 필수 구현]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
저장 데이터 구조:
  {
    type: "단일가산",
    selectedSingleAllowance: "연장",
    premiumRate: 50,
    premiumHours: 8
  }
  ⚠ premiumAmount 저장 금지 → useMemo 계산

반영 범위:
  즉시 금액 문구 → 요약 표시 →
  근무지 합산 → 급여명세 상세
  전 구간 동일 수당명 유지

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[K. 전체 확정 규칙 요약]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
① 수당 순서: 주휴→연차→연장→야간→휴일→세금·공제
② 박스 구분 없음
③ 인라인 안내: 최초 1회 / ①선택 ②3초 후 자동 축소
   threshold: 0.3 / once: true
④ 닫힘 배열: 선택 전 1줄 / 선택 후 2줄
⑤ 글로우잉: 보류 — 사용자 피드백 기반 재오픈
⑤-신규 shimmer:
  대상 1: PremiumSection 최상단 안내영역
    역할: 주의집중 → 개념 이해 유도
  대상 2: Premium 카드 STEP2 입력창 wrapper
    역할: 개념 이해 → 행동 연결
    ※ 실제 시간 입력 input element의 wrapper만 적용
       STEP2 전체 영역 shimmer 금지
  방식: 좌→우 빛 sweep / subtle stagger
  순서: 안내영역 shimmer 시작 →
        250~400ms delay →
        STEP2 입력영역 shimmer 이어짐
  설계 의도: 사용자가 "설명 → 실제 입력 위치"로
             자연스럽게 attention handoff 되도록 구성
  ※ delay 너무 짧으면 동시 shimmer처럼 보임 — 금지
  ※ delay 너무 길면 UX가 느리다고 느껴짐 — 금지
  반복: 3회 후 완전 정지 (infinite 금지)
  시작: 해당 카드 펼쳐진 순간
  종료: 입력 완료 / collapse / 다른 카드 전환
⑥ 수당 안내문구: 직관형 단문 3종
⑦ 즉시 금액 + 수당명 동적 반영 안내문구
⑧ 추가버튼: 단일가산 / 맞춤가산 각각 보유
   목업 보류 / Replit 단계 직접 구현
⑨ 선택 후 해당 버튼만 표시 (비선택 제거)
⑩ 가산율 표기: %추가 통일 / 0.5식 금지
⑪ 요약: 수당명 앞 / 가산율 보조 / 연장→야간→휴일 순
⑫ 맞춤가산: 기존 수당 확장 / 복수선택 / 자동명칭
   (맞춤) 표기 유지
⑬ 근무지 합산: MVP 요약 합산 / 상세 출시 후
⑭ 선택 수당명 전 구간 동적 반영 필수
⑮ 추가버튼 문구: "동일 가산율의 다른 수당을 추가합니다"
⑯ 열림 1개 유지 (expandedRowId)
⑰ 선택 버튼: 선택 후 해당만 표시
⑱ 추가 생성 행: 독립 상태/입력/계산/요약
⑲ 실시간 계산: 입력은 state / 결과는 useMemo
⑳ 삭제 없음 → 가산유형 전체 초기화 대체
㉑ 이중/삼중: 1행 고정 / 추가버튼 없음

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[L. 추가 버튼 규칙]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
버튼 문구:
  "동일 가산율의 다른 수당을 추가합니다"
목업 구현: 보류
실제 구현: Replit 단계에서 목업 없이 직접 구현

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[M. 동시 펼침 규칙]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
열림 1개 유지 원칙:
  새 가산행 열리면 → 기존 펼침 자동 접힘
  이유:
    모바일 공간 절약 / 입력 집중 유지
    상태 꼬임 감소 / 글로우잉 상태 단순화

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[N. 수당 선택 버튼 상태 표시]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
단일/이중/삼중가산:
  선택 전: [연장]  [야간]  [휴일]
  선택 후: 선택된 버튼만 표시 (비선택 제거)
  목적: 닫힘/재열림 시에도 현재 선택 수당 즉시 인지

맞춤가산 (복수선택 / v12.0 확정):
  선택 후 선택된 버튼 유지 (A안)
  비선택 버튼 유지 (재탭으로 개별 해제 가능)
  재탭: 허용 (수당 선택만 개별 해제)
  전체 초기화: 유지 (행 전체 리셋)

  비활성 표시 구분:
    미선택 (선택 가능):
      기본 버튼 / 근무요일 탭과 동일 패턴
    타 행/유형 사용 중 (임시 불가):
      버튼 형태 유지 + opacity 감소 + disabled
      취소선 없음 (해제 시 복귀 가능)
      (구현 참조값: opacity 0.4~0.5 / 정적 UI 후 확정)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[O. 추가 생성된 가산행 규칙]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
① 독립 상태 유지
② 독립 입력 유지
③ 독립 금액 계산
④ 독립 요약 표시
⑤ 선택 수당 중복 불가 (v12.0 확정)

  근거: 동일 수당의 이중계산 방지
        정형↔맞춤은 대체관계 / 누적 적용 불가
        한 근무지 기준 검산 구조

  적용 대상 (사용자 선택이 발생하는 가산행):
    단일가산 행 간
    맞춤가산 행 간
    단일↔맞춤 간

  비적용 대상 (선택 자유 없음):
    이중가산 (조합 고정)
    삼중가산 (고정)

⑥ 기존 가산행 상태 유지
   새 행 추가 시 이전 입력값 변경 없음

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[P. 가산시간 검증 정책] (v12.0 신규)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
검증 조건:
  premiumHours > totalWorkHours

오류 시 처리:
  입력값 유지 (빈값 강제 초기화 금지)
  오류 표시 (빨간 테두리 + 안내문구)
  안내문구:
    "가산시간은 총 근무시간(N시간)을
     초과할 수 없습니다."
  premiumAmount 계산 차단
  isCompleted = false
  추가버튼 비활성 유지

정상 범위:
  사전 안내 없음 / 즉시 계산 수행

입력란 컨텍스트 문구 (고정):
  "총 근무시간 [N시간] 안에 포함된,
   가산금액이 반영되어야 할 시간을
   입력하세요."
  N = totalWorkHours 동적 반영
  §19 C 기존 문구 재사용 / 별도 설계 없음

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
버전 관리 현황
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
v8.0  | 2026-05-04 | 주휴수당 계산 엔진 + UI 구조 확정
v9.0  | 2026-05-09 | v8.0 + v8.x 추가분 통합
v9.1  | 2026-05-11 | 작업리스트 운영 규칙 / C안 완료 / 파트너 AI 명칭
v10.0 | 2026-05-11 | v9.0 + v9.1 통합 / 캘디게 명문화 / 작업 우선순위 확정
v10.1 | 2026-05-15 | §6 제수당 구조 B 확정 / §17 글로벌 전략 / §18 기록보기
                   | §19 가산율 기반 제수당 UI 목업 스펙 (A~O)
v11.0 | 2026-05-16 | §1.4.2 한·영 병기 용어 3구분 도표 완성
                   | §19 J~K 전체 반영 / 변수명 전체 확정
v12.0 | 2026-05-18 | §1.6-4 작업 진행 흐름 규칙 신규
                   | §1.11 GPT 전용 섹션 분리
                   | §19 B/F/J/N/O/P 보완 확정
v13.0 | 2026-05-18 | STEP 1~3 골조/상태/derived 구현 완료
                   | §1.6-4 권장 흐름 + 파트너 검토 기준 MODE A/B 추가
                   | §1.10 JSX/TSX fenced block 규칙 추가
                   | §1.11 GPT 전용 작업 흐름 5가지 추가
                   | §1.12 단계별 구현 경계 원칙 신규
                   |   (골조 구현 용어 / useMemo deps 체크리스트)
                   | usePremium hook 설계 확정
                   | PART 2 인수인계 전면 업데이트
v13.1 | 2026-05-18 | 절대 규칙 — 현재 STEP 범위 외 구조 변경 금지 추가
                   | §1.6-4 — 멈춤 금지 예외 조건 추가
                   | §1.10 — 위치 anchor 강제 추가
                   | §1.11 — 구조 오해 방지 추가 (GPT 전용)
                   | §1.12 — 리팩토링≠기능추가 / 한STEP=한변경 / presentation기준
                   |          동작동일성검증 / 골조완료정의 / setState제한 / race트리거
                   | §1.13 — 신규: Derived Owner 승격 / Hook 추출 증분 / 실제 식별자 기준
작업리스트 v13.1
2026-05-18 기준
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

대기 A: 작업리스트 전체 재조정
  - 필요/대기/폐기 3분류 업데이트
  - 확인 액션 4건:
    1. Agent: P3 juhu row 현재 구현 상태 → 폐기 확인됨 ✅
    2. Agent: P7 annualPay 현재 구현 상태 확인 필요
    3. 직전 쓰레드: P4 UI-A~K 개별 정의 확인 필요
    4. Jin님: P6 검증 체크리스트 성격 확인 필요

대기 B: §18 저장/즐겨찾기 시스템 현황 반영
  - 18-C 신규 섹션 추가
  - 구현 완료 / 미구현 / 보류 / 확정 철학 기록

대기 C: §6.7 P8 holidayHours 현황 + P8-3 정의
  - P8-2 완료 기록
  - P8-3 float drift 정의 및 사용자 피드백 예상 추가

대기 D: P9 재작업 결과 반영
  - PremiumRateCard.tsx — orphan 확인, 삭제 결정 필요
  - NightPayCard.tsx — orphan 확인, 보존/삭제 결정 필요
  - 제수당 설정 버튼 (Home.tsx:402) — 보존/제거 결정 필요

대기 E: §19 변경분 반영
  → 이번 쓰레드에서 직접 매뉴얼 반영 완료 ✅

대기 F: §1.6-4 또는 §1.11
  프롬 검토 시 자동 확인 항목 추가:
  - 기존 구현 충돌 여부
  - 선행 조건 존재 여부
  - 임시 코드 잔재 여부
  적용 범위: 코드 수정 포함 프롬만
             분석/감사 전용 STEP은 제외
