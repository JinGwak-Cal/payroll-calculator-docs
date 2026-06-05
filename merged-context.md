<!-- Auto-generated merged-context.md. NOT Source of Truth. 원본 충돌 시 absolute-rules > current-step > decisions 우선. -->

<!-- ===== absolute-rules.md ===== -->
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
Claude 검토 저장: reviews/active/claude/
GPT 검토 저장: reviews/active/gpt/
완료 작업 이동: reviews/completed/

index.md에는 reviews 전문 미포함
reviews는 필요 시 bash_tool로 직접 참조
# reviews 식별자 규칙
형식: 작업단위(sub.n).파트너명.현업N-n.md

작업단위: P4, G3, UX 등
sub.n: 서브작업 번호 (독립)
현업N: 서브작업 내 현업 번호 (독립)
n: 팔로업 순서 (1씩 증가)

예시:
P4(1).claude.현업1-1.md   ← 서브1, 현업1, Claude 1차
P4(1).gpt.현업1-2.md      ← 서브1, 현업1, GPT 팔로업
P4(1).claude.현업1-3.md   ← 서브1, 현업1, Claude 재반영
P4(1).claude.현업2-1.md   ← 서브1, 현업2 (다른 현업)
P4(2).claude.현업1-1.md   ← 서브2, 현업1
# reviews 식별자 규칙 (확정)
형식: 작업단위(sub.n).파트너명.현업N-n.YYMMDDHHmm.md
총 12자리 날짜시간: 년2자+월2자+일2자+시2자+분2자

예시:
P4(1).claude.현업1-1.2605281430.md
P4(1).gpt.현업1-2.2605281510.md
P4(1).claude.현업1-3.2605281545.md
P4(1).claude.현업2-1.2605281600.md
P4(2).claude.현업1-1.2605281700.md

# reviews 목록 출력 규칙
- 최신 파일이 항상 맨 위에 표시
- 날짜시간 기준 내림차순 정렬
- Claude가 목록 출력 시 자동 적용
# GitHub 문서 접근 우회 규칙
1. raw.githubusercontent.com URL 접근 실패 시 즉시 실패로 판단하지 않는다.
2. 같은 경로의 github.com/.../blob/main/... URL로 재시도한다.
3. GitHub blob Preview 또는 Raw 링크 확인까지 시도한다.
4. 그래도 실패할 때만 "미확보"로 보고한다.
# reviews 목록 출력 형식 (필수)
Claude가 reviews 파일 목록 출력 시 반드시 raw + blob URL 동시 표시:

파일명 (크기)
raw: https://raw.githubusercontent.com/jingwak-maker/payroll-calculator-docs/main/[경로]
blob: https://github.com/jingwak-maker/payroll-calculator-docs/blob/main/[경로]

이유: GPT는 blob URL 생성은 가능하지만 raw 실패 시 자동 전환이 보장되지 않음
따라서 GitHub 문서 전달 시 raw + blob URL을 함께 제공
Jin님이 두 URL 중 작동하는 것을 GPT에 전달
# 저장 후 검증 규칙
reviews 파일 저장 후 반드시:
1. 저장된 파일 내용 실제 읽기
2. 원본 내용과 비교
3. 누락 없음 확인 후 완료 보고
누락 발견 시 즉시 재저장
# 답변 정직성 규칙
사용자가 원하는 답을 예측하여 그 방향으로 답하는 것을 금지한다.
틀린 것을 알면서 정정하지 않는 것을 금지한다.
확실하지 않으면 즉시 "불확실"을 먼저 선언한다.
# 협업 운영 규칙 v1

## §운영-1 자동 판단 금지 (핵심 원칙)
명시적으로 요청되지 않은 행위를 금지한다.
- 보고=보고 / 조사=조사 / 검토=검토
- 생성·저장·업데이트는 명시적으로 요청된 경우에만 수행한다.

## §운영-2 승인 원칙
다음 행위는 반드시 Jin님 승인 후 진행한다.
- 파일 생성 / 삭제 / 덮어쓰기
- 보고용 문서 생성
- 커밋 / GitHub push / 원격 미러 업데이트
- current-step.md 수정 / decisions 수정 / absolute-rules 수정

