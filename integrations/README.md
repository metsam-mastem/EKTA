# External Project Integrations

This directory contains pinned Git submodules for independently governed engineering projects that EKTA references or orchestrates.

## GTC — Gadget Time Capsule

- Canonical upstream: https://github.com/metsam-mastem/GTC
- Local path: `integrations/gtc`
- Pinned upstream commit: `2f0229bd622de4e9ce22196e57fb986659dc7934`
- Integration record: [GTC integration and audit](../docs/integrations/GTC_INTEGRATION.md)

The submodule preserves GTC as an independent project and exposes its complete source tree at the pinned revision. Do not copy GTC data into EKTA's canonical knowledge store without claim-level provenance and a license review. Update the pin only through a reviewed EKTA change.

## 3DCAP — Guided 3D Capture

- Canonical upstream: https://github.com/metsam-mastem/3DCAP
- Local path: `integrations/3dcap`
- Pinned commit: `001f2dc2cf6947244db89e640e39749ff07eceec`
- Upstream branch: `feat/android-guided-capture-mvp`
- Upstream PR: [#1](https://github.com/metsam-mastem/3DCAP/pull/1), Draft
- Audit: [3DCAP integration record](../docs/integrations/3DCAP_INTEGRATION.md)
- Crosswalk: [3DCAP → EKTA](../docs/integrations/3DCAP_KNOWLEDGE_CROSSWALK.md)
- Evidence: [CI and verification](../docs/integrations/3DCAP_EVIDENCE_REGISTER.md)

The submodule exposes the complete upstream source tree. 3DCAP remains authoritative for its application and tests. EKTA does not copy or relicense that source. Update the pin only through a reviewed change with refreshed CI, license and dependency evidence.
