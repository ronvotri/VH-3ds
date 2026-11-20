#!/usr/bin/env python3
"""Self-tests for the EUR Rev1 MSBT/LZH8 patch builder (no 3DS runtime test)."""
import argparse, pathlib, sys, hashlib, json, unicodedata
from build_patch import parse_msbt, rebuild, decode_text, encode_lzh8_literal, decode_lzh8

def main():
 p=argparse.ArgumentParser();p.add_argument('--source-msbt-dir',required=True,type=pathlib.Path);p.add_argument('--patch-root',required=True,type=pathlib.Path);p.add_argument('--translations',required=True,type=pathlib.Path);a=p.parse_args()
 roots=a.patch_root/'romfs/msg/EU_English'; assert roots.is_dir()
 trans={json.loads(s)['id']:json.loads(s)['vi'] for s in a.translations.open(encoding='utf-8') if s.strip()}
 assert len(trans)==1932
 total=0;changed=0
 for src in sorted(a.source_msbt_dir.glob('*.msbt')):
  original=src.read_bytes(); rebuilt,changes,_=rebuild(original,{})
  assert rebuilt==original,src.name+' no-change round-trip failed'
  try:
   from pathlib import Path
   # Use independent LZH8 decompressor supplied with the source handoff where possible.
   sys.path.insert(0,str(a.source_msbt_dir.parent/'references/tools'))
   from lzh8 import decompress
   assert decompress(encode_lzh8_literal(original))==original
  except ModuleNotFoundError:
   assert decode_lzh8(encode_lzh8_literal(original))==original
  binary=roots/(src.name+'.cx')
  if not binary.exists():continue
  uncomp=decode_lzh8(binary.read_bytes());s0,r0=parse_msbt(original);s1,r1=parse_msbt(uncomp)
  assert len(s0)==len(s1)
  for v0,v1 in zip(s0,s1):
   assert v0['tag']==v1['tag']
   if v0['tag']!='TXT2': assert v0['payload']==v1['payload']
  for i,(old,new) in enumerate(zip(r0,r1)):
   rid=f'EUR-REV1::/msg/EU_English/{src.name}.cx#{i:05d}'
   oldtext,oldcontrol=decode_text(old);newtext,newcontrol=decode_text(new)
   assert oldcontrol==newcontrol
   if rid in trans:
    assert newtext==trans[rid],rid
    total+=1
    changed+=(oldtext!=newtext)
   else:assert old==new, rid+' untouched raw entry changed'
  assert decode_lzh8(binary.read_bytes())==uncomp
 assert total==1932,(total,changed)
 # Explicit negative cases: wrong CTRL and non-NFC MUST fail.
 original=next(a.source_msbt_dir.glob('kaiwa.msbt')).read_bytes()
 atext=decode_text(parse_msbt(original)[1][0])[0]
 try: rebuild(original,{0:atext.replace('{CTRL:0e00000004000000}','')})
 except ValueError: pass
 else:raise AssertionError('Control-corrupting translation accepted!')
 try: rebuild(original,{0:'a\u0300'})
 except ValueError: pass
 else:raise AssertionError('Non-NFC translation accepted!')
 print(json.dumps({'verified_source_files':len(list(a.source_msbt_dir.glob('*.msbt'))),'verified_translation_ids':total,'actually_changed_strings':changed,'original_txt2_unedited_entries':'byte identical','LBL1_ATR1':'byte identical','lzh8_roundtrip':True,'malformed_controls_rejected':True,'non_nfc_rejected':True,'game_runtime':'UNTESTED'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()