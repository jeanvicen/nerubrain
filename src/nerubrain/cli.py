"""Create summary tables from local SWC files."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
from .swc import parse_swc, summarize

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("input",type=Path); p.add_argument("--output",type=Path,default=Path("data/processed/morphology_summary.csv")); a=p.parse_args()
    files=sorted(a.input.glob("*.swc")) if a.input.is_dir() else [a.input]
    rows=[]
    for path in files:
        try: rows.append({"file":path.name,**summarize(parse_swc(path))})
        except (OSError, ValueError) as exc: print(f"SKIP {path}: {exc}")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    cols=["file","node_count","root_count","roots","branch_point_count","terminal_count","edge_count","total_path_length","bounding_box","node_types"]
    with a.output.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
        for row in rows:
            for k in ("roots","bounding_box","node_types"): row[k]=json.dumps(row[k],separators=(",",":"))
            w.writerow(row)
    print(f"Summarized {len(rows)}/{len(files)} files -> {a.output}")
if __name__ == "__main__": main()
