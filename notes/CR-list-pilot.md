# Change Requests from OR-0000 Pilot

## CR-001

```
Change ID: CR-001
Parent ID: FR-0002 / Root Pilot ID: PI-0000 / Related IDs: FR-0001
Origin ID: FR-0001, FR-0002 (두 Claim 결과 대조에서 발견)
Target ID: T-P2-1 Evidence Plan Template
대상: Template
변경 사유: Claim-1(자기평가 단어 탐지→Insufficient)과 Claim-2
  (사건 고유 키워드 탐지→Supported)의 차이가 탐지규칙 설계에서
  갈렸음이 확인됨
Before → After: Evidence Plan에 "탐지 규칙(Method)"란만 있음 →
  "Search Strategy"(사건 고유 키워드/행위 키워드/자기평가
  키워드(보조)/제외 키워드)를 먼저 정의하는 하위 섹션 추가
해결하는 설계결함: 탐지규칙 설계 가이드 부재
적용 시점: 다음 Pilot(Re-Pilot) 또는 정식 OR-0001부터
```

## CR-002

```
Change ID: CR-002
Origin ID: FR-0003
Target ID: T-P1 Source Intake Register 또는 SOP §6 Information Model
대상: SOP/Template
변경 사유: Repository는 Created/Modified만 판정 가능, Withdrawn/
  Verified는 판정 불가(구조적 한계) — 어느 Source가 어느 분류를
  담당하는지 매핑이 없었음
Before → After: "Evidence Source별 담당 분류" 매핑표 추가(예:
  Created/Modified→Repository, Withdrawn/Verified→대화Source
  또는 별도 Audit Log)
해결하는 설계결함: Source-분류 매핑 부재
적용 시점: 다음 Pilot 또는 정식 OR-0001부터
```

## CR-003

```
Change ID: CR-003
Origin ID: WD-0001
Target ID: SOP §16 역할모델 / P4 절차
대상: SOP/운영
변경 사유: 이번 Walkthrough의 재현성 검증이 간이형(단일 Reviewer
  내 관점분리)이었고, 완전한 제3자(GPT) 재현이 아니었음
Before → After: 정식 OR-0001부터는 P4에서 실제 GPT(Second-pass
  Reviewer)의 독립 재현을 필수화
해결하는 설계결함: 재현성 검증의 형식적 수행(실질 미흡)
적용 시점: 정식 OR-0001부터 필수
```

Prepared: Claude / Checked: (대기) / Approved: (대기)
