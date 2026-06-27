# 현재 작업 단계

---

## 구조1 전체 로드맵

Previous Product: Payroll Calculator — Development Closed (2606.26)

────────────────────────────────────────

Paycheck Workbook Roadmap

STEP 0 ✅ 완료
- 제품 철학 확정
- 제품 정의 확정
- 협업 시스템 계승
- 문서 정비
- merged-context 전환

STEP 1 ← 현재
기본근무내역 설정 (Table)
- BasicWorkDefinition Entity 설계 완료
- Information / Behavior / Presentation 설계 완료
- 현재: D-PW-008 모바일 Layout 설계 단계

STEP 2
수당근무내역 관리 (Table)
- AllowanceRecord 목록 / 추가 / 수정 / 삭제

STEP 3
Dashboard / 급여기간 요약

STEP 4
영속 저장 (localStorage / Export / Import)

STEP 5
3단 자가 검산

### 각 STEP 공통 실행 절차 (D-PW-016)
① STEP 대상 확인 (D-PW-006)
② 정보 구조 결정 (D-PW-007)
③ 화면 흐름 결정 (D-PW-009)
④ 설계 프레임워크 적용 (D-PW-008)
⑤ UI/UX 검토
⑥ 구현 프롬프트 작성
⑦ 구현
⑧ 검증 (기능·도메인·UX 포함)
⑨ 완료

---

## 구조2 현재 단계

[제품] Paycheck Workbook

[현재 STEP] STEP 1 — 기본근무내역 설정 (Table)

[목표]
BasicWorkDefinition을 기반으로
Decision Browser(Table) + Action Editor(Bottom Sheet) 구현

[범위]
- D-PW-008 모바일 Layout 설계
- Decision Browser Row 구성 (1줄/2줄/3줄 결정)
- Action Editor Bottom Sheet 구성
- 구현 프롬프트 작성

[완료 조건]
- 모바일 Layout 확정
- Replit Agent용 구현 프롬프트 완성

[다음 STEP]
STEP 2 — 수당근무내역 관리 (Table)

---

## 구조2-A 현재 STEP 확정 사항

Domain
- BasicWorkDefinition Entity (D-PW-017)

Information
- Context → Condition → Result (D-PW-019)
- Identity / Schedule / Condition / Result

Behavior
- User Intent → Behavior Contract (D-PW-020)

Presentation
- Decision Browser → List Pattern → Table (D-PW-022)
- Action Editor → Form Pattern → Bottom Sheet (D-PW-022)
- Browser Priority: P1 Identity / P2 Schedule / P3 Result (D-PW-023)
- Editor: Identity → Schedule → Condition → Result Preview

---

## 구조3 다음 작업

D-PW-008 모바일 Layout 설계 (새 쓰레드에서 시작)

첫 번째 결정:
Decision Browser의 Row Layout
→ 1줄 / 2줄 / 3줄 중 어떻게 구성할 것인가?

---

## 구조4 협업 시스템 대기

### 워크플로우 단기
- GitHub Actions 동작 검증 완료 확인 ⏳
- 자동 병합 스크립트 개선

### 워크플로우 중기
- 중앙 Context Builder 구축
- LLM 결과 자동 검증 체계 구축

### 업데이트 대기 (협업 시스템 공통)

[업데이트 대기 #2] absolute-rules.md 목차05 대기 표시 규칙 보완
[업데이트 대기 #3] absolute-rules.md 토큰절약/통과검증 확인 의무화
[업데이트 대기 #6] Replit Agent 협업 재발방지 원칙 (2626.06.25)
[업데이트 대기 #9] absolute-rules.md R17 예외 규칙 추가

---

## 구조5 보류

현재 없음

---

## 구조6 완료요약

### STEP 1 설계 완료 (2606.27)
- BasicWorkDefinition Entity 명세 확정 (D-PW-017)
- 3계층 아키텍처 확정 (D-PW-018)
- Information 인지 모델 확정 (D-PW-019)
- Behavior Contract 확정 (D-PW-020)
- Presentation Design Model 확정 (D-PW-021)
- Decision/Action Role + View 확정 (D-PW-022)
- Information Priority Model 확정 (D-PW-023)
- 설계 가설 관리 등록 (D-PW-024)

### 협업 시스템 전환 완료 (2606.26)
- Payroll Calculator → Paycheck Workbook 전환
- D-PW-000~025 확정
- current-step 3계층 분류 원칙 적용

---
