<!-- Auto-generated at 2026-07-05T20:22:48Z -->
<!-- Source: absolute-rules.md + current-step.md + decisions.md -->
<!-- index.md 는 이 파일의 생성 대상이 아닙니다 -->

# ── absolute-rules.md ──────────────────────────────────────

# absolute-rules.md vNext
# 개정 기준: 0611~0612 문서 체계 개편
# Before 기준: GitHub origin/main 238줄
# After 구조: v1.1 확정안

---

# 구조0 작업환경

## 도구 및 역할
- Claude: 문서 검토·산출물 작성·설계 판단 (주 파트너)
- Replit Agent: 앱 코드 실행·수정·GitHub push
- GPT: 검토 파트너 (새 쓰레드 진입 시 merged-context 기준)
- Manus: 막힌 문제 대안 탐색 용도 (Claude/GPT 모두 막혔을 때, 병목 돌파용)
  결정권 없음. 최종 판단은 SoT 문서 기준. 구현 담당 아님.
- VS Code: 직접 코드 편집
- GitHub: 문서 repo(JinGwak-Cal/payroll-calculator-docs) + 앱 repo

## 환경별 접근 원칙
- Claude → GitHub: bash_tool로 git fetch/checkout (읽기만)
- Replit → GitHub: REST API + WRITE 토큰 (읽기+쓰기)
- GPT → GitHub: raw URL 우선 사용 (읽기 전용)
- Manus → 작업환경 컨텍스트 전달 후 대안 요청 (읽기+판단만)
- main 직접 push 금지 — 모든 도구 공통

### 조작 안내 원칙 (2026-07-03, 근거: notes/evidence-log.md E-002)

- 조작 방법(UI/CLI)을 제안하기 전에 현재 상태(Context)를 먼저 확인한다.
- 반복 실패 시 즉시 재시도하지 않고 Diagnosis Gate를 거친다:
  Context 재확인 → Root Cause 규명 → 대안을 기회비용 기준으로 비교 →
  성공 경험 있는 방법 우선 → 없으면 R8~R17(전체 출력 금지) 원칙 따름

## 3문서 역할 분리 원칙
- absolute-rules.md = 분류 기준·운영 규칙 (상위 규칙)
- manual-v14.md = 항목별 상세 이력 보관
- current-step.md = 현재 추적 목록 요약 (대기·검토대기 항목)
※ 검토대기 항목은 manual-v14(상세)와 current-step(요약) 양쪽에 동시 유지.
  current-step에서만 제거하면 추적 누락 위험 발생.

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
R7. 대형 파일 교체 시 전체 파일이 아니라 변경분만 별도로 전달하고
    "끝에 append" 또는 "이 구간을 이 내용으로 교체" 방식으로 지시한다.
R8. Replit에 파일 요청 시 파일 전체를 채팅창에 출력하는 방식 금지.
    다운로드 링크 또는 grep/구간 지정(예: "200~250행만")으로 대체.
R9. 대형 파일에 대해 전체 cat 금지. grep → 구간 조회 우선.
    여러 bash 명령은 &&로 묶어 호출 횟수 최소화.
R10. GPT 진입 시 기본은 merged-context 1개 URL만 전달.
     예외: review 파일이 별도로 필요한 경우에만 추가 전달.
R11. 문서 변경 시 전체 문서 재출력 금지 — 변경분만 제시.
     수정본 전체 출력은 토큰 낭비의 주요 원인.
R12. 코드 검토 시 파일 전체 출력 금지 —
     변경 함수·변경 블록 단위로만 출력.
R13. 업데이트 대기 항목은 반드시 구분:
     - 정식 업데이트 대기: 구현 방향 확정됨 → current-step 작업확정에 등록
     - 누락방지용 기록: 판단 보류 또는 실존 확인 필요 → current-step 검토대기에 등록
     두 분류를 혼용하면 우선순위 판단이 불가능해짐.
R14. 검토대기 항목은 current-step에서 제거하더라도
     manual-v14 분류 이력에는 반드시 잔존해야 한다.

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

## 목차08 항목 분류 판정 기준

### 상태 분류
- 완료: 구현·검증까지 끝나 더 이상 추적 불필요
- 완료(대체): 원래 목적이 다른 방식으로 달성되어 재구현 불필요 (재오픈 조건 명시 필수)
- 승계: 다른 STEP/문서로 추적 주체가 이전됨 (원 출처에서는 종결)
- 작업확정: 무엇을 할지 결정됐고 구현만 남음
- 검토대기: 코드 확인·정책 결정 등 판단이 끝나지 않아 완료/폐기 어느 쪽도 단정 불가
- 폐기: 현재 구조와 더 이상 양립 불가하여 추적 종료

### 태그 분류 (상태와 별도, 중복 가능)
Feature / Bug / Design / Docs / TechDebt / KnownIssue / UX / Verification

### 항목 기록 형식 (8필드)
상태 / 태그 / 배경 / 이용자필요 / 목표 / 처리방침 / 구현순서 / 판정

### 검토대기 처리 원칙
- 코드 확인 전 임의로 완료/폐기 판정 금지
- 문서 내부에 상충 기록이 있으면 검토대기로 우선 분류

R15. 토큰 절약 검토 의무 — 아래 작업 전 반드시 수행:
- 문서 개정 (decisions/current-step/manual-v14/absolute-rules)
- Replit Agent 프롬프트 작성
- 첨부파일 작업
- 대형 파일 작업 (권장 기준: 300줄 이상 또는 20KB 이상)
- 신규 프로세스 설계

```
 검토는 작업 전에 수행. 작업 완료 후 사후 설명으로 대체 불가.

 작업 전 보고 형식:

 [토큰 절약 검토]

 1-1 검토유무:
 1-2 검토방법:
 1-3 예상 성과:
     - 작업 전 예상 전달량: (파일명, 줄 수)
     - 적용 방식:
     - 예상 절감:

 작업 완료 후 보고 형식:

 [토큰 절약 결과]

 - 실제 전달량:
 - 실제 절감:
```

