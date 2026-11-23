$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root
if (-not (Test-Path ".venv")) {
    py -3 -m venv .venv
}
& .\.venv\Scripts\python.exe -m pip install -e .
& .\.venv\Scripts\python.exe -m uvicorn ekta_runtime.api:app --app-dir runtime --host 127.0.0.1 --port 8000
