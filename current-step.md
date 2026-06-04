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
- Phase 2-2/2-3: B single/double/triple 제거 + adjustedGrossPay 제거 ✅
  → totalPremium = customPremiumTotal만 유지
  → orphan 카드 파일 3개(Single/Double/TriplePremiumCard) 삭제 보류
- Phase 2-4: 공식 종료 ✅ (칩 토글 이미 구현됨 / 잔여는 2-6 이관)

## 다음 작업 ← 현재
Phase 2-7: PremiumSection 화면 분리
- 착수 전 구조 확인 진행 예정

## Phase 2 대기
※ 2-5/2-6은 고위험 모델 작업이므로 2-7/2-8 이후로 순서 재조정됨
2-7. 화면 분리
2-8. 인라인 제거 (2-7 완료 후)
2-5. 근무내역 단위 (고위험 — 별도 설계 보고 후)
2-6. 조합 자동 해석 (2-5 확정 후)
