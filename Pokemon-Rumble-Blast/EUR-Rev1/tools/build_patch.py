#!/usr/bin/env python3
"""Conservative MSBT → LZH8 RomFS patch builder for Super Pokémon Rumble EUR Rev1.

Works only from the user's own EXTRACTED original EU_English .msbt files.
Never touches the source files, never builds/patches CIA, and leaves font binaries alone.

Usage:
 python build_patch.py --source-msbt-dir /path/to/EU_English \
   --translations /path/to/CP011_TONG_HOP_1932.jsonl --output /path/to/out

Safety gates:
 - exact source MSBT file hashes locked in manifest
 - every translation belongs to an existing valid original MSBT message
 - UTF-16LE NFC and reserved token encoding
 - original label/attributes/other sections preserved byte-for-byte
 - unedited TXT2 entries have byte-for-byte identical contents
 - no-change reconstruction exact byte-for-byte for ALL 16 supplied MSBT
 - LZH8 0x40 compression decode round-trip
 - final modified MSBT re-parses to 1932 expected VI strings with same control bytes
"""
import argparse, hashlib, json, re, struct, unicodedata
from pathlib import Path
from collections import Counter, defaultdict

CTRL_RE = re.compile(r'\{CTRL:([0-9a-fA-F]+)\}')
PREFIX = 'EUR-REV1::/msg/EU_English/'
SOURCE_CIA_SHA256 = 'a3fcd6521841bf7f8d0a5cd30103e4d9b36212cbf3f97b5ac9d514e139ffe30f'


def sha(data): return hashlib.sha256(data).hexdigest()

