# Research Backlog

상태값: Prerequisite(선행조건, 다른 기능의 전제) / Deferred(우선순위
밀림) / Blocked(다른 작업 완료 필요) / Waiting(Evidence 부족) /
Idea(아직 정식 제안 안 됨)

**참고**: 이 문서 및 파트너 검토 응답에서 근거 없는 %/별점(예: "95%
승인", "★★★★★")을 사용하지 않는다. 가중치 미확정 상태에서 확신을
숫자로 표현하지 않는다는 원칙(Experimental Score 도입 시 이미 합의)을
검토 코멘트에도 동일하게 적용한다. 대신 구체적 항목별 동의/반대와
근거만 서술한다.

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
