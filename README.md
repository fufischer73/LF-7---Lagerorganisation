# LF 7: Logistik- und Lagerprozesse koordinieren, umsetzen und überwachen

Lernpfad für Industriekaufleute, 2. Lehrjahr (Lehrplan 2024), 40 Std., gebaut mit dem Lernpfad-Baukasten.

- `planung/` – Entwurf der komplexen Lernsituationen und Handlungsprodukte
- `nextcloud/` – OnlyOffice-Materialien je Block (Block-I, Block-II, Block-III) zum Ablegen in der Nextcloud; `werkzeuge/` – Skripte, die sie erzeugen (`block1_bauen.py`, `block2_bauen.py`, `block3_bauen.py`); `bot/` – Anweisung für den KI-Assistenten
- `lernpfad/moodle-aufbau.yaml` – einzige Quelle für Moodle-Kurs und Web-Ansicht; `lernpfad/material/icons/` – Phasen-Symbole
- Bauen: `python3 <Lernpfad-Baukasten>/skripte/moodle_lf.py lernpfad` erzeugt `ausgabe/moodle/*.mbz` und `ausgabe/web/index.html`

| Block | Lernsituationen | Std. |
|---|---|---|
| I Logistik- und Lagerkonzept (HP 1) | LS 64, 65 | 12 |
| II Nachhaltigkeits- und Entsorgungskonzept (HP 2) | LS 70, 69 | 10 |
| III Kosten, Kennzahlen, Transport | LS 66, 67, 68 | 18 |

Ein Fachgespräch nach Block II bezieht sich auf beide Handlungsprodukte. Block III endet mit der Klassenarbeit 1.

## Fertige Dateien (`fertig/`)

- `lf7-logistik_moodle4.5.mbz` – Moodle-Kurs (Sicherung für Moodle 4.5), in einen leeren Kurs wiederherstellen
- `web-ansicht.html` – Erstansicht des Kurses zum Durchsehen im Browser (Datei öffnen, kein Server nötig)
- `LINKS_ausfuellen.md` – Liste der Nextcloud-Links, die noch eingetragen werden müssen

Die Dateien werden mit `python3 <Lernpfad-Baukasten>/skripte/moodle_lf.py lernpfad` erzeugt und hier abgelegt. Bei jeder neuen Version ersetzen.
