# FR-0001 — Finding Register (Claim-1: A-08)

```
Parent ID: ER-0001,ER-0002 / Root Pilot ID: PI-0000 / Current Stage: P3
```

```
Finding 유형: Method Finding (Operational Finding 아님 — OR-SOP
  §11, §12에 따라 이 Pilot에서는 Operational Decision 생성 안 함)

Claim: Source A만으로는 Claim-1(A-08)에 대해 Operational Finding을
  내릴 만큼 충분한 Evidence를 확보하지 못했다.

Basis: ER-0001(자기인정 발언, 원본 사건 locator 미연결),
  ER-0002(집계 주장, 개별 사건 추적성 없음)

Interpretation: grep→Observation→Candidate→Evidence 절차 자체는
  정상 작동함(4건 중 2건을 SOP 기준으로 정확히 제외). 다만 Evidence
  품질이 Operational 판정 기준(원본 turn locator 기반)에 못
  미쳤음. 원인은 탐지 규칙(Method)이 "자기인정 발언"을 찾도록
  설계되어 있었지, "실제 위반 turn"을 직접 찾도록 설계되지
  않았던 것

Confidence: Insufficient (원문 근거는 있으나 Operational 결론을
  내리기엔 부족)

Decision Need: (a) 이번 Pilot에서는 추가 조치 없음 — Insufficient로
  확정하고 종료 (b) 원본 turn 직접 추적은 Deferred Issue로 등록,
  향후 별도 Operational Review에서 재수행 여부는 사용자 승인 필요
```

## Method Finding 요약 (Pilot 전체 관점)

이번 P2의 진짜 성과는 "A-08이 몇 번 위반됐는가"가 아니라 —
**"Evidence가 부족하면 부족하다고 판정하는 절차가 실제로
작동함이 확인됐다"**는 것. Candidate Discovery Rule(grep=후보일
뿐)이 실전에서 정확히 작동해 4건 중 2건을 걸러냈고, 남은 2건도
Operational 기준 미달로 Insufficient 처리됨 — SOP 설계 의도대로
동작.
