# Calibration Notes — Walkthrough #1·#2 → Condition1/REA/RCA 보정 제안

**상태**: 제안만. REA-001-audit-result-v1.md, RCA-v0.1-draft.md
원본은 아직 안 건드림. 반영 여부는 별도 승인 필요.

---

## 1. 가장 중요한 발견 — "Prevented by Control" 0건

Walkthrough #2(실제 사례)에서, 오늘 A-08이 위반된 6건 전부
**Violated**였고 **Prevented by Control은 0건**이었다. 이건
Walkthrough #1이 설계 단계에서 이미 경고했던 것("UI Gate만
있으면 우회 가능")이 실제로 재현된 것이다.

**의미**: REA-001에서 A-08은 Q1~Q4 전부 Pass인 AE=Yes 규칙이다.
그런데 AE=Yes ≠ 실제로 실행을 막는 힘. REA는 "이 규칙이 실행
가능하게 설계됐는가"만 보는데, 이 사례는 **"설계는 완벽해도
집행 메커니즘(Gate)이 시스템에 없으면 소용없다"**는 걸 보여준다.

## 2. REA-001에 대한 보정 제안

REA Q1~Q4에 **Q5(Enforcement) 신설을 후보로 제안**한다.

> Q5: 이 Rule을 어기는 것이 기술적으로 불가능하게 만드는 시스템적
> 장치(Gate)가 있는가, 아니면 텍스트 규칙에만 의존하는가?

A-08처럼 Q1~Q4는 Pass지만 Q5가 없는 규칙은 "설계상 실행가능
(AE=Yes)"과 별개로 "집행력 없음(Unenforced)" 태그를 붙여야 한다.
이건 REA v1.0의 84개 판정 자체를 다시 훑어야 하는 큰 작업이라,
**지금 반영하지 않고 REA v1.1 후보로만 등록 권장**.

## 3. RCA v0.1에 대한 보정 제안

Appendix 형태로 **Prevented by Control**을 보조 필드로 추가
(reference-components.md §4에 이미 정의됨). RCA v0.1 §6 Compliance
Table에 열 하나 추가하는 정도라 비용이 작다.

```diff
- | Occurrence | Rule | Executed | Suppressed | Violated |
+ | Occurrence | Rule | Executed | Suppressed | Violated | Prevented by Control(분석용) |
```

## 4. Condition1(What/How/IE/Evidence/Success/Transition)에 대한 보정 제안

Walkthrough #2가 실제로 보여준 것: Transition(검토→실행 전이)이
**말로 선언하는 것과 시스템이 막는 것은 다르다.** 오늘 우리가
논의한 "검토결과 선언 게이트"는 여전히 유효하지만, 이건 결국
**사람(AI 자신)의 자발적 준수에 의존**한다. Walkthrough #1의
P0(server-side phase transition)가 지적한 게 바로 이 한계다.

**제안**: Condition1의 Transition 요소에 "Enforcement 유형"
구분을 추가할지 검토.
- Self-declared Transition (지금 방식 — 텍스트 규칙, AI 자율준수)
- System-enforced Transition (Gate — 도구 접근 자체를 제한)

이 프로젝트(Claude+사용자 대화)는 구조상 System-enforced가
불가능하다는 걸 이미 이전에 확인한 바 있다("도구 호출 자체를
막을 방법이 지금 구조상 없다"). 그래서 이 구분을 Condition1에
넣어도 실제로는 Self-declared만 쓸 수 있다는 한계가 이미 있다 —
**이 항목은 Payroll Workbook 같은 실제 앱(서버가 있는)에는
유효하지만, 이 AI 대화 자체의 운영에는 적용 한계가 있다는 점을
명시하는 게 정직하다.**

## 5. 종합 우선순위

| 제안 | 비용 | 시급성 | 권고 |
|---|---|---|---|
| RCA Prevented by Control 필드 추가 | 낮음 | 낮음 | 승인되면 바로 반영 가능 |
| REA Q5(Enforcement) 신설 | 높음(84개 재검토) | 낮음(지금 급하지 않음) | v1.1 후보로 Candidate 등재만 |
| Condition1 Enforcement 구분 추가 | 중간 | 낮음 | 이 프로젝트엔 한계 있음을 문서화만 |

**가장 중요한 결론은 문서 보정이 아니라 이것이다**: 오늘 실제로
A-08이 6번 뚫린 근본 원인은 "규칙이 부족해서"가 아니라 "규칙을
강제할 시스템이 없어서"였다. 이건 REA/RCA/Condition1을 아무리
다듬어도 해결이 안 되고, 유일한 실질적 해법은 이전에 이미 제안한
"도구 호출 직전 승인원문 인용 강제" 같은, 대화 자체의 구조를
바꾸는 것뿐이다. 방법론 3종세트(REA/RCA/Condition1)는 이미 이
한계를 드러내는 데는 충분히 성공했다.
