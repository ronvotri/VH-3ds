#!/usr/bin/env python3
"""Restore text-only RC1 after CP014n. Never modifies ROM files."""
import argparse, base64, bz2, hashlib, json, runpy, unicodedata, re
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dump(rows):
    return b''.join((json.dumps(r, ensure_ascii=False, separators=(',', ':'))+'\n').encode() for r in rows)


def parse(data):
    rows = [json.loads(line) for line in data.splitlines() if line.strip()]
    by_id = {r['id']: r for r in rows}
    require(len(by_id) == len(rows), 'Duplicate ID')
    return by_id


def ids_hash(ids):
    return sha(('\n'.join(sorted(ids))+'\n').encode())


def verify(m, k, h, expected):
    require(not (set(m)&k or set(m)&set(h) or k&set(h)), 'Overlapping ledgers')
    actual = {
        'replacement_count': len(m), 'keep_count': len(k), 'hold_count': len(h),
        'mapping_sha256': sha(dump({'id': i, 'vi': m[i]['vi']} for i in sorted(m))),
        'keep_ids_sha256': ids_hash(k),
        'hold_sources_sha256': sha(dump({'id': i, 'source': h[i]['source']} for i in sorted(h))),
        'all_ids_sha256': ids_hash(set(m)|k|set(h)),
    }
    require(actual == expected, 'Ledger or digest differs from manifest: '+str(actual))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--base-ready', action='store_true', help='Use verified CP014n fixture and explicit KEEP JSONL instead of running unpack_batches.py')
    ap.add_argument('--out', type=Path, default=None)
    args = ap.parse_args()
    root = args.root.resolve()
    manifest = json.loads((root/'rc1-manifest.json').read_text(encoding='utf-8'))
    base_globals = None if args.base_ready else runpy.run_path(str(root/'unpack_batches.py'))
    m = parse((root/'translations/merged-CP014n-21925.jsonl').read_bytes())
    h = parse((root/'reviews/remaining-HOLD-CP014n-4337.jsonl').read_bytes())
    if args.base_ready:
        k = set(parse((root/'reviews/keep-CP014n-8550.jsonl').read_bytes()))
    else:
        k = set(base_globals['review_ids']) - set(h)
        require(set(base_globals['ids']) == set(m), 'Base unpack ID mismatch')
    verify(m, k, h, manifest['base'])
    for entry in manifest['deltas']:
        enc = (root/entry['path']).read_bytes()
        blob = hashlib.sha1(('blob '+str(len(enc))+'\0').encode()+enc).hexdigest()
        require(blob == entry['git_blob_sha1'], 'Blob mismatch: '+entry['path'])
        data = bz2.decompress(base64.b64decode(enc))
        rows = parse(data)
        require(len(rows) == entry['count'] and sha(data) == entry['sha256'], 'Invalid delta: '+entry['path'])
        for i, r in rows.items():
            if entry['kind'] == 'legacy-corrections':
                require(i in m and m[i]['vi'] == r['old_vi'], 'Correction precondition failed: '+i)
                m[i] = {'id': i, 'vi': r['vi']}
            else:
                require(i in h and i not in m and i not in k and h[i]['source'] == r['source'], 'Resolution precondition failed: '+i)
                if r['decision'] == 'TRANSLATE':
                    m[i] = {'id': i, 'vi': r['vi']}
                else:
                    require(r['decision'] in ('KEEP_SOURCE_NAME', 'KEEP_FORMAT_LITERAL'), 'Unknown decision: '+i)
                    k.add(i)
                del h[i]
    verify(m, k, h, manifest['final'])
    require(all(r['vi'] and unicodedata.normalize('NFC', r['vi']) == r['vi'] for r in m.values()), 'Empty or non-NFC replacement')
    out = args.out or root/'rc1-output'
    out.mkdir(parents=True, exist_ok=True)
    (out/'merged-RC1-25553.jsonl').write_bytes(dump(m[i] for i in sorted(m)))
    (out/'keep-ids-RC1-8629.txt').write_text('\n'.join(sorted(k))+'\n', encoding='utf-8')
    (out/'remaining-HOLD-RC1-630.jsonl').write_bytes(dump(dict(h[i], decision='DEFER_SOURCE_FALLBACK') for i in sorted(h)))
    (out/'source-ID-ledger-RC1.jsonl').write_bytes(dump({'id': i, 'status': 'REPLACE' if i in m else 'KEEP' if i in k else 'DEFER_SOURCE_FALLBACK'} for i in sorted(set(m)|k|set(h))))
    print('PASS: RC1 25553 replacements, 8629 KEEP, 630 deferred. Text only; not a ROM patch.')


if __name__ == '__main__':
    main()
