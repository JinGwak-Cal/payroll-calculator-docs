## E-008 (Draft, evidence-log.md 미반영)

- Date: 2026-07-04
- Thread: 0703 CostMangm.Prtl.시작 (본 쓰레드)
- Trigger: evidence-log.md, operational-cost-taxonomy.md 등 여러 문서를
  로컬 git commit까지만 완료하고, GitHub(origin/main) push는 안 된 채로
  세션이 계속 진행됨. 이 컨테이너는 다음 쓰레드에서 초기화되어 사라짐.

### Observation

로컬 커밋 완료 상태를 "저장 완료"로 표현했으나, 실제로는 GitHub에
반영되지 않아 다음 쓰레드에서 접근 불가능한 상태였다. 세션 종료 전
이 상태를 점검하는 절차가 없었다.

### Candidate Principle

> 세션/쓰레드 종료 전 산출물의 영속성(Persistence)을 확인한다:
> GitHub 반영 완료 / 로컬에만 존재 / 컨테이너 임시파일만 존재 —
> 이 세 상태를 구분해서 명시한다.

검토)