R16. 토큰 절약 검토 결과가 없으면 문서 작업 프롬프트 승인 금지.
검토 결과 없이 제출된 프롬프트는 반드시 검토 먼저 요청.

R17. 프롬프트 수정 시 전체 재출력 금지.
변경 위치와 변경 내용만 제시한다.

```
 형식:
 - "X번 항목 Y부분을 Z로 교체"
 - "N번째 문단 삭제"
 - "A항목 뒤에 B 추가"

 최초 작성 시 또는 최종 확정 시에만 전체 출력 허용.
 승인 대기 중인 프롬프트 수정은 변경분만 제시한다.
```

---

## 제품 철학

Paycheck Workbook은 수당근무를 관리하여
제수당을 자가 검산하는 급여관리 도구이다.

---

## 공통 설계 원칙

공통 설계 원칙은 모든 제품 설계에 우선 적용한다.

· 기능보다 제품 철학과 제품 정의를 먼저 확정한다
· 사용자의 가장 큰 관심이 화면의 Primary가 된다
· 관리 대상과 계산 결과를 구분한다
· 화면 구조(Flow)와 화면 배치(Layout)를 구분한다
· Form보다 Table을 우선 검토한다
· 모든 설계 제안은 개념 설명으로 끝나지 않는다.
  가능한 경우 텍스트 UI 또는 와이어프레임까지 함께 제안한다.

---

## 협업 응답 원칙

### 검토·리뷰 답변 형식
검토·리뷰 성격의 답변은 반드시 아래 순서를 따른다.
① 결론 (승인 / 조건부 승인 / 변경 / 반대)
② 조건
③ 근거
④ 세부 설명

---

## 프롬프트 작성 전 검증 체크리스트

프롬프트 초안 작성 전 반드시 확인한다.
적용 대상: Replit Agent / Claude / GPT 공통

□ 범위 — 하위 디렉터리 포함 여부 명시
□ 출력 형식 — 명시 여부
□ 출력 제한 — 코드/파일 내용 출력 금지 명시
□ 금지 동작 — 수정/실행 금지 등 읽기 전용 조건

---

## Thread Closing Review

쓰레드 마무리 직전 반드시 수행한다.

□ 새로 확정된 Decision이 있는가?
□ absolute-rules에 들어갈 공통 원칙이 있는가?
□ current-step에 반영할 작업이 있는가?
□ 다음 프로젝트에서도 재사용할 방법론이 있는가?

---

## 설계 원칙 — User Intent 우선

설계가 막히면 먼저 정의한다:
"사용자는 지금 무엇을 하려는가?"

이 질문을 기준으로
Behavior → Information → Presentation을 설계한다.

---

## Release 절대 원칙

- 모든 변경은 `ai/draft` 브랜치를 통해서만 Release한다.
- `main` 직접 수정은 허용하지 않는다.
- Release는 Release Gate 승인 이후에만 수행한다.
- Release 후에는 `merged-context.md`를 기준으로 다음 작업을 시작한다.
- Release Gate 승인 전에 SHA가 변경된 경우, 반드시 재검토 후 재승인한다.

# ── current-step.md ──────────────────────────────────────

# 현재 작업 단계

업데이트: 2026-07-06

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

**Infrastructure Priority (신규, 최우선)**

BR-001 (Bridge Day-1 MVP 구현)

- 결정 완료: `decisions.md` D-BR-001 (2026-07-06)
- 범위: Question 생성/추적, Bridge ID, Sub ID(question_id+sub_no), Current/Next Partner, Comment, Edit, Dispatch, Question 분류(New/Follow-up/Branch)
- 제외: Git Verification, Approval Console, Dashboard, Capability 추상화, History, Persistence 등 (D-BR-001-03 참조)
- Trigger: Stage 0 Bridge Architecture 결정 (notes/direction-hypothesis.md) 후속

**Operational Priority**
TOP-001 (Token Optimization Protocol / OCE 첫 번째 프로토콜)
- Part 0~10 구조 설계 후 작성
- Trigger: Thread Start (DF-00021)

**Engineering Priority**
ER-001 (Environment Reconstruction)
- DS-001 + DS-002 기반 GPT 독립 수행
- Trigger: TOP-001 완료 후 (DF-00002)

---

## 구조3 — 다음 작업

```text
새 쓰레드 시작 시:

1. merged-context.md 읽기 검증
2. BR-001 Bridge Day-1 MVP 구현 착수 (D-BR-001 스코프 기준)
   - 구현 환경 결정 (Replit / VS Code 등) 부터
3. TOP-001 작성 착수
4. ER-001은 TOP-001 완료 후
```

---

## 구조4 — Deferred 요약 (13건)

| Category | Count | 대표 항목 |
|---|---|---|
| Next Sprint | 4 | TOP-001, ER-001, GPT 프롬프트, document 10 |
| Research | 4 | RN-001B 완성, TP-002, TAP, DHM |
| Future | 4 | C-00002/003/039/041 카드화 |
| Long-term | 1 | manual-v14 이관 |

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

---

## D-05 UI 재설계 확정 (2606.15)

### D-05-01 ResultGrid 역할 재정의 — 확정 (2606.15)
- ResultGrid = 결과 표시판 + 입력 진입점
- 가산수당 영역 터치 → 하단 Drawer(Bottom Sheet) 열림
- 실수령액·총급여·기본급·주휴·공제 → 입력 진입 불가 (표시 전용)

### D-05-02 RESULT-04/05 처리 — 확정 (2606.15)
- RESULT-04: 체크박스 방식 제거 확정 / 대체 ON/OFF 방식은 STEP6+ 보류
- RESULT-05: 인라인 펼침 입력 UI 제거 확정 → Drawer로 이전

### D-05-03 Drawer 구조 — 확정 (2606.15)
- 위치: 항상 하단 고정 (Bottom Sheet)
- 칩 구성: [연장][야간][휴일][완료] 한 줄
  - 완료 전: 비선택 칩 유지 / 완료 후: 비선택 칩 제거
