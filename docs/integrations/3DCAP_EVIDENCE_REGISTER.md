# 3DCAP — Evidence and Verification Register

**Audit date:** 2026-11-24  
**Current pinned upstream SHA:** `001f2dc2cf6947244db89e640e39749ff07eceec`  
**Previous CI-tested SHA:** `b72561384a2a5a1b838167e534bb32eac756c9be`  
**Upstream PR:** https://github.com/metsam-mastem/3DCAP/pull/1

## Current-head CI

Latest run: [45308358035](https://github.com/metsam-mastem/3DCAP/actions/runs/45308358035), current pin `001f2dc2cf6947244db89e640e39749ff07eceec` — **IN_PROGRESS** at the last check.
- Android verify job: Gradle setup in progress; unit tests, lint and APK steps pending.
- Windows script parse job: PowerShell 5.1 parse in progress; PowerShell 7 pending.
- No conclusion is claimed for this run until GitHub reports completion.

## Previous run evidence

[Run 45308073649](https://github.com/metsam-mastem/3DCAP/actions/runs/45308073649), previous SHA `b72561384a2a5a1b838167e534bb32eac756c9be`:
- Windows PowerShell 5.1 and PowerShell 7 syntax: PASS.
- Android unit tests: PASS; Gradle reported BUILD SUCCESSFUL for `testDebugUnitTest`.
- Android Lint: FAIL — 7 errors / 8 warnings. The first diagnostic reported Camera2 interop opt-in usage annotated with Kotlin `@OptIn`, while the CameraX marker uses AndroidX's experimental annotation contract.
- Debug APK and artifact upload: SKIPPED after Lint failed.

A focused correction is committed on the current pin: `Camera2CalibrationReader.kt` now uses `@androidx.annotation.OptIn(ExperimentalCamera2Interop::class)`. The current-head CI run must confirm whether this resolves all seven Lint errors.

Earlier run [45303631813](https://github.com/metsam-mastem/3DCAP/actions/runs/45303631813) on CameraX 1.6.0 failed at Kotlin compilation because `ListenableFuture` was unavailable. CameraX 1.6.1 was then adopted; the official release notes identify a fix for that regression.

## Current implementation/verification boundary

| Area | Evidence | Status |
|---|---|---|
| Capture planner | Kotlin implementation/tests | IMPLEMENTED IN SOURCE |
| CameraX capture UI | MainActivity and dependencies | IMPLEMENTED IN SOURCE |
| Session store | Manifest, local storage, recovery/export | IMPLEMENTED IN SOURCE |
| Capture Passport | Model, analyzer, JSON/text report | IMPLEMENTED IN SOURCE |
| Dataset ZIP | Passport, manifest, report, images and hash checks | IMPLEMENTED IN SOURCE |
| COLMAP runner | Windows orchestration script | IMPLEMENTED IN SOURCE |
| Current-head Android tests | Run 45308358035 pending | IN_PROGRESS |
| Current-head Lint | Run 45308358035 pending | IN_PROGRESS |
| Current-head APK | Run 45308358035 pending | NOT_RUN |
| Physical Android device | No device report | NOT_RUN |
| Windows + real COLMAP | No real dataset run | NOT_RUN |
| Sensor-to-JPEG calibration mapping | Not implemented | NOT_IMPLEMENTED |
| Intrinsic solver | Profile/sample contracts only | NOT_IMPLEMENTED |
| Full virtual tour | Manifest/validator only | PARTIAL |

## Required next evidence

**Android CI:** complete run 45308358035; if any Lint errors remain, inspect the full report and fix them without adding an unjustified baseline. Then require unit tests, lint and debug APK upload to PASS on one SHA.

**Physical device:** record device/OS, build SHA, permission flow, camera/lens, orientation, frame count, retake/delete, export and independent ZIP verification.

**Desktop reconstruction:** record Windows/COLMAP versions, input ZIP hash, profile, stage logs/exit codes, sparse files and dense `fused.ply` size/hash.

**Calibration:** measure sensor-to-JPEG mapping with a calibration target and record reprojection error before exporting intrinsics to COLMAP.

All claims refer to the exact source revision stated. This register is an EKTA audit snapshot, not a substitute for upstream CI.


## EKTA current-pin validation

The current EKTA integration head `242be3743d5312010ff320378700a384f8bd5217` passed [EKTA validation run 45308430619](https://github.com/metsam-mastem/EKTA/actions/runs/45308430619).

The workflow completed recursive submodule checkout, pinned-project verification, documentation validation, EKTA unit/runtime tests, explorer HTML/JavaScript validation and typed knowledge-graph export. This run validates the EKTA-side connection to the current 3DCAP gitlink `001f2dc2cf6947244db89e640e39749ff07eceec`. It does not validate the Android app or real reconstruction.
