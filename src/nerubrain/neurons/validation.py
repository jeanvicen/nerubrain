"""Conservative structural checks; these do not assess biological quality."""
from dataclasses import dataclass
from ..swc import Morphology
@dataclass(frozen=True)
class ValidationReport:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    @property
    def valid(self) -> bool:
        return not self.errors
def validate_morphology(morphology: Morphology) -> ValidationReport:
    """Check parent cycles and non-positive radii; preserve input, never repair it."""
    errors=[]; warnings=[]; by_id=morphology.by_id
    for node in morphology.nodes:
        if node.radius <= 0: warnings.append(f"node {node.node_id}: radius is not positive")
        seen=set(); current=node
        while current.parent != -1:
            if current.node_id in seen:
                errors.append(f"parent cycle involving node {current.node_id}"); break
            seen.add(current.node_id); current=by_id[current.parent]
        if errors and errors[-1].startswith("parent cycle"): break
    return ValidationReport(tuple(errors),tuple(warnings))
