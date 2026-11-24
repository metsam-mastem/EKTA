# 3DCAP — License and Dependency Review

**Review date:** 2026-11-24 | **Upstream:** https://github.com/metsam-mastem/3DCAP  
**Pinned revision:** `b72561384a2a5a1b838167e534bb32eac756c9be` | **EKTA license:** UNDECIDED

## Licensing boundary

GitHub metadata for 3DCAP reports no declared license, and the inspected source tree has no root `LICENSE` file. EKTA also has no selected repository-wide license. Therefore this integration adds a Git submodule pointer only. It does not copy or relicense source, documentation, images or assets.

Public visibility does not grant redistribution, modification or commercial-use rights. Code extraction, vendoring, binary redistribution and third-party bundling remain blocked until ownership and license terms are explicitly resolved. This is a conservative governance decision, not a legal opinion.

## Dependency snapshot

| Component | Version / setting |
|---|---|
| Kotlin / Compose plugin | 2.0.21 |
| Android Gradle Plugin | 8.9.1 |
| Gradle / JDK | 8.11.1 / 17 |
| Android SDK | compile 36, target 35, min 26 |
| CameraX camera2/lifecycle/view | 1.6.0 |
| Compose BOM | 2024.12.01 |
| Activity Compose | 1.10.0 |
| Lifecycle Runtime KTX | 2.8.7 |
| AndroidX ExifInterface | 1.3.7 |
| JUnit / org.json | 4.13.2 / 20240303 |

The previous CI run on CameraX 1.6.0 reported unresolved `ListenableFuture` at CameraX call sites. The pinned source upgrades all CameraX artifacts to 1.6.1, whose official release notes identify a fix for this compile-classpath regression. The current pinned revision still requires a fresh CI run.

## Upstream research references

The 3DCAP Research Register treats these as research references, not copied code:
- CameraX, ARCore Depth and COLMAP official documentation.
- OpenScan project ecosystem; check each subproject license.
- MosaicEarth Capture for Android — upstream README states AGPL-3.0-or-later.
- Strata:3D — upstream README states AGPL-3.0-or-later.
- alphashape — GPL-3.0-or-later per upstream register.
- open3dscanner — CC BY-NC-SA 4.0; not suitable for unrestricted commercial reuse without separate permission.

Recheck the exact repository, license file, version and third-party notices before reuse. A README summary is not a full legal audit.

## Privacy observation

The inspected Android manifest does not declare INTERNET permission. The stated capture path stores data locally in app-private storage. This is a source-level observation, not a network-traffic audit or proof of every transitive SDK behavior.

## Closeout checklist
- [ ] Publish an explicit 3DCAP license.
- [ ] Audit transitive dependencies and notices.
- [ ] Identify third-party source, assets and sample data.
- [ ] Decide binary redistribution terms.
- [ ] Decide EKTA license separately.
- [ ] Add license compatibility checks before any future code/data extraction.
