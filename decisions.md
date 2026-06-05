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
- Claude: Project Instructions에 토큰 저장 → 상시 사용
- Replit: Secrets에 토큰 저장 → 상시 사용
- 브랜치 보호 규칙으로 독단 커밋 방지
- main 직접 푸시 금지 / PR 필수 / Jin님 승인 후 병합
