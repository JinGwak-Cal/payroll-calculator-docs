# 절대 규칙
- v13.2 기준 고정
- 재정의 금지
- 없는 부분만 추가 허용
- 전체 재작성 금지
- 증분 코드만 출력
- 캘디게 구조 변경 금지
- 계산은 항상 수행 / 표시만 제어
- premiumAmount state 저장 금지
- 입력은 state / 결과는 useMemo 원칙 유지

# 작업 시작 프로토콜 (모든 AI 파트너 공통 강제)
작업 시작 전 반드시 index.md 실제 읽기 실행
확보 상태 표시 후에만 작업 가능:

[작업 시작 상태]
index.md       □ 미확보 / ■ 확보
current-step   □ 미확보 / ■ 확보
decisions      □ 미확보 / ■ 확보
absolute-rules □ 미확보 / ■ 확보

하나라도 미확보 시:
- 현재 STEP 추정 금지
- 구조 판단 금지
- 코드 생성 금지
- 읽기 실행 후 재시작

# 읽기 검증 프로토콜
■ 확보 표시 조건

반드시 merged-context.md에서 아래 원문을 인용:

1. Auto-generated timestamp
2. Source 라인

그리고 merged-context의 원천 문서 중 하나에서 아래를 추가 인용:

- current-step 최근 변경사항 1건
또는
- decisions 최근 결정사항 1건
또는
- absolute-rules 최근 변경사항 1건
또는
- absolute-rules 최근 변경 없음 + 핵심 규칙 1건

위 조건을 충족하지 못하면
□ 미확보

# 작업 시작 지시 정의
작업 시작 지시란 다음을 의미한다:
- 특정 STEP/G/P/BUG/UX 항목을 진행/검토/구현하라는 지시
- Codex/Claude/Agent 전달문 작성 요구
- "이어서 작업하자" 류의 지시

작업 시작 지시 시 순서:
1. index.md 실제 읽기
2. reviews/active/ 관련 파일 존재 확인
3. 있으면 읽고 반영
4. 없으면 "active review 없음" 보고 후 진행

일반 질문(개념/비용/가능성)은 작업 시작 지시 아님
→ reviews/active 자동 참조 불필요

# AI 협업 구조
Claude 검토 저장: reviews/active/claude/
GPT 검토 저장: reviews/active/gpt/
완료 작업 이동: reviews/completed/

index.md에는 reviews 전문 미포함
reviews는 필요 시 bash_tool로 직접 참조
# reviews 식별자 규칙
형식: 작업단위(sub.n).파트너명.현업N-n.md

작업단위: P4, G3, UX 등
sub.n: 서브작업 번호 (독립)
현업N: 서브작업 내 현업 번호 (독립)
n: 팔로업 순서 (1씩 증가)

예시:
P4(1).claude.현업1-1.md   ← 서브1, 현업1, Claude 1차
P4(1).gpt.현업1-2.md      ← 서브1, 현업1, GPT 팔로업
P4(1).claude.현업1-3.md   ← 서브1, 현업1, Claude 재반영
P4(1).claude.현업2-1.md   ← 서브1, 현업2 (다른 현업)
P4(2).claude.현업1-1.md   ← 서브2, 현업1
# reviews 식별자 규칙 (확정)
형식: 작업단위(sub.n).파트너명.현업N-n.YYMMDDHHmm.md
총 12자리 날짜시간: 년2자+월2자+일2자+시2자+분2자

예시:
P4(1).claude.현업1-1.2605281430.md
P4(1).gpt.현업1-2.2605281510.md
P4(1).claude.현업1-3.2605281545.md
P4(1).claude.현업2-1.2605281600.md
P4(2).claude.현업1-1.2605281700.md

# reviews 목록 출력 규칙
- 최신 파일이 항상 맨 위에 표시
- 날짜시간 기준 내림차순 정렬
- Claude가 목록 출력 시 자동 적용
# GitHub 문서 접근 우회 규칙
1. raw.githubusercontent.com URL 접근 실패 시 즉시 실패로 판단하지 않는다.
2. 같은 경로의 github.com/.../blob/main/... URL로 재시도한다.
3. GitHub blob Preview 또는 Raw 링크 확인까지 시도한다.
4. 그래도 실패할 때만 "미확보"로 보고한다.
# reviews 목록 출력 형식 (필수)
Claude가 reviews 파일 목록 출력 시 반드시 raw + blob URL 동시 표시:

파일명 (크기)
raw: https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/[경로]
blob: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/[경로]

이유: GPT는 blob URL 생성은 가능하지만 raw 실패 시 자동 전환이 보장되지 않음
따라서 GitHub 문서 전달 시 raw + blob URL을 함께 제공
Jin님이 두 URL 중 작동하는 것을 GPT에 전달
# 저장 후 검증 규칙
reviews 파일 저장 후 반드시:
1. 저장된 파일 내용 실제 읽기
2. 원본 내용과 비교
3. 누락 없음 확인 후 완료 보고
누락 발견 시 즉시 재저장

