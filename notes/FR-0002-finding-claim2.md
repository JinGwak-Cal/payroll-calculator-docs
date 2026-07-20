# FR-0002 — Finding Register (Claim-2: C-07)

```
Parent ID: ER-0003 / Root Pilot ID: PI-0000 / Current Stage: P3
```

```
Finding 유형: Method Finding

Claim: Source A만으로 C-07 관련 "단정→반복오답" 사건의 원본 turn
  locator를 3개(message-163, 167, 169) 확보할 수 있었다.

Basis: ER-0003

Interpretation: Claim-1(A-08)과 달리, 이번엔 grep 키워드
  ("제수당")가 사건과 직접 결합돼 있어 탐지가 정확했다. Claim-1은
  "위반"이라는 추상적 자기평가 단어로 탐지했는데, 이건 원본
  사건이 아니라 사후 요약을 찾게 됨. 반면 Claim-2는 사건의
  **도메인 키워드**로 탐지해서 원본 turn 자체를 찾을 수 있었다.
  → 방법론적 시사점: Method(탐지규칙) 설계 시 "자기평가 단어"보다
  "사건 고유 키워드"로 탐지하는 편이 원본 추적에 유리함(Change
  Request 후보)

Confidence: Supported (원본 turn 3개 확보, 다만 "최종 정정 turn"
  자체는 Source A 범위 밖이라 완결 사슬은 아님 — Confirmed는
  아니고 Supported)

Decision Need: 없음(이번 Pilot에서는 결론 확정, 추가 조치 불요)
```

## Method Finding 요약

Claim-1과 Claim-2를 비교하면 절차의 **정확도가 탐지규칙(Method)
설계에 크게 좌우된다**는 게 확인됨 — SOP 자체는 두 경우 모두
동일하게 작동했지만(grep→Observation→Triage→Evidence→Finding),
결과 품질(Insufficient vs Supported)은 Evidence Plan 단계에서
"무엇을 grep할지" 설계가 결정했다. 이건 P5(Exit Decision)에
반영할 만한 Method Decision 후보.
