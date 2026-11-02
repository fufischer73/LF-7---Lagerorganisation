#!/usr/bin/env python3
"""Erzeugt die OnlyOffice-Materialien (.docx) für Block III in nextcloud/Block-III/."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import block3_a, block3_b, block3_c, block3_d, block3_papiere

Z = Path(__file__).resolve().parents[1] / "nextcloud" / "Block-III"
Z.mkdir(parents=True, exist_ok=True)
z = str(Z) + "/"
block3_a.orientierungen(z)
block3_a.strukturlegen(z + "Block-III_Systematisierung_Strukturlegetechnik.docx")
block3_a.klassenarbeit(z + "Block-III_Klassenarbeit-1_Ueberblick_und_Vorbereitung.docx")
block3_a.reflexion(z + "Block-III_Reflexion.docx")
block3_b.ls66_teil1(z + "LS66_Loesungen_Teil1.docx")
block3_b.ls67_teil1(z + "LS67_Loesungen_Teil1.docx")
block3_b.ls68_teil1(z + "LS68_Loesungen_Teil1.docx")
block3_c.lernatelier_ls66(z + "LS66_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block3_c.lernatelier_ls67(z + "LS67_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block3_c.lernatelier_ls68(z + "LS68_Lernatelier_Aufgabenauswahl_und_Zusatz.docx")
block3_c.loesungen_ls66_teil2(z + "LS66_Loesungen_Teil2.docx")
block3_d.loesungen_ls67_teil2(z + "LS67_Loesungen_Teil2.docx")
block3_d.loesungen_ls68_teil2(z + "LS68_Loesungen_Teil2.docx")
block3_papiere.info_blatt(str(Z / "LS68_Info-Blatt_Warenbegleitpapiere_und_Warenwertpapiere_ueberarbeitet.docx"))
block3_papiere.arbeitsblatt_anpassungen(str(Z / "LS68_Arbeitsblatt_Warenbegleitpapiere_Aenderungsvorschlaege.docx"))
print(len(list(Z.glob("*.docx"))), "Dateien")
