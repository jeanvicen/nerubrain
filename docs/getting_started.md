# Getting started

Requires Python 3.10 or newer. The parser, validation helpers, and summary command use only the standard library; install the project with `python -m pip install -e .` or set `PYTHONPATH=src`.

```sh
python -m venv .venv
# Linux/macOS: . .venv/bin/activate
# Windows: .venv\\Scripts\\activate
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/process_neurons.py data/raw --output data/processed/morphology_summary.csv
```

Parse a file with `parse_swc(path)` and inspect conservative checks via `validate_morphology`. Validation is structural only; no scientific quality score is implied. The `data/raw` collection is source-standardized NeuroMorpho CNG SWC, not original acquisition data. Consult [provenance](data_and_citations.md) before redistribution or scientific use.

The downloader requires internet access and respects the API/site terms: `python scripts/download_neurons.py --root . --limit 50 --species human --cell-type pyramidal --pause 0.5`. Availability and query semantics are controlled by NeuroMorpho.org.
