# Release Workflow

버전: v1.0 (2606.29)
기준: TASK-001 AI Push Automation 완료

---

## Release 절차 (6단계)

```
1. ai/draft push
    ↓
2. AI Push workflow 자동 실행
   - Validate & Artifact 생성
   - PR 조회/생성
   - PR HEAD SHA 기록
    ↓
3. Release Gate 승인 (jingwak-maker)
   - Artifact 확인 (commit / changed-files / diff / validate.log)
   - SHA 동일 여부 확인
    ↓
4. PR HEAD SHA 재검증 (승인 전 SHA와 현재 SHA 비교)
    ↓
5. main 자동 반영
   - gh pr merge
   - docs-automation 자동 실행
    ↓
6. merged-context.md 읽기 검증
   - Auto-generated timestamp 확인
   - Source 라인 확인
```

---

## Acceptance Test 체크리스트

```
□ validate 성공
□ Artifact 4개 생성 (commit / changed-files / diff-summary / validate.log)
□ PR 생성 성공
□ 두 번째 push 시 기존 PR 재사용
□ Release Gate 승인 대기 진입
□ 승인 후 gh pr merge 성공
□ docs-automation 자동 트리거
□ merged-context.md 자동 갱신
□ ai/draft == main HEAD 확인
□ SHA 불일치 시 정상 종료
□ Merge Conflict 시 정상 종료 + 로그 구분 확인
□ force-with-lease 실패 시 정상 종료
□ bot self-trigger 방지 (0/4 스킵)
```

---

## 예외 처리

### SHA 불일치
```
원인: Release Gate 승인 대기 중 ai/draft에 새 commit push
처리: Workflow 자동 종료
해결: 새 Workflow 실행 후 재승인
```

### Merge Conflict
```
원인: main과 ai/draft 동일 파일 충돌
처리: Workflow 자동 종료
해결:
  git fetch origin
  git checkout ai/draft
  git rebase origin/main
  git push origin ai/draft --force-with-lease
```

### force-with-lease 실패
```
원인: Merge 이후 ai/draft에 새 commit 감지
처리: Workflow 종료 (정상 보호 동작)
해결: 수동 확인 후 Workflow 재실행
```

### bot self-trigger
```
원인: jin-docs-automation[bot]의 ai/draft push
처리: validate job if 조건으로 자동 스킵 (0/4)
```

---

> Acceptance Test는 시스템 요구사항, 운영 사례는 실제 수행 기록입니다.

## 운영 사례

### TASK-001 (2606.29) — AI Push 구축 및 운영 검증
- AI Push Automation 구축 완료
- Acceptance Test 전 항목 통과
- bot self-trigger 방지 검증
- SHA 재검증 실제 동작 확인

---

## Troubleshooting 원칙 (DBG-002)

GitHub Actions 실패 시 확인 순서:
1. Step 목록 확인
2. 실패 Step 특정
3. 실행된 Workflow가 최신인지 확인
4. 코드(YAML) 검토

---

## 참조

- `absolute-rules.md` — Release 절대 원칙
- `architecture/AI-Workflow.md` — AI 협업 계약서
- `.github/workflows/ai-push.yml` — AI Push Workflow
- `.github/workflows/docs-automation.yml` — 문서 자동화
