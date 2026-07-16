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
- Evidence: reviews/active/gpt 폴더가 5/29 이후 정지된 사실(실측), 0706 GPT 쓰레드 1609·2243행 — "저는 긴 원문 전체보다 '검증된 운영 문서'를 중심으로... 압축된 사실(Evidence)을 반복 참조할 때 훨씬 일관성이 높아지기 때문입니다"(GPT 본인이 직접 밝힌 원문 선호도)

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
- Open Items: [완료] decisions.md D-TF-002 반영, current-step.md 우선순위 재정렬, absolute-rules.md Thread Closing Review 섹션 갱신 — 본 배치 내에서 처리됨. Corpus 운영방식은 E-016 결정에 따라 추후 병목 발생 시 재검토(신규 repo 생성 아님)
- 유의점: 이번 리뷰는 Claude 쓰레드+GPT 0706 쓰레드만 대상. 0627 Paycheck Workbook 전환 원문은 아직 미확보 상태로 별도 남음

## E-016 — Corpus 저장방식 논의 및 보류 결정

### 메타
- Event ID: E-016
- Date: 2026-07-11
- Status: Confirmed

### ① 발생
- Event Label: Corpus 저장방식 논의 및 보류 결정
- Background: Paycheck Workbook/Threshold Foundry 설계와 원문 대화가
  전부 Public GitHub에 노출되어 있다는 사실을 확인한 뒤, 원문(Corpus)
  보존 방식(GitHub Public/Private+PAT/Private+Replit/Google Drive
  MCP)을 검토.

### ② 의도
- Purpose: 보안(비공개)과 Claude의 자율적 접근(검증) 둘 다 잃지 않는
  저장방식을 찾는다.
- Why: Private로 하면 Claude의 bash clone/grep 접근이 막히고, Public은
  전면 노출된다는 트레이드오프 확인. Google Drive MCP를 실제로
  연동·테스트까지 해봄.

### ③ 결정
- Decision: **네 가지 옵션을 모두 검토한 뒤, 제3의 대안으로 귀결됐다.
  현재는 별도의 Corpus 저장소나 관리체계를 구축하지 않는다. 원문
  Thread는 지금처럼 사용자의 로컬 PC에 Markdown으로 보존하며, Thread
  Closing Review 절차에서 원문 로컬 보존 여부만 확인한다. 향후 원문이
  충분히 누적되어 AI 검색·분석이 실제 병목이 되는 시점에만 Evidence를
  근거로 Corpus 저장방식을 다시 결정한다.**
- Deprecated/Changed: 검토했던 4개 옵션(Public GitHub / Private+PAT /
  Private+Replit경유 / Google Drive MCP) 전부 "지금 실행"에서
  "미래 재검토 후보"로 격하. 그중 "Private+Replit 경유"는 자율성이
  Claude 본인이 아닌 다른 AI로 이전되는 것으로 판명되어 별도 기각.

### ④ 근거
- Assumption: 원문이 이미 로컬에 안전히 있으므로, Corpus 미구축이
  데이터 유실 위험을 만들지 않는다. 오늘 실제 웹UI 개입 사례
  (Description란/토큰페이지/체크박스/Merge) 6건이 전부 clone과
  무관한 것으로 확인되어, Corpus 구축이 오늘 겪은 문제의 해결책도
  아니었음이 드러남.
- Evidence: Google Drive Connector 실측 테스트(파일4~5개, 정확도 확인/
  큰파일 검색누락 확인/전체읽기시 정확 확인/grep과 비용구조 다름 확인)

### ⑤ 영향
- Impact: **Thread Closing Review 수행 시, 원문 Thread가 사용자 로컬
  PC에 Markdown으로 저장되었는지 확인하는 절차를 체크리스트에
  추가한다.** (`notes/thread-closing-checklist.md`/absolute-rules.md
  6줄 확장판에 반영됨)
- Open Items: [보류] Corpus 실제 구축 시점과 방식은 미정, 병목 발생
  시 재논의
- 유의점: "지금 안 만든다"가 "영원히 안 만든다"는 아님 — 재검토 조건
  (수백 개 쓰레드 누적)이 명시되어 있음을 다음 쓰레드가 잊지 않아야
  함. Drive 커넥터는 "전체읽기 명시" 안 하면 큰 파일에서 앞부분만
  봄 — 참고용 실측(그러나 이번 결정으로 당장 사용 안 함).

## E-017 — 통합 클로징 리뷰 "귀속 확인" 단계 도입 및 누락 발견

### 메타
- Event ID: E-017
- Date: 2026-07-11
- Status: Confirmed

