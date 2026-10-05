"""Extract the full content of the original SIP docx into JSON for restructuring.

Produces _work/sip_content.json  -> non-empty content blocks (paragraph/table)
         _work/sip_raw.json      -> raw OOXML of every body child, so that the
                                    front matter (title page, certificate with
                                    its full-page image, declaration, etc.) can
                                    be copied across byte-for-byte.
"""
import json, re, sys
from lxml import etree

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = NS['w']

SRC = sys.argv[1] if len(sys.argv) > 1 else 'SIP - M16158 NIkhil Singh.docx'

import zipfile
with zipfile.ZipFile(SRC) as z:
    xml = z.read('word/document.xml')

root = etree.fromstring(xml)
body = root.find('{%s}body' % W)

content, raw = [], []


def cell_text(tc):
    return '\n'.join(''.join(t.text or '' for t in p.iter('{%s}t' % W))
                     for p in tc.findall('{%s}p' % W))


for child in body:
    tag = etree.QName(child).localname
    if tag == 'sectPr':
        raw.append({'kind': 'sectPr', 'xml': etree.tostring(child, encoding='unicode')})
        continue
    blob = etree.tostring(child, encoding='unicode')
    entry = {'kind': tag, 'xml': blob, 'ci': None}
    if tag == 'p':
        text = ''.join(t.text or '' for t in child.iter('{%s}t' % W))
        m = re.search(r'r:embed="(rId\d+)"', blob)
        rid = m.group(1) if m else None
        if text.strip() or rid:
            # style
            ps = child.find('{%s}pPr/{%s}pStyle' % (W, W))
            style = ps.get('{%s}val' % W) if ps is not None else 'Normal'
            jc = child.find('{%s}pPr/{%s}jc' % (W, W))
            al = jc.get('{%s}val' % W) if jc is not None else None
            runs = []
            for r in child.findall('{%s}r' % W):
                rt = ''.join(t.text or '' for t in r.iter('{%s}t' % W))
                if not rt:
                    continue
                rpr = r.find('{%s}rPr' % W)
                sz = None
                bold = ital = False
                if rpr is not None:
                    szel = rpr.find('{%s}sz' % W)
                    if szel is not None:
                        sz = int(szel.get('{%s}val' % W)) / 2.0
                    bold = rpr.find('{%s}b' % W) is not None
                    ital = rpr.find('{%s}i' % W) is not None
                runs.append({'t': rt, 'b': bold, 'i': ital, 'sz': sz})
            entry['ci'] = len(content)
            content.append({'k': 'p', 'style': style, 'al': al, 'img': rid,
                            'text': text, 'runs': runs})
    elif tag == 'tbl':
        rows = []
        for tr in child.findall('{%s}tr' % W):
            rows.append([cell_text(tc) for tc in tr.findall('{%s}tc' % W)])
        widths = []
        grid = child.find('{%s}tblGrid' % W)
        if grid is not None:
            widths = [int(g.get('{%s}w' % W)) for g in grid.findall('{%s}gridCol' % W)]
        entry['ci'] = len(content)
        content.append({'k': 't', 'rows': rows, 'w': widths})
    raw.append(entry)

json.dump(content, open('_work/sip_content.json', 'w'), indent=0, ensure_ascii=False)
json.dump(raw, open('_work/sip_raw.json', 'w'), ensure_ascii=False)
print('content blocks', len(content), '| raw body children', len(raw),
      '| tables', sum(1 for i in content if i['k'] == 't'))
