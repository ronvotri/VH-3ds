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
    ("cp009a-445.jsonl.bz2.b64", bz2.decompress, "cp009a-new-445.jsonl",
     "5329d45ea3fa4122b06918697d005fbcddd9ffe83561175d39dca06350493586", 445),
    ("cp009b-525.jsonl.bz2.b64", bz2.decompress, "cp009b-new-525.jsonl",
     "e38269628a64ae4fe69632ab316909e2a0082978bbe1cc0077d789eb0d86e46e", 525),
    ("cp009c-1030.jsonl.bz2.b64", bz2.decompress, "cp009c-new-1030.jsonl",
     "c72f173c149a9e7ec8453829c81dc3081f08c0e3661e66dde675f0e6eec40fd8", 1030),
    ("cp010a-522.jsonl.bz2.b64", bz2.decompress, "cp010a-new-522.jsonl",
     "e70f143f443d6890bd47113106effc320779be8f06205509b2c068a54fd86083", 522),
    ("cp010b-643.jsonl.bz2.b64", bz2.decompress, "cp010b-new-643.jsonl",
     "c8b3da74ec21fad3f48057f0e7ad652cbc8c37ad3673b1b0ce0e04b46f4ec400", 643),
    ("cp010c-835.jsonl.bz2.b64", bz2.decompress, "cp010c-new-835.jsonl",
     "bfd755404c2556b97267ca1de9414fae7f20f59c364a67f42a540aed485d0f0c", 835),
    ("cp011a-473.jsonl.bz2.b64", bz2.decompress, "cp011a-new-473.jsonl",
     "4b0298b92a4a05dcaf9fab34bfc3cf00f78c9609cac1f0928e2d4d06144c8cc7", 473),
    ("cp011b-604.jsonl.bz2.b64", bz2.decompress, "cp011b-new-604.jsonl",
     "e92384a54b1e0f6b7a24c93786745a2642913fab11e4c22697542ba89df5c6f2", 604),
    ("cp011c-923.jsonl.bz2.b64", bz2.decompress, "cp011c-new-923.jsonl",
     "1c40a70b596c41921947c61761ba583e939729bdc0e0d1af74fbd0ddd572d26c", 923),
    ("cp012a-560.jsonl.bz2.b64", bz2.decompress, "cp012a-new-560.jsonl",
     "a7073240b2a34cb5861eeb90e1dbf675452c16049e19cd0b185f98070a9bbda3", 560),
    ("cp012b-497.jsonl.bz2.b64", bz2.decompress, "cp012b-new-497.jsonl",
     "3a208c9c924fe24b427d058cf0c0654f772cc56854735ae930c03ba8cebbf6d1", 497),
    ("cp012c-527.jsonl.bz2.b64", bz2.decompress, "cp012c-new-527.jsonl",
     "139ad3b4f736d894ff1f4e2a7eb45abb8568a9dc72395d6f9b106fcdc36d541c", 527),
    ("cp012d-416.jsonl.bz2.b64", bz2.decompress, "cp012d-new-416.jsonl",
     "ee48ed9b0e6a066a5cde1a3bfa0fc1c12e3573fd2c0638931bde9b0c2196a617", 416),
    ("cp013a-285.jsonl.bz2.b64", bz2.decompress, "cp013a-new-285.jsonl",
     "00e09a7af0c7a1660713721b37e37840b1b73b43aea50c063683a5dce37da39f", 285),
]
all_data = bytearray()
cp005_data = bytearray()
cp006_data = bytearray()
cp008_data = bytearray()
cp009_data = bytearray()
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
    if filename.startswith('cp009'):
        cp009_data.extend(data)
    print("Restored:", outname, count, "IDs")
