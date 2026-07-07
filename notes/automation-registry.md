# Automation Registry

"무엇이 존재하는가"만 기록한다. "언제 쓰는가"는
automation-decision-matrix.md를 참조.

| 이름 | 형식 | 트리거 | 역할 |
|---|---|---|---|
| pipeline.py | Python (로컬 실행) | Jin 수동 실행 | Lens Distribution/Coverage/Sampling/Bundle 생성 |
| config.json | 설정 파일 | pipeline.py가 읽음 | 키워드 Lens, Sampling 규칙 정의 |
| merge_docs.py | Python (Actions 내부) | docs-automation.yml이 호출 | absolute-rules/current-step/decisions 병합 |
| docs-automation.yml | GitHub Actions | main에 absolute-rules.md/current-step.md/decisions.md push 시 | merged-context.md 자동 재생성 |
| ai-push.yml | GitHub Actions | ai/draft branch push 시 | 검증→PR 생성→release-gate 승인 대기→main merge→ai/draft 재동기화 |
| batch-release.yml | GitHub Actions | ai/draft에 release-manifest.json push 시 | 배치 릴리즈 (세부 미검토) |
| test-token.yml | GitHub Actions (수동 실행, workflow_dispatch) | 수동 트리거 | GitHub App 토큰 발급 테스트 |

Status: Candidate (Bridge 구축되며 항목 추가 예정)