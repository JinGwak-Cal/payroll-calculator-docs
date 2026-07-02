# 01. Concept Card Standard v1.0

> AI Company Concept System 문서군 중 카드 규격(Schema) 정의. 작성 규칙은 [02. Concept Manual] 참조.

---

## 1. 식별자 정책 (ID Policy)

| 구분 | 정의 | 변경 가능 여부 |
|---|---|---|
| **Concept ID** | 영구 고유 식별자. 발급 순서대로 채번. 형식: `C-00001` | **불변** — 어떤 구조 개편에도 절대 바뀌지 않는다. **삭제된 ID는 영구 결번 처리, 재사용 금지** (Git commit 철학과 동일) |
| **Coordinate(좌표)** | 현재 개념체계 안에서 이 개념이 위치한 자리(경로). 형식은 개념체계 버전에 따라 변경될 수 있다 (`T-01` 형 또는 `Theory.Hypothesis.001` 형 등 트리/그래프 모두 지원) | **가변** — 분류체계가 바뀌면 함께 바뀐다 |

모든 카드, 모든 참조(상위/하위/전/후/관련 개념)는 **Concept ID로만** 연결한다. Coordinate는 사람이 읽기 위한 라벨일 뿐, 시스템적 참조에는 쓰지 않는다.

---

## 2. 좌표 체계 (Coordinate)

- 형식: `[Type코드]-[순번]` (예: `H-01`, `WF-03`)
- 의미: 개념체계 그래프 안에서 이 개념의 **현재 위치**
- 좌표는 분류체계 버전에 종속된다. 분류체계가 개편되면 영향받는 모든 카드의 Coordinate를 일괄 갱신한다. 이때 Concept ID는 그대로 유지되므로 모든 외부 참조는 끊기지 않는다.

---

## 3. 상태 체계 (Status)

```
Candidate → Repeated → 승격심사(Promotion Review) → Promoted → Deprecated
                                                              ↘ Archived
```

| Status | 정의 |
|---|---|
| Candidate | 최초 등록. 자유 수정 가능 |
| Repeated | 2개 이상 쓰레드에서 반복 등장 확인됨 |
| Promoted | 승격 심사 통과, Asset Registry 등재, SoT 반영 자격 |
| Deprecated | 잘못된 것으로 판명되어 더 이상 사용하지 않음 |
| Archived | 틀린 건 아니지만 현재 버전에서는 쓰지 않음. 역사적 보존 목적. Deprecated와 구분 — "오류"가 아니라 "구버전" |

---

## 4. 신뢰도 체계 (Stability)

Status(승격 절차상 단계)와는 **독립된 축**이다. Status가 "공식 단계"를 말한다면, Stability는 "실제 사용 신뢰도"를 말한다. 예: Promoted 상태여도 아직 Emerging일 수 있다.

| Stability | 의미 | 예 |
|---|---|---|
| Experimental | 막 제안됨, 검증 전 | Context Threshold(이름 미확정 단계) |
| Emerging | 반복 사용되며 다듬어지는 중 | — |
| Stable | 안정적으로 통용됨 | Dispatcher |
| Core | 프로젝트 운영의 근간, 변경 시 영향 막대 | absolute-rules |

---

## 5. Concept Card 필드 전체

### 5-1. 식별 (Identification)
| 필드 | 규칙 |
|---|---|
| Concept ID | `C-00001` 형식. **불변. 영구 결번** — 삭제돼도 재사용 금지 |
| Coordinate | 현재 분류체계 안에서의 위치(경로). 형식은 버전에 따라 변경 가능 |

### 5-2. 기본 정보 (Basic Info)
| 필드 | 규칙 |
|---|---|
| 이름(한글) | 한글 우선 |
| 영문명 / 약어 | 괄호 병기 |

### 5-3. 정의 (Definition)
| 필드 | 규칙 |
|---|---|
| 공식 정의 | 1문장, 해석 여지 없이 |
| 목적 | 이 개념이 왜 필요한가 |
| 핵심 질문 | 이 개념이 무엇에 답하는가 |

### 5-4. 분류 (Classification)
| 필드 | 규칙 |
|---|---|
| Type | Type 정의는 [04. Concept Dictionary] 참조 |
| Status | 5단계 중 1개 — *승격 절차상 단계* |
| Stability | 4단계 중 1개 — *실사용 신뢰도* |

### 5-5. 관계 (Relations)
| 필드 | 규칙 |
|---|---|
| 상위 개념 | ID 1개만 (단일 상위 원칙) |
| 하위 개념 | ID 목록 |
| 관련 개념 | 횡단 참조, ID 목록 |
| Before(전 단계) | ID |
| After(후 단계) | ID |

### 5-6. 비교 (Comparison)
| 필드 | 규칙 |
|---|---|
| 기존 유사 개념 | 업계 용어명 그대로 — **절대 숨기지 않는다** |
| 차이점 | 1~2문장 |
| 용어 유형 | [05. Naming Guide] 분류 참조 |
| Official Name 후보 | 이름 미확정 개념의 경우 후보 목록만 기재 (확정 강제 안 함) |
| Semantic Boundary *(선택)* | 동일/유사 용어와 어디까지 같고 어디부터 다른지 2~3문장으로 명시. 업계 용어와 정면 충돌하는 카드(예: Context Threshold)에서 사용 권장 |

### 5-7. 근거 (Evidence)
| 필드 | 규칙 |
|---|---|
| Origin Thread | 최초 등장 쓰레드 |
| Discovery Context | 어떤 작업·논의 맥락에서 발견되었는지 1~2문장 |
| Decision Origin | 관련 결정/Closing Review ID (있는 경우) |
| Evidence | 근거 사례 ID (Case Study 등). **선택(Optional)** — Type별 권장 기준은 02. Concept Manual 참조 |

### 5-8. 관리 (Management)
| 필드 | 규칙 |
|---|---|
| Version | v0.1부터 |
| Last Updated | 날짜 |
| 변경 이력 | 간단 로그 |
| Review Result | Approved / Conditionally Approved / Change Requested |
| Review Notes | 검토 과정에서 발견된 운영 규칙 개선 사항 등 — 정의뿐 아니라 "어떻게 이 정의에 도달했는가"도 기록 |
| 비고 | 자유 기술 |

---

*Version: v1.0 | Status: Approved | 작성 규칙은 02. Concept Manual 참조*
