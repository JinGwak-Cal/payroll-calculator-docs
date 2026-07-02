# C-00035 : 운영의 복리 효과 (Experience Compound)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00035 |
| | Coordinate | T-01 |
| **기본** | 이름(한글) | 운영의 복리 효과 |
| | 영문명 / 약어 | Experience Compound |
| **정의** | 공식 정의 | 동일 프로젝트에서 운영 Context가 누적될수록, 기존 Context와 새 Context의 상호작용(재활용)으로 AI 판단의 정확도와 자율성이 비선형(非線形)으로 향상되는 현상 |
| | 목적 | 운영 Context 축적이 단순 정보 증가가 아니라 복리처럼 효과가 가속화된다는 원리를 설명하여, Context 관리의 중요성과 장기 투자 가치를 근거 짓는다 |
| | 핵심 질문 | 왜 운영 Context를 오래 쌓을수록 AI의 자율성이 가속적으로 높아지는가 |
| **분류** | Type | Theory *(검증된 설명 원리로 분류하는 이유: 이 효과는 단일 가설이 아니라 Pilot 전체와 Claude 자율성 관찰(C-00018)에서 반복 확인된 패턴을 설명하는 것이기 때문 — 단, 타 프로젝트에서 재현 검증이 완료된 것은 아니므로 Stability는 낮게 설정)* |
| | Status | Candidate |
| | Stability | Emerging *(본 프로젝트 내에서는 반복 관찰되었으나, 외부 프로젝트 재현 미완료)* |
| **관계** | 상위 개념 | 없음 *(운영복리효과는 Context Threshold를 포함하는 것이 아니라 설명하는 원리 — 포함관계 아닌 설명관계이므로 상위 개념 없음. 향후 "운영 Context 성숙 이론" 같은 더 상위 Theory가 확정되면 재배치)* |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00016 (컨텍스트 쓰레시홀드 — 복리 효과가 임계점에 도달하면 발생하는 결과), C-00012 (Context Layer — 복리 효과가 발생하는 운영 공간), C-00017 (CTI — 복리 효과의 진행도를 측정하는 지표 후보) |
| | Before(전 단계) | 없음 *(운영 Context 누적 자체가 출발점 — 선행 개념 없음)* |
| | After(후 단계) | C-00036 (운영 Context 성숙 이론) *(복리 효과가 충분히 진행되면 성숙 단계로 연결)* |
| **비교** | 기존 유사 개념 | Compound Interest (금융), Learning Curve (심리학·경영), Flywheel Effect (비즈니스 전략) |
| | 차이점 | 금융의 복리는 동일 자산의 재투자 효과이고, Learning Curve는 반복 훈련의 숙련도 향상이다. 본 개념은 "AI가 처리한 Context의 누적"이 AI 자신의 판단 품질을 비선형으로 향상시킨다는 점에서 다르다 — 사람의 학습이 아니라 운영 환경(Context Layer)의 성숙에 의해 AI 자율성이 높아진다는 점이 핵심 차별점이다 |
| | 용어 유형 | 기존용어조합+신개념 |
| | Official Name 후보 | 운영의 복리 효과 / Experience Compound / Context Compound Effect(유력 후보 — Experience보다 "운영 Context"가 핵심임을 명확히 표현) / Operational Compound |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Pilot 전체 과정에서 Standard가 거의 바뀌지 않고 Manual과 운영규칙만 계속 발전했다는 패턴 관찰, 그리고 Claude 자율성 사례(C-00018)에서 "왜 갑자기 자율적으로 변했는가"라는 질문을 추적하며 Context 누적의 비선형 효과라는 설명에 도달함 |
| | Decision Origin | 없음 |
| | Evidence | C-00018 (Claude 자율성 관찰 사례) |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음4-1) |
| | Review Result | Approved (조건부→승인 전환) |
| | Review Notes | ①정의에 "재활용과 상호작용으로 비선형 효과" 명시. ②상위 개념(C-00016) 제거 — 포함관계 아닌 설명관계이므로 관련 개념으로 이동. ③Official Name에 Context Compound Effect 추가. Review Backlog: Theory Promotion Rule(단일 Evidence가 아닌 복수 Case Study 요구) — Theory군 3~5장 후 Manual 검토 |
| | 비고 | **Theory vs Hypothesis 판단 근거**: 운영복리효과는 "왜 이런 현상이 발생하는가"를 설명하는 원리(Theory)이고, Context Threshold(C-00016)는 "이 원리가 실제로 임계점을 만든다"는 미검증 주장(Hypothesis)이다. Theory는 하나 이상의 Observation을 설명하고 하나 이상의 Hypothesis를 낳을 수 있어야 한다는 원칙이 이 카드에서 처음 적용됨. **Promotion 경로**: 타 프로젝트에서 동일 패턴 2회 이상 + Evidence Case Study 복수 확인 후 Promotion Review 진입 |
