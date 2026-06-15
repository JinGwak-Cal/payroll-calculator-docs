<!-- Auto-generated at 2026-06-15T05:51:48Z -->
<!-- Source: absolute-rules.md + current-step.md + decisions.md -->
<!-- index.md 는 이 파일의 생성 대상이 아닙니다 -->

# ── absolute-rules.md ──────────────────────────────────────

# absolute-rules.md vNext
# 개정 기준: 0611~0612 문서 체계 개편
# Before 기준: GitHub origin/main 238줄
# After 구조: v1.1 확정안

---

# 구조1 앱 코드 규칙

## 절대 규칙 (v14.0 기준)
- v14.0 기준 고정
- 재정의 금지
- 없는 부분만 추가 허용
- 전체 재작성 금지
- 증분 코드만 출력
- 캘디게 구조 변경 금지
- 계산은 항상 수행 / 표시만 제어
- premiumAmount state 저장 금지
- 입력은 state / 결과는 useMemo 원칙 유지

---

# 구조2 작업 시작 및 문서 확보

> **Source of Truth 원칙**
> SoT = absolute-rules.md / decisions.md / current-step.md
> merged-context.md = 위 3문서의 파생 통합본 (AI 읽기용 진입 편의 목적)
> 충돌 시 원본 3문서 우선. merged-context는 SoT 아님.

## 목차01 신규 쓰레드 시작 프로토콜
새 쓰레드가 시작되는 순간, 첫 메시지가 무엇이든 간에,
아무것도 묻지 않고 아래를 먼저 실행한다.

1. GitHub 문서 읽기 규칙에 따라 merged-context.md 최신본 확보
2. 읽기 검증 프로토콜 수행
3. 확보 상태 표시
4. 작업 시작 지시인 경우에만 reviews/active 확인

위 과정 실패 시:
- □ 미확보 표시
- 실패 사유만 보고
- 현재 단계 판단 / 작업 시작 / 구현 방향 결정 / 코드 생성 / 우선순위 판단 금지

### 표준 진입 프롬프트 출력 규칙
사용자가 아래 표현을 사용하면:
- "새 쓰레드 준비해줘"
- "새 쓰레드로 옮기자"
- "진입점 만들어줘"
- "새 쓰레드로 넘어가자"

AI는 간단한 안내 한 줄 후,
index.md 구조1-목차02의 표준 진입 프롬프트 전문을
임의 요약·축약·변형 없이 복붙 가능한 형태로 출력한다.
표준 진입 프롬프트 정본은 index.md 구조1-목차02에 저장한다.

## 목차02 GitHub 문서 읽기 규칙

### 서브목차01 신규 쓰레드 첫 진입
새 컨테이너 환경. repo 존재 여부에 따라 분기한다.

**repo 존재 시 (bash_tool 가능):**
1. ```
   cd /home/claude/docs  # 또는 동등 경로
   git fetch origin
   git checkout origin/main -- merged-context.md
   ```
2. merged-context.md Auto-generated timestamp 확인
3. 읽기 검증 프로토콜 수행
4. 작업 시작 상태 표시

**repo 없을 시 (새 컨테이너 또는 bash_tool 불가):**
→ 서브목차03 문서 확보 실패 시 우회로 진행

서브목차02 작업 중 재진입
로컬 docs repo 존재 시 git fetch 기반 최신화를 수행한다.

1. 로컬 repo 확인 (`/home/claude/docs` 또는 동등 경로)
2. git fetch origin
3. origin/main 기준으로 대상 파일 checkout
4. 읽기 검증 프로토콜 수행

리프레시 트리거:

직접 트리거 (사용자 명시 명령 → 즉시 위 절차 재실행):
"리프레시" / "다시 읽어줘" / "최신본 확인" / "최신본 맞아?"

간접 트리거 (외부 결과물·사용자 텍스트의 변경 신호 → 확인 게이트 출력):
"커밋됨" / "병합됨" / "main 갱신" / "반영 완료" / "pushed" / "merged" / "commit" / "PR merged"

