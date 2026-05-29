# S-1 주휴수당 체크박스 버그 분석
생성일: 2026-05-29

## 버그 원인 확정
파일: use-calc_current.tsx (또는 exports/use-calc.tsx.txt)
위치: adjustedResult useMemo (446~468줄)

## 문제 코드
```
const totalJuhuPay = mergedWeekDetails.reduce(
  (sum, week) => sum + (week.juhuPay ?? 0), 0
);
const newGross = baseGross + totalJuhuPay + annualAmount;
const newNet = baseNet + totalJuhuPay + annualAmount;
```

includeJuhu 체크박스 state가 계산에 반영되지 않음
→ 체크박스 OFF해도 totalJuhuPay 항상 포함

## 수정 방법 (최소 증분)
파일: use-calc_current.tsx
수정 위치: 455줄, 459줄

455줄 수정:
전: const newGross = baseGross + totalJuhuPay + annualAmount;
후: const newGross = baseGross + (state.includeJuhu ? totalJuhuPay : 0) + annualAmount;

459줄 수정:
전: ? baseNet + totalJuhuPay + annualAmount
후: ? baseNet + (state.includeJuhu ? totalJuhuPay : 0) + annualAmount

## 절대규칙 검증
- 계산 로직 수정 (calc-engine 아닌 use-calc) ✅
- 최소 증분 (2줄만 수정) ✅
- 구조 변경 없음 ✅
- 리팩토링 없음 ✅

## 연차 비교
state.includeAnnual ? annualLeave.amount : 0
→ 연차는 이미 includeAnnual 체크박스 반영됨
→ 주휴도 동일 패턴으로 수정하면 됨

