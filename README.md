<div align="center">

# NeruBrain
### A transparent foundation for neuronal morphology and biologically grounded neural systems.

[![Python](https://img.shields.io/badge/python-%E2%89%A53.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/code-MIT-2ea44f.svg)](LICENSE)
[![Data: CC BY 4.0](https://img.shields.io/badge/sample_data-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)](docs/roadmap.md)
[![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)](tests/)

**Read real reconstructions. Preserve their provenance. Build explicit models.**

[Getting started](docs/getting_started.md) · [Architecture](docs/architecture.md) · [Roadmap](docs/roadmap.md) · [Data & citations](docs/data_and_citations.md)

</div>

> **Research software in early development.** NeruBrain currently provides a strict, dependency-free SWC reader and conservative structural validation, a small network description model, and an abstract simulation-engine contract. It does **not** implement neuronal dynamics, a Brian2/NEURON adapter, or validated predictions. Structural validity is not biological quality, and no efficiency or scientific realism is claimed.

## Why NeruBrain?

Neural-modeling workflows often combine morphology files, metadata, model assumptions, numerical engines, and analysis scripts without a consistent account of where each datum came from. NeruBrain is being built as an inspectable, openly documented bridge between those layers: morphology in, provenance intact, assumptions explicit, simulations only when a real backend is connected and tested.

The first milestone is intentionally modest: parse SWC safely, retain coordinates and units unchanged, report checkable structural issues without silently “repairing” data, and make small backend-neutral network specifications. That foundation makes later integration and replication easier to audit.

## Current capabilities

- **SWC parsing:** seven-column rows, comments, identifiers, finite numeric values, errors with source and line number.
- **Conservative validation:** duplicate IDs, missing parents, root presence, positive radii, non-finite geometry and parent cycles. Warnings are separate from errors; no scientific quality score is invented.
- **Network descriptions:** named cell populations and directed projections with explicit endpoint validation.
- **Simulation interface:** an abstract adapter contract and validated run settings only; no engine is included.
- **Traceable data workflow:** downloader captures per-cell API metadata, source links, retrieval timestamp, SHA-256 and standardized-file status; processing emits derived summaries without rescaling geometry.
- **Small, auditable example data:** example files in this repository are explicitly synthetic fixtures for software tests, not scientific observations. Any downloaded NeuroMorpho.Org reconstructions are separately labeled in `data/raw/` and retain their own records.

## Quick start

```bash
git clone https://github.com/jeanvicen/nerubrain.git
cd nerubrain
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -e '.[dev]'
pytest
```

Parse and inspect an SWC:

```python
from nerubrain import parse_swc, validate_morphology

cell = parse_swc("data/examples/tiny_tree.swc")
report = validate_morphology(cell)
print(len(cell.nodes), report.valid, report.errors, report.warnings)
```

Download and process a small NeuroMorpho.org subset (the downloader uses the Python standard library):

```bash
python scripts/download_neurons.py --count 50 --species human --region neocortex
python scripts/process_neurons.py
```

The selection is restricted to API records labeled `principal cell` or `pyramidal cell` in the requested brain region; availability varies. Downloading is deliberately rate-limited and may take time. Files are **standardized CNG SWC files**, not original acquisition files. See [data policy and citation guidance](docs/data_and_citations.md) before reuse.

## Architecture

```text
src/nerubrain/
├── core/        domain exceptions
├── neurons/     SWC data model, parser, structural validation
├── networks/    populations and explicit directed projections
├── simulation/  backend interface and run configuration (no engine)
├── io/          provenance/hash helpers
└── utils/       logging helpers
```

The workflow keeps layers separate: acquire with provenance; parse without unit interpretation; validate structure without repair; specify models explicitly; and simulate only after a real engine adapter is implemented, tested and validated. More in [the architecture note](docs/architecture.md).

## Data, integrity & provenance

NeuroMorpho.Org's programmatic distribution provides standardized **CNG SWC versions**; original uploaded files are not currently available programmatically (see their [FAQ](https://neuromorpho.org/myfaq.jsp)). NeruBrain therefore labels those downloaded files as *source-standardized*, never “original raw” or untouched acquisitions. `data/processed/` is for derived outputs only; source-coordinate units are not converted or guessed.

Each downloaded neuron has an adjacent JSON record with the full API metadata response, source URLs, retrieval time, SHA-256 and data-license note. The shared manifest indexes those records. Recompute file digests before use.

**Licenses are distinct:** NeruBrain source code is MIT (`LICENSE`). NeuroMorpho.Org data are distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) subject to the [official terms](https://neuromorpho.org/useterm.jsp); attribution and original reconstruction-paper citations remain required. Do not treat the code license as covering dataset records. For scientific reuse cite the individual reconstruction paper(s), NeuroMorpho.Org (RRID:SCR_002145), and Tecuatl et al. (2024, DOI [10.1096/fba.2024-00048](https://doi.org/10.1096/fba.2024-00048)); consult [citation notes](docs/data_and_citations.md). If publication metadata are missing or uncertain, disclose that instead of guessing.

## Testing & development

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
mypy src
```

Tests use tiny synthetic SWC fixtures and verify expected parser/model behavior. They do not validate scientific conclusions or simulator performance. See [getting started](docs/getting_started.md) for contributor practices.

## Roadmap

- [x] Safe SWC parsing, explicit structural reports and initial test suite.
- [x] Provenance-aware NeuroMorpho CNG download/summary scripts.
- [ ] Expand checked-in openly licensed example corpus with verified metadata and manageable file sizes.
- [ ] Optional morphology analytics with clear unit handling and reproducibility tests.
- [ ] Evaluate a real simulation backend adapter, first with documented reference cases and version-pinned tests.
- [ ] Reproducible model specifications, benchmark protocols and validation against published results.
- [ ] Better visual exploration, model interchange and community-reviewed scientific examples.

All future claims about accuracy, realism, reproducibility, or performance depend on evidence and published validation—not intent.

## Scientific references

- NeuroMorpho.Org, a centrally curated inventory of neuronal reconstructions. RRID: [SCR_002145](https://scicrunch.org/resolver/SCR_002145).
- Tecuatl et al. (2024). NeuroMorpho.Org resource paper. DOI: [10.1096/fba.2024-00048](https://doi.org/10.1096/fba.2024-00048).
- For individual reconstructions, cite the source publication listed in each neuron's API metadata; a collection-level citation is not a substitute.

## Related projects

NeruBrain is an independent project. It studies interoperability and ideas from [Brian2](https://github.com/brian-team/brian2), [NEURON](https://github.com/neuronsimulator/nrn), [NetPyNE](https://github.com/suny-downstate-medical-center/netpyne) and [NeuroBox](https://github.com/NeuroBox3D/neuromorpho), without copying their code or claiming equivalent functionality. Engine integrations are future work.

## Contributing

Issues and focused pull requests are welcome. Please include tests, cite data and papers, state units and assumptions, avoid altering scientific geometry silently, and distinguish software validation from scientific validation. See `CONTRIBUTING.md`.

---

<div align="center"><sub>Built for careful exploration: open methods, explicit assumptions, and provenance that travels with the data.</sub></div>
