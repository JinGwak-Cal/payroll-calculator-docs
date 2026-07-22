# Lesson Learned — Mode Confusion (Cross-Agent Finding)

```
Origin: GPT (Independent Reviewer, PI-0001 실행 중 자체 보고)
Related: Claude(A-08 관련 doc33/34/48 자기분석, 오늘 최소 5회 재현)
Current Stage: P5 / Cross-cutting
```

## 현상 (GPT 자기보고, 원문 그대로 보존)

ZIP 3개(Contract·SOP·Source)를 첨부로 받았을 때는 문서 설명
모드(Explainer Mode)로 계속 흘렀고, 같은 내용을 대화창에 직접
텍스트로 붙여넣고 수행 지시를 명시하자 그제서야 리뷰 수행
모드(Reader/Reviewer Mode)로 전환됨.

## 원인 (GPT 분석)

1. **역할(Goal) 오추론**: 문서를 "분석 대상"으로 해석, "수행해야
   할 역할(Reviewer)"로 먼저 인식 못함
2. **첨부파일은 실행 문맥을 강제하지 못함**: ZIP 안에 Contract·
   SOP·Source가 있어도 "지금부터 너는 OR Reviewer다"라는 명시적
   실행 지시가 없으면 일반 문서분석 패턴으로 시작함
3. 대화창 직접 텍스트 + 사용자의 현재 의도 + 직전 대화가 합쳐져야
   "설명이 아니라 수행"으로 전환됨

## Claude와의 교차 비교 (동일 구조의 다른 사례)

| | GPT (Explainer vs Reviewer) | Claude (검토 vs 실행) |
|---|---|---|
| 현상 | 문서 받으면 설명 모드로 계속 감 | "검토해줘"를 검토+실행으로 확장 |
| 원인 | 역할 문맥이 명시적으로 안 주어지면 디폴트(설명) 모드 유지 | 직전 턴들의 "검토→동의→실행" 패턴에 새 지시어가 휩쓸림(Over-Generalization, doc33) |
| 전환 계기 | 사용자의 명시적 실행지시 + 직접 텍스트 | 사용자의 직접 지적("왜 검토인데 실행했지?") |
| 공통점 | **둘 다 사후에만 교정됨 — 사전에 스스로 못 잡음** | 동일 |

## 재발 방지 원칙 (Cross-Agent, GPT 제안 + Claude 사례로 보강)

> 작업 시작 시 첫 번째 확인은 "이 문서를 설명하는 것인가?"가
> 아니라 "이 문서를 사용하여 어떤 역할을 수행해야 하는가?"여야
> 한다.

Claude 쪽에서 보강: 이 원칙은 "검토결과 선언 게이트"(오늘 이미
합의된 Condition1 요소)와 구조적으로 동일하다 — **AI가 받은
입력이 "정보"인지 "작업지시"인지를 응답 시작 전에 먼저 자문·
선언하는 절차가 있어야 한다**는 게 두 AI에서 독립적으로 확인된
공통 결론이다.

## 이 발견의 처리

이건 OR-METHOD의 P0~P5 절차 결함이 아니라 **AI 자체의 모드
전환(Mode Switching) 결함**이므로, SOP/Template CR로 넣기보다
**absolute-rules.md 또는 교정표 차원의 원칙 후보(Candidate)**로
더 적절하다. R19(Assertion Gate)의 확장 후보로 검토 가능 — 별도
승인 필요.
