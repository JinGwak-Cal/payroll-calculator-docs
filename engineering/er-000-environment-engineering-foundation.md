# ER-000 : Environment Engineering Foundation

Version: v1.0
Status: **FROZEN** — ER-001 착수 전 확정. 변경 시 GPT+Claude 공동 Review 필수.
Purpose: ER 시리즈 전체의 용어·흐름·Evidence 기준을 고정한다.

---

## Freeze-01 : Environment Terminology

| 용어 | 정의 |
|---|---|
| **Environment** | AI가 협업 중 실제로 접근하고 활용할 수 있는 모든 요소의 총합 |
| **Environment Snapshot** | 특정 시점에 AI가 볼 수 있었던 Environment 전체를 동결한 단위 — 재현 실험의 기준이 됨 |
| **Environment Component** | Environment를 구성하는 실체적 요소 (예: manual-v14, decisions.md, merged-context) — "무엇이 존재하는가" |
| **Environment Variable** | 각 Component의 상태를 수치화하는 속성 (예: Visibility, Accessibility, Continuity) — "그것이 어느 정도인가" |
| **Environment Metric** | Environment Variable을 실제로 측정하는 지표 — HDR, 자율 제안률 등 |
| **Environment Reconstruction** | 당시 실제 Environment를 현재 시점에서 복원하는 작업 — RI-12 원칙 적용 |

---

## Freeze-02 : Engineering Flow

ER 전체의 기준 흐름. 이 순서를 벗어나는 분석은 허용하지 않는다.

```
Environment
      ↓
Environment Components
(무엇이 존재했는가)
      ↓
Environment Variables
(각 Component가 어느 정도였는가)
      ↓
Metrics
(변수를 어떻게 측정하는가)
      ↓
Engineering Model
(변수 간 관계와 Threshold 발생 조건)
      ↓
Optimization
(최소 비용으로 최대 Threshold 효과)
      ↓
Reproduction
(다른 AI/환경에서 동일 결과 재현)
```

---

## Freeze-03 : Evidence Hierarchy

Evidence 승격 순서. 하위 단계 Evidence 없이 상위 단계로 건너뛸 수 없다.

```
Conversation (최우선 — 당시 실제 대화 원문)
      ↓
Artifacts (당시 생성된 파일·워크플로우)
      ↓
Workflow (당시 작업 흐름 구조)
      ↓
Decision (당시 확정된 결정 목록)
      ↓
Observation (패턴 관찰 — Claude/GPT/User)
      ↓
Hypothesis (검증 전 가설)
      ↓
Engineering Conclusion (3축 교차검증 후 확정)
```

---

## Backlog (ER-001 이후 검토)

- Environment Ontology
- Environment Taxonomy
- Environment Variable Dictionary
- Metric Dictionary

---

*Version: v1.0 | Status: FROZEN | ER-001 착수 기준점 | 변경 금지 — 변경 필요 시 ER-000 v2로 별도 발행*
