# EKTA Master Taxonomy

EKTA separates a top-level navigation portfolio from three independent classification axes. These registries are the source of truth; this document explains their roles and does not replace their machine-readable IDs.

## A. Top-level Engineering Territories — 26

The approved navigation/portfolio map contains 26 territories. Canonical identifiers and explicit domain mappings are stored in `taxonomy/territories.yml`.

1. Engineering Sciences and Mathematics
2. Systems Engineering
3. Software Engineering
4. Computer Science
5. Operating Systems and Platform Engineering
6. Data Engineering and Database Systems
7. Networking and Telecommunications
8. Distributed Systems and Cloud Infrastructure
9. Artificial Intelligence, Machine Learning, and Agents
10. Electronics and Semiconductors
11. Computer Architecture and Processor Engineering
12. Chip Design
13. PCB and Electronic Systems Design
14. Firmware and Embedded Systems
15. Mechanical, Materials, and Manufacturing Engineering
16. Robotics, Control, and Mechatronics
17. Security, Safety, and Resilience Engineering
18. Testing, Verification, Validation, and Quality Engineering
19. Workflow and Process Engineering
20. Automation Engineering
21. UX, UI, and Human–Machine Interaction
22. Operations and Reliability Engineering
23. Product Engineering
24. Project Engineering and Development Management
25. Documentation, Standards, and Engineering Governance
26. Applied and Interdisciplinary Engineering

Territories organize top-level browsing and portfolio completeness. A territory may have zero associated concepts today; this is a content-coverage gap, not a missing taxonomy node.

## B. Operational Engineering Domains — 25

Operational domains are more granular tags for classifying records. The stable IDs and labels below are governed by `taxonomy/domains.yml`.

1. Software Engineering
2. Computer Engineering and Architecture
3. Operating Systems and Platform Engineering
4. Data Engineering and Database Systems
5. Networking and Telecommunications
6. Electrical and Electronic Engineering
7. Semiconductor and Integrated Circuit Engineering
8. Embedded Systems and Firmware
9. Mechanical Engineering
10. Materials Science and Manufacturing
11. Systems Engineering and Systems Architecture
12. Control Engineering and Automation
13. Robotics and Mechatronics
14. Artificial Intelligence and Machine Learning Systems
15. Cybersecurity and Privacy Engineering
16. Safety, Reliability, and Resilience Engineering
17. Human Factors, UX, UI, and HMI
18. DevOps, SRE, and Operations Engineering
19. Product and Project Engineering
20. Energy and Power Systems
21. Aerospace, Automotive, and Transportation Systems
22. Media, Graphics, Simulation, and Game Engineering
23. Testing, Verification, Validation, and Quality Engineering
24. Workflow and Process Engineering
25. Documentation, Standards, and Engineering Governance

A single operational domain may map to multiple territories. Those mappings are explicit in `taxonomy/territories.yml`; they must not be inferred from label similarity.

## C. Engineering Layers — 10

Canonical IDs, order, and labels are in `taxonomy/layers.yml`.

1. Mission, business, and requirements
2. Human, experience, and interaction
3. Application, agent, and domain logic
4. Workflow, orchestration, and process
5. Service, API, and data
6. Platform, framework, and runtime
7. Operating system and system services
8. Firmware, drivers, and embedded control
9. Hardware architecture and computation
10. Circuit, physical, mechanical, and manufacturing

Cross-cutting concerns include security, safety, performance, reliability, observability, interoperability, maintainability, accessibility, cost, and sustainability.

## D. Knowledge Types — 30

Canonical values are in `taxonomy/knowledge-types.yml`: concept, principle, architecture, component, interface, pattern, anti-pattern, technique, method, algorithm, data-structure, process, workflow, standard, specification, tool, framework, platform, metric, model, failure-mode, hazard, research, evidence, decision, test, playbook, checklist, implementation, and example.

## E. Relationship Predicates

Canonical predicates are in `taxonomy/relations.yml`. Current vocabulary includes IS_A, PART_OF, USES, DEPENDS_ON, IMPLEMENTS, EXTENDS, CONTROLS, EXECUTES, SCHEDULES, OBSERVES, CONNECTS_TO, CONSUMES, PRODUCES, VERIFIED_BY, DEFINED_BY, ALTERNATIVE_TO, COMPETES_WITH, RELATED_TO, SUPERSEDES, and DERIVED_FROM.

Each relationship must have explicit direction, a controlled predicate, stable subject/target identifiers, and provenance or a stated review status.

## F. Classification Rules

- Territory is a navigation/portfolio layer; it is not interchangeable with operational domain.
- Domain, layer, and knowledge type are orthogonal classification axes.
- Multi-tagging is allowed; do not force a concept into only one domain or layer.
- Runtime is a concept; Workflow Runtime is a scoped specialization.
- An implementation is not the concept it implements.
- A tool is not a technique; a standard is not a tool.
- A workflow is not necessarily an engine.
- A layer is an architectural position, not an engineering discipline.
- Stable IDs are immutable and never recycled.