- 입력 흐름: 수당 선택 → 시간 입력(스테퍼+키패드) → 가산율 안내 → 즉시 결과
- 재탭 편집: 기존 값을 유지한 채 편집모드 복귀 (수정 가능 범위는 STEP6+ 확정)
- 추가 버튼: [다른 수당 추가]
- 행 철학: 행 = 근무상황 1건 (수당 총합 입력기 아님)

### D-05-04 가산수당 저장 단위 — 확정 (2606.15)
- 저장 단위: `id + selectedAllowances + premiumRate + premiumHours`
- 저장 금지: `premiumAmount / premiumType / mode / allowanceCombo` (파생값)
- 표준/맞춤 판정: `isStandard = premiumRate === selectedAllowances.length * 50`
  - 절대값 기준 금지: 동일 값이 수당 수에 따라 표준/맞춤 달라지기 때문
- 동일 수당 + 다른 rate = MVP 금지 (A안 확정)
- 맞춤가산 MVP 범위: 단일 수당만 허용

### D-05-05 mapEntriesToCalcInput() — STEP6-2-2 기준 A안 확정 (2606.15)
- 표준가산: 각 수당별 rate=0.5 고정 분배, premiumRate는 isStandard 판정용만 사용
- 맞춤가산(단일): rate = premiumRate / 100
- 시간 합산: 동일 수당 여러 행은 hours 누적 합산
- 근거: calc-engine은 조합 엔진 아님 — night/overtime/holiday 독립 계산 후 합산 구조

### D-05-06 SinglePremiumCard.tsx — 처리 방향 확정 (2606.15)
- Removing 후보 (미사용 dead component)
- 즉시 삭제 아님 — 별도 코드 작업 시 제거

### D-05-07 History 저장 구조 — 확정 (2606.18)
- allowanceRows는 HistoryEntry.inputs 내부에 추가
- HistoryEntry 최상위 필드 추가 금지
- 저장값: PremiumAllowanceEntry[] 원본 입력값만 허용
- 저장 금지: premiumAmount · premiumType · mode · allowanceCombo
- 즐겨찾기/삭제 로직과 충돌 없음
- 구현 전 타입 신설(PremiumAllowanceEntry) 및 복원 검증 함수 필요

### D-05-08 근무지합산 알고리즘 — 확정 (2606.18)
- mapEntriesToCalcInput()에서 동일 수당 hours 누적 합산 후 각 필드 분배
- 표준가산: 각 수당 필드 / 맞춤가산: customPay 필드 — 독립 합산
- 5인 미만 게이팅: calc-engine 내부 아님 — 변환 계층에서 isSmallBiz 참조하여 가산분 0 처리
- 5인 미만 토글 = 연장·야간·휴일 가산분만 제거 (주휴·연차 유지)
- 엔진 수정 없이 구현 가능

### D-05-09 Drawer/allowanceRows 최소구현명세 — 확정 (2606.18)
- 입력 진입점 단일화: "가산수당 설정" 버튼 제거, PremiumScreen MVP 병존 안 함, 단일 진입점=ResultGrid→Drawer
- PremiumScreen/CustomPremiumCard/usePremium은 흡수→참조 제거 확인→삭제 순서로 처리 (선삭제 금지)
- 흡수 대상: 칩 선택 토글 / rate·hours 입력 핸들러 / 완료 조건 판정 / 금액 계산 로직(floor 1회)
- 흡수 안 함: 고정 3행 visible/hidden 구조, resetCustomRows, screen="premium" 라우팅
- PremiumAllowanceEntry 타입 확정: id + selectedAllowances + premiumRate + premiumHours
- isStandard는 저장하지 않고 계산 시 파생 (판정식: premiumRate === selectedAllowances.length * 50)
- ResultGrid Row는 기존 표시 포맷 유지 (체크박스만 제거, 표시 형식 변경 없음)
- 5인 미만 게이팅은 변환 계층에서 처리, 연장·야간·휴일 가산분만 0 처리
- 기존 History의 customPremiumRows는 allowanceRows로 변환 가능해야 하며, 신규 저장은 allowanceRows 기준

### D-05-10 premiumHours 의미 확정 — 급여기간 총 가산시간 (2606.19)
- premiumHours는 연장·야간·휴일 모두 급여기간 기준 총 가산시간으로 해석한다. 1일 기준(per-day) 값이 아니다.
- 연장은 총시간을 그대로 전달한다.
- 야간/휴일은 calc-engine 내부 구조로 인해 변환 계층에서 역산·보정 후 전달하지만, 최종 계산 결과는 입력된 총 가산시간 기준과 동일해야 한다.
- 근무일수를 곱하는 처리(nightHoursPerDay/holidayHoursPerDay류 직접 매핑)는 사용하지 않는다.
- 부동소수점으로 인한 언더슈팅(floor 1원 손실)은 변환 계층에서 극소 보정 처리한다.
- premiumHours의 의미는 입력 모드(uniform / timerange / 2×2 확장모드)에 의해 변경되지 않는다.
- 근거:
  - STEP5-4 §3-3: 입력 즉시 그 시간에 대한 금액만 표시(곱셈 언급 없음)
  - 사용자는 "이번 달 야간 몇 시간 했는지"는 알아도 내부 1일 기준 개념은 모름
  - 2×2 확장모드(요일별 다른 근무시간)에서도 총시간 입력은 모드 독립적으로 동일 작동
  - 입력값의 정확성=사용자 책임 / 계산의 정확성=앱 책임, 단 앱은 입력 의미를 정확히 안내할 책임이 있음
- 변환 계층(custom-premium.ts/use-calc.tsx)에서만 처리, calc-engine.ts(calculate) 미수정 원칙 유지
- Drawer 시간 입력 단계에 안내문구 표시: "가산시간은 급여기간 전체 기준으로 입력합니다. (1일 기준이 아닙니다.)"

