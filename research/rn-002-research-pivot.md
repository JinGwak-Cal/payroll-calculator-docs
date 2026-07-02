# RN-002 : Research Pivot — From AI Behavior to Collaboration Environment Engineering

Version: v1.0
Status: Research Direction Confirmed
Origin: RN-001 진행 중 발견된 연구 방향 전환
Audience: GPT · Claude · CodeX · Research Partners

---

## 1. Executive Summary

이번 연구의 가장 중요한 성과는 Claude의 자율성 향상이 아니라, **연구 대상 자체가 바뀌었다**는 것이다.

초기 연구는 "Claude가 왜 좋아졌는가?"를 설명하려는 시도였다. 그러나 RN-001을 진행하면서 연구의 중심은 AI 모델이 아니라 **Collaboration Environment(협업환경)**로 이동하였다.

앞으로 연구의 목적은 특정 AI의 성능을 설명하는 것이 아니라, 다양한 AI에서 동일한 행동 변화를 재현할 수 있는 **Collaboration Environment Model**을 구축하는 것이다.

핵심 한 문장: **"우리는 AI를 연구하는 것이 아니라, AI가 최고의 협업 성능을 낼 수 있는 환경을 연구한다."**

---

## 2. Research Pivot

**Before**
```
Claude → Context Threshold → CTI → HDR
질문: Claude는 왜 갑자기 자율적으로 행동했는가?
```

**After**
```
Collaboration Environment → Behavior Change → Threshold → Reproducibility
질문: 어떤 협업환경이 AI의 행동을 변화시키는가?
```

연구의 중심이 **AI에서 Environment로 이동**하였다.

---

## 3. New Research Goal

RN-001의 최종 목적은 Claude를 설명하는 것이 아니다. 최종 목적은 **Predictable Collaboration Environment Engineering**이다.

단계별 목표:
1. **재현(Reproduce)**: 동일 Environment에서 동일 행동 변화 재현
2. **설계(Design)**: 원하는 행동 변화를 위한 Environment 설계
3. **예측(Predict)**: Environment 변수로 Threshold 발생 예측
4. **측정(Measure)**: Environment 상태를 정량 지표로 측정
5. **최적화(Optimize)**: 최소 비용으로 최대 Threshold 효과 달성

동일한 Environment를 제공하면 Claude / GPT / CodeX / 다른 AI에서도 비슷한 행동 변화가 발생하는지를 연구한다.

---

## 4. New Engineering Perspective

이번 연구는 AI Engineering이 아니라 **Environment Engineering**이다.

```
Design
  ↓
Environment
  ↓
Measurement
  ↓
Behavior
  ↓
Threshold
  ↓
Prediction
  ↓
Optimization
```

---

## 5. Environment Components & Variables

**Component(무엇이 존재하는가)와 Variable(그것이 어느 정도인가)을 구분한다.**

| Component | 예시 | Variable | 의미 |
|---|---|---|---|
| manual-v14 | 협업 규칙 문서 | Visibility | 얼마나 잘 보이는가 |
| merged-context | 통합 Context 파일 | Accessibility | 얼마나 접근 가능한가 |
| decisions.md | 확정된 결정 목록 | Stability | 얼마나 안정적으로 유지되는가 |
| Feedback | 사용자 피드백 누적 | Density | 얼마나 자주, 명확하게 주어졌는가 |
| Workflow | 작업 흐름 구조 | Continuity | 흐름이 얼마나 끊김 없이 이어지는가 |
| Role | 역할 분리 구조 | Clarity | 역할이 얼마나 명확히 정의되었는가 |

Component는 Threshold Enabler **후보**이고, Variable은 그 Component의 **강도**를 측정하는 지표다.

---

## 6. Measurement Direction

기존 CTI·HDR만으로는 부족하다. Environment 자체를 측정해야 한다.

독립변수 후보 (AI 행동 이전에 존재):
- Environment Visibility
- Decision Availability
- Workflow Continuity
- Feedback Density
- Artifact Accessibility

---

## 7. Document Structure (장기)

```
research/
    RN-001A  (Protocol)
    RN-001B  (Results)
    RN-002   (Research Pivot ← 본 문서)

engineering/
    ER-001   (Environment Reconstruction — 당시 환경 복원)
    ER-002   ...

models/
    Collaboration-Environment-Model.md
    Environment-Metrics.md
    Threshold-Engineering.md
```

- **RN**: 연구 질문과 결과
- **ER**: 환경 복원 및 분석
- **Model**: 검증을 거쳐 일반화된 공학 모델

---

## 8. Immediate Next Actions (ER-001 기준)

① Environment Reconstruction
② Information Availability Mapping
③ Decision Flow Reconstruction
④ Workflow Reconstruction
⑤ Candidate Enabler Extraction
⑥ Collaboration Environment Modeling
⑦ Cross Validation

---

## 9. Research Principle

Claude는 연구 대상이 아니라 **첫 번째 Case Study**이다. 연구 대상은 **Collaboration Environment**이다.

---

## 10. Vision Statement

> "우리는 AI를 더 똑똑하게 만드는 것이 아니라, AI가 최고의 협업 성능을 낼 수 있는 환경을 설계하고 측정하며 재현하는 공학을 연구한다."

본 문서는 현재 Research Pivot Note(RN-002)이나, Threshold Foundry 전체의 연구 철학을 정의한다는 점에서 장기적으로 **Foundation Document** 또는 **Research Charter**로 승격될 가능성이 있다.

---

*Version: v1.1 | Origin: RN-001 → Research Pivot | GPT Review: Approved with Minor Improvements | Next: ER-001 Environment Reconstruction*
