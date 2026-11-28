#!/usr/bin/env python3
"""Reassemble the exact QA049 ZIP; do not modify game files."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
NAME = 'SnackWorld_QA049_INTEGRATION_READY.zip'
SIZE = 6368493
SHA256 = 'f92f1d705e2251453984cdfe941c0b1c8a64f57cc5b5114c61663d1a86c521d0'
DATASET_SHA256 = '77c11605dc8e6b8b2b452892652afdc38a2b215ba7620acce44c07d98e191809'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / NAME)
    args = parser.parse_args()
    blocks = []
    for i in range(1, 18):
        p = ROOT / 'parts' / f'qa049.zip.part{i:02d}'
        try:
            block = p.read_bytes()
        except OSError as exc:
            parser.error(str(exc))
        if len(block) != (224493 if i == 17 else 384000):
            parser.error(f'Incorrect size: {p.name}')
        blocks.append(block)
    blob = b''.join(blocks)
    if len(blob) != SIZE or hashlib.sha256(blob).hexdigest() != SHA256:
        parser.error('Combined ZIP SHA-256 mismatch; no output written.')
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        if archive.testzip() is not None:
            parser.error('ZIP CRC verification failed.')
        dataset = archive.read('QA049_FULL_32067.jsonl')
        if hashlib.sha256(dataset).hexdigest() != DATASET_SHA256:
            parser.error('Dataset SHA-256 mismatch.')
        rows = [json.loads(line) for line in dataset.splitlines()]
        if len(rows) != 32067 or len({r['id'] for r in rows}) != 32067:
            parser.error('Dataset ID verification failed.')
    try:
        with args.output.open('xb') as f:
            f.write(blob)
    except OSError as exc:
        parser.error(str(exc))
    print(f'Verified {args.output}: {SIZE} bytes, 32067 unique IDs, SHA-256 {SHA256}')

if __name__ == '__main__':
    main()
