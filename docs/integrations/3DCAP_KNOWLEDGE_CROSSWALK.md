# 3DCAP — EKTA Knowledge Crosswalk

**Status:** PROPOSED mapping; no canonical concept IDs created  
**Source:** [pinned 3DCAP source](../../integrations/3dcap) at `d0ca3a689631dda944a783d61562ef70564fcd2f`  
**Taxonomy authority:** `taxonomy/territories.yml`, `domains.yml`, `layers.yml`, `knowledge-types.yml`, `relations.yml`

## Rules
- Keep Territory, Domain, Layer and Knowledge Type as independent axes.
- Use only existing registry IDs. Do not create taxonomy values to fit one project.
- Search existing and pending concept IDs before promotion.
- 3DCAP is an implementation reference, not the definition of photogrammetry, camera calibration or dataset provenance.
- Every graph edge requires existing endpoints, context and provenance.

## Candidate territories
| EKTA territory | Relevance |
|---|---|
| `software-engineering` | Android application, Kotlin logic, persistence and export |
| `systems-engineering` | Capture-to-reconstruction lifecycle and interfaces |
| `computer-science` | Image processing, geometry, coordinate transforms and hashing |
| `operating-systems-platform-engineering` | Android runtime, CameraX/Camera2 and Windows execution |
| `data-engineering-databases` | Session manifest, JSON, archive and integrity evidence |
| `firmware-embedded-systems` | Device sensor/camera interface boundary only |
| `testing-verification-validation-quality` | Passport, unit tests, archive validation and CI |
| `workflow-process-engineering` | Capture plan, export and reconstruction stages |
| `ux-ui-human-machine-interaction` | Guided operator workflow and evidence presentation |
| `applied-interdisciplinary-engineering` | Photogrammetry, 3D reconstruction and virtual tours |

## Candidate operational domains
Use existing identifiers: `software-engineering`, `computer-engineering`, `operating-systems-platforms`, `data-engineering`, `embedded-firmware`, `systems-engineering`, `testing-verification-validation-quality`, `workflow-process-engineering`, `human-factors-ux`, `media-graphics-simulation`, `electrical-electronic` (camera/sensor boundary only), `documentation-standards-governance`.

## Candidate engineering layers
- `human-experience`: guided capture, readiness and remediation.
- `application-agent`: Android capture application, Passport analyzer and tour model.
- `workflow-orchestration`: multi-view plan, export and COLMAP stages.
- `service-data`: manifest, Passport JSON, ZIP and evidence.
- `platform-runtime`: Android/CameraX and Windows/COLMAP execution.
- `operating-system`: Android storage/permissions and Windows process/filesystem boundary.
- `firmware-control`: camera/sensor control boundary; not app firmware.
- `hardware-architecture`: camera sensor metadata and device capability.
- `physical-implementation`: lens, sensor optics and physical capture constraints.

## Candidate knowledge types
`architecture`, `component`, `interface`, `workflow`, `specification`, `tool`, `model`, `evidence`, `test`, `implementation`, `research`, `playbook`.

## Candidate concept family — not yet canonical
| Concept | EKTA relevance | 3DCAP evidence |
|---|---|---|
| Multi-view image acquisition | Structured acquisition for reconstruction | CameraX capture flow |
| Spherical coverage planning | Discrete yaw/pitch target coverage | 12 × 3 planner |
| Structure-from-Motion (SfM) | Camera poses and sparse geometry | COLMAP mapper handoff |
| Multi-View Stereo (MVS) | Dense geometry from overlapping views | PatchMatch/stereo fusion stages |
| Photogrammetry dataset | Reproducible image package | manifest + images + Passport |
| Capture Passport | Portable evidence and dataset identity | schema v1 |
| Camera intrinsic calibration | Pixel-to-ray mapping | Profile contract; solver pending |
| Camera extrinsics / pose | Camera pose in a reference frame | Not inferred from planner angles |
| Sensor-to-image transform | Crop/scale/rotation/distortion mapping | Known unresolved boundary |
| Dataset integrity | Corruption and duplicate detection | SHA-256 and byte-size validation |
| Image-quality measurement | Focus, blur, overlap, exposure | Many metrics remain NOT_MEASURED |
| Sparse reconstruction model | Cameras, registered images, 3D points | COLMAP artifact contract |
| Dense point cloud | Fused 3D points | Expected `fused.ply` |
| Virtual-tour scene graph | Panoramas, hotspots and routes | Manifest contract only |

## Candidate typed relations
Use existing predicates only: `IMPLEMENTS`, `USES`, `DEPENDS_ON`, `PRODUCES`, `CONSUMES`, `VERIFIED_BY`, `PART_OF`, `RELATED_TO`, `DERIVED_FROM`. All remain proposed until endpoint records and evidence exist.
