# Methods

NeruBrain reads SWC rows (id, type, x, y, z, radius, parent), retaining input coordinate units and SWC type codes. It checks basic row syntax, finite coordinates, non-negative radii, unique IDs, parent references, and at least one root. It deliberately does not repair malformed morphologies or assert biological completeness/tree connectedness.

Summary metrics: node/root/edge/terminal/branch-point counts, sum of Euclidean parent-child edge lengths, per-axis coordinate bounds, and counts by SWC type. Segment lengths are computed in coordinate units and include all parent-child edges; no soma reconstruction, scaling, pruning, topology correction, or scientific interpretation is performed. Multiple-root inputs are reported, not collapsed. Values depend on source coordinate conventions and standardized-file processing.

The included tiny fixture is synthetic. The fetched dataset is a human/pyramidal metadata-filtered selection and may include inconsistencies or source-specific conventions; inspect records before downstream analysis. The package offers no statistical inference, morphology classification, or medical advice.
