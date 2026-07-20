# AllowanceBrowser 구현 요청

이번 작업은 AllowanceBrowser를 프로젝트 컨벤션에 맞게 구현하는 것입니다.

아래 내용은 구현 코드가 아니라 **설계 계약(Contract)**입니다.

React / TypeScript / Hooks / import / Component 분리 등은 프로젝트 컨벤션에 맞게 작성해주세요.

────────────────────────────────────
작업 원칙
────────────────────────────────────

이번 구현은 AllowanceBrowser 하나를 만드는 것이 목적이 아닙니다.

앞으로 BasicWorkBrowser, History, Dashboard, ResultGrid 등으로 확장될 Browser UI의 첫 번째 Baseline을 만드는 작업입니다.

반복 가능한 패턴을 발견하면 적극적으로 제안해주세요.

단, Contract는 임의 변경하지 말고 반드시 "제안" 형태로 알려주세요.

────────────────────────────────────
Contract Scope
────────────────────────────────────

변경 가능
- 타입
- import
- Hooks
- Component 분리
- 프로젝트 컨벤션 적용
- 스타일 구현 방식

변경 불가
- UX Flow
- State Machine
- Dirty Policy
- Interaction Rule
- Acceptance Criteria

Contract 변경이 필요하면 구현하지 말고 근거와 함께 먼저 제안해주세요.

────────────────────────────────────
Preflight (구현 전 확인, 먼저 이것부터 보고)
────────────────────────────────────

1. AllowanceRow 실제 타입/인터페이스와 전체 필드
2. 가산시간 입력에 현재 적용 중인 Validation(음수 금지/최대값/빈값 처리 등). 없으면 "없음"이라고 답변
3. AllowanceRow가 고유 id를 갖는지. 없다면 현재 무엇으로 Row를 식별하는지
4. 프로젝트에서 사용하는 Button/Input 등 UI Primitive 대표 파일 경로
5. calc-engine에서 이번 화면에 연결할 가장 적절한 함수
6. ResultGrid에서 "전체보기" 진입점을 어느 위치에 추가하는 것이 적절한지
7. HistoryScreen Row Action(편집/삭제 배치)을 그대로 재사용 가능한지

Preflight 확인 후 구현을 시작해주세요.

────────────────────────────────────
Design Reference
────────────────────────────────────

이번 화면은 첨부한 design-principles.md를 기준으로 구현해주세요.

**단, 이 원칙은 아직 확정된 공통 규칙이 아니라 AllowanceBrowser
하나에서 먼저 검증하는 가설입니다. 다른 화면(BasicWorkBrowser,
History, Dashboard 등)에 미리 적용하지 마세요.** 구현 완료 후
실제 화면이 어떻게 보이는지 확인한 다음에만 확산 여부를
결정합니다.

Design Philosophy
- 정보 전달을 장식보다 우선한다
- 구분은 색보다 여백과 위계로 만든다
- 동일한 역할은 동일한 표현을 사용한다
- 값보다 관계를 우선한다

Design Principles
- Typography Hierarchy (3단계)
- Spacing Rhythm
- Contrast
- Separator
- Grouping
- Single Icon Family
- Motion
- Density

Classification
Component(Card) × Feature(수당근무) × Layer(목록/편집) × Mode(Viewing/Editing)

색상은 기존 프로젝트 다크모드 팔레트를 사용하고, 원칙만 적용해주세요.

────────────────────────────────────
AllowanceBrowser Specification Contract
────────────────────────────────────

Props
```
AllowanceBrowser(
  rows: AllowanceRow[]
  onSave(id, patch)
  onDelete(id)
  onAdd()
  calcAmount(hours, type)
)
```
※ 실제 타입은 프로젝트에 맞게 연결

State
```
Empty → Viewing → Editing(rowId) → Confirming → Viewing
```

Interaction
```
행 선택 → snapshot 생성 → draft 생성 → 편집 → 실시간 계산(calcAmount) → 저장 → collapse

같은 행 재선택 → Dirty 검사
  Dirty 없음 → collapse
  Dirty 있음 → Confirm
```

Dirty Policy
```
normalize 후 비교
normalize: trim / 숫자형 변환 / 의미가 같은 값은 동일
비교 대상: hours, memo
비교 제외: amount (파생값)
```

UX Rules
- Header Sticky
- 우측 +추가 버튼
- Empty 상태에서는 바로 편집 시작
- 편집 중에는 저장/취소 표시, Edit 버튼 없음
- 삭제는 저장/취소와 시각적으로 분리된 보조 액션
- 계산 결과 실시간 갱신
- HistoryScreen Row Action 패턴 참고
- 기존 ResultGrid → onPremiumRowTap 흐름 유지

Acceptance Criteria
```
□ Header Sticky
□ +추가 버튼 표시
□ Empty → 편집
□ Row Tap → Inline Editing
□ Dirty 없으면 즉시 Collapse
□ Dirty 있으면 Confirm 표시
□ 저장 시 onSave(id, draft) 1회 호출
□ 계산 결과 실시간 갱신
□ 삭제는 보조 액션
□ ResultGrid → onPremiumRowTap 유지
□ 동시에 하나의 Row만 Editing 상태를 가진다 (Accordion)
```

────────────────────────────────────
구현 완료 후 보고
────────────────────────────────────

다음 형식으로만 보고해주세요.

```
Modified Files
...

Created Files
...

Acceptance Checklist
☑ ...

Known Limitations
...

Improvement Suggestions
...
```