리프레시 확인 게이트:
간접 트리거 감지 시 작업 판단을 멈추고 다음을 출력한다.
"외부 결과물에 main 변경 가능 신호가 있습니다. 현재 문서가 구버전일 수 있으므로 리프레시할까요?"
사용자가 직접 트리거 표현으로 승인 시 위 절차 재실행. 승인 없으면 현재 문서 기준으로 계속 진행.

### 서브목차03 문서 확보 실패 시 우회
bash_tool 사용 불가 시 단계별 우회 후 미확보 처리한다.

1. Raw URL: `https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/merged-context.md`
2. blob URL: `https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/merged-context.md`
3. jsDelivr CDN 재시도
4. 위 모두 실패 시 □ 미확보 표시

미확보 시:
- 읽기 시도 과정 순서대로 보고
- 실패 원인 판단 근거 제시
  (네트워크 차단 / 캐시 문제 / 권한 오류 / 파일 부재 등)
- 필요한 사용자 입력을 1회만 구체적으로 요청
  또는 실행 가능한 대안 1개만 제시
- 아래 항목 전면 금지:
  현재 단계 판단 / 작업 시작 / 구현 방향 결정 /
  코드 생성 / 우선순위 판단

## 목차03 읽기 검증 프로토콜
■ 확보 표시 후 반드시 아래를 제시한다. 인용 없는 ■ 확보는 확보로 인정하지 않는다.

확보 증명 게이트:

필수 (모든 AI 공통):
- merged-context.md Auto-generated timestamp 원문 인용
- merged-context.md Source 라인 원문 인용

가능 시 (bash_tool 환경):
- git fetch origin 실행 결과
- origin/main 기준 커밋 해시

(위 timestamp·Source 인용은 아래 읽기 검증 항목 1·2를 충족한 것으로 본다.)

1. merged-context.md Auto-generated timestamp 원문 인용
2. merged-context.md Source 라인 원문 인용
3. 아래 중 하나 원문 인용:
   * current-step 최근 변경사항 1건 + 변경 시각
   * decisions 최근 결정사항 1건 + 결정 시각
   * absolute-rules 최근 변경사항 1건 + 변경 시각
   * absolute-rules 최근 변경 없음 + 핵심 규칙 1건
4. 현재 작업이 current-step 어느 항목에 해당하는지 설명
위 조건 중 하나라도 충족하지 못하면 반드시 □ 미확보로 표시한다.

## 목차04 작업 시작 프로토콜
작업 시작 전 반드시 merged-context.md 확보 및 읽기 검증 완료 후에만 작업 가능.

### 서브목차01 확보 상태 표시 형식
```
[작업 시작 상태]
merged-context □ 미확보 / ■ 확보 (timestamp 기재)
current-step   □ 미확보 / ■ 확보
decisions      □ 미확보 / ■ 확보
absolute-rules □ 미확보 / ■ 확보
```

### 서브목차02 미확보 시 금지 항목
하나라도 미확보 시:
- 현재 STEP 추정 금지
- 구조 판단 금지
- 코드 생성 금지
- 읽기 실행 후 재시작

## 목차05 작업 시작 지시 정의
작업 시작 지시란 다음을 의미한다:
- 특정 STEP/G/P/BUG/UX 항목을 진행/검토/구현하라는 지시
- Codex/Claude/Agent 전달문 작성 요구
- "이어서 작업하자" 류의 지시

### 서브목차01 작업 시작 지시 해당 항목
- 특정 STEP/G/P/BUG/UX 진행·검토·구현 지시
- 전달문 작성 요구
- "이어서 작업하자" 류

### 서브목차02 작업 시작 지시 시 순서
1. merged-context.md 읽기 검증 완료 확인
2. reviews/active/ 관련 파일 존재 확인
3. 있으면 읽고 반영
4. 없으면 "active review 없음" 보고 후 진행

일반 질문(개념/비용/가능성)은 작업 시작 지시 아님
→ reviews/active 자동 참조 불필요

---

# 구조3 AI 협업 및 Reviews 운영

## 목차01 AI 협업 구조
Claude 검토 저장: reviews/active/claude/
GPT 검토 저장: reviews/active/gpt/
완료 작업 이동: reviews/completed/

