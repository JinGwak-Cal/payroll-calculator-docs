# Evidence Register — EP-0001 (Claim-1: A-08)

```
Parent ID: EP-0001 / Root Pilot ID: PI-0000 / Related IDs: OB-001,OB-002 / Current Stage: P2
```

## Triage 결과 (Candidate 승격 여부)

| OB ID | Candidate 승격 | 사유 |
|---|---|---|
| OB-001 | ✅ Candidate → ER-0001 | Claim-1 직접 관련, 단일 사건 자기인정 |
| OB-002 | ⚠️ Candidate(제한적) → ER-0002 | Claim-1 관련이나 **집계 주장**이라 개별 사건 locator 없음 — Context로 등록 |
| OB-003 | ❌ 제외 | Claim-1(A-08) 범위 아님(다른 Rule) |
| OB-004 | ❌ 제외 | Fact 아님(인용문 내 가상 예시) |

## ER-0001

```
유형: Fact
관련 Claim: Claim-1
검증자: Claude(Prepared), GPT(Checked 대기)
검증방법: locator(L26080) 직접 확인, 문맥상 실제 사건에 대한
  자기인정 발언 확인
반증검토: 없음(자기인정이라 반증 여지 낮음, 다만 "인정"이라는
  발언 자체가 실제 원본 사건의 재현은 아니고 Claude의 사후 해석
  이라는 한계 있음)
결과: 실제 사건 1건 확인(단, 사건 자체의 원본 turn locator는
  이 사건의 인정 발언 위치이지, 위반이 실제 발생한 turn의 위치가
  아님 — 추가 확인 필요)
```

## ER-0002

```
유형: Context (Corroborating, not standalone Fact)
관련 Claim: Claim-1
검증자: Claude(Prepared)
검증방법: locator(L28877) 직접 확인
반증검토: "최소 5번 이상"이라는 표현 자체가 정확한 카운트가
  아님을 자인("최소"라는 표현) — Evidence Plan Acceptance
  기준(원문 매치 근거, "약/최소" 표현 금지)에 저촉되는 자료
결과: 개별 사건으로 분해 불가. 정확한 횟수 주장 근거로 쓸 수 없음
```
