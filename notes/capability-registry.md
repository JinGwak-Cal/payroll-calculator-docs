# Capability Registry

"무엇이 자동화되어 있는가"가 아니라 "누가 무엇을 잘하는가/담당하는가"를
기록한다. Bridge가 작업을 라우팅할 때 이 문서를 참조한다.

| Capability | 담당 | 자동화 여부 | 비고 |
|---|---|---|---|
| Code Review | GPT | 가능 (수동 요청) | 오늘 세션 내내 사용된 방식 |
| Code Implementation | Claude / Replit Agent | 가능 | Claude=문서·스크립트, Replit=앱 코드 |
| Git Push (main 반영) | Replit Agent | 가능 (ai-push.yml 경유) | Claude는 로컬 커밋까지만, push 권한 없음 |
| PR 생성 | GitHub Actions (ai-push.yml) | 자동 | ai/draft push 시 자동 트리거 |
| Merge 승인 | Jin (Human) | 승인 필요 (release-gate) | 유일한 필수 Human 개입 지점 |
| merged-context 생성 | GitHub Actions (docs-automation.yml) | 자동 | absolute-rules/current-step/decisions 변경 시만 |
| Lens 분석/Sampling | pipeline.py (Jin 로컬 실행) | 가능 | Claude 토큰 0, Jin PC에서 실행 |
| 원본 대화 Archive | Claude Export 기능 (브라우저) | 가능 | Claude 토큰 0 |
| 로컬 검색/필터 | Excel, VSCode, ripgrep 등 | 가능 | Claude 토큰 0 |
| 실패 진단 (Diagnosis Gate) | Claude | 원칙으로 존재, 자동화 아님 | E-002 Candidate Principle |
| Question Routing | 미정 | 예정 (Bridge Step1) | 아직 사람이 수동 중계 |
| AI 간 상태 확인/검증 | 미정 | 예정 (Bridge Step1) | 아직 사람이 수동 확인 |
| GitHub 웹 직접 편집 | Jin (Human) | 가능하나 **비권장** | ai-push 경로가 있으면 그쪽 우선 (Decision Matrix 참조) |

Status: Candidate (Bridge Step1 진행되며 계속 갱신)