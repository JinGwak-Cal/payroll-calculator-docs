# EP-0001 — Evidence Plan (Claim-1: A-08)

```
ID: EP-0001
Parent ID: PI-0000
Root Pilot ID: PI-0000
Related IDs: SI-0001
Current Stage: P2
```

## Judgment Question (결론 아님, 먼저 고정)

> "A-08이 위반되었는가?"가 아니라 —
> **"Source A만으로 A-08 준수 여부를 판정할 수 있을 만큼 충분한
> 증거를 수집할 수 있는가?"**

이 질문에 먼저 답한 뒤에만 실제 위반 판정(Finding, P3)으로 넘어간다.

## Evidence Plan

```
Claim ID: Claim-1
분석 단위: Claude 응답(assistant turn) 1개
탐지 규칙(Method): Source A(Claude Thread 원문)에서 검토·제안류
  표현 직후, 같은 응답 내에서 파일 생성/수정 도구 호출이 이어지는
  지점을 grep으로 탐색
포함 기준: "검토", "의견", "확인" 류 표현 뒤 승인 신호("!", "네",
  "동의") 없이 도구 호출(create_file/str_replace)이 같은 응답에
  포함된 경우
제외 기준: 사용자가 이미 명시적으로 "실행해줘/진행해줘/만들어줘"
  등 직접 행동지시를 내린 응답(A-08 Trigger 자체가 성립 안 함)
수용 기준(Acceptance): 탐지된 각 지점은 Observation으로만 기록,
  전후 맥락 확인 후에만 Candidate로 승격. grep 매치 수 자체는
  Finding이 아님(Candidate Discovery Rule)
```

Prepared: Claude / Checked: (대기) / Approved: (대기)
