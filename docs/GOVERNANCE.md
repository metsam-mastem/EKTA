# EKTA Governance

## Authority
The repository maintainer is final authority for scope, canonical taxonomy, license, security policy, and releases. Contributors propose changes through pull requests or RFCs.

## Change classes
| Class | Examples | Minimum control |
|---|---|---|
| Editorial | Typo, clarity | Review |
| Knowledge | Concept, definition, source | Schema and provenance review |
| Taxonomy | Domain, layer, relation | Impact analysis and review |
| Architecture | Graph model, tooling | RFC/ADR and tests |
| Governance | License, status, contribution policy | Explicit maintainer approval |
| Security | Dependency, script, workflow | Security review and tests |

## Source hierarchy
Prefer normative standards and official specifications; official project documentation and source; peer-reviewed research and institutional publications; reproducible technical reports; recognized books; community discussions. This is a preference, not an absolute ranking. Record conflicts, versions, and limitations.

## Integrity
Cite sources for material claims. Record publication/version and access dates. Distinguish source statements from EKTA interpretation. Do not copy protected standards or third-party code without permission. Preserve upstream notices. Never commit secrets or private data. Do not claim tests, audits, builds, or deployments passed without evidence.

## Review gates
Concepts: definition, scope, aliases, taxonomy, relationships, evidence, counterexamples.  
Tools: upstream URL, license, maintenance, security, platform requirements, fit.  
Standards: issuer, exact designation, edition, status, scope, access.  
Code: tests, input validation, error handling, dependency review, documentation, license compatibility.

## Versioning
Use semantic versioning when releases stabilize. Concept records have their own revisions. Breaking schema or ID changes require migration plans.

## Conflicts
Preserve conflicting claims with provenance and explain context. Do not silently overwrite disputed definitions. Use RFCs for unresolved project-wide questions.
