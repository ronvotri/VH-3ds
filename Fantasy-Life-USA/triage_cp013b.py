#!/usr/bin/env python3
"""Prepare an ID-precise Fantasy Life CP013b review queue. No auto-translation.
Usage: python3 triage_cp013b.py /path/to/original-handover.zip
Run from Fantasy-Life-USA, or pass --repo-dir to that folder.
"""
import argparse
import base64
import bz2
from collections import Counter
import csv
import gzip
import json
from pathlib import Path
import re
import unicodedata
from zipfile import ZipFile

FIELDS = ('source', 'source_en', 'english', 'en', 'original', 'text_en', 'text')
CTRL = re.compile(r'\{CTRL:[0-9a-fA-F]+\}')

def read_translation_ids(directory):
    ids = set()
    for path in sorted(directory.glob('*.b64')):
        if '.jsonl.' not in path.name:
            continue
        packed = base64.b64decode(path.read_text(encoding='ascii').strip(), validate=True)
        if path.name.endswith('.bz2.b64'):
            data = bz2.decompress(packed)
        elif path.name.endswith('.gz.b64'):
            data = gzip.decompress(packed)
        else:
            continue
        for number, line in enumerate(data.decode('utf-8-sig').splitlines(), 1):
            if not line.strip():
                continue
            row = json.loads(line)
            identifier = row['id']
            if identifier in ids:
                raise ValueError(f'Duplicate translation ID: {identifier} in {path.name}:{number}')
            if not row.get('vi') or unicodedata.normalize('NFC', row['vi']) != row['vi']:
                raise ValueError(f'Empty or non-NFC translation: {identifier}')
            ids.add(identifier)
    return ids

def english_text(row):
    for key in FIELDS:
        val = row.get(key)
        if isinstance(val, str) and val.strip():
            return val
        if isinstance(val, dict):
            for nested in ('en', 'english', 'text', 'value', 'source'):
                if isinstance(val.get(nested), str) and val[nested].strip():
                    return val[nested]
    return ''

def review_class(source):
    s = CTRL.sub('', source).strip()
    if not s:
        return 'NEEDS_SOURCE_CONTEXT'
    if re.search(r'\b(debug|test|dummy|sound|bgm|asset|texture|filename)\b', s, re.I):
        return 'HOLD_INTERNAL_REVIEW'
    if len(s) <= 42 and s.replace(' ', '').isalpha() and s.istitle():
        return 'REVIEW_NAME_OR_TERM'
    if len(s.split()) >= 5 and (re.search(r'[.!?]', s) or any(word in s.lower() for word in ('you ', 'your ', 'can ', 'please ', 'not ', 'when ', 'after ', 'before '))):
        return 'HIGH_CONTENT_REVIEW'
    return 'REVIEW_MIXED'

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source_zip', type=Path)
    p.add_argument('--repo-dir', type=Path, default=Path(__file__).resolve().parent)
    p.add_argument('--output-dir', type=Path, default=Path('CP013b-review'))
    a = p.parse_args()
    translated = read_translation_ids(a.repo_dir / 'translations')
    if not translated:
        raise RuntimeError('No translation batches found')
    with ZipFile(a.source_zip) as archive:
        matches = [n for n in archive.namelist() if n.replace('\\', '/').split('/')[-1] == '01_CAN_DICH.jsonl']
        if len(matches) != 1:
            raise RuntimeError(f'Expected one 01_CAN_DICH.jsonl, found {len(matches)}')
        sources = [json.loads(line) for line in archive.read(matches[0]).decode('utf-8-sig').splitlines() if line.strip()]
    source_ids = [row.get('id') for row in sources]
    if any(not isinstance(x, str) or not x for x in source_ids) or len(set(source_ids)) != len(source_ids):
        raise RuntimeError('Invalid source IDs')
    missing = translated.difference(source_ids)
    if missing:
        raise RuntimeError(f'{len(missing)} translated IDs do not match the handover source')
    rows = []
    for source_row in sources:
        identifier = source_row['id']
        if identifier in translated:
            continue
        en = english_text(source_row)
        rows.append({
            'id': identifier,
            'source_text': en,
            'group_hint': str(source_row.get('package', source_row.get('group', source_row.get('category', '')))),
            'review_class': review_class(en),
            'translation_status': 'PENDING_HUMAN_REVIEW'
        })
    a.output_dir.mkdir(parents=True, exist_ok=True)
    with (a.output_dir / 'CP013b-remaining-source-review.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id','source_text','group_hint','review_class','translation_status'])
        w.writeheader()
        w.writerows(rows)
    summary = {
        'source_total': len(sources),
        'translated_ids': len(translated),
        'remaining': len(rows),
        'review_classes': dict(Counter(r['review_class'] for r in rows)),
        'warning': 'Review queue only; not a new translation or a playable 3DS patch.'
    }
    (a.output_dir / 'CP013b-source-review-summary.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
