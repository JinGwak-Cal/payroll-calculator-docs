# STEP1-A. Evidence Plan

Collection 전에 무엇을 어떤 방법으로 실측할지 먼저 선언.

| # | Target | Method | Expected Output | Acceptance |
|---|---|---|---|---|
| 1 | A-08(제안-실행 승인게이트) 실제 발생·위반 횟수 | Claude 원문(Source A)에서 "검토 요청→같은 답변 내 파일수정/실행" 패턴 grep | Occurrence Count(정수) | 원문 내 실제 매치 건수와 일치 |
| 2 | C-07(실측검증) 위반 사례 | Source A에서 "됐습니다/없습니다" 서술이 grep/fetch보다 먼저 나온 지점 검색 | Occurrence Count | 원문과 일치 |
| 3 | C-14(규칙제안 대기) 위반 사례 | Source A에서 "규칙 추가"가 승인 없이 즉시 실행된 지점 검색 | Occurrence Count | 원문과 일치 |
| 4 | 오늘 산출물 Created/Modified/Verified/Withdrawn 4분류 | `ls -la` + `git status` + 이번 대화에서 언급된 파일명 대조 | 파일별 4분류 표 | 실제 파일 존재/부재와 일치 |
| 5 | GPT측(Source B) A-08 유사 패턴 | Source B 텍스트 grep(승인 없이 실행, "Preflight를 먼저 수행합니다" 같은 자기실행 선언 패턴) | Occurrence Count(참고용, Source A 대비 보조) | 원문과 일치 |

Acceptance 공통 기준: 모든 Count는 실제 grep 매치 라인 번호를
근거로 제시(추정 표현 "약/최소" 사용 금지 — 오늘 반복된 실수).
