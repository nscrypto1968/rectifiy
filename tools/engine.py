"""Document-assembly engine: numbering, cross-reference repair, re-use of the
original blocks, index/TOC collection and final .docx packaging."""

import json, re, shutil, zipfile, os
from lxml import etree
import docxkit as K

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

CONTENT = json.load(open('_work/sip_content.json'))
RAW = json.load(open('_work/sip_raw.json'))

# raw-block index for every content item
CI2RAW = {b['ci']: i for i, b in enumerate(RAW) if b.get('ci') is not None}

# --------------------------------------------------------------------------
# cross-reference repair: the original numbering (30 chapters, appendices in
# the middle) no longer exists after the restructure.
# --------------------------------------------------------------------------
FIXES = [
    ('EIC-based company and business analysis (Chapter 20)',
     'EIC-based company and business analysis (Chapter 2)'),
    ('where I worked as a Dealer and as an Analyst (see Chapter 20)',
     'where I worked as a Dealer and as an Analyst (see Chapter 2)'),
    ('EIC, company and business analysis (see Chapter 20)',
     'EIC, company and business analysis (see Chapter 2)'),
    ('Rosy Blue Securities Pvt. Ltd. (Chapter 20)',
     'Rosy Blue Securities Pvt. Ltd. (Chapter 2)'),
    ('ratings in Chapter 6 are', 'ratings in Section 3.9 are'),
    ('Formulas appear in Appendix B.', 'Formulas appear in Annexure B.'),
    ('see Appendix B.', 'see Annexure B.'),
    ('The valuation ratios in Chapter 13 use',
     'The valuation ratios in Sections 5.24 to 5.28 use'),
    ('Chapters 3 and 6 (industry context, PESTLE).',
     'Chapter 3 (industry context, PESTLE, Sections 3.2 to 3.10).'),
    ('Chapters 3 and 6 (industry structure, Porter’s Five Forces).',
     'Chapter 3 (industry structure and Porter’s Five Forces).'),
    ('Chapters 4, 5 and 8 to 13.', 'Chapters 4 and 5.'),
    ('supports the listed-market snapshot in Chapter 14.',
     'supports the listed-market snapshot in Section 5.29.'),
    ('introduced in this supplement', 'introduced in this section'),
    ('The existing report’s dated 1 October 2026 snapshot',
     'The dated 1 October 2026 snapshot in Section 5.25'),
    ('the simple P/S proxy in the main report is about 6.83×',
     'the simple P/S proxy calculated in Section 5.25 is about 6.83×'),
    ('Other ratios in the main report also need caveats.',
     'The ratios presented earlier in this chapter also need caveats.'),
    ('approximate paid-up shares stated in the main report',
     'approximate paid-up shares stated in Section 5.25'),
]


# fixes applied to the byte-for-byte front-matter blocks (safe: each target
# string sits inside a single contiguous <w:t> run in the original XML)
RAW_FIXES = [
    ('EIC-based company and business analysis (Chapter 20).',
     'EIC-based company and business analysis (Chapter 2).'),
]


def rawfix(xml):
    for a, b in RAW_FIXES:
        xml = xml.replace(a, b)
    return xml


def fix(text):
    for a, b in FIXES:
        if a in text:
            text = text.replace(a, b)
    return text


