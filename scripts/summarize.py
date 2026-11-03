#!/usr/bin/env python3
"""Convenience wrapper to write CSV summaries from SWC files."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from nerubrain.cli import main
if __name__ == "__main__": main()
