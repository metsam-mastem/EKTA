# Recovery, Continuity and Chat Independence
**Document ID:** EKTA-RECOVERY-0001 | **Status:** OPERATIONAL POLICY BASELINE

## 1. Recovery objective
A qualified maintainer or AI agent must resume from a clean clone without any chat, account memory or private conversation. The repository must state project identity, approved decisions, constraints, implementation state, test evidence, unresolved work and next safe action.

## 2. If this chat is deleted
Deleting a chat may remove its conversational context and attachments that were not independently stored. It does not by itself delete a separately hosted Git repository. However, any requirement, decision, file or credential existing only in chat is at risk. Therefore this project must not depend on this chat as its memory store.

## 3. Canonical recovery order
1. README.md
2. docs/PROJECT_CHARTER.md
3. docs/GOVERNANCE.md
4. docs/PROJECT_STATE.md
5. docs/MASTER_HANDOFF.md
6. docs/INTEGRATION/UPDS_INTEGRATION_INDEX.md
7. docs/INTEGRATION/UPDS_EKTA_INTEGRATION_DECISION.md
8. docs/ACTIVE_WORK.md
9. docs/OPEN_ISSUES.md
10. docs/DECISION_REGISTER.md
11. docs/CONSTRAINTS_AND_ASSUMPTIONS.md
12. docs/EVIDENCE_INDEX.md
13. docs/SESSION_HANDOFF.md
14. relevant schemas, code, tests and CI workflow.

If records conflict, prefer an explicitly approved decision and latest canonical register. Record conflicts; do not silently resolve them.

## 4. Required durable memory
Store identity, mission, non-goals, scope, product boundaries, owner decisions and rejected alternatives, current branch/commit/tree state, implemented vs planned features, requirements/acceptance criteria, architecture/APIs/schemas, risks/assumptions, test commands/results/SHA, source versions/licenses, active tasks and next safe action.

Never store secrets, passwords, access tokens or unnecessary personal data.

## 5. Clean-clone recovery drill
1. Create a fresh directory/environment.
2. Clone the canonical repository.
3. Do not open the original chat or consult personal memory.
4. Read the recovery order.
5. Identify purpose, current branch/commit, approved/proposed decisions, constraints, actual capabilities, latest CI, blockers and next action.
6. Run documented validation and tests.
7. Compare recovered state with canonical registers.
8. Record and repair discrepancies.
9. Have an independent person/agent repeat where feasible.

Acceptance requires complete reconstruction, no critical chat-only decision, reproducible commands and resolved/explicitly blocked discrepancies. Until this drill is executed and evidence committed, recovery is DESIGNED, NOT VERIFIED.

## 6. Backup
Remote Git is the primary durable copy, not the only copy. Maintain an independent mirror or periodic git bundle --all backup; export release artifacts/checksums separately; test restoration; protect backup credentials. Material PR/issue decisions must be copied into canonical records.

## 7. Handoff protocol
At each substantial work unit update PROJECT_STATE, ACTIVE_WORK, OPEN_ISSUES, DECISION_REGISTER, EVIDENCE_INDEX and SESSION_HANDOFF. State exact commit, what changed, what was not done and the next concrete action. Avoid vague instructions such as "continue implementation".

## 8. Portable agent bootstrap prompt
> Work on the canonical EKTA repository without relying on chat history. Read README, PROJECT_CHARTER, GOVERNANCE, PROJECT_STATE, MASTER_HANDOFF, UPDS_INTEGRATION_INDEX, ACTIVE_WORK, OPEN_ISSUES, DECISION_REGISTER, CONSTRAINTS_AND_ASSUMPTIONS, EVIDENCE_INDEX and SESSION_HANDOFF. Inspect actual Git branch, commit, working tree, files and CI. Approved ADRs and repository records are the source of truth. Preserve knowledge and IDs. Do not merge projects, change the license, add hosted dependencies, expose secrets or perform destructive actions without explicit approval. Use TDD for behavior changes. Run exact validation commands. Record evidence and update continuity registers. Distinguish PROPOSED, IMPLEMENTED, VERIFIED, VALIDATED, NOT RUN and BLOCKED. First perform the next safe action in ACTIVE_WORK.

## 9. Remaining recovery limitations
A written protocol is not proof of recovery. Clean-clone drill, independent backup restoration, full document registry, graph traceability, automated state snapshots and project starter generator remain separate work packages until code and test evidence are committed.
