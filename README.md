Omniverse Blueprint Starter (Minnesota)

Overview
- Starter repo to ingest MN public records and user data and convert to Omniverse-ready USD scenes and 2D blueprints.

Contents
- `requirements.txt` — Python preprocessing dependencies.
- `schema.json` — Normalized spatial feature schema.
- `scripts/` — Example preprocessing and conversion scripts.
- `kit_extension/` — Skeleton for an Omniverse Kit extension to visualize and refine scenes.
- `sample_data/` — Placeholders for your input files (GeoJSON, PDFs, LAS, DWG).

Quick setup (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Running examples
- The `scripts/` examples are meant to be run in a standard Python environment for preprocessing. Scripts that use Omniverse/pxr USD should be run inside Omniverse Kit or an environment with USD Python bindings.

Next steps
- Place sample MN datasets into `sample_data/` and update `schema.json` mappings.
- Run `scripts/geojson_to_usd.py` in Omniverse to produce a USD scene.
- Load generated USD into Omniverse Create for review and export.

Privacy and compliance
- Confirm consent for any user-supplied data and remove PII before processing.

License
- MIT (replace or update as needed)
