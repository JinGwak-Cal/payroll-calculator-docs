# Observation + Evidence Register — EP-0002 (Claim-2: C-07)

```
Parent ID: EP-0002 / Root Pilot ID: PI-0000 / Current Stage: P2
```

## Observation Log

| OB ID | locator(message) | 원문 요지 |
|---|---|---|
| OB-005 | message-163 (L13345) | "지난 1주일 안에서는 '제수당' 관련 논의를 찾지 못했습니다" — conversation_search만으로 단정 |
| OB-006 | message-166 (L13410, User) | "왜 없다고 답변한거야?" — 사용자가 실측 방법을 되물음 |
| OB-007 | message-167 (L13418) | 검색방법 설명(conversation_search+recent_chats), "정확히 확인하려면 grep이 필요" 암묵 인정 없음 — 여전히 대화기록 검색에만 의존 |
| OB-008 | message-169 (L13443) | 재검색해도 대화기록 검색만 반복, "Closing Review 부재" 이론으로 오답 지속 — **아직도 SoT 저장소(decisions.md) 직접 grep을 안 함** |

## Triage — Candidate 승격

전부 Claim-2 직접 관련(단정→반복오답 흐름), 원본 turn locator
명확 → 전부 Candidate 승격 → ER-0003

## ER-0003

```
유형: Fact
관련 Claim: Claim-2
검증자: Claude(Prepared)
검증방법: locator(message-163/167/169) 직접 확인, 3개 turn에
  걸쳐 "실측(grep) 없이 대화기록 검색 도구만으로 단정"하는 패턴이
  반복 확인됨
반증검토: message-167에서 검색방법을 스스로 설명은 했으나, 그
  설명 자체가 "SoT 저장소를 grep 안 했다"는 걸 자인하지 않고
  "검색 알고리즘 한계"로만 설명함 — 즉 자기인정이 아니라 사용자
  질문(message-170 "어케 생각해")에 의해 계속 이어짐
결과: **Claim-1과 다르게, 이번엔 원본 turn locator가 명확히
  3개(163/167/169) 확보됨.** 다만 "실제 최종 정정 turn"(grep으로
  진짜 발견한 순간)은 이 Source A 범위 밖(더 뒷부분)에 있어
  이번 Pilot에서는 미추적
```
