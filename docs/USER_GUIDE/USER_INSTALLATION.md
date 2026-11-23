# EKTA User Installation Guide
**Document ID:** EKTA-USER-INSTALL-0001 | **Status:** DOCUMENTATION BASELINE

## Installation modes
1. Source installation — recommended for contributors and maintainers.
2. Source archive — read-only evaluation; Git history and update workflow are limited.
3. Packaged desktop/mobile/offline installation — NOT IMPLEMENTED unless a release artifact is published with platform-specific instructions.

## Clone
~~~sh
git clone https://github.com/metsam-mastem/EKTA.git
cd EKTA
~~~

To use the UPDS integration branch:
~~~sh
git fetch origin
git switch --track origin/integration/upds-documentation-architecture
~~~
If it already exists locally, switch to it directly. Confirm the branch exists before running these commands.

## Isolated Python environment
Linux/macOS:
~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
~~~

Windows PowerShell:
~~~powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
~~~

Install from the dependency manifest actually present on the selected branch. For example, only if requirements.txt exists:
~~~sh
python -m pip install -r requirements.txt
~~~
If the repository uses pyproject.toml or another manifest, follow its documented installation method. Do not guess dependencies.

## Launch
The root README currently documents:
- Windows: powershell -ExecutionPolicy Bypass -File scripts/start.ps1
- Linux/macOS: sh scripts/start.sh

Inspect scripts before running them, especially on unreviewed branches. Then open http://127.0.0.1:8000. API docs, if enabled, are at http://127.0.0.1:8000/docs.

This is a local bootstrap, not a production deployment. Keep the server on loopback; do not expose the development server publicly.

## Validation
Run the UPDS validator on the integration branch:
~~~sh
python tools/validate_upds.py
~~~
Read .github/workflows/validate.yml for the exact full CI commands on the selected commit. Do not claim success unless commands complete with exit code zero and the SHA is recorded.

## Update safely
~~~sh
git status --short
git fetch origin
git pull --ff-only
~~~
Back up or commit local changes first. Pull the intended branch explicitly. Avoid force-push and destructive reset commands unless the owner reviews the impact.

## Uninstall
Stop the runtime, deactivate the virtual environment, and remove the local clone only after backing up uncommitted work and local artifacts. Removing a clone does not delete the remote GitHub repository. Deleting the remote is a separate destructive owner action.

## Security
Inspect scripts; install from trusted manifests; isolate dependencies; avoid elevated privileges; bind locally; never commit secrets; review third-party licenses. The repository's own license remains undecided.

## Known limitations
No signed desktop installer, Android APK, mobile package, production image, hosted service or one-click installer is established by this guide. These require a release pipeline, platform tests, signing and a dedicated installation guide.
