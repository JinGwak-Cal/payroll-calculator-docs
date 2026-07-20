# RCA (Rule Compliance Audit) v0.1 Draft

REA(Rule Execution Audit)가 "Rule이 실행 가능하게 설계됐는가"를
감사한다면, RCA는 "실제 운영에서 그 Rule이 지켜졌는가"를 감사한다.
둘은 하나의 운영 루프를 이룬다:

```
Rule → REA(설계검증) → 운영 → RCA(운영감사) → Evidence
  → Rule Evaluation → REA (반복)
```

---

## 1. 목적 (Purpose)

RCA는 AI가 실제 운영 과정에서 적용 가능한 Rule을 일관되게
준수했는지를 객관적인 Evidence에 기반하여 검증하기 위한 감사
방법론이다. RCA는 Rule을 설계하거나 수정하지 않는다. 운영 중
Rule Compliance를 검증하고, 재현 가능한 Evidence를 축적하여
행동 개선과 Rule 개선의 근거를 제공하는 것을 목적으로 한다.

## 2. 정의 (Definition)

RCA란, 실제 대화에서 발생한 Trigger Occurrence를 기준으로,
적용 가능한 Rule이 의도한 방식으로 수행되었는지를 Evidence에
근거하여 검증하는 감사 절차이다.

## 3. 적용 범위 (Scope)

**감사 대상**: Trigger Occurrence / Applicable Rule / 실제
Action / 실제 Output / Evidence

**감사 대상 아님**: Rule 자체의 설계 품질 / Rule 수정 여부 /
새 Rule 정의 / 방법론 변경 — 이들은 별도 Rule Evaluation(→REA
피드백)으로 남긴다.

## 4. 핵심 원칙 (Core Principles)

- **P1. Evidence First** — 모든 판정은 Evidence에 근거한다.
- **P2. Audit Before Improvement** — 감사와 Rule 개선을 혼동하지
  않는다.
- **P3. Stable Criteria** — 감사 도중 새로운 판정 범주를 만들지
  않는다. 판정이 어려운 사례는 Ambiguity Log에 기록한다.
- **P4. Reproducibility** — 동일 Evidence에 대해 다른 감사자도
  동일한 판정을 내려야 한다.

## 5. 감사 절차 (Audit Process)

1. Audit Readiness 확인 (방법론 확정?/Scope 확정?/감사≠설계변경
   합의?)
2. Scope 선언
3. Trigger Occurrence 식별 (REA Q1 재사용 + 실제 대화 Evidence)
4. Applicable Rule 식별 (한 Event에 복수 Rule 가능, 전부 기록)
5. Compliance 판정 (Executed/Suppressed/Violated — 3분류 고정,
   즉석 신규범주 생성 금지)
6. Evidence 기록
7. Ambiguity 기록 (판정 불가 사례 → Ambiguity Log, 감사기준은
   안 바꿈)
8. Summary 작성
9. Improvement Candidate 분리 (Rule 수정은 여기서 안 함, 후보만)

## 6. 감사 산출물 (Outputs)

### Audit Track (운영 감사 — Compliance 판정만)

① **Compliance Table**
| Occurrence | Rule | Executed | Suppressed | Violated |
|---|---|---|---|---|

② **Evidence Log**
| Occurrence | Evidence | 판정근거 |
|---|---|---|

③ **Ambiguity Log**
| Occurrence | Rule | 모호성 | 후속검토 |
|---|---|---|---|

### Learning Track (개선 감사 — 행동변화·Rule개선 후보)

④ **Behavioral Evidence**
| Occurrence | 기존 행동 | 변화된 행동 | 근거 |
|---|---|---|---|

⑤ **Improvement Candidate**
| Candidate | Reason | Evidence | Priority |
|---|---|---|---|

## 7. 성공 기준 (Success Criteria)

- 감사 기준이 끝까지 유지되었다 (P3 준수)
- 감사 중 Rule이 변경되지 않았다 (P2 준수)
- 동일 Evidence에 대해 재현 가능한 판정이 가능했다 (P4 충족)
- 감사 결과(Audit Track)와 개선 제안(Learning Track)이 명확히
  분리되었다

---

## Appendix A — Compliance Evidence (파일럿 사례, 참고용)

| Rule | Compliance Evidence | Remark |
|---|---|---|
| A-08 | E-006/E-009/E-010 + 2026-07-19 최소 6회 재발(RCA 논의 도중 실시간 재현 포함) | RCA 첫 검증 사례 |
| C-07 | 2026-07-18 "제수당" 오판(DEFER-018) | |
| C-14 | 2026-07-19 R19 신설 즉시실행 | |

## Appendix B — Common Instruction Error Taxonomy (분류체계만)

| Type | 질문 | 대응 사용자 의도 축 |
|---|---|---|
| A. Target | 어디에? | 대상 |
| B. Deliverable | 무엇을? | 목적 |
| C. Scope | 어디까지? | 범위 |
| D. Timing | 언제? | 시점 |

이 표는 분류체계일 뿐이며 Rule이 아니다. Q1~Q4를 직접 내장하지
않는다 — Appendix C 참조.

## Appendix C — Typical Detection Pattern (참조 예시, Rule 아님)

Error Taxonomy 각 Type이 실제로 어떻게 감지될 수 있는지 예시로만
제시. REA Q1~Q4 형식을 빌리되, 이건 새 Rule 제정이 아니라
"이렇게 나타날 수 있다"는 참조용 패턴이다.

| Type | 감지 예시(Q1) | 확인 행동 예시(Q2) | Output 예시(Q3) | 기존 연결점 |
|---|---|---|---|---|
| A. Target | 프로젝트/저장소 2개 이상 얽힘 | 작업 전 "대상: ___" 선언 | 그 선언 문장 | research-backlog.md DEFER-011과 통합 검토 |
| B. Deliverable | 결과물 종류 단어 명시됨 | 요청 산출물 재진술 | "요청 산출물: ___" | QVU 개념과 통합 검토 |
| C. Scope | 축소어/확대어 존재("초안"/"완성" 등) | 깊이수준 명시 | 선언 | 현재까지 가장 독립적인 신규 Type(추후 재검증 대상) |
| D. Timing | 검토/설계 계열 지시어 | 검토결과(승인/수정필요/보류/추가질문) 선언 | 그 선언 | "검토결과 선언 게이트"와 동일 |

---

**상태**: Draft v0.1, 미승인. REA-001처럼 파일럿(A-08/C-07/C-14)
재개 여부는 별도 승인 대기.
