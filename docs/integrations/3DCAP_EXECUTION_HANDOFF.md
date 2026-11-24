# 3DCAP — Execution Handoff and Parallel Workstreams

**Snapshot:** 2026-11-24 | **Source SHA:** `b72561384a2a5a1b838167e534bb32eac756c9be`  
**Upstream PR:** https://github.com/metsam-mastem/3DCAP/pull/1  
**EKTA branch:** `integration/3dcap-capture-reconstruction-v0.1`

## Operating rule
Keep 3DCAP and EKTA as distinct projects. 3DCAP implementation changes stay in its own repository/branch/PR. EKTA receives source references, reviewed knowledge, decisions, evidence and navigation. Do not create a competing copy of the app.

## Parallel workstreams

| Stream | Repo boundary | Priority | Next task | Acceptance evidence |
|---|---|---:|---|---|
| A — Android build recovery | 3DCAP | P0 | Verify CameraX 1.6.1 compile-classpath correction with fresh CI; resolve any remaining compiler diagnostics | Unit tests, lint and APK PASS on one SHA |
| B — Passport/data contract | 3DCAP | P1 | Verify JSON invariants, partial EXIF semantics and fail-closed export | Unit + ZIP tests PASS; archive inspected |
| C — Device validation | 3DCAP | P1 | Install APK; test permissions, orientation, capture, retake/delete and export | Device report with OS/build SHA |
| D — Desktop reconstruction | 3DCAP | P1 | Run Windows COLMAP on a real Passport ZIP | Logs, run-summary, sparse model and fused.ply |
| E — Calibration | 3DCAP | P2 | Measure Camera2 sensor-to-JPEG transform and solve calibration target | Reprojection report and validated mapping |
| F — Source connection | EKTA | P0 | Review .gitmodules, gitlink and source checkout | Submodule resolves to exact pin |
| G — Knowledge crosswalk | EKTA | P1 | Search existing IDs and promote selected concepts | No duplicate IDs; valid source-backed records |
| H — License/dependency governance | Both | P0 | Resolve 3DCAP license and audit dependency notices | Published license and reviewed inventory |
| I — Integration validation | EKTA | P2 | Add CI checks for submodule URL/path/pin | CI detects pin drift |

## Dependencies
- A blocks build/test success and device validation.
- B can be reviewed in parallel; runtime validation waits for A.
- C requires a built APK.
- D requires a real exported dataset and compatible Windows/COLMAP.
- E must finish before raw Camera2 intrinsics are passed downstream.
- F/G can proceed independently of Android build recovery.
- H blocks vendoring and redistribution, not a source submodule reference.

## Release gates
1. Exact source pin and reproducible checkout.
2. Android unit tests, lint and APK build PASS.
3. Device capture and ZIP export validated.
4. Passport and image integrity independently verified.
5. COLMAP stage logs and required sparse/dense artifacts validated.
6. Sensor-to-JPEG calibration mapping validated.
7. Tour viewer, authoring and package validated.
8. License and dependency terms resolved.

## Pin update protocol
Fetch upstream commit and PR state; inspect source diff, docs, dependencies, license and CI; update gitlink and evidence in one EKTA PR; run EKTA validation; retain review until checks pass.

## Explicit limitation
No autonomous background process runs between chat turns. Work continues when another execution turn is initiated. This handoff does not claim a 3DCAP CI pass, physical-device pass, Windows reconstruction pass or license approval.
