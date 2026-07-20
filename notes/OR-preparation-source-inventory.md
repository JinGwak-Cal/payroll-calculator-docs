# Operation Review — 준비 문서 (Work Package + Source Inventory)

## Work Package Contract

```
목표: 최초 정식 Operation Review 수행 (Pilot v0와 달리 검증된
      Evidence 기반)
Input: Original Sources(Claude/GPT Thread 원문), SoT(4개 파일),
      Repository(로컬 clone), 사용자 첨부(zip 2개, Need Unknown)
Authority(판단 기준): Condition1, SoT(decisions/current-step/
      absolute-rules/research-backlog), 오늘 합의된 결정들
범위: A-08/C-07/C-14 등 핵심 Rule 위반 실측, 오늘 산출물 정리,
      Gap 분석, 다음 작업 패키지 도출
완료조건(Exit): Operation Review 문서 완성 + Evidence Source
      Inventory 확정 + push 여부 결정(실행은 별도)
제외범위(Deferred): REA Patch 27건 적용, RCA 정식 재파일럿 실행,
      저장소 재구조화 실행 — 이 Review에서는 "결정"까지만,
      "실행"은 별도 승인 후
산출물: 본 문서, Operation Review 본문(뒤에 작성)
가정(Assumptions): Claude 원본=텍스트만(생성파일 내용 미포함),
      GPT 원본=Chrome 직접 복사 확인(Export 메타데이터 미포함
      가능성 있음)
```

## Evidence Source Inventory (STEP0-A)

| Source | 확보 | 비고 |
|---|---|---|
| A. Claude Thread 원문 | ✅ | 메시지 1~278, URL 대조 확인. 생성 파일(REA-001 등) 실제 내용은 미포함(파일명만) |
| B. GPT Thread 원문 | ✅ | Chrome에서 직접 열어 복사 확인(사용자 확인). Export 메타데이터는 미포함될 수 있음 |
| C. Repository(로컬 clone) | ✅ | bash 직접 검증 가능, 오늘 이미 여러 차례 grep/git status 확인 |
| D. SoT 4개 파일 | ✅ | decisions/current-step/absolute-rules/research-backlog, 오늘 실측 완료 |
| E. 사용자 첨부 zip(0720마누스_클로드실행files, Pilot_V0_files) | **Need Unknown** | Physical 미확보(제 환경엔 미업로드). 필요 여부·용도(Reference/Archive/Evidence/Artifact) 자체가 미판정 |
| F. 파트너 산출물(REA/RCA/Walkthrough md) | ✅ | 제가 직접 생성한 것이라 로컬 저장소에 실제 파일로 존재 |

## Source Completeness Check

**Physical Completeness (파일 자체가 존재하는가)**
- A,B,C,D,F: ✅ 존재 확인
- E: Physical 미확보(제 환경엔 미업로드)

**Operational Completeness (이번 Operation 목적 수행에 충분한가)**
- 목적(Rule 위반 실측, SoT Gap 확인)에는 A+B+C+D+F로 충분 — E 없이도 수행 가능
- E의 실제 용도는 Need Unknown이라 완전한 Operational Completeness 판정은 STEP1 이후로 유보

## 원본 확보 도구 (Source Capture Method)

→ 참조: `source-capture-method-reference.md` (매 Operation Review마다
반복 기술하지 않음)

## Transition 판정 (STEP0 → STEP1)

```
STEP0 종료
Input: Original Sources(A,B) + SoT(D) + Repository(C) + 첨부(E, 미판정)
Evidence: 위 Source Inventory 표(grep/git status/사용자확인으로 실측)
Remaining Risk: E(zip 2건) 용도 Need Unknown / F(파트너 산출물)
  분류 미완 / STEP1 Evidence Classification 체계 미완
Transition: Go
Reason: STEP1(Evidence Collection)이 요구하는 입력은 A, B, C, D, F —
  전부 확보 완료(Operational Completeness 충족). E는 Need Unknown
  이나 STEP1 핵심 목적(Rule 위반 실측)에 불필요하므로 Hold 사유
  아님
```
