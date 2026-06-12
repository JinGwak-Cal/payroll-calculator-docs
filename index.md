# payroll-calculator-docs

급여 계산기 앱 개발 및 AI 협업 운영을 위한 문서 저장소.

---

## 구조1 문서 개요

### 목차01 프로젝트 목적
- 급여 계산기 앱의 설계·구현·검증 기록
- AI 파트너(Claude/GPT)와의 협업 운영 규칙 관리
- 문서 체계를 통한 컨텍스트 유지 및 인계

### 목차02 새 쓰레드 시작 방법

> **표준 진입 프롬프트 정본은 이 섹션에 저장한다.**
> 새 쓰레드 준비 요청 시 AI는 아래 전문을 복붙 가능한 형태로 출력한다.

---
**[표준 진입 프롬프트 — 복붙용]**

이어서 작업하자. 읽기 검증 프로토콜부터 실행.

우선순위:
1. docs repo 존재 여부 확인
2. repo 존재 시 (bash_tool 가능):
   git fetch origin
   git checkout origin/main -- merged-context.md
3. repo 없거나 git fetch 불가 시:
   Raw URL 시도 → 실패 시 blob URL → 실패 시 jsDelivr

반드시 아래를 원문 인용하여 읽기 성공 증명:
- merged-context.md Auto-generated timestamp
- merged-context.md Source 라인
- current-step 또는 decisions 또는 absolute-rules 최근 항목 1건
- 현재 작업이 current-step 어느 항목인지 설명

인용 없는 ■ 확보는 확보로 인정하지 않는다.

문서: https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/merged-context.md

읽기 검증 완료 후 대기.
---

---

## 구조2 Source of Truth 안내

### 목차01 SoT 3문서 정의
이 저장소의 Source of Truth는 아래 3문서다.

| 문서 | 역할 | SoT |
|------|------|-----|
| absolute-rules.md | 모든 AI 파트너 공통 강제 규칙 | ✅ |
| decisions.md | 확정된 설계·정책 결정 근거 | ✅ |
| current-step.md | 현재 작업 단계 및 전체 로드맵 | ✅ |
| index.md | 진입점·안내·문서 구조 설명 | 파생 |
| merged-context.md | AI 읽기용 자동 통합본 | 파생 |
| archive/ | 과거 기록 보관 | 참조용 |

### 목차02 우선순위
충돌 시 우선순위:
```
absolute-rules > decisions > current-step > index > merged-context
```

---

## 구조3 merged-context 안내

### 목차01 파생본 설명
- merged-context.md = absolute-rules + decisions + current-step 자동 통합본
- **SoT 아님** — 원본 3문서가 항상 우선
- 충돌 발견 시 원본 3문서 기준으로 판단
- GitHub Actions가 3문서 변경 시 자동 재생성

### 목차02 URL 및 실패 시 처리
**정상 접근:**
```
raw: https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/merged-context.md
blob: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/merged-context.md
```

**접근 실패 시:**
Jin님이 직접 최신본을 복붙하거나,
absolute-rules GitHub 문서 읽기 규칙의 우회 순서를 따른다.

---

## 구조4 문서 위치 안내

### 목차01 각 문서 역할 및 위치

| 문서 | 역할 | raw URL |
|------|------|---------|
| absolute-rules.md | AI 파트너 공통 규칙 | https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/absolute-rules.md |
| decisions.md | 설계·정책 결정 근거 | https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/decisions.md |
| current-step.md | 현재 작업 단계 | https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/current-step.md |
| index.md | 진입점·문서지도·링크허브 | https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/index.md |
| merged-context.md | AI 읽기용 통합본 | https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/merged-context.md |

### 목차02 archive 위치
과거 기록 및 폐기·이관된 항목:
```
archive/
  absolute-rules-before-0612.md  ← absolute-rules 개편 전 원본 백업
  absolute-rules-retired.md      ← absolute-rules 폐기 항목
  decisions-retired.md           ← decisions 폐기 항목
  current-step-retired.md        ← current-step 완료 이력
  index-retired.md               ← index 이관·흡수 이력 (예정)
```

blob: https://github.com/JinGwak-Cal/payroll-calculator-docs/tree/main/archive

