# Engineering Terminology and Concept Boundaries

Status: PROPOSED reference guide. Purpose: clarify terms surfaced by the 2021 note and prevent category errors in EKTA records.

## 1. Software development assets

| Term | Definition | Boundary |
|---|---|---|
| Programming language | Formal language used to express computations and program behavior | Not an IDE, runtime, or SDK |
| Library | Reusable implementation exposing callable functionality to a consuming program | The caller generally controls when library functions are invoked |
| Framework | Reusable structure establishing conventions and often controlling application flow through inversion of control | May contain or depend on libraries |
| SDK | Platform- or service-oriented development kit containing some combination of APIs, libraries, tools, documentation, examples, emulators, or test utilities | A bundle/category, not a single executable |
| JDK | Java Development Kit; Java-specific development kit and tool distribution | Concrete ecosystem-specific development kit/toolchain |
| API | Contract through which software capabilities are exposed to consumers | Interface contract, not necessarily its implementation |
| ABI | Binary-level interface contract covering calling conventions, symbols, data layout, and compatibility | Lower-level than most source APIs |
| IDL | Interface Definition Language describing interfaces, operations, and data types independently of a particular implementation | Description language; generated bindings/stubs are separate artifacts |
| Protocol | Rules and message formats governing communication between participants | May be described by an IDL/schema, but is not identical to one |
| Runtime | Execution environment and supporting services available while a program runs | Not the same as compiler or development kit |
| Compiler | Translator transforming source or intermediate representations into another representation | May be one tool inside an SDK |
| Interpreter | Program that executes a language representation by interpreting or evaluating it | Real systems may combine interpretation and compilation |
| Toolchain | Coordinated set of tools used to build, test, package, sign, or release software | Broader than a compiler |
| IDE | Integrated development environment combining editing and development tools | Commonly orchestrates external toolchains |
| Package | Distribution unit containing software and metadata | Distinct from package format and package manager |
| Module | Unit of code organization and encapsulation defined by a language or platform | May be distributed inside a package |
| Plugin | Extension loaded by a host through an extension contract | Requires host compatibility and lifecycle rules |
| Middleware | Software mediating between components, layers, or services | Meaning depends on architecture context |

## 2. Architecture and design

| Term | Definition | Boundary |
|---|---|---|
| Architecture | Fundamental organization of a system, embodied in elements, relationships, environment, and principles governing design and evolution | Not merely a diagram |
| Architecture description | Work product expressing an architecture through views, models, and rationale | ISO/IEC/IEEE 42010 distinguishes architecture from its description |
| Architecture viewpoint | Conventions for constructing and interpreting a view to address stakeholder concerns | A viewpoint defines rules; a view is produced using them |
| Architecture view | Representation of a system from a particular viewpoint | A system may have multiple consistent views |
| Structure | Arrangement of elements and relationships | One structure may be part of an architecture description |
| Component | Encapsulated system element with defined responsibilities and interfaces | Granularity is context-dependent |
| Module | Code-level or design-level unit of organization | May or may not be independently deployable |
| Interface | Boundary contract through which elements interact | Can be software, electrical, mechanical, or human-facing |
| Design pattern | Reusable named solution structure for a recurring design problem in context | Not a finished implementation |
| Architectural style | Family of architectural organization rules and constraints | Broader than an individual design pattern |
| ADR | Architecture Decision Record documenting context, decision, alternatives, and consequences | Records rationale; does not replace the architecture |

## 3. Planning and management

| Term | Definition | Boundary |
|---|---|---|
| Strategy | Long-term direction and choices for achieving objectives under constraints | Answers why and where |
| Governance | Allocation of authority, accountability, decision rights, policies, and oversight | Not synonymous with project management |
| Portfolio | Collection of investments, projects, products, or programs managed to strategic objectives | Selection and balance |
| Program | Coordinated management of related projects and activities to realize combined benefits | Not simply a large project |
| Project | Temporary endeavor undertaken to create a unique product, service, or result | Bounded objective and lifecycle |
| Product | Offering that creates value for a defined user/customer context and evolves over time | May outlive many projects |
| Plan | Arrangement of work, sequence, resources, dependencies, schedule, and controls | Management artifact, not the work itself |
| Schedule | Time-oriented representation of activities, dependencies, milestones, and dates | One part of planning |
| Execution | Performance of planned or authorized work | Requires monitoring and control |
| Operations | Ongoing activities sustaining a system or service in use | Distinct from temporary delivery |
| Management | Coordinating people, resources, decisions, and work toward objectives | Different from governance, though connected |

### Plan families

- strategic and business plans;
- product and portfolio plans;
- project management plans;
- engineering, technical, and architecture plans;
- development and implementation plans;
- quality and verification plans;
- security, safety, and risk plans;
- resource, staffing, procurement, and supplier plans;
- financial, cost, and benefits plans;
- release, deployment, transition, operations, and maintenance plans;
- communication, configuration, and documentation plans;
- contingency, continuity, and recovery plans.

