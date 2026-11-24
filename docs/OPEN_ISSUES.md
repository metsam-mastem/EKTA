# Open Issues and Questions

1. **Owner decision:** EKTA-ADR-0003 remains PROPOSED; approve, revise or reject the UPDS cross-cutting/separable subsystem boundary.
2. **Latest CI:** verify the latest PR #23 head after the read-only registry API and test assertion updates.
3. **Recovery drill:** clean-clone recovery without ChatGPT/chat has NOT RUN.
4. **Backup drill:** independent portable archive and restore with checksum has NOT RUN.
5. **Registry write lifecycle:** current registry is read-only list/get; create/update, revisions, audit events and approval/promotion flows are NOT IMPLEMENTED.
6. **Traceability:** full typed chain source/need → requirement → decision → component → test/run → evidence → release is NOT IMPLEMENTED.
7. **Dashboard/starter:** completeness dashboard and project starter generator are NOT IMPLEMENTED.
8. **Artifact policy:** define binary evidence storage, checksum, access, retention and external artifact references.
9. **Schema status model:** decide whether lifecycle, implementation, verification, approval and evidence maturity remain independent dimensions before expanding schema.
10. **Taxonomy mapping:** map document families to existing territories/domains/layers/types without changing canonical registry counts.
11. **License:** EKTA license remains undecided; do not add license file or infer reuse rights.
12. **External standards:** verify edition/status/rights before asserting conformance.
13. **Archive fidelity:** session archive is a structured context summary, not a verbatim raw ChatGPT transcript.
14. **PR status:** PR #23 remains draft and unmerged pending review; old PR #3 is closed, not merged.


15. **Latest manifest CI:** corrected manifest at commit `7577f43f20de2ec166257a79cc2a238fea79c470` parses as YAML, but no full CI pass has been observed on that exact head after the prior manifest-format failure.
