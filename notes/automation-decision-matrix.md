# Automation Decision Matrix

작업을 시작하기 전, 이 표부터 확인한다. "자동화가 있는가?"를
먼저 확인하지 않고 사람에게 수동 작업을 요청하는 것이 오늘 세션
최대 실수 중 하나였다 (예: ai-push.yml을 몰라서 GitHub 웹 5개 파일
수동 편집부터 제안한 사례).

| 작업 | 자동화 존재 | 사용 도구 | 허용된 사람 개입 |
|---|---|---|---|
| 문서(notes/ 등)를 main에 반영 | YES | ai-push.yml (ai/draft push) | release-gate 승인 클릭만 |
| GitHub 파일 직접 웹 편집 | 가능하나 우회 경로 | — | ai-push 사용 불가할 때만 최후 수단 |
| merged-context.md 갱신 | YES | docs-automation.yml | 없음 (완전 자동) |
| CSV/Lens 분석 | YES | pipeline.py | conversations.json 준비 + 1회 실행만 |
| Thread별 Sampling | YES | pipeline.py (config.json 규칙) | 없음 (규칙 수정 시에만 config.json 편집) |
| 대화 원본 보존 | YES | Claude Export 기능 | 버튼 클릭 1회 |
| GitHub 코드 push (앱) | YES | Replit Agent | 지시문 전달 + 결과 확인 |
| AI 간 질문/답변 전달 | NO (예정, Bridge Step1) | 현재는 사람이 복붙 | 전체 수동 (개선 대상) |

Status: Candidate (신규 자동화 추가 시 이 표부터 갱신)