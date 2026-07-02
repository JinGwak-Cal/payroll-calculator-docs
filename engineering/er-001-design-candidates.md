# ER-001 Design Candidates

Version: v1.0
Status: Hypothesis — Evidence 미확보, ER-001에서 검증 예정
Note: ER-000(FROZEN) 수정 금지. 검증 완료 후 ER-000 v2 또는 Engineering Model 반영 결정.

---

## DC-01 : Perception Layer

**현재 Engineering Flow (ER-000 Freeze-02):**
```
Environment → Components → Variables → Metrics → Model → Optimization → Reproduction
```

**검토 후보 (삽입 위치: Environment 직후):**
```
Environment
      ↓
Perception  ← 후보
      ↓
Reasoning   ← 후보
      ↓
Behavior
```

**이유:** 동일한 Environment라도 AI가 실제로 인지(Perceive)했는지에 따라 행동이 달라질 가능성이 있다.

예시:
```
manual-v14 존재 (Environment)
      ≠
AI가 실제 읽음 (Perception)
      ≠
이해함 (Reasoning)
      ≠
활용함 (Behavior)
```

**Status:** Hypothesis | **Evidence:** 미확보 | **검증:** ER-001

---

## DC-02 : Interpretation Layer

**현재 Evidence Hierarchy (ER-000 Freeze-03):**
```
... → Observation → Hypothesis → Engineering Conclusion
```

**검토 후보 (Observation과 Hypothesis 사이 삽입):**
```
Observation
      ↓
Interpretation  ← 후보
      ↓
Hypothesis
```

**이유:** Evidence와 해석을 더 명확히 분리하기 위함. RN-001의 RI-04(Evidence와 Interpretation 분리) 원칙과도 일치한다.

**Status:** Hypothesis | **Evidence:** 미확보 | **검증:** ER-001

---

## DC-03 : Environment State Transition

**현재:** Environment Component 존재 여부만 정의됨 (Exists / Not Exists).

**검토 후보 — 7단계 State Transition:**
```
Exists
  ↓
Available
  ↓
Discovered
  ↓
Read
  ↓
Understood
  ↓
Applied
  ↓
Reused
```

**이유:** Environment는 존재하지만 AI가 실제 어느 State까지 도달했는지가 Threshold 발생의 핵심 변수일 가능성이 있다.

특히 사용자의 반복 패턴:
```
읽기 검증 성공 → 새 쓰레드 Context 복원 → 안정적 작업 재개
```
을 설명할 수 있는 후보.

**Status:** Hypothesis | **Evidence:** 사용자의 반복 Context Reconstruction 사례(부분 확보) | **검증:** ER-001

---

## Promotion 조건

ER-001 완료 후 다음 기준으로 승격 여부 결정:

| Candidate | 승격 조건 | 승격 대상 |
|---|---|---|
| DC-01 Perception Layer | Conversation Analytics에서 "환경 존재 ≠ AI 활용" 사례 3건 이상 | ER-000 v2 Engineering Flow 수정 |
| DC-02 Interpretation Layer | Evidence/Interpretation 혼재로 인한 연구 오류 사례 확인 | ER-000 v2 Evidence Hierarchy 수정 |
| DC-03 State Transition | 동일 Component가 다른 State에서 다른 Threshold 효과를 냈다는 Evidence | Environment Variable Dictionary 신설 |

---

*Version: v1.0 | Status: Hypothesis | ER-000 수정 없음 | ER-001 검증 후 결정*
