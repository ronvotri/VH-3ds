#!/usr/bin/env python3
"""Apply the six RC1a text corrections to verified RC1 data, never a ROM."""
import argparse, base64, bz2, hashlib, json
from pathlib import Path
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(m): return b''.join((json.dumps({'id':i,'vi':m[i]},ensure_ascii=False,separators=(',',':'))+'\n').encode() for i in sorted(m))
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('rc1',type=Path)
    p.add_argument('out',type=Path)
    a=p.parse_args()
    rows=[json.loads(l) for l in a.rc1.read_text(encoding='utf-8-sig').splitlines() if l.strip()]
    m={r['id']:r['vi'] for r in rows}
    if len(rows)!=len(m) or len(m)!=25553 or sha(dump(m))!='44f1730feeb5a9fa00ec3438b8807fa1c3ce8518aca4609d30d63f4438170dce': raise ValueError('Wrong RC1 mapping')
    raw=bz2.decompress(base64.b64decode((Path(__file__).resolve().parent/'reviews/rc1a-corrections.jsonl.bz2.b64').read_bytes()))
    if sha(raw)!='bfabaea511b820bd833f0869a19b9ee86edec03fb60ccd333b2f9982dc594165': raise ValueError('Wrong delta hash')
    edits=[json.loads(l) for l in raw.splitlines() if l.strip()]
    if len(edits)!=6 or len({r['id'] for r in edits})!=6: raise ValueError('Wrong delta count')
    for r in edits:
        if m.get(r['id'])!=r['old_vi']: raise ValueError('Old value mismatch: '+r['id'])
        m[r['id']]=r['vi']
    data=dump(m)
    if sha(data)!='0aa42752f27313f2125480137e203e016e1768ccb786240b6f55d2e158ae76ff': raise ValueError('RC1a hash mismatch')
    if a.out.resolve()==a.rc1.resolve(): raise ValueError('Output must be different from input')
    with a.out.open('xb') as f: f.write(data)
    print('PASS RC1a: 25553 text replacements; no ROM patch')
if __name__=='__main__': main()
