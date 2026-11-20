#!/usr/bin/env python3
"""Build one source-indexed translation master. STAGING ONLY: does not patch ROM.

python KidIcarusUprising/build_master.py --zip SOURCE.zip --translations KidIcarusUprising/translations --out build/kid_icarus --strict
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

SOURCE_SUFFIX = "ban_dich/tieng_anh_can_dich.jsonl"
CONTROL = re.compile(r"\{CTRL:[0-9a-fA-F]+\}")

def read_jsonl(s, name):
    for n, line in enumerate(s.splitlines(), 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{name}:{n}: {exc}") from exc
        if not isinstance(x, dict) or not isinstance(x.get("id"), str):
            raise ValueError(f"{name}:{n}: missing id")
        yield x

def build(zip_path, translations, out):
    with ZipFile(zip_path) as z:
        paths = [n for n in z.namelist() if n.endswith(SOURCE_SUFFIX)]
        if len(paths) != 1:
            raise ValueError(f"Expected one EN JSONL: found {len(paths)}")
        source = list(read_jsonl(z.read(paths[0]).decode("utf-8-sig"), paths[0]))
    issues = []
    original = {}
    for x in source:
        if x["id"] in original:
            issues.append({"kind": "duplicate_source", "id": x["id"]})
        original[x["id"]] = x
    overlay, origin_file = {}, {}
    batches = sorted(translations.glob("batch_*.jsonl"))
    for path in batches:
        for x in read_jsonl(path.read_text(encoding="utf-8-sig"), str(path)):
            key = x["id"]
            if key in overlay:
                issues.append({"kind": "duplicate_overlay", "id": key, "first": origin_file[key], "again": path.name})
                continue
            overlay[key], origin_file[key] = x, path.name
            if key not in original:
                issues.append({"kind": "unknown_id", "id": key})
                continue
            en, vi = original[key].get("source") or "", x.get("vi")
            if not en:
                issues.append({"kind": "blank_original", "id": key})
            if not isinstance(vi, str) or not vi.strip():
                issues.append({"kind": "blank_translation", "id": key})
                continue
            if "source" in x and x["source"] != en:
                issues.append({"kind": "source_mismatch", "id": key})
            if CONTROL.findall(en) != CONTROL.findall(vi):
                issues.append({"kind": "control_mismatch", "id": key})
    master = []
    for src in source:
        x = dict(src)
        edited = overlay.get(x["id"])
        if edited and src.get("source") and isinstance(edited.get("vi"), str) and edited["vi"].strip():
            x["vi"] = edited["vi"]
            x["status"] = edited.get("status", "draft")
            x["batch"] = origin_file[x["id"]]
        else:
            x["vi"] = ""
            x["status"] = "untranslated_blank" if not src.get("source") else "preserve_source"
        master.append(x)
    report = {
        "scope": "master JSONL staging only; NOT a playable 3DS patch",
        "source_rows": len(source),
        "source_nonempty": sum(bool(x.get("source")) for x in source),
        "source_blank": sum(not x.get("source") for x in source),
        "batch_files": len(batches),
        "unique_overlay_ids": len(overlay),
        "master_rows": len(master),
        "overlay_applied": sum(bool(x["vi"]) for x in master),
        "nonempty_without_overlay": sum(bool(x.get("source")) and not x["vi"] for x in master),
        "issue_counts": dict(Counter(e["kind"] for e in issues)),
        "issues": issues,
    }
    out.mkdir(parents=True, exist_ok=True)
    (out / "kid_icarus_master.jsonl").write_text(
        "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in master), encoding="utf-8"
    )
    (out / "preflight_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--zip", required=True, type=Path)
    p.add_argument("--translations", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--strict", action="store_true")
    a = p.parse_args()
    if not a.zip.is_file() or not a.translations.is_dir():
        p.error("ZIP or translations directory not found")
    report = build(a.zip, a.translations, a.out)
    print(json.dumps({k:v for k,v in report.items() if k != "issues"}, ensure_ascii=False, indent=2))
    if a.strict and report["issues"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
