# Engineering Change Registry

Version: v1.1
Status: Active
Start: Sprint-1 Baseline (2026-07-02)

---

## Change Type 정의

| Type | 코드 | 의미 |
|---|---|---|
| Baseline | BL | 기준선 확립 |
| Change Proposal | CH | 변경 제안 (왜 변경했는가) |
| Patch | PF | 문서 수정 적용 |
| Review Decision | RV | 검토 결정 기록 |
| Freeze | FR | 문서 동결 |
| Promotion | PM | 개념/문서 승격 |

---

## Registry

| Global ID | Type | Local ID | Target | Status | Reason | Evidence | Reviewer | Date |
|---|---|---|---|---|---|---|---|---|
| BL-00001 | BL | — | Sprint-1 Closing Review v2.1 | Confirmed | Sprint-1 Freeze. Registry 시작점 | Sprint-1 Closing Review | GPT+Claude | 2026-07-02 |
| PF-00001 | PF | SCR-P01 | Sprint-1 Closing Review | Applied | Section Order 변경 (Asset Review→Freeze Review) | GPT Review | GPT | 2026-07-02 |
| PF-00002 | PF | SCR-P02 | Sprint-1 Closing Review | Applied | Asset Lifecycle 확장 | GPT Review | GPT | 2026-07-02 |
| PF-00003 | PF | SCR-P03 | Sprint-1 Closing Review | Applied | Frozen/Reference Inputs 분리 | GPT Review | GPT | 2026-07-02 |
| PF-00004 | PF | SCR-P04 | Sprint-1 Closing Review | Applied | Lesson 7 Engineering Principle 승격 | GPT Review | GPT | 2026-07-02 |
| PF-00005 | PF | SCR-P05 | Sprint-1 Closing Review | Applied | Research Statistics 섹션 신설 | GPT Review | GPT | 2026-07-02 |
| PF-00006 | PF | SCR-P06 | Sprint-1 Closing Review | Applied | 제목 Baseline Charter v1.0 명시 | GPT Review | GPT | 2026-07-02 |
| FR-00001 | FR | — | Sprint-1 Closing Review v2.1 | Frozen | Sprint-1 Baseline Document | BL-00001 | GPT+Claude | 2026-07-02 |
| FR-00002 | FR | — | ER-000 v1.0 | Frozen | Engineering Foundation | ER-000 | GPT+Claude | 2026-07-02 |
| FR-00003 | FR | — | RN-001A v1.1 | Frozen | Research Protocol | RN-001A | GPT+Claude | 2026-07-02 |
| PF-00007 | PF | ECR-P01 | Engineering Change Registry | Applied | CH 타입 추가, Reason/Evidence 컬럼 추가 | GPT Review | GPT | 2026-07-02 |
| FR-00004 | FR | — | TCA v1.4 | Frozen | Methodology Baseline FROZEN | GPT+Claude | 2026-07-02 |
| FR-00005 | FR | — | Thread Closing Review v1.1 | Freeze Candidate | Exit Criteria 완료 후 FROZEN 예정 | GPT+Claude | 2026-07-02 |

---

## Deferred Register (Sprint-2 처리 대기)

| Deferred ID | 항목 | 출처 | Timeline | Owner | Trigger |
|---|---|---|---|---|---|
| DF-00001 | document 10 Threshold Foundry 통찰 5건 반영 | Sprint-1 합의 | Next Sprint | ER-001 이후 | Thread Start |
| DF-00002 | ER-001 착수 (GPT 독립 수행) | Sprint-1 Closing Review | Next Sprint | ER-001 | TOP-001 완료 후 |
| DF-00003 | GPT ER-001 수행 요청 프롬프트 작성 | 이 쓰레드 | Next Sprint | ER-001 | Thread Start |
| DF-00004 | 4계층 Context 저장 구조 설계 | RN-001B Backlog | Research | ER-001 이후 | ER-001 완료 |
| DF-00005 | C-00002 쓰레드 클로징 파이프라인 카드 | Forward Reference | Future | Sprint-2 | Sprint-2 착수 |
| DF-00006 | C-00003 Concept Card 자체 카드화 | Forward Reference | Future | Sprint-2 | Sprint-2 착수 |
| DF-00007 | C-00039 SoT Integration 카드 | Forward Reference | Future | Architecture | Architecture군 검토 후 |
| DF-00008 | C-00041 RCS 카드화 | RCS v1.1 존재 | Future | Sprint-2 | Sprint-2 착수 |
| DF-00009 | manual-v14 협업 원칙 → thread-handoff 이관 | 이 쓰레드 논의 | Long-term | TOP-001 | TOP-001 완료 후 |
| DF-00010 | Batch Release 2차 | 로컬 커밋 대기 | — | — | ✅ Completed |
| DF-00011 | ECR GitHub 반영 | 이 쓰레드 | — | — | ✅ Completed |
| DF-00020 | RN-001B 완성 (Source A~H 수집) | Thread Closing Audit | Research | RN-001 | ER-001 착수 후 |
| DF-00021 | TOP-001 작성 | Sprint-1 Thread Closing | Next Sprint | TF-S02-T01 | Thread Start |
| DF-00022 | OCE 프레임워크 설계 | Sprint-1 Thread Closing | Next Sprint | TOP-001 | TOP-001 완료 |
| DF-00023 | TP-002: TCA Lifecycle 순서 개선 | Sprint-1 Thread Closing | Research | ER-001 이후 | ER-001 시작 |
| DF-00024 | TAP 설계 | Sprint-1 Thread Closing | Research | Sprint-2 | TCA Evidence 확보 |
| DF-00025 | DHM 설계 | Sprint-1 Thread Closing | Research | Sprint-2 | TAP 완료 후 |
| DF-00026 | Research State Model | Sprint-1 Thread Closing | Research | RN-001B | ER-001 착수 |
| DF-00027 | TNS Thread ID 소급 적용 | Manual Rule 18 | Future | Sprint-2+ | Sprint-2 착수 |

---

## 운영 규칙

1. 모든 변경은 CH(제안) → RV(검토) → PF(적용) 순서로 기록한다.
2. Global ID는 Type-순번 형식 (5자리).
3. Deferred 항목은 Deferred Register에 먼저 등록한다.
4. Reviewer 반드시 명시.

**Next IDs**: PF-00008 / FR-00006 / CH-00001 / RV-00001 / PM-00001 / DF-00028

---

*Version: v1.1 | BL-00001 기준 | Sprint-2부터 전면 적용*