assert len(ids) == 18785
assert len(cp005_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp005_data).hexdigest() == '309d868dc821d859cc587f5b8a80e435b1d25fb54bdaa47acc023c0a7adb3ce0'
(root / 'cp005-complete-2000.jsonl').write_bytes(cp005_data)
assert len(cp006_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp006_data).hexdigest() == 'b49cbcc488a705ab2eba24d96f5593d4d87d2b785822d6dc7685007c1fdc18a5'
(root / 'cp006-complete-2000.jsonl').write_bytes(cp006_data)
assert len(cp008_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp008_data).hexdigest() == 'daeac626ec53a92aba0952cb36ca7c9638e977010ca3e7afbebcf1f01ccad6e6'
(root / 'cp008-complete-2000.jsonl').write_bytes(cp008_data)
assert len(cp009_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp009_data).hexdigest() == 'e61bfaa20fbb9c9fb58066052b814e9681ba426eba2b5c111376d730c0581477'
(root / 'cp009-complete-2000.jsonl').write_bytes(cp009_data)
out = root / "merged-CP013a-18785.jsonl"
# Apply a verified correction to one CP007 untranslated title, without adding its ID again.
corrections = [json.loads(line) for line in (root / 'cp009c-corrections-1.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(corrections) == 1
corr = corrections[0]
assert corr['id'] == 'FL-USA::F00008554@000014f8'
all_rows = [json.loads(line) for line in all_data.decode('utf-8').splitlines()]
hits = 0
for row in all_rows:
    if row['id'] == corr['id']:
        assert row['vi'] == "Blacksmith's Song: Behold, the Master Smith!"
        row['vi'] = corr['vi']
        hits += 1
assert hits == 1
all_data = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows)).encode('utf-8')
assert len(all_rows) == 18785
pre_cp010c = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:13665])).encode('utf-8')
assert hashlib.sha256(pre_cp010c).hexdigest() == 'ec5b7ce6d0376ca0c91d94de4480e9a6605039a3734eaa23646fb04eb7b4c68b'
cp010_data = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[12500:14500])).encode('utf-8')
assert len(cp010_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp010_data).hexdigest() == 'cbbf89fd83d26cb8ebc7ca4755fabe65cd56462a2debd7a3c95d86d8a8ab8585'
(root / 'cp010-complete-2000.jsonl').write_bytes(cp010_data)
# Confirm the complete 13,022 approved CP010a entries are unchanged in CP010b output.
pre_cp010b = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:13022])).encode('utf-8')
assert hashlib.sha256(pre_cp010b).hexdigest() == '637113202084ac176043917ce18d5913c6712aece71e94b4b642a5f591fbd78b'
# Confirm 12,500 previously approved entries remain byte-identical after the legacy correction.
old_prefix = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:12500])).encode('utf-8')
assert hashlib.sha256(old_prefix).hexdigest() == 'bb8d3a23d01e5c1f2c4b89fbe2aec35529d62475a81acf638c9a18998ecad67b'
pre_cp011a = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:14500])).encode('utf-8')
assert hashlib.sha256(pre_cp011a).hexdigest() == '0da060b95836903301b85ca3b961351e260b295eed8125462035b294f6204b66'
pre_cp011b = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:14973])).encode('utf-8')
assert hashlib.sha256(pre_cp011b).hexdigest() == 'e407b947b136411745a4e253c868d3d2bd0208ab29d38277e4bb9b2691ba6987'
pre_cp011c = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:15577])).encode('utf-8')
assert hashlib.sha256(pre_cp011c).hexdigest() == 'b627c103a485f87dce708831c26cdfa9bc904d1c146689fda9f2b8bc79bcdf30'
cp011_data = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[14500:16500])).encode('utf-8')
assert len(cp011_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp011_data).hexdigest() == '7180b6e26e5854e3d92d4ace435936ef855bc60935bb59a2bd453e0920c7f929'
(root / 'cp011-complete-2000.jsonl').write_bytes(cp011_data)
pre_cp012a = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:16500])).encode('utf-8')
assert hashlib.sha256(pre_cp012a).hexdigest() == 'f571e0ffec0ea67f8768fe6110d8d76b9ee1ad03a594cda450db17615dac7074'
pre_cp012b = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:17060])).encode('utf-8')
assert hashlib.sha256(pre_cp012b).hexdigest() == 'd0049d16bb2bc945c97d76ae94d43d971a1b687ce13f5ad6a5401cf00689dfe5'
pre_cp012c = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:17557])).encode('utf-8')
assert hashlib.sha256(pre_cp012c).hexdigest() == 'a66a8703876165316420fa9dbdca987bd9fb386bd90692524498eb28a9a4d7f5'
pre_cp012d = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:18084])).encode('utf-8')
assert hashlib.sha256(pre_cp012d).hexdigest() == 'b414d20de2ae935e01bd0340d45f4ea2367e9e29aec982404fa54b9c59e495bb'
cp012_data = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[16500:18500])).encode('utf-8')
assert len(cp012_data.decode('utf-8').splitlines()) == 2000
assert hashlib.sha256(cp012_data).hexdigest() == '909e0100bf53eaef2ceb3af7880d418f0555440719048cd6ca98875b17418228'
(root / 'cp012-complete-2000.jsonl').write_bytes(cp012_data)
pre_cp013a = (''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in all_rows[:18500])).encode('utf-8')
assert hashlib.sha256(pre_cp013a).hexdigest() == '037d707bc441ca32f7ca8b36404882f56ad8ce591b8304b2e17d4d5b0baba05f'
assert hashlib.sha256(all_data).hexdigest() == '02ac3b537cd5ef62733f5753caf4a7a79b4b5d17146fb9cfd42342b3ba64d56c'
out.write_bytes(all_data)
print("PASS: 18785 unique processed entries =>", out)

# CP013b: preserve the independently verified CP013a prefix.
cp013b_data = bz2.decompress(base64.b64decode((root / "cp013b-208.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013b_data).hexdigest() == "4b8fbfea8ae9d2de3e00841aa16ddd872f21845b3caec55574dafa0be4e49e8c"
cp013b_rows = [json.loads(line) for line in cp013b_data.decode("utf-8").splitlines()]
assert len(cp013b_rows) == 208
for row in cp013b_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 18993
(root / "cp013b-new-208.jsonl").write_bytes(cp013b_data)
(root / "merged-CP013b-18993.jsonl").write_bytes(all_data + cp013b_data)
print("PASS: 18993 unique processed entries =>", root / "merged-CP013b-18993.jsonl")

# CP013c: append only to the verified CP013b prefix.
cp013c_data = bz2.decompress(base64.b64decode((root / "cp013c-118.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013c_data).hexdigest() == "caa176ee3ee0e6f178f545572dd834e3d8314b02e433c8c5f360cd674d280594"
cp013c_rows = [json.loads(line) for line in cp013c_data.decode("utf-8").splitlines()]
assert len(cp013c_rows) == 118
for row in cp013c_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19111
(root / "cp013c-new-118.jsonl").write_bytes(cp013c_data)
(root / "merged-CP013c-19111.jsonl").write_bytes(all_data + cp013b_data + cp013c_data)
print("PASS: 19111 unique processed entries =>", root / "merged-CP013c-19111.jsonl")
