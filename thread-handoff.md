# 스레드 이관 문서 — 2026.06.03

새 스레드에서 이 문서를 읽고 이어서 작업할 것.

---

## 1. 프로젝트 개요

앱: 알바 급여 계산기 (payroll-calculator)
개발 환경: Replit (artifacts/salary-calculator)
문서 저장소: GitHub (JinGwak-Cal/payroll-calculator-docs)
협업 구조: Jin님(의사결정) + Claude(문서/검토/GitHub) + GPT(파트너 검토) + Replit(코드 구현)
GitHub 토큰: Jin님 보관 (Fine-grained, payroll-calculator-docs 전용, Contents Read/Write만)
앱 코드(payroll-calculator) 접근 불가 — 앱 코드 확인은 Replit에 요청

---

## 2. 협업 운영 규칙 v1

§운영-1 자동 판단 금지 — 명시적으로 요청되지 않은 행위 금지
§운영-2 승인 원칙 — 파일 생성/삭제/덮어쓰기/커밋/push 모두 Jin님 승인 필요
§운영-3 읽기 전용 원칙 — 읽어줘/확인해줘/검토해줘 = 읽기 전용
§운영-4 생성 승인 원칙 — 생성해/작성해/저장해 표현 있을 때만 생성 허용
§운영-5 덮어쓰기 원칙 — 기존 파일 존재 시 승인 전까지 모든 작업 중단
§운영-6 GitHub 원칙 — commit/push/생성/수정/삭제 모두 명시적 승인
§운영-7 자동 커밋 원칙 — 사전 보고 가능 시 사전 보고, 불가 시 즉시 보고
§운영-8 특별 관리 문서 — current-step.md / decisions.md / absolute-rules.md 승인 필수
§운영-9 범위 초과 원칙 — 작업 범위 외 파일 수정 금지
§운영-10 계산 로직 특별 규칙 — calc-engine.ts / use-calc.tsx 수정 전 반드시 보고→승인

Replit 지시문 상단 고정:
[권한 제한]
수정 금지라고 하면 파일 생성/삭제/덮어쓰기/커밋/push 모두 금지입니다.
보고용 문서 생성도 명시적 승인 없이는 금지입니다.
기존 파일 덮어쓰기 금지. GitHub push 금지.
원격 미러 업데이트 금지. 자동 커밋 발생 시 즉시 보고.

---

## 3. 최근 완료 작업

- Phase 1 계산 엔진 정비 ✅
- S-1~S-1-4 주휴 관련 버그/구조 정리 ✅
- UI-Audit 01~04 ✅
- Premium 재설계 구조 확정 ✅ (절충안 대안4)
- BUG-1: History reload 누락 9필드 복원 수정 ✅ (커밋 3a45e36)
- ResultGrid 표준가산율 선택 UI 제거 ✅ (커밋 a3f4e0d)

---

## 4. 확정된 설계 방향

### 구조
- 절충안(대안4): 표준 3종은 기존 A Total 슬롯 유지 + 맞춤만 독립 가산 모듈로 분리
- 표준가산 진실원천 = 시스템 A / B(Premium) = 입력 UI 또는 제거 대상

### 표준가산
- 연장/야간/휴일 = 0.5 고정 / 특수 가산율 → 맞춤가산
- 이중/삼중: UI상 결합 입력, 내부에서 선택 수당별 동일시간 분해
- 5인미만 ON 시 A 게이팅으로 자동 0

### 맞춤가산
- 맞춤 = 가산분, 5인미만 = 0
- 저장: 원본 입력값 기준, customPay는 파생값
- 향후 위험수당/약정수당 → 별도 기능으로 분리

### floor 정책
- Premium row별 최종값 Math.floor() 1회 후 합산 (Premium에만 적용)

### 저장/복원 원칙
- CalcState에 새 필드 추가 시 handleHistoryReload 복원부(Home :206-233)에 반드시 동시 추가
- 미추가 시 BUG-1 재발

---

## 5. 현재 작업 상태

현재: Phase 2-1 착수 대기

Phase 2 대기:
2-0. B→A 매핑 설계 ✅
2-1. 맞춤 독립 모듈 구현
  ⚠️ 필수: CalcState 맞춤 필드 추가 시 복원부 동시 추가
2-2. 표준 3종 A 연결 (연장 완료, 야간/휴일 총량 경로 정리)
2-3. B totalPremium 제거
2-4~2-8. 칩 토글/근무내역/조합해석/화면분리/인라인제거

Phase 3~5 대기

---

## 6. 앱 이중 시스템

시스템 A (use-calc/calc-engine/ResultGrid) = 실수령 반영 = 진실원천
시스템 B (use-premium/PremiumSection) = 표시용 → 입력 UI로 전환/제거 예정

---

## 7. 디자인 원칙 (확정)

§원칙-0~7 확정. 색상: emerald(실수령)/red(공제)/검정·회색(나머지)/indigo(인터랙션)

---

## 8. 이 파일 관리 원칙

Claude가 세션 종료 전 항상 최신 상태로 업데이트.
새 스레드 시작 시 Claude에게 "thread-handoff.md 내용 줘"라고 하면 됨.
GPT에게는 이 파일 내용을 Jin님이 직접 붙여넣기.
