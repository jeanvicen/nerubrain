# Data provenance and attribution

The bundled `data/raw/` sample contains NeuroMorpho.org **standardized CNG SWC** files downloaded from the live site and paired JSON sidecars. These are not the original laboratory submissions. NeuroMorpho.org describes the original and standardized versions as separate available resources; this deliverable has obtained the standardized files only. Metadata is sourced from the public NeuroMorpho.org REST API; the exact record, retrieval time, download URL and SHA-256 are captured per file.

Sample selection is a convenience cohort of human neurons with a pyramidal cell-type match, capped at 50. Search filters are not a scientific sampling design. Do not treat it as representative. Records may change upstream; regenerate with `python -m nerubrain.dataset --limit 50 --species human --cell-type pyramidal` and preserve the manifest for reproducibility.

NeuroMorpho.org's current Terms of Use state that NeuroMorpho.org is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). For publications using its materials, the terms require three citations: (1) each original paper describing the reconstruction, as listed in its detailed metadata; (2) NeuroMorpho.Org (RRID:SCR_002145); and (3) Tecuatl C, Ljungquist B, Ascoli GA (2024), “Accelerating the continuous community sharing of digital neuromorphology data,” FASEB Bioadv. 6(7):207–221, doi:10.1096/fba.2024-00048. The source archive and metadata are captured per record; verify original paper details before reuse. This repository does not relicense source morphologies under MIT. Code is MIT; data is governed by NeuroMorpho.org's CC BY 4.0 terms.

- API documentation: <https://neuromorpho.org/apiReference.html>
- Terms of Use: <https://neuromorpho.org/termsofuse.jsp>
- FAQ (standardized/original files): <https://neuromorpho.org/myfaq.jsp>
- Portal: <https://neuromorpho.org/>

The terms also require programmatic access through the API for metadata and direct HTTP URLs for SWC files; the downloader follows these requirements. Consult the current terms before redistribution or publication: <https://neuromorpho.org/useterm.jsp>.

This small sample is intended for reproducible software tests and demonstrations, not clinical or diagnostic use.
