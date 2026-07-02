# 03. Concept System v1.0

> AI Company Concept System 전체 구조. Lifecycle과 Meta Model을 포함.

---

## Concept Lifecycle (개념 생명주기)

Concept Card는 정적 스냅샷이지만, Concept System 차원에서는 개념이 거치는 흐름이 존재한다:

```
발견 → 명명 → 정의 → 관계화 → 후보등록 → 반복검증 → 승격심사(Promotion Review) → 승격 → 운영 → 폐기/보관
```

이 흐름은 카드 개별 필드가 아니라 **시스템 레벨의 절차**로 관리한다. Status 필드는 이 Lifecycle 중 "후보등록~운영~폐기/보관" 구간을 카드 단위로 스냅샷한 것이다.

**승격심사(Promotion Review)와 승격(Promotion)은 다른 단계다.** 심사는 절차이고, 승격은 그 절차의 결과다.

---

## Meta Model (메타 모델) — 후보, 문서화만

Concept Card 자체도 하나의 개념이다. 향후 구조 확장을 대비해 다음 계층을 인식해 둔다 (지금은 별도 카드화하지 않음):

```
Concept (개념) → Card (카드) → Field (필드) → Rule (운영 규칙)
```

Graph DB 이관 시 이 메타 계층이 스키마 설계의 기반이 된다.

---

## 문서 구조 (Document Map)

```
AI Company Concept System
├── 01. Concept Card Standard   (카드 규격)
├── 02. Concept Manual          (작성 규칙)
├── 03. Concept System          (전체 구조 — 본 문서)
├── 04. Concept Dictionary      (Type 정의)
└── 05. Naming Guide            (용어 정책)
```

---

## 저장 정책

지금은 **Markdown + Git**. Graph Migration Ready 원칙에 따라 관계 필드는 항상 Concept ID로 참조한다. 향후 단계적 이관 경로:

```
Markdown + Git → Obsidian → Neo4j(Graph DB)
```

---

*Version: v1.0 | Status: Approved*
