# TTP v1.0 — Thread Transition Protocol

본 문서는 운영 정책(Policy)와 운영 절차(Procedure)를 함께 정의한다.
각 절의 역할은 독립적으로 관리되며, 정책과 절차는 필요에 따라
각각 변경될 수 있다.

작성일: 2026-07-17
Pilot: Operational Case #1 (D-PW-034 Layout Refactoring + TTP 자기적용)

## 1. Purpose
TTP는 Thread Transition 과정에서 각 단계의 진입, 기존 SOP의 호출,
성공검증, 다음 단계 Trigger를 오케스트레이션하는 프로토콜이다.
Thread 종료 이후에도 SoT와 작업 컨텍스트의 일관성을 유지하며,
다음 Thread가 동일한 기준선(Baseline)에서 시작되도록 보장한다.

## 2. Scope
Thread 종료 판단 시점 ~ 다음 Thread 시작 직전까지.
생명주기: Entry → Work → Exit Condition → Exit
- Scope Summary / Scope Entry Event / Scope Exit Condition
  (목적 달성+Scope밖 항목 분리+Bridge 준비완료) / Scope Exclusion

## 3. Procedure
Thread Work → Closing Review → Delivery → Freeze
→ Trigger Detection → Addendum(필요시) → Exit Condition PASS
→ Bridge(필요시) → Next Thread Baseline 확정

Execution Resume Trigger: 새 론점 발생 시, 현재 단계 성공검증에
필요한 정보인지 먼저 판정 후 아니면 Backlog로.

오케스트레이션 원칙: TTP는 각 단계를 직정 정의하지 않고, 각 단계가
호출하는 기존 SOP(TCA, Delivery SOP 등)의 실제 수행 여부만 검증한다.

## 4. Relationship
기존 자산(Closing Review/Delivery Closing/Pilot/Freeze Point/
Trigger/Addendum/Bridge)을 매핑, 대체하지 않고 역할만 재구성.
신규 번호체계 없음, Evidence는 기존 Event Card(E-XXX) 참조.

## 5. Trigger
원칙: Freeze 이후 Baseline 변경 여부
사례: main 미반영 지속 / SoT 신귔 결정 / current-step 시작조건
변경 / Scope Drift(Thread 종료범위 넘어 새 독립작업 시작)

## 6. Validation (지속 수집)
Closing 누락 / Addendum-Trigger 대응 / Bridge 품질 /
Output-Outcome PASS 일치 / Boundary Drift 건수 / 탐색비용 / 재작업회수

Success Classification: Complete PASS(Output+Outcome 완룼) /
Deferred PASS(일부만 완룼, 나머지는 다음 Scope 검증 — Closing 안막음) / Fail

Validation Matrix(Pilot 관찰용, 의무아님): 막힌 셀만 기록,
반복사용 셀만 v1.1 승격. Bridge Validation Level(L1/L2/L3)은
v1.1 연구단계 유보.

## 7. Pilot History
Operational Case #1 = 본 스레드
Closing Review: Complete / Delivery: Deferred(이월) / Freeze: Complete
/ Trigger: Complete / Addendum: Complete / Bridge: Deferred PASS

## 8. Backlog
Question-Centric Review SOP / Review Coverage Check / Outcome First
Rule / Execution Resume Trigger 정식편입 여부 / Bridge Level 일반화
여부 / Validation Matrix 셀 축소
