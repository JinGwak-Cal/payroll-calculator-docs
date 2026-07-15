# 현재 작업 단계

업데이트: 2026-07-06 (Thread Closing Review 완료 — Bridge Day-1 종료, Payroll 출시 우선 전환)

---

## 구조1 — 현재 Sprint

**Sprint-2 준비 완료**

Sprint-1 완료 (2026-07-02):
- Concept Cards 43개 GitHub main 반영
- TCA v1.4 Methodology Baseline FROZEN
- Engineering Change Registry v1.1 신설
- Thread Transition Manifest TM-001 작성
- 2차 Batch Release 완료

---

## 구조2 — 현재 우선순위  ← 현재

**Release Priority (신규 최우선, 2026-07-06 전략 전환)**
Payroll Calculator 출시 우선 — 현금흐름 확보가 현재 최우선 목표.
(2026-07-11 D-TF-003로 재확인: 보안·권한 최적화보다 속도 우선,
저장소/문서는 전면 공개 상태 유지)
Threshold Foundry는 운영을 멈추지 않고 Evidence를 계속 축적하되,
새 방법론/Rule 승격(Promotion)은 출시를 우선하며 상황에 따라
유연하게 판단한다 (못박힌 게이트 아님).

**Infrastructure Priority — 완료 (2026-07-06)**
BR-001 (Bridge Day-1 MVP + Layer2 GPT↔Claude 자동전달)
- 결정: `decisions.md` D-BR-001(Layer1), D-BR-004~006(Layer2)
- Layer1: ai-bridge-workbench 배포 완료, 실사용 확인
- Layer2: OpenRouter 경유 Claude+OpenAI 연동, Playwright E2E
  실브라우저 검증 완료 (author:CLAUDE 메시지가 GPT 재호출 payload에
  포함되는 것까지 확인)
- Day-2 백로그: Persistence, Budget Cap 로직, 여러 Question 동시
  관리, 배포 시 인증 필요 (구조4 Deferred 참조)

**Operational Priority (TOP-001/ER-001) — Paycheck Workbook 출시 후행**
Release Priority 확정 이후 순서를 바로잡음: 인프라 작업은 출시를
막지 않는 후행 작업으로 재배치. Threshold Foundry는 "선행 작업"이
아니라 "Evidence 축적 → 후행 반영" 트랙으로 운영.

TOP-001 (Token Optimization Protocol / OCE 첫 번째 프로토콜)
- Part 0~10 구조 설계 후 작성
- Trigger: Paycheck Workbook 출시 이후

**Engineering Priority**
ER-001 (Environment Reconstruction)
- DS-001 + DS-002 기반 GPT 독립 수행
- Trigger: TOP-001 완료 후 (DF-00002)

---

## 구조3 — 다음 작업

```
새 쓰레드 시작 시:
1. merged-context.md 읽기 검증
2. **ResultGrid 배치 원칙·세부 배치 설계 (STEP2 구현 선행작업,
   D-PW-034)** — ResultGrid 역할·Row구조는 D-05-01/D-05-02에서
   이미 SoT 확정됨. 확정된 정보 우선순위(상태속성→시간속성→
   세금/공제)에 따라 세부 배치를 완료한 후 STEP2로 진행
3. 이어서 Paycheck Workbook STEP2(AllowanceRecord Browser/수당근무
   목록) 구현 착수
   - Row 구성·공통규칙 확정됨: D-PW-028~033 (2026-07-13)
   - UX 확정: 형태=테이블, 진입=ResultGrid "전체보기" 버튼,
     삭제=목록에서 바로
   - 현황(2026-07-09/11 Evidence): Editor(AllowanceDrawer) 완료 /
     Browser(목록 UI) 미구현 — D-PW-022 Role 기준 Gap 확정
   - 착수 파일: src/components/premium/AllowanceBrowser.tsx (신규)
   - 참고: SinglePremiumCard/DoublePremiumCard/TriplePremiumCard는
     dead code(미사용) — Browser 작업 시 혼동 주의
4. TOP-001/ER-001은 Paycheck Workbook 출시 이후
```

---

## 구조4 — Deferred 요약 (14건)

| Category | Count | 대표 항목 |
|---|---|---|
| Next Sprint | 4 | TOP-001, ER-001, GPT 프롬프트, document 10 |
| Research | 4 | RN-001B 완성, TP-002, TAP, DHM |
| Future | 4 | C-00002/003/039/041 카드화 |
| Long-term | 1 | manual-v14 이관 |
| Process | 1 | E-009/E-010/E-011 원칙은 absolute-rules 승격 완료(DF-00028). 나머지 방법론 Candidate(DF-00029~034)는 Payroll 출시 우선, 유연 판단 |
| Bridge Layer2 | 4 | Persistence, Budget Cap 로직, 여러 Question 동시 관리, 배포 시 인증 |

전체 목록: `research/patch-registry.md` Deferred Register 참조

---

## 구조5 — 참조 문서

- `research/tm-001-thread-transition-manifest.md` — Thread Bootstrap
- `research/sprint-1-closing-review.md` — Sprint-1 Baseline
- `research/tca-thread-closing-audit-protocol.md` — Closing 방법론
- `research/patch-registry.md` — Engineering Change Registry
- `engineering/er-000-environment-engineering-foundation.md` — Engineering Foundation

---

## 구조6 — 이전 완료 (Paycheck Workbook)

TASK-001 AI Push 구축 완료 (2606.29)
TASK-002 AI Push 기반 첫 운영 변경 완료 (2606.29)
Concept System Sprint-1 완료 (2026-07-02)
