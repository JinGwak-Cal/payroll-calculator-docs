# AllowanceBrowser — Specification Contract

> **⚠️ Superseded (2026-07-17)** — 이 Contract의 인라인 편집
> 구조(State Machine/Interaction/Dirty Policy)는 D-PW-036(목록+
> 기존 AllowanceDrawer 재사용)으로 대체되었습니다. 이 문서는
> 기록용으로만 보존합니다. 실제 구현은 D-PW-036을 따르세요.

이 문서는 구현 코드가 아니라 **설계 계약**입니다. TSX/Hooks/실제
타입/import는 Replit Agent가 프로젝트 컨벤션에 맞춰 작성합니다.

## Contract Scope

**변경 가능**: 타입, import, UI 컴포넌트, 프로젝트 컨벤션
**변경 불가**: UX Flow, State Machine, Dirty Policy, Interaction
Rule — 변경이 필요하다고 판단되면 임의로 변경하지 말고 근거와
함께 제안해주세요.

## Props Contract (인터페이스 계약, 실제 타입 아님)

```
AllowanceBrowser(
  rows: PremiumAllowanceEntry[]      // Preflight 확정: id/selectedAllowances/premiumRate/premiumHours
  onSave(id, patch)
  onDelete(id)
  onAdd()
  calcAmount(...) -> amount   // 실제 시그니처는 프로젝트 구조에
                              // 맞게 연결 (Adapter). Contract는
                              // "계산 위임 지점"만 표현
)
```

## 편집 범위 (2026-07-17 P-3 반영, MVP 범위 한정 — 영구 아님)

인라인 편집 가능: **가산시간(premiumHours)만**. 수당종류
(selectedAllowances)·가산율(premiumRate) 변경은 기존 Drawer로
위임 — §6 하드차단(표준↔맞춤 동일 수당 차단) 로직 인라인 복제
회피 목적. **이번 MVP의 검증 범위로 승인된 것이며, Drawer를
영구 존속시키기로 확정한 것은 아님** — Browser+Inline Editor
패턴 검증 후 재검토 대상.

## State Diagram

```
Empty ──(rows.length > 0)──> Viewing
Viewing ──(행 탭)──> Editing(rowId)
Editing ──(재탭, dirty=false)──> Viewing
Editing ──(재탭, dirty=true)──> Confirming(rowId)
Confirming ──(저장)──> Viewing (onSave 호출)
Confirming ──(취소)──> Editing (draft 유지, 확인만 닫힘)
Editing ──(저장 버튼)──> Viewing (onSave 호출, dirty 무관)
```

## Sequence — 행 펼침→저장

```
1. 사용자가 행 탭
2. snapshot = 현재 row 값 저장
3. draft = snapshot 복사, 입력 필드에 바인딩
4. 사용자가 가산시간 수정 → draft.hours 갱신
5. liveAmount = calcAmount(draft.hours, row.type) → 화면에 즉시 반영
6. "저장" 탭 → onSave(row.id, draft) 호출 → Viewing 복귀
```

## Sequence — 행 접기 (Dirty 체크)

```
1. 사용자가 같은 행 재탭
2. dirty = normalize(draft) != normalize(snapshot)
   - normalize: trim, 숫자형 변환, "의미가 같은 값은 같은 값"
   - 비교 대상: hours, memo (amount는 파생값이라 제외)
3. dirty == false → 즉시 Viewing 복귀
4. dirty == true → Confirming 상태로 전환 (저장/취소 노출)
```

## UX 규칙 (Specification Contract — 변경 시 근거와 함께 제안)

- Header: Sticky 고정 + 우측 "+추가"
- 정렬: 최근수정순, 번호 고정(삭제돼도 재번호 없음)
- Empty: 별도 화면 없이 곧장 편집 상태로 진입
- 편집 상태 주 액션: 저장/취소 (편집 버튼 없음 — 이미 편집 중이므로)
- 삭제: 주 액션과 시각적으로 분리된 보조 액션 (크기 강제 없음,
  터치 영역 축소 금지)
- 계산금액: 실시간 계산 결과 표시
- 아이콘 배치 근거: `src/components/history/HistoryScreen.tsx` 선례
  (Star/Trash가 행 안, 우측)

## Design Reference

본 화면은 `design-principles.md`를 따른다.

Classification: Component(Card) × Feature(수당근무) ×
Layer(목록/편집) × Mode(Viewing/Editing)

## Pseudocode (참고용, 실제 Hooks 아님)

```
on rowTap(row):
  if expandedId == row.id:
    if isDirty(draft, snapshot): showConfirm()
    else: collapse()
  else:
    expand(row); snapshot = row; draft = row

on save(row.id, draft):
  onSave(row.id, draft)
  collapse()
```

## Acceptance Criteria

- [ ] Header는 Sticky로 동작한다
- [ ] "+추가" 버튼이 항상 Header 우측에 표시된다
- [ ] Empty 상태에서는 즉시 추가(편집) 흐름으로 진입할 수 있다
- [ ] 행 탭 시 인라인 편집이 열린다
- [ ] Dirty가 없으면 재탭 시 즉시 접힌다
- [ ] Dirty가 있으면 Confirming 상태가 나타난다
- [ ] 저장 시 onSave(id, draft)가 1회 호출된다
- [ ] 계산 결과는 입력 변경 즉시 갱신된다
- [ ] 삭제는 저장/취소와 시각적으로 분리된 보조 액션으로 표시된다
- [ ] 기존 ResultGrid → onPremiumRowTap 동작은 유지된다 (대체 아님)
- [ ] 동시에 하나의 Row만 Editing 상태를 가질 수 있다 (아코디언)
