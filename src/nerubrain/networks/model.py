"""Small declarative network descriptors; they perform no simulation."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Population:
    name: str
    size: int
    cell_type: str
    def __post_init__(self):
        if not self.name.strip() or self.size < 1 or not self.cell_type.strip(): raise ValueError("population requires a name, positive size, and cell_type")
@dataclass(frozen=True)
class Projection:
    name: str
    source: str
    target: str
    def __post_init__(self):
        if not all(x.strip() for x in (self.name,self.source,self.target)): raise ValueError("projection name and endpoints are required")
def validate_projection(projection: Projection, populations: dict[str, Population]) -> None:
    """Raise ValueError when either named population is unknown."""
    missing=[x for x in (projection.source,projection.target) if x not in populations]
    if missing: raise ValueError(f"unknown population endpoint(s): {', '.join(missing)}")
