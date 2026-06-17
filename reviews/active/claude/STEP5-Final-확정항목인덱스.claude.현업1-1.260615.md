# STEP5-Final — 확정 항목 인덱스

- **문서 종류**: STEP5 확정사항 요약 인덱스 — 신규 설계 아님
- **작성**: Claude (현업1-1 협업)
- **기준 시각**: 2606.15
- **참조 문서**: STEP5-ResultGrid-Review-01 · STEP5-2-3-Drawer-IA-RESULT04-통합검토 · STEP5-4-Drawer-확정안

---

## §1. ResultGrid 역할 재정의 (→ STEP5-1)
- ResultGrid = 결과 표시판 + 입력 진입점
- 가산수당 영역 터치 → 하단 Drawer 열림
- 실수령액/총급여/기본급/주휴/공제 → 입력 진입 불가

---

## §2. RESULT-01~05 처리 방향 (→ STEP5-1, STEP5-2-3)
- RESULT-01: `rounded-2xl` → `rounded-3xl` 통일 후보
- RESULT-02: Primary 위계 강화 필요 (`text-base` 상향 검토)
- RESULT-03: Row 구조 정식화 (Component=Row 신규값은 UI-Audit-05 개정 항목)
- RESULT-04: 체크박스 방식 제거 확정, 대체 ON/OFF 방식은 STEP6+ 보류
- RESULT-05: 인라인 펼침 입력 제거 확정, Drawer로 이전

---

## §3. 시나리오 확정 (→ STEP5-2-3)
- 시나리오 A 확정: 컨테이너 + 반복 Row 구조 유지
- docs↔code 불일치: manual-v14의 single/double/triple/custom 4구조는 미구현 목표안, 현재 코드는 Custom 1구조
- SinglePremiumCard.tsx: Removing 후보

---

## §4. 영역 구분 확정 (→ STEP5-4)
- 상태유급형 수당: 주휴(노터치) / 연차(별도 개선, STEP6-1)
- 시간속성 수당: 연장 / 야간 / 휴일 / 맞춤가산 → 하단 Drawer 입력
- 공제/차감: 수당 아님, Drawer 대상 아님, 현행 구조 유지

---

## §5. Drawer 구조 확정 (→ STEP5-4)
- 위치: 항상 하단 고정 (Bottom Sheet)
- 칩: [연장][야간][휴일][완료] 한 줄 — 완료 전 비선택 유지, 완료 후 비선택 제거
- 흐름: 수당 선택 → 시간 입력(스테퍼+키패드) → 가산율 안내 → 즉시 결과
- 재탭 편집: 기존 값을 유지한 상태로 편집모드 복귀 (수정 가능 범위는 STEP6 단계에서 확정)
- 추가 버튼: [다른 수당 추가]
- 행 철학: 행 = 근무상황 1건 (수당 총합 입력기 아님)

---

## §6. 저장 구조 확정 (→ STEP5-4, STEP6-2-1 참조)
- 저장 단위: `id + selectedAllowances + premiumRate + premiumHours`
- 저장 금지: `premiumAmount / premiumType / mode / allowanceCombo`
- 표준/맞춤 판정: `premiumRate === selectedAllowances.length * 50`

---

## §7. 용어 (→ manual-v14, STEP6-2-1)
- 가산 입력 브릿지: 통칭 (§구조-2 입력기 역할 분리 + §구조-3 조합 자동 해석의 실무 별칭)
- 기존 manual-v14 및 코드에서 사용된 관련 용어: premiumType / allowanceCombo / selectedSingleAllowance / selectedCustomAllowances
- 현재 저장 구조 후보: selectedAllowances (STEP6-2-1 기준)

---

## §8. SinglePremiumCard 처리
- SinglePremiumCard.tsx: Removing 후보 (미사용 dead component, 즉시 삭제 아님)

---

## decisions 반영 후보 문장
1. RESULT-05 인라인 입력 UI 제거 확정 (§구조-6 기존 확정사항 재연결)
2. ResultGrid = 결과 표시판 + 입력 진입점 (§구조-6/6-1)
3. 시간속성 수당 입력 = 하단 Drawer (가산 입력 브릿지, 통칭)
4. 행 = 근무상황 1건 (수당 총합 입력기 아님)
5. 저장 단위: id + selectedAllowances + premiumRate + premiumHours

---

## 보류 전달 (STEP6+)
- RESULT-04 대체 ON/OFF 방식
- 편집모드 수정 가능 범위
- PremiumScreen 흡수 여부
- 연차 개선 (STEP6-1)
- mapEntriesToCalcInput() (STEP6-2-2)
- 최대 행 수 확정

---

*본 문서는 STEP5 확정사항 인덱스이며, 세부 내용은 각 참조 문서를 기준으로 한다.*
