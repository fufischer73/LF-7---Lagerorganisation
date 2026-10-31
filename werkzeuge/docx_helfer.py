"""Kleine Hilfen, um die OnlyOffice-Materialien (.docx) einheitlich zu erzeugen."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TEAL = RGBColor(0x0d, 0x4f, 0x4f)


def _shade(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), color)
    tcPr.append(sh)


class Dok:
    def __init__(self, kopfzeile, titel, status=None):
        self.d = Document()
        for s in self.d.sections:
            s.left_margin = s.right_margin = Cm(2); s.top_margin = s.bottom_margin = Cm(1.8)
            s.header.paragraphs[0].text = kopfzeile
            s.header.paragraphs[0].runs[0].font.size = Pt(8.5)
            s.header.paragraphs[0].runs[0].font.color.rgb = RGBColor(0x63, 0x6e, 0x72)
        st = self.d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
        for n, sz in (("Heading 1", 16), ("Heading 2", 12.5), ("Heading 3", 11)):
            h = self.d.styles[n]; h.font.name = "Calibri"; h.font.size = Pt(sz); h.font.color.rgb = TEAL; h.font.bold = True
        t = self.d.add_heading(titel, 0)
        for r in t.runs:
            r.font.size = Pt(20); r.font.color.rgb = TEAL; r.font.name = "Calibri"
        if status:
            self.hinweis(status, "FFF3CD")

    def h1(self, t): self.d.add_heading(t, 1)
    def h2(self, t): self.d.add_heading(t, 2)
    def h3(self, t): self.d.add_heading(t, 3)

    def p(self, text, fett=False, kursiv=False):
        para = self.d.add_paragraph(); r = para.add_run(text); r.bold = fett; r.italic = kursiv
        return para

    def punkte(self, items, stil="List Bullet"):
        for i in items:
            self.d.add_paragraph(i, style=stil)

    def nummern(self, items):
        self.punkte(items, "List Number")

    def hinweis(self, text, farbe="E8F5E9"):
        t = self.d.add_table(rows=1, cols=1); t.style = "Table Grid"
        c = t.rows[0].cells[0]; c.text = text; _shade(c, farbe)
        for para in c.paragraphs:
            for r in para.runs: r.font.size = Pt(10)
        self.d.add_paragraph()

    def tabelle(self, kopf, zeilen, breiten=None, groesse=9.5):
        t = self.d.add_table(rows=1, cols=len(kopf)); t.style = "Table Grid"; t.autofit = False
        for i, h in enumerate(kopf):
            c = t.rows[0].cells[i]; c.text = ""
            r = c.paragraphs[0].add_run(h); r.bold = True; r.font.color.rgb = RGBColor(255, 255, 255); _shade(c, "0D4F4F")
        for z in zeilen:
            cells = t.add_row().cells
            for i, v in enumerate(z):
                cells[i].text = str(v)
        for row in t.rows:
            for c in row.cells:
                for para in c.paragraphs:
                    for r in para.runs: r.font.size = Pt(groesse)
        if breiten:
            for row in t.rows:
                for i, w in enumerate(breiten): row.cells[i].width = Cm(w)
        self.d.add_paragraph()

    def speichern(self, pfad):
        self.d.save(pfad)
