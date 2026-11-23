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
    ("cp006c03-600.jsonl.bz2.b64", bz2.decompress, "cp006c03-new-600.jsonl",
     "edac3870265815e1e62dfe438075610ce77becfe5781dae18b40b7d1ace2152b", 600),
    ("cp007-2000.jsonl.bz2.b64", bz2.decompress, "cp007-new-2000.jsonl",
     "52b047c193a310f7942c78b4409dab9d217c1982ea0110798c95677b0ad40cb8", 2000),
    ("cp008a-1610.jsonl.bz2.b64", bz2.decompress, "cp008a-new-1610.jsonl",
     "083720e8654a1c53dc95d900c466133a5b4d6b3e31d1aaefd17ff61e80de750d", 1610),
    ("cp008b-390.jsonl.bz2.b64", bz2.decompress, "cp008b-new-390.jsonl",
     "9640411f905472d66a00225a5ac0df777802835e0555d01fcb3d6d869556dec5", 390),
]
all_data = bytearray()
cp005_data = bytearray()
cp006_data = bytearray()
cp008_data = bytearray()
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
    if filename.startswith('cp006'):
        cp006_data.extend(data)
    if filename.startswith('cp008'):
        cp008_data.extend(data)
    print("Restored:", outname, count, "IDs")
assert len(ids) == 10500
assert len(cp005_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp005_data).hexdigest() == '309d868dc821d859cc587f5b8a80e435b1d25fb54bdaa47acc023c0a7adb3ce0'
(root / 'cp005-complete-2000.jsonl').write_bytes(cp005_data)
assert len(cp006_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp006_data).hexdigest() == 'b49cbcc488a705ab2eba24d96f5593d4d87d2b785822d6dc7685007c1fdc18a5'
(root / 'cp006-complete-2000.jsonl').write_bytes(cp006_data)
assert len(cp008_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp008_data).hexdigest() == 'daeac626ec53a92aba0952cb36ca7c9638e977010ca3e7afbebcf1f01ccad6e6'
(root / 'cp008-complete-2000.jsonl').write_bytes(cp008_data)
out = root / "merged-CP008-10500.jsonl"
out.write_bytes(all_data)
print("PASS: 10500 unique translations =>", out)
