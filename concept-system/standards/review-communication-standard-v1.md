# Review Communication Standard (RCS) v1.0
Status: Confirmed

## 목적 (Purpose)

GPT와 Claude 등 협업 파트너 간 검토 결과를 빠짐없이, 한 번의 복사·붙여넣기로 전달하기 위한 표준 응답 형식을 정의한다.

---

## 기본 원칙 (Principles)

1. 협업 파트너가 반드시 알아야 하는 내용은 예외 없이 Partner Copy 영역에 포함한다.
2. 사용자를 위한 설명과 파트너 전달용 내용은 분리한다.
3. 응답의 첫 부분은 항상 Partner Copy로 시작한다.
4. Partner Copy는 하나의 코드블록으로 작성하여 한 번에 복사할 수 있도록 한다.
5. GPT Notes에는 설명, 통찰, 장기 아이디어만 작성한다.
6. 파트너가 검토하거나 판단해야 할 내용은 GPT Notes에만 존재해서는 안 된다.
7. Partner Copy만 전달해도 협업이 가능해야 한다.

---

## 표준 응답 구조 (Standard Response Structure)

① Partner Copy → ② GPT Notes 순서를 기본으로 한다.

---

## Partner Copy 표준 형식

```
Document
- [검토 대상 카드 ID 및 이름]

Approval
(Approved / Approved with Minor Improvements / Change Requested / Rejected)

Review Result
- 전체 검토 결과
- 핵심 결론

Changes
- 수정이 필요한 사항
- 변경 권고 사항

Rationale
- 판단 근거
- 적용한 원칙
- 기존 결정과의 관계

Check Items

즉시 반영
- 실제 수정 대상만 기록한다. 설명이나 의견은 포함하지 않는다.

Backlog
- 다음 Sprint
- 추후 검토
- 보류 항목

Decision

확정
- 이번에 확정된 내용

보류
- 나중에 다시 검토할 내용
```

---

## GPT Notes

Partner Copy 이후에만 작성한다.

허용 내용: 추가 설명, 장기 통찰, 대안 비교, 향후 아이디어, 참고사항.

금지: Partner Copy에 없는 새로운 수정사항, Partner가 반드시 알아야 하는 결정사항.

---

## 문체 규칙 (Writing Rules)

1. 한글 제목과 영문 제목을 기본 병기한다. 예) Context Threshold (컨텍스트 쓰레시홀드)
2. Concept ID, Coordinate, 약어(CTI, HDR 등), 기호는 가능한 한 한글 설명과 함께 표기한다.
3. 문장은 자연스러운 문단으로 작성한다.
4. 한두 단어만 쓰고 반복적으로 줄을 바꾸는 문체를 사용하지 않는다.
5. 제목, 표, 단계도, 계층 구조 등 구조 표현이 필요한 경우에만 줄바꿈을 사용한다.
6. 설명 문단은 일반 문장처럼 이어서 작성한다.

나쁜 예) "Dispatcher는 / 작업을 / 관리한다."
좋은 예) "Dispatcher는 작업 흐름을 관리한다."

---

## 목표

읽기 쉽고, 복사하기 쉽고, 누락 없이, AI와 사람 모두가 동일한 정보를 공유할 수 있는 협업 응답 형식을 유지한다.

---

*Version: v1.1 | Status: Confirmed | Origin: Research Thread #001 → Sprint-1 운영 중 확정. v1.1: Document 헤더 추가, Check Items 운영 기준 명시*
