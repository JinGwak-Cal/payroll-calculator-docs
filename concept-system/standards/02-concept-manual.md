# 02. Concept Manual v1.0

> Concept Card 작성 시 따라야 하는 운영 규칙. Standard(규격)와 달리 운영하면서 계속 갱신될 가능성이 높은 문서.

---

## 운영 규칙 (Ontology Manual)

1. 정의는 반드시 1문장, 해석 여지를 남기지 않는다.
2. 상위 개념은 1개만 허용한다 — 다중 상위가 필요해 보이면 분류 자체를 재검토하라는 신호다.
3. **불변은 Concept ID뿐**이다. Coordinate, Status, Stability는 모두 변경 가능하다.
4. Candidate 상태에서는 자유 수정 가능. Promoted 전환 이후 변경은 버전업으로만 한다.
5. 관계 필드는 이름이 아닌 Concept ID로만 기재한다 (Graph Migration Ready 원칙).
6. 업계에 같은 의미의 기존 용어가 있으면 반드시 "기존 유사 개념" 필드에 명시한다 — 숨기지 않는다. 이는 AI Company의 철학이다.
7. 이름이 확정되지 않은 개념은 "Official Name 후보" 필드에 복수 후보를 남기고, 정의와 차별점을 먼저 고정한 뒤 이름을 나중에 결정한다.
8. 분류체계 자체가 바뀌는 수준의 변화는 개별 카드 수정이 아니라 **개념체계 전체의 버전업**으로 처리한다.
9. 같은 의미인지 다른 의미인지 애매한 경우, Stability를 Experimental로 두고 반복 검증을 기다린다.
10. Policy(운영 정책) 분류는 신설 보류, 후보로만 남긴다. Rule(실행 규칙)과 달리 Promotion Policy, Storage Policy, Naming Policy 등 운영 정책 성격 개념이 누적되면 별도 Type 또는 Rule의 Subtype 도입을 검토한다.
11. **Forward Reference Rule**: 아직 작성되지 않은 Concept도 Concept ID를 먼저 예약(Reserved)할 수 있다. 카드 작성 중 미작성 개념을 참조해야 하면 ID를 채번해 예약하고, 해당 카드는 추후 그 ID로 정식 작성한다.
12. **Evidence 필드는 선택(Optional)이다.** Type에 따라 생략 가능하다 — 권장 기준: Case Study(필수) / Hypothesis(권장) / Workflow·Rule·기타(선택).
13. Status 판단 시 "반복(Repeated)"의 기준은 **서로 다른 Thread**에서의 재등장이다. 동일 Thread 내 반복 사용은 Repeated로 인정하지 않는다 — 이 경우 Status는 Candidate 유지, Stability만 Emerging으로 올릴 수 있다.
14. **Link Consistency Rule**: 관계(상위/하위/관련/전/후)를 추가·삭제·변경한 경우, 영향을 받는 카드의 역참조도 함께 검토한다. 단, 항상 자동 갱신을 강제하지는 않는다 — 상위/하위는 역참조가 비교적 명확하지만, 관련 개념은 항상 대칭이 아닐 수 있으므로 **검토**를 원칙으로 한다.
15. **Relation Type Consistency**: Before/After(시간·절차 관계)와 상위/하위(포함 관계)는 가능한 한 서로 다른 대상을 가리킨다. 동일 대상을 참조해야 하는 경우 예외로 허용하되, 그 이유를 Review Notes에 기록한다.
16. **Registry Consistency**: Reserved 상태의 Concept ID(Forward Reference)는 Candidate Registry에도 반드시 기록한다. 예약 현황을 별도 관리해 ID 충돌을 방지한다.

---

## Manual Change Log

각 규칙이 어느 Pilot에서 비롯되었는지 추적한다.

| 규칙 | Origin |
|---|---|
| Rule 1~9 | Standard 설계 단계 (Pilot 이전) |
| Rule 10 | Standard 설계 단계 |
| Rule 11 (Forward Reference) | Pilot-001 |
| Rule 12 (Evidence Optional) | Pilot-001 |
| Rule 13 (Repeated 판단기준) | Pilot-001 |
| Rule 14 (Link Consistency) | Pilot-003 |
| Rule 15 (Relation Type Consistency) | Pilot-003 |
| Rule 16 (Registry Consistency) | Pilot-004 Review |

---

*Version: v1.0 | Status: Approved — 운영하며 지속 갱신 예정*