### D-05-11 timerange 모드 야간 우선순위 확정 (2606.19)
- timerange(출퇴근시간) 모드에서도 allowanceRows에 야간 입력이 있으면, 엔진의 자동 야간 산출값보다 Drawer 입력을 우선 반영한다(A안).
- 근거: allowanceRows 활성 시 Drawer 입력이 SoT — 사용자의 명시적 의사가 엔진의 자동 추정보다 우선해야 한다는 원칙(D-05-10)에 따름.
- 구현: 변환 계층에서 inputMode를 "direct"로 전환해 엔진의 timerange 자동 야간 분기를 우회. 기본급/주휴/연차 등 base 계산에는 영향 없음(duration이 이미 hoursPerDay에 반영되어 패턴 동일).
- calc-engine.ts(calculate) 미수정 원칙 유지.

### D-05-12 STEP6-2 구현 완료 (2606.19)

* 가산수당 입력 체계(Drawer/allowanceRows) 구현 완료, 1/5~5/5 전 단계 검증 통과
* calc-engine.ts(calculate)는 구현 기간 전체 동안 미수정 유지
* 변환 계층(custom-premium.ts / use-calc.tsx)에서만 처리 원칙 유지
* dead component 정리 완료:
  PremiumScreen / PremiumSection / CustomPremiumCard 삭제, usePremium 훅 제거
* use-premium.tsx는 공용 타입 모듈로 축소 유지
  (AllowanceType / CustomPremiumRow / PremiumAllowanceEntry / initialCustomPremiumRows)
* History 저장/복원 연결 완료
* legacy customPremiumRows 기록은 allowanceRows로 변환 후 정상 복원
* SinglePremiumCard / DoublePremiumCard / TriplePremiumCard는 범위 외로 유지
* 후속 보류 이슈: use-calc.tsx Fast Refresh 비호환 — dev HMR 중 일시적 null context 오류 가능. 프로덜션 영향 없음. 필요 시 별도 리팩토링 task로 분리.

### D-05-13 토큰 절약 검토 절차 확정 (2606.22)

* 문서 작업, Replit Agent 프롬프트 작성, 대형 파일 작업(권장 기준: 300줄 이상 또는 20KB 이상), 신규 프로세스 설계 시 반드시 토큰 절약 검토를 수행한다.

* 토큰 절약 검토는 실제 작업 전에 수행하며, 작업 완료 후 사후 설명으로 대체할 수 없다.

* 프롬프트 수정 시에는 R17을 적용하며, 승인 대기 중인 프롬프트는 변경분만 제시한다.

* 작업 전 검토 형식:

  [토큰 절약 검토]

  1-1 검토유무:
  1-2 검토방법:
  1-3 예상 성과:
  - 작업 전 예상 전달량: (파일명, 줄 수)
  - 적용 방식: (append/변경분 삽입/구간 지정 등)
  - 예상 절감: (줄 수 또는 파일 수)

* 작업 완료 후 보고 형식:

  [토큰 절약 결과]

  * 실제 전달량: (줄 수)
  * 실제 절감: (줄 수)

* 일반 질의응답에는 적용하지 않는다.

* 토큰 절약 검토 결과가 없으면 문서 작업 프롬프트 승인 금지.

### D-05-14 Replit Agent 협업 재발방지 원칙 (2606.25)

* 작업환경 모델 고정
  · Replit Agent 환경에서 Shell/bash/git clone 직접 실행 제안 금지
  · 확정된 협업 구조(Claude=설계, Agent=실행) 임의 변경 금지
  · 작업환경 모델을 잃었을 때 즉시 merged-context 재확인

* 최소 정보 요청 원칙
  · 파일명 → 경로 → 구간 → tar.gz → 전체 순서 준수
  · 단계 건너뛰기 금지 / 전체 파일 출력은 최후수단

* Replit Agent 실패 종료 규칙
  · 모든 조회 프롬프트에 실패 종료 조건 포함
  · "30초 내 응답 없으면 '실패'만 출력"
  · "파일이 없으면 '파일 없음'만 출력"

* 구현 단계 진실원천 우선순위
  · Replit 워킹트리 > GitHub
  · 원인 추측 전 워킹트리 코드 확인

* 설계 범위 확대 금지
  · 현재 STEP 범위만 구현
  · 새 UI/컴포넌트/구조 추가는 다음 STEP으로 분리

* 승인 판정 규칙
  · 첫 줄에 반드시 판정 명시: 승인 / 조건부 승인 / 보완 필요 / 반려
  · 조건부 승인 시 첫 줄에 반드시 "조건부 승인"으로 시작 (승인으로 시작 후 조건 붙이기 금지)
  · "좋습니다. 다만..." 형식 금지

* 추측보다 검증 우선
  · 최종 판정은 실제 build/tsc/lint 결과 기준

* 복붙 우선 원칙
  · 사용자가 "변경분만"을 요구하지 않는 이상, 수정사항이 반영된 복붙 가능한 최종본을 먼저 제시하고, 변경 설명은 그 다음에 제시한다.

* 대기 규칙
  · 대기 등록 후 사용자 지시 전까지 새 제안 시작 금지
  · 공식 문서 반영 전이라도 즉시 준수

* 기존 컴포넌트 재사용 전 확인 규칙
  · 기존 컴포넌트/훅/유트 재사용 가능 여부를 먼저 조사
  · import 확인 → 중첩 확인 → 구현 순서 준수

* 협업 자세 원칙
  · 사용자의 토큰 비용, 클릭 수, 복붙 횟수를 실제 작업 비용으로 간주
  · AI가 편한 방식보다 사용자의 작업환경에서 덝 번거로운 방식을 우선
  · 프롬프트 초안은 한 번에 실행 가능한 품질을 목표로 작성
  · 사용자가 뻔히 요구할 보완은 선제 반영
  · 같은 유형의 실수를 반복하지 않도록 체크리스트를 재점검

* 토큰 비용 안내
  · 토큰 소모량이 불필요한 경우를 제외하고, 질문 또는 제안 시 예상 토큰 소모량을 함께 언급