## §운영-3 읽기 전용 원칙
다음 표현은 모두 읽기 전용 요청으로 간주한다.
읽어줘 / 확인해줘 / 검토해줘 / 평가해줘 / 조사해줘 / 보고해줘
위 요청 시: 수정·생성·삭제·커밋·push 모두 금지

## §운영-4 생성 승인 원칙
다음 표현이 있을 때만 생성 행위를 허용한다.
생성해 / 작성해 / 저장해 / 등록해 / 업데이트해 / 반영해
위 표현이 없으면 생성 행위 금지
읽기 전용 표현 + 생성 표현이 동시 존재 시 생성 표현 우선

## §운영-5 덮어쓰기 원칙
기존 파일이 존재할 경우 자동 덮어쓰기를 금지한다.
반드시 다음 중 하나를 사용자에게 확인받는다: 신규 파일 생성 / 기존 파일 업데이트 / 작업 중단
승인 응답을 받기 전까지 해당 파일에 대한 모든 작업을 중단한다.

## §운영-6 GitHub 원칙
commit / push / 파일 생성·수정·삭제 / 원격 미러 업데이트
모두 명시적 승인 후 진행

## §운영-7 자동 커밋 원칙
사전 보고 가능 시 사전 보고. 불가능한 경우 발생 즉시 보고.
보고 항목: 커밋 해시 / 변경 파일 / 변경 내용 요약

## §운영-8 특별 관리 문서
current-step.md / decisions / absolute-rules
생성·수정·삭제 모두 승인 필수

## §운영-9 범위 초과 원칙
작업 지시 범위 외 파일(.replit / index.css 전역 / 환경설정 등) 수정 금지
필요 시 사전 보고 후 승인

## §운영-10 계산 로직 특별 규칙
calc-engine.ts / use-calc.tsx / 계산 결과에 직접 영향을 주는 파일
수정 전 반드시: 변경 필요성 보고 → 영향 범위 보고 → 승인 획득


<!-- ===== current-step.md ===== -->
# 현재 작업 단계

## 최근 완료 (앱 개발)

* BUG-1: History reload 누락 9필드 복원 수정 ✅ (커밋 3a45e36)
* ResultGrid 표준가산율 선택 UI 제거 ✅ (커밋 a3f4e0d)
* floor 정책: use-premium.tsx 4곳 Math.floor() ✅
* Phase 2-1-A: CalcState customPremiumRows 편입 ✅
* Phase 2-1-B: handleHistoryReload 복원 추가 ✅
* Phase 2-1-D: use-premium → CalcState 연결 ✅
* Phase 2-1 reload E2E 검증 통과 ✅
* Phase 2-1-C: customPay grossPay 연결 ✅
  → custom-premium.ts 신규 / calc-engine CalcInput.customPay / use-calc 주입
* Phase 2-2/2-3: B single/double/triple 제거 + adjustedGrossPay 제거 ✅
  → totalPremium = customPremiumTotal만 유지
  → orphan 카드 파일 3개(Single/Double/TriplePremiumCard) 삭제 보류
* Phase 2-4: 공식 종료 ✅ (칩 토글 이미 구현됨 / 잔여는 2-6 이관)
* Phase 2-7: PremiumSection 화면 분리 ✅
  → PremiumScreen.tsx 신규
  → Screen 타입 "premium" 추가
  → Home 인라인 렌더 제거

## 최근 완료 (워크플로우 개선)

* 문제 진단 완료: 최신 문서 LLM 자동 주입 부재
* Fine-grained 토큰 3개 발급 완료
  → GITHUB_APP_TOKEN (replit-app-write)
  → GITHUB_DOCS_READ_TOKEN (docs-read)
  → GITHUB_DOCS_WRITE_TOKEN (PayRollCalculator 재활용)
* Replit Secrets 저장 완료
* archive/ 폴더 생성 완료
* index.md 통합 개편 완료
* decisions.md 최신화 완료
* merged-context.md 생성 완료

## 다음 작업 ← 현재

1. current-step.md / decisions.md GitHub 반영
2. merged-context.md GitHub 반영
3. GitHub Actions 설계 및 구현

## Phase 2 대기 (앱 개발)