index.md에는 reviews 전문 미포함
reviews는 필요 시 bash_tool로 직접 참조

## 목차02 Reviews 식별자 규칙 (확정)
형식: 작업단위(sub.n).파트너명.현업N-n.YYMMDDHHmm.md
총 12자리 날짜시간: 년2자+월2자+일2자+시2자+분2자

예시:
P4(1).claude.현업1-1.2605281430.md
P4(1).gpt.현업1-2.2605281510.md
P4(1).claude.현업1-3.2605281545.md
P4(1).claude.현업2-1.2605281600.md
P4(2).claude.현업1-1.2605281700.md

## 목차03 Reviews 목록 출력 규칙
- 최신 파일이 항상 맨 위에 표시
- 날짜시간 기준 내림차순 정렬
- Claude가 목록 출력 시 자동 적용

## 목차04 Reviews 목록 출력 형식
Claude가 reviews 파일 목록 출력 시 반드시 raw + blob URL 동시 표시:

파일명 (크기)
raw: https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/[경로]
blob: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/[경로]

이유: GPT는 blob URL 생성은 가능하지만 raw 실패 시 자동 전환이 보장되지 않음
따라서 GitHub 문서 전달 시 raw + blob URL을 함께 제공
Jin님이 두 URL 중 작동하는 것을 GPT에 전달

## 목차05 저장 후 검증 규칙
reviews 파일 저장 후 반드시:
1. 저장된 파일 내용 실제 읽기
2. 원본 내용과 비교
3. 누락 없음 확인 후 완료 보고
누락 발견 시 즉시 재저장

---

# 구조4 AI 행동 규칙

## 목차01 답변 정직성 규칙
사용자가 원하는 답을 예측하여 그 방향으로 답하는 것을 금지한다.
틀린 것을 알면서 정정하지 않는 것을 금지한다.
확실하지 않으면 즉시 "불확실"을 먼저 선언한다.

## 목차02 지시 이행 불가 시 응답 규칙
지시를 이행할 수 없는 경우 반드시 아래 형식으로 답변한다.
못 하는 이유: [구체적 원인]
대안: [가능한 방법]
"안 됩니다"만 답하는 것을 금지한다.

## 목차03 업데이트 위치 제안 규칙
업데이트 내용의 위치 제안 시 반드시:
1. 해당 문서의 전체 구조를 먼저 파악한다
2. "[A] (N번째 줄) 와 [B] (N번째 줄) 사이" 형식으로 명시한다
3. 위치 선정 이유를 함께 제시한다

## 목차04 작업 단계 선제 제시 규칙
지시 이행 시 반드시:
모든 작업 단계를 구분하여 일목요연하게
한 페이지 이내 분량으로 먼저 제시한다

---

# 구조5 협업 운영 규칙

## 목차01 생성·수정 통제 (§운영1+3+4)

### §운영-1 자동 판단 금지 (핵심 원칙)
명시적으로 요청되지 않은 행위를 금지한다.
- 보고=보고 / 조사=조사 / 검토=검토
- 생성·저장·업데이트는 명시적으로 요청된 경우에만 수행한다.

### §운영-3 읽기 전용 원칙
다음 표현은 모두 읽기 전용 요청으로 간주한다.
읽어줘 / 확인해줘 / 검토해줘 / 평가해줘 / 조사해줘 / 보고해줘
위 요청 시: 수정·생성·삭제·커밋·push 모두 금지

### §운영-4 생성 승인 원칙
다음 표현이 있을 때만 생성 행위를 허용한다.
생성해 / 작성해 / 저장해 / 등록해 / 업데이트해 / 반영해
위 표현이 없으면 생성 행위 금지
읽기 전용 표현 + 생성 표현이 동시 존재 시 생성 표현 우선

## 목차02 승인 원칙 (§운영2+5+8)

### §운영-2 승인 원칙
다음 행위는 반드시 Jin님 승인 후 진행한다.
- 파일 생성 / 삭제 / 덮어쓰기
- 보고용 문서 생성
- 커밋 / GitHub push / 원격 미러 업데이트
- current-step.md 수정 / decisions 수정 / absolute-rules 수정