* Replit 프롬프트 작성 체크리스트
  · 범위 최소화 / 하위 경로 명시 / 출력 형식 지정 / 출력 금지 명시
  · 수정 금지 명시 / 실패 종료 조건 포함 / 토큰 절약 순서 준수
  · 현재 STEP 범위 확인 / 기존 컴포넌트/훅/유트 재사용 여부 조사
  · import 중복·중첩 확인 / 복붙 가능한 최종본 제시 / 첫 줄 판정 명시

### D-05-15 수당근무 내역 UX 최종 확정안 (2606.25)

* 2줄 표준 형식 (공통 UI 규격)
  · 1줄: 번호(displayNo) + 메몤 (식별자, 고정)
  · 2줄: 입력 시각(createdAt) · 적용수당 · 가산율
  · 목록 / 선택 Sheet / 비교편집 / 요약 카드 모두 동일 형식 적용
  · 예시

    #01  토요일 특근
    06-25 14:30 · 연장·야간 · 150%

* 삭제 Placeholder 확정
  · 기본: ▶ #02
  · 클릭: ▼ #02 (이용자 삭제)
  · 재클릭: ▶ #02
  · 번호 재정렯 없음. 설명/시각/카드 없음.

* 식별자 고정 원칙
  · displayNo / 메몤 / createdAt = 수정해도 변하지 않음
  · 수정 가능한 것: 적용수당 / 가산율만

* 비교편집 UX 방향 확정
  · MVP를 먼저 구현하여 현재 STEP 범위를 유지하고, 3단 비교편집은 후속 STEP으로 분리한다.
  · MVP (저비용): Drawer 상단 기존 입력 요약 카드만 추가
    - 읽기전용 카드 1개 / 실시간 diff 없음 / 기존 Drawer 구조 유지
  · 풀 구현 (후순위): 3단 비교편집 구조
    - 기존 입력 / 수정 입력 / 예상 수정 실시간 동기화
    - 구현 비용: AllowanceDrawer 150~200줄 영향 / state 3~5개 추가
    - STEP 5 이후로 보류

* 구현 원칙
  · 기존 컴포넌트 우선 재사용
  · 최소 증분 구현
  · 현재 STEP 범위를 넘는 UI 확장 금지


---

## D-PW-000 제품 철학 확정 (2606.26)

Paycheck Workbook은 수당근무를 관리하여 제수당을 자가 검산하는 급여관리 도구이다.

이 한 문장이 모든 기능 추가, UI 변경, 우선순위 판단의 기준점이 된다.

---

## D-PW-001 프로젝트 전환 확정 (2606.26)

Paycheck Workbook은 Payroll Calculator에서 파생된 독립 제품이다.

- 계산엔진 / 협업 시스템 / 개발 철학 계승
- 제품 철학과 UI는 독립적으로 발전
- 기존 Repository 유지, paycheck-workbook 브랜치로 개발
- 새 Repository 생성하지 않음
- main은 Payroll Calculator 최종 상태로 보존
- 제품 성숙 후 필요 시 Repository 분리 가능

---

## D-PW-002 제품 정의 확정 (2606.26)

- 급여(기본급/제수당)는 자동 계산 결과이며 관리 대상이 아님
- 기본근무는 설정 대상 (반복 패턴 / 계산 기준)
- 수당근무는 핵심 관리 대상 (추가 / 수정 / 삭제 / 저장)
- 모든 기록은 수당근무를 중심으로 이루어짐

---

## D-PW-003 협업 시스템 운영 원칙 확정 (2606.26)

- 문서 구조 변경 없음 (absolute-rules / current-step / decisions / manual / reviews)
- merged-context 읽기 프로토콜 변경 없음
- current-step 초기화 금지
  → Payroll Calculator 종료 선언 후 Workbook 시작으로 연결
- Workbook 관련 결정사항을 기존 decisions에 연속하여 기록한다

---

## D-PW-004 GitHub 운영 원칙 확정 (2606.26)

Repository 공유 → Branch 분리 → 제품 분리

- paycheck-workbook 브랜치에서 개발
- main = Payroll Calculator 최종 보존
- 새 Repository 생성 조건: 베타 출시 / 외부 공개 / 별도 배포 시점

---

## D-PW-005 제품 도메인 모델 확정 (2606.26)

급여
├── 기본급       ← 자동 계산 결과
└── 제수당       ← 자동 계산 결과

근무
├── 기본근무     ← 설정 대상 (반복 패턴 / 계산 기준)
└── 수당근무     ← 관리 대상 (추가 / 수정 / 삭제 / 저장)

급여는 관리하지 않는다. 근무를 관리하면 급여는 따라온다.

---

## D-PW-006 제품 빌드업 순서 확정 (2606.26)

STEP 1: 기본근무내역 설정
STEP 2: 수당근무내역 관리
STEP 3: Dashboard / 급여요약
STEP 4: 영속 저장 및 데이터 관리 (localStorage / Export / Import 포함)
STEP 5: 3단 자가 검산

- UI와 데이터 구조 확정 후 영속 저장 적용
- Dashboard 구현 중 localStorage 일부 선행 가능
- 이 순서는 개발 일정이 아니라 제품이 성장하는 단계이다

---

## D-PW-007 Dashboard 정보 구조 확정 (2606.26)

Dashboard 정보 계층: 결과 → 구성 → 관리 → 안내

총급여 / 실수령        ← 결과
────────────
기본급 / 제수당        ← 구성
────────────
수당근무 관리          ← 관리
────────────
급여 이해 / 명세 참조  ← 안내

- 기본근무 관리를 Dashboard Primary로 두지 않음
- 기본근무는 설정 성격이므로 Dashboard 중심이 아님

---

## D-PW-008 UI 설계 프레임워크 확정 (2606.26)

모든 신규 기능은 아래 순서로 설계한다:

