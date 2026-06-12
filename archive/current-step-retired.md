# current-step-retired.md
<!-- archived from current-step.md during 0612 doc revision -->

## 완료 이력

### 앱개발 완료 상세
- BUG-1: History reload 누락 9필드 복원 수정 ✅ (커밋 3a45e36)
- ResultGrid 표준가산율 선택 UI 제거 ✅ (커밋 a3f4e0d)
- floor 정책: use-premium.tsx 4곳 Math.floor() ✅
- Phase 2-1-A: CalcState customPremiumRows 편입 ✅
- Phase 2-1-B: handleHistoryReload 복원 추가 ✅
- Phase 2-1-C: customPay grossPay 연결 ✅
  → custom-premium.ts 신규 / calc-engine CalcInput.customPay / use-calc 주입
- Phase 2-1-D: use-premium → CalcState 연결 ✅
- Phase 2-1 reload E2E 검증 통과 ✅
- Phase 2-2/2-3: B single/double/triple 제거 + adjustedGrossPay 제거 ✅
  → totalPremium = customPremiumTotal만 유지
  → orphan 카드 파일 3개(Single/Double/TriplePremiumCard) 삭제 보류
- Phase 2-4: 공식 종료 ✅ (칩 토글 이미 구현됨 / 잔여는 2-6 이관)
- Phase 2-7: PremiumSection 화면 분리 ✅
  → PremiumScreen.tsx 신규
  → Screen 타입 "premium" 추가
  → Home 인라인 렌더 제거

### 워크플로우 완료 상세
- 문제 진단 완료: 최신 문서 LLM 자동 주입 부재
- Fine-grained 토큰 3개 발급 완료
  → GITHUB_APP_TOKEN (replit-app-write)
  → GITHUB_DOCS_READ_TOKEN (docs-read)
  → GITHUB_DOCS_WRITE_TOKEN (PayRollCalculator 재활용)
- Replit Secrets 저장 완료
- archive/ 폴더 생성 완료
- index.md 통합 개편 완료
- decisions.md 최신화 완료
- merged-context.md 생성 완료
- GitHub App (Jin-Docs-Automation) 구축 완료
- GitHub Actions workflow_dispatch 추가 완료
- merge_docs.py 검증 조건 업데이트 완료

### 워크플로우 대기 → 완료 이동
- current-step + decisions 자동 병합 스크립트 ✅
- GitHub Actions 구축 완료 ✅
- GitHub Actions 동작 검증 완료 ✅