### §운영-5 덮어쓰기 원칙
기존 파일이 존재할 경우 자동 덮어쓰기를 금지한다.
반드시 다음 중 하나를 사용자에게 확인받는다:
신규 파일 생성 / 기존 파일 업데이트 / 작업 중단
승인 응답을 받기 전까지 해당 파일에 대한 모든 작업을 중단한다.

### §운영-8 특별 관리 문서
current-step.md / decisions / absolute-rules
생성·수정·삭제 모두 승인 필수

## 목차03 GitHub 및 토큰 운영 (§운영6+7+Replit)

### §운영-6 GitHub 원칙
commit / push / 파일 생성·수정·삭제 / 원격 미러 업데이트
모두 명시적 승인 후 진행

### §운영-7 자동 커밋 원칙
사전 보고 가능 시 사전 보고. 불가능한 경우 발생 즉시 보고.
보고 항목: 커밋 해시 / 변경 파일 / 변경 내용 요약

### Replit 및 토큰 운영
- Replit Secrets에 3개 토큰 저장 완료
  → GITHUB_APP_TOKEN
  → GITHUB_DOCS_READ_TOKEN
  → GITHUB_DOCS_WRITE_TOKEN
- main 직접 푸시 금지 / PR 필수 / Jin님 승인 후 병합
- payroll-calculator-docs 수정은 Jin님 승인 및 PR 절차를 통해서만 허용
- 대화창 토큰 노출 원칙적으로 지양

## 목차04 범위 관리 (§운영9+10)

### §운영-9 범위 초과 원칙
작업 지시 범위 외 파일(.replit / index.css 전역 / 환경설정 등) 수정 금지
필요 시 사전 보고 후 승인

### §운영-10 계산 로직 특별 규칙
calc-engine.ts / use-calc.tsx / 계산 결과에 직접 영향을 주는 파일
수정 전 반드시: 변경 필요성 보고 → 영향 범위 보고 → 승인 획득

## 목차05 토큰 절약 원칙

토큰 절약의 적은 긴 답변이 아니라 재작업이다. 정확성은 하한선, 그 위에서 분량 최소화.
R1. 검토 요청 → 파일 안 건드림. 의견만.
R2. 승인 후 변경. 검토와 반영을 구분한다.
    검토 요청 시: 의견 제시만 / 문서수정·확정본작성·커밋지시 금지
    변경 필요 시: ①변경분 제시 ②검토결과 ③승인요청 ④승인 후 반영안 ⑤승인 후 수정
    변경은 승인 후 1회. 변경분만. 전체 재생성 금지.
R3. 변경분 우선. 변경 없는 내용 반복 금지. 결론 먼저, 근거는 필요 범위만.
    모든 검토·피드백·제안·평가는 두괄식(유지/변경/보완/추가/삭제/반려)으로 판단 먼저.
R4. 확정된 답은 다시 묻지 않는다.
R5. 불확실하면 추측해 길게 쓰지 말고 한 줄로 확인.
R6. 내용 바뀌면 제목도 변경. 중복본 양산 금지.

---

# 구조6 문서 체계 및 관리

## 목차01 문서 역할 정의

각 문서의 역할과 Source of Truth 범위:

| 문서 | 역할 | SoT 여부 |
|------|------|---------|
| absolute-rules.md | 모든 AI 파트너 공통 강제 규칙 | ✅ SoT |
| current-step.md | 현재 작업 단계 및 전체 로드맵 | ✅ SoT |
| decisions.md | 확정된 설계·정책 결정 근거 | ✅ SoT |
| index.md | 진입점·안내·문서 구조 설명 | 파생 (SoT 아님) |
| merged-context.md | AI 읽기용 자동 통합본 | 파생 (SoT 아님) |

연결 구조:
```
index.md (지도/진입점)
    ↓
absolute-rules.md (규범)
    ↓
decisions.md (근거)
    ↓
current-step.md (현재 상태)
    ↓
merged-context.md (AI용 자동 통합)
```

충돌 시 우선순위:
absolute-rules > decisions > current-step > index > merged-context

## 목차02 문서 식별 및 분류 체계

