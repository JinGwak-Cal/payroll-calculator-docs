# AI 협업 계약서 (AI Workflow Contract)

버전: v1.0 (2606.29)
기준: Stage 1 검증 완료

---

## 원칙

이 문서는 각 AI의 역할을 단순 기술이 아닌
**계약(Contract)** 으로 정의한다.

AI나 도구가 교체되더라도
이 계약이 유지되는 한 협업 방식은 유지된다.

---

## Part 1 — 현재 운영 Workflow (Stage 1, 검증 완료)

### 전체 흐름

```
사용자 (목표 제시)
    ↓
GPT (설계/분해/리뷰)
    ↓
CodeX (Repository 분석/근거 수집)
    ↓
Claude (구현)
    ↓
AI Push (Validate/PR/Release/Sync)
    ↓
GPT (최종 리뷰)
    ↓
사용자 (Release Gate 승인)
    ↓
main 반영
```

---

## AI별 계약

### 1. 사용자

| 항목 | 내용 |
|------|------|
| Input | 없음 (시작점) |
| Output | 작업 목표 (자연어) |
| Handoff | GPT에게 목표 전달 |
| DoD | 목표가 명확하게 기술됨 |

---

### 2. GPT

| 항목 | 내용 |
|------|------|
| Input | 사용자 목표 + 프로젝트 컨텍스트 |
| Output | 작업 분해 / 설계 / Claude 지시 프롬프트 / 리뷰 결과 |
| Handoff | CodeX 우선 전달, 필요 시 Claude 직접 전달 |
| DoD | 설계 승인 완료 / 리뷰 결과 문서화 |

---

### 3. CodeX

| 항목 | 내용 |
|------|------|
| Input | Repository URL + 조사 범위 + 필요 Evidence |
| Output | 파일 목록 / diff / Root Cause / Evidence |
| Handoff | Claude에게 파일 경로 + Evidence 전달 |
| DoD | Root Cause가 Evidence로 증명됨 (DBG-002 준수) |

---

### 4. Claude

| 항목 | 내용 |
|------|------|
| Input | 파일 경로 + Evidence + 구현 지시 + 제약 조건 |
| Output | 수정된 파일 / 새 파일 / 커밋 메시지 |
| Handoff | ai/draft 브랜치에 push |
| DoD | 구현 완료 + ai/draft push 성공 |

**Claude 운영 원칙**
- 승인 없이 구현 진입 금지
- 조건부 승인은 조건을 다시 승인받아야 함
- 30줄 이상 프롬프트는 변경분만 먼저 제시
- 재출력 금지 — 파일로 제공

---

### 5. AI Push

| 항목 | 내용 |
|------|------|
| Input | ai/draft 브랜치 push 이벤트 |
| Output | main 반영 + 후속 Workflow(docs-automation) 수행 + ai/draft 동기화 |
| Handoff | 없음 (최종 실행) |
| DoD | Acceptance Test 전 항목 통과 |

**AI Push 운영 원칙**
- bot self-trigger 방지
- Conflict 자동 해결 없음
- SHA 불일치 시 재승인
- force-with-lease 실패 시 수동 확인

---

### 6. AI Push

| 항목 | 내용 |
|------|------|
| Input | ai/draft 브랜치 push 이벤트 |
| Output | main 반영 + 후속 Workflow(docs-automation) 수행 + ai/draft 동기화 |
| Handoff | 없음 (최종 실행) |
| DoD | Acceptance Test 전 항목 통과 |

**AI Push 운영 원칙**
- bot self-trigger 방지
- Conflict 자동 해결 없음
- SHA 불일치 시 재승인
- force-with-lease 실패 시 수동 확인

---

## 운영 계약 — Release Gate

> Release Gate는 AI 계약이 아닌 **사람의 승인 절차**다.
> AI와 사람의 책임 경계는 여기서 나뉜다.

| 항목 | 내용 |
|------|------|
| 승인자 | jingwak-maker |
| 승인 대상 | Artifact (commit / changed-files / diff / validate.log) |
| 승인 조건 | SHA 동일 + Validate 통과 + 내용 확인 |
| 거부 조건 | SHA 불일치 / Validate 실패 / 내용 미확인 |
| 승인 후 | gh pr merge 자동 실행 |

---

## Part 2 — 확장 계획 (Stage 2~6)

> ⚠️ 이하는 미검증 계획입니다. 구현 완료 시 Part 1로 승격됩니다.

### Stage 2: Prompt 자동 생성
- GPT가 각 AI에게 최적화된 프롬프트 자동 생성
- 사용자 Relay 제거

### Stage 3~4: AI Workflow Engine
- CodeX → Claude → AI Push 자동 연결
- GPT Review 자동 연결

### Stage 5: MCP 연동
- AI 간 직접 작업 전달
- 프롬프트 Relay 제거

### Stage 6: AI Development Team
- 사용자: 목표 제시 + 승인만
- AI: 설계 / 분석 / 구현 / 검증 / 배포 전담

---

*이 문서는 Stage 진행에 따라 버전업된다.*
