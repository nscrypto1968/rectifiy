"""Emitters that reproduce, byte-for-byte in style, the OOXML idioms used in
'SIP - M16158 NIkhil Singh.docx' so that rebuilt content is visually identical
to the student's original file.

Conventions captured from the original document
-----------------------------------------------
* Default font          : Times New Roman (docDefaults), body 12 pt (sz 24)
* Heading 1             : bold, ALL CAPS, 14 pt, centred  (style "Heading1")
* Heading 2             : bold, ALL CAPS, 12 pt            (style "Heading2")
* Heading 3             : bold, 12 pt                      (style "Heading3")
* Body paragraph        : justified, spacing after 120 twips
* Chapter banner        : bold 14 pt, centred, before 120 / after 160, line 240
* Table caption         : bold 10 pt, keepNext, before 80 / after 60
* Source note           : italic 10 pt, before 40 / after 140
* Figure caption        : bold 10 pt, centred, keepNext, after 20
* Figure note           : italic 10 pt, centred, after 140
* Tables                : tblW auto, centred, fixed layout, tblLook 04A0
                          header row  -> cantSplit + tblHeader, shading D9D9D9,
                                         borders sz 4 (top/bottom) sz 3 (l/r),
                                         bold 10 pt
                          body rows   -> cantSplit, borders sz 2 all round,
                                         banded shading FFFFFF, 10 pt
                          cell margin -> 75/90/75/90 dxa, vAlign center
                          col 1 left-aligned, remaining columns centred
"""

from xml.sax.saxutils import escape

# Usable text width between the 907-twip side margins of the original page
# set-up (11909 - 907 - 907 = 10095). The original tables are laid out on a
# 9936-twip grid, so we keep exactly that.
TABLE_WIDTH = 9936

_RSID = ' w:rsidR="005F2FC4" w:rsidRDefault="00000000"'


def _t(text):
    """A <w:t> run body with whitespace preserved."""
    return '<w:t xml:space="preserve">%s</w:t>' % escape(text)


# --------------------------------------------------------------------------
# paragraphs
# --------------------------------------------------------------------------

def para(text, justify=True, after=None, bold=False, italic=False,
         size=None, center=False, keep=False):
    """A normal body paragraph in the original's idiom."""
    pr = []
    if keep:
        pr.append('<w:keepNext/>')
    if after is not None:
        pr.append('<w:spacing w:after="%d"/>' % after)
    if center:
        pr.append('<w:jc w:val="center"/>')
    elif justify:
        pr.append('<w:jc w:val="both"/>')
    rpr = []
    if bold:
        rpr.append('<w:b/>')
    if italic:
        rpr.append('<w:i/>')
    if size:
        rpr.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size * 2, size * 2))
    rpr = '<w:rPr>%s</w:rPr>' % ''.join(rpr) if rpr else ''
    return ('<w:p%s><w:pPr>%s</w:pPr><w:r>%s%s</w:r></w:p>'
            % (_RSID, ''.join(pr), rpr, _t(text)))


def chapter(label, page_break=True):
    """The centred bold 14 pt 'CHAPTER n' banner."""
    pb = '<w:pageBreakBefore/>' if page_break else ''
    return ('<w:p%s><w:pPr>%s<w:keepNext/>'
            '<w:spacing w:before="120" w:after="160" w:line="240" w:lineRule="auto"/>'
            '<w:jc w:val="center"/></w:pPr>'
            '<w:r><w:rPr><w:b/><w:bCs/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>'
            '%s</w:r></w:p>' % (_RSID, pb, _t(label)))


def h1(text, page_break=False):
    pb = '<w:pageBreakBefore/>' if page_break else ''
    return ('<w:p%s><w:pPr><w:pStyle w:val="Heading1"/>%s</w:pPr>'
            '<w:r>%s</w:r></w:p>' % (_RSID, pb, _t(text)))


def h2(text):
    return ('<w:p%s><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>'
            '<w:r>%s</w:r></w:p>' % (_RSID, _t(text)))


def h3(text):
    return ('<w:p%s><w:pPr><w:pStyle w:val="Heading3"/></w:pPr>'
            '<w:r>%s</w:r></w:p>' % (_RSID, _t(text)))


def subtitle(text):
    """Italic 10 pt chapter strap-line used under every Heading 1."""
    return ('<w:p%s><w:pPr><w:spacing w:after="160"/></w:pPr>'
            '<w:r><w:rPr><w:i/><w:sz w:val="20"/></w:rPr>%s</w:r></w:p>'
            % (_RSID, _t(text)))


