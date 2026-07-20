# Operation Review SOP v0.1

Status: Draft v0.1 (OR-METHOD-001 산출물, Freeze 아님)
근거: OR-METHOD-001 Final Baseline v0.1 (GPT, Manus 권고 흡수)

---

## 1. Mission

이 SOP는 정식 Operation Review가 아니라, OR-METHOD-001(방법론
설계 Work Package)의 산출물이다. 목적: OR SOP, Template Pack,
Pilot Instance, Change Control 네 가지를 설계·검증·동결하는 것.

## 2. Deliverables (4계층)

```
Operation Review SOP v0.1 → Template Pack v0.1 → OR-0000 Pilot
Instance → Change Log
```
각 층 독립 버전·변경이력 보유.

## 3. Lifecycle

```
Design → SOP v0.1 → Template Pack v0.1 → OR-0000 Pilot →
Change Review → Decision → SOP v1.0(Freeze 시에만)
```

## 4. Pilot 내부 구조 (P0~P5 — Pilot 전용, 공식 STEP 명칭 아님)

```
OR-0000 Pilot
├── P0 Review Charter & Authority
├── P1 Source Intake
├── P2 Evidence Lifecycle (Plan→Capture→Normalize→Classify→Verify→Packet)
├── P3 Findings & Knowledge
├── P4 Traceability Walkthrough
└── P5 Exit Decision
```
주의: 이 조직 전체(현재 진행 중인 OR-METHOD-001 자체)의 공식
명칭은 기존 STEP-1~STEP4를 유지한다. P0~P5는 Pilot Instance
내부에서만 쓴다.

## 5. Scope Cap

Pilot Contract 필수 항목: Review 대상 / Claim 범위 / Source 범위
/ Artifact 범위 / 포함·제외 / 성공기준 / 중단기준 / 종료기준 /
승인자 / Reviewer / Change Owner. 범위 밖 사항은 Deferred Issue로만
기록. **Pilot 중 범위 확대 금지.**

## 6. Information Model (공식 계층)

```
Raw Source → Observation → Candidate → Evidence → Finding → Decision
```
- Observation: Raw Source/Tool에서 얻은 미해석 관측값. 독립
  Register 없음. Claim 관련성 평가를 거쳐야 Candidate가 됨.
- Observation 자체는 Evidence도 Finding도 아님.

## 7. Core Rules

- **Candidate Discovery Rule**: 검색 결과=Candidate Discovery.
  검색 결과만으로 Finding 불가.
- **Zero Match Rule**: 검색결과 0건은 Finding 아님, 부재 Finding은
  별도 검증 필요.
- **Source Integrity Rule**: Source=기록의 저장소. 사실 주장은
  Evidence 확정 이후에만.
- **Artifact Independence Rule**: Derived Artifact≠Evidence,
  반드시 검증 거침.

## 8. Method Freeze Rule

Pilot 시작 이후 SOP/Template/Acceptance Rule/Workflow/Evidence
Rule을 직접 수정하지 않는다. 발견사항은 전부 Change Request로
기록.

## 9. Stop / Restart Rule

Pilot 중 방법론 유효성을 해치는 중대 결함 발견 시 Pilot 중단
가능. 사유는 Pilot Issue로 기록, 수정 후 Restart 여부 결정.

## 10. Pilot Issue Flow

```
Observation → Pilot Issue → Change Request → Review → Approval →
Next Version
```
Observation이 자동으로 Change Request가 되지 않음.

## 11. Method Decision / Operational Decision 분리

- **Method Decision**: SOP/Template/Workflow/용어 수정
- **Operational Decision**: 실제 Operation의 Finding/승인/실행

Pilot에서는 Method Decision만 수행. Operational Decision은
생성하지 않는다(Pilot 산출물은 방법론 검증용, 실제 Operation의
공식 Finding으로 자동 승격 안 됨 — Meta Boundary Rule).

## 12. Exit Decision (Pilot 종료 시 5가지 중 1개)

| 상태 | 의미 |
|---|---|
| Freeze | v1.0 동결 |
| Revise & Re-Pilot | 수정 후 Pilot 반복 |
| Inconclusive | 결론 부족 |
| Stop / Re-scope | 범위 재설정 |
| Abort | Operation 종료 |

Freeze가 유일한 성공 조건 아님.

## 13. Version Control

```
Issue → Change Request → Review → Approval → Next Version
```
원본은 항상 보존, 직접 덮어쓰지 않는다.

## 14. OR-METHOD-001 Exit Gate

다음 전부 충족 시 종료: SOP v0.1 작성 / Template Pack 작성 /
OR-0000 Pilot 완료 / Change Log 작성 / Exit Decision 완료.
Freeze 아니어도(Revise & Re-Pilot 등) 정상 종료 가능.

**주의**: 이 Exit Gate는 방법론(SOP/Template/Pilot) 완료 여부만
판정한다. 산출물의 저장소 보존(commit/push) 여부는 판정 대상이
아니다 — §14-A Thread Closing Gate 참조 (CL-009).

## 14-A. Thread Closing Gate (CL-009, Exit Gate와 별도)

목적: 세션 종료 전 모든 산출물이 안전하게 보존되었음을 확인한다.
OR-METHOD Exit Gate(방법론 완료)와는 성격이 다르다 — Method
Complete ≠ Repository Preserved(예: Freeze 완료됐어도 인터넷
장애로 push 실패하면 Thread는 못 닫음).

필수 조건:
```
□ Commit 완료
□ Push 완료
□ Closing Review 완료
□ 산출물 저장 확인
□ Thread Closing 승인
```
이 Gate를 통과하지 못하면 OR-METHOD가 Exit Gate를 통과했어도
Thread는 닫지 않는다.

## 15. Transition

OR-METHOD-001 종료 후, Method Decision이 완료된 경우에만 다음
Work Package(`OR-0001 Formal Operation Review`) 생성.

## 16. 역할 (축소 모델 — Manus 권고 반영)

정식 6역할 대신 각 기록에 3필드만 사용:
- **Prepared**: 작성자(Analyst 역할, 현재는 Claude)
- **Checked**: Second-pass Reviewer(현재는 GPT — "독립성"은
  Raw Source 접근권+반증가능성으로 판단, 모델이 다르다는 사실만으로
  자동 성립 안 함)
- **Approved**: Decision Authority(사용자)
