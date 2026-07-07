# START HERE

## 최상단 고정 (항상 여기부터 갱신)

**Mission**: Bridge Step1 (Bridge Protocol / Bridge Interface /
Approval Console) 설계 및 최소 동작 구현

**Context**: 본 조사(approval Lens 토큰 절약 연구) 도중, 사람이
AI 간 데이터 중계자(Data Courier) 역할을 하며 발생하는 비용
(Human Mediation/Delegation/Attention/Question Loss)이 반복
확인되어, 연구를 계속하기 전에 이 병목을 해소하는 인프라를
먼저 구축하기로 결정함 (2026-07-04, Jin 승인).

**Entry Point**: `notes/direction-hypothesis.md`의
"2026-07-04 결정 — Bridge Architecture (Stage 0)" 섹션부터 읽기

**Next Action**: Bridge Step1 범위(Protocol/Interface/Console) 설계
착수. 완료 후 `notes/research-backlog.md`의 DEFER-001(approval
Relevance 판단)로 복귀.

---

새 AI 세션이든 새 사람이든, 이 프로젝트에 처음 들어오면 이 문서부터
읽는다. 아래 순서대로 진행하면 헤매지 않는다.

## 1. 프로젝트 목적
Payroll Calculator 개발 + Threshold Foundry(Collaboration Engineering
System) 운영. 규칙을 만드는 게 아니라 규칙이 탄생하는 과정을 설계함.

## 2. 현재 Direction
→ `notes/direction-hypothesis.md` 참조.
현재 최우선 항목: **Bridge Architecture (Stage 0)** —
Human Mediation Cost를 줄이기 위한 AI 간 협업 인프라.

## 3. 반드시 읽을 문서 (이 순서로)
```
1. notes/direction-hypothesis.md   ← 왜 지금 이 작업을 하는지
2. notes/automation-decision-matrix.md  ← 뭔가 하기 전에 자동화부터 확인
3. notes/capability-registry.md    ← 누가 무엇을 담당하는지
4. notes/research-backlog.md       ← 미뤄둔 작업, 왜 미뤘는지
```

## 4. 자동화 목록
→ `notes/automation-registry.md` (존재 목록)
→ `notes/automation-decision-matrix.md` (언제 쓰는지)

## 5. Bridge 사용법
아직 Step1 구축 전. 구축되면 여기 갱신.

## 6. 현재 진행중 연구
→ `notes/research-backlog.md`의 DEFER-001 (approval Lens Relevance
판단) — Bridge Step1 완료 후 재개 예정.

## 7. Entry Point (지금 무엇부터 해야 하는가)
Bridge Step1 설계: Bridge Protocol / Bridge Interface / Approval
Console. `notes/direction-hypothesis.md`의 "2026-07-04 결정 —
Bridge Architecture (Stage 0)" 섹션 참조.

## 8. 참고 — Evidence/Methodology 문서
- `notes/evidence-log.md` — 실제 관찰된 사건만 (E-001~E-009)
- `notes/methodology-notes.md` — 검증 안 된 메커니즘 가설 (MH-001~003)
- `notes/thread-closing-checklist.md` — 쓰레드 종료 전 점검용
- `notes/operational-cost-taxonomy.md` — 운영 비용 분류 (Source/Stage/Severity)

## 9. 매 쓰레드 종료 시
`notes/thread-closing-checklist.md` 사용. Persistence Check 반드시
확인 (로컬 커밋만 하고 GitHub push 안 하면 다음 쓰레드에서 소멸함 — E-008 참조).