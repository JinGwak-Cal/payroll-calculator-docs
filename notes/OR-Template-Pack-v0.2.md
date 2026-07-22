# Operation Review Template Pack v0.2

Status: Draft v0.2 (v0.1 보존, notes/OR-Template-Pack-v0.1.md 참조). 각 양식에 Prepared/Checked/Approved 3필드 포함.

## 공통 Traceability 필드 (CL-008, 모든 템플릿 공통 헤더)

ID 체계: PI(Pilot Instance/Contract) / SI(Source Intake) /
EP(Evidence Plan) / OB(Observation) / ER(Evidence Register) /
EPK(Evidence Packet) / FR(Finding) / WD(Walkthrough) /
XD(Exit Decision) / CR(Change Request)

모든 산출물(T-P0 제외 — 자신이 Root)에 아래 4필드 필수:
```
ID:
Parent ID: (직접 상위 문서 — 계층 표현)
Root Pilot ID: (최상위 Contract — 항상 PI-0000 형태로 즉시 점프)
Related IDs: (Parent 외 추가로 참조/결합하는 ID들 — 관계 표현.
  예: EPK가 여러 ER을 묶을 때)
Current Stage: (P0~P5 중 현재 속한 단계 — grep P2 등으로 단계별
  조회 가능하게)
```

---

## T-P0. Pilot Control Contract (Review Charter) — CL-006 승격판

```
Pilot ID:
Goal:
Review 대상(Operation):
Claim 범위:
Source 범위:
Artifact 범위:
포함:
제외:
Success Criteria:
Stop Criteria:
Exit Decision Target:
  □ Freeze
  □ Revise & Re-Pilot
  □ Inconclusive
  □ Stop / Re-scope
  □ Abort
Source Inventory Reference (T-P1):
Expected Deliverables:
  □ Observation Log
  □ Evidence Register
  □ Evidence Packet
  □ Finding Register
  □ Walkthrough Record
  □ Exit Decision Record
Deferred Rule: Out-of-Scope Issue → Deferred Issue → Change
  Request Candidate
Prepared:
Reviewer (Checked):
Approver:
Change Owner:
```

## T-P1. Source Intake Register

```
| Source ID | 유형(Raw/Reference/Derived/Execution/Archive) |
  상태(Available/Missing/Need Unknown/Not Required/Deferred) |
  Physical | Operational | 비고 |
```
Need Unknown 전이 규칙: 자동 Go 불가. (a)Not Required (b)Deferred
with accepted risk (c)Missing+Hold (d)Available after intake 중
하나로만 전이.

### Source Capability Mapping (CL-010/CR-002, 신규)

어느 Source가 어느 판정을 담당할 수 있는지 먼저 명시. 근거(OR-0000
Claim-3): Repository는 Created/Modified만 판정 가능, Withdrawn/
Verified는 원천적으로 판정 불가(구조적 한계) — 매 Pilot마다
아래 표를 채운다.

```
| 분류 대상 | 담당 Source | 이유/한계 |
|---|---|---|
| Created/Modified | Repository(git status) | 직접 판정 가능 |
| Withdrawn | 대화 Source(Raw Source) | git엔 흔적 안 남음(커밋 전 삭제 시) |
| Verified | 대화 Source 또는 별도 Audit Log | git 개념 아님 |
```

## T-P2-1. Evidence Plan

```
Claim ID:
분석 단위:

Search Strategy (CL-010/CR-001, 탐지 규칙 설계 전 먼저 정의):
  - 사건 고유 키워드(domain-specific, 원본 turn 직결 가능성 높음):
  - 행위 키워드(사용자/AI 행동 서술):
  - 자기평가 키워드(보조용, "위반/실수" 등 — 원본 turn과
    직결 안 될 위험 있음, 단독 사용 금지):
  - 제외 키워드:

탐지 규칙(Method): (위 Search Strategy 기반으로 구체화)
포함/제외 기준:
수용 기준(Acceptance):
```
주의: 결과를 본 뒤 탐지 규칙을 바꾸지 않는다(Method Freeze Rule).
근거(OR-0000 Pilot): Claim-1(자기평가 키워드만 사용)은
Insufficient, Claim-2(사건 고유 키워드 사용)는 Supported로
갈렸음 — Search Strategy를 먼저 명시하면 이 차이를 설계
단계에서 예방 가능.

## T-P2-2. Observation Log (독립 Register 아님, Evidence Plan 하위 임시기록)

```
Observation ID | Source ID | locator | raw text/snippet |
Claim 관련성(Y/N) → Y면 Candidate로 승격
```

## T-P2-3. Evidence Register

```
Evidence ID | Candidate ID | 유형(Fact/Context/Counter-evidence/Gap) |
검증자 | 검증방법 | 반증검토 | 결과
```

## T-P2-4. Evidence Packet (Finding 확정 전 최소 단위)

```
Claim:
Evidence refs:
반대 근거(Counter-evidence):
판정 규칙(어느 Rule/버전):
결론(잠정):
```

## T-P3. Finding Register

```
Finding ID | 유형(Rule Compliance/Decision/Pattern/Failure/
  Calibration/No Finding) | Claim | Basis(Evidence ID) |
  Interpretation | Confidence(Confirmed/Supported/Tentative/
  Insufficient) | Decision Need
```

## T-P4. Traceability Walkthrough Record

```
Walkthrough 대상 Finding ID:
Reviewer(Checked):
재현 유형(CR-003 신규): □ 정식 독립재현(제3자, Raw Source 접근권
  보유) □ 간이형(Pilot 전용 예외, 작성자 관점분리) — 정식 OR에서
  간이형 선택 시 Method Freeze Rule 위반으로 간주, Pilot 전용
재현 절차(Source→Evidence→Finding 추적):
결함 발견 여부:
결론: 승인/재작업
```

## T-P5. Exit Decision Record

```
Pilot ID:
Exit 상태(Freeze/Revise&Re-Pilot/Inconclusive/Stop-Rescope/Abort):
근거:
Method Decision 목록(있다면):
Prepared / Checked / Approved:
```

## T-CC. Change Request / Change Log

```
Change ID: (CR-XXXX)
Parent ID / Root Pilot ID / Related IDs / Current Stage: (공통필드)
Origin ID: (이 변경이 발견된 인스턴스 — 예: WD-0001)
Target ID: (이 변경이 수정할 대상 — 예: T-WD Template, 또는 SOP 조항)
대상(SOP/Template/Rule/Workflow):
변경 사유:
Before → After:
해결하는 설계결함:
적용 시점:
Prepared / Checked / Approved:
```

## T-IDX. Traceability Index (CL-008 신규)

Pilot 전체의 모든 ID를 한 줄씩 등록. grep으로 고아 문서(Parent
없음)·존재하지 않는 Parent 참조·특정 Pilot 소속 전체 문서·특정
단계(Stage) 전체 문서·미완료 문서를 즉시 찾을 수 있게 하는 목적.

```
| ID | Type | Parent ID | Root Pilot ID | Related IDs | Current Stage | Status |
|---|---|---|---|---|---|---|
| PI-0000 | Contract | — | PI-0000 | — | P0 | Active |
```

검증 규칙: Parent ID가 비어있는데 자기 자신이 Root가 아니면 →
고아(Orphan) 문서. Parent ID가 이 표에 없는 ID를 가리키면 → 끊긴
참조(Broken Reference). 둘 다 Pilot Issue로 기록.
