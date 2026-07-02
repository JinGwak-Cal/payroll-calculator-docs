# Thread Closing Audit Protocol (TCA)

Version: v1.4
Status: METHODOLOGY BASELINE FROZEN
Type: Research Methodology (RM-001)
Origin: Sprint-1 Closing Review 누락 사례에서 도출
Date: 2026-07-02

---

## Part 0 — Scope

**TCA 적용 대상:**
- Thread Closing
- Sprint Closing
- Research Closing

**TCA 비적용 대상:**
- 일반 Review
- 단순 Patch
- 일상 질의응답

---

## Part 1 — Principles

### Audit First Principle

> **"기억에 의존하지 말고, Audit을 먼저 수행하라."**
> **"Closing Review는 작성하기 전에 Audit되어야 한다."**

모든 Summary, Closing Review, Sprint Review, Freeze, Promotion은 Audit 이후에만 수행한다. TCA는 그 첫 번째 구현 사례이다.

### Freeze Rationale

TCA v1.4는 현 시점의 최적 설계이기 때문에 Freeze하는 것이 아니라, Sprint-2 Engineering(ER-001)에서 실제 적용·검증하기 위한 Methodology Baseline으로 Freeze한다. 향후 변경은 실제 Engineering 수행에서 확보된 Evidence에 의해서만 Patch-Freeze Protocol을 통해 수행한다.

---

## Part 2 — Audit Objects & Domains

| Domain | Input | Activity | Output |
|---|---|---|---|
| Conversation Audit | Thread Conversation | 미완료·보류·예약 항목 추출 | Discussion Items |
| Research Audit | RN / RP / ER | 연구 상태 점검 | Research Status |
| Engineering Audit | Assets / Cards / Files | Engineering 상태 점검 | Engineering Status |
| Traceability Audit | Registry | 연결성 검증 | Registry Integrity |
| Release Audit | GitHub / Manifest | Release 상태 확인 | Release Integrity |
| Governance Audit | Operating Documents | 운영체계 검증 | Operational Integrity |

---

## Part 3 — Lifecycle

```
Conversation Audit (Domain 1)
      ↓
Research Audit (Domain 2)
      ↓
Engineering Audit (Domain 3)
      ↓
Traceability Audit (Domain 4)
      ↓
Release Audit (Domain 5)
      ↓
Governance Audit (Domain 6)
      ↓
Classification (Completed / Deferred / Cancelled)
      ↓
Decision
      ↓
Applicable Registry Update
      ↓
Closing Review 작성
      ↓
Freeze
      ↓
3-Document Update
      ↓
Thread Handoff
```

---

## Part 4 — Procedure

### Domain 1 — Conversation Audit
- 완성되지 않은 논의
- "나중에 하자"고 한 항목
- 질문만 하고 실행 안 된 것
- 보류된 논의

### Domain 2 — Research Audit
- 미착수 연구 (ER, RN 등)
- 미작성 프롬프트
- 미검증 가설
- Evidence 미확보 항목

### Domain 3 — Engineering Audit
- 생성 문서·카드·파일 vs Registry 등록 여부
- GitHub 반영 여부
- Forward Reference (예약만 된 카드)
- 미완료 Release

### Domain 4 — Traceability Audit
- 결정사항 → Evidence 연결 여부
- Patch → Registry 등록 여부
- Deferred → Registry 등록 여부

### Domain 5 — Release Audit
- GitHub main 반영 여부
- Manifest 상태
- Batch Release 대기 파일

### Domain 6 — Governance Audit
- Freeze 누락 여부
- Registry 누락 여부
- Decision 누락 여부
- Current Step 갱신 여부
- 3문서 Update 준비 여부
- Thread Handoff 준비 여부

---

## Part 5 — Classification & Decision

Audit 결과를 다음으로 분류 후 결정:

| 분류 | 의미 |
|---|---|
| Completed | 이번 Sprint에서 완료 |
| Deferred | 다음 처리 대상 — Timeline + Owner 명시 필수 |
| Cancelled | 의도적 폐기 |

**Deferred Timeline 분류:**

| Timeline | 의미 | Owner 예시 |
|---|---|---|
| Next Sprint | 다음 Sprint에서 처리 | ER-001, RN-002 |
| Research | 특정 연구에서 처리 | RN-003, ER-002 |
| Future | 미래 Sprint (시점 미정) | Architecture |
| Long-term | 장기 과제 | EM, Model |

Deferred 항목은 반드시 Timeline과 Owner를 명시한 후 Registry에 등록한다.

---

## Part 6 — Exit Criteria

- [ ] 모든 Audit Domain 완료 (Domain 1~6)
- [ ] 모든 미완료 항목 분류 완료 (Completed / Deferred / Cancelled)
- [ ] Deferred에 Timeline + Owner 명시 완료
- [ ] Applicable Registry 갱신 완료
- [ ] Closing Review 작성 완료 (3-Document Update Summary 포함)
- [ ] Freeze 완료
- [ ] 3-Document Update 완료
- [ ] Thread Handoff 완료

---

## Part 7 — TCA Outputs

TCA 수행 결과 생성되는 공식 산출물:

- Closing Review (3-Document Update Summary 포함)
- Engineering Change Registry Update
- Deferred Register Update (Timeline + Owner)
- Thread Handoff
- Next Sprint Input

Audit는 종료가 아니라 다음 Sprint의 입력을 생성하는 Engineering Process이다.

---

## Part 8 — 3-Document Update Gate

3문서(absolute-rules, decisions, current-step)는 Closing Review Freeze 후에만 갱신한다.

```
TCA Audit (Domain 1~6)
      ↓
Closing Review Freeze
      ↓
absolute-rules (검증된 Rule만)
decisions (운영 결정만)
current-step (현재 Sprint/작업만)
      ↓
Thread Handoff
```

**Closing Review 내 3-Document Update Summary 필수:**
```
## 3-Document Update Summary
absolute-rules: [추가/변경 또는 "변경 없음"]
decisions: [추가된 운영 결정]
current-step: Sprint / 주요 작업 / Deferred 건수
```

---

## Part 9 — Future Expansion

- Sprint Closing Audit
- Research Audit
- Release Audit
- Promotion Audit
- Baseline Audit
- Environment Audit (ER-001 이후)

---

*Version: v1.4 | Status: METHODOLOGY BASELINE FROZEN | RM-001 | 2026-07-02*
*첫 적용: 이 쓰레드 Closing | 다음 변경: ER-001 Evidence 기반 Patch만 허용*
