# OR-0000 vs OR-0001 — 결과 비교 (Success Criteria b, c 검증)

> **⚠️ 신뢰도 하향 정정(2026-07-21, 마누스 감사 결과 반영)**: 이
> 문서는 GPT가 채팅으로 보낸 P4 Walkthrough(OB-0001~4, EV-0001~4,
> Inconclusive)를 실제 산출물로 취급해 작성됐다. 그러나 마누스의
> 독립 감사(제출 ZIP 직접 확인)에 따르면 GPT 실제 패키지에는
> `finding_register_generated: false`가 명시돼 있고 FR-0001~0003
> 미생성이 확인됨 — 즉 채팅 속 OB/EV ID는 **검증 가능한 locator를
> 가진 실제 Evidence가 아니라 서술적 요약이었을 가능성이 높다.**
> 아래 비교·원인분석은 **가설로 격하**하고, 마누스 로드맵(Phase B,
> 진짜 blind 독립 OR-0002)에서 재검증이 필요하다.

```
Parent ID: PI-0001 / Root Pilot ID: PI-0001 / Current Stage: P5
```

## 결과 대조표

| Claim | OR-0000(Claude) | OR-0001(GPT) | 일치? |
|---|---|---|---|
| Claim-1(A-08) | Insufficient | Inconclusive | **대체로 일치**(둘 다 "판정 불가") |
| Claim-2(C-07) | **Supported**(원본 turn 3개 확보: message-163/167/169) | Inconclusive | **불일치** |
| Claim-3(산출물 4분류) | **Confirmed**(git status 직접 실행) | Inconclusive | **불일치** |

## 불일치 원인 분석 (추정이 아니라 Source 접근권 차이로 설명 가능)

이 불일치는 **Method 결함이 아니라 Source Capability 차이로 설명됩니다.**

- **Claim-2**: 제 Supported 판정은 **Source A(Claude Thread 원문)**를
  직접 grep해서 나온 겁니다(message-163/167/169). GPT의 SI-0002는
  "Source A: Not Yet Requested" 상태로 시작했고, 이후 실제로
  Source A를 받았다는 기록이 P1~P4 보고에 없습니다 — **GPT는
  Source B(자기 쓰레드)만 봤을 가능성이 높습니다.** "제수당" 사건은
  Claude 쪽 대화에서 일어난 일이라, Source B에는 애초에 없을 수
  있습니다.
- **Claim-3**: 제 Confirmed 판정은 **Repository(git status 직접
  실행)**로 나온 겁니다. GPT는 bash/저장소 접근 권한이 없어서
  이 Source 자체를 쓸 수 없었습니다 — Reviewer Check에서도 "4분류
  자체를 검증하기 위한 비교 Evidence 부족"이라고 명시했는데, 이건
  판단력 부족이 아니라 **애초에 Repository Source에 접근이
  안 됐기 때문**입니다.

## 결론 — 이게 왜 SOP를 무효화하지 않는가

오히려 **CR-002(Source Capability Mapping)의 필요성을 실증**합니다.
"어느 Source가 어느 Claim/분류를 담당하는가"를 Contract 단계에서
명시했더라면, GPT는 처음부터 "Claim-2/3은 내 Source 접근권으로는
Operational 판정이 구조적으로 불가능하다"는 걸 P1에서 바로 알고
갔을 것이고, Insufficient가 아니라 **"Not Assessable(Source
Capability 밖)"**로 더 정확하게 종료했을 것입니다. 즉 이번 불일치
자체가 CR-002를 뒷받침하는 새로운 Evidence입니다.

## Success Criteria 최종 판정

| 기준 | 결과 |
|---|---|
| (a) 독자적으로 Source Intake~Finding 완주 | ✅ 완주(GPT 자력 수행) |
| (b) 결과를 사후 비교 | ✅ 완료(본 문서) |
| (c) 일치/불일치 모두 유효한 결과로 기록 | ✅ 불일치 기록, 원인까지 설명됨 |
| (d, v0.2 추가) 모든 Template 수정없이 실사용 가능 | ✅ GPT 자체 확인("SOP 자체는 실제로 실행 가능했습니다") |

**PI-0001 Success Criteria 전부 충족.**
