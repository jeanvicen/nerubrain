"""NeuroMorpho.org downloader with conservative defaults and provenance."""
from __future__ import annotations
import argparse, json, re, time, urllib.parse, urllib.request, hashlib
from pathlib import Path
from typing import Any

API = "https://neuromorpho.org/api/neuron/select"
BASE = "https://neuromorpho.org/"
USER_AGENT = "NeruBrain/0.1 (reproducible research utility; https://github.com/jeanvicen/nerubrain)"

def request(url: str, timeout: int = 45) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, text/plain, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()

def select_records(limit: int = 50, species: str = "human", cell_type: str = "pyramidal", pause: float = 0.4) -> list[dict[str, Any]]:
    if not 1 <= limit <= 500 or pause < 0:
        raise ValueError("limit must be 1..500 and pause non-negative")
    query = f"cell_type:{cell_type}"
    records: list[dict[str, Any]] = []
    page = 0
    while len(records) < limit:
        params = urllib.parse.urlencode({"q": query, "fq": f"species:{species}", "page": page, "size": min(50, limit-len(records))})
        data = json.loads(request(f"{API}?{params}"))
        batch = data.get("_embedded", {}).get("neuronResources", [])
        if not batch:
            break
        records.extend(batch)
        if len(records) >= data.get("page", {}).get("totalElements", 0):
            break
        page += 1
        if len(records) < limit:
            time.sleep(pause)
    return records[:limit]

def standardized_url(record: dict[str, Any]) -> str:
    name, archive = record.get("neuron_name"), record.get("archive")
    if not name or not archive or not re.fullmatch(r"[A-Za-z0-9_.-]+", name) or not re.fullmatch(r"[A-Za-z0-9_. -]+", archive):
        raise ValueError("unsafe/missing neuron_name or archive in API record")
    return f"{BASE}dableFiles/{urllib.parse.quote(archive.lower(), safe='')}/CNG%20version/{urllib.parse.quote(name, safe='')}.CNG.swc"

def download_set(root: Path, limit: int = 50, species: str = "human", cell_type: str = "pyramidal", pause: float = 0.5, overwrite: bool = False) -> dict[str, Any]:
    root = Path(root)
    raw_dir = root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    records = select_records(limit, species, cell_type, pause)
    manifest = {"dataset": "NeuroMorpho.org selected standardized morphology sample", "retrieved_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "query": {"species": species, "cell_type": cell_type}, "requested_limit": limit, "records": []}
    for i, record in enumerate(records):
        name = record["neuron_name"]
        swc_path = raw_dir / f"{name}.CNG.swc"
        meta_path = raw_dir / f"{name}.metadata.json"
        url = standardized_url(record)
        if not swc_path.exists() or overwrite:
            payload = request(url)
            if len(payload) > 20_000_000 or not payload.lstrip().startswith((b"#", b"0", b"1", b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9")):
                raise ValueError(f"Unexpected payload for {name}; refusing to save")
            swc_path.write_bytes(payload)
        digest = hashlib.sha256(swc_path.read_bytes()).hexdigest()
        provenance = {"metadata_source": f"{API}?q=cell_type:{cell_type}&fq=species:{species}", "standardized_file_url": url, "file_status": "NeuroMorpho.org CNG standardized SWC; original reconstruction not bundled", "license": "NeuroMorpho.org Terms of Use; source datasets licensed CC BY 4.0 where indicated", "retrieved_utc": manifest["retrieved_utc"], "sha256": digest, "record": record}
        meta_path.write_text(json.dumps(provenance, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        manifest["records"].append({"neuron_name": name, "archive": record.get("archive"), "species": record.get("species"), "swc": f"data/raw/{swc_path.name}", "metadata": f"data/raw/{meta_path.name}", "sha256": digest, "source_url": url})
        if i + 1 < len(records): time.sleep(pause)
    (root / "data" / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--species", default="human")
    parser.add_argument("--cell-type", default="pyramidal")
    parser.add_argument("--pause", type=float, default=0.5)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    result = download_set(args.root, args.limit, args.species, args.cell_type, args.pause, args.overwrite)
    print(f"Saved {len(result['records'])} records to {args.root / 'data'}")
if __name__ == "__main__": main()
