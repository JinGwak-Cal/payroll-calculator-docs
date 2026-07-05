# Threshold Foundry Direction

Status: Candidate

이 문서는 Threshold Foundry의 현재 Direction(전략적 방향)을 기록한다.

Direction은 Evidence나 Methodology와 성격이 다르다.

- Evidence는 "무엇이 일어났는가"를 기록한다.
- Methodology는 "어떻게 할 것인가"를 정의한다.
- Direction은 "우리는 어디로 갈 것인가"를 선택한다.

Direction은 과학적 가설(Hypothesis)이 아니다.

Direction은 참·거짓을 증명하는 대상이 아니라,
Threshold Foundry가 선택한 현재의 전략적 방향이다.

Direction 자체는 Evidence로 증명되지 않는다.

그러나 Direction의 적합성은 앞으로 만들어질 Evidence와
운영 경험을 통해 지속적으로 평가되고 다듬어진다.

---

# Threshold Foundry Structure (Current Understanding)

다음 구조는 현재 논의를 통해 정리된 이해 모델이며,
최종 구조로 확정된 것은 아니다.

```
                    Threshold Foundry

                           │
          ┌────────────────┴────────────────┐
          │                                 │

     Discovery Domain              Operational Domain

          │                                 │

      Direction                     absolute-rules
      Evidence                      decisions
      Methodology                   current-step
```

현재 이해는 다음과 같다.

- Discovery Domain은 새로운 Direction, Evidence, Methodology를 만들어가는 영역이다.
- Operational Domain은 검증된 운영 정보를 Source of Truth(SoT)로 관리하는 영역이다.

이 구조 자체 역시 앞으로 운영 경험을 통해 계속 검토될 수 있다.

---

# Direction

```
                    Threshold Foundry

                          │
      ┌───────────────────┼───────────────────┐
      │                   │                   │
      ▼                   ▼                   ▼

 Human Value      Collaboration        Business Value
 (인간 가치)        Engineering         (비즈니스 가치)

 AI 시대에          Human + AI          지속 가능한
 인간답게           협업환경             서비스/제품
 살아가기           최적화              창출

      └───────────────────┼───────────────────┘
                          │
                          ▼

        Evidence-based Collaboration Optimization
```

---

# 1. Human Value (Why)

Threshold Foundry는 AI가 사람을 대체하는 것을 목표로 하지 않는다.

우리가 지향하는 것은

AI 시대에도 사람이 주체적으로 사고하고,

협업하고,

성장할 수 있는 환경이다.

특히 완전 자동화 이전의 현실적인 협업 환경에서

Human과 AI가 함께 문제를 해결하며 성장할 수 있는 기반을 중요한 가치로 둔다.

---

# 2. Collaboration Engineering (How)

Threshold Foundry는 Human과 AI가 함께 문제를 해결하는 과정에서 발생하는

- 이해
- 오해
- 판단
- 학습

을 중요한 협업 Evidence로 바라본다.

Evidence Engineering은 이러한 협업 과정에서 생성되는 Evidence를 축적하고,

그 Evidence를 기반으로 협업환경의 지속적인 최적화를 지향하는 공학이다.

CMP, ER, TM, TCA 등은 이러한 협업환경을 구현하기 위한 Methodology이다.

---

# 3. Business Value (What)

Threshold Foundry는 협업환경 자체를

지속 가능한 Product와 Service로 발전시키는 것을 목표로 한다.

관심의 중심은 완전 자동화 자체가 아니라,

Human과 AI가 함께 일하는 현실적인 협업 환경을 설계하고 지원하는 데 있다.

이를 통해

AI 시대를 살아가는 개인과 조직이

보다 자연스럽게 AI와 협업할 수 있는 기반을 제공하고자 한다.

---

# Relationship

```
Human Value
      │
      ▼
Collaboration Engineering
      │
      ▼
Business Value
```

- Why : 왜 존재하는가
- How : 어떻게 구현하는가
- What : 무엇을 만들어 제공하는가