① 목적 (Purpose) — 왜 필요한가?
② 화면 구조 (Screen Flow) — 어디서 어디로?
③ 화면 배치 (Layout) — 사용자가 보는 UI
④ 데이터 (Data Model) — 무엇을 저장하는가?
⑤ 구현 영향 (Implementation) — 추가/수정/제거
⑥ 사용자 관점 (User Perspective) — 무엇을 알고 싶은가?
⑦ 화면 Primary — D-PW-009 참조

---

## D-PW-009 기본 화면 흐름 확정 (2606.26)

급여기간 목록
↓
급여기간 Dashboard
↓
기본근무내역 설정
↓
수당근무내역 관리
↓
3단 자가 검산

- ResultGrid에서 바로 Drawer 편집으로 가지 않음
- Dashboard → 수당근무 관리 메뉴 통해 진입

---

## D-PW-010 Primary 원칙 확정 (2606.26)

사용자의 가장 큰 관심사가 그 화면의 Primary가 된다.

- Dashboard Primary: 총급여 / 제수당
- 수당목록 Primary: 기록 목록
- 3단 자가 검산 Primary: 변경 결과

Primary는 기능이 아니라 사용자의 관심으로 결정한다.

---

## D-PW-011 영속 저장 원칙 확정 (2606.26)

기록 기반 제품이므로 급여기간 데이터를 세션 종료 후에도 유지해야 한다.

- localStorage 방식 채택
- 구현 시점: STEP 4 (UI/데이터 구조 확정 후)
- Dashboard 구현 중 일부 선행 가능
- 조건: 앱 종료 후 재진입 시 수당근무 내역 보존

---

## D-PW-012 Table 중심 UI 원칙 확정 (2606.26)

Paycheck Workbook의 입력 UI는 Form 중심이 아니라 Table 중심으로 설계한다.

| 구분 | 목적 | 성격 |
|------|------|------|
| 기본근무내역 설정 Table | 반복 근무 패턴 설정 | 설정 |
| 수당근무내역 관리 Table | 수당근무 이벤트 기록 및 관리 | 기록 |

모바일 Table 원칙:
- 가장 중요한 컬럼만 1행 표시
- 부가 정보는 같은 Row의 2행으로 확장
- Workbook 느낌 유지하면서 모바일 가독성 확보

---

## D-PW-013 협업 문서 운영 원칙 확정 (2606.26)

현 단계에서는 기존 협업 문서 체계를 유지한다.

제품 철학과 공통 설계 원칙은 absolute-rules에 요약만 반영한다.
전문은 Reference 문서로 관리한다.
Repository 독립 시 문서 체계를 정식 분리한다.

---

## D-PW-014 Current-step 운영 원칙 확정 (2606.27)

① current-step에는 현재 진행 중인 STEP만 유지한다.
② 완료된 STEP은 current-step에서 즉시 제거한다.
③ 완료 이력은 Git History와 decisions가 담당한다.
④ 제품 전환 시 decisions에 종료 선언을 기록하고,
   current-step은 새 제품 기준으로 교체한다.
⑤ archive/current-step-retired.md는 생성하지 않는다.
   단, 제품 종료 사실 자체는 decisions에 1회 기록한다.

---

## D-PW-015 Payroll Calculator 종료 선언 (2606.27)

Payroll Calculator 개발 종료.
Paycheck Workbook으로 제품 전환 완료 (2606.26).
이후 current-step은 Paycheck Workbook 기준으로만 운영.

현재 상태 스냅샷:
- ✅ Paycheck Workbook 제품 방향 확정
- ✅ D-PW-000~013 확정
- ✅ 협업 시스템 전환 완료
- ✅ 새 쓰레드 이관 준비 완료
- 이제부터는 문서 단계가 아니라 구현 단계

---

## D-PW-016 STEP 실행 절차 확정 (2606.27)

모든 STEP에 동일하게 적용되는 표준 실행 프로세스:

① STEP 대상 확인        (D-PW-006)
② 정보 구조 결정        (D-PW-007)
③ 화면 흐름 결정        (D-PW-009)
④ 설계 프레임워크 적용  (D-PW-008)
   - Purpose / Screen Flow / Layout
   - Data Model / Implementation
   - User Perspective
   - Primary ← D-PW-010 기준 적용
⑤ UI/UX 검토
⑥ 구현 프롬프트 작성
⑦ 구현
⑧ 검증 (기능·도메인·UX 포함)
⑨ 완료

---

## D-PW-017 BasicWorkDefinition Entity 명세 확정 (2606.27)

### 분류 / 필드 / 저장여부 / 파생여부

| 분류 | 필드 | 저장 | 파생 |
|------|------|------|------|
| 사업장 | 사업장명 | ✔ | |
| 사업장 | 5인미만 여부 | ✔ | |
| 급여기준 | 시급 | ✔ | |
| 근무규칙 | 근무패턴 | ✔ | |
| 근무규칙 | 근무요일 | ✔ | |
| 시간정의 | 출근시각 | ✔ | |
| 시간정의 | 퇴근시각 | ✔ | |
| 시간정의 | 휴게시간 | ✔ | |
| 계산결과 | 근무시간 | | ✔ |

### Relationship
- BasicWorkDefinition 1:N AllowanceRecord
- BasicWorkDefinition N:1 PayPeriodSummary

### 최소 Lifecycle
- 생성: 사용자가 기본근무를 처음 설정할 때
- 수정: 근무 조건이 바뀔 때
- 참조: 수당근무 기록 생성 시
※ 삭제·보관·Export는 해당 STEP에서 구체화

---

## D-PW-018 3계층 아키텍처 확정 (2606.27)

```
Domain Layer
    ↓
Information Layer
    ↓
Presentation Layer
```

- Domain: Entity (SoT) — 변경 최소화
- Information: 인지 모델 — UX에 따라 조정 가능
- Presentation: 표현 전략 — 구현 방식, 가장 유연

※ Behavior Contract는 독립 Layer가 아니라
  Information과 Presentation을 연결하는 행동 규약

---

## D-PW-019 Information 인지 모델 확정 (2606.27)

```
Context → Condition → Result
```

