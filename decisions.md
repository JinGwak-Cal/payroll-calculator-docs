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

## R1 표준가산 가산율 구조 (2606031200)

### 확정
- 표준가산(연장/야간/휴일)은 0.5 고정 격자로 처리
- 이중(연장+야간 = 1.0) / 삼중(연장+야간+휴일 = 1.5)은 0.5 단위 분해로 A per-type 슬롯에 매핑
- 0.5 격자로 표현 안 되는 가산율은 맞춤가산으로 처리

### 전제 조건
- A의 overtimePremiumRate·nightPremiumRate·holidayPremiumRate가 모두 0.5일 때만 분해 합 일치
- 사용자가 PremiumRateCard에서 율 변경 시 이중/삼중 분해 불일치 발생 가능 → 별도 검토 필요

---

## 기존 잠복 버그 — History reload 복원 누락 (2606031200)

### 확인된 버그 3종 (맞춤 절충안과 독립 이슈)
- prevWeek: 저장은 되나 복원부(Home :206–233) 화이트리스트 누락 → reload 시 직전 state 잔존
- attendanceByWeek: 동일 — 저장되나 복원 누락 → reload 시 직전 state 잔존
- 연차 5개 필드(includeAnnual/annualLeaveMode/Months/Remaining/Attendance): 동일 → reload 시 저장된 연차값 무시, 직전 state 잔존

### 원인
- loadState가 부분병합 방식({...prev, ...s}) → 복원부에 명시 안 된 키는 직전 state가 유지됨
- 저장은 {...state} 전체 자동, 복원은 수동 화이트리스트 → 새 필드 추가 시 복원부 명시 필수

### 주의
- 맞춤가산 state를 CalcState에 편입할 때 복원부(Home :206–233)에 맞춤 키 명시 추가 필수
- 미추가 시 동일 버그 재현됨
