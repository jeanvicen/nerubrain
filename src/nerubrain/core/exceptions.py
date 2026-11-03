"""Domain-specific errors used by NeruBrain."""
class NeruBrainError(Exception):
    """Base exception for package-level errors."""
class ValidationError(NeruBrainError, ValueError):
    """Input violates an explicitly checked structural constraint."""
