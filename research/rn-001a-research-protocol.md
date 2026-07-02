# RN-001A : Context Threshold Enabler Study — Research Protocol

Version: v1.0
Status: Active
Linked Cards: C-00016, C-00018, C-00022
Note: 연구 결과는 RN-001B에 기록. Claude 역할 = Researcher (Reporter 아님).

---

## 0. Research Scope

본 연구는 Claude의 성능 평가가 아니라 **Context Threshold 현상을 유발한 Collaboration Environment**를 연구한다. Claude는 연구 대상(Subject)인 동시에 공동 연구자(Researcher)이다. AI 모델 평가는 범위 밖이다.

연구 대상: "2026년 6월 27일 당시의 Claude가 왜 변했는가" — 현재의 Claude가 아니라 **당시의 AI**를 연구한다.

장기: Context Threshold Enabler Study → AI Context Engineering Study로 확장 가능.

---

## 1. Research Integrity Rules (연구 무결성 원칙)

**이 원칙은 무엇을 하면 안 되는가를 정의한다. 모든 RN에 공통 적용된다.**

| Rule | 원칙 | 핵심 금지 |
|---|---|---|
| RI-01 | 기억으로 쓰지 않는다. Memory is not Evidence. | 당시 문서 확인 전 원인 추정 금지 |
| RI-02 | 빈칸을 추론으로 메우지 않는다. | Evidence 없는 구간은 "모름 / 확인 필요"로 남긴다 |
| RI-03 | 결과를 먼저 만들지 않는다. | Evidence→Pattern→Hypothesis→Possible Cause→Conclusion 순서 필수 |
| RI-04 | Evidence와 Interpretation을 섞지 않는다. | Fact / Interpretation / Hypothesis를 분리 기술 |
| RI-05 | 직접 진술과 해석을 구분한다. | 인용 먼저, 해석은 그 다음 |
| RI-06 | Evidence 등급을 올리지 않는다. | 스니펫→원문→교차검증 과정 없이 Primary Evidence 취급 금지 |
| RI-07 | 현재 Context를 과거에 투영하지 않는다. | 당시 실제로 있었던 것만 기준 |
| RI-08 | 하나의 Evidence로 원인을 확정하지 않는다. | Claude 진술 + 실제 로그 + GPT 관찰 최소 3축 일치 필요 |
| RI-09 | 연구자와 피실험자를 혼동하지 않는다. | Claude는 자신의 진술만으로 자신의 가설을 입증 불가 |
| RI-10 | 반증 가능성을 반드시 찾는다. | 내 가설이 틀렸을 Evidence를 먼저 찾는다 |
| RI-11 | "모른다"는 연구 결과를 허용한다. | 억지 결론보다 "Evidence 부족" 선언이 더 가치 있다 |
| RI-12 | 당시 환경만 평가한다. | 현재 완성된 문서·Concept System으로 당시를 평가 금지 |
| RI-13 | 모든 주장에는 출처를 연결한다. | Evidence ID / Conversation / File / Timeline 중 하나 이상 필수 |
| RI-14 | Environment와 Enabler를 혼동하지 않는다. | 존재했던 것(Environment) ≠ 기여한 것(Enabler) |
| RI-15 | 연구 종료 시에도 가설은 살아있을 수 있다. | Theory 완성이 아닌 재현 가능한 Evidence가 목표 |
| RI-16 | 연구자는 '당시의 AI'를 연구한다. | 당시 대화 원문 > 당시 문서 > 당시 생성 파일 > 현재 회상 |

**Evidence 우선순위 (RI-16 상세):**
1. 당시 대화 원문 (Conversation)
2. 당시 문서 (Documents)
3. 당시 생성 파일 (Artifacts)
4. 당시 사용자 피드백 (Feedback)
5. 당시 Claude 고백 (Self-report)
6. 현재 Claude 회상
7. 현재 GPT 해석

---

## 2. Core Research Question

**"어떤 Collaboration Environment가 Context Threshold를 발생시켰는가?"**

| RQ | 질문 |
|---|---|
| RQ-1 | Claude는 자신의 변화 원인을 무엇이라고 설명하는가? |
| RQ-2 | GPT는 같은 변화를 어떻게 독립적으로 관찰했는가? |
| RQ-3 | 둘의 설명은 어디까지 일치하는가? |
| RQ-4 | 실제 대화 로그는 어느 쪽을 지지하는가? |
| RQ-5 | Threshold Enabler의 핵심 요소는 무엇인가? |
| RQ-6 | 다른 AI에서도 같은 환경이 재현되는가? |
| RQ-7 | 어떤 Collaboration 패턴이 Threshold 발생과 상관관계를 갖는가? |
| RQ-8 | 사용자의 어떤 개입이 Threshold를 촉진 또는 지연시켰는가? |

---

## 3. Research Protocol (수행 순서)

```
① 연구 범위 확정
      ↓
② 당시 환경 복원 (Environment Reconstruction)
      ↓
③ Evidence 확보 (Source A~H)
      ↓
④ Structured Interview (당시 문서 확인 후에만)
      ↓
⑤ Timeline Reconstruction
      ↓
⑥ GPT Counter Observation (독립 수행, Claude 보고서 미열람)
      ↓
⑦ Cross Validation (3축 이상 교차)
      ↓
⑧ Ablation + Addition Test 설계
      ↓
⑨ Collaboration Enabler Catalog 작성
      ↓
⑩ Context Threshold Theory(C-00016) Update
```

---

## 4. Evidence Priority

- **Priority A**: 실제 로그·문서·시점 (항상 최우선)
- **Priority B**: Claude 직접 진술, GPT 직접 관찰
- **Priority C**: 후속 추론, 간접 해석

