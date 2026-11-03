# Architecture (alpha)

NeruBrain separates data parsing, conservative checks, small model descriptors, and future simulator integration. It is a research-software starter, not a validated computational neuroscience platform.

- `neurons/` stores SWC reader primitives in `swc.py` and structural checks in `neurons/validation.py`.
- `networks/` provides simple immutable population/projection descriptors; no dynamics or connection generation.
- `simulation/` defines a backend contract and run-parameter value object; no Brian2, NEURON, or other engine is included.
- `io/` computes file hashes; `dataset.py` downloads standardized source files and records metadata; `cli.py` writes derived CSV summaries.
- `core/` contains shared domain errors. `utils/` provides a package logger.

Coordinates and radii remain unchanged in source units; the package does not infer units, repair trees, or assert biological validity. Extensions should preserve source provenance, state assumptions, test deterministic behavior, and distinguish implementation from validated scientific results.
