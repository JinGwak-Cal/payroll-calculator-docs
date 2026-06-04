# 현재 작업 단계

## 최근 완료
- BUG-1: History reload 누락 9필드 복원 수정 ✅ (커밋 3a45e36)
- ResultGrid 표준가산율 선택 UI 제거 ✅ (커밋 a3f4e0d)
- floor 정책: use-premium.tsx 4곳 Math.floor() ✅
- Phase 2-1-A: CalcState customPremiumRows 편입 ✅
- Phase 2-1-B: handleHistoryReload 복원 추가 ✅
- Phase 2-1-D: use-premium → CalcState 연결 ✅
- Phase 2-1 reload E2E 검증 통과 ✅
- Phase 2-1-C: customPay grossPay 연결 ✅
  → custom-premium.ts 신규 / calc-engine CalcInput.customPay / use-calc 주입

## 다음 작업 ← 현재
Phase 2-2/2-3: B single/double/triple 제거 + adjustedGrossPay 제거
- 구조 조사 완료
- 방향 확정: A 진실원천 / B 제거 / result.grossPay 기준 정리

## Phase 2 대기
2-3. totalPremium → custom subtotal 전환 또는 제거
2-4~2-8. 칩 토글/근무내역/조합해석/화면분리/인라인제거
