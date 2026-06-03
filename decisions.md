# 파트너 협의 결정사항

## 맞춤가산 정체성 (2606031200)

### 확정
- 맞춤가산 = 가산분 (법정가산의 커스텀 버전)
- 5인 미만 사업장에서 맞춤가산도 0 처리 (표준가산과 동일 게이팅)
- 맞춤가산 계산: 각 행별 hours × wage × rate 후 Math.floor() 1회, 행별 결과 합산
- 맞춤가산 저장 원칙: floor된 금액이 아닌 원본 입력값(hours/rate/선택정보) 기준으로 저장·복원. customPay는 항상 재계산되는 파생값으로만 취급

### 향후 확장 방향
- 위험수당/약정수당 등 별도수당 필요 발생 시 → 별도 기능으로 추가 (맞춤가산과 분리)
- 현 단계에서 맞춤가산에 별도수당 개념 혼입 안 함

### 근거
- selectedCustomAllowances = overtime/night/holiday → 맞춤은 가산의 커스텀 버전
- Premium 전체 = 가산분 계산기 (기본급 아님)
- 현재 코드 구조와의 일관성 우선

---

## R1 결합가산 처리 방향 확정 (2606031200)

### 확정
- 표준가산(연장/야간/휴일)은 0.5 고정
- 표준가산으로 표현되지 않는 특수 가산율은 맞춤가산으로 처리
- 이중/삼중은 UI상 결합 입력, 내부에서는 선택된 수당 각각 같은 시간으로 분해
  예: 연장+야간 3시간 → 연장 3시간 + 야간 3시간
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

---

## 기존 잠복 버그 — History reload 복원 누락 (2606031200)

### 확인된 버그 9종 → 수정 완료 (커밋 3a45e36)
- overtimeHoursManual / includeDeductions
- prevWeek / attendanceByWeek
- includeAnnual / annualLeaveMode / annualLeaveMonths / annualLeaveRemaining / annualLeaveAttendance

### 원인
- loadState가 부분병합 방식({...prev, ...s}) → 복원부에 명시 안 된 키는 직전 state가 유지됨
- 저장은 {...state} 전체 자동, 복원은 수동 화이트리스트 → 새 필드 추가 시 복원부 명시 필수

### 주의
- 맞춤가산 state를 CalcState에 편입할 때 복원부(Home :206–233)에 맞춤 키 명시 추가 필수
- 미추가 시 동일 버그 재현됨
