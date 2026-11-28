#!/usr/bin/env python3
"""Read-only QA049 source preflight. Never imports, repacks, or patches CFG."""
import argparse
import hashlib
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def sha(data):
    return hashlib.sha256(data).hexdigest()

def inspect_source(path, expected, rows):
    if not path.is_file():
        return {'status': 'missing'}
    try:
        data = path.read_bytes()
    except OSError as exc:
        return {'status': 'read_error', 'detail': str(exc)}
    actual = sha(data)
    out = {'actual_sha256': actual, 'actual_file_bytes': len(data)}
    if actual != expected['file_sha256']:
        return {**out, 'status': 'hash_mismatch'}
    # Hypothesis from SOURCE_GUIDANCE/04; not a complete CFG parser.
    if len(data) < 12:
        return {**out, 'status': 'header_too_short'}
    start, size = struct.unpack_from('<II', data, 4)
    out.update(pool_start=start, declared_pool_bytes=size)
    if start < 12 or start > len(data) or size > len(data)-start:
        return {**out, 'status': 'pool_header_mismatch'}
    raw_pool = b''.join(bytes.fromhex(row['raw_hex']) + b'\0' for row in rows)
    pool = data[start:start+size]
    if sha(raw_pool) != expected['source_pool_sha256']:
        return {**out, 'status': 'manifest_pool_mismatch'}
    if pool[:len(raw_pool)] != raw_pool:
        return {**out, 'status': 'pool_bytes_mismatch'}
    # Do not infer padding, metadata, or unknown references are disposable.
    tail = pool[len(raw_pool):]
    out['extra_pool_bytes'] = len(tail)
    out['extra_pool_all_zero'] = all(b == 0 for b in tail)
    invalid = [ref['record_byte_offset'] for row in rows
               for ref in row['references_known']
               if not 0 <= ref['record_byte_offset'] < len(data)]
    if invalid:
        return {**out, 'status': 'known_ref_out_of_bounds', 'invalid_offsets': invalid}
    return {**out, 'status': 'source_match_extra_pool' if tail else 'source_match_exact_pool'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--base', type=Path, required=True, help='Extracted Base archive root containing data/txt/ja')
    ap.add_argument('--update', type=Path, required=True, help='Extracted Update archive root containing data/txt/ja')
    ap.add_argument('--dataset', type=Path, default=ROOT/'QA049_FULL_32067.jsonl')
    ap.add_argument('--manifest', type=Path, default=ROOT/'source_manifest.json')
    ap.add_argument('--report', type=Path, default=ROOT/'preflight_result.json')
    args = ap.parse_args()
    from collections import defaultdict, Counter
    manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
    blob = args.dataset.read_bytes()
    if sha(blob) != manifest['dataset_sha256']:
        ap.error('Dataset SHA-256 mismatch; refuse validation against altered dataset.')
    groups = defaultdict(list)
    for line in blob.splitlines():
        row = json.loads(line)
        groups[row['source_kind'], row['file']].append(row)
    roots = {'base': args.base.resolve(), 'update': args.update.resolve()}
    if roots['base'] == roots['update']:
        ap.error('Base and Update roots must be separate.')
    dest = args.report.resolve()
    if any(dest.is_relative_to(root) for root in roots.values()):
        ap.error('Report must be written outside both source roots.')
    if dest in (args.dataset.resolve(), args.manifest.resolve()):
        ap.error('Report must not overwrite input data.')
    expected_keys = [(m['source_kind'], m['file']) for m in manifest['files']]
    if len(expected_keys) != len(set(expected_keys)) or set(expected_keys) != set(groups):
        ap.error('Manifest coverage mismatch.')
    result = []
    for m in manifest['files']:
        key = (m['source_kind'], m['file'])
        rows = sorted(groups[key], key=lambda x: x['pool_offset'])
        root = roots[key[0]]
        path = (root / key[1]).resolve()
        if not path.is_relative_to(root):
            check = {'status': 'path_outside_root'}
        elif any(row['file_sha256'] != m['file_sha256'] for row in rows):
            check = {'status': 'manifest_file_hash_mismatch'}
        else:
            check = inspect_source(path, m, rows)
        result.append({'source_kind': key[0], 'file': key[1], 'expected_sha256': m['file_sha256'], **check})
    counts = dict(Counter(x['status'] for x in result))
    matched = counts.get('source_match_exact_pool', 0) + counts.get('source_match_extra_pool', 0)
    summary = {'dataset_sha256': manifest['dataset_sha256'], 'expected_files': len(result),
               'matched_source_files': matched, 'status_counts': counts,
               'all_exact_pool_matches': counts.get('source_match_exact_pool', 0) == len(result),
               'importer_ready': False, 'runtime_verified': False,
               'note': 'Source checks only. No CFG node grammar, references, font or ARC0 validated.',
               'files': result}
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k!='files'}, ensure_ascii=False, indent=2))
    print('Report:', dest)
    return 0 if matched == len(result) and summary['all_exact_pool_matches'] else 2

if __name__ == '__main__':
    raise SystemExit(main())