def caption(text):
    """Bold 10 pt table caption, kept with the table that follows."""
    return ('<w:p%s><w:pPr><w:keepNext/><w:spacing w:before="80" w:after="60"/></w:pPr>'
            '<w:r><w:rPr><w:b/><w:sz w:val="20"/></w:rPr>%s</w:r></w:p>'
            % (_RSID, _t(text)))


def source(text):
    """Italic 10 pt 'Source / note:' line placed under a table."""
    if not text.lower().startswith(('source', 'note')):
        text = 'Source / note: ' + text
    return ('<w:p%s><w:pPr><w:spacing w:before="40" w:after="140"/>'
            '<w:jc w:val="both"/></w:pPr>'
            '<w:r><w:rPr><w:i/><w:sz w:val="20"/></w:rPr>%s</w:r></w:p>'
            % (_RSID, _t(text)))


def bullet(text, bold=False):
    rpr = '<w:rPr><w:b/></w:rPr>' if bold else ''
    return ('<w:p%s><w:pPr><w:pStyle w:val="ListBullet"/><w:spacing w:after="50"/>'
            '<w:ind w:left="317" w:hanging="202"/><w:jc w:val="both"/></w:pPr>'
            '<w:r>%s%s</w:r></w:p>' % (_RSID, rpr, _t(text)))


def number(text):
    return ('<w:p%s><w:pPr><w:pStyle w:val="ListNumber"/><w:spacing w:after="50"/>'
            '<w:jc w:val="both"/></w:pPr><w:r>%s</w:r></w:p>' % (_RSID, _t(text)))


def figure(rid, cx, cy, pic_id=1):
    """Inline picture paragraph, centred, exactly as in the original."""
    return (
        '<w:p%s><w:pPr><w:spacing w:before="60" w:after="20"/><w:jc w:val="center"/>'
        '</w:pPr><w:r><w:rPr><w:noProof/></w:rPr><w:drawing>'
        '<wp:inline distT="0" distB="0" distL="0" distR="0">'
        '<wp:extent cx="%d" cy="%d"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:docPr id="%d" name="Picture %d"/><wp:cNvGraphicFramePr>'
        '<a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>'
        '</wp:cNvGraphicFramePr>'
        '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:nvPicPr><pic:cNvPr id="0" name="image.png"/><pic:cNvPicPr/></pic:nvPicPr>'
        '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        '</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
        % (_RSID, cx, cy, pic_id, pic_id, rid, cx, cy))


def figcaption(text):
    return ('<w:p%s><w:pPr><w:keepNext/><w:spacing w:after="20"/>'
            '<w:jc w:val="center"/></w:pPr>'
            '<w:r><w:rPr><w:b/><w:sz w:val="20"/></w:rPr>%s</w:r></w:p>'
            % (_RSID, _t(text)))


def fignote(text):
    return ('<w:p%s><w:pPr><w:spacing w:after="140"/><w:jc w:val="center"/></w:pPr>'
            '<w:r><w:rPr><w:i/><w:sz w:val="20"/></w:rPr>%s</w:r></w:p>'
            % (_RSID, _t(text)))


def pagebreak():
    return '<w:p%s><w:r><w:br w:type="page"/></w:r></w:p>' % _RSID


# --------------------------------------------------------------------------
# tables
# --------------------------------------------------------------------------

class Raw(str):
    """Cell content that is already run-level XML (e.g. a PAGEREF field)."""
    pass


_BMID = [5000]


def with_bookmark(xml, name):
    """Wrap the runs of a single paragraph in a Word bookmark."""
    _BMID[0] += 1
    bid = _BMID[0]
    start = '<w:bookmarkStart w:id="%d" w:name="%s"/>' % (bid, name)
    end = '<w:bookmarkEnd w:id="%d"/>' % bid
    i = xml.find('</w:pPr>')
    j = xml.rfind('</w:p>')
    if i < 0 or j < 0:
        return start + xml + end
    i += len('</w:pPr>')
    return xml[:i] + start + xml[i:j] + end + xml[j:]


def pageref(bookmark, cached=''):
    """A PAGEREF field with a cached result, so a number shows even before
    the reader presses F9; Word recomputes it exactly on update or print."""
    rpr = '<w:rPr><w:sz w:val="20"/></w:rPr>'
    return ('<w:r>%s<w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r>%s<w:instrText xml:space="preserve"> PAGEREF %s \\h </w:instrText></w:r>'
            '<w:r>%s<w:fldChar w:fldCharType="separate"/></w:r>'
            '<w:r>%s<w:t>%s</w:t></w:r>'
            '<w:r>%s<w:fldChar w:fldCharType="end"/></w:r>'
            % (rpr, rpr, bookmark, rpr, rpr, escape(str(cached)), rpr))


