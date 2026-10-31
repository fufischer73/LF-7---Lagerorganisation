#!/usr/bin/env python3
"""Erzeugt die OnlyOffice-Materialien (.docx) für Block I in nextcloud/Block-I/."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import block1_a, block1_b, block1_c

Z = Path(__file__).resolve().parents[1] / "nextcloud" / "Block-I"
Z.mkdir(parents=True, exist_ok=True)
z = str(Z) + "/"
block1_a.auftrag_hp1(z + "Block-I_Handlungsprodukt-1_Auftrag.docx")
block1_a.orientierungen(z)
block1_a.strukturlegen(z + "Block-I_Systematisierung_Strukturlegetechnik.docx")
block1_a.reflexion(z + "Block-I_Zwischenreflexion.docx")
block1_b.ls64_teil1(z + "LS64_Loesungen_Teil1.docx")
block1_b.ls65_teil1(z + "LS65_Loesungen_Teil1.docx")
block1_c.lernatelier_ls64(z + "LS64_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block1_c.lernatelier_ls65(z + "LS65_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block1_c.loesungen_ls64_teil2(z + "LS64_Loesungen_Teil2.docx")
block1_c.loesungen_ls65_teil2(z + "LS65_Loesungen_Teil2.docx")
print(*sorted(p.name for p in Z.glob("*.docx")), sep="\n")