Plans are classified by concern, not as sequential lifecycle stages. A project may maintain one integrated management plan with subordinate plans. Do not create a separate plan document for every label unless governance, risk, contract, or scale justifies it.

## 4. Documentation and information products

| Artifact | Purpose |
|---|---|
| Concept note | Captures an early idea, context, assumptions, and questions |
| Business case | Justifies an initiative through options, costs, benefits, and risks |
| Charter | Authorizes an initiative and states purpose, scope, authority, and success conditions |
| Requirement specification | Defines verifiable needs, constraints, and acceptance conditions |
| System/software specification | Describes required properties and behavior of a system or software item |
| Architecture description | Communicates architecture through viewpoints, views, models, and rationale |
| Design description | Explains detailed structural and behavioral design |
| Interface/API reference | Describes interface elements and their contracts |
| Developer guide | Helps developers perform development tasks and understand contribution conventions |
| Tutorial | Teaches a newcomer through a guided learning experience |
| How-to guide | Gives steps to accomplish a specific task |
| User manual | Explains how intended users operate a product |
| Installation guide | Explains prerequisites, installation, configuration, and initial verification |
| Operations runbook | Gives repeatable procedures for operating or responding to known conditions |
| Maintenance manual | Supports diagnosis, repair, update, and preventive maintenance |
| Test plan | Defines test scope, strategy, resources, schedule, environment, and responsibilities |
| Test case | Defines preconditions, inputs, actions, and expected results |
| Test report | Records execution, results, deviations, and evidence |
| Release notes | Summarizes changes, compatibility, known issues, and upgrade considerations |
| Decision record | Captures a decision, rationale, alternatives, and consequences |
| Research report | Synthesizes a question, method, sources, findings, limitations, and implications |

## 5. Source, reference, standard, policy, and evidence

- Source: origin from which information or an artifact is obtained.
- Reference: a source explicitly cited or consulted to support a statement or decision.
- Standard: published consensus or normative document established by a recognized body or community.
- Regulation: legally binding rule issued by an authorized regulator or legislature.
- Specification: documented set of requirements, properties, interfaces, or constraints.
- Requirement: a need, capability, condition, or constraint to be satisfied by a system, product, process, or organization.
- Policy: approved high-level rule or intent governing decisions and behavior.
- Procedure: defined sequence or method for performing an activity.
- Guideline: recommended practice that permits contextual judgment.
- Convention: agreed recurring practice or naming/format rule.
- Best practice: context-dependent practice supported by credible experience or evidence; not automatically mandatory.
- Evidence: inspectable information supporting a claim, decision, or verification result.
- Conformance: fulfillment of specified requirements within a stated scope, edition, and assessment basis.
- Certification: formal attestation by an authorized body under a defined scheme; not implied by internal testing.

## 6. Documentation design: Diátaxis

Organize technical assistance around four reader needs:
1. Tutorials — learning through guided lessons.
2. How-to guides — accomplishing a task.
3. Reference — precise description of the system.
4. Explanation — understanding concepts, context, and rationale.

This complements rather than replaces role-based manuals, governance documents, specifications, or engineering records.

## 7. Quality and evidence vocabulary

- Verification: objective evidence that specified requirements have been fulfilled.
- Validation: objective evidence that the resulting system/product satisfies intended use and stakeholder needs in its operational context.
- Testing: execution or evaluation activity designed to reveal behavior, defects, or requirement compliance.
- Inspection/review: examination of an artifact or process without necessarily executing it.
- Quality assurance: planned and systematic activities providing confidence quality requirements will be fulfilled.
- Quality control: operational techniques used to fulfill quality requirements and identify nonconformities.
- Risk: effect of uncertainty on objectives; record context, likelihood, consequence, treatment, and owner.
- Hazard: condition or source with potential to cause harm; analyze separately from general project risk.
- Failure mode: specific manner in which an item or process can fail to perform a required function.

## 8. Primary references

- SWEBOK Guide V4.0a: https://www.computer.org/education/bodies-of-knowledge/software-engineering/resources/
- SWEBOK V4.0 topics: https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics
- ISO/IEC/IEEE 15288:2023: https://www.iso.org/standard/81702.html
- ISO/IEC/IEEE 42010:2022: https://www.iso.org/standard/74393.html
- NASA Systems Engineering Handbook: https://www.nasa.gov/reference/systems-engineering-handbook/
- Diátaxis: https://diataxis.fr/

This guide paraphrases public descriptions and defines EKTA-local terminology boundaries. It does not reproduce copyrighted normative clauses, grant access to standards, or establish conformance.
