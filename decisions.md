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
