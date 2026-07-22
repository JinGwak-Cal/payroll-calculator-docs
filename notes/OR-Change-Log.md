# Change Log — OR-METHOD-001

원본 3개 문서(OR-preparation-source-inventory.md,
source-capture-method-reference.md, OR-STEP1-A-evidence-plan.md)는
**삭제·덮어쓰기 하지 않고 그대로 보존**. 아래는 그로부터 파생된
개정 이력.

---

## CL-001

- 대상: OR-preparation-source-inventory.md → OR-SOP-v0.1.md §14
  (Exit Gate), T-P0(Template)로 재구성
- 변경 사유: Work Package Contract가 "최초 정식 OR 수행"을 목표로
  선언 + STEP0→STEP1 "Go" 선언 — 방법론 미완성 상태에서 실행을
  선언한 자기모순 발견 (Manus 지적)
- 해결하는 설계결함: 설계 단계와 실행 단계의 혼동
- 적용 시점: 2026-07-20, OR-METHOD-001 채택 시

## CL-002

- 대상: OR-preparation-source-inventory.md의 F(파트너 산출물) 분류
  → OR-SOP-v0.1.md §6 Information Model
- 변경 사유: 자기 생성 문서(REA/RCA 등)를 독립 Source로 취급한 것은
  순환논증(Manus 지적)
- 해결하는 설계결함: Source/Artifact/Evidence/Finding 미분리로
  인한 순환논증 위험
- 적용 시점: 2026-07-20

## CL-003

- 대상: OR-STEP1-A-evidence-plan.md의 Acceptance("원문과 일치")
  → OR-SOP-v0.1.md §7 Candidate Discovery Rule
- 변경 사유: grep 매치 건수를 곧바로 위반 판정 근거로 쓰면
  맥락·승인여부·시점 확인이 생략됨(Manus 지적)
- 해결하는 설계결함: grep=Candidate Discovery일 뿐 Finding 아님을
  명시 안 했던 것
- 적용 시점: 2026-07-20

## CL-004

- 대상: (신규) 역할모델
- 변경 사유: 6개 formal role은 현재 실제 참여자(사용자·Claude·GPT)
  규모에 과설계(GPT 지적) + "GPT=Independent Reviewer" 자동성립
  아님(Manus 지적, Raw Source 접근권+반증가능성 조건 필요)
- 해결하는 설계결함: 역할 정의 없음 + 과도한 역할 확장 위험
- 적용 시점: 2026-07-20, Prepared/Checked/Approved 3필드로 축소

## CL-006

- 대상: OR-Template-Pack-v0.1.md T-P0 (Pilot Contract → Pilot
  Control Contract로 승격)
- 변경 사유: 12개 필수 체크리스트 대조 결과 Goal/Exit Decision
  Target/Change Owner/Source Inventory Reference/Deliverables/
  Deferred Rule 누락, Reviewer·Approver는 필드 자체는 있으나
  T-P0에서 참조 안 됨(Traceability 부족)
- 해결하는 설계결함: T-P0가 시작 양식 수준에 그쳐 Pilot 전체를
  통제하지 못했던 것
- 적용 시점: 2026-07-20, 6개 항목 추가로 T-P0를 Pilot 전체
  통제문서로 승격

## CL-007

- 대상: OR-0000-pilot-contract.md
- 변경 사유: Review 대상을 "오늘 쓰레드 Rule 준수 여부"로 적으면
  Pilot이 오늘 Thread를 심사하는 것처럼 보임(GPT 지적) — Goal이
  방법론 검증인데 대상이 실제 심사처럼 뒤섞임. Success Criteria에
  Template 실사용성 검증 항목 누락. Stop Criteria의 양적 기준
  ("3건 이상")이 자의적
- 해결하는 설계결함: Review Target/Pilot Material 미분리, SOP
  자체 검증 기준 누락, Stop 기준의 임의성
- 적용 시점: 2026-07-20, Review Target/Pilot Material 분리 +
  Success Criteria (d) 추가 + Stop Criteria 질적기준 우선화

## CL-008

- 대상: OR-Template-Pack-v0.1.md (전체 템플릿에 Traceability
  필드 추가, T-IDX 신설)
- 변경 사유: 산출물 간 참조관계가 ID체계·역참조 필드 없이는
  확보 안 됨. Parent ID 단독으로는 계층은 표현되나 관계(한 Evidence
  Packet이 여러 Evidence Register를 묶는 경우 등)는 표현 불가
  (GPT 지적)
- 해결하는 설계결함: Traceability 미확보, 다대다 관계 표현 불가,
  단계별/소속별 일괄 조회 불가
- 적용 시점: 2026-07-20, ID체계(PI/SI/EP/OB/ER/EPK/FR/WD/XD/CR) +
  공통 4필드(Parent ID/Root Pilot ID/Related IDs/Current Stage) +
  T-IDX(Traceability Index, 고아·끊긴참조 검증규칙 포함) + CR에
  Origin/Target 추가

## CL-009

- 대상: OR-SOP-v0.1.md §14 (Exit Gate 옆에 §14-A 신설)
- 변경 사유: Push 완료를 OR-METHOD Exit Gate에 넣자는 제안이
  있었으나, 방법론 완료 판정(Exit Gate)과 산출물 보존 절차(Git
  운영)는 성격이 다름(GPT 지적) — "Method Complete ≠ Repository
  Preserved" (예: Freeze 완료돼도 인터넷 장애로 push 실패 시
  Thread는 못 닫아야 함)
- 해결하는 설계결함: 방법론 판정 기준과 운영 절차의 결합
- 적용 시점: 2026-07-20, Thread Closing Gate를 Exit Gate와 별도
  섹션(§14-A)으로 신설 — Commit/Push/Closing Review/산출물저장확인/
  Thread Closing 승인 5개 조건

## CL-010

- 대상: OR-SOP-v0.2.md, OR-Template-Pack-v0.2.md (신규 파일,
  v0.1은 보존)
- 변경 사유: OR-0000 Pilot Exit Decision(Revise & Re-Pilot)에서
  도출된 CR-001~003 반영
- 해결하는 설계결함: (CR-001) 탐지규칙 설계 가이드 부재 (CR-002)
  Source-분류 매핑 부재 (CR-003) 재현성 검증의 형식적 수행
- 적용 시점: 2026-07-20
  - CR-001: T-P2-1에 Search Strategy(사건고유/행위/자기평가(보조)/
    제외 키워드) 하위섹션 추가
  - CR-002: T-P1에 Source Capability Mapping 표 추가
  - CR-003: SOP P4 설명 + T-P4에 "정식 독립재현 vs 간이형(Pilot
    전용)" 구분 필드 추가, 정식 OR에서 간이형 선택 시 Method
    Freeze Rule 위반으로 명시
- 최소증분 원칙 준수: CR-001~003 외 신규 아이디어 추가 없음

