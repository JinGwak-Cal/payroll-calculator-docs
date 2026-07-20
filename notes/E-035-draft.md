## E-035 — Operation Pipeline 부재로 인한 개발 중단 Loss (Pilot 제안 → 3자 토론 → Phase 분리 합의)

### ① 사건
- 사용자가 Pilot 운영 개선 제안서(이벤트 기반 상기 / 통합 후속 검토
  목록 / QVU) 공유
- Claude(본 세션)가 grep 실측으로 기존 SoT 대조 → 3개 항목 모두
  기존 문서(Thread Closing Review, Concept Registry System, Bridge
  D-BR-001, 교정표 Gate Row1)와 부분 중복 확인, Evidence Log 등재만
  제안
- 사용자가 파트너(GPT)의 반박 3건(배경 5가지 설명, Registry-Pipeline
  구분 반박, GPT Operation Pipeline 초안) 전달
- 파트너는 "Registry 통합이 아니라 Pipeline 통합"이라 반박하며
  Threshold Foundry Phase1(단기)/Phase2(장기, 출시 후) 분리안과
  "63 Matrix" 태깅 개념을 제시
- 사용자가 이 토론 자체가 개발(Paycheck Workbook STEP2
  AllowanceBrowser 착수 대기 중)을 여러 메시지째 세워두고 있다는
  자기지시적(self-referential) Loss를 직접 지적
- 사용자 최종 지시: 장기 근본해결은 "지금까지 논의된 사항 기록"만
  하고, 단기 임시방편은 "파트너 안대로 파이프라인을 실제로 구축"

### ② 의도
- Threshold Foundry(장기, "규칙이 탄생하는 과정을 설계")와 별개로,
  개발 중 발생하는 운영 아이디어가 흩어지지 않고 최소한으로
  유지되게 하는 것이 목적
- current-step.md Release Priority(2026-07-06) / D-TF-003
  (2026-07-11) 원칙("출시 속도 우선, Threshold Foundry는 Evidence만
  축적, Rule 승격은 출시 이후")과 충돌하지 않는 범위에서만 실행

### ③ 결정
- 장기설계(Threshold Foundry Phase2: Pattern Discovery → 63 Matrix
  → Threshold → Pilot → Promotion → Correction Table)는 지금
  SOP화하지 않고 이번 Event 기록으로만 남긴다
- 단기(Phase1)만 즉시 도입: Operational Event → Evidence(raw
  기록, Thread/Conversation/Related Decision 등 Context Link
  포함) → Operational Classification(63 Matrix를 대표 구현으로
  포함하는 상위 분류 단계) → Deferred/Candidate 저장 → 즉시
  개발 복귀
- 별도 문서 `notes/operation-pipeline-phase1.md` 신설(Draft)
- 63 Matrix 태깅을 "63 Matrix 전용"이 아니라 "Operational
  Classification"이라는 상위 개념으로 재배치 — 향후 TTP/Bridge/
  Layer 등 다른 분류 엔진 추가 가능성을 열어둠(파트너 제안 반영,
  2026-07-17)

### ④ 근거
- current-step.md 구조2: "Threshold Foundry는... 새 방법론/Rule
  승격(Promotion)은 출시를 우선하며 상황에 따라 유연하게 판단한다"
- notes/direction-hypothesis.md: Discovery Domain/Operational
  Domain 구조 (Status: Candidate, "최종 구조로 확정된 것은 아니다")
- concept-system/cards/c-00021-registry-system.md: "단일 Candidate
  Registry로는... 4종 구성으로 식별됨" — 과거 단일 Registry 통합
  시도가 부족 판정된 이력 (Registry 통합과 Pipeline 통합은 별개
  라는 근거)
- 63 Matrix: 저장소 전체 grep 결과 0건이었으나(2026-07-17, 2회
  확인), 같은 날 사용자가 제시한 TTP 표 제안 문서(표1~표5)로 실체
  확인됨 — TTP Lifecycle 7행(Closing Review~Next Baseline) × Micro
  템플릿 9열(①What~⑨Next Trigger) = 63. 저장소 문서가 아니라 이번
  쓰레드 내 사용자 제공 원문이 63 Matrix의 최초 정의였음
- 이 grep 0건 자체가 E-035의 핵심 근거다: 63 Matrix는 실제로는
  이미 (다른) Thread 안에서 정의되어 있었지만 Repository에 반영되지
  않아 부재로 확인된 것 — 즉 "Thread에서 태어난 운영 자산이
  Repository까지 도달하지 못하는 Loss 패턴"의 실제 사례(파트너
  지적, 2026-07-17)
- 이 사건은 운영 개념이 부족해서 발생한 것이 아니라, 이미
  존재하는 운영 자산이 Repository까지 연결되지 못한 결과 발생한
  Loss다 (파트너 지적, 2026-07-17)

### ⑤ 영향
- Impact: SoT 문서(absolute-rules.md / decisions.md /
  current-step.md) 변경 없음. notes/ 신규 Draft 파일 2건 추가만
  (본 E-035 + operation-pipeline-phase1.md)
- Open Items: [해소] 63 Matrix 실체는 확인됨(위 근거 참조).
  [미정의 유지] 개별 셀 코드 표기법(M12/M27/M48 등 번호 규칙)은
  아직 미확정 — 필요 시 별도 확정
- 다음 Thread Bridge 시 이 Draft 2건의 존재를 함께 전달할 것
