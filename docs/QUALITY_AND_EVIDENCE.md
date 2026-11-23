# EKTA Quality and Evidence Standard

## Evidence classes
- E0 Assertion: unsupported statement or idea.
- E1 Secondary: credible secondary explanation.
- E2 Primary documentation: official specification, documentation, or source.
- E3 Reproducible evidence: executable test, benchmark, trace, or independently reproducible result.
- E4 Independent corroboration: multiple independent high-quality sources or reviews.

This is not a universal truth score. A normative standard may be authoritative for conformance but not comparative performance.

## Claim provenance
Record claim text, source IDs, source authority/type, version/date, exact section/page/line/commit, conditions, limitations, conflicts, reviewer/date, confidence, and uncertainty.

## Source quality dimensions
Authority, proximity to primary evidence, recency, reproducibility, methodological transparency, independence, scope fit, and known conflicts.

## Comparison rules
Compare like with like. Record hardware/software versions and test conditions. Distinguish theoretical peak from measured performance. Report units and methodology. Avoid conclusions from a single benchmark unless explicitly limited. Include cost, energy, latency, throughput, reliability, portability, and maintenance trade-offs when relevant.

## Verification status
PASS: acceptance criteria executed and met.  
FAIL: criteria executed and not met.  
NOT_RUN: not executed.  
BLOCKED: cannot execute due to a recorded blocker.

Source review is not implementation testing. Static inspection is not runtime validation. Passing a test does not prove untested properties.
