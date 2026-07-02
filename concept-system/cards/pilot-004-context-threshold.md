# Pilot-004 : 컨텍스트 쓰레시홀드 (Context Threshold)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00016 |
| | Coordinate | H-01 |
| **기본** | 이름(한글) | 컨텍스트 쓰레시홀드 |
| | 영문명 / 약어 | Context Threshold (CT) |
| **정의** | 공식 정의 | 프로젝트 운영 Context가 충분히 성숙하여 AI가 사람의 개입 없이 자율적 판단을 시작하는 임계점 |
| | 목적 | 모델 성능이 아니라 운영 Context의 성숙도가 AI 자율성을 결정한다는 가설을 설명한다 |
| | 핵심 질문 | AI는 언제부터, 왜 자율적으로 판단하기 시작하는가 |
| **분류** | Type | Hypothesis *(아직 단일 관찰에 기반한 미검증 가설 — Concept Dictionary 정의에 따라 Theory가 아닌 Hypothesis로 분류)* |
| | Status | Candidate |
| | Stability | Experimental |
| **관계** | 상위 개념 | C-00012 (컨텍스트 레이어) |
| | 하위 개념 | C-00017 (컨텍스트 쓰레시홀드 지수, CTI) *[Forward Reference — 미작성, ID 예약]* |
| | 관련 개념 | C-00018 (클로드 컨텍스트 쓰레시홀드 관찰 사례) *[Forward Reference — 미작성, ID 예약. Pilot-005에서 정식 작성 예정]* |
| | Before(전 단계) | C-00018 (클로드 관찰 사례) *[관찰이 가설보다 먼저 발생 — 시간순 관계이므로 Rule 15상 상위/하위와 별개로 유지]* |
| | After(후 단계) | C-00017 (CTI) |
| **비교** | 기존 유사 개념 | Context Window, Context Engineering, Context Threshold (Claude Code 등 일부 환경에서 "토큰 임계값 — 자동 압축/Compaction 트리거" 의미로 사용) |
| | 차이점 | 동일한 이름이 이미 업계에서 사용 중이나 완전히 다른 의미다. 업계의 Context Threshold는 **모델 내부 토큰 관리** 임계값(압축 시점)을 가리키는 반면, 본 개념은 **프로젝트 운영 Context의 성숙도**에 따른 자율성 발생 임계점을 가리킨다. 영역 자체가 다르다(모델 메모리 관리 vs 프로젝트 운영) |
| | 용어 유형 | 기존용어조합+신개념 |
| | Official Name 후보 | Context Threshold / Operational Context Threshold / Collaboration Context Threshold / Autonomous Context Threshold / Context Maturity Threshold / Context Readiness Threshold *(이름 미확정 — 정의와 차별점을 먼저 고정하고, 동명이의 충돌 해소를 위해 추후 비교 후 확정)* |
| | Semantic Boundary | Claude Code 등 일부 환경의 Context Threshold는 모델의 토큰 사용량에 따른 자동 압축(Compaction) 시점을 의미한다. 본 개념은 프로젝트 운영 맥락(Context Layer)의 성숙도에 따라 AI 자율성이 발생하는 시점을 의미한다. 측정 대상(토큰 vs 운영 성숙도)과 결과(압축 실행 vs 자율판단 시작)가 모두 다르다 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | "왜 Claude는 어느 순간 갑자기 자율적으로 변했을까?"라는 질문을 끝까지 추적하는 과정에서 가설로 도달함. 이후 AI Overview 검색을 통해 동명의 기존 업계 용어(토큰관리형)가 발견되어 차별화 필요성이 확인됨 |
| | Decision Origin | 없음 |
| | Evidence | C-00018 (클로드 관찰 사례) — *권장 필드, Type=Hypothesis이므로 Manual Rule 12에 따라 권장* |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Pilot-004) |
| | Review Result | 검토 대기 |
| | Review Notes | After(C-00017)와 하위 개념(C-00017)이 동일 대상을 가리킴 — Rule 15 예외 사유: CTI는 Context Threshold를 측정하는 지표이므로 "포함관계(하위)"와 "다음 단계(After, 가설→측정으로 이어지는 절차)"가 본질적으로 같은 방향을 가리키는 게 자연스러운 케이스. 의식적 허용 |
| | 비고 | 이름이 미확정인 첫 Pilot 사례. Naming Guide 절차(개념 먼저, 이름 나중)를 그대로 적용한 케이스 |

---

## Pilot 검증 메모

- **동명이의 충돌을 정면으로 다룬 첫 카드.** "기존 유사 개념" 필드에 숨기지 않고 명시(Manual Rule 6)했고, 차이점에서 영역 자체가 다름을 명확히 했다 — Standard가 설계한 대로 정확히 작동함.
- **Before가 상위/하위와 다른 대상(C-00018)을 가리키고, After는 하위 개념(C-00017)과 동일한 대상을 가리킴.** Rule 15("가능한 한 서로 다른 대상")는 지켜졌으나, After=하위개념 중복은 자연스러운 예외로 보임 — Pilot-003에서 정한 "예외 시 Review Notes에 기록" 원칙을 여기 적용해야 하는지 확인 필요.
- Type=Hypothesis로 분류하면서 Evidence가 처음으로 "권장" 등급에서 실제 채워짐 — Manual Rule 12(Type별 Evidence 권장기준)이 의도대로 작동.
- Official Name 후보가 6개나 등록된 첫 사례 — 이 정도 규모의 후보 비교를 Naming Guide 차원에서 한 번 더 다뤄야 할 수도 있음 (다음 Pilot 또는 별도 Sprint 후보).
