# VES Installation and Setup

## Requirements
Python 3.11+ for model core/tests; a modern browser for the static visual prototype. No database server, cloud service, account or network connection is required for the core slice.

## Install test dependencies
From projects/ves:

    python -m pip install -e ".[dev]"

The optional development extra installs PyYAML for the EKTA taxonomy crosswalk test. Runtime modules otherwise use the Python standard library.

## Run tests

    python -m unittest discover -s tests -v

## Run visual prototype
Open web/index.html. If local-file restrictions apply:

    python -m http.server 8000 --directory web

Open http://127.0.0.1:8000.

## Data
The browser prototype stores demo state in browser local storage. Export JSON before clearing browser data. The Python SQLiteProjectStore is a separate local persistence adapter. Neither mechanism is an encrypted vault or a cloud backup service.
