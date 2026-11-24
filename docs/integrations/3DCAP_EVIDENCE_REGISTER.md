# 3DCAP — Evidence and Verification Register

**Audit date:** 2026-11-24  
**Current pinned upstream SHA:** `b72561384a2a5a1b838167e534bb32eac756c9be`  
**Previous CI-tested SHA:** `d0ca3a689631dda944a783d61562ef70564fcd2f`  
**Upstream PR:** https://github.com/metsam-mastem/3DCAP/pull/1

## Current-head status

| Area | Evidence | Status | Boundary |
|---|---|---|---|
| Source | Branch `feat/android-guided-capture-mvp` at current pin | OBSERVED | PR remains Draft |
| CameraX build correction | All CameraX artifacts upgraded from 1.6.0 to 1.6.1 | COMMITTED IN SOURCE | Latest-head CI not yet observed |
| Capture planner | Kotlin implementation and tests present | IMPLEMENTED IN SOURCE | Not proof of surface visibility |
| CameraX UI | MainActivity and CameraX dependencies present | IMPLEMENTED IN SOURCE | Build not verified on current head |
| Session store | Manifest, local storage, recovery/export code | IMPLEMENTED IN SOURCE | Current-head tests NOT_RUN |
| Capture Passport | Model, analyzer, JSON/text report and docs | IMPLEMENTED IN SOURCE | Current-head tests NOT_RUN |
| Dataset ZIP | Passport, manifest, report, images and integrity checks | IMPLEMENTED IN SOURCE | Phone export NOT_RUN |
| COLMAP runner | Windows PowerShell orchestration source | IMPLEMENTED IN SOURCE | End-to-end NOT_RUN |
| Latest-head Android unit tests | No workflow run observed on current pin | NOT_RUN | Previous revision failed compilation |
| Latest-head Android Lint | No workflow run observed | NOT_RUN | — |
| Latest-head Debug APK | No workflow run/artifact observed | NOT_RUN | — |
| Physical Android device | No device report found | NOT_RUN | Permissions, orientation, performance unverified |
| Windows + real COLMAP | No real dataset run found | NOT_RUN | Sparse/dense outputs not established |
| JPEG calibration mapping | Design boundary documented | NOT_IMPLEMENTED | Sensor coordinates not mapped to saved JPEG |
| Intrinsic solver | Profile/sample contracts only | NOT_IMPLEMENTED | No checkerboard/ChArUco solver |
| Virtual tour | Manifest/validator model | PARTIAL | Viewer, authoring and export deferred |

## Previous CI failure and diagnosis

[Run 45303631813](https://github.com/metsam-mastem/3DCAP/actions/runs/45303631813) tested previous SHA `d0ca3a689631dda944a783d61562ef70564fcd2f`, not the current pin. It failed during Kotlin compilation at `:app:compileDebugKotlin`. Reported diagnostics included inaccessible `com.google.common.util.concurrent.ListenableFuture`, unresolved `addListener`, `unbindAll`, `bindToLifecycle`, and a missing `name` argument diagnostic. Android Lint and Debug APK steps were skipped.

The failure matches the documented CameraX 1.6.0 compile-classpath regression. The upstream CameraX release notes state that CameraX 1.6.1 fixes the `ListenableFuture` compile error. The current source revision upgrades camera-camera2, camera-lifecycle and camera-view to 1.6.1. This is a targeted source correction, not yet a verified build fix.

## PowerShell evidence

The previous CI run reported PowerShell 5.1 and PowerShell 7 syntax parsing as PASS. The current source pin does not change the PowerShell runner, but no new CI result has been observed on the current pin. Syntax PASS does not prove archive extraction or COLMAP execution.

## Required next evidence

**Android CI:** run unit tests, lint and debug APK build on the current pin; record exact commit and workflow run.

**Physical device:** record device/OS, build SHA, permission flow, camera/lens, orientation, frame count, retake/delete behavior, export and independent ZIP verification.

**Desktop reconstruction:** record Windows/COLMAP versions, input ZIP hash, profile, stage logs/exit codes, sparse model files and dense `fused.ply` size/hash.

**Calibration:** measure sensor-to-JPEG mapping with a calibration target and record reprojection error before exporting intrinsics to COLMAP.

All claims refer to the exact source revision stated. This register is an EKTA audit snapshot, not a substitute for upstream CI.
