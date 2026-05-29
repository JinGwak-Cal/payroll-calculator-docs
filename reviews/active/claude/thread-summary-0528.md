# 협업 구조 설계 문답 요약
생성일: 2026-05-28

## 채택 구조: B안 중심
Claude 답변 → GitHub 자동 저장 → GPT URL로 읽기 → Jin님 복붙 1회 → Claude 저장 → 최종 반영

## 폴더 구조
docs/reviews/active/claude/ - Claude 검토
docs/reviews/active/gpt/ - GPT 검토
docs/reviews/completed/ - 완료 보관

## 토큰 비교
복붙: 전체 대화 맥락 = 누적 토큰 소모
GitHub 읽기: 파일명 매칭으로 관련 파일만 = 대폭 감소
index.md 최적화: 74,255 bytes → 2,527 bytes (97% 감소)

## 식별자 규칙 (확정)
형식: 작업단위(sub.n).파트너명.현업N-n.YYMMDDHHmm.md
최신 파일 항상 맨 위 표시 (날짜시간 기준 내림차순)

## 작업 흐름 (보조 규칙, 상황에 따라 순서 변경 가능)
기본:
Claude 분석+저장 → GPT 교차검증 → Claude 최종 반영

선행 교차검증 필요 시:
GPT 먼저 검토 → Claude 분석+저장 → GPT 재검토

Jin님이 상황에 따라 순서 결정
→ 절대 규칙 아님, 작업 진행 보조 규칙

## Jin님 개입 지점
① GPT에게 URL 전달 (새 대화 시작 시)
② GPT 답변 Claude에 복붙 (교차검증 후)

## 상태유급형 수당 작업 순서 (GPT 검토 반영)
P4 주휴 미결
→ P7 연차수당
→ 상태유급형 그룹 정리
→ 시간속성형 UI 재검토
→ G-8 라벨 체계 뒤집기

P4 미결 항목:
- 파란 배지 ①: 개근 여부 선택
- 파란 배지 ②: 주 15시간 이상 근무 여부

