# 05. Naming Guide v1.0

> 용어 정책. 새 개념의 이름을 정할 때 따르는 원칙과 AI Company Concept System 자체의 공식 명칭.

---

## 용어 유형 분류

새 개념의 이름을 지을 때 5종 유형 중 하나로 분류한다:

| 유형 | 설명 | 예 |
|---|---|---|
| 기존용어 | 업계 용어 그대로 사용 | Dispatcher |
| 기존용어확장 | 기존 용어에 의미를 더함 | Context Layer |
| 기존용어조합 | 기존 용어 둘을 합침 | Context Score |
| 기존용어조합+신개념 | 조합이면서 새로운 의미층 추가 | Context Threshold |
| 완전신조어 | 필요할 때만 최소화하여 사용 | (현재 없음) |

원칙: 새로운 말을 만들기 위해 새 말을 만들지 않는다. 기존 용어를 최대한 활용하고, 정말 필요한 부분만 새 개념을 만든다.

---

## 이름 확정 절차

1. 이름부터 정하지 않는다 — **개념(정의·차별점)을 먼저 고정**한다.
2. 이름 미확정 개념은 Concept Card의 "Official Name 후보" 필드에 복수 후보를 기재한다.
3. 업계에 동일/유사 의미의 기존 용어가 있으면 반드시 "기존 유사 개념" 필드에 명시한다 — 숨기지 않는다.
4. 좋은 이름의 기준은 "새롭다"가 아니라 "오해되지 않는다", 그리고 "설명 비용이 가장 낮다"이다.

---

## 공식 명칭 (Official Naming)

| 구분 | 내용 |
|---|---|
| Official Name | **AI Company Concept System** (개념체계) |
| Category | An Operational Knowledge Model for AI Collaboration |
| 정의 | AI Company 운영에 필요한 개념을 발견·명명·정의·분류·관계화하고 생명주기까지 관리하는 개념체계 |
| Naming Rationale | Concept System은 가장 설명 비용이 낮고, 기존 Knowledge Model과 Ontology의 장점을 흡수하면서도 AI Company의 범위를 가장 정확하게 표현하기 때문에 채택한다 |
| 외부 설명 (영문) | An operational knowledge model for AI collaboration. |
| 관련 개념 — Knowledge Model | 가장 가까운 기존 개념. 단, Knowledge Model은 주로 *구조*를 다루는 반면 우리는 *운영·생명주기*까지 포함하므로 범위가 더 크다 |
| 관련 개념 — Knowledge Graph | 향후 Graph DB 이관 시의 **구현 기술**. 이름 후보가 아님 — 혼동 방지를 위해 명확히 구분 |
| 관련 개념 — Ontology | 형식논리·추론까지 포함하는 시맨틱웹 표준 용어. 우리 작업 범위보다 큰 개념이라 채택하지 않음 |
| 용어 유형 | 기존용어 조합 + 도메인 한정 (완전 신조어 아님 — "Concept"과 "System" 모두 기존 용어, 새로운 것은 "AI Company Concept System"이라는 조합) |

---

## Reserved Terms (예약 용어)

공식 채택된 용어는 다른 의미로 재사용하지 않는다. 새 개념이 기존 예약 용어와 이름이 겹치면, 이름을 바꾸거나 기존 용어와의 관계(상위/하위/관련)를 명시한다.

| 용어 | 상태 |
|---|---|
| Dispatcher | Reserved |
| Concept Harvest (개념수확) | Reserved |
| Candidate Registry (후보등록부) | Reserved |
| Asset Registry (자산등록부) | Reserved |
| AI Company Concept System | Reserved |

이 목록은 Pilot 진행과 함께 계속 확장된다.

---

**모든 공식 용어는 Concept Dictionary에 단 하나의 공식 정의만 가진다.**

---

*Version: v1.0 | Status: Approved*
