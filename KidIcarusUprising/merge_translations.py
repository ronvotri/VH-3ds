#!/usr/bin/env python3
"""Apply Kid Icarus translation overlays to the complete source JSONL.
Usage: python merge_translations.py SOURCE.jsonl OUTPUT.jsonl
Expected source: ban_dich/tieng_anh_can_dich.jsonl from the 2026-11-18 handover.
"""
import json
import re
import sys
from pathlib import Path

def load_jsonl(path):
    for line_no, line in enumerate(Path(path).read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.strip():
            obj = json.loads(line)
            if not isinstance(obj, dict) or "id" not in obj:
                raise ValueError(f"{path}:{line_no}: missing id")
            yield obj

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python merge_translations.py SOURCE.jsonl OUTPUT.jsonl")
    source_file, output_file = map(Path, sys.argv[1:])
    if source_file.resolve() == output_file.resolve():
        raise SystemExit("Input and output must differ.")
    items = list(load_jsonl(source_file))
    by_id = {r["id"]: r for r in items}
    if len(by_id) != len(items):
        raise SystemExit("Duplicate IDs in source.")
    overlays = {}
    for p in sorted((Path(__file__).parent / "translations").glob("batch_*.jsonl")):
        for r in load_jsonl(p):
            key = r["id"]
            if key in overlays:
                raise SystemExit(f"Duplicate overlay id: {key}")
            if key not in by_id:
                raise SystemExit(f"Unrecognized ID: {key}")
            if "source" in r and r["source"] != by_id[key].get("source"):
                raise SystemExit(f"English source mismatch at {key}")
            if not r.get("vi"):
                raise SystemExit(f"Missing Vietnamese at {key}")
            src_ctrl = re.findall(r"\\{CTRL:[^}]+\\}", by_id[key].get("source", ""))
            vi_ctrl = re.findall(r"\\{CTRL:[^}]+\\}", r["vi"])
            if src_ctrl != vi_ctrl:
                raise SystemExit(f"Control codes differ at {key}: source={src_ctrl}, vi={vi_ctrl}")
            if not by_id[key].get("source"):
                raise SystemExit(f"Refusing to edit empty original at {key}")
            overlays[key] = r
    for record in items:
        t = overlays.get(record["id"])
        if t:
            record["vi"] = t["vi"]
            record["status"] = t["status"]
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in items), encoding="utf-8")
    print(f"Total source records: {len(items)}, overlay entries: {len(overlays)}, pending: {len(items)-len(overlays)}")
if __name__ == "__main__":
    main()
