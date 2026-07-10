# context-history.md

> 새 세션에서 Event를 추가할 때마다, 아래처럼 **세션 배치 헤더**를
> 하나 새로 만들고 그 아래 Event들을 넣는다. 파일 전체에 한 번만
> 적는 게 아니라, 배치가 바뀔 때마다 새로 추가한다.

---

## 배치: 2026-07-10/11

**Source Threads**
- Claude: 본 쓰레드 (0703 CostMangm.Prtl.시작 계열, 0710 작업분)
- GPT: 0706_3_AI_WorkBench

역할: GPT=설계/방향, Claude=구현/검증(grep·clone·repo 대조).

---

## E-011 — 기본값 교정표(Default Correction Table) v6 확정

### 메타
- Event ID: E-011
- Date: 2026-07-10/11
- Status: Confirmed

### ① 발생
- Event Label: 기본값 교정표(Default Correction Table) v6 확정
- Background: 프로젝트 지식에 오래된 v3가 방치된 채(오타 포함) 실제로는 반영이 안 되고 있었음을 발견. GPT 쪽(0706 쓰레드)에서도 같은 파일을 병행 검토 중이었음.

### ② 의도
- Purpose: 표가 "체크리스트"로 비대해지는 것을 막고, 실제로 행동을 바꾸는 규칙만 남긴다
- Why: "저장≠적용" 문제가 교정표 자신에게서도 반복됨을 확인했기 때문

### ③ 결정
- Decision: v6 확정 — 발송 전 전체 점검(0번, 표 전체 대상으로 일반화), 완료보고/Mapping/규칙제안/Activation 4개 행 복원, 참조자료·풀센텐스·기존결정확인·용어병기 유지
- Deprecated/Changed: "0번=새용어 표현점검"이라는 좁은 정의는 폐기, "0번=표 전체 자기점검"으로 교체. GPT는 "용어병기는 Handbook행"이라 주장했으나 기각(사용자가 재차 반박)

### ④ 근거
- Assumption: 표는 "많을수록 좋은 게 아니라, 실제 실수를 막는 최소집합"이어야 한다
- Evidence: 이 쓰레드 내 v3→v6 반복 편집 기록, GPT 쓰레드 7641~7945행(동일 주제 병행 검토)

### ⑤ 영향
- Impact: 다음 쓰레드부터 파일(지식) 재업로드 필요(v6로 교체)
- Open Items: [미착수] GPT가 제안한 "8/9번 통합", "6번 일반화"는 이번 v6에 미반영 — 다음 개정 후보
- 유의점: 프로젝트 지식은 자동 갱신 안 됨, 매번 수동 재업로드 필요

---

## E-012 — STEP2 수당근무목록 화면(Browser) 미구현 확인

### 메타
- Event ID: E-012
- Date: 2026-07-09/10
- Status: Confirmed

### ① 발생
- Event Label: STEP2 수당근무목록 화면(Browser) 미구현 확인
- Background: STEP2(AllowanceRecord Browser/수당근무 목록) 복귀 시 Editor/Browser/Dashboard 관계가 불명확해 다수 문서를 대조해야 했음

### ② 의도
- Purpose: STEP2의 실제 진행 상태를 정확히 파악해 재작업 없이 복귀
- Why: 문서(D-PW-009)와 실제 구현(ResultGrid→Drawer 직행)이 서로 다른 시점의 결정이라 충돌했기 때문

### ③ 결정
- Decision: STEP2 = Editor(AllowanceDrawer) 완료 / Browser 미구현. 진입경로는 ResultGrid 버튼("전체보기")으로, 삭제는 목록에서 바로(확인단계 포함)로 결정
- Deprecated/Changed: D-05-09("ResultGrid→Drawer 단일진입")는 D-PW-009(6/26)가 이미 폐기했음을 확인. 이 폐기 사실이 문서에 명시 안 돼 있어 오늘 재확인 작업이 발생

### ④ 근거
- Assumption: Presentation 설계를 별도 STEP으로 안 벌리고, UX 3개 결정(형태/진입/삭제)만 내리고 바로 구현으로 감(출시 우선 전략과 일치)
- Evidence: Replit 조사 결과(AllowanceDrawer.tsx 완료, Browser 미구현), decisions.md D-PW-022/024, manual-v14.md 수당순서, ui-audit 라인1849

### ⑤ 영향
- Impact: 다음 Replit 프롬프트는 AllowanceBrowser(가칭) 신규 구현으로 바로 진행 가능
- Open Items: [미착수] 수당 표시순서(주휴→연차→연장→야간→휴일→공제) 정렬이 Row순서 재정렬보다 선행되어야 함(ui-audit 기존 지침)
- 유의점: 파일명(AllowanceBrowser.tsx 등)은 아직 확정 아님 — 구현 단계에서 결정

---

## E-013 — GPT 클로징 작업흐름(Closing Workflow) 단순화

### 메타
- Event ID: E-013
- Date: 2026-07-10
- Status: Confirmed

### ① 발생
- Event Label: GPT 클로징 작업흐름(Closing Workflow) 단순화
- Background: GPT 전용 클로징 체크리스트(notes/gpt-closing-checklist.md)를 별도로 만들려다, "왜 두 번 하나"는 지적으로 방향 전환

### ② 의도
- Purpose: GPT에게 새로운 절차 부담을 주지 않으면서도 원문을 보존
- Why: GPT 스스로 "압축된 Evidence를 선호한다"고 밝혔고, 5/29 GPT 체크리스트 시도가 실제로 하루 만에 중단된 전례가 있었기 때문

