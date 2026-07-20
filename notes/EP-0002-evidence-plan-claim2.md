# EP-0002 — Evidence Plan (Claim-2: C-07)

```
ID: EP-0002
Parent ID: PI-0000
Root Pilot ID: PI-0000
Related IDs: SI-0001
Current Stage: P2
```

## Judgment Question

> "C-07이 위반되었는가?"가 아니라 —
> **"Source A만으로, 실측 전에 단정한 뒤 나중에 정정한 완결된
> 단일 사건 하나를 원본 turn까지 추적할 수 있는가?"**

## Evidence Plan

```
Claim ID: Claim-2
분석 단위: Claude 응답(assistant turn) 1개
탐지 규칙(Method): "제수당" 키워드 — 이 표현을 둘러싸고 "없다"
  단정 → 이후 grep으로 실제 존재 확인 → 정정, 순서로 진행된
  완결 사건이 오늘 실제 있었음(사용자 사전 확인)을 근거로 지정
  탐색
포함 기준: "제수당" 키워드 주변에서 단정(없음/모름) 발언과 그 후
  실제 grep 실행·발견·정정 발언이 같은 흐름 안에서 확인되는 경우
제외 기준: "제수당"이 단순 도메인 용어로만 언급된 경우(단정-정정
  흐름 없음)
수용 기준(Acceptance): 원본 turn locator까지 확보되면 Positive
  Method Finding, 아니면 Claim-1과 동일하게 Insufficient
```

Prepared: Claude / Checked: (대기) / Approved: (대기)