def _cell(text, width, header=False, align_center=True, shade=None, bold=False):
    if header:
        borders = ('<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:left w:val="single" w:sz="3" w:space="0" w:color="000000"/>'
                   '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:right w:val="single" w:sz="3" w:space="0" w:color="000000"/>')
        shade = 'D9D9D9'
        bold = True
    else:
        borders = ''.join('<w:%s w:val="single" w:sz="2" w:space="0" w:color="000000"/>' % s
                          for s in ('top', 'left', 'bottom', 'right'))
    shd = ('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % shade) if shade else ''
    jc = '<w:jc w:val="center"/>' if align_center else ''
    rpr = '<w:rPr>%s<w:sz w:val="20"/></w:rPr>' % ('<w:b/>' if bold else '')
    ppr = ('<w:pPr><w:keepNext/>'
           '<w:spacing w:after="0" w:line="240" w:lineRule="auto"/>%s</w:pPr>' % jc)
    paras = []
    if isinstance(text, Raw):
        paras.append('<w:p%s>%s%s</w:p>' % (_RSID, ppr, str(text)))
    else:
        for line in str(text).split('\n'):
            paras.append('<w:p%s>%s<w:r>%s%s</w:r></w:p>'
                         % (_RSID, ppr, rpr, _t(line)))
    return ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/><w:tcBorders>%s</w:tcBorders>%s'
            '<w:tcMar><w:top w:w="75" w:type="dxa"/><w:left w:w="90" w:type="dxa"/>'
            '<w:bottom w:w="75" w:type="dxa"/><w:right w:w="90" w:type="dxa"/></w:tcMar>'
            '<w:vAlign w:val="center"/></w:tcPr>%s</w:tc>'
            % (width, borders, shd, ''.join(paras)))


def table(rows, widths=None, header=True, first_col_left=True, bold_first_col=False):
    """Render a list-of-lists as a table in the original document's style."""
    ncols = max(len(r) for r in rows)
    rows = [list(r) + [''] * (ncols - len(r)) for r in rows]
    _len = lambda v: 0 if isinstance(v, Raw) else len(str(v))
    if not widths:
        # weight columns by the amount of text they carry
        load = []
        for c in range(ncols):
            load.append(max(8, sum(_len(r[c]) for r in rows) / float(len(rows))))
        total = sum(load)
        widths = [max(620, int(TABLE_WIDTH * x / total)) for x in load]
        drift = TABLE_WIDTH - sum(widths)
        widths[-1] += drift
    else:
        scale = TABLE_WIDTH / float(sum(widths))
        widths = [int(w * scale) for w in widths]
        widths[-1] += TABLE_WIDTH - sum(widths)

    grid = ''.join('<w:gridCol w:w="%d"/>' % w for w in widths)
    out = ['<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:jc w:val="center"/>'
           '<w:tblLayout w:type="fixed"/>'
           '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" '
           'w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
           '<w:tblGrid>%s</w:tblGrid>' % grid]

    for i, row in enumerate(rows):
        is_hdr = header and i == 0
        trpr = ('<w:trPr><w:cantSplit/>%s<w:jc w:val="center"/></w:trPr>'
                % ('<w:tblHeader/>' if is_hdr else ''))
        body_index = i - (1 if header else 0)
        shade = None if is_hdr else ('FFFFFF' if body_index % 2 == 0 else None)
        cells = []
        for c, val in enumerate(row):
            centred = not (c == 0 and first_col_left)
            cells.append(_cell(val, widths[c], header=is_hdr,
                               align_center=centred, shade=shade,
                               bold=(bold_first_col and c == 0 and not is_hdr)))
        out.append('<w:tr%s>%s%s</w:tr>' % (' w:rsidR="005F2FC4"', trpr, ''.join(cells)))
    out.append('</w:tbl>')
    return ''.join(out)


def interp(text, label='Interpretation'):
    """MMS-template style interpretation box, rendered with the original
    document's own grey/white table palette instead of the template's colours."""
    return table([[label], [text]], widths=[TABLE_WIDTH],
                 header=True, first_col_left=True)


def spacer():
    return '<w:p%s><w:pPr><w:spacing w:after="0"/></w:pPr></w:p>' % _RSID
