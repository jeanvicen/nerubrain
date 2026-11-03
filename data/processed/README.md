# Processed outputs

`morphology_summary.csv` is regenerated from all locally available `data/raw/*.swc` inputs by:

```sh
PYTHONPATH=src python -m nerubrain.cli data/raw --output data/processed/morphology_summary.csv
```

Every row is descriptive and uses coordinate units from its own SWC. The original records and checksums are in `data/manifest.json`; source metadata is in each raw-file sidecar.
