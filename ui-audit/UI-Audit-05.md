# UI-Audit (05. 분류체계 확정)

- **문서 종류**: UI 인덱싱 분류체계 정본(正本) — 이후 모든 UI 분류·치환·토큰의 기준
- **버전**: 05-분류체계확정-검증반영 (C안 + 검증원칙 X-1~4 + 제거우선 X-5~6)
- **작성**: Claude (현업1-1 협업, GPT안 통합)
- **기준 시각**: 2606.13
- **상위 참조**: UI-Audit(03 원칙)·(04 토큰계층)·(06 디자인언어)
- **무결성 규칙**: 모든 UI는 Type×Component×Feature×Layer 4축 주소를 반드시 가진다.
  주소를 부여할 수 없는 UI는 **미분류 큐**에 등록하고, 공통 UI 치환을 진행하지 않는다.
  Emphasis·Status·Signature·Notes·Lifecycle은 주소가 아니라 태그/속성으로 관리한다.

> ⚑ **manual 반영 필수**: 본 문서의 Lifecycle·Signature·Notes 정의와 값 목록은
> 추후 manual 업데이트에 반드시 포함할 것. (현업1-1 지시, 2606.13)
> ※ Interaction은 Type이 흡수하므로 독립 속성에서 제거 (C안, 2606.13).

---

## 1. 주소 = 4축 인덱싱 (Type × Component × Feature × Layer)

UI의 **정체성**. 사용자가 무엇을 하든 변하지 않는다.

### 1축 Type — "이 UI는 무슨 일을 하는 존재인가" (상호작용 성격 내포)
Input · Display · Action · Navigation · Feedback · Overlay · System

> Type은 *분류(Classification)*인 동시에 **상호작용 유형(Interaction)을 내포**한다.
> (예: Input=값 입력 / Display=정적 표시 / Action=실행 / Navigation=이동.)
> 따라서 Interaction은 독립 속성으로 두지 않고 Type이 흡수한다. (C안, 2606.13)

### 2축 Component — "이 UI는 어떤 모양인가"
Card · Button · Input · Chip · Toggle · Tab · Drawer · Amount · Note · Label · Divider · Header

### 3축 Feature — "이 UI는 어느 기능에 속하는가"
Global · WorkInput · Premium · WeeklyHoliday · AnnualLeave · Tax · Insurance · History · Simulator · Share · BusinessScale

### 4축 Layer — "사용자가 어느 화면 단계에서 보는가"
Input · Result · Detail

> ✅ **LAYER-OVERLAP 해소 (2606.13)**: 'Overlay'·'System'을 Layer축에서 제거.
> 두 값은 Type축이 전담 → 같은 단어가 두 축에 겹치는 문제 제거.
> Drawer 내부 내용은 Layer=Input/Detail로 분류, Drawer 컨테이너 자체는 Type=Overlay.

### 인덱싱 예시
| UI | Type | Component | Feature | Layer |
|----|------|-----------|---------|-------|
| 실수령액 표시 | Display | Amount | Global | Result |
| Premium Drawer | Overlay | Drawer | Premium | Detail |
| 주휴 선택 카드 | Input | Card | WeeklyHoliday | Input |
| Toast | Feedback | Note | Global | Result |
| StickyHeader | System | Header | Global | Result |

> Layer는 "보이는 화면 단계"만 표현(Input/Result/Detail). UI의 존재 목적(Overlay/Feedback/System)은 Type이 담당.

---

## 2. 태그 = 표현 속성 (변하거나 시선용)

### Emphasis — 시선 우선순위 (고정 속성)
Primary · Secondary · Tertiary
- 예: 실수령액=Primary / 주휴금액=Secondary / 안내문=Tertiary
- 레벨4 레이어 토큰의 위계 결정에 직결.

### Status — 현재 동작 상태 (가변 속성)
Default · Selected · Disabled · Loading · Error · Success
- §원칙-7 준수: **색이 아닌 폰트·테두리·명암으로 표현** (의미색 Emerald/Red/Amber 제외).

---

## 3. 속성 4영역 구조 (C안 확정)

UI의 정보는 종류가 다른 4영역으로 관리한다. 섞지 않는다.

| 영역 | 항목 | 질문 |
|------|------|------|
| 주소(Identity) | Type·Component·Feature·Layer | 너는 누구냐 (분류) |
| 태그(Presentation) | Emphasis·Status | 지금 어떻게 보이냐 (표현) |
| 설계(Design) | Signature·Notes | 왜 이렇게 만들었냐 (설계 의도) |
| 관리(Management) | Lifecycle | 구현 어디까지 됐냐 |

### Signature — 이 UI를 무엇으로 기억해야 하는가 (설계 의도, 단 하나)
- 예: 실수령액=큰 숫자 / Chip=선택 여부 / Warning Note=주의성.
- **Type(분류)과 종류가 다른 정보다.** Signature는 분류가 아니라 *설계 의도*이므로
  Type에 흡수하지 않고 독립 칸으로 명시한다 → 미구현 UI의 **설계 계약서** 역할.
- 구현자는 이 한 값만 지키면 됨. 잘못 잡으면 한 줄 수정으로 교정.

### Notes — 예외·주의·제약 (운영 지침)
- 예: "이 Drawer는 모바일 우선 / 3줄 이상 금지".
- 분류도 설계도 아닌 *운영 메모*라 독립 유지.

### Lifecycle — 구현 생애주기
Planned · Built · Redesign · Removing
- Removing 항목은 좌표 부여 생략(작업 낭비 차단).