### 서브목차01 식별자 체계
형식: 상태-문서-구조-목차-서브목차

상태 코드:
- B = Before (개정 전)
- A = After (개정 후)

문서 식별자:
- A = absolute-rules
- I = index
- C = current-step
- D = decisions
- M = merged-context

예시: B-A-02-03-S01
- B = Before
- A = absolute-rules
- 02 = 구조2
- 03 = 목차03
- S01 = 서브목차01

### 서브목차02 sot 판정 기준
sot는 개정 후에도 해당 내용이 현행 Source of Truth, 현행 규칙으로 유지되는지를 표시한다.

- sot=y: K/R/S/M/T/N (개정 후 현행 규칙으로 유지)
- sot=n: X/archive 전용/구버전

### 서브목차03 복수분류 규칙
- 허용: 최대 2개 조합
- 순서: 앞=현재처리 / 뒤=이후처리
- 예: M+T / T+R / R+S
- 예외: K 단독 사용 / X 단독 사용

### 서브목차04 흡수 vs 살아남는 판정 기준
통합(M) 시 독립 목차는 사라질 수 있다.
단, 내용이 통합본에 남아 있으면 sot=y.
즉 형식(독립 목차)이 사라져도 내용이 현행 규칙에 존재하면 현행 유지로 판정한다.

### 서브목차05 archive 판정 기준
- archive=y: 폐기(X) / 구버전 / 현행 규칙에서 제외
- archive=n: 현행 유지 / 이동 / 통합 / 개정

### 서브목차06 분류코드 정의
| 코드 | 의미 |
|------|------|
| N | 신규 |
| K | 보존 |
| R | 개정 |
| S | 분리 |
| M | 통합 |
| T | 이동 |
| X | 폐기 |

## 목차03 대상 파일 판단 기준
- absolute-rules.md → 모든 파트너 공통 강제 규칙
- current-step.md → 현재 작업 단계 변경
- decisions.md → 확정된 결정 사항
- index.md → 진입점/운영구조 변경
- manual-v14.md → 앱 개발 설계/스펙 변경

## 목차04 매뉴얼 업데이트 규칙

### 업데이트 후 확인
- absolute-rules.md 수정 시:
  절대 규칙 및 운영 규칙이 약화/훼손되지 않았는가?

## 목차05 대기 표시 규칙
- 신규 대기 → 내용 상세 표시
- 기존 대기 (미반영) → 제목 + 한 줄만

