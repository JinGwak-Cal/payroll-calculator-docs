# Research Backlog

상태값: Prerequisite(선행조건, 다른 기능의 전제) / Deferred(우선순위
밀림) / Blocked(다른 작업 완료 필요) / Waiting(Evidence 부족) /
Idea(아직 정식 제안 안 됨) / Candidate(OCP Capture 완료, 설계는
아직 시작 안 함 — Idea보다 구체적 문제정의는 있으나 Pilot 이전)

**Candidate 세부 추적 (2026-07-17 추가 — Reporting SOP 사례로
발견된 간극 반영)**: Candidate는 "아이디어가 생겼다"만 보장하지,
"실제 문서에 반영됐다"를 보장하지 않는다. Candidate 항목은
아래 4단계 중 현재 단계를 반드시 함께 표기한다.
- Candidate: 아이디어·문제정의는 생김, 귀속 위치 미정
- Assigned: 어느 문서/파일에 반영할지는 정해짐, 실제 반영 전
- Applied: 실제 문서에 반영 완료(diff 존재)
- Verified: 다음 쓰레드에서도 실제로 확인됨(merged-context 등
  통해 재확인 완료)
"Bridge로 넘기겠다"는 표현은 Assigned조차 보장하지 않으므로,
Bridge 인계 문구만으로 처리 완료로 간주하지 않는다.

**참고**: 이 문서 및 파트너 검토 응답에서 %/별점(예: "95% 승인",
"★★★★★")은 단독으로 사용하지 않는다. 별점·퍼센트를 표시할 때는
반드시 그 옆에 구체적 근거(현재 상태/관찰/영향/권고 등)를 함께
서술해야 하며, 근거 없이 숫자·별점만 제시하는 것은 금지한다
(2026-07-17 개정 — 기존 "전면 금지" 원칙을 "한눈에 보는 요약 효과는
유지하되 근거 병기를 필수화"로 완화. 근거: 사용자가 별점의 요약
가치는 인정하되, 근거 부재만 문제 삼음). **우려 기록(반영 안 함)**:
파트너가 "근거 병기 허용이 오히려 '★★★★★+근거3개'식 재남용으로
이어질 수 있다"는 우려 제기(2026-07-17). 사용자 본인이 직접
승인한 결정이라 지금은 되돌리지 않음 — 실제 남용 사례 발견 시
재검토.

