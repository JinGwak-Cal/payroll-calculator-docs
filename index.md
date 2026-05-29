<!-- Auto-generated at 2026-05-29T12:07:52Z -->

# absolute-rules

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
Claude 검토 저장: docs/reviews/active/claude/
GPT 검토 저장: docs/reviews/active/gpt/
완료 작업 이동: docs/reviews/completed/

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
raw: https://raw.githubusercontent.com/jingwak-maker/payroll-calculator-docs/main/[경로]
blob: https://github.com/jingwak-maker/payroll-calculator-docs/blob/main/[경로]

이유: GPT는 blob URL 생성은 가능하지만 raw 실패 시 자동 전환이 보장되지 않음
따라서 GitHub 문서 전달 시 raw + blob URL을 함께 제공
Jin님이 두 URL 중 작동하는 것을 GPT에 전달
# 저장 후 검증 규칙
reviews 파일 저장 후 반드시:
1. 저장된 파일 내용 실제 읽기
2. 원본 내용과 비교
3. 누락 없음 확인 후 완료 보고
누락 발견 시 즉시 재저장


# current-step

# 현재 작업 단계
STEP 5 완료 ✅
§19-B-1 완료 ✅
UX-02-5 shimmer 완료 ✅

다음: 대기 G (G-1~G-8) 처리

[대기 G 목록]
G-1: 섹션 안내영역 + STEP2 입력창 shimmer 이후 동시 강조 신호 
G-2: STEP3 금액 문구 능동 반영 "[수당]수당으로 총급여에 추가됩니다"
G-3: 선택 후 닫힘 상태 수당유형 미반영 버그 수정
G-4: 선택 전 닫힘 보조 문구 정책 결정
G-5: 섹션 안내영역 "총 근무시간 [N시간]" 동적 반영
G-6: 가산 금액 총급여 실제 반영 여부 검증
G-7: "세전 표시용·실수령에는 반영 안됨" 문구 정책 확인
G-8: [심각 고민 중] 라벨 체계 뒤집기 검토

# decisions

# 파트너 협의 결정사항

# manual-v14

full doc: https://raw.githubusercontent.com/jingwak-maker/payroll-calculator-docs/main/manual-v14.md
