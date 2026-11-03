# Data provenance and citation

`data/raw/` contains NeuroMorpho.org standardized CNG SWC representations plus per-record JSON metadata. These are not the original laboratory acquisition files or submitted reconstructions. `data/manifest.json` enumerates records; metadata sidecars preserve API record fields, standardized file URL, retrieval time, and SHA-256 digest. Verify hashes before downstream use.

NeuroMorpho.org data are not relicensed by this repository's MIT software license. Use is subject to the [official terms](https://neuromorpho.org/useterm.jsp), applicable CC BY 4.0 attribution conditions, and each reconstruction's source publication/license. Cite NeuroMorpho.org (RRID:SCR_002145), the individual reconstruction source paper/owner, and the resource paper by Tecuatl et al. (2024), https://doi.org/10.1096/fba.2024-00048. Confirm the record-level license before redistributing; if uncertain, do not infer it. The local sidecar license field is a note, not legal advice or a claim that every source has identical terms.

All summaries in `data/processed/` are derived and do not modify source coordinate units. The included `examples/tiny_neuron.swc` is a synthetic software fixture, not an observation.