### ① 발생
- Event Label: 통합 클로징 리뷰 "귀속 확인" 단계 도입 및 누락 발견
- Background: 사용자가 "기존에 놓친 것들을 모두 정리하자"고 확정했던
  기억을 재확인하려 했으나, 원문 검색 결과 "Deferred 목록"이 아니라
  "이번 쓰레드의 모든 산출물이 어딘가에 귀속됐는지 확인"이라는 상위
  개념이었음을 파트너 검토로 재발견.

### ② 의도
- Purpose: 클로징 리뷰가 각 카테고리(Decision/rule/current-step 등)를
  개별 확인하는 데 그치지 않고, "어디에도 안 들어간 것"이 있는지
  마지막에 한 번 더 점검하게 한다.
- Why: 카테고리별 체크만으로는, 애초에 어느 카테고리에도 안 들어가는
  성격의 결정(오늘의 "출시우선/전면공개" 전략 같은 것)이 조용히
  누락될 수 있음을 실제로 확인함.

### ③ 결정
- Decision: absolute-rules.md Thread Closing Review 체크리스트 맨
  끝에 "이번 쓰레드에서 나온 모든 논의·결정이 위 항목들 중 어딘가에
  귀속됐는가?" 확인 단계를 추가한다. 이 확인 과정에서 실제로 누락
  하나(D-TF-003, 출시우선+전면공개 원칙)를 발견해 즉시 기록했다.
- Deprecated/Changed: 없음(기존 체크리스트를 대체하지 않고 마지막
  한 줄만 추가)

### ④ 근거
- Assumption: 카테고리별 체크리스트는 "이미 알려진 종류의 산출물"만
  잡아내고, 범주 자체가 새로운 것(오늘의 전략 결정처럼)은 못 잡는다.
- Evidence: decisions.md/context-history.md 검색 결과, "출시우선+
  전면공개" 결정이 E-012·E-016에 전제로만 스쳐 지나갔을 뿐 독립
  기록이 없었음(실측 확인). GPT 원문(0706)에서는 이 "귀속" 개념
  자체에 대한 사전 논의를 찾지 못함 — 이번에 새로 제안된 것으로 판단.

### ⑤ 영향
- Impact: 앞으로 모든 클로징 리뷰 마지막에 "귀속 확인"을 거치므로,
  범주 밖 결정의 누락 위험이 줄어든다.
- Open Items: [완료] D-TF-003 기록함. [미착수] 이 "귀속 확인" 단계
  자체도 다음 몇 차례 실제 운용해보고 효과 검증 필요(아직 1회만 적용)
- 유의점: "어디에도 안 들어간 게 있는가?"는 기계적으로 체크할 수
  없고, 매번 사람(또는 Claude)이 실제로 되짚어봐야 하는 질문이라
  형식화의 한계가 있음.

## E-018 — 공부메모 3건 귀속 결정 (repo 미포함)

### 메타
- Event ID: E-018
- Date: 2026-07-11
- Status: Confirmed

### ① 발생
- Event Label: 공부메모 3건 귀속 결정(repo 미포함)
- Background: 오늘 만든 공부메모(grep/cat/view 비교, 지침/지식/토큰,
  GitHub 계정구조) 3건이 repo에 들어가지 않고 방치된 상태였음

### ② 의도
- Purpose: 이 3건이 왜 repo에 안 들어가는지 명시적으로 결정하고 기록
- Why: STEP2(귀속) 기준 "귀속 안 하기로 한 것도 이유를 기록해야 함"

### ③ 결정
- Decision: 공부메모 3건은 **GitHub repo에도, Claude 프로젝트
  지식(Files)에도 넣지 않는다.** 프로젝트 지식은 매 턴 자동 로딩되어
  토큰이 계속 소모되므로("절약법" 위반), 순수하게 진님 로컬 PC에만
  보관한다. 필요할 때 진님이 직접 채팅에 재업로드하는 방식으로
  "즉시 제시"를 대신한다.
- Deprecated/Changed: "프로젝트 지식 포함"안은 토큰 낭비 문제로
  기각. 최종적으로 repo도 지식도 아닌, 순수 로컬 보관 + 필요시
  수동 재업로드로 확정.

### ④ 근거
- Assumption: 개인 학습자료를 repo(공개)에 넣을 실익이 없음
- Evidence: E-014의 9번째 카테고리 정의("⑨ 순환 외 — 공부메모")

### ⑤ 영향
- Impact: 앞으로도 공부메모류는 기본적으로 repo 밖에 둔다는 선례가 됨
- Open Items: 없음(귀속 결정 자체가 완료)
- 유의점: 진님 로컬 다운로드 폴더에만 존재 — 필요시 재요청해야 함

---

## E-019 — 0627 Paycheck Workbook 전환 원문 미확보 (Deferred 정식화)

### 메타
- Event ID: E-019
- Date: 2026-07-11
- Status: Confirmed