# --------------------------------------------------------------------------
# document state
# --------------------------------------------------------------------------
class Doc:
    def __init__(self):
        self.out = []
        self.ch = 0
        self.tn = 0
        self.fn = 0
        self.annex = None         # e.g. 'A' while inside an annexure
        self.tables = []          # (label, title)
        self.figures = []         # (label, title)
        self.toc = []             # dicts for the index table
        self.used = set()
        self._bk = 0

    def _newbk(self):
        self._bk += 1
        return '_Rpt%d' % self._bk

    # -- raw passthrough ---------------------------------------------------
    def raw(self, a, b):
        for i in range(a, b + 1):
            self.out.append(rawfix(RAW[i]['xml']))

    def add(self, xml):
        self.out.append(xml)

    # -- structure ---------------------------------------------------------
    def chapter(self, n, title, strap=None, roman=None):
        self.ch = n
        self.tn = 0
        self.fn = 0
        self.annex = None
        bk = self._newbk()
        self.add(K.with_bookmark(K.chapter('CHAPTER %d' % n), bk))
        self.add(K.h1(title))
        if strap:
            self.add(K.subtitle(strap))
        self.toc.append({'chap': 'Chapter %d' % n, 'no': '', 'title': title.upper(),
                         'lvl': 0, 'bk': bk})

    def part(self, title, strap=None, chap_label=''):
        """Un-numbered front/back-matter heading (References, Annexures...)."""
        self.tn = 0
        self.fn = 0
        bk = self._newbk()
        self.add(K.with_bookmark(K.h1(title, page_break=True), bk))
        if strap:
            self.add(K.subtitle(strap))
        self.toc.append({'chap': chap_label, 'no': '', 'title': title.upper(),
                         'lvl': 0, 'bk': bk})

    def annexure(self, letter, title):
        self.annex = letter
        self.tn = 0
        self.fn = 0
        bk = self._newbk()
        self.add(K.with_bookmark(K.chapter('ANNEXURE %s' % letter), bk))
        self.add(K.h1(title))
        self.toc.append({'chap': 'Annexure %s' % letter, 'no': '',
                         'title': title.upper(), 'lvl': 0, 'bk': bk})

    def sec(self, no, title, toc=True):
        bk = self._newbk()
        self.add(K.with_bookmark(K.h2('%s %s' % (no, title)), bk))
        if toc:
            self.toc.append({'chap': '', 'no': no, 'title': title, 'lvl': 1,
                             'bk': bk})

    def sub(self, title):
        self.add(K.h3(title))

    # -- content -----------------------------------------------------------
    def p(self, *texts):
        for t in texts:
            self.add(K.para(fix(t)))

    def plain(self, text, **kw):
        self.add(K.para(fix(text), **kw))

    def b(self, items, bold=False):
        for t in items:
            self.add(K.bullet(fix(t), bold=bold))

    def n(self, items):
        for t in items:
            self.add(K.number(fix(t)))

    def src(self, text):
        self.add(K.source(fix(text)))

    def ip(self, text, label='Interpretation'):
        self.add(K.interp(fix(text), label))

    # -- numbered captions -------------------------------------------------
    def _tlabel(self):
        self.tn += 1
        if self.annex:
            return 'Table %s.%d' % (self.annex, self.tn)
        return 'Table %d.%d' % (self.ch, self.tn)

    def _flabel(self):
        self.fn += 1
        return 'Figure %d.%d' % (self.ch, self.fn)

    def cap(self, title):
        lab = self._tlabel()
        bk = self._newbk()
        self.tables.append((lab, title, bk))
        self.add(K.with_bookmark(K.caption('%s. %s' % (lab, fix(title))), bk))
        return lab

    def tbl(self, rows, widths=None, header=True, first_col_left=True):
        rows = [[fix(str(c)) for c in r] for r in rows]
        self.add(K.table(rows, widths=widths, header=header,
                         first_col_left=first_col_left))

    def fig(self, rid, cx, cy, title, note=None, pic_id=1):
        lab = self._flabel()
        bk = self._newbk()
        self.figures.append((lab, title, bk))
        self.add(K.figure(rid, cx, cy, pic_id))
        self.add(K.with_bookmark(K.figcaption('%s. %s' % (lab, fix(title))), bk))
        if note:
            self.add(K.fignote(fix(note)))

    # -- re-use of original blocks ----------------------------------------
    def o(self, a, b=None):
        """Render original content items, auto-detecting their role.
        ``o(i)`` renders one item, ``o(a, b)`` renders the inclusive range.
        Headings and chapter banners from the old structure are dropped -
        the new structure supplies its own."""
        if b is None:
            self._one(a)
        else:
            for i in range(a, b + 1):
                self._one(i)

    def oo(self, a, b, skip=()):
        for i in range(a, b + 1):
            if i in skip:
                continue
            self._one(i)

    def _one(self, i):
        it = CONTENT[i]
        self.used.add(i)
        if it['k'] == 't':
            rows = [[fix(c) for c in r] for r in it['rows']]
            self.add(K.table(rows, widths=it.get('w') or None))
            return
        style = it['style']
        text = fix(it['text'].strip())
        runs = it['runs']
        sz = runs[0]['sz'] if runs else None
        bold = runs[0]['b'] if runs else False
        ital = runs[0]['i'] if runs else False
        if it['img']:
            return  # figures are placed explicitly via .fig()
        if style in ('Heading1', 'Heading 1', 'Heading2', 'Heading 2',
                     'Heading3', 'Heading 3'):
            return
        if sz in (14.0, 15.0) and bold:
            return  # old chapter banner / appendix banner
        if not text:
            return
        # table / exhibit caption -> renumber into the new scheme
        m = re.match(r'^(?:Table|Exhibit)\s+[A-Z]?[0-9]+[A-Za-z]?\.\s*(.+)$', text)
        if m and sz in (10.0, None) and bold:
            self.cap(m.group(1))
            return
        m = re.match(r'^Figure\s+[0-9]+\.\s*(.+)$', text)
        if m and bold:
            lab = self._flabel()
            bk = self._newbk()
            self.figures.append((lab, m.group(1), bk))
            self.add(K.with_bookmark(
                K.figcaption('%s. %s' % (lab, m.group(1))), bk))
            return
        if sz == 10.0 and bold:
            self.add(K.caption(text))
            return
        if sz == 10.0 and ital:
            self.add(K.source(text))
            return
        if ital and it.get('al') == 'center':
            self.add(K.fignote(text))
            return
        if style in ('ListBullet', 'List Bullet'):
            self.add(K.bullet(text, bold=bold))
            return
        if style in ('ListNumber', 'List Number'):
            self.add(K.number(text))
            return
        if style in ('ListParagraph', 'List Paragraph'):
            self.add(K.bullet(text, bold=bold))
            return
        # all-caps pseudo strap-lines from the old supplement chapters
        if text.isupper() and len(text) < 60:
            return
        self.add(K.para(text, bold=bold, italic=ital,
                        size=int(sz) if sz and sz != 12.0 else None))


