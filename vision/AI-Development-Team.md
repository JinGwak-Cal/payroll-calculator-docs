# AI Development Team — 비전 문서

## 최종 목표

사람은 개발자가 아니라 **Product Owner** 역할만 수행한다.

---

## Stage 0. 현재(기존 방식)

```
사용자 → Claude/GPT → 사용자 판단 → GitHub
```

- AI는 도구
- 사용자가 대부분의 작업 흐름을 관리

---

## Stage 1. AI 역할 분리 ✅ 완료 (2606.29)

```
사용자
    ↓
GPT (설계/리뷰)
CodeX (조사/원인분석)
Claude (구현)
AI Push (PR/Merge/Release)
    ↓
사용자 (Release Gate 승인)
```

---

## Stage 2. AI Dispatcher

GPT가 단순 리뷰어에서 AI Dispatcher로 진화.

```
사용자: "D-PW-031 구현"
    ↓
GPT → Task Graph 생성
    → Task-1: Repository 조사 → CodeX
    → Task-2: 구현 → Claude
    → Task-3: 검증 → AI Push
    → Task-4: 리뷰 → GPT
```

GPT는 각 AI에게 최적화된 프롬프트를 자동 생성.

---

## Stage 3. AI Push = Release Engine

```
Claude 구현
    ↓ AI Push
    ↓ Validate → Artifact → Release Gate
    ↓ 사용자 승인
    ↓ 자동 Merge → 자동 Sync
```

Release Button = 사람이 코드가 아니라 **제품을 승인하는 버튼**

---

## Stage 4. AI Workflow Engine

```
사용자 → GPT → Task Graph
    → AI Dispatcher
    → CodeX → Claude → AI Push
    → GPT Review → Release Gate → 사용자 승인
```

---

## Stage 5. MCP 기반 AI 협업

현재: 사용자 → GPT → (복사) → CodeX
미래: GPT → CodeX (직접 전달)

---

## Stage 6. 최종 목표

### 사용자가 하는 일
1. 작업 목표 제시 ("D-PW-031 구현")
2. Release Gate 승인

끝.

### AI가 수행하는 일
작업 분해 / 조사 / Repository 분석 / Root Cause 분석 /
구현 / 테스트 / PR 생성 / Merge / 문서 갱신 / 리뷰

---

## 핵심 인식

우리가 만드는 것은 단순한 "AI Push"가 아니다.
**AI가 하나의 개발팀으로 협업하는 개발 시스템(AI Development Team)** 을 구축하고 있다.