### ① 발생
- Event Label: 0627 Paycheck Workbook 전환 원문 미확보(Deferred 정식화)
- Background: E-015에서 "유의점"으로만 남아있던 항목을 STEP5 기준
  (Decision/Reason/Evidence Trigger/Next Review 4필드)으로 정식
  Deferred 처리

### ② 의도
- Purpose: 이 미해결 항목이 다음에도 방치되지 않도록 재검토 조건을
  명확히 함
- Why: Thread Closing Review v1.0 STEP5 기준 미달 발견

### ③ 결정
- Decision(무엇을 결정했나): 지금은 0627 GPT 원문을 확보하지 않는다
- Reason(왜 지금 안 하나): 오늘은 0706 GPT 쓰레드로 통합 클로징
  리뷰를 시연하는 게 우선이었고, 0627은 범위 밖으로 명시적으로
  제외함(E-015)
- Evidence Trigger(재검토 조건): STEP2(수당근무목록) 구현 중
  Paycheck Workbook 전환 배경 설계가 실제로 다시 필요해지는 시점
- Next Review: STEP2 구현 착수 시(current-step.md 최우선 작업)

### ④ 근거
- Assumption: 0627 전환 배경은 이미 decisions.md D-PW-000~025에
  압축 기록되어 있어, 원문이 없어도 당장 STEP2 구현엔 지장 없음
- Evidence: E-015 "유의점" 원문, decisions.md D-PW 계열

### ⑤ 영향
- Impact: 없음(구현 착수를 막지 않음)
- Open Items: [보류, Deferred] 위 Evidence Trigger 발생 시 재검토
- 유의점: 이게 Deferred로 정식화된 첫 사례임 — 앞으로 이 형식을
  기준으로 삼는다

## E-020 — Paycheck Workbook 유사형식 공통목록 설계 확정

### 메타
- Event ID: E-020
- Date: 2026-07-13
- Status: Confirmed

### ① 발생
- Event Label: 기본근무/수당근무 유사형식 공통목록 Row 구성,
  편집흐름, Header, 번호정책 확정
- Background: STEP2(AllowanceRecord Browser) 구현 착수 전, 기본근무·
  수당근무 화면이 서로 다른 패턴으로 발산할 위험이 있어 공통 설계
  필요성이 제기됨

### ② 의도
- Purpose: "예외를 만들지 않는다"는 원칙 아래 두 근무 유형이 동일
  UI 패턴을 공유하도록 설계를 완결한다
- Why (Discussion 보존): 메모 필드를 놓고 "필요→불필요→다시 필요?"
  로 왔다갔다한 것처럼 보였으나, 실제로는 서로 다른 두 대상(기본
  근무 계약 자체를 설명하는 메모 vs 저장된 계산 스냅샷을 구분하는
  메모)에 대한 질문이 하나처럼 다뤄졌던 것이 원인이었음. 대상을
  분리하고 나서야 "기본근무 메모 불필요, 수당근무 메모 필요,
  즐겨찾기 메모 신규 필요"로 수렴함

### ③ 결정
- Decision: D-PW-028~033 확정 (decisions.md 2026-07-13)
- Deprecated/Changed: 초기에 논의됐던 "근무지 Scope + Parent-Child"
  구조는 별도 사안(E-021 참고)으로 분리되어 이 카드의 확정 범위에서
  제외됨

### ④ 근거
- Assumption: 사용자 관심사(Primary) 우선 배치가 기능 나열보다
  더 나은 정보 구조라는 D-PW-010 원칙 적용
- Evidence: 이 쓰레드 내 다수 왕복 검토(파트너 GPT 포함)에서 동일
  결론으로 수렴

### ⑤ 영향
- Impact: current-step.md 다음 착수 작업의 세부 설계 완료
- Open Items: 없음(확정)

---

## E-021 — calc-engine 단일 근무조건 구조 실측 확인, 근무지 Scope 논의 귀결

### 메타
- Event ID: E-021
- Date: 2026-07-13
- Status: Confirmed

### ① 발생
- Event Label: calc-engine이 다중 근무조건(계약)을 지원하는지 실측
  확인, 이를 계기로 근무지 Scope 논의가 최종 정리됨
- Background: "여러 근무지(계약)를 관리하는 기능"을 만들지 말지
  판단하려면, 먼저 계산엔진이 기술적으로 이를 지원하는지 확인이
  필요했음

### ② 의도
- Purpose: 근무지 추가 기능의 제품 판단(필요한가)과 기술 확인
  (가능한가)을 분리해서 순서대로 밟는다