> ※ **Interaction 제거**: 상호작용 유형은 Type이 흡수(§1 참조). 독립 속성 아님. (C안)

---

## 4. UI Spec Card 템플릿 (미구현 UI 선분류용)

구현 전에도 채울 수 있는 필드로만 구성 → 구현 즉시 토큰 자동 상속.

```
① UI ID
② 한 줄 기능 정의
[주소]   ③ Type  ④ Component  ⑤ Feature  ⑥ Layer
[태그]   ⑦ Emphasis  ⑧ Status
[설계]   ⑨ Signature  ⑩ Notes
[관리]   ⑪ Lifecycle
```
※ Interaction 칸 없음 — Type이 흡수(C안). 11필드.

---

## 5. 미분류 큐 규칙
- 4축 좌표를 하나라도 부여 못 하면 → 미분류 큐 등록 → 해당 UI 치환 **중단**.
- 큐 항목은 축 값 보강 또는 신규 값 제안으로 해소 후 재진입.

---

## 6. 치환 기준 (공통 컴포넌트화)

### 치환 대상
앱 곳곳에 하드코딩된 산재 스타일. (전수조사 "정리 필요 후보" = 1차 치환 큐: PerDayInput·ResultGrid·StickyHeader 등)

```jsx
// before
<div className="rounded-2xl border-gray-100 px-4">

// after — 좌표(주소)를 props로 전달, 컴포넌트가 토큰을 조회·적용
<AppCard type="display" component="card"
         feature="weeklyHoliday" layer="result"
         emphasis="secondary" status="default" />
```

### 효과
"Result Layer의 Card padding 전부 축소" → 개별 파일 수정 없이 **토큰 단일 원천 1곳**만 변경.

---

## 7. 색상 체계 (UI-Audit 06 연동)

| 구분 | 색 | 사용 위치 | 비고 |
|------|----|-----------|----|
| Primary Brand | **Blue-Gray** | 헤더·포커스·주요강조 | "일상복" / 신뢰·차분·전연령 |
| 보조 강조 | **Indigo** | Drawer헤더·특별기능·시뮬레이터·강조카드 | "정장" |
| 의미색(불변) | Emerald | 실수령 | 의미 절대 불변 |
| 의미색(불변) | Red | 공제 | 의미 절대 불변 |
| 의미색(불변) | Amber | 주의 | 의미 절대 불변 |

> ✅ **SELECT-COLOR 해소 = A안 확정 (2606.13)**: 선택 상태(Status=Selected)는 **색 사용 금지**.
> 명암·테두리·폰트로만 표현(§원칙-7 준수). Blue-Gray는 선택상태가 아니라 브랜드/포커스/주요강조에만 사용.
> → "깔끔·정돈" 목표와 정합.

---

## X. 벤치마킹 검증을 통해 확인된 추가 원칙 (2606.13 반영)

### X-1. 4축 체계의 성격 — 발명이 아니라 재구성
4축(Type×Component×Feature×Layer)은 프로젝트 내부 발명이 아니라,
**업계 표준 디자인 시스템 구조를 프로젝트 규모에 맞게 재구성**한 것이다.
- Apple HIG 검증: Type·Component·Layer 축 대응 개념 모두 존재.
- Toss(TDS) 검증: Feature 축 실재 / Component 통일 / Emphasis 위계 모두 확인.
→ 4축은 임시 설계안이 아니라 **장기 유지 가능한 분류체계**로 간주한다.

### X-2. UI 생성 순서 원칙 — 주소 → 설계 → 상태
UI는 항상 아래 순서로 정의한다.
1. 주소(Type / Component / Feature / Layer)
2. 설계(Signature / Notes)
3. 상태(Status)
- Status는 **마지막** 단계에서 부여한다. Status를 먼저 설계하지 않는다.
- (Toss 컴포넌트 가이드가 상위옵션→요소→상태변화 순으로 점층 구성된 것과 동형.)

### X-3. 미구현 UI 설계 원칙
미구현 UI도 구현 전부터 주소와 설계를 가진다.
- 구현 후 분류가 아니라: **주소 정의 → Signature 정의 → 구현** 순.
- 모든 신규 UI는 **Spec Card를 먼저 작성**한다.

### X-4. 미분류 금지 원칙 (예외 없음)
4축 주소를 부여할 수 없는 UI는 **구현 대상이 아니다.**
- 미분류 큐에 등록 → 분류 확정 후 진행. 예외 없음.

### X-5. 제거 우선 원칙 (철학)
UI 개선은 **추가보다 제거를 우선**한다.
신규 UI 생성은 최후의 수단으로 간주한다.
- 상세 절차는 **§X-6**을 따른다. (본 항목은 원칙 선언만, 단계는 X-6이 정본)
- 근거: Apple HIG 검증 결과 (06 §6-6).

### X-6. UI 단순화 검토 절차 (정식 절차)
UI 개선 시 다음 순서를 따른다. (이 5단계가 "추가보다 제거"의 유일한 정식 절차)
1. 제거 가능 여부
2. 기존 UI와 통합 가능 여부
3. 표현 단순화 가능 여부
4. 위치 이동 가능 여부
5. 신규 UI 추가 ← 마지막 단계에서만 검토

> 위치 이동(4단계)은 반드시 유지. Premium·ResultGrid·History 등은 새 카드 추가보다
> 위치 이동으로 해결될 가능성이 높다.

**우선 제거 검토 대상:**
- 중복 설명
- 중복 요약
- 동일 의미 색상 (§원칙-2)
- 장식성 아이콘
- 중복 카드
- 불필요한 Divider
