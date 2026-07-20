# Operation Capture Pipeline(OCP, 운영 캡처 파이프라인) — Phase 1 (경량, 즉시 적용)

Status: Draft — 사용자 최종 승인 완료(2026-07-17), ai/draft push 대기
작성: 2026-07-17, E-035 근거

> **OCP는 운영 문제를 해결하는 Pipeline이 아니라, 운영 문제를
> Capture하여 개발 흐름을 보호하는 Pipeline이다.**
> (참고: TTP가 Thread Lifecycle을 관리한다면, OCP는 Operational
> Knowledge Lifecycle의 Capture 구간만 담당한다. 둘은 경쟁 관계가
> 아니라 프로젝트 운영의 두 축이다.)

## Why this Pipeline exists (이 Pipeline이 존재하는 이유)
정확한 명칭은 Operation Pipeline이 아니라 **Operation Capture
Pipeline(OCP)**이다. 이 Pipeline은 Threshold Foundry를 구현하기 위한
것이 아니다.
개발 중 떠오르는 운영 아이디어가 Thread 안에만 남고 Repository로
연결되지 못해, 몇 주 뒤 동일한 논의를 반복하는 Loss를 줄이기
위해 존재한다. (실제로 이번 63 Matrix 자체가 이 Loss의 사례다 —
Thread 안에서는 이미 정의되어 있었으나 Repository에는 반영되지
않아, grep으로는 존재가 확인되지 않았다.) Phase1의 목표는 운영
자산을 최소 비용으로 Capture하여 즉시 개발로 복귀하는 것이다.

## 목적
개발(Payroll Calculator / Paycheck Workbook) 중 발생하는 운영
아이디어·이슈를 그 자리에서 잃어버리지 않으면서도, 개발 흐름을
세우지 않기 위한 최소 절차다. Threshold Foundry의 완성형
(Pattern Discovery → 63 Matrix → Threshold → Pilot → Promotion →
Correction Table, Phase 2)은 Payroll 출시 이후로 미룬다
(current-step.md 구조2 Release Priority 근거, D-TF-003).

## Trigger
개발 중 아래 중 하나가 발생하면 이 파이프라인을 호출한다:
- 새로운 운영 아이디어·개선점이 떠오름
- 반복되는 실수·패턴을 발견함
- "이거 나중에 검토해야겠다"는 판단이 섬

## 문제 정의 (사용자 원문, 그대로 보존)
> "이용자는 지금 개발에 전념하고 싶지만, 자꾸 이런 운영의
> 파잎라인 부재가 가장 큰 LOSS이다. 작업진행을 방해하고 에너지를
> 엉뚱한데 새게 만드는 요인이라, 완전한 해결(장기해결)은
> 밑그림만 그리더라도, 당장 부담을 줄일 수 있는 임시방편(단기
> 해결)이라도 반드시 파이프라인을 만들어야 한다."

## Flow (Phase 1 — 이 이상 하지 않는다)

1. **Operational Event 발생**
2. **Evidence 기록** — `notes/context-history.md`에 다음 회차
   E-번호로 raw 기록(① 사건 ② 의도 ③ 결정 ④ 근거 ⑤ 영향 형식만
   채움, 판정·승격 없음)
3. **Context Link(맥락 연결)** — Evidence 기록 시 최소한
   Thread(어느 쓰레드인지) / Conversation(대화 식별) / Related
   Decision(관련 decisions.md 항목)을 함께 남긴다. 몇 달 뒤
   "이게 어느 Thread였지?"가 반복되지 않게 하기 위함.
4. **Operational Classification(운영 분류)** — 이번 Event를
   어떤 분류 엔진으로 분류할지 표기. 현재는 63 Matrix 하나만
   존재하지만, 앞으로 TTP/Bridge/Layer 등 다른 분류 엔진이
   추가될 수 있으므로 이 단계는 "63 Matrix 전용"이 아니라
   "Operational Classification"이라는 상위 개념으로 둔다.
   - 대표 구현 1: **63 Matrix** = TTP Lifecycle 7행(Closing
     Review~Next Baseline) × Micro 템플릿 9열(①What~⑨Next
     Trigger) = 63. 태깅 방법: "행이름×열이름"으로 표기(예:
     "Closing Review × Success Criteria"), 셀 번호(M12 등) 규칙은
     아직 미확정 — 지금은 이름 그대로 쓰고 번호는 나중에 붙인다
     (Matrix가 바뀔 가능성이 있어 번호를 먼저 고정하지 않음)
   - 원출처: 2026-07-17 파트너(GPT) TTP 표 제안 문서(표1~표5)
5. **Capture Complete(Capture 완료)** — 위 2~4단계(Evidence·
   Context Link·Classification)가 채워지면 이 시점에서 "Capture
   끝"으로 선언한다. 이 선언 이후로는 이번 Event에 대한 추가 판단
   (Threshold 판정 등)을 하지 않는다.
   > **주의(2026-07-17, Reporting SOP 유실 사례로 추가)**:
   > Capture Complete는 "Candidate 단계"에 도달했다는 뜻일 뿐,
   > 실제 문서 반영(Applied)이나 다음 쓰레드에서의 재확인
   > (Verified)을 보장하지 않는다. "Bridge로 넘기겠다"는 언급
   > 자체도 Assigned조차 보장 못 한다는 것이 실제로 확인됨
   > (research-backlog.md DEFER-015 참조). Candidate 항목은
   > Candidate→Assigned→Applied→Verified 중 현재 단계를 반드시
   > 함께 표기한다.
6. **Deferred/Candidate 저장** — `current-step.md` 구조4 Deferred
   또는 `research-backlog.md` DEFER-XXX 중 하나에 한 줄만 연결
7. **즉시 개발로 복귀** — 그 이상의 판단(Threshold 판정·Promotion·
   SOP화)은 이 단계에서 하지 않는다.
   > **이 Pipeline의 종료 조건은 운영 판단의 완료가 아니라,
   > 개발을 중단하지 않을 만큼 Capture가 완료된 시점이다.**

## 명시적으로 하지 않는 것 (Phase 2로 이연, 출시 이후)
- Pattern Discovery
- Threshold 판정
- Pilot 검증
- Correction Table / Handbook 반영

이들은 Threshold Foundry Phase 2(출시 이후) 소관이며, 이 문서의
책임 범위 밖이다.

## 미확정 항목 (승인 전 확인 필요)
- 63 Matrix의 M12/M27/M48 같은 개별 셀 코드 표기법(행-열을
  어떤 규칙으로 번호화할지)은 아직 확정되지 않음 — 필요 시
  "행이름×열이름"으로 그대로 쓰거나, 이후 코드 규칙을 별도 확정
- 이 문서를 어디에 반영할지: notes/ 그대로 둘지, absolute-rules.md
  에 1줄 참조만 추가할지는 별도 확인 필요
- TTP(표1~표5) 자체는 아직 Threshold Foundry Phase2 소관 초안
  단계이며, 이번 Phase1 문서는 그 표 중 "Matrix" 구조만 차용한
  것일 뿐 TTP 전체를 지금 채택하는 것은 아님
