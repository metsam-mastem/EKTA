# Engineering Lifecycle Crosswalk

## 1. Purpose

This document maps EKTA's knowledge organization view to lifecycle work. It is a practical crosswalk, not a mandatory waterfall sequence or a claim that every project needs every artifact.

ISO/IEC/IEEE 15288:2023 defines a common framework of system life-cycle process descriptions and allows selected processes to be applied iteratively, concurrently, and recursively. EKTA therefore treats lifecycle stages as organizing views over work, not a rigid one-way pipeline.

## 2. Lifecycle work areas

| Work area | Core questions | Typical outputs |
|---|---|---|
| Opportunity and discovery | What problem, opportunity, users, context, and evidence exist? | research brief, problem statement, stakeholder map |
| Feasibility and concept | Is the solution desirable, feasible, viable, safe, and supportable? | options analysis, concept of operations, business case |
| Requirements | What must be achieved, under which constraints, and how will acceptance be judged? | needs, requirements, constraints, acceptance criteria |
| Architecture | What fundamental structures and decisions address stakeholder concerns? | architecture description, views, ADRs, interface strategy |
| Design | How will each element be realized? | design models, detailed specifications, schemas |
| Implementation / realization | How are software, hardware, data, processes, and content built? | source, configured components, fabricated items |
| Integration | How do elements work together across boundaries? | integrated baseline, interface tests, integration records |
| Verification | Does each realized element conform to its specified requirements? | verification cases, results, objective evidence |
| Validation | Does the integrated solution satisfy intended use and stakeholder needs? | validation scenarios, user evaluation, acceptance evidence |
| Transition and deployment | How is the solution moved into its intended environment? | release, installation, migration, training, handover |
| Operations and support | How is the system operated, monitored, and supported? | runbooks, telemetry, incident and service records |
| Maintenance and evolution | How are defects, changes, obsolescence, and new needs handled? | patches, upgrades, change records, revised baselines |
| Retirement | How are services, assets, data, and obligations safely ended or transferred? | retirement plan, data disposition, archive, closure evidence |

## 3. Cross-cutting management and technical activities

These may span multiple work areas: project and technical planning; decision management; risk and opportunity management; configuration and information management; measurement and assessment; quality assurance; security, privacy, safety, resilience; supplier and acquisition management; knowledge and competency management; stakeholder communication.

## 4. Traceability chain

Need → Requirement → Architecture / Design → Decision → Implementation item → Verification / Validation case → Evidence → Release / Operational outcome.

Links can be many-to-many. Record rationale and source, not just IDs. A requirement can be verified by multiple tests; one test can cover multiple requirements. Validation evidence may be contextual and cannot always be reduced to a simple pass/fail assertion.

## 5. Gate outcomes

- PASS: required check executed and acceptance condition satisfied.
- FAIL: check executed and acceptance condition not satisfied.
- NOT_RUN: check has not been executed.
- BLOCKED: check cannot be executed because a stated dependency or condition is missing.

A plan or checklist is not evidence that work occurred. A test case is not a test result. A diagram is not proof of conformance.

## 6. Tailoring

Select and tailor lifecycle work based on consequence of failure and hazard exposure; novelty and technical uncertainty; system complexity and integration boundaries; legal, contractual, and regulatory obligations; operational lifetime and support model; team size, supplier structure, delivery cadence; and cost of producing and maintaining evidence.

Record omitted activities and rationale when risk, contract, or governance requires it.