| ID | 제목 | Status | Reason |
|---|---|---|---|
| DEFER-001 | approval Lens Relevance 판단 | Deferred | Bridge Architecture 우선 구축 결정 (Jin 승인) |
| DEFER-002 | Bridge Step2+ (Question Bridge: Card 단위 UI, 멀티 라우팅, 상태 시각화, 부분/편집 전달 등) | Idea | Step1(최소 동작) 완료 전까지는 설계 범위 확대 보류 |
| DEFER-003 | Role 축을 Operational Cost Taxonomy에 추가 | Idea | Bridge Step1 실 운영 후 필요성 확인되면 도입 |
| DEFER-004 | E-008(Persistence Loss) Evidence 번호 승격 여부 | Waiting | 반복 관찰(2회 이상) 필요, 현재 1회만 확인 |
| DEFER-005 | bridge-protocol.md / bridge-interface.md / approval-console.md | Idea | Bridge Step1 설계 완료 후 문서화 |
| DEFER-006 | release-checklist.md | Idea | 필요성 아직 미확인 |
| DEFER-007 | onboarding-checklist.md | Idea | START-HERE.md로 우선 대체, 부족함 확인되면 별도 생성 |
| DEFER-008 | reviews/active, reviews/completed 폴더 | Idea | 필요성 아직 미확인 |
| DEFER-009 | Bridge Verification에 Artifact Verification 추가 (Expected/Actual/Missing/Unexpected/Duplicate 자동 비교) | Idea | Bridge Step1에서, Replit push 결과와 예상 산출물 diff를 자동 대조하는 기능으로 설계 |
| DEFER-010 | 쓰레드 시작 시 Repository baseline(commit SHA) 자동 기록 | **Prerequisite** | Delayed Closing Baseline Check의 필수 입력값 — 이게 없으면 Delayed 판정 자체가 불가능함. 다른 백로그 항목과 달리 "나중에"가 아니라 "먼저" 처리 대상 |
| DEFER-011 | Multi-Target Ambiguity: 여러 Repl 프로젝트/저장소가 동시에 있을 때 지시 대상 혼동 | Idea | 실제 사례: ai-bridge-workbench Repl에 payroll-calculator-docs용 지시를 전달함. 해결책: 매 작업 전 Repository Context Declaration(AGENTS.md 0번 항목) 의무화로 완화 시도 중, 반복되면 Evidence 승격 검토 |
| DEFER-012 | Decision Relationship & Lifecycle Management — 새 Decision 기록 시 관련 기존 Decision의 상태·관계를 함께 재평가하는 절차 | **Candidate (단계: Candidate)** | 2026-07-17 AllowanceBrowser 구현 검토 중 실제 재현 2건(D-05-09가 D-PW-009에 대체된 사실을 놓침, "편집화면=테이블형 인라인" 확정 사실이 Repository 미반영) — 반복 근거로 우선순위 높음. 단, 지금 설계하지 않고 AllowanceBrowser 완료 후 최우선으로 재검토(OCP 복귀조건=완료 시점, 시간 기준 아님) |
| DEFER-015 | Reporting SOP — 실행 컨텍스트(채널)별 그룹화 후 그룹 내 번호 부여, 의존관계·진행상태 표시 | **Candidate (단계: Candidate)** | 원문 발단(Jin): 승인 유형별로 그룹 지어 번호 매기면 시작·종료 확인이 쉬움. 실제 형식: [A.채널1]/[B.채널2] 그룹 + A-1/A-2 순번 + 완료·진행중·대기 표시. GPT 검토 결론: 교정표(AI 오동작 교정) 성격 아님 — Reporting SOP/협업 운영 가이드로 분류. absolute-rules.md R18 추가 제안은 이 결론에 따라 철회. **2026-07-16 "0716_리절트그리드_재배치" 쓰레드에서 이미 한 번 "Candidate 지정"까지 갔으나 Assigned/Applied 단계로 못 넘어가고 유실된 전례 있음 — "Bridge로 넘기겠다"는 언급만으로는 Assigned도 보장 안 됨이 실증됨. 실제 파일화/Bridge 메모/폐기 중 미결정** |
| DEFER-016 | 가산수당 금액계산식이 목록(AllowanceList)과 Drawer 양쪽에 중복 구현됨 | Idea | D-PW-036 구현 중 발견. calc-engine이 Frozen Scope라 함수 공유 불가, floor(hours×wage×rate/100)이 2곳에 각각 존재. Replit 제안: src/lib 공용 헬퍼로 추출(calc-engine 밖이라 Frozen 무관). 수식 변경 시 2곳 동기화 필요 리스크 |
| DEFER-017 | 삭제 액션에 확인창(Confirm) 필요 여부 — D-PW-030 정책과 통합 검토 | Idea | D-PW-036에서는 HistoryScreen 기존 패턴(확인창 없음)과 일관되게 즉시삭제로 구현됨. D-PW-030의 "변경 시 확인창" 정책이 Drawer에도 원래 미구현 상태라, 삭제·편집 취소 확인 정책을 한 번에 재검토할 필요 |
| DEFER-018 | Retrieval Question Classification — 질문 유형별 검색 경로 분리 + 검증 선행 원칙 | **Applied (단계: Applied — R19 Assertion Gate로 실제 반영)** | 2026-07-18 "제수당" 사례로 발견. 최초 원인 추정(귀속통로 없음/클로징리뷰 누락)은 grep 미실시 상태에서 나온 성급한 진단이었고, 실측(grep) 결과 반증됨(D-PW-000/005/007에 이미 존재). 진짜 원인 둘: (1) SoT grep보다 conversation_search(과거 채팅)를 먼저/반복 사용, (2) 검증 전에 큰 원인부터 추론(교정표 #8/#9 위반). 질문유형별 경로: "결정됐나?"→SoT grep 우선 / "어디까지 구현됐나?"→current-step+reviews / "예전에 논의했잖아"→conversation_search+원본Thread / "왜 이렇게 결정됐나"→conversation_search→Decision Candidate→SoT. 추가로 "도메인 개념 존재"(SoT)와 "특정 화면에 그 개념을 적용하자는 UX 논의"(원본 Thread)는 서로 다른 층위이므로 SoT에서 개념을 찾았다고 원본 Thread Evidence가 무의미해지지 않음. **2026-07-18 추가**: 파트너가 이 사건을 "MEG/EBA(Evidence Before Assertion)"라는 신규 규칙으로 제안했으나, 확인 결과 claude-default-correction-table.md Row 7·8·9(0706~0711 확정, 현재도 운영 중)가 이미 동일 내용("됐습니다/없습니다 서술 금지, 실측 결과만 제출, 사실·추론·확인불가 구분") — 신규 등재 대신 기존 Row 7·8·9를 실제로 위반한 실증 사례로 재분류함 |

## DEFER-012 상세 (2026-07-17, Capture Complete)

- 재구성: 진화 경로 자체는 하나 — "번호매김/대분류 관행"도
  "OCP"도 둘 다 "운영 중 잃어버리지 않기 위해서"라는 같은
  문제의식에서 나온 결과. 문서상 직접 계보는 없지만 동일 뿌리.
- 핵심 통찰(파트너 제안): "무엇을 저장할까"보다 "언제 기존 것을
  다시 봐야 하는가"가 먼저다 — 저장 구조 설계보다 Trigger 정의가
  선행돼야 함
- 재검토 Trigger 후보 4개: ①새 Decision 생성 시 ②Current Step
  변경 시 ③Thread Closing 시 ④통합 Closing 시 — 이 네 시점에
  관련 기존 Decision을 재검토
- 경량 실천안(설계 전 임시 적용 가능): Decision 기록 시 "관련
  기존 Decision: 없음/D-XXX" + "영향: 신규/수정/대체/범위변경/참고"
  체크 한 줄만 추가
- Capture Complete: 이 이상 설계하지 않음. AllowanceBrowser 완료
  후 최우선으로 재검토 (기존 결정 유지)
- **2026-07-17 갱신**: STEP1(개별 Decision에 `#### Lifecycle`
  인라인 블록 추가 — Status/Supersedes/Superseded by/Trigger/
  Reason)은 설계 대기 없이 오늘부터 실제 가동 시작함(D-05-09,
  D-PW-031, D-PW-035, current-step.md 구조3에 실제 기록됨).
  STEP2(Trigger·Evidence 정식 분류), STEP3(decision-lifecycle.md
  독립 문서, 그래프 관리)는 여전히 Candidate로 보류

## DEFER-001 상세

- 계획됨: Distribution → Coverage → Purity → Relevance → Sampling → Observation
- 진행 상태: Purity까지 완료. Relevance 단계 진입 직전 Bridge Architecture로 우선순위 전환.
- 재개 조건: Bridge Step1 구축 완료 후
- 필요 자산: bundles/approval_bundle.md, bundles/approval_bundle.json (Jin 로컬에 이미 생성됨, pipeline.py 실행 결과)

## DEFER-009 상세 (근거 Evidence)

- 계기: Replit Agent가 "완료" 보고했으나, 실제 GitHub 확인 결과
  evidence-log.md의 E-009, methodology-notes.md의 MH-003이
  누락된 채 push됨 (session2.diff 반영 시도, 2026-07-04)
- Supporting 사례 2: thread-closing-checklist.md 전체 내용이 통째로
  중복 반복된 사고. 독립 Evidence(E-010 등)로 분리하지 않고, 지금은
  "Artifact Verification 부재 → 중복/누락 미검출"로 동일 원인 설명이
  가능하므로 DEFER-009의 Supporting 사례로 통합 관리한다.
- 필요 절차: Expected Deliverables 목록 → Actual(GitHub 실제 상태) →
  Missing/Unexpected/Duplicate 자동 비교 → Verified 여부 출력
- 표현 주의: "충돌 없음"과 "release-gate/Actions 검증 통과"는
  다른 개념. Bridge Verification은 후자까지 확인해야 함.

### E-010 승격 기준 (지금은 등록하지 않음)

다음 중 하나라도 재현되면 그때 "E-010. Duplicate Artifact"로 독립
Evidence 분리:
- 서로 다른 상황에서 문서 중복이 다시 발생
- 다른 AI/파이프라인에서도 동일한 중복 생성 문제 발생
- Artifact Verification(DEFER-009) 도입 이후에도 중복이 계속 발생

---

## DEFER-012 Evidence Collection Protocol (ECP)

- 상태: Idea/Candidate
- 목적: Thread Closing Review STEP0(원문 확보)의 최적 수집 방법 확립
- 비교 대상: Claude 자체기능 / ChatGPT 자체기능 / 공식 Export data /
  브라우저 저장도구(SingleFile) / 브라우저 자동화(Playwright) /
  ChatExport AI
- 평가 대상: Conversation(텍스트) / AI Generated Asset(이미지·파일) /
  User Attachment(첨부) / Metadata
- 1차 실측 (2026-07-13, ChatExport AI 무료판):
  - Claude: 텍스트·아티팩트·첨부파일 전부 실제 파일 보존 확인 →
    Accepted 후보
  - ChatGPT: 텍스트만 성공, 첨부파일 8건 중 8건 "Could not resolve
    download URL" 실패 → 별도 도구 필요
  - 도구 결함: 동일 zip 내 conversation.md 헤더와 manifest.json
    title 불일치 사례, 메시지 수 공식 JSON(37개) 대비 7배 과다
    보고(255개) 사례 발견 — 서드파티 메타데이터 단독 신뢰 금지
    원칙의 근거
- 다음 후보: ChatGPT Pro Tools/ChatGPT Library Exporter(이미지 전용,
  미검증), Playwright PoC(장기 처방, 미착수)
- 재검토 조건: Playwright PoC 착수 시 또는 GPT 자산 전용 도구 검증 시

---

## DEFER-013 default-correction-handbook.md 실재 여부 결정

- 상태: 미결정 (경량 Task)
- 배경: claude-default-correction-table.md와 event-card-template.md
  양쪽에서 "상세 배경·Lifecycle·SOP는 notes/default-correction-
  handbook.md 참고"라고 참조하지만, 해당 파일은 저장소에 존재하지
  않음 (2026-07-13 확인)
- 결정 필요 사항: 실제로 그 파일을 만들 것인지, 아니면 참조 문구
  자체를 제거할 것인지
- 재검토 조건: 다음에 이 참조를 실제로 열어보려다 다시 없다는 것을
  발견하는 시점 (또는 임의 시점에 정리)

---

## DEFER-014 Closing Review 검증 자동화 — Manifest-driven 구조 전환

- 상태: Idea/Candidate
- 배경: pr-gate.yml/post-merge-gate.yml을 이번 클로징(2026-07-13)
  전용으로 하드코딩함(v0). 다음 클로징마다 workflow 파이썬 코드
  자체를 수정해야 하는 구조는 "자동화가 아니라 자동화 코드 재작성
  절차"가 됨
- 목표 구조: workflow는 고정, `closing-review-manifest.json`을
  매 클로징마다 생성해서 검증 엔진이 그 manifest를 읽게 함
  (Local Preflight/PR Gate/Post-Merge Gate 3단이 동일 manifest 공유)
- 재검토 조건: 다음 클로징 리뷰 착수 시, 또는 pr-gate.yml을 두 번째로
  수동 갱신하게 되는 시점
