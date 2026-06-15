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

현재 단계: STEP 4 — UI 인벤토리 작성 (★실질적 UI 설계 시작점) — 완료
다음 단계: STEP 5 — ResultGrid 중심 재설계 검토 및 UI 체계 후속 정리
비고:
- STEP4 결과: Inventory 22건 + Source Gap 4건, UI-Audit(01) §1~9 전수 매핑 완료
- UI-Audit(01~04) 원본 수정 없음 (인벤토리는 별도 산출물로 보존)
- ResultGrid(RESULT-01~05) Lifecycle=Redesign 표시만, 재설계는 STEP5 이후
- RESULT-03 Component(Card/Row) 분류 검토사항 → STEP5 ResultGrid 재설계 시 시나리오 A/B 재검토 (산출물 §5 참조)

---

## 구조2-A 현재 STEP 필요 문서 (Required Documents)

※ 구조는 확정되었으나 UI-Audit 문서는 아직 repo URL 등록 전 상태. URL 확보 후 즉시 갱신.
※ 현재 STEP 수행에 필수인 문서만 기재. 참고문서·선택문서는 포함하지 않음.

| 문서ID | raw | blob | 상태 | 용도 |
|--------|-----|------|------|------|
| UI-Audit-01 | TBD | TBD | URL 등록 대기 | 9개 영역 전수조사 원본 |
| UI-Audit-05 | TBD | TBD | URL 등록 대기 | 4축·C안·색상3층 정본 |
| UI-Audit-06 | TBD | TBD | URL 등록 대기 | X-5/X-6 절차 정본 |

STEP 전환 시 본 표를 해당 STEP 기준으로 갱신.
표에 없거나 URL 미기재 시 → 사용자에게 1회 요청 후 진행.

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

### UI 인벤토리 완료
- STEP4 UI Inventory 작성 완료 (Inventory 22건 + Source Gap 4건)
- UI-Audit(01) §1~9 전수 매핑 확인, 누락 없음
- RESULT-03 Component 분류(Card/Row) 검토사항 → STEP5 ResultGrid 재설계 시 재검토 (산출물 §5 참조)
- 산출물: UI-Inventory-STEP4-22건.md

상세: archive/current-step-retired.md 참조
