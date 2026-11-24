# EKTA Chat Deletion and Project Recovery Runbook
**Document ID:** EKTA-RECOVERY-0001  
**Status:** OPERATING PROCEDURE — clean-clone drill NOT YET EXECUTED

## 1. What survives chat deletion
Deleting a ChatGPT conversation does not delete commits, branches, PRs, issues, releases or files in GitHub. It can remove access to chat-only reasoning, unsaved drafts, attachments not stored elsewhere and uncommitted decisions. The repository is the durable source of truth only for information that has actually been committed and backed up.

## 2. Before deleting the conversation
- Confirm the canonical repository URL and that you can sign in to GitHub independently of ChatGPT.
- Open the current continuity archive, project state and session handoff.
- Confirm the latest clean integration branch and PR are visible.
- Download or clone the repository to a local device.
- Create a portable source archive and calculate SHA-256.
- Store the archive in a second location independent of the GitHub account.
- Keep credentials out of the archive and repository.
- Verify that all important external attachments, datasets, binaries and source repositories have their own durable location and checksum.
- Do not delete the chat until the archive and backup are accessible.

## 3. Clean-clone recovery
On a fresh machine with Python 3.11+ and Git installed:

```bash
git clone https://github.com/metsam-mastem/EKTA.git
cd EKTA
git checkout main
git pull --ff-only
git status --short
```

To inspect the UPDS proposal without merging it:

```bash
git fetch origin
git checkout integration/upds-independent-continuity
git status --short
```

Install and run checks according to the current repository's README and pyproject.toml. At the documented baseline, the repository uses a Python package, FastAPI/Uvicorn and development dependencies; always inspect current requirements before executing commands.

```bash
python -m pip install -e ".[dev]"
python tools/validate_docs.py
python -m unittest discover -s tests -v
python tools/validate_frontend.py
python tools/build_graph.py
python tools/validate_upds.py
```

The final command becomes valid after the UPDS CI integration is present in the branch. Do not assume it exists on main until merged.

## 4. Resume the work
Read:
1. README.md
2. docs/PROJECT_CHARTER.md
3. docs/GOVERNANCE.md
4. docs/CONTEXT_CONTINUITY.md
5. docs/MASTER_HANDOFF.md
6. docs/PROJECT_STATE.md
7. docs/INTEGRATION/UPDS_INTEGRATION_INDEX.md
8. docs/PROJECT_CONTINUITY/CHAT_SESSION_ARCHIVE_2026-11-24.md
9. docs/ACTIVE_WORK.md
10. docs/DECISION_REGISTER.md
11. docs/CONSTRAINTS_AND_ASSUMPTIONS.md
12. docs/OPEN_ISSUES.md
13. docs/EVIDENCE_INDEX.md
14. docs/SESSION_HANDOFF.md
15. relevant code, schemas, tests and CI logs.

Check live PR status, current main HEAD and latest workflow run before any code changes. Older handoff facts may have become stale.

## 5. Backup and restore
A Git clone is not a second-account backup. Create a source archive from a clean checkout, compute its hash, copy it to a second storage provider/device, then restore into a new directory and run validation. Keep Git history if the chosen archive format permits it. Never overwrite the only working copy during restore.

## 6. Acceptance criteria for independence
- A new contributor can identify product mission and current version.
- All approved decisions, constraints and open work are discoverable.
- Build/install/test instructions reproduce the current baseline.
- A clean clone can run validation without chat or model memory.
- The latest PR and branch can be identified from repository records.
- All required source artifacts are accessible or explicitly marked external/missing.
- A second backup can be restored and its checksum verified.
- No undocumented credential or proprietary connector is required for core recovery.

## 7. Current verification
At document creation, the clean-clone drill and independent backup restore have NOT RUN. This runbook defines the procedure; it is not evidence that the procedure passed.
