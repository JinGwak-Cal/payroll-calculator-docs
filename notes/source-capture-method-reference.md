# Reference — Source Capture Method

Operation Review마다 반복 기술하지 않고 참조만 하는 공통 방법론.
(향후 저장소 재구조화 시 reference/ 폴더로 이동 예정)

| 도구 | 대상 | 기능 | 위치 |
|---|---|---|---|
| ChatGPT Exporter | GPT 전용 | 대화 쓰레드를 PDF/MD/JSON/Text로 다운로드 | 사이드바 하단 Export 버튼 — [Chrome 웹스토어](https://chromewebstore.google.com/detail/ilmdofdhpnhffldihboadndccenlnfll) |
| AI Chat Exporter | GPT+Claude 등 멀티 | 대화창에 Export 버튼 표시, MD/HTML 저장 | 화면 상주 플로팅 위젯 — [Chrome 웹스토어](https://chromewebstore.google.com/detail/elhmfakncmnghlnabnolalcjkdpfjnin) |

현재는 대화 원문 확보만 다룸. 사용자·AI 자산(파일/ZIP 등) 확보
도구는 추후 추가.

## 상태값 체계 (Source/Artifact/Evidence 공통)

Operation Review 전체에서 아래 5개 상태값을 공통으로 사용한다.

- **Available**: 확보 완료
- **Missing**: 확보 필요하나 없음
- **Need Unknown**: 필요 여부 자체가 미판정
- **Not Required**: 이번 Operation 목적에 불필요로 판정됨
- **Deferred**: 나중 Operation으로 이월