---

## 5. Evidence Source 구조

### Source A — Claude Self-Investigation
당시 문서 확보 후 Structured Interview를 통해서만 작성. 기억 기반 추론은 Evidence 불인정.

### Source B — Historical Environment Reconstruction (구: Historical Evidence)
당시 Claude가 보고 있던 **전체 환경**(대화 + GitHub + decisions + Workflow + AI Push + current-step + release-workflow)을 복원한다. "무슨 일이 있었는가"가 아니라 "당시 Claude는 어떤 환경에서 작업했는가"를 복원하는 것이 목적이다.

### Source C — GPT Environment Reconstruction Report (ER-001)
Claude의 Self-Investigation(내부 관점)과 별개로 GPT가 외부 관점에서 수행하는 **Environment Reconstruction**이다. Claude 보고서 미열람 상태로 독립 수행.

ER-001 구성:
1. Conversation Reconstruction
2. Artifact Reconstruction
3. Workflow Reconstruction
4. Decision Reconstruction
5. Information Availability Map
6. Threshold Timeline
7. Candidate Enablers
8. Evidence Matrix
9. Counter Observation
10. Cross Validation Input

### Source D — Conversation Analytics
실제 Thread에서 HDR, 자율 제안 횟수, Review 길이, 승인률, 재질문 빈도 측정.

### Source E — Environment Reconstruction
당시 실제 제공 환경 복원. 현재 환경 아님.

### Source F — Collaboration Trace
GPT Review ↔ Claude 수정 ↔ 사용자 피드백 반복 과정 자체를 분석.

### Source G — User Intervention Analysis
사용자 개입 시점·방식·피드백 패턴을 독립 변수로 분석.

### Source H — Environment Snapshot
재현 실험 기준이 되는 당시 환경 Frozen Snapshot.

---

## 6. Evidence Classification

모든 진술을 3종으로 분류 (RI-04, RI-05 적용):
- **직접 진술**: 명시적으로 원인이라고 언급한 내용
- **간접 추론**: 관찰 사실로부터 논리적 도출
- **후속 가설**: 검증 전 가설적 주장

---

## 7. Bias Control

| 주체 | 편향 | 교정 |
|---|---|---|
| Claude | 자기 보고 편향 | Source D 교차 검증 |
| GPT | 관찰자 편향 | Claude 진술 미열람 상태로 먼저 수행 |
| 사용자 | 기억 편향 | Source B 당시 문서 우선 |

---

## 8. Structured Interview Protocol

Source B 확보 후에만 실시. 답변은 **Evidence / Opinion / Hypothesis** 3종 구분 기록.

질문 (초안):
1. 당시 자율성이 높아졌다고 느낀 구체적 시점은 언제인가?
2. 그 시점 직전 환경 요소 중 가장 결정적이었던 것은?
3. 없었지만 있었으면 더 빨리 도달했을 요소는?
4. 현재 이 쓰레드에서도 같은 현상이 발생했는가?

---

## 9. Verification Plan — Ablation + Addition Test

**독립변수**: decisions.md / current-step / manual-v14 / Closing Review / merged-context / Concept Card / Collaboration Trace 패턴 / User 개입 시점

**종속변수**: HDR / 자율 판단률 / Review 품질 / 다음 단계 제안률 / 오류율

Source B·D·H 확보 후 설계 구체화.

---

## 10. Deliverables

| 산출물 | 담당 | 상태 |
|---|---|---|
| Context Threshold Timeline | Source B | 미착수 |
| Environment Reconstruction | Source E | 미착수 |
| Environment Snapshot | Source H | 미착수 |
| Evidence Set Collection | Source B | 부분 확보 (고백 Evidence Set 확보됨) |
| Collaboration Trace Report | Source F | 미착수 |
| User Intervention Analysis | Source G | 미착수 |
| Claude Research Report | Source A | 미착수 |
| GPT Counter Observation Report | Source C | 미착수 |
| Conversation Analytics | Source D | 미착수 |
| Evidence Cross Validation | 교차 검증 | 미착수 |
| **Collaboration Enabler Catalog** | 종합 | 미착수 |
| Threshold Enabler Ranking | 종합 | 미착수 |
| Context Threshold Theory Update | 최종 | 미착수 |

---

## 11. Evidence ID 체계

모든 인용에 안정적 식별자를 부여한다. 형식: `E-[순번]`

예: `E-001` — Claude 고백 원문 (B-003)

각 가설은 반드시 Evidence ID를 참조해야 한다. ID 없는 주장은 Hypothesis 표시.

---

## 12. Negative Evidence

**RI-10 전용 섹션**: 후보 Enabler를 반박하는 관찰을 적극 수집한다.

형식:
```
NE-001
반박 대상: [Enabler 후보명]
관찰: [반박 내용]
출처: [Evidence ID]
판단: 반박 강도 (강/중/약)
```

---

## 13. Enabler Promotion Criteria

후보(Candidate) → 검증됨(Verified)으로 승격하는 객관적 조건:

1. Claude 진술 + 실제 로그 + GPT 관찰 **3축 모두 일치** (RI-08)
2. **Negative Evidence가 없거나** 반박이 "약" 이하
3. **Ablation Test**: 해당 요소 제거 시 종속변수 변화 확인
4. **Reproducibility**: 다른 컨텍스트에서도 동일 효과 재현 가능성

미충족 시 Candidate 유지, 부분 충족 시 "Probable" 등급 부여.

---

*Version: v1.1 | Status: Active | Claude 역할: Researcher | GPT Review: Approved with Minor Improvements | 결과는 RN-001B 참조*
