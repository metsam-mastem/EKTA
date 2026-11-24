# 3DCAP — Evidence and Verification Register

**Audit date:** 2026-11-24 | **Pinned SHA:** `d0ca3a689631dda944a783d61562ef70564fcd2f`  
**Upstream PR:** https://github.com/metsam-mastem/3DCAP/pull/1

| Area | Evidence | Status | Boundary |
|---|---|---|---|
| Source | Branch `feat/android-guided-capture-mvp` at pinned SHA | OBSERVED | PR is Draft, not merged |
| Capture planner | Kotlin implementation and tests present | IMPLEMENTED IN SOURCE | Not proof of surface visibility |
| CameraX UI | MainActivity and CameraX dependencies present | IMPLEMENTED IN SOURCE | Latest compile failed |
| Session store | Manifest, local storage, recovery/export code | IMPLEMENTED IN SOURCE | Latest test gate failed |
| Capture Passport | Model, analyzer, JSON/text report and docs | IMPLEMENTED IN SOURCE | Assertions did not complete in latest CI |
| Dataset ZIP | Passport, manifest, report, images and integrity checks | IMPLEMENTED IN SOURCE | Phone export NOT_RUN |
| COLMAP runner | Windows PowerShell orchestration source | IMPLEMENTED IN SOURCE | End-to-end NOT_RUN |
| PowerShell 5.1 parse | CI run 45303631813 | PASS | Syntax only |
| PowerShell 7 parse | CI run 45303631813 | PASS | Syntax only |
| Android unit tests | CI run 45303631813 | FAIL | Kotlin compilation failed before tests |
| Android Lint | CI run 45303631813 | SKIPPED | Earlier step failed |
| Debug APK | CI run 45303631813 | SKIPPED | No artifact established by this run |
| Physical Android device | No device report found | NOT_RUN | Permissions, orientation, performance unverified |
| Windows + real COLMAP | No real dataset run found | NOT_RUN | Sparse/dense outputs not established |
| JPEG calibration mapping | Design boundary documented | NOT_IMPLEMENTED | Sensor coordinates not mapped to saved JPEG |
| Intrinsic solver | Profile/sample contracts only | NOT_IMPLEMENTED | No checkerboard/ChArUco solver |
| Virtual tour | Manifest/validator model | PARTIAL | Viewer, authoring and export deferred |

## Latest CI failure

[Run 45303631813](https://github.com/metsam-mastem/3DCAP/actions/runs/45303631813), commit `d0ca3a689631dda944a783d61562ef70564fcd2f`, overall **FAIL**. The `Unit tests` step failed during Kotlin compilation at `:app:compileDebugKotlin`. Reported diagnostics:
- Cannot access `com.google.common.util.concurrent.ListenableFuture`.
- Unresolved `addListener`, `unbindAll` and `bindToLifecycle`.
- A further missing `name` argument diagnostic.

The current evidence does not prove these diagnostics share one root cause. Inspect the Gradle dependency graph and exact call sites before choosing a fix. Test assertions did not complete; Lint and APK steps were skipped.

## Evidence required next

**Android CI:** fix compile diagnostics, then run unit tests, lint and debug APK build on one recorded commit.

**Physical device:** record device/OS, build SHA, permission flow, camera/lens, orientation, frame count, retake/delete, export and ZIP verification.

**Desktop reconstruction:** record Windows/COLMAP versions, input ZIP hash, profile, stage logs/exit codes, sparse files and dense `fused.ply` size/hash.

**Calibration:** measure sensor-to-JPEG mapping with a calibration target and record reprojection error before exporting intrinsics to COLMAP.

All claims refer to the pinned upstream revision. This register is an EKTA audit snapshot, not a substitute for upstream tests.