Context
├── Identity  (이 근무는 무엇인가 — Primary 기준)
└── Schedule  (언제 이루어지는가)

Condition: 출퇴근시각 / 휴게시간 / 시급 / 5인미만 여부

Result: 근무시간 (파생값 — 저장 안 함)

---

## D-PW-020 Behavior Contract 확정 (2606.27)

User Intent 중심으로 정의. 플랫폼이 바뀌어도 유지.

```
User Intent → Behavior Contract → System Behavior
```

BasicWorkDefinition Behavior Contract:
- 조회: Decision Browser 진입
- 선택: Action Editor 열림
- 수정 후 저장: Browser 복귀 + Row 업데이트
- 뒤로가기(변경 없음): 즉시 복귀
- 뒤로가기(변경 있음): 확인 후 복귀
- 삭제: 확인 후 Row 제거
- 추가: 빈 Action Editor 열림

---

## D-PW-021 Presentation Design Model 확정 (2606.27)

```
User Intent
    ↓
Pattern (Basis)
    ↓
Component
    ↓
Visual
```

- Pattern은 구현보다 오래 유지되는 표현 전략의 기준
- SoT가 아니라 Basis (표현 전략의 기준)

---

## D-PW-022 Decision/Action Role + View 확정 (2606.27)

### Role (불변 — 사용자 목적)
- Decision: 탐색·비교·선택
- Action: 생성·수정·저장

### View (가변 — 구현 방식)
- Browser: 현재 구현 (List Pattern → Table)
- Editor: 현재 구현 (Form Pattern → Bottom Sheet)

현재 구현:
- Decision Browser → List Pattern → Table
- Action Editor → Form Pattern → Bottom Sheet

---

## D-PW-023 Information Priority Model 확정 (2606.27)

### Decision Browser
- P1 Identity (사업장명) — Primary
- P2 Schedule (근무요일·패턴)
- P3 Result (근무시간 자동계산)

### Action Editor
Identity → Schedule → Condition → Result Preview

※ Condition은 Browser 범위 밖 — Action Editor 책임

---

## D-PW-024 설계 가설 관리 (2606.27)

검증 시점: STEP 2 완료 후 일괄 검토

① Workspace 패턴
   가설: Workspace = Decision Browser + Action Editor
   검증 시점: STEP 1·2 완료 후
   승격 조건: 동일 패턴이 STEP 1·2에서 반복 확인 시

② 4계층 아키텍처
   가설: Interaction을 독립 Layer로 추가
   검증 시점: STEP 1·2 Behavior Contract 비교 후
   승격 조건: Behavior Contract가 독립 Layer로
             역할 분리 확인 시

③ STEP별 Browser 일반화
   가설:
   STEP 1: BasicWorkDefinition Browser
   STEP 2: AllowanceRecord Browser
   STEP 3: PayPeriodSummary Browser
   검증 시점: STEP 2 설계 후
   승격 조건: AllowanceRecord Browser가
             동일 구조로 설계될 때

---

## D-PW-025 STEP 1 설계 완료 및 Presentation 단계 전환 선언 (2606.27)

D-PW-017~023까지 완료.
이후 STEP 1은 원칙 수립이 아니라
Presentation(D-PW-008) 적용 단계로 전환한다.

---

---

## D-PW-026 TASK-001 AI Push Automation 완료 (2606.29)

### 결정
Claude가 생성한 commit을 사용자 Release Gate 승인만으로
GitHub main에 반영하는 AI Push 파이프라인 구축 완료.

### 구현 완료
- GitHub App: Jin-Docs-Automation (App ID: 3979368)
- Workflow: .github/workflows/ai-push.yml
- 브랜치: ai/draft (영구 유지)
- Environment: release-gate (Required Reviewer: jingwak-maker)

### 파이프라인
```
ai/draft push
    ↓ Validate & Artifact
    ↓ PR 조회/생성 (재사용 우선)
    ↓ PR HEAD SHA 기록
    ↓ Release Gate (사용자 승인)
    ↓ SHA 재검증
    ↓ gh pr merge
    ↓ docs-automation
    ↓ ai/draft 동기화
```

### 운영 원칙
- bot self-trigger 방지: validate job `if: github.actor != 'jin-docs-automation[bot]'`
- Conflict 자동 해결 없음 — 재동기화 후 재실행
- force-with-lease 실패 시 수동 확인
- SHA 불일치 시 재승인 필요

### DBG-002 GitHub Actions 디버깅 순서
1. Step 목록 확인
2. 실패 Step 특정
3. 실행된 Workflow가 최신인지 확인
4. 코드(YAML) 검토

---

## D-PW-027 AI 역할 분리 확정 (2606.29)

TASK-001 구축 과정에서 AI 역할이 실질적으로 분리됨.

### 확정된 역할
- GPT: 설계 / 리뷰 / AI 간 결과 교차검증
- CodeX: Repository 분석 / Evidence 기반 Root Cause 분석
- Claude: 구현 / 수정 / 테스트 대응
- AI Push: Validate / PR / Merge / Release / Sync
- 사용자: 목표 제시 + Release Gate 승인

### 참조 문서
- `vision/AI-Development-Team.md` — 장기 비전 (Stage 0~6)
- `architecture/AI-Workflow.md` — AI 협업 계약서
- `roadmap.md` — Phase 2~5 실행 계획

---

## D-CS-001 Concept System Sprint-1 완료 (2026-07-02)

AI Company Concept System Sprint-1 완료. Concept Cards 43개 GitHub main 반영.

### 확정 사항
- Concept Card Standard v1.0, Manual Rule 1~19 확정
- RCS(Review Communication Standard) v1.1 확정
- Research Pivot: AI Behavior Research → Collaboration Environment Engineering
- TCA v1.4 Thread Closing Audit Protocol — Methodology Baseline FROZEN
- Engineering Change Registry v1.1 신설
- Patch-Freeze Applicability Rule (Rule 17) 확정
- Thread Naming Standard TNS (Rule 18) 확정
- Diff-Only Review Rule (Rule 19) 확정

