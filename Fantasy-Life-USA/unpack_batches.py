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
    ("cp004-2000.jsonl.bz2.b64", bz2.decompress, "cp004-new-2000.jsonl",
     "4b8e00d1223f7e9c4f520f816d7a11ae46fd09d3cd0bf183ee358cca2c2fa395", 2000),
    ("cp005a-700.jsonl.bz2.b64", bz2.decompress, "cp005a-new-700.jsonl",
     "834af3e6f435f7f5efd95af3e4b7381d535638ecc807765f6e307f5a2b9a26d3", 700),
    ("cp005b-900.jsonl.bz2.b64", bz2.decompress, "cp005b-new-900.jsonl",
     "d3146947fbbcfea183fb6cd095138f9a055cfb9bf84c5e5190e779d62464de7b", 900),
    ("cp005c-400.jsonl.bz2.b64", bz2.decompress, "cp005c-new-400.jsonl",
     "052ed3544734b7b358d86a655298e0e5d7cd238688d3c2bfe4ffce8fe456f738", 400),
    ("cp006a-500.jsonl.bz2.b64", bz2.decompress, "cp006a-new-500.jsonl",
     "6eb788b0b2eaeef7863fb51a8b3de0ed3e73704ee4317e0474ad57e3ba3179d2", 500),
    ("cp006b-500.jsonl.bz2.b64", bz2.decompress, "cp006b-new-500.jsonl",
     "f967eeba1206e1c65e64ae4e45830d3e948a00d16f27627ed418d62bdae467e3", 500),
    ("cp006c-100.jsonl.bz2.b64", bz2.decompress, "cp006c-new-100.jsonl",
     "c1e1a2ffda6213db043c5e23ef2afc77ac38bfe29a71772991246d87974ed220", 100),
    ("cp006c02-300.jsonl.bz2.b64", bz2.decompress, "cp006c02-new-300.jsonl",
     "8ba564ad0377ce51afd72deb42590abefd892d603b234c05a42de0899b905b04", 300),
]
all_data = bytearray()
cp005_data = bytearray()
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
    if filename.startswith('cp005'):
        cp005_data.extend(data)
    print("Restored:", outname, count, "IDs")
assert len(ids) == 5900
assert len(cp005_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp005_data).hexdigest() == '309d868dc821d859cc587f5b8a80e435b1d25fb54bdaa47acc023c0a7adb3ce0'
(root / 'cp005-complete-2000.jsonl').write_bytes(cp005_data)
out = root / "merged-001-059.jsonl"
out.write_bytes(all_data)
print("PASS: 5900 unique translations =>", out)
