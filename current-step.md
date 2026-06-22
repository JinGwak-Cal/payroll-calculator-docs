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

현재 단계: STEP6-1 — 연차 개선 (진입 전)
직전 완료: STEP6-2 구현 5/5 — History 저장/복원 연결 + dead component 정리 — 완료 (2606.19)
다음 단계: STEP6-1 착수 — ResultGrid 순서 정렬 · 연차 개선 설계
비고:
- STEP5 결과: ResultGrid 역할 재정의 · Drawer 구조 확정 · RESULT-04/05 제거 확정 · 시나리오 A 확정
- STEP6-2-1~2-5 문서 확정 완료 (저장단위/변환로직/History검증/근무지합산/UI최소명세)
- STEP6-2 구현 1/5: 타입(PremiumAllowanceEntry)·상태(allowanceRows)·변환함수 작성 완료
- STEP6-2 구현 2/5: mapEntriesToCalcInput() 작성, 5인 미만 게이팅 작성 완료 (calc-engine 미수정)
- STEP6-2 구현 3/5: Drawer UI 구현, ResultGrid 연결(탭 진입), PremiumScreen 라우팅 제거 완료
- STEP6-2 구현 4/5: 계산 라이브 연결, premiumHours=총가산시간 확정(D-05-10), timerange 야간 Drawer 우선(D-05-11) 완료
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
| STEP6-2-5 | reviews/active/claude/STEP6-2-5-Drawer-allowanceRows-최소구현명세.claude.현업1-1.260618.md | Drawer/allowanceRows 최소구현명세 |

STEP5 완료 — 참고용 (필요 시)
| 문서ID | 경로 | 용도 |
|--------|------|------|
| STEP5-ResultGrid-Review-01 | reviews/active/claude/STEP5-ResultGrid-Review-01.claude.현업1-1.260615.md | ResultGrid 역할·RESULT-01~05 처리 |
| STEP5-4-Drawer-확정안 | reviews/active/claude/STEP5-4-Drawer-확정안.claude.현업1-1.260615.md | Drawer 구조 확정 |

STEP 전환 시 본 표를 해당 STEP 기준으로 갱신.
표에 없거나 URL 미기재 시 → 사용자에게 1회 요청 후 진행.

---

## 구조3 다음 작업

1. STEP6-1 착수 — ResultGrid 순서 정렬 · 연차 개선 설계
2. STEP6-2 구현 검증
3. STEP6-1 — 연차 개선
4. UI-Audit-05 개정 — Component=Row 신규값 반영

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

### manual-v14 전수조사 결과 (2606.19) — 대기/검토 항목 요약
※ 상세 8필드 내역은 manual-v14.md "분류 이력(2606.19)" 참조

작업확정(구현 결정됨):
- [높음] R15~R17 운영 정착 검증 (2606.22)
  ※ 3회 이상 연속 적용 + 위반 사례 0건 확인 시 제거
- [높음] ResultGrid 순서 정렬 — STEP6-1 첫 작업
- [높음] 대기#5 표준 진입 프롬프트 absolute-rules.md 중복 보관
- [높음] UI-Audit 기반 UI 통일 적용 — 5단계(STEP6-1→ResultGrid→상태유급형→시간속성→전체정리)
- [높음] 모드 확장(2×2 구조) — Jin님 주도, 요구사항 정리부터 시작
- [보통] History UX 개선 STEP 신설 후보: 18-A 저장기록2줄 / 18-B 드래그리오더링
- [보통] 근무지 합산 — 독립 STEP 신설 (18-C)
- [낮음] P-C 가산율 비정수 입력 — 실사용 조사 후
- [STEP6-1 이후] UX-01 세금·공제 아코디언

검토대기(판단 보류, 선행 확인 필요):
- BUG-01 기록보기 저장버튼 토글 오작동
- P9 PremiumRateCard/NightPayCard 실존·참조 확인
- P11/P12 WeekStatus 코드 실존 확인 (절대 임의 폐기 금지)
- UI-L 적용화면 확정 필요 (Known Issue #1)
- Fast Refresh use-calc.tsx (Tech Debt, 기록만)
- Float Drift 전수 검증 (Verification, 누락방지용 — 현재 알려진 버그 없음)
- P-A 기록보기 버튼 실존 확인
- P-B 피드백 기능(구글폼/메일) 작동 확인
- P-D 하단 기능모음 실존 확인
- AI OCR 기반 진입 퍼널 검토 (급여명세서→근로계약서→N잡러, 18-C 이후 사업 확장 후보)

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
- STEP6-2-5 Drawer/allowanceRows 최소구현명세 확정 완료

상세: archive/current-step-retired.md 참조
