# AI Collaboration Rules

이 문서는 이 저장소에서 작업하는 모든 AI 코딩 에이전트(Replit Agent
등)가 작업 시작 시 가장 먼저 참고해야 하는 규칙입니다.

**이 문서는 Payroll Calculator Repl 환경(로컬 Git 저장소
`payroll-calculator`와 GitHub Contents API 대상
`JinGwak-Cal/payroll-calculator-docs`를 함께 다루는 환경) 기준으로
작성되었습니다.** 다른 Repl(예: ai-bridge-workbench)은 역할이 다르므로
별도 정책이 필요할 수 있습니다.

---

## 0. Repository Context Declaration (MANDATORY, 최우선)

작업을 실행하기 전, 매번 먼저 아래를 보고합니다:

```
[Repository Context]
Target repository:
Reason:
Access method:
Working directory (if any):
Current branch:
```

Repository rules:
1. Target이 로컬 `payroll-calculator` 프로젝트면 → Local Git만 사용.
2. Target이 `JinGwak-Cal/payroll-calculator-docs`면 → 명시적으로
   로컬 clone이 제공되지 않는 한 GitHub Contents API 대상으로 취급.
3. `payroll-calculator-docs`에 로컬 Git 저장소가 존재한다고
   가정하지 않는다.

대상 저장소가 모호하면, 그때만 작업을 멈추고 확인을 기다린다
(모호하지 않으면 매번 승인받을 필요 없이 진행).

---

## 1. Patch Application Policy (MANDATORY)

If `git apply` fails:

DO NOT:
- fuzzy apply
- write a custom patch parser
- reconstruct the patch
- search for similar lines
- apply patches heuristically
- manually merge based on the diff

The ONLY permitted actions are:

1. Run: `git apply --check <patch>`
2. Report the exact error output.
3. STOP and wait for further instructions.

If complete replacement file contents are provided instead of a patch:

DO NOT use patch logic. Overwrite the entire file exactly as provided.
Do not merge, do not preserve surrounding text, do not reconstruct.

This policy is mandatory for every patch operation in this project
unless explicitly instructed otherwise in the same conversation.

## 2. Verification Before Reporting (MANDATORY)

- Trust actual repository state over your own memory or previous
  completion reports. Never repeat a previous completion report
  without re-verifying against current state first.
- Verification method depends on access method (see Section 0):
  - Local Git repository: `git rev-parse HEAD`, `git log origin/<branch> -1`,
    confirm the SHA actually changed after your push.
  - GitHub Contents API repository: re-fetch the file content via API
    (GET) after writing (PUT), and confirm the expected string/section
    actually appears in the fetched content — not just that the API
    call returned success.
- Do not declare completion based on assumption or a prior report.
  Always show the fresh verification output.
- Before reporting completion, confirm that the repository you just
  verified matches the Target repository declared in the Repository
  Context (Section 0). A verification against the wrong repository
  is not a valid verification.
- If verification cannot be completed for any reason, do not declare
  the task completed. Explicitly report "Verification incomplete"
  and explain why.

## 3. Approval Rules

- Do not push directly to `main`. Push to `ai/draft`; the `ai-push.yml`
  workflow handles validation, PR creation, and release-gate approval.
- Do not merge without human release-gate approval.

## 4. Evidence Rules

- See `notes/evidence-log.md` Candidate Entry Criteria before adding
  new Evidence entries. Observation and Mechanism (Hypothesis) must
  stay separated — mechanism explanations go in
  `notes/methodology-notes.md`, not `evidence-log.md`.

## 5. Commit Rules

- One logical change = one commit with one descriptive message.
  Do not split a single logical change into per-file commits unless
  explicitly asked.

## 6. No Guessing Rules

- Never assume Evidence/identifier numbers (e.g. E-009, MH-003) from
  memory. Always check current repository state first
  (`notes/evidence-log.md`, `notes/methodology-notes.md`) and assign
  the next available number. See `notes/thread-closing-checklist.md`
  Identifier Check section.

---

참고 문서 (더 자세한 내용):
- `notes/automation-decision-matrix.md` — 어떤 작업에 어떤 자동화를 쓰는지
- `notes/capability-registry.md` — 누가 무엇을 담당하는지
- `notes/START-HERE.md` — 프로젝트 전체 온보딩
