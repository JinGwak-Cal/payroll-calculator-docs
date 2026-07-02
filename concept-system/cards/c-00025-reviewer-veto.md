# C-00025 : 리뷰어 우선권 (Reviewer Quality Veto)

| 그룹 | 필드 | 내용 |
|---|---|---|
| **식별** | Concept ID | C-00025 |
| | Coordinate | R-03 |
| **기본** | 이름(한글) | 리뷰어 우선권 |
| | 영문명 / 약어 | Reviewer Quality Veto |
| **정의** | 공식 정의 | 디스패처가 작업 흐름을 통제하더라도, 품질 판단에서는 Reviewer의 결정이 디스패처보다 우선한다는 권한 규칙 |
| | 목적 | 속도(흐름 유지)가 품질(검증)을 침해하지 못하도록 권한 서열을 명확히 한다 |
| | 핵심 질문 | 흐름과 품질이 충돌할 때 누구의 판단이 우선하는가 |
| **분류** | Type | Rule |
| | Status | Candidate |
| | Stability | Emerging |
| **관계** | 상위 개념 | C-00023 (역할분리) |
| | 하위 개념 | 없음 |
| | 관련 개념 | C-00020 (Review System) |
| | Before(전 단계) | C-00023 (역할분리) |
| | After(후 단계) | 없음 |
| **비교** | 기존 유사 개념 | Quality Gate, Branch Protection Rule (Git) |
| | 차이점 | Quality Gate는 보통 자동화된 검사(테스트 통과 등)를 가리키지만, 본 개념은 **사람 또는 AI Reviewer의 주관적 품질 판단에 거부권을 부여**하는 권한 규칙이라는 점에서 다르다 |
| | 용어 유형 | 기존용어확장 |
| | Official Name 후보 | Reviewer Quality Veto(현재) / Reviewer Veto / Reviewer Quality Authority — 현재 이름 유지, 추후 비교 가능성만 기록 |
| **근거** | Origin Thread | Research Thread #001 |
| | Discovery Context | Dispatcher가 작업 흐름의 속도를 우선시할 경우 품질이 희생될 위험이 논의되며, Reviewer에게 명시적 거부권을 부여하는 방향으로 정리됨 |
| | Decision Origin | 없음 |
| | Evidence | 없음 |
| **관리** | Version | v1.0 |
| | Last Updated | 2026-06-30 |
| | 변경 이력 | 최초 작성 (Sprint-1, 묶음1-3) |
| | Review Result | Approved |
| | Review Notes | 묶음1(Rule군) 일괄 승인. Rule군 중 AI Company 운영철학(속도보다 품질 우선)을 가장 잘 드러내는 카드로 평가됨. 영문명 대안 후보 기록(현재명 유지) |
| | 비고 | C-00023 템플릿 적용 — Rule군 묶음 리뷰 대상 |
