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

# CP013d: append only to the previously checked prefix.
cp013d_data = bz2.decompress(base64.b64decode((root / "cp013d-96.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013d_data).hexdigest() == "694cc80972f3449b9de24b5202fd3f4df77034fa9d4be835cd48fde10c32662a"
cp013d_rows = [json.loads(line) for line in cp013d_data.decode("utf-8").splitlines()]
assert len(cp013d_rows) == 96
for row in cp013d_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19207
(root / "cp013d-new-96.jsonl").write_bytes(cp013d_data)
(root / "merged-CP013d-19207.jsonl").write_bytes(all_data + cp013b_data + cp013c_data + cp013d_data)
print("PASS: 19207 unique processed entries =>", root / "merged-CP013d-19207.jsonl")

# CP013e: preserve the old translations, and keep name dispositions separate.
cp013e_data = bz2.decompress(base64.b64decode((root / "cp013e-33.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013e_data).hexdigest() == "990af65270dd9c6f42945663424f7c26a0d302903e2a57dedb0998e15b7bf3ed"
cp013e_rows = [json.loads(line) for line in cp013e_data.decode("utf-8").splitlines()]
assert len(cp013e_rows) == 33
for row in cp013e_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19240
review_dir = root.parent / "reviews"
review_data = bz2.decompress(base64.b64decode((review_dir / "cp013e-name-decisions.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(review_data).hexdigest() == "9e05b82e5e2e36bef71292630d574d6b03528b29783488eec9506ddb7dabbeae"
review_rows = [json.loads(line) for line in review_data.decode("utf-8").splitlines()]
review_ids = set()
for row in review_rows:
    assert set(row) == {"id", "source", "decision"}
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    assert row["decision"] in {"KEEP_SOURCE_NAME", "HOLD_PLACEHOLDER"}
    review_ids.add(row["id"])
assert len(review_ids) == 2696
assert sum(r["decision"] == "KEEP_SOURCE_NAME" for r in review_rows) == 2599
assert sum(r["decision"] == "HOLD_PLACEHOLDER" for r in review_rows) == 97
(root / "cp013e-new-33.jsonl").write_bytes(cp013e_data)
(root / "merged-CP013e-19240.jsonl").write_bytes(all_data + cp013b_data + cp013c_data + cp013d_data + cp013e_data)
(review_dir / "cp013e-name-decisions.jsonl").write_bytes(review_data)
print("PASS: 19240 translated entries, 2599 KEEP_SOURCE_NAME, 97 HOLD_PLACEHOLDER")

# CP013f: append translations and verify the separate KEEP ledger.
cp013f_data = bz2.decompress(base64.b64decode((root / "cp013f-113.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013f_data).hexdigest() == "4eb1e0ccd1ac4cd3430b21d40b62fe2a7b798047aae1e8aa78609fbeeb8b352f"
cp013f_rows = [json.loads(line) for line in cp013f_data.decode("utf-8").splitlines()]
assert len(cp013f_rows) == 113
for row in cp013f_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19353
cp013f_keep_data = bz2.decompress(base64.b64decode((review_dir / "cp013f-keep.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013f_keep_data).hexdigest() == "7978fad9809afa1dad66071d2d2b89628c68d4d6ae67b4b3ec45da1cf366a3f8"
cp013f_keep_rows = [json.loads(line) for line in cp013f_keep_data.decode("utf-8").splitlines()]
assert len(cp013f_keep_rows) == 1019
for row in cp013f_keep_rows:
    assert set(row) == {"id", "source", "decision"}
    assert row["decision"] == "KEEP_SOURCE_NAME"
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
assert len(review_ids) == 3715
(root / "cp013f-new-113.jsonl").write_bytes(cp013f_data)
(root / "merged-CP013f-19353.jsonl").write_bytes(all_data + cp013b_data + cp013c_data + cp013d_data + cp013e_data + cp013f_data)
(review_dir / "cp013f-keep.jsonl").write_bytes(cp013f_keep_data)
print("PASS: 19353 translated entries, 3618 KEEP_SOURCE_NAME, 97 HOLD_PLACEHOLDER")

# CP013g: preserve all prior bytes and separate translation, KEEP and HOLD.
cp013g_data = bz2.decompress(base64.b64decode((root / "cp013g-56.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013g_data).hexdigest() == "fca32d6f4511c71fcb2cbd92812a0b084fbb67b15097867a9ffe598d4fd226b5"
cp013g_rows = [json.loads(line) for line in cp013g_data.decode("utf-8").splitlines()]
assert len(cp013g_rows) == 56
for row in cp013g_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19409
cp013g_keep_data = bz2.decompress(base64.b64decode((review_dir / "cp013g-keep.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013g_keep_data).hexdigest() == "2e97e4b0c57fd8120f9ffa622128924a83a5460a0a125876331afaec0ae08019"
cp013g_keep_rows = [json.loads(line) for line in cp013g_keep_data.decode("utf-8").splitlines()]
assert len(cp013g_keep_rows) == 1065
for row in cp013g_keep_rows:
    assert set(row) == {"id", "source", "decision"} and row["decision"] == "KEEP_SOURCE_NAME"
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
cp013g_hold_data = bz2.decompress(base64.b64decode((review_dir / "cp013g-hold.jsonl.bz2.b64").read_text(encoding="ascii").strip(), validate=True))
assert hashlib.sha256(cp013g_hold_data).hexdigest() == "285c841ae9ea1a28a389af5fcdadaf1885c3a065d0335639202465293bd870e1"
cp013g_hold_rows = [json.loads(line) for line in cp013g_hold_data.decode("utf-8").splitlines()]
assert len(cp013g_hold_rows) == 628
for row in cp013g_hold_rows:
    assert set(row) == {"id", "source", "reason"}
    assert row["reason"] in {"RAW_VARIANT_NEEDS_MATCH", "AMBIGUOUS_LABEL"}
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
assert len(review_ids) == 5408
(root / "cp013g-new-56.jsonl").write_bytes(cp013g_data)
(root / "merged-CP013g-19409.jsonl").write_bytes(all_data + cp013b_data + cp013c_data + cp013d_data + cp013e_data + cp013f_data + cp013g_data)
(review_dir / "cp013g-keep.jsonl").write_bytes(cp013g_keep_data)
(review_dir / "cp013g-hold.jsonl").write_bytes(cp013g_hold_data)
print("PASS: 19409 translated entries, 4683 KEEP, 725 HOLD in CP013e-g ledgers")

# CP013h: distinguish translated labels, exact KEEP names, unresolved names,
# and semantic cross-language suggestions that must never be applied automatically.
def restore_cp013h_file(directory, name, checksum, count):
    data = bz2.decompress(base64.b64decode((directory / (name + ".bz2.b64")).read_text(encoding="ascii").strip(), validate=True))
    assert hashlib.sha256(data).hexdigest() == checksum
    rows = [json.loads(line) for line in data.decode("utf-8").splitlines()]
    assert len(rows) == count
    assert len({r["id"] for r in rows}) == count
    (directory / name).write_bytes(data)
    return data, rows

cp013h_data, cp013h_rows = restore_cp013h_file(root, "cp013h-28.jsonl", "6b42ba2b4df301b2d955d5073e41df85eb4395fd605f469a72c3be482de10d2e", 28)
for row in cp013h_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19437
_, cp013h_keep_rows = restore_cp013h_file(review_dir, "cp013h-keep.jsonl", "719ab70da1f510ddae80b333c6f41f1a53c54fd2580f716f3dac8cd7d06ba6c1", 121)
for row in cp013h_keep_rows:
    assert set(row) == {"id", "source", "decision"} and row["decision"] == "KEEP_SOURCE_NAME"
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
_, cp013h_hold_rows = restore_cp013h_file(review_dir, "cp013h-hold.jsonl", "28b2ea7bfe690efbdc9a46c7d5256268fe9c45be21bcabc9a152f8dc475d560f", 4095)
cp013h_hold_by_id = {}
for row in cp013h_hold_rows:
    assert set(row) == {"id", "source", "reason"}
    assert row["reason"] in {"HOLD_RAW_ITEM_NAME", "HOLD_ES_NAME", "HOLD_PLACEHOLDER"}
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
    cp013h_hold_by_id[row["id"]] = row
assert len(review_ids) == 9624
_, cp013h_candidates = restore_cp013h_file(review_dir, "cp013h-en-candidates.jsonl", "c49f2c9e1819133de96b6019310f4e11e7ddb3073e49958a7d4a6d9180f7633e", 54)
for row in cp013h_candidates:
    assert set(row) == {"id", "source", "english_candidates", "evidence_ids", "status"}
    assert row["status"] == "SEMANTIC_MATCH_NOT_APPLIED"
    assert row["id"] in cp013h_hold_by_id
    assert row["source"] == cp013h_hold_by_id[row["id"]]["source"]
    assert cp013h_hold_by_id[row["id"]]["reason"] == "HOLD_ES_NAME"
(root / "cp013h-new-28.jsonl").write_bytes(cp013h_data)
(root / "merged-CP013h-19437.jsonl").write_bytes(all_data + cp013b_data + cp013c_data + cp013d_data + cp013e_data + cp013f_data + cp013g_data + cp013h_data)
print("PASS: 19437 translation entries, 4804 KEEP, 4820 HOLD in CP013e-h ledgers, 54 unapplied candidate matches")

# CP013i: localize remaining English music and descriptive labels;
# do not modify internal asset labels or protected terms.
cp013i_data, cp013i_rows = restore_cp013h_file(root, "cp013i-49.jsonl", "83e1ba5446ce675722f2367300f9ee90f432571be05b34436ec2711eb6bd826c", 49)
for row in cp013i_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    ids.add(row["id"])
assert len(ids) == 19486
_, cp013i_keep_rows = restore_cp013h_file(review_dir, "cp013i-keep.jsonl", "e31bf2318835a94cbffc8a9e4156190a3531141d86311801c26fc7804a963a25", 412)
for row in cp013i_keep_rows:
    assert set(row) == {"id", "source", "decision"} and row["decision"] == "KEEP_SOURCE_NAME"
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
_, cp013i_hold_rows = restore_cp013h_file(review_dir, "cp013i-hold.jsonl", "71ef5e9a6020a7cbc111cd56e8ea7a57f448c647004c9ad48b020ec8de1123de", 805)
for row in cp013i_hold_rows:
    assert set(row) == {"id", "source", "reason"} and row["reason"] in {"HOLD_UI_ASSET_METADATA", "HOLD_PLACEHOLDER"}
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
assert len(review_ids) == 10841
(root / "cp013i-new-49.jsonl").write_bytes(cp013i_data)
(root / "merged-CP013i-19486.jsonl").write_bytes(all_data + cp013b_data + cp013c_data + cp013d_data + cp013e_data + cp013f_data + cp013g_data + cp013h_data + cp013i_data)
print("PASS: 19486 translation entries, 5216 KEEP, 5625 HOLD in CP013e-i ledgers")

# CP013j and CP013k: independently restore each batch, with strict ID separation.
latest_data = (root / "merged-CP013i-19486.jsonl").read_bytes()
for checkpoint, count, checksum, total, keep_spec, hold_spec in [
    ("j", 121, "d772dfb5c106710697d9b436112b38a8328a9ccfbb6fa8cc8fc7bbc9a52cf99b", 19607, None,
     (464, "b24b71f6f0f6892dfe605a235ad269c455ec2172cca658d0af027b243000255f")),
    ("k", 18, "b6ab7ec5f0ed5d281ed13c1a02d112d0b2cf9dffb76972847372b4b9c0f8934f", 19625,
     (85, "8c3b2dbcc88290f8e8e39bbf4565d4951cfb3cd5c34345a7b48771ab60e30a5b"),
     (1634, "7039dcc515276de2800cb92af71253845d9d409162a41184166968afc26a3c3e")),
]:
    prefix = "cp013" + checkpoint
    data, new_rows = restore_cp013h_file(root, f"{prefix}-{count}.jsonl", checksum, count)
    for row in new_rows:
        assert set(row) == {"id", "vi"} and row["vi"]
        assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
        ids.add(row["id"])
    assert len(ids) == total
    for kind, spec in [("keep", keep_spec), ("hold", hold_spec)]:
        if spec is None:
            continue
        n, digest = spec
        _, ledger = restore_cp013h_file(review_dir, f"{prefix}-{kind}.jsonl", digest, n)
        for row in ledger:
            assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
            if kind == "keep":
                assert set(row) == {"id", "source", "decision"} and row["decision"] == "KEEP_SOURCE_NAME"
            else:
                assert set(row) == {"id", "source", "reason"} and row["reason"].startswith("HOLD_")
            review_ids.add(row["id"])
    latest_data += data
    (root / f"{prefix}-new-{count}.jsonl").write_bytes(data)
    (root / f"merged-CP013{checkpoint}-{total}.jsonl").write_bytes(latest_data)
assert len(ids) == 19625 and len(review_ids) == 13024
print("PASS: 19625 translation entries, 5301 KEEP, 7723 HOLD")

# CP013l: classify the remaining source IDs without treating HOLD as completed.
cp013l_data, cp013l_rows = restore_cp013h_file(root, "cp013l-11.jsonl", "e3d7605a53ea524bc2b41486b21b3b8e7e8c3eceae662ae4055cc004e83bde74", 11)
for row in cp013l_rows:
    assert set(row) == {"id", "vi"} and row["vi"]
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    ids.add(row["id"])
_, cp013l_keep_rows = restore_cp013h_file(review_dir, "cp013l-keep.jsonl", "a23a695f81a72029f13dd901aea82dcb02e81140be4552eefbb87dcaaef93a9b", 145)
for row in cp013l_keep_rows:
    assert set(row) == {"id", "source", "decision"}
    assert row["decision"] in {"KEEP_SOURCE_NAME", "KEEP_FORMAT_LITERAL"}
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
assert sum(r["decision"] == "KEEP_FORMAT_LITERAL" for r in cp013l_keep_rows) == 17
_, cp013l_hold_rows = restore_cp013h_file(review_dir, "cp013l-hold.jsonl", "22693f30be26e31460f03a30eeebb05e55c6e3ac53cd73332613b72cc8accad0", 2007)
for row in cp013l_hold_rows:
    assert set(row) == {"id", "source", "reason"} and row["reason"].startswith("HOLD_")
    assert row["id"] not in ids and row["id"] not in review_ids, row["id"]
    review_ids.add(row["id"])
assert len(ids) == 19636 and len(review_ids) == 15176
assert len(ids | review_ids) == 34812
(root / "cp013l-new-11.jsonl").write_bytes(cp013l_data)
(root / "merged-CP013l-19636.jsonl").write_bytes(latest_data + cp013l_data)
print("PASS: 19636 translation entries, 5446 KEEP, 9730 HOLD; classification counts cover 34812 IDs")

# CP014a: resolve previously held IDs without rewriting historical ledgers.
hold_by_id = {}
for r in review_rows:
    if r["decision"] == "HOLD_PLACEHOLDER":
        hold_by_id[r["id"]] = r
for checkpoint in ("g", "h", "i", "j", "k", "l"):
    for line in (review_dir / f"cp013{checkpoint}-hold.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        assert r["id"] not in hold_by_id
        hold_by_id[r["id"]] = r
assert len(hold_by_id) == 9730
assert set(hold_by_id) <= review_ids
_, resolutions = restore_cp013h_file(review_dir, "cp014a-resolutions.jsonl", "917a9885679d89cf22a79b213075a24115d0f57f6edcd0e56f1a29f032218eaa", 326)
cp014a_translations = []
cp014a_keep = []
for row in resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014a_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] == "KEEP_FORMAT_LITERAL"
        cp014a_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014a_translations) == 73 and len(cp014a_keep) == 253
assert len(ids) == 19709 and len(hold_by_id) == 9404
assert len(review_ids) == 15103 and len(review_ids - set(hold_by_id)) == 5699
assert not ids & review_ids and len(ids | review_ids) == 34812
def cp014a_jsonl(rows):
    return "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows).encode("utf-8")
cp014a_data = cp014a_jsonl(cp014a_translations)
(root / "cp014a-new-73.jsonl").write_bytes(cp014a_data)
(root / "merged-CP014a-19709.jsonl").write_bytes((root / "merged-CP013l-19636.jsonl").read_bytes() + cp014a_data)
(review_dir / "cp014a-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014a_keep))
(review_dir / "remaining-HOLD-CP014a-9404.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 19709 translation entries, 5699 KEEP, 9404 HOLD")

# CP014b: exact fallback-label translation and explicit source-preservation decisions.
_, cp014b_resolutions = restore_cp013h_file(review_dir, "cp014b-resolutions.jsonl", "aa7eb1fe89174f79833f875b2012410555e1e66966fc7f5d870725b060db27b3", 744)
cp014b_translations = []
cp014b_keep = []
for row in cp014b_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] == "GENERIC_FALLBACK_LABEL"
        assert row["vi"] and row["vi"] != row["source"]
        cp014b_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] in {"KEEP_FORMAT_LITERAL", "KEEP_SOURCE_NAME"}
        cp014b_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014b_translations) == 519 and len(cp014b_keep) == 225
assert sum(r["decision"] == "KEEP_SOURCE_NAME" for r in cp014b_keep) == 19
assert len(ids) == 20228 and len(hold_by_id) == 8660
assert len(review_ids) == 14584 and len(review_ids - set(hold_by_id)) == 5924
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014b_data = cp014a_jsonl(cp014b_translations)
(root / "cp014b-new-519.jsonl").write_bytes(cp014b_data)
(root / "merged-CP014b-20228.jsonl").write_bytes((root / "merged-CP014a-19709.jsonl").read_bytes() + cp014b_data)
(review_dir / "cp014b-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014b_keep))
(review_dir / "remaining-HOLD-CP014b-8660.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20228 translation entries, 5924 KEEP, 8660 HOLD")

# CP014c: resolve descriptive labels and retain resource descriptors unchanged.
_, cp014c_resolutions = restore_cp013h_file(review_dir, "cp014c-resolutions.jsonl", "ff85192518442c95498cdfe6becfdd7eb5a87b68c35f4dff70e4651b1c83f927", 1031)
cp014c_translations = []
cp014c_keep = []
for row in cp014c_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"CONTEXTUAL_UI_LABEL", "GENERIC_CREATURE_CATEGORY", "GENERIC_HOUSE_OR_TRANSPORT_LABEL"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014c_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] == "KEEP_FORMAT_LITERAL"
        assert row["reason"] in {"PRESERVE_UI_RESOURCE_DESCRIPTORS", "PRESERVE_AUDIO_RESOURCE_DESCRIPTORS", "EXPLICIT_RESERVED_SLOT_LABEL", "PRESERVE_EVENT_REFERENCE_OR_RESERVED_SLOT"}
        cp014c_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014c_translations) == 71 and len(cp014c_keep) == 960
assert len(ids) == 20299 and len(hold_by_id) == 7629
assert len(review_ids) == 14513 and len(review_ids - set(hold_by_id)) == 6884
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014c_data = cp014a_jsonl(cp014c_translations)
(root / "cp014c-new-71.jsonl").write_bytes(cp014c_data)
(root / "merged-CP014c-20299.jsonl").write_bytes((root / "merged-CP014b-20228.jsonl").read_bytes() + cp014c_data)
(review_dir / "cp014c-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014c_keep))
(review_dir / "remaining-HOLD-CP014c-7629.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20299 translation entries, 6884 KEEP, 7629 HOLD")

# CP014d: system messages, Bliss reward headings and protected source literals.
_, cp014d_resolutions = restore_cp013h_file(review_dir, "cp014d-resolutions.jsonl", "c603640ee8d145eca94daf8ad339045ba6a3ea10225cf39bbb2dd50a0d1095bf", 341)
cp014d_translations = []
cp014d_keep = []
for row in cp014d_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"SYSTEM_MESSAGE", "BLISS_REWARD_HEADING"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014d_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] in {"KEEP_SOURCE_NAME", "KEEP_FORMAT_LITERAL"}
        assert row["reason"] in {"MAP_CONNECTION_REFERENCE", "NUMBERED_PET_TABLE_LABEL", "CORE_STAT_LABEL", "EXPLICIT_DUMMY_SLOT", "NAMED_BLISS_FEATURE"}
        cp014d_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014d_translations) == 45 and len(cp014d_keep) == 296
assert len(ids) == 20344 and len(hold_by_id) == 7288
assert len(review_ids) == 14468 and len(review_ids - set(hold_by_id)) == 7180
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014d_data = cp014a_jsonl(cp014d_translations)
(root / "cp014d-new-45.jsonl").write_bytes(cp014d_data)
(root / "merged-CP014d-20344.jsonl").write_bytes((root / "merged-CP014c-20299.jsonl").read_bytes() + cp014d_data)
(review_dir / "cp014d-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014d_keep))
(review_dir / "remaining-HOLD-CP014d-7288.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20344 translation entries, 7180 KEEP, 7288 HOLD")

# CP014e: resolve descriptive labels and preserve marked or matching source names.
_, cp014e_resolutions = restore_cp013h_file(review_dir, "cp014e-resolutions.jsonl", "b3925a80d6bb0e7e9966ba6fc08dc10f4594cdc8118a5a6e596eed64583c266c", 1129)
cp014e_translations = []
cp014e_keep = []
for row in cp014e_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"DESCRIPTIVE_EVENT_LABEL", "CONTEXTUAL_UI_LABEL", "GENERIC_CREATURE_CATEGORY"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014e_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] in {"KEEP_SOURCE_NAME", "KEEP_FORMAT_LITERAL"}
        assert row["reason"] in {"PRESERVE_HASH_MARKED_SOURCE", "CASEFOLD_NAME_MATCH", "CREATURE_CATEGORY_TERM"}
        cp014e_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014e_translations) == 49 and len(cp014e_keep) == 1080
assert len(ids) == 20393 and len(hold_by_id) == 6159
assert len(review_ids) == 14419 and len(review_ids - set(hold_by_id)) == 8260
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014e_data = cp014a_jsonl(cp014e_translations)
(root / "cp014e-new-49.jsonl").write_bytes(cp014e_data)
(root / "merged-CP014e-20393.jsonl").write_bytes((root / "merged-CP014d-20344.jsonl").read_bytes() + cp014e_data)
(review_dir / "cp014e-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014e_keep))
(review_dir / "remaining-HOLD-CP014e-6159.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20393 translation entries, 8260 KEEP, 6159 HOLD")

# CP014f: resolve descriptive labels and preserve technical descriptors.
_, cp014f_resolutions = restore_cp013h_file(review_dir, "cp014f-resolutions.jsonl", "203ffa86774b0acd96344caced97d2aee3c0efb98d4f76949b8febb18c80bf28", 230)
cp014f_translations = []
cp014f_keep = []
for row in cp014f_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"DESCRIPTIVE_EVENT_LABEL", "STATISTICS_LABEL", "CONTEXTUAL_UI_LABEL", "HOUSE_LAYOUT_LABEL", "DESCRIPTIVE_LOCATION_LABEL"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014f_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] == "KEEP_FORMAT_LITERAL"
        assert row["reason"] in {"PRESERVE_AI_OR_TARGET_DESCRIPTOR", "EXPLICIT_RESERVED_EFFECT_DESCRIPTOR", "EXPLICIT_DUMMY_SLOT", "EXPLICIT_TEST_OR_RESERVED_MAP_LABEL"}
        cp014f_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014f_translations) == 114 and len(cp014f_keep) == 116
assert len(ids) == 20507 and len(hold_by_id) == 5929
assert len(review_ids) == 14305 and len(review_ids - set(hold_by_id)) == 8376
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014f_data = cp014a_jsonl(cp014f_translations)
(root / "cp014f-new-114.jsonl").write_bytes(cp014f_data)
(root / "merged-CP014f-20507.jsonl").write_bytes((root / "merged-CP014e-20393.jsonl").read_bytes() + cp014f_data)
(review_dir / "cp014f-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014f_keep))
(review_dir / "remaining-HOLD-CP014f-5929.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20507 translation entries, 8376 KEEP, 5929 HOLD")

# CP014g: contextual labels and orthographic name matches, without rewriting names.
_, cp014g_resolutions = restore_cp013h_file(review_dir, "cp014g-resolutions.jsonl", "e22d7463259713137bef34a747bdbbeff7118ad16c49c285b934aa3ab50b6552", 138)
cp014g_translations = []
cp014g_keep = []
for row in cp014g_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"AVATAR_VOICE_LABEL", "SYSTEM_MESSAGE", "BLISS_REWARD_HEADING", "GENERIC_TRANSPORT_LABEL", "STATISTICS_LABEL", "CATEGORY_LABEL", "CONTEXTUAL_UI_LABEL", "DESCRIPTIVE_EVENT_LABEL", "DESCRIPTIVE_LOCATION_LABEL"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014g_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] == "KEEP_SOURCE_NAME"
        assert row["reason"] in {"ORTHOGRAPHIC_NAME_MATCH", "NAMED_EN_TABLE_ENTRY"}
        cp014g_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014g_translations) == 49 and len(cp014g_keep) == 89
assert len(ids) == 20556 and len(hold_by_id) == 5791
assert len(review_ids) == 14256 and len(review_ids - set(hold_by_id)) == 8465
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014g_data = cp014a_jsonl(cp014g_translations)
(root / "cp014g-new-49.jsonl").write_bytes(cp014g_data)
(root / "merged-CP014g-20556.jsonl").write_bytes((root / "merged-CP014f-20507.jsonl").read_bytes() + cp014g_data)
(review_dir / "cp014g-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014g_keep))
(review_dir / "remaining-HOLD-CP014g-5791.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20556 translation entries, 8465 KEEP, 5791 HOLD")

# CP014h: resolve contextual labels and preserve structured source references.
_, cp014h_resolutions = restore_cp013h_file(review_dir, "cp014h-resolutions.jsonl", "669f1fa8cbaee497001588fe0ca2c35dc2fbbf9401a339a082f61a6a33f4dfbc", 96)
cp014h_translations = []
cp014h_keep = []
for row in cp014h_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"DESCRIPTIVE_EVENT_LABEL", "STATISTICS_LABEL", "AVATAR_LAYOUT_LABEL", "HOUSE_LAYOUT_LABEL", "CONTEXTUAL_UI_LABEL"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014h_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] in {"KEEP_SOURCE_NAME", "KEEP_FORMAT_LITERAL"}
        assert row["reason"] in {"STRUCTURED_ENCOUNTER_REFERENCE", "PROTECTED_TERM_OR_FEATURE", "EXPLICIT_FORMAT_LITERAL"}
        cp014h_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014h_translations) == 42 and len(cp014h_keep) == 54
assert len(ids) == 20598 and len(hold_by_id) == 5695
assert len(review_ids) == 14214 and len(review_ids - set(hold_by_id)) == 8519
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014h_data = cp014a_jsonl(cp014h_translations)
(root / "cp014h-new-42.jsonl").write_bytes(cp014h_data)
(root / "merged-CP014h-20598.jsonl").write_bytes((root / "merged-CP014g-20556.jsonl").read_bytes() + cp014h_data)
(review_dir / "cp014h-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014h_keep))
(review_dir / "remaining-HOLD-CP014h-5695.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
print("PASS: 20598 translation entries, 8519 KEEP, 5695 HOLD")

# CP014i: distinguish actual resolution from provisional source-name preservation.
_, cp014i_resolutions = restore_cp013h_file(review_dir, "cp014i-resolutions.jsonl", "4ebbe67d5c592fcea677c5bdcb0e2d3679bd8a5b742824faa53f4ae62cee002b", 160)
cp014i_translations = []
cp014i_keep = []
for row in cp014i_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] == "CONTEXTUAL_LABEL"
        assert row["vi"] and row["vi"] != row["source"]
        cp014i_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] in {"KEEP_SOURCE_NAME", "KEEP_FORMAT_LITERAL"}
        assert row["reason"] == "SOURCE_TERM_OR_STRUCTURED_LABEL"
        cp014i_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014i_translations) == 138 and len(cp014i_keep) == 22
_, cp014i_pending_names = restore_cp013h_file(review_dir, "cp014i-preserve-pending.jsonl", "2991d987d00bd7836abc6c9ae971e0be0d0256d5e7055a9afc29e698df09dfb2", 3814)
pending_name_ids = set()
for row in cp014i_pending_names:
    i = row["id"]
    assert set(row) == {"id", "source", "decision", "reason"}
    assert row["decision"] == "PRESERVE_PENDING_NAME_QA"
    assert row["reason"] in {"RAW_ITEM_TABLE", "RAW_NPC_TABLE", "RAW_CREATURE_TABLE"}
    assert i in hold_by_id and i in review_ids and i not in ids and i not in pending_name_ids
    assert row["source"] == hold_by_id[i]["source"]
    pending_name_ids.add(i)
# Pending names remain in HOLD. Never add them to KEEP or the translated output.
assert len(ids) == 20736 and len(hold_by_id) == 5535
assert len(review_ids) == 14076 and len(review_ids - set(hold_by_id)) == 8541
assert len(pending_name_ids) == 3814 and len(set(hold_by_id) - pending_name_ids) == 1721
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014i_data = cp014a_jsonl(cp014i_translations)
(root / "cp014i-new-138.jsonl").write_bytes(cp014i_data)
(root / "merged-CP014i-20736.jsonl").write_bytes((root / "merged-CP014h-20598.jsonl").read_bytes() + cp014i_data)
(review_dir / "cp014i-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014i_keep))
(review_dir / "remaining-HOLD-CP014i-5535.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
(review_dir / "remaining-active-HOLD-CP014i-1721.jsonl").write_bytes(cp014a_jsonl(r for i,r in hold_by_id.items() if i not in pending_name_ids))
print("PASS: 20736 translation entries, 8541 KEEP, 5535 HOLD (3814 provisional names + 1721 other)")

# CP014j: translate explicit descriptors; retain unverified names and drafts in HOLD.
_, cp014j_resolutions = restore_cp013h_file(review_dir, "cp014j-resolutions.jsonl", "3c07cc6503a5416475bd63305605086b97e6ceffde973be1c734990af6342eda", 104)
cp014j_translations = []
cp014j_keep = []
for row in cp014j_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids and i not in pending_name_ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"PARTIAL_DESCRIPTOR", "CONTEXTUAL_LABEL"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014j_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] in {"KEEP_SOURCE_NAME", "KEEP_FORMAT_LITERAL"}
        assert row["reason"] in {"SOURCE_NAME_OR_FEATURE", "EXPLICIT_DUMMY"}
        cp014j_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014j_translations) == 97 and len(cp014j_keep) == 7
_, cp014j_pending = restore_cp013h_file(review_dir, "cp014j-preserve-pending.jsonl", "5903de8a5274596da2bf2dd989b2900a1ecd7e1563d272dd26a879788b547bc1", 1005)
for row in cp014j_pending:
    i = row["id"]
    assert set(row) == {"id", "source", "decision", "reason"}
    assert row["decision"] == "PRESERVE_PENDING_NAME_QA"
    assert row["reason"] in {"RAW_ITEM_OR_CREATURE_OR_LOCATION_NAME", "RAW_SKILL_LABEL"}
    assert i in hold_by_id and i in review_ids and i not in ids and i not in pending_name_ids
    assert row["source"] == hold_by_id[i]["source"]
    pending_name_ids.add(i)
_, cp014j_drafts = restore_cp013h_file(review_dir, "cp014j-drafts.jsonl", "919129f30b0db463c97adcc04d205214b1afa68da38c5ad7a30c0563a5465207", 27)
for row in cp014j_drafts:
    i = row["id"]
    assert set(row) == {"id", "source", "vi", "reason"}
    assert row["reason"] in {"SPANISH_NAME_UNVERIFIED", "DELIVERY_FEATURE_AMBIGUOUS"}
    assert i in hold_by_id and i not in pending_name_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"] and row["vi"] != row["source"]
assert len(ids) == 20833 and len(hold_by_id) == 5431
assert len(review_ids) == 13979 and len(review_ids - set(hold_by_id)) == 8548
assert len(pending_name_ids) == 4819 and len(set(hold_by_id) - pending_name_ids) == 612
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014j_data = cp014a_jsonl(cp014j_translations)
(root / "cp014j-new-97.jsonl").write_bytes(cp014j_data)
(root / "merged-CP014j-20833.jsonl").write_bytes((root / "merged-CP014i-20736.jsonl").read_bytes() + cp014j_data)
(review_dir / "cp014j-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014j_keep))
(review_dir / "remaining-HOLD-CP014j-5431.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
(review_dir / "remaining-active-HOLD-CP014j-612.jsonl").write_bytes(cp014a_jsonl(r for i,r in hold_by_id.items() if i not in pending_name_ids))
print("PASS: 20833 translation entries, 8548 KEEP, 5431 HOLD (4819 provisional names + 612 other)")

# CP014k: recover official EN_A equipment names from aligned source-table groups.
_, cp014k_resolutions = restore_cp013h_file(review_dir, "cp014k-resolutions.jsonl", "5ce73c6f33e0a8f9e3b75e26bc379ff943f44f0141fdae9ff66d3452a8f4bd8d", 123)
cp014k_translations = []
cp014k_keep = []
for row in cp014k_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids and i not in pending_name_ids
    assert row["source"] == hold_by_id[i]["source"]
    if row["decision"] == "TRANSLATE":
        assert set(row) == {"id", "source", "decision", "reason", "vi"}
        assert row["reason"] in {"EN_A_EQUIPMENT_NAME_ALIGNMENT", "EN_A_LOCATION_NAME_SEMANTIC_MATCH", "CONTEXTUAL_LABEL"}
        assert row["vi"] and row["vi"] != row["source"]
        cp014k_translations.append({"id": i, "vi": row["vi"]})
        review_ids.remove(i)
        ids.add(i)
    else:
        assert set(row) == {"id", "source", "decision", "reason"}
        assert row["decision"] == "KEEP_SOURCE_NAME"
        assert row["reason"] == "EXACT_LOCATION_NAME_CASEFOLD"
        cp014k_keep.append({"id": i, "source": row["source"], "decision": row["decision"]})
    del hold_by_id[i]
assert len(cp014k_translations) == 121 and len(cp014k_keep) == 2
assert sum(r["reason"] == "EN_A_EQUIPMENT_NAME_ALIGNMENT" for r in cp014k_resolutions) == 104
assert sum(r["reason"] == "EN_A_LOCATION_NAME_SEMANTIC_MATCH" for r in cp014k_resolutions) == 4
assert len(ids) == 20954 and len(hold_by_id) == 5308
assert len(review_ids) == 13858 and len(review_ids - set(hold_by_id)) == 8550
assert len(pending_name_ids) == 4819 and len(set(hold_by_id) - pending_name_ids) == 489
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014k_data = cp014a_jsonl(cp014k_translations)
(root / "cp014k-new-121.jsonl").write_bytes(cp014k_data)
(root / "merged-CP014k-20954.jsonl").write_bytes((root / "merged-CP014j-20833.jsonl").read_bytes() + cp014k_data)
(review_dir / "cp014k-resolved-keep.jsonl").write_bytes(cp014a_jsonl(cp014k_keep))
(review_dir / "remaining-HOLD-CP014k-5308.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
(review_dir / "remaining-active-HOLD-CP014k-489.jsonl").write_bytes(cp014a_jsonl(r for i,r in hold_by_id.items() if i not in pending_name_ids))
print("PASS: 20954 replacement entries, 8550 KEEP, 5308 HOLD (4819 provisional names + 489 other)")

# CP014l: promote manually aligned source names and explicit contextual labels.
_, cp014l_resolutions = restore_cp013h_file(review_dir, "cp014l-resolutions.jsonl", "a9add11979e1bb54795a1210517e8aaa21ef2bb94fcc824b8efbaf9da8290b7b", 451)
cp014l_translations = []
for row in cp014l_resolutions:
    i = row["id"]
    assert i in hold_by_id and i in review_ids and i not in ids
    assert row["source"] == hold_by_id[i]["source"]
    assert set(row) == {"id", "source", "decision", "reason", "vi"}
    assert row["decision"] == "TRANSLATE"
    assert row["reason"] in {"EN_A_ITEM_NAME_ALIGNMENT", "CONTEXTUAL_LABEL"}
    assert row["vi"] and row["vi"] != row["source"]
    if row["reason"] == "EN_A_ITEM_NAME_ALIGNMENT":
        assert i in pending_name_ids
        pending_name_ids.remove(i)
    else:
        assert i not in pending_name_ids
    cp014l_translations.append({"id": i, "vi": row["vi"]})
    review_ids.remove(i)
    ids.add(i)
    del hold_by_id[i]
assert len(cp014l_translations) == 451
assert sum(r["reason"] == "EN_A_ITEM_NAME_ALIGNMENT" for r in cp014l_resolutions) == 447
assert len(ids) == 21405 and len(hold_by_id) == 4857
assert len(review_ids) == 13407 and len(review_ids - set(hold_by_id)) == 8550
assert len(pending_name_ids) == 4372 and len(set(hold_by_id) - pending_name_ids) == 485
assert pending_name_ids <= set(hold_by_id)
assert not ids & review_ids and len(ids | review_ids) == 34812
cp014l_data = cp014a_jsonl(cp014l_translations)
(root / "cp014l-new-451.jsonl").write_bytes(cp014l_data)
(root / "merged-CP014l-21405.jsonl").write_bytes((root / "merged-CP014k-20954.jsonl").read_bytes() + cp014l_data)
(review_dir / "remaining-HOLD-CP014l-4857.jsonl").write_bytes(cp014a_jsonl(hold_by_id.values()))
(review_dir / "remaining-active-HOLD-CP014l-485.jsonl").write_bytes(cp014a_jsonl(r for i,r in hold_by_id.items() if i not in pending_name_ids))
(review_dir / "remaining-pending-names-CP014l-4372.jsonl").write_bytes(cp014a_jsonl(r for i,r in hold_by_id.items() if i in pending_name_ids))
print("PASS: 21405 replacement entries, 8550 KEEP, 4857 HOLD (4372 provisional names + 485 other)")
