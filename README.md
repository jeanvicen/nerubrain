# NeruBrain

A small, reproducible starter kit for neuron morphology research: direct NeuroMorpho.org metadata retrieval, standardized SWC data with per-record provenance, a dependency-free SWC parser and transparent summaries, tests, and a notebook. Code is MIT-licensed; source morphologies retain their own terms and attribution.

## Included dataset

`data/raw/` contains a capped human/pyramidal sample (up to 50 records) of **NeuroMorpho.org standardized CNG SWC** files, with metadata sidecars. These are not the original submitted laboratory files. Each sidecar/manifest identifies the API record, download URL and SHA-256. See [data provenance](docs/DATA_PROVENANCE.md) and [methodology](docs/METHODOLOGY.md). Review original dataset terms and cite the data owners before reuse.

## Quick start (Python 3.10+)

No runtime dependencies. From this folder:

```sh
PYTHONPATH=src python examples/quickstart.py
PYTHONPATH=src python -m nerubrain.cli data/raw --output data/processed/morphology_summary.csv
PYTHONPATH=src python -m unittest discover -s tests -v
```

The tests also work with pytest if it is already available; the project does not require pytest.

Install locally if desired: `python -m pip install -e .` (installation is optional). To re-fetch, requiring internet access:

```sh
PYTHONPATH=src python -m nerubrain.dataset --root . --limit 50 --species human --cell-type pyramidal --pause 0.5
```

The downloader uses the official API for records and the corresponding standardized CNG SWC file URL, a polite pause, a 20 MB per-file cap, and SHA-256 sidecars. Existing files are kept unless `--overwrite` is supplied. API/site availability and their current terms apply.

Convenience wrappers are available as `python scripts/summarize.py data/raw --output data/processed/morphology_summary.csv` and `python scripts/fetch_sample.py --root . --limit 50`.

## Python API

```python
from nerubrain import parse_swc, summarize
morphology = parse_swc("data/raw/neuron.CNG.swc")
summary = summarize(morphology)
```

`summary` reports counts, bounding box and total parent-child Euclidean path length in source coordinate units. This is a basic data utility, not a validated scientific measurement pipeline. See `notebooks/explore_sample.ipynb`.

## Layout

- `src/nerubrain/`: parser, downloader, CLI
- `data/raw/`: downloaded standardized SWC + source metadata sidecars
- `data/manifest.json`: selected records and hashes
- `data/processed/`: reproducible summary output
- `tests/`, `examples/`, `notebooks/`, `docs/`

## License and attribution

Software: MIT, see `LICENSE`. NeuroMorpho.org content is separately governed by the current terms and source archive attribution; no blanket MIT relicensing of morphology data is implied. Cite NeuroMorpho.org and each applicable source publication/owner. Attribution checklist and links: `docs/DATA_PROVENANCE.md`.
