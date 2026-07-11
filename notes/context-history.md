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
