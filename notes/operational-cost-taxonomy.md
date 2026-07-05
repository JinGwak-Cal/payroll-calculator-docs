# Operational Cost Taxonomy

기존 `evidence-log.md`의 Cost Model(Governance/Resource/Interaction/
Communication/Recovery Cost)과는 별도의 분류 체계입니다.

- **Cost Model** (기존): 철학적/구조적 분류. Threshold Foundry 전체
  운영에 적용되는 상위 개념.
- **Operational Cost Taxonomy** (신규, 이 문서): 토큰 절약 연구
  전용, 실제 관찰(E-001~E-007)에서 귀납적으로 도출된 실무 분류.

두 체계를 병합하지 않는 이유: 목적이 다름(철학적 분류 vs 운영 실험
분류). 병합 시 "Human Mediation Cost가 Interaction Cost와 뭐가
다른가" 같은 불필요한 논쟁이 생김.

---

## 분류 축 — Source(원인) vs Stage(단계), 서로 다른 두 축

이전 버전은 "무엇 때문에(원인)"와 "언제(단계)"가 한 목록에 섞여
있었음. Recovery/Reading은 원인이 아니라 결과/단계이므로 분리함.
(GPT 제안 반영)

### Operational Cost (Source — 왜 비용이 생겼는가)

| Cost 유형 | 정의 | 관련 Evidence |
|---|---|---|
| Token Cost | AI가 읽고 쓰는 텍스트 분량 자체의 비용 | EV-05, 이번 세션 recent_chats 대량 호출 |
| Human Mediation Cost | AI가 다른 AI/스크립트에게 시킬 수 있는 기계적 작업을 사람이 대신 중계하는 비용 | 이번 세션 approval 샘플링 요청 사례 |
| Coordination Cost | 여러 AI·사람 간 조율(승인, 재확인)에 드는 비용 | E-003, E-006 |
| Delegation Cost (신규) | AI가 수행 가능한 작업을 적절한 대상(다른 AI)에게 위임하지 못해 발생하는 비용 | E-006 (GitHub push를 Replit Agent 대신 사람에게 요청) |

### Operational Stage (언제 비용이 나타나는가 — 위 Source들의 결과로 나타나는 단계)

| Stage | 정의 | 관련 Evidence |
|---|---|---|
| Reading | 문서·환경 읽기 절차 단계에서 비용이 드러남 | EV-01, EV-07 (읽기 검증 프로토콜) |
| Analysis | 분석/판단 단계에서 비용이 드러남 | E-007 (Question Loss) |
| Proposal | 제안 단계에서 비용이 드러남 | E-006 |
| Recovery | 잘못된 진행을 되돌리는 단계에서 비용이 드러남 | E-001, E-002 |
| Release | 실제 반영(배포/커밋/push) 단계에서 비용이 드러남 | E-006 (push 권한 문제) |

### 사건 표기 예시

```
E-006  Source: Human Mediation, Coordination, Delegation
       Stage:  Proposal, Recovery

E-007  Source: Coordination
       Stage:  Analysis
```

이렇게 표기하면 나중에 "Recovery가 가장 많이 발생하는 Source는?" 같은
집계가 가능해짐.

### Severity 축 (세 번째 축 — 심각도가 아니라 반복성 기준)

| Severity | 정의 |
|---|---|
| Routine | 1회성, 정상 운영 범위 |
| Repeated | 같은 세션/짧은 기간 내 재현됨 |
| Structural | 여러 쓰레드·기간에 걸쳐 반복 → 구조적 문제 후보 |

### 사건 표기 예시 (3축)

```
E-007  Source: Coordination
       Stage:  Analysis
       Severity: Repeated
```

### 추가된 Source — Human Attention Cost

| Cost 유형 | 정의 | 관련 Evidence |
|---|---|---|
| Human Attention Cost | 사람이 여러 문답을 오가며 화면을 오르내리거나, 놓친 게 없는지 계속 확인하는 데 드는 주의력 소모. Token Cost와 독립적 | 이번 세션, Jin님이 반복 언급한 화면 왕복 피로 |

### Future Axis (예약, 아직 측정 안 함)

```
Role (Candidate)
- Human
- GPT
- Claude
- Bridge
- GitHub
- Replit
```

Bridge Step1 실제 운영 후 필요성이 확인되면 네 번째 축으로 도입.
지금은 이름만 예약하고 측정 체계는 만들지 않는다.

### 추가된 Source — Approval Bypass (Delegation Cost와 별개)

| Cost 유형 | 정의 | 관련 Evidence |
|---|---|---|
| Approval Bypass | 사람이 내려야 할 결정을 AI가 생략하거나 대신 확정해버리는 비용. Human Mediation(일을 떠넘김)과 반대 방향 | 이번 세션, "승인 대기 중" 발언 후 확인 없이 진행한 사례 |

## 주의사항 (E-006 교훈 반영)

이 분류 자체도 아직 Candidate입니다. Evidence가 각 Cost 유형에
충분히 매핑되기 전까지 확정하지 않습니다. 병합/재분류가 필요하면
이 문서만 수정하고, 실제 evidence-log.md의 기존 Cost Model은
건드리지 않습니다.