# --------------------------------------------------------------------------
# index (table of contents) in the Debt-Market reference layout
# --------------------------------------------------------------------------
def _pg(bk, pages):
    return K.Raw(K.pageref(bk, (pages or {}).get(bk, '')))


def build_index(doc, pages=None):
    rows = [['', '', 'CONTENT', 'PAGE NO.']]
    for e in doc.toc:
        if e['lvl'] == 0:
            rows.append([e['chap'], '', e['title'], _pg(e['bk'], pages)])
        else:
            rows.append(['', e['no'], e['title'], _pg(e['bk'], pages)])
    return K.table(rows, widths=[1250, 850, 6336, 1500],
                   header=True, first_col_left=True)


def build_list_of(entries, head_a, head_b, pages=None):
    rows = [[head_a, head_b, 'PAGE NO.']]
    for lab, title, bk in entries:
        rows.append([lab, title, _pg(bk, pages)])
    return K.table(rows, widths=[1250, 7186, 1500], header=True,
                   first_col_left=True)


# --------------------------------------------------------------------------
# packaging
# --------------------------------------------------------------------------
NSDECL = (' xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
          ' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
          ' xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"'
          ' xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
          ' xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"'
          ' xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"'
          ' xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"'
          ' xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"'
          ' xmlns:v="urn:schemas-microsoft-com:office:office"')


def write_docx(src, dst, body_xml_blocks, words=None, pages=None):
    with zipfile.ZipFile(src) as z:
        names = z.namelist()
        data = {n: z.read(n) for n in names}

    root = etree.fromstring(data['word/document.xml'])
    body = root.find('{%s}body' % W)
    sectpr = body.findall('{%s}sectPr' % W)[-1]
    sect_copy = etree.fromstring(etree.tostring(sectpr))
    for child in list(body):
        body.remove(child)

    for blob in body_xml_blocks:
        frag = etree.fromstring('<wrap%s>%s</wrap>' % (NSDECL, blob))
        for el in list(frag):
            body.append(el)
    body.append(sect_copy)

    data['word/document.xml'] = etree.tostring(
        root, xml_declaration=True, encoding='UTF-8', standalone=True)

    if words or pages:
        app = data.get('docProps/app.xml', b'').decode('utf-8')
        if words:
            app = re.sub(r'<Words>\d+</Words>', '<Words>%d</Words>' % words, app)
            app = re.sub(r'<Characters>\d+</Characters>',
                         '<Characters>%d</Characters>' % (words * 6), app)
        if pages:
            app = re.sub(r'<Pages>\d+</Pages>', '<Pages>%d</Pages>' % pages, app)
        data['docProps/app.xml'] = app.encode('utf-8')

    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.writestr(n, data[n])
