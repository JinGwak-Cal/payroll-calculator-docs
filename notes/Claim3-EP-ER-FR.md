# EP-0003 / ER-0004 / FR-0003 — Claim-3 (산출물 4분류)

```
ID: EP-0003 / Parent ID: PI-0000 / Root Pilot ID: PI-0000 /
Related IDs: SI-0001 / Current Stage: P2→P3
```

## Judgment Question

> "Repository(SRC-C) 상태만으로 오늘 산출물을 Created/Modified/
> Verified/Withdrawn 4분류로 정확히 나눌 수 있는가?"

## Evidence Plan

```
탐지 규칙: git status --short 직접 실행(추정/기억 아님)
Acceptance: 4분류 각각 최소 1건 이상 실제 사례로 확인
```

## 실측 결과 (Observation, 추측 아님)

```
$ git status --short
Modified(M): 4건 — absolute-rules.md, current-step.md,
  decisions.md, notes/research-backlog.md
Created(??): 30건 — notes/ 신규 파일 전체
```

## Evidence Register — ER-0004

```
유형: Fact
검증방법: bash 직접 실행 결과
결과:
  - Modified: git status로 100% 정확히 식별됨 (4건)
  - Created: git status로 100% 정확히 식별됨 (30건)
  - Withdrawn(예: AllowanceBrowser.draft.tsx): **git status로는
    전혀 안 보임** — 커밋 전에 생성→삭제된 파일은 git status에
    아무 흔적도 안 남음(untracked 상태에서 삭제하면 그냥 사라짐).
    실제로 `ls` 재확인해야만 "없다"는 걸 알 수 있고, "왜 없는지
    (원래 없었나/만들었다 지웠나)"는 git만으로는 구분 불가
  - Verified: git 개념 자체가 아님. "검증했다"는 사실은 대화
    로그(Source A)에만 남고 Repository(SRC-C)에는 안 남음
```

## Finding Register — FR-0003

```
Finding 유형: Method Finding

Claim: Repository(SRC-C) 단독으로는 4분류 중 2개(Created,
  Modified)만 정확히 판정 가능하고, 나머지 2개(Withdrawn,
  Verified)는 판정 불가능하다.

Basis: ER-0004

Interpretation: 이건 이번 Pilot에서 나온 **가장 구조적인
  발견**이다. Withdrawn/Verified는 Repository가 아니라 반드시
  Source A(대화 로그) 또는 별도 Audit Log가 있어야 판정 가능함
  → Evidence Source 설계 시 "어느 Source가 어느 분류를 담당하는지"
  를 명시해야 함(현재 SOP엔 이 매핑이 없음 — Change Request 후보)

Confidence: Confirmed (실측 기반, 반증 여지 낮음 — git 자체의
  구조적 한계이므로)

Decision Need: Change Request 후보 — "Evidence Source별 담당
  분류" 매핑을 SOP 또는 Template에 추가할지는 P5에서 결정
```
