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
- Phase 2-2/2-3: B single/double/triple 제거 + adjustedGrossPay 제거 ✅
  → totalPremium = customPremiumTotal만 유지
  → orphan 카드 파일 3개(Single/Double/TriplePremiumCard) 삭제 보류

## 다음 작업 ← 현재
Phase 2-4 착수 전 — PremiumSection(custom only) 구조 검증
- 2-2/2-3 제거 여파 없는지 점검 후 2-4 진행

## Phase 2 대기
2-4. 칩 토글 정리
2-5. 근무내역 UI 정리
2-6. 조합 해석 로직 정리
2-7. 화면 분리
2-8. 인라인 입력 제거
