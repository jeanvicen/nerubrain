"""Small logging helper; does not configure process-wide handlers."""
import logging

def get_logger(name: str = "nerubrain") -> logging.Logger:
    """Return a namespaced logger.

    Args:
        name: Logger name; defaults to the project namespace.

    Returns:
        A standard-library logger instance.
    """
    return logging.getLogger(name)
