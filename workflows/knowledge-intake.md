# Knowledge Intake Playbook

**Workflow ID:** EKTA-WFL-000001  
**Status:** PROPOSED  
**Owner:** EKTA maintainer

## Purpose

Turn an unstructured engineering question, term, source, repository, or observation into a reviewable and reusable EKTA knowledge item.

## Inputs

- A question, engineering problem, term, technique, or implementation.
- Context and scope boundaries.
- Candidate evidence URLs/files/repositories, if available.
- Desired output type: concept, technique, architecture, source, implementation, decision, test, or playbook.

## Procedure

1. **Define the gap.** Write one precise question and record what is out of scope.
2. **Capture sources.** Preserve canonical URLs, versions/commits, access dates, and reuse constraints.
3. **Assess evidence.** Identify primary vs secondary sources, known bias, staleness, and missing evidence.
4. **Normalize terminology.** Select a canonical label, aliases, language variants, and disambiguation notes.
5. **Classify.** Select territory, operational domain, engineering layer, and knowledge type from canonical registries.
6. **Create identity.** Allocate one stable EKTA ID; never reuse an existing ID.
7. **Model relationships.** Add only relations with clear predicate semantics and known target IDs. Mark unresolved links explicitly.
8. **Write the record.** Use the appropriate template and distinguish definitions, interpretations, proposals, and verified claims.
9. **Validate.** Run schema, taxonomy, link, duplicate-ID, test, and graph-export checks.
10. **Review.** Request content/evidence review and technical review as relevant.
11. **Publish.** Merge the reviewed change. Do not promote evidence status merely because the pull request merged.
12. **Apply and verify.** When the knowledge is used in a real design or workflow, record context, acceptance criteria, and outcome evidence.

## Outputs

- A canonical Git record with a stable identifier.
- Source provenance and evidence notes.
- Controlled taxonomy assignments.
- Typed relationships or explicit unresolved-link records.
- CI/test evidence and a review decision.

## Stop conditions

Stop and mark BLOCKED when source access or rights are unclear, essential context is missing, taxonomy fit is unresolved, evidence contradicts itself, or a safety/security review is required but unavailable.

## Acceptance criteria

- The item is discoverable by canonical name, aliases, ID, and relevant tags.
- Every taxonomy value exists in its registry.
- Every asserted relationship is controlled and traceable.
- Sources support the wording used.
- CI and required review gates pass.
- No unverified status promotion is present.
