# OR-0000 Traceability Index (실행 중)

| ID | Type | Parent ID | Root Pilot ID | Related IDs | Current Stage | Status |
|---|---|---|---|---|---|---|
| PI-0000 | Contract | — | PI-0000 | — | P0 | Active |
| SI-0001 | Source Intake | PI-0000 | PI-0000 | — | P1 | Complete |
| EP-0001 | Evidence Plan | PI-0000 | PI-0000 | SI-0001 | P2 | In Progress |
| OB-log(4건) | Observation | EP-0001 | PI-0000 | — | P2 | Complete |
| ER-0001 | Evidence Register | EP-0001 | PI-0000 | OB-001 | P2 | Complete |
| ER-0002 | Evidence Register | EP-0001 | PI-0000 | OB-002 | P2 | Complete(제한적) |
| FR-0001 | Finding | ER-0001,ER-0002 | PI-0000 | — | P3 | Complete (Method Finding, Insufficient) |
| EP-0002 | Evidence Plan | PI-0000 | PI-0000 | SI-0001 | P2 | Complete |
| ER-0003 | Evidence Register | EP-0002 | PI-0000 | OB-005,OB-006,OB-007,OB-008 | P2 | Complete |
| FR-0002 | Finding | ER-0003 | PI-0000 | — | P3 | Complete (Method Finding, Supported) |
| EP-0003 | Evidence Plan | PI-0000 | PI-0000 | SI-0001 | P2 | Complete |
| ER-0004 | Evidence Register | EP-0003 | PI-0000 | — | P2 | Complete |
| FR-0003 | Finding | ER-0004 | PI-0000 | — | P3 | Complete (Method Finding, Confirmed) |
| WD-0001 | Walkthrough | PI-0000 | PI-0000 | FR-0001,FR-0002,FR-0003 | P4 | Complete (재현성 간이형, 나머지 3항목 정식 통과) |
| CR-001 | Change Request | FR-0002 | PI-0000 | FR-0001 | P5 | Applied(v0.2) |
| CR-002 | Change Request | FR-0003 | PI-0000 | — | P5 | Applied(v0.2) |
| CR-003 | Change Request | WD-0001 | PI-0000 | — | P5 | Applied(v0.2) |
| XD-0001 | Exit Decision | PI-0000 | PI-0000 | FR-0001,FR-0002,FR-0003,WD-0001,CR-001,CR-002,CR-003 | P5 | **Complete — Revise & Re-Pilot** |
