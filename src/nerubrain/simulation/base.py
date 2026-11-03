"""Abstract contract for future simulator adapters, not a simulator."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass(frozen=True)
class RunConfig:
    duration_ms: float
    timestep_ms: float
    def __post_init__(self):
        if self.duration_ms <= 0 or self.timestep_ms <= 0 or self.timestep_ms > self.duration_ms: raise ValueError("duration and timestep must be positive, with timestep <= duration")
class SimulationBackend(ABC):
    """Adapters must document units, deterministic settings, and output schema."""
    @abstractmethod
    def run(self, model, config: RunConfig):
        """Run a backend-specific model and return backend-defined results."""
