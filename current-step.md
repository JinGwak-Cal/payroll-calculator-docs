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

현재 단계: STEP 6 — 가산수당 입력 체계 재설계 — 진행 중
직전 완료: STEP 5 — ResultGrid 중심 재설계 검토 — 완료 (2606.15)
다음 단계: STEP6-1 — 연차 개선
비고:
- STEP5 결과: ResultGrid 역할 재정의 · Drawer 구조 확정 · RESULT-04/05 제거 확정 · 시나리오 A 확정
- STEP6-2-1 완료: PremiumAllowanceEntry 저장 단위 확정 (id+selectedAllowances+premiumRate+premiumHours)
- STEP6-2-2 완료: mapEntriesToCalcInput() A안 확정 · 맞춤가산 MVP=단일 수당만 허용
- STEP6-2-3 완료: History 저장 구조 검증 — HistoryEntry.inputs 내부에 allowanceRows 추가 확정
- STEP6-2-4 완료: 근무지합산 알고리즘 검증 — 변환 계층 처리 확정
- 미완료 잔여 순서: STEP6-1(연차 개선)
  ※ 번호상 STEP6-1은 연차 개선이나, 선행조건상 STEP6-2-3/2-4를 먼저 진행한다.
- RESULT-03 Component=Row 신규값은 UI-Audit-05 개정 항목으로 별도 반영 필요

---

## 구조2-A 현재 STEP 필요 문서 (Required Documents)

※ 현재 STEP 수행에 필수인 문서만 기재. 참고문서·선택문서는 포함하지 않음.
※ URL은 repo 화면의 파일 경로 기준으로 생성. raw fetch 캐시 문제와 별개로 blob 기준 확인 대상.

STEP6 — 가산수당 입력 체계 재설계
| 문서ID | 경로 | 용도 |
|--------|------|------|
| STEP5-Final-확정항목인덱스 | reviews/active/claude/STEP5-Final-확정항목인덱스.claude.현업1-1.260615.md | STEP5 확정사항 종합 인덱스 |
| STEP6-2-1 | reviews/active/claude/STEP6-2-1-PremiumAllowanceEntry-데이터모델확정.claude.현업1-1.260615.md | 저장 단위 확정 |
| STEP6-2-2 | reviews/active/claude/STEP6-2-2-행배열구조-CalcInput변환.claude.현업1-1.260615.md | mapEntriesToCalcInput() A안 확정 |
| STEP6-2-3 | reviews/active/claude/STEP6-2-3-History-저장구조검증.claude.현업1-1.260618.md | History 저장 구조 검증 |
| STEP6-2-4 | reviews/active/claude/STEP6-2-4-근무지합산알고리즘검증.claude.현업1-1.260618.md | 근무지합산 알고리즘 검증 |

STEP5 완료 — 참고용 (필요 시)
| 문서ID | 경로 | 용도 |
|--------|------|------|
| STEP5-ResultGrid-Review-01 | reviews/active/claude/STEP5-ResultGrid-Review-01.claude.현업1-1.260615.md | ResultGrid 역할·RESULT-01~05 처리 |
| STEP5-4-Drawer-확정안 | reviews/active/claude/STEP5-4-Drawer-확정안.claude.현업1-1.260615.md | Drawer 구조 확정 |

STEP 전환 시 본 표를 해당 STEP 기준으로 갱신.
표에 없거나 URL 미기재 시 → 사용자에게 1회 요청 후 진행.

---

## 구조3 다음 작업

1. STEP6-1 — 연차 개선
2. UI-Audit-05 개정 — Component=Row 신규값 반영

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

### UI 재설계 완료 (STEP5 / STEP6-2-1 / STEP6-2-2)
- STEP5 ResultGrid 역할 재정의 완료 (결과 표시판 + 입력 진입점)
- RESULT-04 체크박스 방식 제거 확정 / RESULT-05 인라인 입력 제거 확정
- 시나리오 A 확정 (컨테이너 + 반복 Row 구조)
- Drawer(Bottom Sheet) 구조 확정 (칩: [연장][야간][휴일][완료])
- STEP6-2-1 PremiumAllowanceEntry 저장 단위 확정 (id+selectedAllowances+premiumRate+premiumHours)
- STEP6-2-2 mapEntriesToCalcInput() A안 확정 · 맞춤가산 MVP=단일 수당만 허용
- STEP6-2-3 History 저장 구조 검증 완료
- STEP6-2-4 근무지합산 알고리즘 검증 완료

상세: archive/current-step-retired.md 참조
