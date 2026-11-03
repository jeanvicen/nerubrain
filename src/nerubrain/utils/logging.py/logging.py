"""Package logger configuration helper; leaves root logging untouched."""
import logging
def get_logger(name: str = "nerubrain") -> logging.Logger:
    return logging.getLogger(name)
