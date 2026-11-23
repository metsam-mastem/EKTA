# EKTA User Setup Guide
**Document ID:** EKTA-USER-SETUP-0001 | **Status:** DOCUMENTATION BASELINE

## Purpose
Setup prepares a workstation, access model and workspace conventions. Installation obtains the repository and dependencies; setup additionally verifies readiness and establishes safe operating practices.

## Supported baseline
- Python 3.11+ for runtime and validation tools.
- Git for clone, branch, history and synchronization.
- Current desktop browser.
- Windows PowerShell, Linux shell or macOS shell.
- Network access for initial clone and package installation.

The current CI workflow and package metadata override this guide if they differ. Node.js may be required for frontend validation; inspect package manifests and CI before installing it.

## Prepare the workstation
1. Install Git from its official distribution.
2. Install Python 3.11+ and confirm the interpreter.
3. Install a current browser.
4. Ensure adequate free storage for source, virtual environment and package cache; no fixed minimum is claimed because dependencies evolve.
5. Confirm access to GitHub and package indexes.
6. Prefer a non-admin account for routine work.

~~~sh
git --version
python --version
python -m pip --version
~~~

On Windows, use the correct Python launcher if python is not mapped to 3.11+.

## Repository identity and access
Canonical repository: https://github.com/metsam-mastem/EKTA

Verify owner/name before cloning. Read-only access is sufficient for browsing. Push/PR requires write access. Use SSH or a credential manager; never paste tokens into source, chat, screenshots, logs or shell history.

## Working modes
- Reader: clone or download; do not modify canonical records.
- Local explorer: install runtime dependencies and launch the local read-only workbench.
- Contributor: create a feature branch, follow contribution/quality rules and submit a PR.
- Maintainer: review ADRs, schema changes, CI evidence, release notes and recovery readiness.

## Workspace layout
Keep the clone in a stable location, such as ~/work/EKTA or C:\work\EKTA. Keep scratch downloads, temporary experiments, credentials and personal notes outside the repository unless intentionally curated. Never commit .env files, tokens, private keys or confidential personal/customer data.

Separate repository source, disposable virtual environment, temporary scratch directory and independent backup.

## Branch discipline
The UPDS integration work is on integration/upds-documentation-architecture. It is not necessarily the default branch. Inspect local/remote branches and PR status before editing. Do not commit directly to main.

## Configuration
The read-only bootstrap does not require a production account or hosted database for basic local exploration. Do not add secrets, hosted services or new cloud dependencies unless a documented feature requires them and the project owner approves.

Only use environment variables documented by code. Any new setting needs a placeholder-only example, reference docs, startup validation, tests and security review.

## Initial readiness checklist
- [ ] Correct repository URL and branch verified.
- [ ] Git/Python versions checked.
- [ ] Working tree clean before changes.
- [ ] Dependencies isolated.
- [ ] Repository validators pass.
- [ ] Existing tests pass.
- [ ] Runtime health responds after startup.
- [ ] Browser explorer loads without errors.
- [ ] No secrets or private data staged.

Record exact commands, environment, commit SHA and results. Failed checks are FAIL; unexecuted checks are NOT RUN.

## Troubleshooting
Wrong Python: select correct interpreter and recreate virtual environment. Permission denied: inspect file and Git credential permissions; do not run everything as administrator. Dependency failure: capture platform, interpreter, exact error and manifest; do not randomly upgrade packages. Port conflict: inspect owning process and use only a supported override. Browser failure: inspect process, bind address, port and local firewall. Authentication failure: verify remote and credential manager without exposing credentials.

Setup is complete only when readiness checks are recorded. This guide does not claim every OS/hardware combination has been tested.
