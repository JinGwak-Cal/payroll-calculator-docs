# CR-004~011 — OR-0001 Pilot Feedback Report 기반 (v0.3 입력)

Origin: OR-0001 Pilot Feedback Report v0.2 (GPT, Independent
Reviewer). 근거: 실제 P0~P5 완주 후 작성된 SOP 실행성 피드백.

## CR-004 (P1, 우선순위 최상)

```
대상: T-P0 Pilot Control Contract
변경 사유: Reviewer가 "이번 Review의 성공조건/종료조건/제외범위"를
  반복 확인해야 했음 — Contract에 Success/Exit Criteria가 있었지만
  실제 사용 중 재확인이 필요할 만큼 눈에 안 띄었음
Before → After: Contract 구조를 "Success Criteria → Exit Criteria"
  명시적 하위 섹션으로 재배치
```

## CR-005 (P1, 우선순위 최상)

```
대상: T-P1 Source Intake
변경 사유: "Source가 있는가"보다 "Source가 충분한가"가 더 큰
  판단부담이었음 — Source Completeness Matrix + Transition
  Gate("P2로 진행 가능한가?") 명시적 산출물 부재
Before → After: T-P1에 Source Completeness Matrix, Transition
  Gate(Can proceed to P2?) 신규 하위 산출물 추가
```

## CR-006 (P2)

```
대상: T-P2-2 Observation Log / T-P2-3 Evidence Register 사이
변경 사유: Observation→Evidence 사이 "Candidate" 단계가 실제로는
  판단오류를 줄이는 핵심 단계였는데, Template에서 비중이 낮음
  (OR-0000에서도 이미 Triage 단계로 실질 수행했으나 정식
  Register는 아니었음 — 두 Pilot 모두에서 동일하게 확인된 Gap)
Before → After: Candidate Register를 정식 Artifact로 승격,
  Observation Log와 Evidence Register 사이 필수 단계로 정의
```

## CR-007 (P3)

```
대상: T-P3 Finding Register
변경 사유: Confidence 필드는 있으나(Confirmed/Supported/
  Tentative/Insufficient), "왜 Insufficient/Inconclusive인지"
  별도 설명 요구가 반복됨. Evidence Coverage 개념 부재
Before → After: Finding Register에 Evidence Coverage, Reason for
  Inconclusive 필드 추가
```

## CR-008 (P4, 우선순위 최상)

```
대상: T-P4 이전 단계
변경 사유: Walkthrough 전에 Claim과 Evidence를 연결하는 중간
  구조가 없어 Reviewer가 직접 구성해야 했음(가장 큰 Gap으로 보고됨)
Before → After: Walkthrough 이전에 Claim Mapping → Evidence
  Coverage Matrix 신규 Artifact 추가
```

## CR-009 (P5, 우선순위 최상)

```
대상: T-P5 이전(Exit Decision 직전)
변경 사유: 종료 이유를 검증하는 절차(Closing Gate)가 없고, 남은
  작업이 다음 Review로 안 이어짐
Before → After: Exit Decision 이전 Closing Gate 신규(Observation
  Complete/Candidate Complete/Evidence Complete/Finding Closed/
  Deferred Recorded/Next Trigger Defined)
```

## CR-010 (Cross-stage)

```
대상: SOP 전반
변경 사유: 각 단계 종료 시 "왜 다음 단계로 갈 수 있는가"를 확인
  하는 절차(Transition Gate)가 구조적으로 전 단계에 없음 — CR-005/
  CR-008과 같은 근본 원인
Before → After: 모든 P0~P5 단계 경계에 공통 Transition Gate 형식
  표준화(이미 CR-005/008이 개별 사례로 반영하지만, 전체 표준화는
  별도 항목으로 유지)
```

## CR-011 (Cross-stage)

```
대상: SOP/Template 전반
변경 사유: Reviewer의 판단 과정 자체가 중요한 Evidence였는데
  Artifact로 안 남음. Claim별 Supporting/Contrary/Missing Evidence
  구분 기능 부족(Coverage 확인 기능 부족)
Before → After: CR-008(Evidence Coverage Matrix)이 이 문제를 상당
  부분 해결 — 별도 항목으로 유지하되 CR-008과 통합 검토
```

**상태: 전부 Candidate(v0.3 입력 후보), 미적용.** 실제 v0.3 반영은
별도 승인 필요.
