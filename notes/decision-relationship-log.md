# decision-relationship-log.md

**성격**: 이제부터 정식 방식은 **각 Decision 항목(decisions.md)
옆에 `#### Lifecycle` 블록을 인라인으로 붙이는 것**입니다(Status/
Supersedes/Superseded by/Trigger/Reason). 이 파일은 그 인라인
블록들을 한눈에 모아보는 **집계용 색인**입니다 — Trigger별 빈도
분석 등 나중 분석에 씁니다. 개별 Decision을 읽는 사람은 이 파일을
몰라도 되고, decisions.md 안의 Lifecycle 블록만 보면 됩니다.

## 인라인 Lifecycle 기록 규칙

```md
#### Lifecycle
- Status: Active / Partially Superseded / Superseded / Archived
- Supersedes: (있으면 D-XXX)
- Superseded by: (있으면 D-XXX)
- Trigger: UX Review / Preflight / Code Inspection / User Test /
  Bug / Performance / Architecture / External Requirement
- Reason: 왜 바뀌었는지 한두 문장
```

## 색인 (decisions.md에 실제로 인라인 기록된 것들)

| Decision | Trigger | Superseded by | 비고 |
|---|---|---|---|
| D-05-09(2606.18) | UX Review / Preflight | D-PW-009, D-PW-035 | 진입경로+편집범위 둘 다 부분 대체 |
| D-PW-031(2026-07-13) | Preflight | D-PW-035 | 메모 구현 누락 발견·복구 |
| D-PW-035(2026-07-17, 신규) | Preflight | 없음(Active) | P-1/P-2/P-3 확정 |
| current-step.md 구조3 편집화면 항목 | Preflight | D-PW-035 | 필드별 하이브리드로 정정 |


