# Research Backlog

상태값: Deferred(우선순위 밀림) / Blocked(다른 작업 완료 필요) /
Waiting(Evidence 부족) / Idea(아직 정식 제안 안 됨)

| ID | 제목 | Status | Reason |
|---|---|---|---|
| DEFER-001 | approval Lens Relevance 판단 | Deferred | Bridge Architecture 우선 구축 결정 (Jin 승인) |
| DEFER-002 | Bridge Step2+ (Question Bridge: Card 단위 UI, 멀티 라우팅, 상태 시각화, 부분/편집 전달 등) | Idea | Step1(최소 동작) 완료 전까지는 설계 범위 확대 보류 |
| DEFER-003 | Role 축을 Operational Cost Taxonomy에 추가 | Idea | Bridge Step1 실 운영 후 필요성 확인되면 도입 |
| DEFER-004 | E-008(Persistence Loss) Evidence 번호 승격 여부 | Waiting | 반복 관찰(2회 이상) 필요, 현재 1회만 확인 |
| DEFER-005 | bridge-protocol.md / bridge-interface.md / approval-console.md | Idea | Bridge Step1 설계 완료 후 문서화 |
| DEFER-006 | release-checklist.md | Idea | 필요성 아직 미확인 |
| DEFER-007 | onboarding-checklist.md | Idea | START-HERE.md로 우선 대체, 부족함 확인되면 별도 생성 |
| DEFER-008 | reviews/active, reviews/completed 폴더 | Idea | 필요성 아직 미확인 |

## DEFER-001 상세

- 계획됨: Distribution → Coverage → Purity → Relevance → Sampling → Observation
- 진행 상태: Purity까지 완료. Relevance 단계 진입 직전 Bridge Architecture로 우선순위 전환.
- 재개 조건: Bridge Step1 구축 완료 후
- 필요 자산: bundles/approval_bundle.md, bundles/approval_bundle.json (Jin 로컬에 이미 생성됨, pipeline.py 실행 결과)