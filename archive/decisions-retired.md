# decisions-retired.md
<!-- archived from decisions.md during 0611 doc revision -->

## 완료 이력

### 기존 잠복 버그 — History reload 복원 누락 (2606031200)
#### 확인된 버그 9종 → 수정 완료 (커밋 3a45e36)
- overtimeHoursManual / includeDeductions
- prevWeek / attendanceByWeek
- includeAnnual / annualLeaveMode / annualLeaveMonths / annualLeaveRemaining / annualLeaveAttendance

### Phase 2-4 공식 종료 확정 (2606041200)
- 2-4(칩 토글 입력기) 공식 종료
  → 칩 토글은 이미 CustomPremiumCard STEP1에 구현되어 있음
  → 잔여(안내문 [N시간] 동적화)는 2-6으로 이관
- orphan 카드 파일 3개(SinglePremiumCard/DoublePremiumCard/TriplePremiumCard) 삭제 보류
  → 별도 정리 작업으로 분리

### 워크플로우 개선 처방 우선순위 (2606041200)
#### 진단
- 핵심 문제: 최신 문서가 LLM에 강제로 주입되지 않는 것
- LLM 성능 부족이 아닌 문서 자동 주입 부재에서 발생
#### 1단계 (무료, 즉시) — 완료
1. Archive 폴더 구축 — 구문서 오염 방지
2. index.md 우선순위 명시 — GPT/Claude/Replit 동일 기준
3. 프롬프트 제약 강화 — current-step 확보 전 추정 금지
#### 2단계 (거의 무료, 단기) — 완료
4. current-step + decisions 자동 병합 스크립트
5. GitHub Actions 검증

### GitHub Actions 우선순위 확정 (2606051200) — 완료
- 협업 자동화 관점에서 높은 우선순위
- 역할: merged-context 자동 생성 / index 검증 / 불일치 경고
- GPT 읽기 문제와 별개

### GitHub Actions 자동화 구축 완료 (2606062200)
- GitHub App (Jin-Docs-Automation) 생성 및 JinGwak-Cal 조직에 설치
- JinGwak-Cal 조직으로 저장소 이전 완료
- Ruleset Bypass actor 설정 완료
- merged-context.md 자동 재생성 동작 확인 ✅
- 1차 A안(bot bypass) 안정화 완료
- 2차 전환 검토: 운영 안정화 후 재검토

## 폐기 항목

### 향후 검토 사항 (2606051200) — 폐기
- 운영 규칙 v1의 absolute-rules.md 이관 여부 검토
  → 0611 개편에서 실제 이관 작업 진행으로 별도 기록 불필요