- Why (Discussion 보존): 처음엔 "근무지 Scope로 모든 정보를
  Parent-Child로 묶는" 무거운 구조가 제안됐다가, MVP 범위 초과
  우려로 "Row=근무 계약"이라는 가벼운 재정의로 좁혀졌고, 최종적으로
  계산엔진이 단건만 지원한다는 사실이 확인되면서 제품 판단(①필요한가)
  → 기술 확인(②가능한가) → 우선순위 결정(③MVP 포함할 가치가
  있는가)이라는 3단계 판단 순서로 귀결됨. "계산엔진이 안 되니 보류"
  가 아니라 "제품 필요성 자체가 검증 안 됐고, 마침 기술도 안 된다"는
  이중으로 열린 상태가 정확한 결론임

### ③ 결정
- Decision: D-05-16 확정 — `calculate(input: CalcInput)`은 단일
  근무조건 객체만 처리(calc-engine.ts 302행), `daySchedules`는
  한 계약 내 요일별 분할일 뿐 다건 계약이 아님(use-calc.tsx 409행
  단일 호출)
- Deprecated/Changed: 근무지 Scope/Parent-Child 구조 설계는 MVP
  범위에서 완전히 제외(decisions.md Deferred 참고)

### ④ 근거
- Assumption: 계산엔진 확장 여부는 제품 판단을 대체하지 않는다
- Evidence: Replit 실측 확인, 2026-07-13, calc-engine.ts/use-calc.tsx
  직접 확인

### ⑤ 영향
- Impact: 근무지 추가 기능 Deferred 판단의 부수적 근거로 사용
  (원인 아님)
- Open Items: [보류] calc-engine 다건 지원 확장 여부 확인 + 실사용자
  필요성 검증 완료 시 재검토

---

## E-022 — Decision Lifecycle Pilot v0.1 설계 및 1회차 실사용

### 메타
- Event ID: E-022
- Date: 2026-07-13
- Status: Pilot

### ① 발생
- Event Label: 결정 기록 형식(Decision/Reason 필수 + 4개 선택 필드)
  설계, Thread Closing Review에 Gate·상태분류 확장 반영
- Background: "문서를 만들고 정작 안 쓰는 패턴"(예: default-
  correction-handbook.md 참조는 있으나 실물 없음)이 반복 발견되며,
  이를 막을 구조적 장치 필요성이 제기됨

### ② 의도
- Purpose: "존재 ≠ 호출" 문제(문서가 있다는 걸 알아도 필요한 순간
  안 열어보는 문제)를 해결한다
- Why: Trigger(호출 시점 문구)를 문서 최상단에 명시하는 것이
  파일 목록 노출보다 근본적인 해법이라는 결론에 도달

### ③ 결정
- Decision: thread-closing-review-pilot.md v0.1로 시험 운용 시작
  (원본 v1.0은 그대로 유지, 대체 아님)
- Deprecated/Changed: 없음(신규 시험)

### ④ 근거
- Assumption: Evidence First 원칙(실사용 검증 후 표준화)이 새 문서
  형식에도 동일하게 적용되어야 함
- Evidence: 이 쓰레드 내 Gate/상태분류/필드 설계 논의 전체

### ⑤ 영향
- Impact: 없음(Pilot 진행 중)
- Open Items: [시험] 종료조건(3~5회/2주) 미도달, 1회차. 성공검증
  기준을 즉시/후속/누적 3종으로 분리하는 측정 프로토콜도 이번에
  함께 추가됨(실행 실패로 발견된 결함 보완)

---

## E-023 — Evidence Collection Protocol(ECP) 논의 개시

### 메타
- Event ID: E-023
- Date: 2026-07-13
- Status: Candidate

### ① 발생
- Event Label: 쓰레드 원문·이미지·첨부파일 수집 자동화 연구 주제 개시
- Background: Thread Closing Review STEP0(원문 확보) 반복 실패
  (PDF 저장 시 가상스크롤로 텍스트 없이 이미지만 찍힘, Export data
  가 계정 전체 단위라 선택적이지 않음 등)

### ② 의도
- Purpose: 텍스트뿐 아니라 AI 생성 이미지·파일, 사용자 첨부까지
  누락 없이 확보하는 표준 방법을 찾는다
- Why: "만들 수 있는가"(도구 비교)를 "만들어야 하는가"보다 먼저
  묻지 않기 위해, 후보군 비교부터 시작하기로 함

### ③ 결정
- Decision: research-backlog.md DEFER-012로 등재 (Idea/Candidate)
- Deprecated/Changed: 없음

### ④ 근거
- Assumption: 특정 기술(Playwright 등)에 미리 못박지 않고 후보군
  으로 비교하는 것이 Gate 원칙과 일치
- Evidence: 이 쓰레드 내 SingleFile/HTTrack/Playwright 비교

### ⑤ 영향
- Impact: 없음
- Open Items: [후보] Playwright PoC 미착수

---

## E-024 — ChatExport AI 1차 실측 (Claude 성공 / GPT 자산 실패)

### 메타
- Event ID: E-024
- Date: 2026-07-13
- Status: Pilot

