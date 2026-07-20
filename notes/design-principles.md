# design-principles.md — 공통 시각 디자인 원칙

## Design Philosophy

- 정보 전달을 장식보다 우선한다
- 구분은 색보다 여백과 위계로 만든다
- 동일한 역할은 동일한 표현을 사용한다
- 값보다 관계를 우선한다

## 이 문서의 성격 — 가설(Hypothesis), 확정 아님

이 원칙들은 아직 앱 전체에 적용이 확정된 게 아닙니다. **같은
내용도 어떻게 보이느냐에 따라 사람 반응이 크게 갈린다**는 전제로,
AllowanceBrowser 하나에서 먼저 테스트합니다. 여기서 실제로
좋은 반응이 나오는지 확인한 뒤에만 다른 화면(BasicWorkBrowser,
History, Dashboard 등)으로 확산 여부를 결정합니다. 지금 이
원칙을 다른 화면에 미리 적용하지 마세요.

이 문서는 특정 화면 전용이 아니라, 검증되면 앱 전체 화면이
재사용할 수 있는 공통 원칙 후보입니다. UI-Audit 프레임워크(전체공통
/기능별/레이어별/Mode 분류)가 정식 분류표로 성숙하기 전까지, 이
문서가 그 "전체공통" 축의 임시 근거 역할을 합니다.

값(정확한 px/색상)이 아니라 **관계**를 우선 규정합니다 — 폰트나
밀도가 바뀌어도 관계는 유지되기 때문입니다.

## 원칙 (관계 중심)

1. **Typography Hierarchy (3단계)**: 본문 > 보조정보 > 안내문구.
   크기·색 대비로 구분하되, 3단계를 넘지 않음
2. **Spacing Rhythm**: Outer Padding > Inner Gap. 같은 레벨의
   요소끼리는 간격을 통일
3. **Contrast 관계**: Card Contrast < Text Contrast (카드 배경
   구분은 은은하게, 글자 대비는 선명하게)
4. **Separator**: 가능한 한 은은한 구분을 우선한다. 필요 시
   0.5px, 1px, opacity 조절 등으로 구현한다 (해상도·플랫폼에 따라
   0.5px 지원이 다를 수 있으므로 값을 고정하지 않음)
5. **Grouping**: Header / Row / Editor 처럼 기능 단위로 명확히
   그룹화, 그룹 간 간격 > 그룹 내 간격
6. **단일 아이콘 패밀리**: 화면 전체에서 아이콘 스타일 하나만 사용
7. **Motion**: 펼침/접힘 등 상태 전환에 짧은(0.1~0.2초) 트랜지션
8. **Density**: 너무 빽빽하지도 너무 넓지도 않게 — 참조: 오늘
   AllowanceBrowser 목업 밀도

## 참고 수치 (기본값, 프로젝트 팔레트에 맞춰 조정 가능)

- Padding: 12~14px / Gap: 8~10px
- Border-radius: 8~12px
- Font: 본문 14px / 보조 12~13px

## 검증 절차 (다음 단계)

1. AllowanceBrowser **목록 화면**(2026-07-17 D-PW-036 재확정 —
   기존 인라인 편집 계획은 폐기, 읽기전용 목록+기존 Drawer 재사용
   구조로 변경) 구현 완료
2. 실제 화면을 보고 반응 확인 (좋아 보이는지, 왜 그런지)
3. 반응이 좋으면 → 다른 화면 확산 검토 (Candidate)
4. 반응이 안 좋으면 → 이 문서를 수정하거나 폐기

## 분류 축 (UI-Audit 프레임워크, 값은 미확정)

Component(Card/Button/...) × Feature(수당근무/기본근무/...) ×
Layer(목록/입력/결과/상세) × **Mode(Viewing/Editing)** — Mode 축은
2026-07-17 AllowanceBrowser 논의에서 추가 제안됨(같은 Card+Feature
라도 Viewing/Editing 간 여백·버튼 배치가 달라질 수 있음)