※ 2-5/2-6은 고위험 모델 작업이므로 2-7/2-8 이후로 순서 재조정됨
2-8. 인라인 제거 확인 및 잔여 정리
2-5. 근무내역 단위 (고위험 — 별도 설계 보고 후)
2-6. 조합 자동 해석 (2-5 확정 후)

## 워크플로우 개선 단계 대기

### 2단계 (단기)

* current-step + decisions 자동 병합 스크립트
* GitHub Actions 검증

### 3단계 (중기)

* 중앙 Context Builder
* LLM 결과 자동 검증

<!-- ===== decisions.md ===== -->
# 파트너 협의 결정사항

## 맞춤가산 정체성 (2606031200)
### 확정
- 맞춤가산 = 가산분 (법정가산의 커스텀 버전)
- 5인 미만 사업장에서 맞춤가산도 0 처리 (표준가산과 동일 게이팅)
- 맞춤가산 계산: 각 행별 hours × wage × rate 후 Math.floor() 1회, 행별 결과 합산
- 맞춤가산 저장 원칙: floor된 금액이 아닌 원본 입력값(hours/rate/선택정보) 기준으로 저장·복원. customPay는 항상 재계산되는 파생값으로만 취급
### 향후 확장 방향
- 위험수당/약정수당 등 별도수당 필요 발생 시 → 별도 기능으로 추가 (맞춤가산과 분리)

## R1 결합가산 처리 방향 확정 (2606031200)
### 확정
- 표준가산(연장/야간/휴일)은 0.5 고정
- 표준가산으로 표현되지 않는 특수 가산율은 맞춤가산으로 처리
- 이중/삼중은 UI상 결합 입력, 내부에서는 선택된 수당 각각 같은 시간으로 분해
- 표준가산은 각 0.5 고정 (연장+야간 = 1.0 / 연장+야간+휴일 = 1.5)
- 5인미만 ON 시 A 게이팅에 의해 자동 0 처리
- 표준가산 진실원천 = 시스템 A (실수령 반영 경로)
- B(Premium)는 계산 진실원천이 아닌 입력 UI / 제거 대상
- UI 프리셋: ResultGrid의 0.5/1.0/1.5 버튼 제거 → "표준가산 50% 고정 · 특수율은 맞춤가산 사용" 정적 안내로 대체 (커밋 a3f4e0d)
### floor 정책 확정
- Premium 가산 row별 최종값에 Math.floor() 1회 적용 후 합산
- 적용 범위: Premium 단일/이중/삼중/맞춤 row에만
- 기본급/주휴/연차/세금·공제는 기존 계산 방식 유지
### state 처리
- nightPremiumRate·overtimePremiumRate·holidayPremiumRate state 유지 (UI만 고정)
- 저장/복원 구조 무변경

## 기존 잠복 버그 — History reload 복원 누락 (2606031200)
### 확인된 버그 9종 → 수정 완료 (커밋 3a45e36)
- overtimeHoursManual / includeDeductions
- prevWeek / attendanceByWeek
- includeAnnual / annualLeaveMode / annualLeaveMonths / annualLeaveRemaining / annualLeaveAttendance
### 주의
- 맞춤가산 state를 CalcState에 편입할 때 복원부(Home :206–233)에 맞춤 키 명시 추가 필수
- 미추가 시 동일 버그 재현됨

## Phase 2-4 공식 종료 + 2-4~2-8 순서 재확정 (2606041200)
### 확정
- 2-4(칩 토글 입력기) 공식 종료
  → 칩 토글은 이미 CustomPremiumCard STEP1에 구현되어 있음
  → 잔여(안내문 [N시간] 동적화)는 2-6으로 이관
- orphan 카드 파일 3개(SinglePremiumCard/DoublePremiumCard/TriplePremiumCard) 삭제 보류
  → 별도 정리 작업으로 분리
### 재확정된 작업 순서
1. 2-7 화면 분리 (저위험 — PremiumSection 무상태 구조)
2. 2-8 인라인 제거 (2-7 완료 후)
3. 2-5 근무내역 단위 (고위험 — 별도 설계 보고 후 진행)
   → customPremiumRows 영속·계산·history reload 연쇄 영향
