#!/usr/bin/env python3
"""Restore committed Fantasy Life VI text JSONL; Python 3 stdlib only."""
from pathlib import Path
import base64
import bz2
import gzip
import hashlib
import json

root = Path(__file__).resolve().parent / "translations"
inputs = [
    ("batch-001.jsonl.gz.b64", gzip.decompress, "batch-001.jsonl",
     "84870069b5a459d088c5e852cdb88e87c7d07ae968369896868fd2e6e9a5e471", 100),
    ("cp002-200.jsonl.bz2.b64", bz2.decompress, "cp002-new-200.jsonl",
     "8bc732e85e7542db83a920e4dd7189662e4d33d0fc633642e413a9c2385a0c94", 200),
    ("cp003-200.jsonl.bz2.b64", bz2.decompress, "cp003-new-200.jsonl",
     "dcfd61bdd206f2ffc0beaecc9c8fa1ec6722a7baa121f3def6d333a3052dfd46", 200),
]
all_data = bytearray()
ids = set()
for filename, decompressor, outname, sha, count in inputs:
    packed = base64.b64decode((root / filename).read_text(encoding="ascii").strip(), validate=True)
    data = decompressor(packed)
    assert hashlib.sha256(data).hexdigest() == sha, "SHA-256 mismatch: " + filename
    rows = [json.loads(line) for line in data.decode("utf-8").splitlines()]
    assert len(rows) == count, (filename, len(rows))
    for row in rows:
        assert set(row.keys()) == {"id", "vi"}, row
        assert row["id"] not in ids, "Duplicate ID: " + row["id"]
        assert row["vi"], "Empty translation: " + row["id"]
        ids.add(row["id"])
    (root / outname).write_bytes(data)
    all_data.extend(data)
    print("Restored:", outname, count, "IDs")
assert len(ids) == 500
out = root / "merged-001-005.jsonl"
out.write_bytes(all_data)
print("PASS: 500 unique translations =>", out)