### 참조 문서
- `research/sprint-1-closing-review.md` — Sprint-1 Baseline Charter
- `research/tca-thread-closing-audit-protocol.md` — TCA v1.4
- `research/patch-registry.md` — Engineering Change Registry
- `concept-system/` — Concept Cards 43개

---

## D-CS-002 Research Pivot 확정 (2026-07-02)

Threshold Foundry 연구 방향 전환 확정.

### 확정 사항
- 연구 대상: AI → Collaboration Environment
- 연구 목표: 재현 가능한 Collaboration Environment Engineering
- 핵심 질문: "어떤 협업환경이 AI의 자율성과 판단 품질을 향상시키는가?"
- ER-001 착수 조건: 모두 충족 (Ready 상태)

### 다음 단계
1. TOP-001 (Token Optimization Protocol) — Operational Priority
2. ER-001 (Environment Reconstruction) — Engineering Priority

## D-TF-001 Direction 개념 도입 (2026-07-03)

- Direction(전략적 선택) 개념을 도입
- 초기 저장 위치: notes/direction-hypothesis.md
- absolute-rules 구조 변경 없음
- SoT 3문서 체계(absolute-rules / decisions / current-step) 변경 없음
- Direction의 최종 물리적 위치는 실제 운영 경험을 축적한 후 재검토한다.


## D-BR-001 Bridge Day-1 MVP 확정 (2026-07-06)

Bridge Day-1 MVP 범위 및 세부사항 확정.
Claude/GPT 교차검토 완료
(Stage 0 Bridge Architecture,
`notes/direction-hypothesis.md` 후속 결정).

### D-BR-001-01 Bridge 정체성

- Bridge는 AI를 실행·자동화하는 시스템이 아니다.
- Bridge는 여러 AI 파트너(GPT/Claude/Replit 등) 사이에서 Question을 잃어버리지 않고 전달·추적하는 **Question Workbench**이다.
- Dashboard, 프로젝트 관리 시스템(Jira 류)이 아니다.

### D-BR-001-02 Day-1 판단 기준
(교차검토로 2회 수정된 최종 기준)

1차 기준:
"운영에서 반복되는가?"

→ 문제점:
Verification처럼 실제로 반복되는 것과
Bridge가 처리할 문제를 구분하지 못함

2차 기준:
"Bridge 안에서 반복되는가?"

→ 문제점:
Bridge가 아직 존재하지 않아
검증 불가능한 순환논리

최종 기준:
"Bridge가 해결하려는 핵심 문제인가?"

→ Question Loss / Working Memory 외부화에 해당하는가로 판단

→ 실제로 반복되는 작업이라도
Bridge 책임 범위 밖이면 제외

예)

Git Verification은 반복되지만
Git Workflow 문제이지
Question 전달·추적 문제가 아님

이 기준은 향후 기능 추가 여부 판단 시 재사용한다.

### D-BR-001-03 Day-1 MVP 기능 확정

| 기능 | Bridge 핵심 문제 | Day-1 |
|---|---|---|
| Question 생성/추적 | 예 | 포함 |
| Bridge ID 자동 생성 (Human 번호와 분리, 종료까지 불변) | 예 | 포함 |
| Sub ID (`question_id` + `sub_no` 분리 필드, 플랫 리스트 — 트리 UI 아님) | 예 | 포함 |
| Current Partner / Next Partner (From-To 구조, Partner 고정 아님) | 예 | 포함 |
| Comment | 예 | 포함 |
| Edit | 예 | 포함 |
| Dispatch (Question + Comment 조합 생성) | 예 | 포함 |
| Question 분류: New / Follow-up(기존 ID 유지) / Branch(신규 ID + Parent 기록) | 예 | 포함 |
| Git Verification | 아니오 (Bridge 핵심 문제가 아님, Git Workflow 영역) | 제외 |
| Approval Console | 아니오 (Bridge 핵심 문제가 아님, 별도 도입 예정) | 제외 |
| Dashboard / Capability 추상화 / History / Event Log / Auto Routing / SQLite·JSON Persistence / AI 자동화 | 아니오 | 제외 |

Day-1에서는 Question 분류(New/Follow-up/Branch)를 데이터 모델 수준으로 지원한다.

UI는 최소 구현 원칙을 적용하며,
플랫 리스트와 분류 뱃지 표시만 제공한다.

트리 구조(접기/펼치기)는 Day-1 범위에서 제외한다.

### D-BR-001-04 Sub ID 구현 방식

- `Q-0007-1` 문자열 파싱 방식 기각
- `question_id` + `sub_no` 분리 필드 채택
- 근거: 파싱 없이 정렬·그룹핑 가능, 확장 시 안전
- UI: 트리(접기/펼치기) 방식 기각 → 플랫 리스트 채택
- 근거: 구현 비용보다 운영(인지) 비용이 핵심
- Bridge 목적(Working Memory 외부화)상 매번 사용할 때 해석 비용이 적은 방식 우선

### D-BR-001-05 상태 명칭

Completed → No Next Target

- Day-1에는 Verification/Approval이 없어
Completed가 실제 완료(Git push/Merge)를 의미하지 않음에도 그렇게 오인될 인지적 위험이 있어 명칭 변경
- 지금 바꾸는 구조 비용은 거의 0이나,
나중에 바꾸면 "Completed = 끝났다"는 인지적 관성이 누적되므로 지금 확정
- 향후 Verification 도입 시

Working

↓

Awaiting Verification

↓

Completed

구조로 확장한다.

### D-BR-001-06 Partner 구조

- Partner는 고정하지 않고 From/To 선택 구조 사용
- Capability 중심 추상화(Capability → Partner 2단계 선택)는 Day-1 기각
- Partner가 5개 이상으로 증가하는 시점을 Trigger로 재검토(Deferred)

### 참조 문서

- `notes/direction-hypothesis.md`
  - Stage 0 Bridge Architecture 결정
- Bridge MVP 교차검토 대화 기록
  (Claude/GPT, 2026-07-06)