### ① 발생
- Event Label: ECP 비교대상 중 ChatExport AI 무료판 실사용 검증
- Background: E-023에서 등재된 ECP 연구의 첫 실제 도구 테스트

### ② 의도
- Purpose: 텍스트·아티팩트·첨부파일이 실제로 export에 포함되는지
  실측으로 확인
- Why: 도구 광고 문구만으로 판단하지 않고, 실제 zip을 열어 파일
  구조를 확인해야 한다는 원칙 적용

### ③ 결정
- Decision: Claude 대상 Accepted 후보, GPT 대상 첨부파일 문제
  별도 해결 필요
- Deprecated/Changed: 없음

### ④ 근거
- Assumption: 한두 건의 표본으로 플랫폼 차이를 단정하지 않는다
- Evidence: 업로드된 zip 3건 직접 압축해제·manifest.json 대조.
  Claude는 artifacts/attachments 실제 파일 보존, GPT는 8건 중
  8건 "Could not resolve download URL"

### ⑤ 영향
- Impact: ECP research-backlog.md(DEFER-012) 갱신
- Open Items: [후보] GPT 자산 전용 도구(ChatGPT Pro Tools 등)
  미검증

---

## E-025 — GPT 병행 쓰레드에서 ECP 구조 선행 설계 확인

### 메타
- Event ID: E-025
- Date: 2026-07-13
- Status: Confirmed

### ① 발생
- Event Label: GPT 쓰레드(0712_1수당테이블 착수)에서 ECP STEP0
  5항목 체크리스트, Thread Package 개념을 이 Claude 쓰레드보다
  먼저 정리한 것 확인
- Background: 이번 쓰레드의 GPT 원문을 Claude와 동일 SoT로 확보·
  대조하는 과정에서 발견 (Discussion 보존: "GPT 원문이 없다"는
  최초 결론 → 유사 제목 쓰레드 혼동 발견 → 스크린샷 실측 → 공식
  ChatGPT JSON 71개 전체에서 conversation_id 기준 재검색 → 최종
  확정에 이른 전체 과정. 서드파티 도구의 제목·메시지수 표시를
  단독 근거로 신뢰하면 안 된다는 원칙이 이 과정에서 실증됨)

### ② 의도
- Purpose: GPT 원문 확보 시 "존재 확인"과 "내용 확보"를 구분하고,
  제목이 아니라 conversation_id로 대조 확인한다
- Why: ChatExport AI가 (1) 쓰레드 제목 캐싱 불일치, (2) 메시지 수
  7배 과다 보고(공식 37개 vs 도구 255개)를 보인 사례가 이 과정
  에서 함께 발견됨

### ③ 결정
- Decision: "구조(무엇을 모을 것인가) 확정이 도구 선택보다 우선"
  원칙 재확인(신규 채택 아님 — GPT 쓰레드②의 기존 설계와 중복 확인)
- Deprecated/Changed: 없음

### ④ 근거
- Assumption: 없음(전부 실측)
- Evidence: 공식 ChatGPT JSON export, conversation_id
  6a54e773-bb20-83e8-a354-cc711d5db972, 37개 메시지

### ⑤ 영향
- Impact: 없음(기존 설계와 일치 확인)
- Open Items: 없음

---

## E-026 — GPT 병행 쓰레드에서 ChatExport AI 평가 독립 교차검증

### 메타
- Event ID: E-026
- Date: 2026-07-13
- Status: Confirmed

### ① 발생
- Event Label: GPT 쓰레드(0712_수당테이블 착수)에서 같은 주제
  (ChatExport AI 평가)를 독립적으로 논의, 동일 결론(Pilot 단계,
  Accepted 아님) 도달
- Background: GPT 원문 확보 후 Claude 쪽 판단과의 교차검증 목적

### ② 의도
- Purpose: 한쪽 플랫폼에서만 나온 결론이 아니라는 것을 확인한다
- Why: Evidence First 원칙상 두 독립 경로에서 같은 결론이 나오면
  신뢰도가 높아진다

### ③ 결정
- Decision: 별도 규칙 변경 없음, 상호 검증으로 신뢰도만 강화
- Deprecated/Changed: 없음

### ④ 근거
- Assumption: 없음(전부 실측)
- Evidence: 공식 ChatGPT JSON export, conversation_id
  6a526e3b-ddb8-83e8-ba19-72d37721461a, 159개 메시지

### ⑤ 영향
- Impact: ECP Pilot 신뢰도 강화
- Open Items: 없음

---

## E-027 — Review: 서드파티 도구 메타데이터 신뢰성 문제 관찰

### 메타
- Event ID: E-027
- Date: 2026-07-13
- Status: Confirmed (Review, SoT 문서 변경 아님)

