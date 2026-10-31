#!/usr/bin/env python3
"""Erzeugt die OnlyOffice-Materialien (.docx) für Block II in nextcloud/Block-II/."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import block2_a, block2_b, block2_c

Z = Path(__file__).resolve().parents[1] / "nextcloud" / "Block-II"
Z.mkdir(parents=True, exist_ok=True)
z = str(Z) + "/"
block2_a.auftrag_hp2(z + "Block-II_Handlungsprodukt-2_Auftrag.docx")
block2_a.orientierungen(z)
block2_a.strukturlegen(z + "Block-II_Systematisierung_Strukturlegetechnik.docx")
block2_a.fachgespraech_schueler(z + "Block-II_Zertifizierung_Fachgespraech_Ablauf.docx")
block2_a.fachgespraech_lehrkraft(z + "Block-II_Fachgespraech_Fragen_und_Raster_Lehrkraft.docx")
block2_a.reflexion(z + "Block-II_Reflexion.docx")
block2_b.ls70_teil1(z + "LS70_Loesungen_Teil1.docx")
block2_b.ls69_teil1(z + "LS69_Loesungen_Teil1.docx")
block2_c.lernatelier_ls70(z + "LS70_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block2_c.lernatelier_ls69(z + "LS69_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block2_c.loesungen_ls70_teil2(z + "LS70_Loesungen_Teil2.docx")
block2_c.loesungen_ls69_teil2(z + "LS69_Loesungen_Teil2.docx")
print(*sorted(p.name for p in Z.glob("*.docx")), sep="\n")
