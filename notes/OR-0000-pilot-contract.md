# OR-0000 Pilot Control Contract (실제 값)

```
Pilot Status

Design Complete
Pilot Execution Starts Here

From this point forward, all newly generated artifacts are Pilot
Instance artifacts, not methodology design artifacts.
```

```
Pilot ID: OR-0000

Goal: Operation Review SOP v0.1과 Template Pack v0.1이 실제
      Operation Review를 지원할 수 있는지 제한된 Pilot을 통해
      검증한다. Pilot은 제한된 표본 Claim을 이용하여 P0~P5 절차와
      Template의 실행 가능성, 추적 가능성, 일관성 및 통제성을
      검증한다. Pilot의 결과는 Operational Finding이 아니라
      Method Decision이며, SOP·Template Pack의 유지, 수정 또는
      재검증 여부를 판정 대상으로 한다.

Review Target: OR-METHOD-001 Pilot Execution (SOP v0.1 + Template
      Pack v0.1의 실행 가능성 검증)

Pilot Material: 2026-07-17~20 Thread(Source A/B) — 오늘 Thread의
      Rule 준수 자체를 심사하는 것이 아니라, 검증 재료로만 사용

Claim 범위: 표본 3건 (Pilot Material에서 추출)
      - Claim-1: A-08(제안-실행 승인 게이트) 위반 여부
      - Claim-2: C-07(실측검증) 위반 여부
      - Claim-3: 오늘 산출물 Created/Modified/Verified/Withdrawn
        4분류 정확성

Source 범위: Source A(Claude Thread 원문, 메시지 1~278) +
      Repository(로컬 clone) — Source B(GPT 원문)는 참고용,
      Claim-1/2 판정에는 비필수(2026-07-20 기존 합의)

Artifact 범위: notes/*.md (오늘 생성/수정분)

포함: 위 Claim 3건, 대응 Source/Artifact 확인
제외: A-08/C-07의 전수 판정, REA Patch 27건 적용, RCA 정식 재실행,
      저장소 구조 변경, C-14 및 그 외 Rule (표본 확대는 Re-Pilot
      대상)

Success Criteria: (a) 3개 Claim 각각에서 Observation→Candidate→
      Evidence→Finding 흐름이 실제로 완주됨 (b) Confidence 등급이
      부여됨 (c) 서로 다른 검토자(Claude 작성, GPT Second-pass)가
      같은 Evidence로 같은 결론에 도달 가능한지 확인됨 (d) 모든
      필수 Template가 추가 수정 없이 실사용 가능해야 함(SOP
      자체의 검증)

Stop Criteria: 1차 기준(질적) — Pilot 진행 중 Reviewer가 "이
      상태로는 Method 검증을 더 이상 진행할 수 없다"고 판단하는
      경우 즉시 Stop. 2차 기준(참고용, 절대 규칙 아님) — Claim
      하나가 Source 부족이면 그 Claim만 Inconclusive 처리하고
      계속. Pilot Issue가 다수 누적되는 경우도 참고 신호일 뿐,
      최종 판단은 질적 기준을 따름

Exit Decision Target:
  ☑ Revise & Re-Pilot 예상 (근거: T-P0 자체가 CL-006으로 이미
    1회 개정된 이력이 있어, 실제 값 채우는 과정에서 추가 결함
    발견 가능성 높음)
  □ Freeze
  □ Inconclusive
  □ Stop / Re-scope
  □ Abort

Source Inventory Reference (T-P1): OR-preparation-source-
      inventory.md의 Evidence Source Inventory 표 (A,C,D,F는
      Available, B는 Available, E는 Need Unknown/Not Required
      후보)

Expected Deliverables:
  ☑ Observation Log
  ☑ Evidence Register
  ☑ Evidence Packet (Claim당 1개)
  ☑ Finding Register
  □ Walkthrough Record (P4는 이번 Pilot 축소범위 — 표본 3건규모라
    별도 Reviewer 재현 절차는 간이형으로만 수행)
  ☑ Exit Decision Record

Deferred Rule: Out-of-Scope Issue → Deferred Issue → Change
      Request Candidate (예: C-14, ZIP 처리 등은 이 Pilot 범위
      밖이라 발생 시 Deferred Issue로만 기록)

Prepared: Claude (Analyst)
Reviewer (Checked): GPT (Second-pass — Raw Source 접근권 있음,
      반증 가능)
Approver: 사용자
Change Owner: 사용자 (SOP/Template 변경 최종 승인)
```