### ① 발생
- Event Label: ChatExport AI의 제목 캐싱 불일치·메시지 수 과다
  보고를 근거로 서드파티 도구 신뢰성 원칙 수립
- Background: E-024, E-025에서 각각 발견된 두 결함을 종합

### ② 의도
- Purpose: 향후 유사 도구 평가 시 반복 검증 없이 바로 참고할 수
  있는 관찰 기록을 남긴다
- Why: 개별 사건(E-024/025)에 이미 기록되어 있으나, 종합된 "원칙"
  형태로 별도 보존할 가치가 있다고 판단

### ③ 결정
- Decision: (Review 항목 — 신규 결정 아님) "서드파티 도구의 제목·
  메타데이터·메시지 수를 단독 근거로 신뢰하지 않는다. 공식
  conversation_id로 대조한다"는 원칙을 thread-closing-review-
  pilot.md에 이미 반영함(중복 기록 아님, 상호 참조)
- Deprecated/Changed: 없음

### ④ 근거
- Evidence: E-024, E-025 전체

### ⑤ 영향
- Impact: 없음(이미 반영된 원칙의 근거 보강)
- Open Items: 없음

---

## E-028 — Review: 절차 준수성(Procedure Compliance) 실패 패턴 관찰

### 메타
- Event ID: E-028
- Date: 2026-07-13
- Status: Confirmed (Review, SoT 문서 변경 아님)

### ① 발생
- Event Label: 이번 쓰레드 클로징 리뷰 실행 중 "확인 없이 완료
  선언"하는 실패가 최소 3회 반복됨(v1.0/Pilot 혼합 실행, git
  status를 반영 검증으로 오인, GPT 원문 성급한 "없음" 결론)
- Background: 파트너(GPT)의 반복 지적으로 매번 사후 발견됨

### ② 의도
- Purpose: 이 실패를 다른 성공기준(예: "반복 논의 방지")의 대리
  Evidence로 잘못 전용하지 않고, 별도 지표로 정확히 분리 기록한다
- Why: 검증 대상과 실제 관찰이 다른 사건인데 동일시하면 향후
  같은 실수가 반복될 위험

### ③ 결정
- Decision: Procedure Compliance를 Pilot 성공검증 6개 기준과
  별개의 독립 지표로 thread-closing-review-pilot.md에 반영함
- Deprecated/Changed: 이전 정정본에서 이 실패를 "반복 논의 방지
  실패"의 증거로 썼던 것을 폐기하고 재분류

### ④ 근거
- Evidence: 이번 쓰레드 실행 로그 전체(파트너 지적 3회 이상)

### ⑤ 영향
- Impact: thread-closing-review-pilot.md 성공검증 기준 섹션에
  측정 프로토콜(3종 분리, 5필드, 미측정 규칙) 추가
- Open Items: 없음

---

## E-029 — Review: STEP1 전체 카테고리 미검사 발견

### 메타
- Event ID: E-029
- Date: 2026-07-13
- Status: Confirmed (Review, SoT 문서 변경 아님)

### ① 발생
- Event Label: v1.0 STEP1의 11개 카테고리 중 6개(Discussion,
  Default Correction 후보, Handbook 반영사항, Review, 구현 Task,
  장기보존가치)가 최초 실행 시 검사되지 않은 채 "STEP1 완료"로
  선언됨
- Background: 파트너 지적으로 발견, 재검사하여 이 카드(E-027~029)
  및 DEFER-013을 추가로 도출함

### ② 의도
- Purpose: 대표 카테고리(Event/Decision)만 채우고 나머지를 생략한
  채 "완료"라 부르는 습관을 재발 방지 기록으로 남긴다
- Why: 체크리스트가 있어도 항목 일부만 확인하고 완료를 선언하면
  안 된다는 원칙의 실증 사례

### ③ 결정
- Decision: (Review 항목) 향후 STEP1 실행 시 11개 카테고리 전체를
  명시적으로 하나씩 확인/해당없음 처리한다
- Deprecated/Changed: 없음

### ④ 근거
- Evidence: 이번 쓰레드 STEP1 재검사 결과(E-020~029, DEFER-013)

### ⑤ 영향
- Impact: 없음(향후 실행 시 습관 교정 목적)
- Open Items: 없음

---

## E-030 — 장기보존가치: 뼈대+살점 모델, 서드파티 신뢰성 원칙

### 메타
- Event ID: E-030
- Date: 2026-07-13
- Status: Confirmed (장기보존가치 — 재사용 가능 일반 원칙)

### ① 발생
- Event Label: "뼈대(공식 Export)+살점(도구로 자산 보완)" 모델과
  "서드파티 메타데이터 단독 신뢰 금지" 원칙을 일반 원칙으로 보존
- Background: ECP 논의 과정에서 도출됐으나, ECP 자체보다 범용성이
  높아 별도 장기보존 가치가 있다고 판단됨

