#!/usr/bin/env python3
"""Convenience wrapper; run from any directory; requires network access only."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from nerubrain.dataset import main
if __name__ == "__main__": main()
