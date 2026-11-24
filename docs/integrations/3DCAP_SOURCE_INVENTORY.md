# 3DCAP — Complete Pinned Source Inventory

**Upstream:** https://github.com/metsam-mastem/3DCAP  
**Pinned commit:** `b72561384a2a5a1b838167e534bb32eac756c9be`  
**EKTA submodule:** `integrations/3dcap`  
**Inventory generated from:** Git tree API at the pinned commit, recursive=true  
**Tree entries:** 71 total; **50 files** and 21 directories. The tree response was not truncated.

This is a path inventory, not a license grant or a claim that every source file has passed tests. The full file contents are available through the pinned submodule.

## 1. Root and build
- `README.md`
- `build.gradle.kts`
- `gradle.properties`
- `settings.gradle.kts`

## 2. Android application and core/data/tour source
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/studio/threedcap/MainActivity.kt`
- `app/src/main/java/studio/threedcap/core/CalibrationSampleSetAnalyzer.kt`
- `app/src/main/java/studio/threedcap/core/Camera2SensorCalibration.kt`
- `app/src/main/java/studio/threedcap/core/CameraCalibrationProfile.kt`
- `app/src/main/java/studio/threedcap/core/CaptureManifest.kt`
- `app/src/main/java/studio/threedcap/core/CapturePassport.kt`
- `app/src/main/java/studio/threedcap/core/CapturePassportAnalyzer.kt`
- `app/src/main/java/studio/threedcap/core/CapturePassportJson.kt`
- `app/src/main/java/studio/threedcap/core/CapturePlanner.kt`
- `app/src/main/java/studio/threedcap/core/ColmapWorkflowPlan.kt`
- `app/src/main/java/studio/threedcap/core/DatasetQualityAnalyzer.kt`
- `app/src/main/java/studio/threedcap/core/FrameQualityAnalyzer.kt`
- `app/src/main/java/studio/threedcap/core/OrientationCalibration.kt`
- `app/src/main/java/studio/threedcap/core/PassportTextReport.kt`
- `app/src/main/java/studio/threedcap/core/StabilityGate.kt`
- `app/src/main/java/studio/threedcap/data/Camera2CalibrationReader.kt`
- `app/src/main/java/studio/threedcap/data/CameraExifReader.kt`
- `app/src/main/java/studio/threedcap/data/CaptureSessionStore.kt`
- `app/src/main/java/studio/threedcap/tour/TourManifest.kt`

## 3. Automated tests
- `app/src/test/java/studio/threedcap/core/CalibrationSampleSetAnalyzerTest.kt`
- `app/src/test/java/studio/threedcap/core/Camera2SensorCalibrationContractTest.kt`
- `app/src/test/java/studio/threedcap/core/CameraCalibrationProfileTest.kt`
- `app/src/test/java/studio/threedcap/core/CaptureManifestTest.kt`
- `app/src/test/java/studio/threedcap/core/CapturePassportTest.kt`
- `app/src/test/java/studio/threedcap/core/CapturePlannerTest.kt`
- `app/src/test/java/studio/threedcap/core/ColmapWorkflowPlanTest.kt`
- `app/src/test/java/studio/threedcap/core/DatasetQualityAnalyzerTest.kt`
- `app/src/test/java/studio/threedcap/core/FrameQualityAnalyzerTest.kt`
- `app/src/test/java/studio/threedcap/core/OrientationCalibrationTest.kt`
- `app/src/test/java/studio/threedcap/core/StabilityGateTest.kt`
- `app/src/test/java/studio/threedcap/data/CaptureSessionStoreTest.kt`
- `app/src/test/java/studio/threedcap/tour/TourValidatorTest.kt`

## 4. Project documentation
- `docs/ARCHITECTURE.md`
- `docs/BUILD.md`
- `docs/CAPTURE_PASSPORT_DATA_CONTRACT.md`
- `docs/CAPTURE_PASSPORT_IMPLEMENTATION_PLAN.md`
- `docs/CAPTURE_PASSPORT_SPEC.md`
- `docs/QUALITY_EVIDENCE_MODEL.md`
- `docs/REQUIREMENTS.md`
- `docs/RESEARCH_REGISTER.md`
- `docs/TOUR_FORMAT.md`
- `docs/USER_GUIDE.md`

## 5. Windows reconstruction tooling
- `tools/windows/Invoke-3DCapColmap.ps1`

## 6. CI workflows
- `.github/workflows/android.yml`

## 7. Retrieve and verify
```bash
git submodule update --init --recursive
git -C integrations/3dcap rev-parse HEAD
git -C integrations/3dcap ls-tree -r --name-only HEAD
```

Expected commit: `b72561384a2a5a1b838167e534bb32eac756c9be`.

## 8. Inventory limits
The inventory records paths at one exact commit. It does not include Git history objects outside that commit, Git LFS payloads if any, untracked local files, build outputs or generated datasets. Refresh it whenever the submodule pointer changes.