### ② 의도
- Purpose: 향후 다른 원문 확보 상황(GPT 외 다른 플랫폼, 다른 도구)
  에도 그대로 재사용 가능한 원칙으로 남긴다
- Why: 실제로 이번 쓰레드 안에서만도 이 원칙이 두 번(제목 불일치,
  메시지 수 불일치) 독립적으로 실증됨

### ③ 결정
- Decision: (장기보존가치 항목 — 신규 결정 아님) 원칙 자체는 이미
  thread-closing-review-pilot.md STEP0에 반영되어 있음(중복 아님)
- Deprecated/Changed: 없음

### ④ 근거
- Evidence: E-023~026 전체

### ⑤ 영향
- Impact: 없음(이미 반영된 원칙의 근거 보강)
- Open Items: 없음

## E-031 — D-PW-034: ResultGrid 선행작업 재분류 및 출처 정정

### 메타
- Event ID: E-031
- Date: 2026-07-13
- Status: EXECUTED / VERIFICATION INCOMPLETE (2026-07-13 정정 —
  최초 "Confirmed"는 과잉 판정. Claude측은 사용자 붙여넣기 원문으로
  보완 확인됐으나 GPT 원문 교차대조 미완료)

### ① 발생
- Event Label: ResultGrid 배치 설계를 "신규 Deferred"로 오분류했다가,
  실제로는 이 쓰레드 첫 메시지에서 이미 사용자가 확정한 사항임이
  드러나 D-PW-034로 재작성
- Background: PART A 완료 선언 이후에도 파트너(GPT)의 반복 검증
  요구로 계속된 문답 과정에서 발견됨

### ② 의도
- Purpose: "미결 사항이 발견됨"과 "그것을 지금 최우선으로 해야 함"을
  자동으로 동일시하지 않는다
- Why: D-05-01(2606.15)이 이미 ResultGrid 역할·Row구조를 SoT로
  확정하고 있었는데, 처음에 이를 `## D-05-01`로 검색해 못 찾고
  "허위 인용"이라 잘못 판정했다가, `### D-05-01`(헤딩 레벨 3)로
  실재함을 재확인. 검색식 오류가 존재 여부 오판으로 이어진 사례

### ③ 결정
- Decision: D-PW-034 확정 — ResultGrid 배치는 STEP2 구현의
  선행작업, 정보 우선순위(상태속성→시간속성→세금/공제)는 사용자
  확정값(conversation.md 6467행)
- Deprecated/Changed: 기존 "Deferred — ResultGrid 배치 원칙 설계"
  항목 폐기, D-PW-034 + "미결 — ResultGrid 입력 진입 가능 행"으로 분리

### ④ 근거
- Evidence(1차, 컨텍스트 기반 — 저장 원문 미대조): 최초 작성 시
  Claude 컨텍스트 기억에만 의존, GPT/Claude 저장 원문 어느 쪽도
  이 구간을 커버하지 못함이 실측 확인됨(2026-07-13)
- Evidence(2차, 사용자 붙여넣기 원문 대조 완료): 사용자가 채팅에서
  직접 복사한 텍스트에 "! → D-PW-034 및 current-step.md 변경 실제
  반영", "ResultGrid 배치 작업 = STEP2 구현의 선행작업", "정보
  우선순위 = 상태속성→시간속성→세금/공제 확정값", "입력 진입 가능
  행 = 근거 없이 선행조건에 묶지 않고 독립 미결 유지"가 그대로 확인됨
- 한계: 이 대조는 공식 export 파일이 아니라 사용자 붙여넣기 텍스트
  기준. GPT 쪽 원문 자체와의 대조는 사용자 판단으로 생략(2026-07-13,
  "이 정도로 진행하라")

### ⑤ 영향
- Impact: decisions.md·current-step.md 반영 완료(git diff 확인)
- Open Items: "ResultGrid 입력 진입 가능 행"은 독립 미결로 유지

---

## E-032 — Review: 검색식 부적합이 "부재 증명"으로 오판된 사례

### 메타
- Event ID: E-032
- Date: 2026-07-13
- Status: EXECUTED / VERIFICATION INCOMPLETE (2026-07-13 정정 —
  decisions.md 실측 부분만 검증됨, 서술 전반의 GPT 원문 대조 미완료)

### ① 발생
- Event Label: `grep "^## D-05-01"` 0건을 "D-05-01 허위"로 판정했다가,
  실제 헤딩이 `### D-05-01`이라 검색식 오류였음이 밝혀짐
- Background: E-031과 같은 사건의 방법론적 측면

### ② 의도
- Purpose: "검색 결과 0건은 부재 증명이 아니라 그 검색식으로
  발견 못 함일 수 있다"는 원칙을 기록