4. 2-6 조합 자동 해석 (2-5 확정 후)
   → 자동요율 vs STEP2 수동입력 우선순위 정책 결정 선행 필요
### 근거
- PremiumSection 무상태(presentational) 구조 확인
- 2-5 모델 변경은 customPremiumRows/저장복원/계산공식/history reload 동시 영향 고위험
- 저위험 작업으로 표면 정리 후 고위험 진행

## 워크플로우 개선 처방 우선순위 확정 (2606041200)
### 진단
- 핵심 문제: 최신 문서가 LLM에 강제로 주입되지 않는 것
- LLM 성능 부족이 아닌 문서 자동 주입 부재에서 발생

### 1단계 (무료, 즉시)
1. Archive 폴더 구축 — 구문서 오염 방지
2. index.md 우선순위 명시 — GPT/Claude/Replit 동일 기준
3. 프롬프트 제약 강화 — current-step 확보 전 추정 금지

### 2단계 (거의 무료, 단기)
4. current-step + decisions 자동 병합 스크립트
5. GitHub Actions 검증

### 3단계 (중기)
6. 중앙 Context Builder
7. LLM 결과 자동 검증

### 토큰 운영 정책
- Claude 토큰 운용은 별도 검토 중
- Replit: Secrets에 토큰 저장 → 상시 사용
- 브랜치 보호 규칙으로 독단 커밋 방지
- main 직접 푸시 금지 / PR 필수 / Jin님 승인 후 병합
- payroll-calculator-docs 수정은 Jin님 승인 및 PR 절차를 통해서만 허용

## 워크플로우 개선 추가 확정사항 (2606051200)

### 문서 체계 확정

* Source of Truth = absolute-rules / current-step / decisions
* merged-context.md = 파생/캐시 문서 (Source of Truth 아님)
* merged-context 충돌 시 원본 문서 우선
* index.md = 안내/진입점 역할만 (Source of Truth 아님)
* manual-v14 = archive 이동 금지 / 우선순위 하향 유지
* archive/ = 과거 기록 보관용 / 현재 판단 근거 사용 금지

### GPT 표준 컨텍스트 확정

* GPT raw/jsdelivr/blob URL 접근 반복 실패 확인
* GPT 표준 진입 방식 = merged-context.md
* merged-context.md도 URL 읽기 실패 가능성 있음
* 최후 수단 = Jin님 직접 복붙
* GitHub Actions는 GPT 읽기 문제 해결책 아님
  → 문서 동기화·검증·자동화 인프라 역할

### GitHub Actions 우선순위 확정

* 협업 자동화 관점에서 높은 우선순위
* 역할: merged-context 자동 생성 / index 검증 / 불일치 경고
* GPT 읽기 문제와 별개

### 토큰 운영 정책

* Replit: Secrets에 3개 토큰 저장 완료
  → GITHUB_APP_TOKEN
  → GITHUB_DOCS_READ_TOKEN
  → GITHUB_DOCS_WRITE_TOKEN
* Claude 토큰 운용은 별도 검토
* 대화창 토큰 노출은 원칙적으로 지양
* 인프라 완성 후: Replit이 GitHub 쓰기 담당 / Claude는 검토 중심
* main 직접 푸시 금지 / PR 필수 / Jin님 승인 후 병합

### Replit 운영 규칙 확정

* 승인 없는 자동 커밋 금지
* 범위 외 파일 수정 금지
* payroll-calculator-docs 직접 수정 금지
* 토큰 값 출력/노출 금지
* 작업 시작 전 absolute-rules / current-step / decisions 확인 필수

### 문서 책임 정의

index.md

* 프로젝트 진입점
* 운영 규칙
* 문서 우선순위
* 작업 시작 프로토콜

absolute-rules.md

* 절대 규칙

current-step.md

* 현재 작업 상태
* 다음 작업
* 완료 작업
* 대기 작업

decisions.md

* 확정 결정사항
* 정책
* 우선순위 결정

merged-context.md

* absolute-rules
* current-step
* decisions 자동 병합본
* Source of Truth 아님

### 향후 검토 사항 (TODO)
- 운영 규칙 v1의 absolute-rules.md 이관 여부 검토