# 답변 정직성 규칙
사용자가 원하는 답을 예측하여 그 방향으로 답하는 것을 금지한다.
틀린 것을 알면서 정정하지 않는 것을 금지한다.
확실하지 않으면 즉시 "불확실"을 먼저 선언한다.

# 지시 이행 불가 시 응답 규칙
지시를 이행할 수 없는 경우 반드시 아래 형식으로 답변한다.
못 하는 이유: [구체적 원인]
대안: [가능한 방법]
"안 됩니다"만 답하는 것을 금지한다.

# 업데이트 위치 제안 규칙
업데이트 내용의 위치 제안 시 반드시:
1. 해당 문서의 전체 구조를 먼저 파악한다
2. "[A] (N번째 줄) 와 [B] (N번째 줄) 사이" 형식으로 명시한다
3. 위치 선정 이유를 함께 제시한다

# 작업 단계 선제 제시 규칙
지시 이행 시 반드시:
모든 작업 단계를 구분하여 일목요연하게
한 페이지 이내 분량으로 먼저 제시한다

# 협업 운영 규칙 v1

## §운영-1 자동 판단 금지 (핵심 원칙)
명시적으로 요청되지 않은 행위를 금지한다.
- 보고=보고 / 조사=조사 / 검토=검토
- 생성·저장·업데이트는 명시적으로 요청된 경우에만 수행한다.

## §운영-2 승인 원칙
다음 행위는 반드시 Jin님 승인 후 진행한다.
- 파일 생성 / 삭제 / 덮어쓰기
- 보고용 문서 생성
- 커밋 / GitHub push / 원격 미러 업데이트
- current-step.md 수정 / decisions 수정 / absolute-rules 수정

## §운영-3 읽기 전용 원칙
다음 표현은 모두 읽기 전용 요청으로 간주한다.
읽어줘 / 확인해줘 / 검토해줘 / 평가해줘 / 조사해줘 / 보고해줘
위 요청 시: 수정·생성·삭제·커밋·push 모두 금지

## §운영-4 생성 승인 원칙
다음 표현이 있을 때만 생성 행위를 허용한다.
생성해 / 작성해 / 저장해 / 등록해 / 업데이트해 / 반영해
위 표현이 없으면 생성 행위 금지
읽기 전용 표현 + 생성 표현이 동시 존재 시 생성 표현 우선

## §운영-5 덮어쓰기 원칙
기존 파일이 존재할 경우 자동 덮어쓰기를 금지한다.
반드시 다음 중 하나를 사용자에게 확인받는다: 신규 파일 생성 / 기존 파일 업데이트 / 작업 중단
승인 응답을 받기 전까지 해당 파일에 대한 모든 작업을 중단한다.

## §운영-6 GitHub 원칙
commit / push / 파일 생성·수정·삭제 / 원격 미러 업데이트
모두 명시적 승인 후 진행

## §운영-7 자동 커밋 원칙
사전 보고 가능 시 사전 보고. 불가능한 경우 발생 즉시 보고.
보고 항목: 커밋 해시 / 변경 파일 / 변경 내용 요약

## §운영-8 특별 관리 문서
current-step.md / decisions / absolute-rules
생성·수정·삭제 모두 승인 필수

## §운영-9 범위 초과 원칙
작업 지시 범위 외 파일(.replit / index.css 전역 / 환경설정 등) 수정 금지
필요 시 사전 보고 후 승인

## §운영-10 계산 로직 특별 규칙
calc-engine.ts / use-calc.tsx / 계산 결과에 직접 영향을 주는 파일
수정 전 반드시: 변경 필요성 보고 → 영향 범위 보고 → 승인 획득

# 매뉴얼 업데이트 규칙

## 업데이트 후 확인
- absolute-rules.md 수정 시:
  절대 규칙 및 운영 규칙이 약화/훼손되지 않았는가?

## 대기 표시 규칙
- 신규 대기 → 내용 상세 표시
- 기존 대기 (미반영) → 제목 + 한 줄만

## 대기 형식
[업데이트 대기 #N]
내용: [추가/수정할 내용]
대상 파일: [어느 파일]
근거: [왜 그 파일인지]
우선순위: 높음 / 보통 / 낮음

## 대상 파일 판단 기준
absolute-rules.md → 모든 파트너 공통 강제 규칙
current-step.md   → 현재 작업 단계 변경
decisions.md      → 확정된 결정 사항
index.md          → 진입점/운영구조 변경
manual-v14.md     → 앱 개발 설계/스펙 변경

## URL 참조 규칙
문서 내 모든 URL은 JinGwak-Cal 기준으로 유지한다.
jingwak-maker URL 사용 금지.
올바른 URL 형식:
raw: https://raw.githubusercontent.com/JinGwak-Cal/payroll-calculator-docs/main/[파일명]
blob: https://github.com/JinGwak-Cal/payroll-calculator-docs/blob/main/[파일명]

## 적용 시점
Jin님 승인 후 일괄 반영 (소소한 사항은 모아서)
