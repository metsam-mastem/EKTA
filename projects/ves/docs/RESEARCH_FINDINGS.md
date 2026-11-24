# VES Research Findings and Technology Decision Brief

**Date:** 2026-11-24  
**State:** Decision-ready preliminary research; not a final legal or conformance audit.

## 1. Central finding

No single existing modeling language or visual editor is sufficient for a universal engineering workbench spanning software, hardware, firmware, data, process, materials and organizational systems. The strongest architecture is a shared semantic model with multiple domain-specific notations and interchangeable visual renderers.

The key product distinction is therefore not “a prettier UML editor”. It is a model-first workbench in which one engineering entity can appear as a card, node, diagram element, form record, document section or physical assembly item without creating duplicate source records.

## 2. Standards are complementary, not competing

| Standard / notation | Best-fit problem | VES role |
|---|---|---|
| UML | Software structure and behavior | Software view adapter |
| SysML v2 / KerML | Systems engineering, requirements, structure, behavior and constraints | Primary systems-engineering interchange candidate |
| C4 | Software architecture communication at multiple abstraction levels | Architecture visualization profile |
| ArchiMate | Enterprise architecture and business/technology relationships | Organization and enterprise view |
| BPMN 2.0 | Business and operational process flows | Process view |
| ERD | Data entities and relationships | Data model view |
| OpenAPI / AsyncAPI | HTTP and event-driven interface contracts | Interface contract adapter |
| EDA / HDL | Electronic design and digital hardware description | Specialist hardware exchange |
| CAD / mechanical formats | Geometry, parts and assemblies | External specialist integration |

### Consequence
VES should not force all objects into UML classes or SysML blocks. It should define its own small, typed, versioned interchange model and map to standards through explicit adapters. Each adapter reports supported constructs, unsupported constructs and conversion loss.

## 3. Open-source tool findings

| Project | Strength | Limitation / integration boundary | Recommendation |
|---|---|---|---|
| XYFlow / React Flow | Interactive node/edge canvases, custom nodes and handles | It is a rendering/interaction toolkit, not a semantic engineering repository | Preferred candidate for the production Board renderer |
| Excalidraw | Fast freeform drawing and whiteboard interaction | Freehand diagrams do not automatically provide typed engineering semantics | Optional Freeform Board adapter |
| Eclipse SysON | SysML v2-oriented system modeling environment | Specialist modeling product; maturity, APIs, deployment and supported views need feature-by-feature validation | Keep as external SysML adapter candidate |
| Eclipse Sirius Web | Framework for custom graphical modeling workbenches | Greater framework and model-runtime complexity | Evaluate only if VES needs deep custom semantic editors |
| bpmn-js / form-js | Mature BPMN rendering/editing and form components | BPMN-specific; review bpmn.io licensing and watermark conditions | Optional process adapter |
| KiCad | Full specialist schematic and PCB workflow | Separate engineering tool and license boundary; not a generic card canvas | External tool integration and file exchange |
| Penpot | Design systems, UI assets and collaborative interface design | Not an engineering semantic-model engine | Design-system research/reference |

### Recommended composition
1. XYFlow for connected engineering boards.
2. A separate freeform renderer for sketch-like boards.
3. SysON as an optional external systems-modeling integration.
4. bpmn-js for BPMN-specific editing.
5. KiCad for schematic/PCB specialist work.
6. VES-owned model and adapters as the stable center.

Do not embed or fork all candidate projects. Prefer file/API boundaries and preserve the ability to replace each renderer.

## 4. Why the model-first decision matters

A drawing tool stores shapes and lines. An engineering workbench must store identity, type, properties, constraints, ports, relationships, provenance, evidence and version.

Therefore:
- Entity is the canonical engineering object.
- Card is a visual projection of an Entity.
- Placement is a Board-local position reference.
- Relationship is a typed semantic edge.
- Board is a composition/view, not a separate data source.
- Deck is a reusable catalog of definitions/references.
- Form is a typed editing and validation contract.

This separation enables multiple views without duplicate entities and permits renderer replacement without data migration.

## 5. Local-first and resource strategy

For the first releases, SQLite plus versioned JSON interchange is preferable to mandatory cloud infrastructure:
- no server cost for a single-user workspace;
- offline operation;
- inspectable backups;
- easy repository-based review;
- simple migration path toward a future team service.

SQLite is a persistence adapter, not the semantic model itself. Git is suitable for reviewable snapshots and project artifacts, not as a high-frequency concurrent database.

## 6. License and provenance gates

A public repository or a visible GitHub source tree is not, by itself, permission to copy or embed code. Before adoption, record exact package/version, license file, transitive dependencies, notices, security advisories and distribution obligations.

Specific cautions:
- XYFlow and Excalidraw list permissive licensing upstream; preserve license notices and verify the exact package release.
- bpmn.io licensing has watermark-related conditions for applicable usage; inspect current terms before distribution.
- KiCad program, documentation and libraries have distinct licensing terms; keep it outside the VES process boundary initially.
- SysON and Sirius Web require review of their EPL ecosystem, deployment dependencies and APIs.
- Do not treat a candidate listing in this report as legal clearance.

## 7. Technology decisions for VES 0.1

| Concern | Decision |
|---|---|
| Canonical model | VES-owned, renderer-independent |
| First core runtime | Python standard library |
| Local persistence | SQLite |
| Interchange | Versioned JSON + JSON Schema |
| First visual prototype | Dependency-free HTML/CSS/JS |
| Production board candidate | React + TypeScript + XYFlow |
| Freeform candidate | Excalidraw adapter |
| Systems notation | SysML v2/KerML adapter, not a core dependency |
| Process notation | BPMN adapter |
| Hardware design | KiCad external integration |
| Cloud | Optional later capability, not a prerequisite |

## 8. Research limitations and open questions

- No controlled performance benchmark has been run on the target Redmi phone or Lenovo device.
- No browser usability test has been completed.
- No Windows or Android package has been built.
- No full SysML v2 or UML round-trip conformance suite exists yet.
- Candidate license notes are preliminary; legal review is still required before shipping dependencies.
- The current prototype is not a production multi-board editor and does not yet expose the Python Form Engine as a visual Form Builder.

## 9. Next evidence to collect

1. Compare XYFlow and Excalidraw under the same 500-node/1,000-edge synthetic board.
2. Test the browser prototype on desktop, Android phone and low-resource hardware.
3. Build a SysML v2 import/export fixture set and quantify semantic loss.
4. Test SQLite project sizes, startup time, save latency and backup/restore.
5. Run accessibility checks for keyboard operation, contrast and touch targets.
6. Complete a package-by-package license and security review before production dependency selection.

## Primary sources
- OMG SysML specification: https://www.omg.org/spec/SysML
- OMG SysML v2 adoption announcement: https://www.omg.org/news/releases/pr2025/07-21-25.htm
- XYFlow repository: https://github.com/xyflow/xyflow
- Excalidraw repository: https://github.com/excalidraw/excalidraw
- Eclipse SysON repository: https://github.com/eclipse-syson/syson
- Eclipse Sirius Web: https://github.com/eclipse-sirius/sirius-web
- bpmn-js repository: https://github.com/bpmn-io/bpmn-js
- KiCad licensing: https://www.kicad.org/about/licenses/
- Penpot repository: https://github.com/penpot/penpot
