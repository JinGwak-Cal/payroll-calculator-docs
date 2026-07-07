# Methodology Notes — Mechanism Hypotheses

이 문서는 evidence-log.md와 분리된 공간입니다.
evidence-log.md는 "무엇이 관찰됐는가"(Observation)만 담고,
이 문서는 "왜 그런 일이 생기는가"에 대한 **검증되지 않은 설명**을 담습니다.

원칙: 이 문서의 내용은 절대 Observation으로 취급하지 않습니다.
새 Evidence가 이 가설을 반박하거나 강화하면 그때 갱신합니다.

---

## MH-001. Question Loss의 가능한 메커니즘 (관련: E-007)

출처: GPT 제안, 검증되지 않음
Confidence: Low (Supporting Evidence: E-007, 1건)

가능한 설명 후보 (상호 배타적이지 않음):
1. 앞 질문에 대한 응답 생성이 길어지면, 뒤 질문이 처리 흐름에서
   밀려날 수 있다 (작업 메모리 유사 현상).
2. 응답 생성 중 새로운 사고 전개가 일어나면, 원래 질문 목록에서
   이탈할 수 있다.
3. 질문 "개수"가 아니라 질문 안에 포함된 하위 Task 개수가 영향을
   줄 수 있다 (예: "2번" 안에 A/B/C/D가 있으면 사실상 4개 질문).

**중요**: 이 셋 다 Claude/GPT의 내부 처리 과정에 대한 외부 관찰자의
추측이며, 모델이 자기 내부를 직접 관찰해서 확인한 것이 아닙니다.
검증 방법이 생기기 전까지 Hypothesis 상태로 유지합니다.

관련 Evidence: E-007 (Observation만, 메커니즘 설명 제외한 버전)

---

## MH-002. 역할 배정 오류(Misallocation)가 여러 Cost의 공통 원인일 가능성

출처: GPT 제안, 검증되지 않음
Confidence: Low (Supporting Evidence: 없음 — 여러 Cost가 동시에
관찰된 정황은 있으나, 공통 원인이라는 인과관계는 미검증)

가설: "적절한 주체에게 적절한 작업이 배정되지 않을 때 운영 비용이
발생한다"는 단일 원인이 아래 여러 증상으로 나타난다.

```
AI가 해야 할 일을 사람이 하면      → Human Mediation Cost
다른 AI가 해야 할 일을 사람이 하면  → Delegation Cost
사람이 해야 할 결정을 AI가 대신 하면 → Approval Bypass
질문 관리 책임이 불분명하면        → Question Loss
```

**주의**: 이 넷이 실제로 하나의 원인에서 나오는지, 아니면 우연히
같은 세션에서 동시에 관찰된 별개의 문제인지는 아직 구분되지 않음.
Evidence가 더 쌓여 이 인과관계를 지지하거나 반박하기 전까지
Confidence: Low 유지.

---

## MH-003. Approval Signal Misinterpretation의 가능한 메커니즘 (관련: E-009)

출처: GPT 제안, 검증되지 않음
Confidence: Low (Supporting Evidence: E-009, 1건)

가능한 설명 후보:
1. 같은 내용이 반복해서 입력되면, AI가 "사용자가 강조/확인하려는
   의도"로 해석해 승인 신호로 오인할 수 있다.
2. 명시적 언어("예", "승인") 없이 행동 패턴만으로 의도를 추론하려는
   경향이 실패로 이어질 수 있다.

**중요**: 검증되지 않은 추측이며 Observation과 분리 유지.