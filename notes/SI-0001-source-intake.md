# SI-0001 — Source Intake Register (P1)

```
ID: SI-0001
Parent ID: PI-0000
Root Pilot ID: PI-0000
Related IDs: —
Current Stage: P1
```

근거: `OR-preparation-source-inventory.md`(Evidence Source
Inventory, 2026-07-20 grep/git status 실측)를 Pilot 표준 형식으로
재등록.

| Source ID | 유형 | 상태 | Physical | Operational | 비고 |
|---|---|---|---|---|---|
| SRC-A | Raw Source | Available | ✅ | ✅ | Claude Thread 원문(메시지 1~278), URL 대조 확인. 생성 파일 실제 내용 미포함(파일명만) |
| SRC-B | Raw Source | Available | ✅ | ✅ | GPT Thread 원문, Chrome 직접 복사 확인(사용자 확인). Export 메타데이터 미포함 가능 |
| SRC-C | Raw Source | Available | ✅ | ✅ | Repository(로컬 clone), bash 직접 검증 가능 |
| SRC-D | Raw Source | Available | ✅ | ✅ | SoT 4개 파일(decisions/current-step/absolute-rules/research-backlog) |
| SRC-E | Archive(후보) | Need Unknown | ❌ | 미판정 | 사용자 첨부 zip 2건(0720마누스_클로드실행files, Pilot_V0_files) — 제 환경 미업로드, 용도 미판정 |
| SRC-F | **Derived Artifact** (재분류, CL-002) | Available | ✅ | ✅ | REA/RCA/Walkthrough 등 — 독립 Source 아님, 참고자료로만 사용 |

## Source Completeness Check (P1 결과)

- **Physical**: SRC-A,B,C,D,F 확보 / SRC-E 미확보
- **Operational**: 이번 Pilot(Claim-1,2,3)에는 SRC-A + SRC-C로
  충분. SRC-B는 보조참고, SRC-D는 Claim-3(산출물 분류) 검증용,
  SRC-E는 불필요(Claim 범위 밖)

## Transition (P1 → P2)

```
Transition: Go
Reason: Claim-1(A-08), Claim-2(C-07), Claim-3(산출물 4분류) 각각
  요구하는 Source(SRC-A, SRC-C, SRC-D)가 전부 Available.
  SRC-E(Need Unknown)는 이번 Pilot Claim 범위 밖이라 Hold 사유
  아님 — Deferred Issue로만 기록
```

Prepared: Claude / Checked: (P4 Walkthrough 시 GPT) / Approved: (대기)
