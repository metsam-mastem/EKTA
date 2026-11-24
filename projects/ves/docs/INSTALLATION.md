# VES Installation and Setup

## Requirements
Python 3.11+ for model core/tests; a modern browser for the static visual prototype. No database server, cloud service, account or network connection is required for this slice.

## Run tests
From projects/ves:

    python -m unittest discover -s tests -v

## Optional editable install

    python -m pip install -e .

## Run visual prototype
Open web/index.html. If local-file restrictions apply:

    python -m http.server 8000 --directory web

Open http://127.0.0.1:8000.

## Data
The browser prototype stores demo state in browser local storage. Export JSON before clearing browser data. This is not yet a production persistence or backup mechanism.
