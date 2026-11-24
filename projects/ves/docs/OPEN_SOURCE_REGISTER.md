# Open-source and Standards Candidate Register

**Review state:** preliminary candidate register; not legal clearance or compatibility certification.

| Candidate | Potential role | Current stance | License / risk gate |
|---|---|---|---|
| XYFlow / React Flow | Node/edge canvas | Preferred candidate for production board renderer | MIT stated upstream; verify exact package/version and notices |
| Excalidraw | Freeform whiteboard | Optional view/adapter; avoid blind fork | MIT; retain notices and asset attribution |
| Eclipse SysON | SysML v2 modeling | External specialist adapter candidate | Inspect EPL-2.0 and dependencies; test API and maturity |
| Eclipse Sirius Web | Custom graphical modeling | Evaluate if custom domain editors become necessary | EPL-2.0 ecosystem and deployment complexity |
| bpmn-js / form-js | BPMN and form editor | Optional BPMN adapter | Preserve bpmn.io watermark; inspect current terms |
| KiCad | Schematic/PCB | External tool and file exchange, not embedded source initially | Majority GPLv3-or-later; libraries have separate CC-BY-SA terms |
| Penpot | Design-system reference | UX research/reference, not core runtime dependency | Verify current license and self-hosting model |

## Selection criteria
License and transitive dependency review; maintenance/release cadence; import/export fidelity; offline and low-resource performance; accessibility/mobile behavior; replaceability; security posture.

## Standards candidates
SysML v2 and KerML for systems modeling; UML for software structure/behavior; C4 for software architecture views; ArchiMate for enterprise architecture; BPMN 2.0 for processes; ERD for data; OpenAPI/AsyncAPI for interface contracts; EDA/HDL formats for digital hardware. Each adapter must declare supported profile/version, unsupported constructs and conversion-loss report.

## Primary-source register
- OMG SysML: https://www.omg.org/spec/SysML — SysML v2 formal version listed with September 2025 adoption; SysML v1 remains in use during transition.
- OMG announcement: https://www.omg.org/news/releases/pr2025/07-21-25.htm — final adoption announcement for SysML v2, KerML and API/Services.
- XYFlow: https://github.com/xyflow/xyflow — upstream describes React Flow and Svelte Flow; repository states MIT.
- Excalidraw: https://github.com/excalidraw/excalidraw — upstream repository and MIT license.
- bpmn-js: https://github.com/bpmn-io/bpmn-js — upstream toolkit; license includes watermark retention condition.
- KiCad licenses: https://www.kicad.org/about/licenses/ — program, documentation and libraries have distinct license terms.

## Evidence policy
Before adoption, record official URL, exact revision, release version, license file, dependencies, security advisories, test fixtures and review date. Candidate listing does not imply production integration.
