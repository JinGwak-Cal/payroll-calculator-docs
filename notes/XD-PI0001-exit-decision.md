# Exit Decision — PI-0001 (OR-0001)

```
Parent ID: PI-0001 / Root Pilot ID: PI-0001 / Current Stage: P5
```

## Exit 상태

```
☑ Revise & Re-Pilot
□ Freeze
□ Inconclusive (Pilot 자체는 Inconclusive 아님 — SOP 실행성은
  Pass, Claim 결과만 Inconclusive)
□ Stop / Re-scope
□ Abort
```

## 근거

GPT 자체 결론과 동일: **"SOP와 Template Pack이 실제 독립
Reviewer에 의해 끝까지 실행 가능한지 검증한 첫 실행 사례"**로
성공. 다만 비교 분석(OR-0000-vs-OR-0001-comparison.md)에서
CR-002(Source Capability Mapping)의 실제 필요성이 재확인됐고,
GPT의 2차 제안(doc "2.")에서 신규 CR 후보가 추가로 나옴 —
v0.3 없이 Freeze하기엔 이르다.

> **⚠️ 2026-07-21 정정**: 마누스 독립 감사 결과, GPT의 실제
> 제출 패키지에는 Finding Register가 생성되지 않았음이 확인됨
> (`finding_register_generated: false`). 즉 이 Exit Decision이
> 근거로 삼은 GPT의 채팅상 Walkthrough/Finding은 검증된 산출물이
> 아니라 서술적 요약이었을 가능성이 높다. **"OR-0001 완료"라는
> 판정 자체를 재검토해야 한다** — 마누스 권고대로 GPT가 실제
> 파일 기반 SI/EP/OB/ER/EPK/FR/WD/XD를 제출하는 진짜 독립 실행이
> 필요.

## 신규/기존 CR 매핑 확인

GPT의 2차 제안(Claim Mapping / Claim별 Source Index / Evidence
Coverage(Supporting·Contrary·Missing) / Decision Log / Closing
Gate 상세 7항목)을 기존 CR-004~011과 대조:

| GPT 2차 제안 | 매핑 |
|---|---|
| Claim Mapping | CR-008과 동일(중복, 신규 아님) |
| Claim별 Source Index | CR-005(Source Completeness Matrix)로 흡수 |
| Evidence Coverage(3분류) | CR-011과 동일(중복) |
| Decision Log("왜 Candidate/Evidence/Finding이 됐는가") | **부분 신규** — CR-006(Candidate Register 승격)이 구조는 다루지만 "판단 이유 로그"까지는 명시 안 함 |
| Closing Gate 상세 7항목 체크리스트 | CR-009 구체화(중복, 신규 아님) |

## CR-012 (신규)

```
대상: T-P2-3 Evidence Register 또는 T-P3 Finding Register
변경 사유: Candidate/Evidence/Finding 각 단계에서 "왜 그렇게
  판단했는가"의 이유 자체가 Artifact로 안 남음(GPT 지적, Decision
  Log). OR-0000/OR-0001 둘 다 결과만 기록했지 판단 과정 자체는
  서술로만 존재
Before → After: Evidence Register 또는 Finding Register에
  "Decision Rationale"(이 Candidate/Evidence/Finding으로 판단한
  이유 1~2문장) 필드 추가
```

## CR-013 (신규)

```
대상: T-P3 Finding Register Confidence 값 목록
변경 사유: 이번 비교에서 확인됨 — Insufficient/Inconclusive는
  "증거가 있는데 부족"과 "애초에 그 Source Capability로는 판정
  불가능"이 섞여 있음(Claim-2/3에서 실증)
Before → After: Confidence 값에 "Not Assessable(Source Capability
  밖)"을 Insufficient와 구분되는 별도 값으로 추가
```

## 최종 권고

**v0.3 진행 후 재파일럿(OR-0002) 권장.** 이번 두 Pilot(OR-0000,
OR-0001)에서 겹치지 않게 발견된 CR이 총 13건(CR-001~013)이고,
이 정도 축적이면 v0.3 한 번에 다 반영해서 다시 검증하는 게
효율적. Freeze는 v0.3 이후 OR-0002 결과를 보고 재논의.
