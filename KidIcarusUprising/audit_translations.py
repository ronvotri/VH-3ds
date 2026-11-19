#!/usr/bin/env python3
"""Audit Kid Icarus JSONL batches against the handover ZIP without editing data.

Usage: python KidIcarusUprising/audit_translations.py --zip HANDOVER.zip
Optional: --translations DIR --output REPORT.json
Exit code 1 on structural errors. This is not semantic, glyph, or 3DS display QA.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile

SUFFIX = "ban_dich/tieng_anh_can_dich.jsonl"
CONTROL = re.compile(r"\{CTRL:[^}]+\}")

def parse(lines, label):
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{label}:{n}: {exc}") from exc
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise ValueError(f"{label}:{n}: id missing")
        yield row

def section(key):
    if "resident/03.bin#" in key:
        return "resident/03.bin"
    if "resident/04.bin#" in key:
        return "resident/04.bin"
    if "/stage/" in key:
        return "stage dialogue"
    return "other"

def audit(zip_path, translation_dir):
    with ZipFile(zip_path) as archive:
        matches = [p for p in archive.namelist() if p.endswith(SUFFIX)]
        if len(matches) != 1:
            raise ValueError(f"Expected one {SUFFIX}; found {len(matches)}")
        originals = list(parse(archive.read(matches[0]).decode("utf-8-sig").splitlines(), matches[0]))
    errors, warnings, source, seen = [], [], {}, {}
    groups = defaultdict(lambda: {"total":0, "nonempty":0, "processed":0, "uncovered":0})
    for item in originals:
        key = item["id"]
        if key in source:
            errors.append({"kind":"duplicate_source_id", "id":key})
        source[key] = item
        groups[section(key)]["total"] += 1
        groups[section(key)]["nonempty"] += bool(item.get("source"))
    for path in sorted(translation_dir.glob("batch_*.jsonl")):
        for row in parse(path.read_text(encoding="utf-8-sig").splitlines(), str(path)):
            key = row["id"]
            if key in seen:
                errors.append({"kind":"duplicate_overlay_id", "id":key, "first":seen[key], "again":str(path)})
                continue
            seen[key] = str(path)
            if key not in source:
                errors.append({"kind":"unknown_id", "id":key})
                continue
            original = source[key]
            if not original.get("source"):
                errors.append({"kind":"blank_original", "id":key})
            if not isinstance(row.get("vi"), str) or not row["vi"].strip():
                errors.append({"kind":"missing_translation", "id":key})
            if "source" in row and row["source"] != original.get("source"):
                errors.append({"kind":"source_mismatch", "id":key, "file":str(path)})
            if CONTROL.findall(original.get("source") or "") != CONTROL.findall(row.get("vi") or ""):
                errors.append({"kind":"control_mismatch", "id":key})
            if "source" not in row:
                warnings.append({"kind":"no_source_snapshot", "id":key})
            groups[section(key)]["processed"] += 1
    for key,item in source.items():
        if item.get("source") and key not in seen:
            groups[section(key)]["uncovered"] += 1
    return {
        "totals":{"source_rows":len(originals), "source_nonempty":sum(bool(x.get("source")) for x in originals),
                  "source_blank":sum(not bool(x.get("source")) for x in originals),
                  "unique_processed":len(seen), "nonempty_uncovered":sum(x["uncovered"] for x in groups.values())},
        "by_section":dict(sorted(groups.items())),
        "error_count":len(errors), "errors":errors,
        "warning_count":len(warnings), "warnings":warnings
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--zip", required=True, type=Path)
    p.add_argument("--translations", type=Path, default=Path(__file__).parent/"translations")
    p.add_argument("--output", type=Path)
    args=p.parse_args()
    if not args.zip.is_file() or not args.translations.is_dir():
        p.error("Source ZIP or translation directory not found")
    report=audit(args.zip,args.translations)
    data=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.write_text(data,encoding="utf-8")
    else:
        print(data)
    print(f"Unique={report['totals']['unique_processed']}, pending={report['totals']['nonempty_uncovered']}, errors={report['error_count']}, warnings={report['warning_count']}",file=sys.stderr)
    return int(report["error_count"]>0)

if __name__=="__main__":
    raise SystemExit(main())
