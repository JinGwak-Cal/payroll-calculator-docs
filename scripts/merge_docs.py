#!/usr/bin/env python3
"""
merge_docs.py
absolute-rules.md / current-step.md / decisions.md 를 병합하여
merged-context.md 를 재생성한다.

절대 규칙:
- index.md 는 건드리지 않는다.
- 소스 3개 파일은 수정하지 않는다.
- merged-context.md 만 생성/덮어쓰기 한다.
"""

import sys
import re
from datetime import datetime, timezone
from pathlib import Path

# ── 경로 설정 ──────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
SOURCES = [
    ("absolute-rules.md", REPO_ROOT / "absolute-rules.md"),
    ("current-step.md",   REPO_ROOT / "current-step.md"),
    ("decisions.md",      REPO_ROOT / "decisions.md"),
]
OUTPUT = REPO_ROOT / "merged-context.md"
INDEX  = REPO_ROOT / "index.md"          # 절대 건드리지 않음 — 존재 확인용만


# ── V-1: 소스 파일 존재 확인 ────────────────────────────────
def check_existence(sources):
    missing = [name for name, path in sources if not path.exists()]
    if missing:
        print(f"[FAIL] V-1: 소스 파일 없음 → {missing}", file=sys.stderr)
        sys.exit(1)
    print("[OK] V-1: 소스 파일 3개 모두 존재")


# ── V-2: 0바이트 확인 ─────────────────────────────────────
def check_not_empty(sources):
    empty = [name for name, path in sources if path.stat().st_size == 0]
    if empty:
        print(f"[FAIL] V-2: 빈 파일 발견 → {empty}", file=sys.stderr)
        sys.exit(1)
    print("[OK] V-2: 소스 파일 모두 비어 있지 않음")


# ── V-3: current-step.md 에 ← 현재 마커 1개 존재 확인 ────────
def check_current_marker(sources):
    _, path = next((s for s in sources if s[0] == "current-step.md"), (None, None))
    content = path.read_text(encoding="utf-8")
    markers = re.findall(r"←\s*현재", content)
    if len(markers) == 0:
        print("[FAIL] V-3: current-step.md 에 '← 현재' 마커가 없음", file=sys.stderr)
        sys.exit(1)
    if len(markers) > 1:
        print(f"[WARN] V-3: '← 현재' 마커가 {len(markers)}개 — 중복 확인 필요")
    else:
        print("[OK] V-3: '← 현재' 마커 1개 확인")


# ── V-4: absolute-rules.md 필수 헤더 존재 확인 ───────────────
def check_absolute_rules_headers(sources):
    _, path = next((s for s in sources if s[0] == "absolute-rules.md"), (None, None))
    content = path.read_text(encoding="utf-8")
    required = ["# 구조1 앱 코드 규칙", "# 구조2 작업 시작 및 문서 확보"]
    missing = [h for h in required if h not in content]
    if missing:
        print(f"[FAIL] V-4: absolute-rules.md 필수 헤더 없음 → {missing}", file=sys.stderr)
        sys.exit(1)
    print("[OK] V-4: absolute-rules.md 필수 헤더 확인")


# ── V-5: decisions.md 날짜시간 형식 + 결정 상태값 확인 ──────────
def check_decisions(sources):
    _, path = next((s for s in sources if s[0] == "decisions.md"), (None, None))
    content = path.read_text(encoding="utf-8")

    # 날짜시간 형식 (YYMMDDHHmm — 10자리 숫자)
    if not re.search(r"\d{10}", content):
        print("[FAIL] V-5: decisions.md 날짜시간(YYMMDDHHmm) 없음", file=sys.stderr)
        sys.exit(1)

    # 결정 상태값 존재 여부
    status_keywords = ["확정", "보류", "폐기"]
    if not any(kw in content for kw in status_keywords):
        print("[WARN] V-5: decisions.md 에 결정 상태값(확정/보류/폐기) 없음")
    else:
        print("[OK] V-5: decisions.md 날짜시간 + 결정 상태값 확인")


# ── index.md 안전 확인 (건드리지 않음, 존재만 로그) ──────────────
def check_index_untouched():
    if INDEX.exists():
        print(f"[OK] index.md 존재 확인 (자동화 대상 아님 — 건드리지 않음)")
    else:
        print("[WARN] index.md 없음 (자동화와 무관)")


# ── 병합 실행 ──────────────────────────────────────────────
def merge(sources):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        f"<!-- Auto-generated at {timestamp} -->",
        f"<!-- Source: absolute-rules.md + current-step.md + decisions.md -->",
        f"<!-- index.md 는 이 파일의 생성 대상이 아닙니다 -->",
        "",
    ]

    for name, path in sources:
        content = path.read_text(encoding="utf-8").rstrip()
        lines.append(f"# ── {name} ──────────────────────────────────────")
        lines.append("")
        lines.append(content)
        lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] merged-context.md 생성 완료 ({OUTPUT})")
    print(f"     타임스탬프: {timestamp}")


# ── 메인 ──────────────────────────────────────────────────
def main():
    validate_only = "--validate-only" in sys.argv

    if validate_only:
        print("=== merge_docs.py 검증 전용 모드 ===")
    else:
        print("=== merge_docs.py 시작 ===")

    check_existence(SOURCES)
    check_not_empty(SOURCES)
    check_current_marker(SOURCES)
    check_absolute_rules_headers(SOURCES)
    check_decisions(SOURCES)
    check_index_untouched()

    if validate_only:
        print("=== 검증 완료 (생성 생략) ===")
    else:
        merge(SOURCES)
        print("=== 완료 ===")


if __name__ == "__main__":
    main()