### 대기 형식
[업데이트 대기 #N]
내용: [추가/수정할 내용]
대상 파일: [어느 파일]
근거: [왜 그 파일인지]
우선순위: 높음 / 보통 / 낮음

## 목차06 URL 참조 규칙
문서 내 모든 URL은 JinGwak-Cal 기준으로 유지한다.
jingwak-maker URL 사용 금지.
올바른 URL 형식:
raw: https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/[파일명]
blob: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/[파일명]

## 목차07 적용 시점
Jin님 승인 후 일괄 반영 (소소한 사항은 모아서)

# ── current-step.md ──────────────────────────────────────

# 현재 작업 단계

---

## 구조1 전체 로드맵

출시까지 전체 단계:
1. 문서 체계 정비 ← 진행 중
2. Premium Phase 잔여 작업 (2-8 → 2-5 → 2-6)
3. 상태유급형(주휴·연차) 정리
4. 시간속성 수당 UI 정리
5. UI 통일
6. 검증
7. 출시 준비

---

## 구조2 현재 단계 ← 현재

현재 단계: STEP 4 — UI 인벤토리 작성 (★실질적 UI 설계 시작점) — 완료
다음 단계: STEP 5 — ResultGrid 중심 재설계 검토 및 UI 체계 후속 정리
비고:
- STEP4 결과: Inventory 22건 + Source Gap 4건, UI-Audit(01) §1~9 전수 매핑 완료
- UI-Audit(01~04) 원본 수정 없음 (인벤토리는 별도 산출물로 보존)
- ResultGrid(RESULT-01~05) Lifecycle=Redesign 표시만, 재설계는 STEP5 이후
- RESULT-03 Component(Card/Row) 분류 검토사항 → STEP5 ResultGrid 재설계 시 시나리오 A/B 재검토 (산출물 §5 참조)

---

## 구조2-A 현재 STEP 필요 문서 (Required Documents)

※ 구조는 확정되었으나 UI-Audit 문서는 아직 repo URL 등록 전 상태. URL 확보 후 즉시 갱신.
※ 현재 STEP 수행에 필수인 문서만 기재. 참고문서·선택문서는 포함하지 않음.

| 문서ID | raw | blob | 상태 | 용도 |
|--------|-----|------|------|------|
| UI-Audit-01 | TBD | TBD | URL 등록 대기 | 9개 영역 전수조사 원본 |
| UI-Audit-05 | TBD | TBD | URL 등록 대기 | 4축·C안·색상3층 정본 |
| UI-Audit-06 | TBD | TBD | URL 등록 대기 | X-5/X-6 절차 정본 |

STEP 전환 시 본 표를 해당 STEP 기준으로 갱신.
표에 없거나 URL 미기재 시 → 사용자에게 1회 요청 후 진행.

---

## 구조3 다음 작업

1. current-step.md 개정 완료 및 archive/current-step-retired.md 생성
2. index.md 개편
3. merged-context 재생성 확인
4. 신규 쓰레드 진입 테스트

---

## 구조4 대기

### 앱개발 대기
※ 2-5/2-6은 고위험 모델 작업이므로 2-8 이후 순서 유지
- Phase 2-8: 인라인 제거 확인 및 잔여 정리
- Phase 2-5: 근무내역 단위 (고위험 — 별도 설계 보고 후)
- Phase 2-6: 조합 자동 해석 (2-5 확정 후)

### 워크플로우 단기
- GitHub Actions 동작 검증 완료 확인 ⏳
- 자동 병합 스크립트 개선

### 워크플로우 중기
- 중앙 Context Builder 구축
- LLM 결과 자동 검증 체계 구축

---

## 구조5 보류

현재 없음

---

## 구조6 완료요약

### 앱개발 완료
- Premium Phase 완료 (Phase 2-1~2-4, 2-7)
- BUG-1 History reload 복원 ✅
- floor 정책 확정 ✅

### 워크플로우 완료
- 문제 진단: 최신 문서 LLM 자동 주입 부재 확인
- Fine-grained 토큰 3개 발급 및 Replit Secrets 저장
- GitHub App (Jin-Docs-Automation) 구축 완료
- GitHub Actions 구축 완료

### 문서 체계 개편 완료
- absolute-rules.md 구조 전면 개편 (v14.0 / 0612) ✅
- decisions.md 구조 개편 (D-01~D-04) ✅
- archive 구조 일부 구축 완료 ✅
- merged-context 자동 재생성 확인 ✅

### UI 인벤토리 완료
- STEP4 UI Inventory 작성 완료 (Inventory 22건 + Source Gap 4건)
- UI-Audit(01) §1~9 전수 매핑 확인, 누락 없음
- RESULT-03 Component 분류(Card/Row) 검토사항 → STEP5 ResultGrid 재설계 시 재검토 (산출물 §5 참조)
- 산출물: UI-Inventory-STEP4-22건.md

상세: archive/current-step-retired.md 참조

# ── decisions.md ──────────────────────────────────────

# 파트너 협의 결정사항

---

## D-01 앱 정책

### D-01-01 맞춤가산 정체성 — 확정 (2606031200)
- 맞춤가산 = 가산분 (법정가산의 커스텀 버전)
- 5인 미만 사업장에서 맞춤가산도 0 처리 (표준가산과 동일 게이팅)
- 맞춤가산 계산: 각 행별 hours × wage × rate 후 Math.floor() 1회, 행별 결과 합산
- 맞춤가산 저장 원칙: floor된 금액이 아닌 원본 입력값(hours/rate/선택정보) 기준으로 저장·복원. customPay는 항상 재계산되는 파생값으로만 취급

### D-01-02 맞춤가산 정체성 — 향후 확장 방향
- 위험수당/약정수당 등 별도수당 필요 발생 시 → 별도 기능으로 추가 (맞춤가산과 분리)

### D-01-03 R1 결합가산 처리 — 확정 (2606031200)
- 표준가산(연장/야간/휴일)은 0.5 고정
- 표준가산으로 표현되지 않는 특수 가산율은 맞춤가산으로 처리
- 이중/삼중은 UI상 결합 입력, 내부에서는 선택된 수당 각각 같은 시간으로 분해
- 표준가산은 각 0.5 고정 (연장+야간 = 1.0 / 연장+야간+휴일 = 1.5)
- 5인미만 ON 시 A 게이팅에 의해 자동 0 처리
- 표준가산 진실원천 = 시스템 A (실수령 반영 경로)
- B(Premium)는 계산 진실원천이 아닌 입력 UI / 제거 대상
- UI 프리셋: ResultGrid의 0.5/1.0/1.5 버튼 제거 → "표준가산 50% 고정 · 특수율은 맞춤가산 사용" 정적 안내로 대체 (커밋 a3f4e0d)

### D-01-04 R1 결합가산 처리 — floor 정책 확정
- Premium 가산 row별 최종값에 Math.floor() 1회 적용 후 합산
- 적용 범위: Premium 단일/이중/삼중/맞춤 row에만
- 기본급/주휴/연차/세금·공제는 기존 계산 방식 유지

### D-01-05 R1 결합가산 처리 — state 처리
- nightPremiumRate·overtimePremiumRate·holidayPremiumRate state 유지 (UI만 고정)
- 저장/복원 구조 무변경

### D-01-06 기존 잠복 버그 — 주의
- 맞춤가산 state를 CalcState에 편입할 때 복원부(Home :206–233)에 맞춤 키 명시 추가 필수
- 미추가 시 동일 버그 재현됨
- 수정 완료 이력: archive/decisions-retired.md 참조

---

## D-02 작업 순서

### D-02-01 재확정된 작업 순서 (2606041200)
1. 2-7 화면 분리 (저위험 — PremiumSection 무상태 구조) ✅
2. 2-8 인라인 제거 (2-7 완료 후)
3. 2-5 근무내역 단위 (고위험 — 별도 설계 보고 후 진행)
   → customPremiumRows 영속·계산·history reload 연쇄 영향
4. 2-6 조합 자동 해석 (2-5 확정 후)
   → 자동요율 vs STEP2 수동입력 우선순위 정책 결정 선행 필요

### D-02-02 근거
- PremiumSection 무상태(presentational) 구조 확인
- 2-5 모델 변경은 customPremiumRows/저장복원/계산공식/history reload 동시 영향 고위험
- 저위험 작업으로 표면 정리 후 고위험 진행

---

## D-03 워크플로우 정책

### D-03-01 중기 과제
- 중앙 Context Builder 구축
- LLM 결과 자동 검증 체계 구축

### D-03-02 토큰·GitHub 운영 정책 (통합: B-D-03-05 + B-D-03-09)
<!-- B-D-03-10 Replit 운영 규칙: decisions → absolute-rules 구조5 목차03
     "GitHub 및 토큰 운영 (§운영6+7+Replit)"에 이동+통합 완료 (T+M)
     현행 규칙 위치: absolute-rules.md 구조5-목차03 -->
- Replit Secrets에 3개 토큰 저장 완료
  → GITHUB_APP_TOKEN
  → GITHUB_DOCS_READ_TOKEN
  → GITHUB_DOCS_WRITE_TOKEN
- main 직접 푸시 금지 / PR 필수 / Jin님 승인 후 병합
- payroll-calculator-docs 수정은 Jin님 승인 및 PR 절차를 통해서만 허용
- 대화창 토큰 노출 원칙적으로 지양

### D-03-03 문서 체계 확정 (2606051200)
- Source of Truth = absolute-rules / current-step / decisions
- merged-context.md = 파생/캐시 문서 (Source of Truth 아님)
- merged-context 충돌 시 원본 문서 우선
- index.md = 안내/진입점 역할만 (Source of Truth 아님)
- manual-v14 = archive 이동 금지 / 우선순위 하향 유지
- archive/ = 과거 기록 보관용 / 현재 판단 근거 사용 금지

### D-03-04 GPT 표준 컨텍스트 확정 (2606051200)
- GPT raw/jsdelivr/blob URL 접근 반복 실패 확인
- GPT 표준 진입 방식 = merged-context.md
- merged-context.md도 URL 읽기 실패 가능성 있음
- 최후 수단 = Jin님 직접 복붙
- GitHub Actions는 GPT 읽기 문제 해결책 아님
  → 문서 동기화·검증·자동화 인프라 역할

### D-03-05 GitHub Actions 도입 근거 (2606051200)
<!-- B-D-03-11: 문서 책임 정의 → absolute-rules 구조6으로 이동 완료 (SoT=Y 유지) -->
<!-- 현행 규칙 위치: absolute-rules.md 구조6-목차01 문서 역할 정의 -->
<!-- B-D-03-08: archive 아닌 K 유지 — "왜 Actions를 도입했는가"의 결정 근거 -->
- 협업 자동화 관점에서 높은 우선순위
- 역할: merged-context 자동 생성 / index 검증 / 불일치 경고
- GPT 읽기 문제와 별개로 문서 동기화·자동화 인프라 역할
- 구축 완료 이력: archive/decisions-retired.md 참조

---

## D-04 문서 체계 개편 결정 (0612)

### D-04-01 식별자 체계 도입 이유
- 문서 개편 시 Before/After 항목 추적 불가 문제 해결
- 상태-문서-구조-목차-서브목차 형식으로 이동 경로 명확화
- 예: B-A-02-03-S01 → A-A-02-02-S03 (어디서 어디로 갔는지 즉시 파악)

### D-04-02 sot 판정 기준 도입 이유
- 통합(M) 시 흡수된 항목이 현행 규칙인지 아닌지 판단 기준 부재 문제 해결
- "형식(독립 목차)이 사라져도 내용이 현행 규칙에 존재하면 현행 유지"
- sot=y/n으로 단순화하여 파트너 간 혼선 방지

### D-04-03 복수분류 허용 이유
- 문서 개편에서 이동+통합, 이동+개정 등이 동시 발생하는 현실 반영
- 단일 분류 강제 시 정보 손실 발생 (예: T만 표기 시 통합 사실 소실)
- 최대 2개 조합, 앞=현재처리/뒤=이후처리 순서 규칙으로 혼선 방지

### D-04-04 archive 분리 이유
- 폐기/구버전 항목이 현행 문서에 남아 파트너 혼선 유발
- sot와 archive를 독립 판정하여 "이동했지만 현행 유지(sot=y, archive=n)"와
  "폐기됐지만 기록 보존(sot=n, archive=y)" 구분

### D-04-05 SoT 3문서 체계 확정 이유
- merged-context는 파생본이므로 SoT로 삼으면 원본 훼손 시 판단 기준 소실
- index는 안내 역할이므로 규칙 저장 위치로 부적합
- absolute-rules / current-step / decisions 3문서만 SoT로 확정하여 단일 진실원천 유지

---

## UI-Audit 검증 결과 확정 (2606.13)
1. 4축 체계 채택 — Type·Component·Feature·Layer
2. C안 채택 — Interaction은 Type 흡수 / Signature·Notes 독립 유지
3. 색상 3층 확정 — Brand=Blue-Gray / Accent=Indigo / Semantic=Emerald·Red·Amber
4. 제거 우선 원칙 채택 (실행 절차는 UI-Audit(05) X-6 참조)
5. 단일 주인공 원칙 — 화면당 Primary 1개
6. 콘텐츠 우선 원칙 — 장식보다 숫자·내용·결과 우선
7. 여백은 구조 — Spacing 우선, Divider·Border·Card 후순위
8. 벤치마킹 목적 재정의 — 분류체계 검증·제거기준 확보·토큰값 참조 (예쁜 UI 탐색 아님)
9. 토큰값 조사 참조원 및 우선순위 확정 — Apple HIG → Apple Wallet → Toss → KakaoBank
   · Apple Wallet은 제거우선(X-5)·단순화절차(X-6) 검증용 핵심 참조원
   (상세 근거: UI-Audit 05·06)
