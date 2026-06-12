# 현재 작업 단계

---

## 구조1 전체 로드맵

출시까지 전체 단계:
1. 문서 체계 정비 ← 진행 중
2. Premium Phase 잔여 작업 (2-8 → 2-5 → 2-6)
3. 상태유급형(주휴·연차) 정리
4. 시간속성 수당 UI 정리
5. UI 통일
6. 검증
7. 출시 준비

---

## 구조2 현재 단계 ← 현재

문서 체계 개편 및 Archive 구조 정비
- absolute-rules.md 구조 전면 개편 ✅
- decisions.md 구조 개편 ✅
- current-step.md 개정 진행 중 ⏳
- index.md 개편 예정

---

## 구조3 다음 작업

1. current-step.md 개정 완료 및 archive/current-step-retired.md 생성
2. index.md 개편
3. merged-context 재생성 확인
4. 신규 쓰레드 진입 테스트

---

## 구조4 대기

### 앱개발 대기
※ 2-5/2-6은 고위험 모델 작업이므로 2-8 이후 순서 유지
- Phase 2-8: 인라인 제거 확인 및 잔여 정리
- Phase 2-5: 근무내역 단위 (고위험 — 별도 설계 보고 후)
- Phase 2-6: 조합 자동 해석 (2-5 확정 후)

### 워크플로우 단기
- GitHub Actions 동작 검증 완료 확인 ⏳
- 자동 병합 스크립트 개선

### 워크플로우 중기
- 중앙 Context Builder 구축
- LLM 결과 자동 검증 체계 구축

---

## 구조5 보류

현재 없음

---

## 구조6 완료요약

### 앱개발 완료
- Premium Phase 완료 (Phase 2-1~2-4, 2-7)
- BUG-1 History reload 복원 ✅
- floor 정책 확정 ✅

### 워크플로우 완료
- 문제 진단: 최신 문서 LLM 자동 주입 부재 확인
- Fine-grained 토큰 3개 발급 및 Replit Secrets 저장
- GitHub App (Jin-Docs-Automation) 구축 완료
- GitHub Actions 구축 완료

### 문서 체계 개편 완료
- absolute-rules.md 구조 전면 개편 (v14.0 / 0612) ✅
- decisions.md 구조 개편 (D-01~D-04) ✅
- archive 구조 일부 구축 완료 ✅
- merged-context 자동 재생성 확인 ✅

상세: archive/current-step-retired.md 참조
