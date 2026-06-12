# absolute-rules-retired.md
<!-- archived from absolute-rules.md during 0611~0612 doc revision -->

## 폐기 항목

### reviews 식별자 규칙 (구버전)
| archive | sot | Archived Date | Replacement | 폐기 사유 |
|---------|-----|--------------|-------------|---------|
| y | n | 0612 | A-A-03-02-S01 | 날짜시간(YYMMDDHHmm) 포함 확정본으로 대체 |

원문:
형식: 작업단위(sub.n).파트너명.현업N-n.md

예시:
P4(1).claude.현업1-1.md   ← 서브1, 현업1, Claude 1차
P4(1).gpt.현업1-2.md      ← 서브1, 현업1, GPT 팔로업
P4(1).claude.현업1-3.md   ← 서브1, 현업1, Claude 재반영
P4(1).claude.현업2-1.md   ← 서브1, 현업2 (다른 현업)
P4(2).claude.현업1-1.md   ← 서브2, 현업1

---

### GitHub 문서 읽기 규칙 - 기존 단일 읽기 우선순위
| archive | sot | Archived Date | Replacement | 폐기 사유 |
|---------|-----|--------------|-------------|---------|
| y | n | 0612 | A-A-02-02-S01~S03 | 신규 쓰레드 / 작업 중 재진입 분기로 대체 |

원문:
우선순위:
- bash_tool 가능 시: git fetch origin 후 origin/main 기준으로 읽기
- Raw URL 직접 읽기
- blob URL 직접 읽기
- jsDelivr CDN 재시도

폐기 이유:
신규 쓰레드(새 컨테이너) vs 작업 중 재진입(로컬 repo 존재)으로
환경이 다르므로 단일 순서로 처리 불가.
구조2-목차02 서브목차01~03으로 분기 대체됨.
