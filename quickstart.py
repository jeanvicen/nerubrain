"""Run from project root: PYTHONPATH=src python examples/quickstart.py"""
from pathlib import Path
from nerubrain import parse_swc, summarize
sample=Path("examples/tiny_neuron.swc")
print(summarize(parse_swc(sample)))