def encode_lzh8_literal(raw):
    """Simple 0x40 LZH8 encoder with balanced, 8-bit, literal-only Huffman tree.
    Not size-optimal; valid format, but game-runtime compatibility needs testing.
    9-bit tree: pair-relative child pointers and left/right leaf bits.
    """
    if not 0 < len(raw) < (1 << 24): raise ValueError('0x40 size must fit 24-bit header')
    def pack_bits(values):
        acc = bits = 0; out = bytearray()
        for value, width in values:
            assert value >= 0 and value < (1 << width)
            acc = (acc << width) | value; bits += width
            while bits >= 8:
                bits -= 8; out.append((acc >> bits) & 255); acc &= (1 << bits) - 1
        if bits: out.append(acc << (8 - bits))
        return bytes(out)
    nodes = []
    for i in range(1, 513):
        if i >= 256: val = i - 256 if i < 512 else 0
        else:
            dist = (2 * i - (i & ~1)) // 2 - 1
            assert 0 <= dist <= 127
            val = dist | (0x180 if i >= 128 else 0)
        nodes.append((val, 9))
    tree_bits = pack_bits(nodes)
    block_len = ((2 + len(tree_bits) + 3) // 4) * 4
    table = struct.pack('<H', block_len // 4 - 1) + tree_bits
    table += bytes(block_len - len(table))
    distance_tree = b'\x00' + pack_bits([(0, 5)] * 4)
    assert len(distance_tree) == 4
    return b'\x40' + len(raw).to_bytes(3, 'little') + table + distance_tree + raw


class Bits:
    def __init__(self, data, pos=0): self.data=data;self.pos=pos
    def get(self, n):
        end=self.pos+n
        if end>len(self.data)*8:raise ValueError('Truncated LZH8 stream')
        a=self.pos//8; b=(end+7)//8
        result=(int.from_bytes(self.data[a:b],'big')>>(b*8-end))&((1<<n)-1)
        self.pos=end;return result


def decode_lzh8(data):
    if data[:1] != b'\x40':raise ValueError('Expected LZH8 0x40')
    size=int.from_bytes(data[1:4],'little'); start=4
    if not size: size=struct.unpack_from('<I',data,4)[0];start=8
    block=(struct.unpack_from('<H',data,start)[0]+1)*4
    stop=(start+block)*8;bits=Bits(data,start*8+16)
    tree=[0]*1024; i=1
    while bits.pos<stop-8 and i<len(tree):tree[i]=bits.get(9);i+=1
    bits.pos=stop
    start=bits.pos;block=(bits.get(8)+1)*4;stop=start+block*8
    dt=[0]*64;i=1
    while bits.pos<stop and i<len(dt):dt[i]=bits.get(5);i+=1
    bits.pos=stop
    def symbol(table, width):
        pos=1;mask=(1<<(width-2))-1
        for _ in range(len(table)):
            side=bits.get(1);node=table[pos]
            ch=(pos&~1)+((node&mask)+1)*2+side
            if ch>=len(table):raise ValueError('LZH8 bad Huffman tree')
            if node&((1<<(width-1))>>side):return table[ch]
            if ch==pos:raise ValueError('LZH8 tree cycle')
            pos=ch
        raise ValueError('LZH8 excessive tree depth')
    out=bytearray()
    while len(out)<size:
        sym=symbol(tree,9)
        if sym<256:out.append(sym);continue
        length=(sym&255)+3; sym2=symbol(dt,5)
        distance=1 if sym2==0 else (1<<(sym2-1))+bits.get(sym2-1)+1
        if distance>len(out) or len(out)+length>size:raise ValueError('Bad LZH8 reference')
        pattern=out[-distance:];out.extend((pattern*((length+distance-1)//distance))[:length])
    return bytes(out)


def parse_msbt(data):
    if data[:10]!=b'MsgStdBn\xff\xfe' or data[12]!=1:
        raise ValueError('Not little-endian, UTF16 MSBT')
    if struct.unpack_from('<I',data,18)[0]!=len(data):raise ValueError('MSBT size mismatch')
    count_sections=struct.unpack_from('<H',data,14)[0]
    pos=32; sections=[]
    for _ in range(count_sections):
        tag=data[pos:pos+4].decode('ascii')
        size=struct.unpack_from('<I',data,pos+4)[0]
        end=pos+16+size; aligned=(end+15)&~15
        if aligned>len(data):raise ValueError('Invalid MSBT section length')
        sections.append({'tag':tag,'header':data[pos:pos+16],
                         'payload':data[pos+16:end], 'pad':data[end:aligned]})
        pos=aligned
    if pos != len(data):raise ValueError('Unexpected MSBT trailer')
    txt_sections=[s for s in sections if s['tag']=='TXT2']
    if len(txt_sections)!=1:raise ValueError('MSBT must have exactly one TXT2')
    txt=txt_sections[0]['payload'];num=struct.unpack_from('<I',txt)[0]
    offs=struct.unpack_from('<'+'I'*num,txt,4)
    if not all(offs[i]<=offs[i+1] for i in range(num-1)):raise ValueError('TXT2 offsets not sorted')
    if offs[0] != 4+4*num:raise ValueError('TXT2 unexpected first offset')
    raws=[txt[start:(offs[i+1] if i+1<num else len(txt))] for i,start in enumerate(offs)]
    if len(raws)!=num:raise ValueError('Wrong TXT2 count')
    return sections, raws


def decode_text(raw):
    out=[];pos=0;controls=[];term_pos=None
    while pos+2 <=len(raw):
        cp=int.from_bytes(raw[pos:pos+2],'little')
        if cp==0:term_pos=pos;break
        if cp in (14,15):
            start=pos
            if pos+6>len(raw):raise ValueError('Truncated control header')
            pos+=6
            if cp==14:
                if pos+2>len(raw):raise ValueError('Truncated control params length')
                size=int.from_bytes(raw[pos:pos+2],'little');pos+=2+size
            if pos>len(raw):raise ValueError('Control overrun')
            he=raw[start:pos].hex();controls.append(he);out.append('{CTRL:'+he+'}')
        else:
            out.append(raw[pos:pos+2].decode('utf-16le',errors='strict'))
            pos+=2
    if term_pos is None:raise ValueError('Unterminated MSBT string')
    if any(c!=0 for c in raw[term_pos:]):raise ValueError('Unexpected non-zero string tail')
    return ''.join(out),controls


def encode_text(vi):
    if vi != unicodedata.normalize('NFC',vi):raise ValueError('Translation not NFC')
    chunks=[];pos=0
    for m in CTRL_RE.finditer(vi):
        chunks.append(vi[pos:m.start()].encode('utf-16le'))
        val=bytes.fromhex(m.group(1))
        if len(val)<6 or val[:2] not in (b'\x0e\x00',b'\x0f\x00'):
            raise ValueError('Malformed control '+m.group(0))
        if val[:2]==b'\x0e\x00':
            if len(val)<8 or len(val)!=8+int.from_bytes(val[6:8],'little'):
                raise ValueError('Malformed 0x0e control')
        if val[:2]==b'\x0f\x00' and len(val)!=6:raise ValueError('Malformed 0x0f control')
        chunks.append(val);pos=m.end()
    rem=vi[pos:]
    chunks.append(rem.encode('utf-16le'))
    if '\x00' in vi or '\x0e' in vi or '\x0f' in vi:
        raise ValueError('Reserved raw characters in translation')
    return b''.join(chunks)+b'\x00\x00'


def rebuild(source, replacements):
    sections,raws=parse_msbt(source)
    if any(i<0 or i>=len(raws) for i in replacements):raise ValueError('Replacement out of bounds')
    raw_out=[];changed=0
    for i, raw in enumerate(raws):
        if i not in replacements:
            raw_out.append(raw);continue
        original,controls=decode_text(raw)
        vi=replacements[i]
        if original==vi:raw_out.append(raw);continue
        expected_controls=CTRL_RE.findall(original)
        actual_controls=CTRL_RE.findall(vi)
        if expected_controls!=actual_controls:
            raise ValueError(f'Token mismatch at #{i:05d}: {expected_controls} != {actual_controls}')
        raw_out.append(encode_text(vi));changed+=1
    count=len(raw_out)
    offsets=[];payload=bytearray(4+4*count)
    struct.pack_into('<I',payload,0,count)
    for i, raw in enumerate(raw_out):
        offsets.append(len(payload));struct.pack_into('<I',payload,4+i*4,len(payload));payload+=raw
    out=bytearray(source[:32]); out_sections=[]
    for sec in sections:
        if sec['tag']=='TXT2':
            pl=bytes(payload)
        else: pl=sec['payload']
        hdr=bytearray(sec['header']);struct.pack_into('<I',hdr,4,len(pl))
        out_sections.append((sec['tag'],pl))
        out+=hdr+pl
        pad_len=(-len(out))%16
        if pl==sec['payload'] and len(sec['pad'])==pad_len:out+=sec['pad']
        else:out+=bytes([0xab])*pad_len
    struct.pack_into('<I',out,18,len(out))
    return bytes(out),changed,out_sections


def build(src_dir,trans_path,out_dir):
    if not src_dir.is_dir():raise ValueError('Missing original .msbt directory')
    all_rows=[json.loads(line) for line in trans_path.open(encoding='utf-8') if line.strip()]
    if len(all_rows)!=1932:raise ValueError(f'Expected 1932 CP011 rows, got {len(all_rows)}')
    seen=set(); grouped=defaultdict(dict)
    for row in all_rows:
        rid=row['id'];vi=row['vi'];m=re.fullmatch(re.escape(PREFIX)+r'([A-Za-z_0-9]+\.msbt)\.cx#(\d{5})',rid)
        if not m:raise ValueError('Invalid translation ID: '+rid)
        if rid in seen:raise ValueError('Duplicate ID '+rid)
        seen.add(rid);file=m.group(1);index=int(m.group(2));grouped[file][index]=vi
    found=set(f.name for f in src_dir.glob('*.msbt'))
    if len(found)!=16:raise ValueError('Expected 16 native MSBT source files, got '+str(len(found)))
    if not set(grouped).issubset(found):raise ValueError('Source missing MSBT file(s)')
    report={'source_cia_sha256_reference':SOURCE_CIA_SHA256,'status':'binary-built-not-game-tested',
            'translation_count':len(all_rows),'patched_msbt':[],'no_change_smoke':[],
            'font_status':'BLOCKED: original BCFNT assets not present in handover ZIP',
            'test_status':'NOT TESTED in a 3DS game runtime'}
    dst=out_dir/'romfs/msg/EU_English';dst.mkdir(parents=True,exist_ok=True)
    for source_file in sorted(src_dir.glob('*.msbt')):
        name=source_file.name;original=source_file.read_bytes()
        _,orig_strings=parse_msbt(original)
        # Enforce structural no-change round-trip across all 16 original files.
        same,ch,sects=rebuild(original,{})
        if same!=original:raise ValueError(name+': no-change rebuild NOT byte-identical')
        cx0=encode_lzh8_literal(same)
        if decode_lzh8(cx0)!=original:raise ValueError(name+': LZH8 no-change round-trip failed')
        report['no_change_smoke'].append({'file':name,'msbt_bytes':len(original),'sha256':sha(original),'PASS':True})
        if name not in grouped:continue
        # Verify CP011 record keys map to actual UTF16 TXT2 source records.
        repl=grouped[name]
        if any(i>=len(orig_strings) for i in repl):raise ValueError(name+' has out-of-range record id')
        updated,changed,new_sections=rebuild(original,repl)
        osec, old_raw=parse_msbt(original)
        nsec,new_raw=parse_msbt(updated)
        if len(old_raw)!=len(new_raw):raise ValueError('Message count changed')
        if len(osec)!=len(nsec):raise ValueError('Section count changed')
        for old,new in zip(osec,nsec):
            if old['tag']!=new['tag']:raise ValueError('Section order changed')
            if old['tag']!='TXT2' and old['payload']!=new['payload']:
                raise ValueError('Nontext section changed unexpectedly')
        for i,r in enumerate(new_raw):
            tx,ct=decode_text(r)
            old_tx,old_ct=decode_text(old_raw[i])
            if old_ct!=ct:raise ValueError(name+f': CTRL changed in row {i}')
            if i in repl:
                if tx!=repl[i]:raise ValueError(name+f': text failed to encode at {i}')
            elif r!=old_raw[i]:raise ValueError(name+f': untouched original bytes changed at {i}')
        cx=encode_lzh8_literal(updated)
        if decode_lzh8(cx)!=updated:raise ValueError(name+': generated LZH8 fails roundtrip')
        (dst/(name+'.cx')).write_bytes(cx)
        report['patched_msbt'].append({'file':name,'romfs_path':'/msg/EU_English/'+name+'.cx',
            'candidate_count':len(repl),'actually_changed':changed,'original_bytes':len(original),
            'updated_bytes':len(updated),'cx_bytes':len(cx),
            'msbt_original_sha256':sha(original),'msbt_updated_sha256':sha(updated),
            'cx_sha256':sha(cx),'msbt_structural_QA':True,'lzh8_decode_QA':True})
    if sum(r['candidate_count'] for r in report['patched_msbt'])!=1932:raise ValueError('Not all translations built')
    report['patched_count']=len(report['patched_msbt'])
    (out_dir/'QA_CP012.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return report


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-msbt-dir',required=True,type=Path)
    ap.add_argument('--translations',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args()
    print(json.dumps(build(a.source_msbt_dir,a.translations,a.output),ensure_ascii=False,indent=2))

if __name__=='__main__': main()