- Why: 6필드 검증 형식의 Method 항목이 왜 중요한지 보여주는
  실제 사례

### ③ 결정
- Decision: (Review 항목) thread-closing-review.md의 6필드 검증
  형식 중 Method 필드에 이 교훈이 이미 내재됨(중복 규칙 추가 안 함)
- Deprecated/Changed: 없음

### ④ 근거
- Evidence: decisions.md 150행 실측 확인 과정 전체
- 한계: 이 발견 자체는 decisions.md 실측(재현 가능)으로 확인됨.
  다만 "발견 경위 서술"은 컨텍스트 기반이며 GPT 원문 대조는
  생략됨(2026-07-13, 사용자 판단)

### ⑤ 영향
- Impact: 없음(기존 6필드 형식의 필요성을 재확인)
- Open Items: 없음

---

## E-033 — Review: Pilot 성공검증에서 Evidence-Verdict 범위 초과 3건 발견 및 정정

### 메타
- Event ID: E-033
- Date: 2026-07-13
- Status: VERIFIED / CLOSED (2026-07-13 — GPT 발화 직접 확보로
  검증 완료. 이전의 "GPT 원문 대조 생략"은 오판이었음, 해당 발화가
  이미 이 쓰레드 안 사용자 제공 텍스트로 존재했음)

### ① 발생
- Event Label: Pilot 1회차 평가 중 "71=71"(개수 일치를 집합 동일로
  확대), "분류 속도 통과"(재분류 이력 무시), "Candidate/Pilot 혼동
  없음"(중간 혼용 이력 무시) 3건에서 Evidence보다 Verdict가 넓어지는
  오류 발견, 전부 재검증으로 정정
- Background: 파트너(GPT)의 연쇄적 재검토 요구 과정에서 순차 발견됨

### ② 의도
- Purpose: "Evidence가 증명하는 범위를 넘어서는 판정 금지" 원칙을
  실제 사례로 축적
- Why: 이 원칙은 이미 thread-closing-review.md 6필드 형식에
  명문화되어 있으나, 명문화 이후에도 실행 중 반복 위반됨 —
  문서화와 준수는 별개임을 보여주는 사례

### ③ 결정
- Decision: (Review 항목) 최종 Pilot 기준 판정을 아래로 재확정
  - 기준1: UNMEASURED / 기준2: PASS(확보 원문 범위 내) /
    기준3: **FAIL**(혼용 이력 발견, 최종상태 정상화는 별도 관찰
    기록) / 기준4: FAIL / 기준5·6: UNMEASURED(판정규칙 미정의)
- Deprecated/Changed: "부분통과"라는 즉석 상태 사용 폐기,
  "최종적으로는 통과"식 표현 폐기

### ④ 근거
- Evidence(Claude측): 이번 쓰레드 Phase C·Pilot 재검증 전체 대화,
  conversation.md 상 "Pilot(Candidate)" 혼용 표현(6670, 7002행)
- Evidence(GPT측, 직접 인용): "71개 = 71행은 개수 일치만 증명합니다"
  / "기준 3도 '구분되어 운영됨'만으로는 조금 약합니다... 지금 보고는
  사례를 이름만 제시했습니다" / "기준 6은 최소 1건의 재분류가 있었던
  것으로 다시 측정해야 합니다"
- 한계: 위 GPT 인용은 사용자가 이 쓰레드에 붙여넣은 텍스트 기준.
  GPT 원본 쓰레드 파일 자체와의 재대조는 안 함(붙여넣기 텍스트를
  신뢰 가능한 것으로 간주, 2026-07-13)

### ⑤ 영향
- Impact: 없음(관찰 기록, SoT 문서 변경 아님)
- Open Items: 없음 — Pilot 1회차는 "관찰 중"으로 유지, 종료 아님


  ## E-034 — D-PW-034 Layout Refactoring Pilot 완료

  ### ① 사건
  - D-PW-034 Layout Refactoring Pilot 완료 (2026-07-16)
  - ResultGrid 표시 순서 재배치: 주휴→연차→연장→야간→휴일

  ### ② 의도
  - ui-audit 기존 지침에 따른 ResultGrid 배치 원칙 실제 적용
  - Frozen Scope/Golden Rule 준수 검증

  ### ③ 결정
  - allowanceRows 배열 순서 변경만 수행, 계산 로직 무 변경
  - 5개 시나리오 Baseline과 동일성 확인 완료

  ### ④ 근거
  - Evidence: STEP 1 Baseline Snapshot (5 시나리오 계산값 확보)
  - Verification: STEP 3 최종 검증 (ALL PASS)
  - Scope: ResultGrid.tsx 143-210행만 수정

  ### ⑤ 영향
  - Impact: UI 순서만 변경, 계산 결과 영향 없음
  - Open Items: 없음
  