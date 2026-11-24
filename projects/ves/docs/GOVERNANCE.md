# VES Engineering Governance

## Status vocabulary
PROPOSED, DRAFT, IN REVIEW, ACCEPTED, IMPLEMENTED, VERIFIED, DEPRECATED. Implementation and verification are separate states.

## Change protocol
1. Record requirement and rationale.
2. Write/update acceptance tests before behavior changes.
3. Implement the smallest vertical slice.
4. Run focused tests and then full project tests.
5. Review security, data loss, licensing and portability.
6. Record evidence and update status.
7. Submit branch/PR; never write directly to EKTA main.

## Evidence rules
No PASS without executable evidence. No Windows/Android support claim without installation/runtime tests on target devices. No standards-conformance claim without versioned conformance fixtures.

## Independence
VES documentation, source, schemas and setup instructions must be sufficient to understand and run VES without the originating chat. EKTA is its knowledge/governance host, not a runtime dependency.