Business는 Human Value를 실현하기 위한 결과이며,

Collaboration Engineering은 그 둘을 연결하는 실행 영역이다.

---

# Position

Direction은 Rule이 아니다.

Direction은 Methodology도 아니다.

Direction은 Threshold Foundry 전체가 어떤 방향으로 나아갈 것인지를 설명하는
전략적 선택이다.

Direction은 앞으로 운영 과정에서 계속 평가되고 다듬어질 수 있지만,

현재는 Candidate 상태로 관리한다.

Direction의 최종 문서 위치와 운영 방식은
실제 운영 경험을 충분히 축적한 이후 다시 판단한다.

---

## Review Request

Threshold Foundry Direction에 대해 다음 관점에서 검토 부탁드립니다.

1. Direction의 정의(전략적 선택)가 적절한가?
2. Human Value → Collaboration Engineering → Business Value 흐름이 자연스러운가?
3. 두 개의 다이어그램이 Direction을 설명하는 데 도움이 되는가?
4. Discovery Domain / Operational Domain 설명이 현재 단계(Candidate)에 맞게 과도한 단정을 피하고 있는가?
5. Direction 문서의 범위(Why / How / What)가 적절한가?
6. 과도하거나 부족한 부분이 있다면 어떤 점을 보완하면 좋을까?

철학적 수사보다 운영성과 구조적 일관성 중심으로 검토 부탁드립니다.

---

## 2026-07-04 결정 — Bridge Architecture (Stage 0)

승인 근거 (Jin님, 명시적 사전 논리):
- 복구 비용 없음(새 쓰레드에서 진행, 현재 쓰레드 산출물은 그대로 보존)
- 실행 전 두 파트너(GPT/Claude) 의견 청취 완료
- 기대 유익(Flow 개선)이 현재 반복되는 병목(복붙, 전달, 누락 확인) 비용의
  최소 몇 배로 판단됨

결정 사항:
- Bridge Architecture는 별도 연구 대상이 아니라, 현재 진행 중인
  approval Lens 연구(및 향후 모든 CMP 연구)를 수행하기 위한
  **연구 인프라(Infrastructure)**로 정의한다.
- 순서: 본 쓰레드(Evidence 정리, PR/Merge) → 새 쓰레드(Bridge Step1
  구축) → 본 연구(approval Lens)로 복귀, Bridge 위에서 계속.

```
Stage 0   Bridge Infrastructure       ← 다음 쓰레드
Stage 1   Approval Study (재개)
Stage 2   Cost Model
Stage 3   Methodology
Stage 4   Automation
```

Bridge Step1 범위 (다음 쓰레드에서 설계):
- Bridge Protocol: AI A → Bridge → AI B → Bridge → Approval → GitHub → Archive
- Bridge Interface: AI끼리 어디서 어떻게 대화할지 (GitHub Discussion /
  Markdown / JSON / SQLite 등, MCP 불필요)
- Approval Console: 사람은 복붙 없이 판단만 하는 화면/절차

원칙: "사람은 판단한다. AI는 수행한다. Bridge는 조율하고 전달한다."
(전달 + 상태관리 + 승인대기 + 결과취합 + 로그기록)

### 계층 구조 (Infrastructure의 위치)

```
Evidence
   ↓
Methodology
   ↓
Infrastructure   ← Bridge는 여기 속함 (Direction의 일부가 아니라
   ↓                Methodology와 Operation을 연결하는 층)
Operation
```

Infrastructure 정의: Infrastructure(Bridge, 향후 SQLite/MCP/Approval
Console/Agent 등 포함)는 연구 대상이 아니라, 연구 비용을 줄이기
위한 기반이다. 이 계층 정의 덕분에 Bridge 외에 다른 Infrastructure가
추가되어도 같은 층에 자연스럽게 확장된다.

Status: Candidate (설계 전, 다음 쓰레드에서 구체화 예정)