### ③ 결정
- Decision: GPT는 평소대로 대화만 하고, 종료 시 사용자가 원문을 복사해 Claude에게 전달 → Claude가 Corpus 저장+Evidence/Decision 추출까지 통합 수행
- Deprecated/Changed: notes/gpt-closing-checklist.md 신규 생성 계획 폐기

### ④ 근거
- Assumption: Claude가 GitHub 쓰기 권한이 없으므로, Corpus 저장소 반영의 마지막 단계는 사용자가 수행
- Evidence: reviews/active/gpt 폴더가 5/29 이후 정지된 사실(실측), 0706 GPT 쓰레드에서도 같은 결론 도달(7264행 이하)

### ⑤ 영향
- Impact: 앞으로 GPT 대화 종료 시 "원문 복사→Claude 전달"이 표준 절차가 됨(이번이 첫 실행)
- Open Items: [미착수] Corpus 전용 비공개 GitHub repo 아직 미생성, [미착수] absolute-rules.md Thread Closing Review 섹션 갱신 아직 미반영
- 유의점: 개별 스레드 export 기능이 Claude/GPT 둘 다 없어 수동 복사(Ctrl+A)에 의존 — 대용량 쓰레드는 잘림 위험

---

## E-014 — 문서 구조(Documentation Architecture) 재편 — Threshold Foundry 엔진 중심

### 메타
- Event ID: E-014
- Date: 2026-07-10
- Status: Confirmed

### ① 발생
- Event Label: 문서 구조(Documentation Architecture) 재편 — Threshold Foundry 엔진 중심
- Background: 개발/운영 문서가 계속 늘면서 실효성 확인이 필요해짐

### ② 의도
- Purpose: 문서를 "몇 개 있는가"가 아니라 "선순환 엔진에서 무슨 역할을 하는가"로 재분류
- Why: 초기 분류(9개 카테고리)가 문서분류와 엔진역할을 섞어놨다는 지적(GPT 및 사용자 공통) 반영

### ③ 결정
- Decision: Threshold Foundry를 상위 엔진, Paycheck Workbook을 첫 Case Study로 재정의. CASE(개발소스8+Evidence28) vs ENGINE(구조화45+운영14+대기4+은퇴7+저장소7) 구조 확정
- Deprecated/Changed: 이전 "9개 병렬 카테고리"안 폐기(개발과 운영 성격이 섞여 있었음)

### ④ 근거
- Assumption: 개념체계(34개 중 25개 Candidate 정체)와 리뷰(28개 정지)가 멈춘 건 문서체계 결함이 아니라 개발활동 자체가 멈춘 파생효과
- Evidence: git log 실측(concept-system 7/02 이후 무변화, reviews 6/20·5/29 이후 무변화), 중복파일 2건 발견(02-concept-manual.md, 깨진 archive 폴더)

### ⑤ 영향
- Impact: 향후 문서 추가 시 "이건 Case용인가 Engine 공통인가"부터 구분
- Open Items: [보류] 정리대상 2건(중복/깨진폴더) 삭제 여부는 진님 판단 대기, [미착수] 개념카드 34개 중 실제 사용된 것만 골라 승격심사
- 유의점: 문서 URL에 괄호/공백 있으면 마크다운 링크가 깨질 수 있어 %인코딩 필요

---

## E-015 — 이벤트 카드 양식(Event Card Template) 확정

### 메타
- Event ID: E-015
- Date: 2026-07-11
- Status: Confirmed

### ① 발생
- Event Label: 이벤트 카드 양식(Event Card Template) 확정
- Background: 통합 클로징 리뷰의 마지막 단계(실제 파일 반영)가 계속 미뤄지다가, 쓰레드가 길어져 지금 실행 결정

### ② 의도
- Purpose: 이번 쓰레드 전체의 미처리 작업이 유실되지 않고 다음 쓰레드로 이어지게 함
- Why: 클로드/GPT 각자 안을 티키타카 검토(중복 재작명 다수 발견·기각)한 뒤 통합

### ③ 결정
- Decision: Event Card 11항목/5클러스터(발생·의도·결정·근거·영향) 확정. Trigger는 Background에 흡수, Open Items/보류사항은 태그로 통합
- Deprecated/Changed: GPT가 제시한 단순화된 9필드 템플릿(Event ID/Title/Date/Trigger/Evidence/Decision/Impact/Related Documents/Status)은 기각 — 협상 완료된 6개 필드(Purpose/Why/Deprecated/Assumption/Open Items/유의점)를 무단 누락했기 때문

### ④ 근거
- Assumption: 이 카드 형식이 앞으로 모든 Event 기록의 표준이 된다
- Evidence: 본 쓰레드 전체(교정표 v3~v6 협상 과정), GPT 쓰레드(0706) 동일주제 병행기록

### ⑤ 영향
- Impact: 다음 쓰레드는 이 5건(E-011~E-015)부터 확인하고 시작
- Open Items: [미착수] decisions.md D-TF-002~005 반영, current-step.md 우선순위 재정렬, absolute-rules.md Thread Closing Review 섹션 갱신, Corpus 비공개 repo 생성 — 전부 다음 작업으로 이월
- 유의점: 이번 리뷰는 Claude 쓰레드+GPT 0706 쓰레드만 대상. 0627 Paycheck Workbook 전환 원문은 아직 미확보 상태로 별도 남음
