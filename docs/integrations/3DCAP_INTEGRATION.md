# 3DCAP Integration into EKTA

**Audit:** 2026-11-24 | **Status:** PROPOSED — integration PR review pending  
**Upstream:** https://github.com/metsam-mastem/3DCAP  
**Pinned branch:** `feat/android-guided-capture-mvp`  
**Pinned commit:** `d0ca3a689631dda944a783d61562ef70564fcd2f`  
**Upstream PR:** [#1 — Android guided-capture MVP](https://github.com/metsam-mastem/3DCAP/pull/1), open/Draft  
**EKTA source path:** `integrations/3dcap`

## 1. Integration boundary

3DCAP remains an independently governed project. EKTA connects to its complete source tree through a Git submodule pinned to an exact commit. No application source, documentation, image or other upstream asset is copied into EKTA-owned files or relicensed by this change.

- 3DCAP remains authoritative for its Android application, capture/session logic, Capture Passport, dataset export, COLMAP handoff, tests, build configuration and project roadmap.
- EKTA remains authoritative for cross-domain taxonomy, canonical concept identities, typed knowledge relationships, research synthesis, architecture decisions and portfolio navigation.
- The submodule pin is a reproducible source reference. It does not imply that upstream PR #1 is merged or release-ready.
- Update the pin only through a reviewed EKTA change with refreshed source, license, dependency and CI evidence.
- No new canonical EKTA concept IDs or taxonomy relations are created by this integration. Candidate mappings are kept in the crosswalk pending duplicate-ID and evidence review.

## 2. Product definition

3DCAP is an Android-first, offline-first guided multi-view object-capture workspace. Its intended lifecycle is:

`Capture → Dataset Validation → Reconstruction Handoff → 3D Output → Virtual Tour`

The current development baseline implements guided acquisition, local session integrity, dataset evidence and a desktop reconstruction handoff. The complete photogrammetry engine and tour authoring experience are not claimed as complete.

Core responsibilities:
1. Guide multi-view image acquisition using a deterministic yaw/pitch plan.
2. Store images and session metadata locally.
3. Report planner coverage, repeated views and available camera metadata.
4. Produce a versioned Capture Passport with explicit evidence and limitations.
5. Export a portable ZIP containing source images, manifest and Passport.
6. Validate and hand off a dataset to desktop COLMAP.
7. Define a future offline virtual-tour data contract.

## 3. Source inventory

The full upstream repository is available at `integrations/3dcap`. Important areas:

| Upstream path | Responsibility |
|---|---|
| `app/src/main/java/studio/threedcap/MainActivity.kt` | Compose application shell, camera preview and capture UI |
| `core/CapturePlanner.kt` | Spherical 36-target capture plan |
| `core/OrientationCalibration.kt`, `StabilityGate.kt` | Orientation calibration and stability gate |
| `core/FrameQualityAnalyzer.kt`, `DatasetQualityAnalyzer.kt` | Luma signal and planner/metadata diagnostics |
| `core/CapturePassport*.kt`, `PassportTextReport.kt` | Typed evidence passport, analysis, JSON and text report |
| `core/CameraCalibrationProfile.kt`, `Camera2SensorCalibration.kt` | Calibration contract and raw Camera2 factory metadata |
| `data/CaptureSessionStore.kt` | Local session storage, recovery and ZIP export |
| `data/CameraExifReader.kt`, `Camera2CalibrationReader.kt` | EXIF and optional Camera2 metadata |
| `core/ColmapWorkflowPlan.kt` | Reconstruction stages and artifact contract |
| `tour/TourManifest.kt` | Initial scene/hotspot/route model |
| `app/src/test/` | Kotlin unit and session/ZIP contract tests |
| `tools/windows/Invoke-3DCapColmap.ps1` | Windows archive validation and COLMAP runner |
| `docs/` | Architecture, requirements, Passport, evidence, build, research, user and tour docs |
| `.github/workflows/android.yml` | Android build/test and PowerShell syntax workflow |

The source submodule is the complete code connection. EKTA's dossiers are synthesis and navigation, not a second copy of the app.

## 4. Architecture findings

### Capture geometry
The default plan has 12 azimuth sectors at 30° and 3 pitch bands (-25°, +15°, +55°), totaling 36 planner targets. This is an angular coverage scaffold, not proof of physical surface visibility, image overlap, parallax quality or reconstructability.

### Session manifest
The versioned manifest records session/frame identity, sequence, filename/path, timestamp, planner yaw/pitch, byte size, SHA-256 and optional camera metadata. Planner angles are target metadata, not camera extrinsics.

### Capture Passport
The Passport is a portable evidence snapshot, not a 3D model or calibration certificate. Schema v1 records session identity, planner identifier, frame count, coverage, typed checks, findings, limitations and remediation.

The ZIP contract includes `passport.json`, `passport-report.txt`, `manifest.json`, `COLMAP_IMPORT.txt` and `images/`. Missing measurements must remain `NOT_MEASURED`, never silently become PASS. Planner-cell coverage does not prove geometric completeness.

### Integrity
The exporter verifies registered image paths, byte sizes and SHA-256 while streaming the archive. The Windows runner independently checks archive paths, manifest entries, sizes and hashes before starting COLMAP.

## 5. Calibration and coordinate boundary

EXIF is descriptive metadata, not a calibrated intrinsic matrix or per-image camera pose. Optional Camera2 factory values remain in raw sensor/pre-correction coordinates. The current implementation does not establish the transformation to saved CameraX JPEG after crop, scale, rotation or distortion correction. Raw values must not be passed to COLMAP as saved-image intrinsics until that mapping is measured and validated.

The typed calibration profile and sample-diversity gate are contracts. Checkerboard/ChArUco detection, intrinsic solving, profile persistence and calibration UI remain incomplete.

## 6. Reconstruction and tour boundary

The Windows runner is intended to invoke COLMAP feature extraction, exhaustive matching, sparse mapping, image undistortion, PatchMatch stereo and stereo fusion. It validates sparse model files and expected dense `fused.ply`.

The runner passed PowerShell syntax parsing in Windows PowerShell 5.1 and PowerShell 7 in the latest observed run. A real Windows + dataset + COLMAP reconstruction remains **NOT_RUN**.

The tour manifest defines scenes, panorama assets, hotspots and routes. Panorama stitching/rendering, interactive navigation, hotspot authoring and tour packaging remain deferred.

## 7. Build/runtime snapshot

| Setting | Pinned development configuration |
|---|---|
| Language/UI | Kotlin, Jetpack Compose |
| Camera | CameraX 1.6.0; optional Camera2 interop |
| Android | minSdk 26, compileSdk 36, targetSdk 35 |
| Build | AGP 8.9.1, Gradle 8.11.1, JDK 17 |
| Metadata | AndroidX ExifInterface 1.3.7 |
| Tests | JUnit 4.13.2; org.json 20240303 |
| Operation | Offline-first; session data stored app-private |
| Network | No INTERNET permission in inspected initial manifest |

The repository has no checked-in Gradle wrapper; CI provisions Gradle 8.11.1. Exact versions are recorded in the upstream build files.

## 8. Current maturity and verification

At pinned commit `d0ca3a689631dda944a783d61562ef70564fcd2f`:
- Capture planning, camera UI, local session storage, metadata extraction, Passport contracts/analysis, ZIP export and Windows COLMAP handoff code are present.
- Latest observed CI: [run 45303631813](https://github.com/metsam-mastem/3DCAP/actions/runs/45303631813), overall **FAIL**.
- PowerShell 5.1 and PowerShell 7 syntax: **PASS**.
- Android unit-test job: **FAIL** during Kotlin compilation at `:app:compileDebugKotlin`; test assertions did not complete.
- Reported diagnostics include inaccessible `com.google.common.util.concurrent.ListenableFuture`, unresolved `addListener`, `unbindAll`, `bindToLifecycle`, and a missing `name` argument diagnostic.
- Android Lint and Debug APK steps: **SKIPPED**.
- Physical Android device: **NOT_RUN**.
- Real Windows/COLMAP dataset reconstruction: **NOT_RUN**.
- Saved-JPEG calibration mapping and intrinsic solver: **NOT_IMPLEMENTED**.
- Full interactive virtual tour: **NOT_IMPLEMENTED**.

Do not infer test success, APK availability or end-to-end readiness from source presence.

## 9. EKTA workspace connection

- **DISCOVERY:** camera acquisition, photogrammetry, image-quality evidence, COLMAP, dataset formats, calibration and virtual-tour sources.
- **ENCYCLOPEDIA:** distinct concepts and mechanisms with stable IDs, source provenance and typed relations.
- **DECISION LAB:** mobile vs desktop reconstruction, CameraX/Camera2 coordinate handling, COLMAP profiles, offline trade-offs and licensing.
- **EXECUTION LAB:** build/test commands, capture procedures, dataset validation, export and reconstruction playbooks.

See the [knowledge crosswalk](3DCAP_KNOWLEDGE_CROSSWALK.md), [evidence register](3DCAP_EVIDENCE_REGISTER.md), [license/dependency review](3DCAP_LICENSE_DEPENDENCY_REVIEW.md) and [execution handoff](3DCAP_EXECUTION_HANDOFF.md).

## 10. Reproducible checkout

```bash
git clone --recurse-submodules https://github.com/metsam-mastem/EKTA.git
# or, in an existing checkout:
git submodule update --init --recursive
git -C integrations/3dcap rev-parse HEAD
```

Expected 3DCAP revision: `d0ca3a689631dda944a783d61562ef70564fcd2f`.

## 11. Integration work packages

| ID | Work package | Acceptance evidence |
|---|---|---|
| 3DCAP-EKTA-01 | Pin full source tree and register project boundary | Exact submodule SHA and independent authority |
| 3DCAP-EKTA-02 | Crosswalk EKTA taxonomy and relations | Reviewed mapping; no duplicate IDs or unapproved taxonomy changes |
| 3DCAP-EKTA-03 | Register architecture, Passport and data contracts | Source-linked dossiers |
| 3DCAP-EKTA-04 | Validate submodule URL/path/pin in EKTA CI | CI detects pin drift and broken source checkout |
| 3DCAP-EKTA-05 | Close upstream build/device/desktop evidence gaps | Green CI plus device and reconstruction reports |
| 3DCAP-EKTA-06 | Complete license and dependency review | Explicit license decision and notices |
| 3DCAP-EKTA-07 | Promote candidate concepts into canonical EKTA records | Duplicate search, stable IDs, sources and validated relations |

## 12. Audit limitations

This is a source-tree, documentation, dependency-manifest and CI metadata review. It is not a legal opinion, device test, security audit, image-quality benchmark or proof of successful COLMAP reconstruction. Refresh the audit whenever the submodule pin changes.


## Complete source inventory

The pinned source tree contains a complete file-by-file index at [3DCAP Source Inventory](3DCAP_SOURCE_INVENTORY.md). The submodule itself remains the canonical source; this inventory is generated navigation, not copied source code.
