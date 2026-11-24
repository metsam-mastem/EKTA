# ECPS Research Register

**Research snapshot:** 2026-11-24 · Primary/official sources preferred.  
This register records design relevance and constraints; it does not claim ECPS conformance or implementation.

| Reference | Relevance | ECPS decision / limit |
|---|---|---|
| [OMG SysML v2](https://www.omg.org/spec/SysML) | Formal system structure, behavior, requirements, analysis and verification | UMSF/VEL adapter research reference; no SysML conformance claim |
| [OMG SysML v2 overview](https://www.omg.org/sysml/SysML-2.htm) | Textual and graphical notation, formal semantics and standardized API | Study for system model exchange; do not duplicate its semantics unnecessarily |
| [OpenMath 2.0](https://openmath.org/standard/) | Machine-readable mathematical object semantics | MUA semantic payload adapter candidate |
| [W3C MathML Core](https://www.w3.org/TR/mathml-core/) | Browser mathematical notation and rendering | Renderer/interchange candidate, not a physical geometry contract |
| [W3C MathML 4](https://www.w3.org/TR/mathml4/) | Broader mathematical markup work | Reviewed as Working Draft; monitor status before implementation |
| [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) | Structural interchange validation | Used for ECPS manifest; semantic cross-reference rules remain Python/application checks |
| [UCUM](https://ucum.org/ucum) | Machine-readable unit codes and semantics | Candidate unit profile; no ECPS unit algebra/parser implemented |
| [FMI 3.0.2](https://fmi-standard.org/docs/3.0.2/) | Dynamic model exchange and co-simulation | Simulation adapter candidate; not a general architecture graph |
| [FMI reference repository](https://github.com/modelica/fmi-standard) | Standard sources, schemas, API headers and release history | Pin exact version and capability profile for any future adapter |
| [OpenModelica FMI guide](https://openmodelica.org/doc/OpenModelicaUsersGuide/OpenModelicaUsersGuide-latest.pdf) | Tool-specific FMI support | Support differs by version/interface; validate exact workflow before claiming compatibility |
| [FreeCAD API](https://www.freecad.org/api/) | Parametric CAD and geometric model integration | CAD adapter candidate; MUA frame/units mapping must be explicit |
| [Three.js WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer) | Browser 3D rendering | Workbench renderer only; not part of the canonical model or core contract |
| [VEL foundation PR #10](https://github.com/metsam-mastem/EKTA/pull/10) | Existing EKTA visual grammar | Reuse and cross-reference; do not create a duplicate visual language |
| [UMSF foundation PR #11](https://github.com/metsam-mastem/EKTA/pull/11) | Existing EKTA semantic coordinate framework | UMSF owns semantic addresses; ECPS must not reinterpret them as Cartesian coordinates |
| [MUA foundation PR #19](https://github.com/metsam-mastem/EKTA/pull/19) | Mathematical object and coordinate-frame foundation | MUA owns mathematical coordinate frames and object semantics |
| [VES foundation PR #20](https://github.com/metsam-mastem/EKTA/pull/20) | Interactive engineering workbench | VES owns board-local placement; board coordinates are not physical geometry |

## Findings

1. The user's original X/Y/Z/T idea contains at least two different mathematical objects: UMSF's semantic address `(layer ID, module ID, view-relative depth, temporal validity)` and MUA's geometric/mathematical coordinate frame. They must remain separate.
2. VES board placement is a view-layout coordinate system. It is not a physical coordinate frame.
3. VEL connections are typed port-to-port relations. A visual line or spatial proximity must not be silently converted into a semantic or physical connection.
4. UMSF already separates semantic addresses from a typed relationship graph. This prevents overloading axes with edges, breadth, scope or scale.
5. MUA already has coordinate-frame and mathematical-object schemas. ECPS should reference those rather than define another geometric frame schema.
6. A federated model is safer than an early forced-unification: each subsystem remains authoritative, while ECPS validates links and compiles synchronized view plans.
7. Schema validity, source availability, visual correctness and engineering truth are different validation levels and need separate evidence.

## Unresolved research

- Compare stable identity and alias strategies across UMSF, VEL, MUA and VES.
- Define relation-to-port mapping without inventing ports or predicates.
- Define coordinate-frame composition and dimensional/unit compatibility in MUA.
- Determine whether projection manifests should support multiple source models per view.
- Define cache invalidation and stale-projection behavior when source commits change.
- Evaluate accessible 2D rendering and low-memory fallback before adding 3D.
- Determine licensing and conformance boundaries for specialist adapters.

## Source verification policy

Re-check current standards editions and tool support at adapter implementation time. Official standards pages establish published specifications; vendor/project documentation establishes only the documented capabilities of that tool. A listed source is not evidence that ECPS has implemented or passed an adapter.
