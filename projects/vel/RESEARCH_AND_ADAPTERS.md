# VEL Research Register and Adapter Strategy

**Research snapshot:** 2026-11-24  
**Purpose:** Record external projects that informed the design. This is a curated starting register, not a complete audit of every release, dependency, or license file.

## Findings

| Project / standard | Relevant capability | Proposed VEL use | Caution |
|---|---|---|---|
| FINOS CALM / CalmStudio | Architecture-as-code, typed nodes/relationships, visual editor, JSON interchange | Software-architecture adapter and model synchronization patterns | CALM Studio has been described by FINOS as experimental; verify current maturity and schema version before production use |
| SysML v2 / Eclipse SysON | Systems engineering model, graphical and textual representations | Systems/hardware domain profile and future adapter | SysON has been in incubation; validate feature coverage and implementation maturity |
| Eclipse Sirius Web | Domain-specific graphical modeling workbench | Reference for metamodel-driven editors | Heavier server/client stack; likely unsuitable for the first low-resource MVP |
| React Flow / xyflow | Custom nodes, edges, handles, interactive graph canvas | Primary candidate for the first web canvas | UI library only; VEL semantics and persistence remain our responsibility |
| Rete.js | Visual programming, dataflow/control-flow processing | Optional execution-oriented graph engine | Do not add alongside React Flow without a demonstrated need |
| Excalidraw | Free-form sketching and diagram interchange | Sketch intake and annotation adapter | Not a typed engineering model by itself |
| ELK / elkjs | Automatic graph layout, ports, nested graphs | Layout engine for complex VEL diagrams | Layout output must not change semantics |
| D2 | Text-to-diagram language and multiple layout engines | Diagram export adapter | Export mapping may be lossy |
| LikeC4 | Architecture-as-code and multiple architecture views | Software architecture export/reference | Domain coverage is narrower than universal VEL |
| Structurizr / C4 | Multiple views from one architecture model | Viewpoint and abstraction-level design | C4 focuses on software architecture |
| Archi / ArchiMate | Enterprise architecture viewpoints and relationships | Organization/business/technology profile | Distinguish ArchiMate semantics from VEL core |
| EventStorming | Physical collaborative modeling with colored cards | Physical card workshop method | Color conventions are method-specific, not universal VEL semantics |
| ComfyUI | Node graph workflows, reusable subgraphs, JSON workflows | Workflow profile and reusable pattern inspiration | GPL-3.0; evaluate license compatibility before code reuse |
| Node-RED | Event-driven flow editor and device/service integrations | Automation profile and interoperability reference | Runtime and node ecosystem have their own security model |
| BehaviorTree.CPP | Hierarchical control and behavior trees | Decision/sequence/selector profile | Specialized runtime semantics |
| KiCad | Typed electrical symbols, pins, nets, design checks | Electronics profile and physical port inspiration | GPL-3.0 and additional component/library terms require review |

## Primary project links

- CALM: https://github.com/finos/architecture-as-code
- SysON: https://github.com/eclipse-syson/syson
- Sirius Web: https://github.com/eclipse-sirius/sirius-web
- React Flow: https://github.com/xyflow/xyflow
- Rete.js: https://github.com/retejs/rete
- Excalidraw: https://github.com/excalidraw/excalidraw
- ELK: https://github.com/kieler/elkjs
- D2: https://github.com/terrastruct/d2
- LikeC4: https://github.com/likec4/likec4
- Structurizr: https://github.com/structurizr/structurizr
- Archi: https://github.com/archimatetool/archi
- EventStorming: https://www.eventstorming.com/
- ComfyUI: https://github.com/Comfy-Org/ComfyUI
- Node-RED: https://github.com/node-red/node-red
- BehaviorTree.CPP: https://github.com/BehaviorTree/BehaviorTree.CPP
- KiCad: https://gitlab.com/kicad/code/kicad

## Selection decision

For a low-resource first increment, use a small independent VEL JSON model and Python validator. When a web canvas is implemented, evaluate React Flow first and ELK for layout. Keep Rete.js optional for cases where graph execution is required. Use CALM, SysML v2, D2, LikeC4, C4, and ArchiMate as adapters or reference models rather than making any one of them the canonical VEL model.

## License and provenance policy

- A public repository is not automatically permission to copy or redistribute its source.
- Record the exact upstream project, version/commit, license, retrieval date, and modifications before importing code.
- Prefer independent implementations of ideas and documented interfaces.
- Re-check upstream license files before shipping or vendoring dependencies.
- This register records links and design observations; it does not certify legal compatibility.
