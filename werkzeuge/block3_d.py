"""Block III, Teil D: Lösungen Teil 2 für LS 67 und LS 68."""
from docx_helfer import Dok
from block1_b import STATUS
from block3_a import KOPF
import rechnen_block3 as r
de = r.de


def loesungen_ls67_teil2(pfad):
    d = Dok(KOPF + " · LS 67", "LS 67 Lösungen Teil 2: Aufgaben 1 bis 19 und Zusatzaufgaben", STATUS)
    A7 = r.A7
    t7 = [["a", "58 St.", "40 St.", de(A7["a"][0]), f"{de(A7['a'][1], 0)} Tage"],
          ["b", f"{de(A7['b'][0], 0)} kg", "3.850 kg", "4,20", f"{de(A7['b'][1], 0)} Tage"],
          ["c", "6.300 St.", f"{de(A7['c'][1], 1)} St.", de(A7["c"][0]), "35 Tage"],
          ["d", "450 Pack.", "65 Pack.", de(A7["d"][0]), f"{de(A7['d'][1], 0)} Tage"],
          ["e", f"{de(A7['e'][0], 0)} St.", "420 St.", "5,75", f"{de(A7['e'][1], 0)} Tage"]]
    L = [
     ("Aufgabe 1", "a) Verstöße gegen Grundsätze der Lagerhaltung: Ordnung und Übersichtlichkeit, freie Gänge und Verkehrswege, Sicherheit (Stapelhöhe, Standfestigkeit, Brandschutz), "
      "schnelle Auffindbarkeit und Zugriff, Kennzeichnung der Ware, Schutz vor Beschädigung, Platz für Ein- und Auslagerung. b) Folgen: Suchzeiten, Verluste und Beschädigungen, Unfälle, "
      "Brandgefahr, aufwendige Inventur, Wertminderung der Ware."),
     ("Aufgabe 2", "Individuell (Erkundungstour)."),
     ("Aufgabe 3", "a Festplatzsystem (Artikel haben festen Platz). b chaotische Lagerhaltung (ohne Software findet man nichts). c Festplatzsystem. d Festplatzsystem (feste Plätze, Inventur schnell). "
      "e chaotische Lagerhaltung (Einlagerung auf freien Flächen)."),
     ("Aufgabe 4", "a) Die Behauptung gilt nicht grundsätzlich. Das Freiplatzsystem nutzt die Fläche besser, spart Raum und damit Raumkosten; es braucht aber Lagerverwaltungssoftware, Pflege "
      "und Schulung, birgt Fehlerrisiken und verlängert Wege. Das Festplatzsystem ist einfacher, braucht mehr Fläche. b) ba Bei Vorratshaltung (viele Bestände) ist Platz knapp: Das Freiplatzsystem "
      "wird eher vorteilhaft. bb Bei bedarfsorientierter Beschaffung (kleine Bestände, schneller Durchlauf) verliert der Flächenvorteil an Bedeutung, ein Festplatzsystem ist oft einfacher und ausreichend."),
     ("Aufgabe 5", "a LIFO (von oben nach unten, zuletzt eingelagertes zuerst). b FIFO (Gefäß wird unten geöffnet, zuerst Eingelagertes zuerst). c FIFO (neue Ware hinten, alte vorn). "
      "d HIFO (die wertvollste Ware zuerst). e LIFO (vom aufgeschütteten Haufen oben entnommen)."),
     ("Aufgabe 6", "a Löhne für Fachlageristen: fix. b buchhalterischer Wertverlust (Abschreibung): fix. c Aufwendungen für verdorbene, beschädigte und gestohlene Waren: variabel. "
      "d Unterhalt (Strom, Heizung, Wasser): überwiegend fix, nur der verbrauchsabhängige Teil ist variabel. e IT und Kommunikation: fix. f Versicherungen für Brandschutz: fix. "
      "g Verpackungsmaterial: variabel. (Zuordnung mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 7", "Absatz : Ø Lagerbestand = Umschlagshäufigkeit; 360 : Umschlagshäufigkeit = Ø Lagerdauer. Ergebnisse siehe Tabelle unten."),
     ("Aufgabe 8", f"a) aa Jahresbasis: (34 + {r.END8[-1]}) : 2 = {de(r.AVG8_J, 1)} St. ab Monatsbasis: (34 + {sum(r.END8)}) : 13 = {de(r.AVG8_M)} St. ac Bestellmenge und Mindestbestand: 6 + 25 : 2 = {de(r.AVG8_B, 1)} St. "
      f"b) Ø Lagerwert: {de(r.AVG8_J * r.EP8)} €, {de(r.AVG8_M * r.EP8)} € und {de(r.AVG8_B * r.EP8)} €. c) Am aussagekräftigsten ist die Monatsbasis, weil sie die Schwankungen im Jahr "
      f"(Bestände zwischen 4 und 28 St.) berücksichtigt. Die Jahresbasis (nur Anfang und Ende) und die Rechnung aus Mindestbestand und Bestellmenge bilden den Verlauf nicht ab."),
     ("Aufgabe 9", f"a) Endbestände: Werkstoff 1: {', '.join(map(str, r.W1_['ends']))} kg. Werkstoff 2: {', '.join(map(str, r.W2_['ends']))} St. Werkstoff 3: {', '.join(map(str, r.W3_['ends']))} L (Januar bis Dezember). "
      f"b) Ø Lagerbestand auf Monatsbasis (Anfangsbestand + 12 Endbestände) : 13 und Ø Lagerwert: W1 {de(r.W1_['avg'])} kg und {de(r.W1_['wert'])} €; W2 {de(r.W2_['avg'])} St. und {de(r.W2_['wert'])} €; "
      f"W3 {de(r.W3_['avg'])} L und {de(r.W3_['wert'])} €. c) Jahresverbrauch: W1 {r.W1_['verbrauch']} kg, W2 {r.W2_['verbrauch']} St., W3 {r.W3_['verbrauch']} L. "
      f"d) Umschlagshäufigkeit: W1 {de(r.W1_['uh'])}, W2 {de(r.W2_['uh'])}, W3 {de(r.W3_['uh'])}. e) Weitere Maßnahmen bei W3 (UH unter 1, Ø Lagerdauer über 360 Tage, großer Zukauf im März) und W2 "
      "(UH ca. 2). f) Maßnahmen: kleinere und häufigere Bestellungen, Bestellmenge an Verbrauch anpassen, Mindestbestand prüfen, Kanban oder Rahmenverträge, Abverkauf von Restbeständen, Lagerzeit überwachen."),
     ("Aufgabe 10", f"a) Bestände nach den Buchungen: " + ", ".join(f"{dd} {b}" for dd, z, b in r.BEST10) + " (Ausgang 22 am 30.06.). b) Ø Lagerbestand auf Monatsbasis: (22 + "
      f"{r.EB_JUL} + {r.EB_AUG} + {r.EB_SEP}) : 4 = {de(r.AVG10_M, 2)} St. (Endbestände Juli, August, September). c) Umschlagshäufigkeit im Quartal: {r.ABSATZ10} : {de(r.AVG10_M)} = {de(r.UH10)}; "
      f"Ø Lagerdauer: 90 : {de(r.UH10)} = {de(r.DAUER10, 1)} Tage. Die Umschlagshäufigkeit liegt unter dem Vorquartal (10,0), die Lagerdauer ist länger; zugleich war der Bestand Ende Juli mit 1 Stück "
      f"gefährlich knapp. d) Mit Anfangs- und Endbestand: (22 + {r.EB_SEP}) : 2 = {de(r.AVG10_J, 1)} St.; Umschlagshäufigkeit {de(r.ABSATZ10 / r.AVG10_J)}, Lagerdauer {de(90 / (r.ABSATZ10 / r.AVG10_J), 1)} Tage. "
      "Das Ergebnis weicht deutlich ab, weil der Bestand unterjährig stark schwankt; die Monatsbasis ist genauer."),
     ("Aufgabe 11", f"a) Annahme: Die 72 St. sind der Ø Bestand je Quartal. Umschlagshäufigkeit im ersten Quartal 378 : 72 = {de(r.UH11_Q1)}, im zweiten 239 : 72 = {de(r.UH11_Q2)}; hochgerechnet "
      f"aufs Jahr (Absatz der zwei Quartale mal 2): (378 + 239) · 2 : 72 = {de(r.UH11_J)}. Das liegt deutlich über dem Branchenwert 7,5: Der Bestand ist sehr knapp, die Lieferfähigkeit "
      "sollte geprüft werden. b) Mögliche Maßnahmen: Bestellmengen verkleinert, Just-in-Time oder Kanban eingeführt, Sortiment bereinigt, Aktionen zur Absatzsteigerung, Rahmenverträge mit Lieferanten, "
      "Abbau eiserner Bestände. (Berechnung mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 12", "a) " + "; ".join(f"{n}: Umschlagshäufigkeit {de(v[0], 1)}, Ø Lagerdauer {de(v[2], 0)} Tage" for n, v in r.SP.items()) + " (Quartal, 90 Tage). b) Zu eliminieren ist das Produkt mit der niedrigsten Umschlagshäufigkeit "
      f"und der längsten Lagerdauer: Bauklötze (0,5; 180 Tage). c) Umsatzeinbruch: 28 Packungen · 18,50 € = {de(r.SP['Bauklötze'][3])} € netto im Quartal. Auffangen kann ihn ein Produkt mit hoher Umschlagshäufigkeit und "
      "passender Zielgruppe, zum Beispiel Puzzle (3,7) oder Holzspielfiguren (4,0), das mit mehr Absatz die Fläche und das Kapital der Bauklötze nutzt."),
     ("Aufgabe 13", "a Verkürzung (Abverkauf senkt den Bestand). b Verlängerung (höherer Ø Bestand). c Verkürzung (mehr Absatz). d Verlängerung (tendenziell weniger Absatz). e Verkürzung (niedrigerer Ø Bestand). "
      "f keine Änderung (der Marktzins beeinflusst die Lagerzinsen, nicht die Lagerdauer)."),
     ("Aufgabe 14", f"a) Ø Lagerdauer = 360 : 2,55 = {de(r.DAUER14, 1)} Tage; Lagerzinssatz = 8,5 % · {de(r.DAUER14, 1)} : 360 = {de(r.ZS14 * 100, 3)} %. b) Ø Lagerwert = 87 · 378,00 € = 32.886,00 €; "
      f"Lagerzinsen = 32.886,00 € · {de(r.ZS14 * 100, 3)} % ≈ {de(r.ZINS14)} € (im Jahr)."),
     ("Aufgabe 15", f"a) Lagerzinssatz = 750 : 46.500 = {de(r.ZS15 * 100, 3)} %. b) Maximale Ø Lagerdauer = 1,613 % · 360 : 9,25 % = {de(r.DAUER15, 1)} Tage. c) Bei 100 Tagen wären die Lagerzinsen "
      f"46.500 · 9,25 % · 100 : 360 = {de(r.ZINS15_100)} €, also {de(r.ZINS15_100 - 750)} € über der Grenze. Die Lagerdauer müsste um rund 37 Tage sinken (Bestellmengen, Abverkauf, Absatzförderung)."),
     ("Aufgabe 16", f"Annahmen: Alle Werte pro Monat, Lagerzinssatz 4,5 % p. a. Lagerzinsen = 6.925 · 4,5 % : 12 = {de(r.ZINS16)} €. Lagerhaltungskosten = 2.540,00 + {de(r.ZINS16)} = {de(r.GES16)} €. "
      f"Gebundene Stücke: 6.925 : 138,50 = {de(r.STK16, 0)} St. Stückbezogene Lagerhaltungskosten ≈ {de(r.JE16)} € je Stück und Monat."),
     ("Aufgabe 17", f"a) Lagernutzungsgrad = genutzte Fläche : Gesamtfläche = {r.AUS17} : {r.FL17} = {de(r.NG17 * 100, 1)} %. b) Auslastung je Lager: Eigenlager 72,8 %, Fremdlager 1: 51,9 %, Fremdlager 2: 79,1 %. "
      "Fremdlager 1 braucht nur 148 m²; im Eigenlager sind 170 m² frei, sodass dieses Lager aufgegeben werden könnte (Einsparung 285 m² · 18,75 € = 5.343,75 € je Zeiteinheit bei den Mietkosten). "
      "c) Voraussetzungen: ausreichend freie Fläche im Eigenlager, Umorganisation (Festplatz- oder Freiplatzsystem, Lagerverwaltung), Vertragsfristen, Umlagerung, Inventur, Wege und Zugriff, Kosten der Umstellung."),
     ("Aufgabe 18", "Der Nutzungsgrad schwankt stark (55 %, 87 %, 76 %, 34 %): Der Absatz ist saisonal. Im 2. Quartal liegt die Spitze, im 4. Quartal ist das Lager weitgehend leer. Das Lager ist für die Spitze "
      "dimensioniert; sinnvoll wären flexible Flächen oder ein Fremdlager nur für die Spitzenzeiten."),
     ("Aufgabe 19", "a Mengenrabatte beim Einkauf: Ø Lagerbestand ↑, Ø Lagerwert ↑, Umschlagshäufigkeit ↓, Ø Lagerdauer ↑, Lagerzinssatz ↑ (größere Bestellmengen, länger gelagert). "
      "b Dauerhafte Preissenkung am Absatzmarkt: Absatz ↑; Ø Lagerbestand bei gleicher Beschaffung ↓ oder gleich, Ø Lagerwert ↓, Umschlagshäufigkeit ↑, Ø Lagerdauer ↓, Lagerzinssatz ↓."),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h3("Aufgabe 7: Tabelle der Ergebnisse")
    d.tabelle(["", "Absatz", "Ø Lagerbestand", "Umschlagshäufigkeit", "Ø Lagerdauer (volle Tage)"], t7, [1.2, 3.4, 3.8, 4.2, 4.4])
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Plus: Kennzahlen-Tabelle", "Formeln für Ø Lagerbestand (Anfangsbestand plus zwölf Endbestände durch 13), Ø Lagerwert, Umschlagshäufigkeit, bedingte Formatierung für Werte unter 3 "
         f"(Werkstoff 2 mit {de(r.W2_['uh'])} und Werkstoff 3 mit {de(r.W3_['uh'])} werden markiert)."],
        ["Basis: Fachartikel", "Festplatzsystem: feste Plätze, schnelles Auffinden, Platzierung schnell drehender Artikel nahe am Kommissionierplatz. Freiplatzsystem: Einlagerung auf freien "
         "Plätzen, nur mit Lagerverwaltungssoftware, bessere Flächennutzung; Artikel müssen ggf. aus mehreren Lagerorten zusammengetragen werden. Beides mit Textstellen belegen."],
        ["Kreativ: Kennzahlen im Betrieb", "Kriterien: Kennzahl genannt und erklärt, Beispiel nachvollziehbar, vertrauliche Daten geschützt."],
        ["BNE: Lagerbestand und Ressourcen", "Zum Beispiel: Hoher Bestand bindet Fläche und Energie (Heizung, Licht), erhöht Ausschuss und Entsorgung; Maßnahmen: bedarfsgerechte Bestellungen, Abverkauf, "
         "Mehrwegbehälter, Kennzahlen zur Überwachung (Umschlagshäufigkeit, Entsorgungsquote)."],
    ], [4.0, 13.0])
    d.speichern(pfad)


def loesungen_ls68_teil2(pfad):
    d = Dok(KOPF + " · LS 68", "LS 68 Lösungen Teil 2: Aufgaben 1 bis 20 und Zusatzaufgaben", STATUS)
    L = [
     ("Aufgabe 1", "a) Der Straßenverkehr dominiert Beförderungsmenge und -leistung mit großem Abstand (ungefähr drei Viertel); danach folgen Eisenbahn und Binnenschifffahrt, Seeverkehr, Rohrleitungen und Luftverkehr haben kleine Anteile. "
      "b) Gründe: flächendeckendes Straßennetz, Haus-zu-Haus-Lieferung, hohe Flexibilität und Schnelligkeit, kurze Strecken, Just-in-Time-Anforderungen, geringe Umschlagzeiten; Bahn und Binnenschiff sind an feste Netze und Terminale gebunden. "
      "(Prozentwerte aus der Grafik im Heft entnehmen.)"),
     ("Aufgabe 2", "Individuell mit Routenplaner und Fahrplänen. Erwartung: Bei langen Strecken (München–Berlin, Hamburg–Köln) kann das Flugzeug am schnellsten sein, auf kurzen Strecken (Stuttgart–Mannheim) sind Lkw und Bahn "
      "schneller als ein Flug; Umschlagzeiten und Anfahrt zum Flughafen sind zu beachten."),
     ("Aufgabe 3", "a) Wasserstraßen konzentrieren sich auf wenige große Flüsse und Kanäle; sie bilden kein flächendeckendes Netz wie die Straße, einzelne Regionen sind nicht erreichbar. "
      "b) ba Mainz: Rhein (und Main), bb Deggendorf: Donau, bc Braunschweig: Mittellandkanal (Stichkanal), bd Bremen: Weser. (Mit den Seiten der Wasserstraßenverwaltung abgleichen.)"),
     ("Aufgabe 4", "Individuell (Karte des Bundesamts für Kartographie und Geodäsie)."),
     ("Aufgabe 5", "Individuell: Anbieter vergleichen nach Leistungen (Express, Abholung, Sendungsverfolgung, Versicherung, Preise)."),
     ("Aufgabe 6", "a) Preise bei zwei bis drei KEP-Diensten im Ort recherchieren (Paket mit 210 · 120 · 30 cm und 28 kg ist oft ein Sperrgut- oder Spezialpaket). b) Der Express-Aufschlag erhöht den Preis deutlich, "
      "verkürzt aber die Lieferzeit. c) Mögliche Folgen des steigenden Paketaufkommens: Verkehr und Emissionen in Städten, Lärm, Verpackungsmüll, hohe Belastung der Zusteller, Engpässe bei Peaks."),
     ("Aufgabe 7", "a) Beispiel: aa München: Lkw (Straße), eventuell Bahn; ab London: Luftfracht (leicht, hochwertig, eilig) oder Lkw/Fähre; ac Schweden: Lkw mit Fähre oder Luftfracht je nach Eilbedürftigkeit. "
      "b) Lkw nach München: Direktverkehr; Lkw plus Luftfracht plus Lkw: multimodaler Verkehr. c) Vorlauf: Transport vom Kunden/Werk zum Flughafen (Lkw); Hauptlauf: Flug; Nachlauf: vom Zielflughafen zum Kunden. "
      "Die Läufe sind wichtig, weil an den Schnittstellen umgeschlagen wird (Zeit, Kosten, Fehlerquellen)."),
     ("Aufgabe 8", "a Ursprungszeugnis: Warenbegleitpapier (1). b Konnossement: Warenwertpapier (2). c Frachtbrief: Warenbegleitpapier (1). d Zollfaktura: Warenbegleitpapier (1). e Ladeschein: Warenwertpapier (2). "
      "f Packliste: Warenbegleitpapier (1). g Lagerschein: Warenwertpapier (2). (Einordnung von Ursprungszeugnis, Zollfaktura, Packliste mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 9", "a (1) Warenbegleitpapiere (informiert über die Lieferung). b (2) Warenwertpapiere (verbrieft den Anspruch auf Auslieferung). c (1). d (2). e (2). "
      "Hinweis: Die Begründungen sind nicht in allen Fällen trennscharf (siehe Info-Blatt und Änderungsvorschläge)."),
     ("Aufgabe 10", "a) aa Werkverkehr (eigener Lkw): Lieferschein, Packliste bzw. Ladeliste; ein Frachtbrief ist nicht nötig, weil kein Frachtvertrag besteht. ab Fremdtransport über das Binnenschiff: Frachtbrief oder "
      "Ladeschein (auf Verlangen des Absenders); der Frachtführer erhält die Güter und stellt das Papier aus; der Empfänger in Duisburg erhält Ware gegen Vorlage. b) Zweck: Der Lieferschein beschreibt die Lieferung, "
      "der Frachtbrief beweist den Frachtvertrag und die Übernahme und begleitet das Gut, der Ladeschein verbrieft den Anspruch auf Ablieferung und ist übertragbar. "
      "(Zum Wortlaut siehe Info-Blatt; Zuordnung mit dem Heft abgleichen.)"),
     ("Aufgabe 11", "a F (der Frachtführer führt den Transport durch). b S (der Spediteur organisiert und plant). c S (Speditionsvertrag zwischen Versender und Spediteur). "
      "d F (der Frachtführer verlädt betriebssicher und haftet). e S (Selbsteintritt). f F (Verspätungsschaden: zunächst der Frachtführer haftet). g S (ADSp). h F (Frachtvertrag verpflichtet zur Beförderung). "
      "(Zuordnung d und f mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 12", "Der Käufer (Fahrradfachhändler) trägt beim Versendungskauf die Preisgefahr, sobald die Ware an die Transportperson übergeben wurde (Versendungskauf, § 447 BGB); der Kaufpreis ist trotz Verlust zu zahlen. "
      "Der Verkäufer kann Schadenersatz vom Spediteur oder Frachtführer verlangen; dessen Haftung ist der Höhe nach begrenzt (§§ 431, 461 HGB). Eine Transportversicherung schließt die Lücke. "
      "Hinweis: Wortlaut von § 447 BGB und §§ 431, 461 HGB noch nicht abgeglichen. Vorgehen vor dem Einsatz prüfen."),
     ("Aufgabe 13", "Individuell (Frachtbörsen im Bundesland recherchieren)."),
     ("Aufgabe 14", f"a) Fixkosten Werkverkehr: Fahrer 12 · 3.550,00 = 42.600,00 € plus 28.552,50 € = {de(r.FIX14)} € pro Jahr. Spedition 4,75 €/km, variable Kosten Werkverkehr 2,10 €/km. "
      f"Kritische Entfernung = {de(r.FIX14)} : (4,75 − 2,10) = {de(r.KRIT14, 0)} km. Grafik: Spedition als Gerade durch den Ursprung mit 4,75 €/km, Werkverkehr beginnt bei {de(r.FIX14)} € und steigt um 2,10 €/km. "
      f"b) Bei 14.350 km: Werkverkehr {de(r.EIGEN14)} €, Spedition {de(r.FREMD14)} €. Empfehlung: Spedition (14.350 km liegen unter 26.850 km). c) Werkverkehr lohnt sich erst bei mehr als 26.850 km im Jahr; "
      "bei wachsendem Kundenstamm kann das erreicht werden. Weitere Aspekte: Auslastung der Fahrzeuge (Rückfracht), Flexibilität, Kontrolle, Kapitalbindung, Personalrisiken."),
     ("Aufgabe 15", f"Annahmen: Alle Werte pro Monat; Treibstoff und Wartung gelten als variabel mit der Fahrleistung. a) Eigener Transporter: 560,00 + 125,00 (1.500 : 12) + 1.500,00 (18.000 : 12) + 300,00 (3.600 : 12) + 1.600,00 = "
      f"{de(r.MON15)} €. Spedition: 8.000 · 0,49 = {de(r.FREMD15)} €. Die Spedition ist um {de(r.MON15 - r.FREMD15)} € im Monat günstiger. b) Fixe Kosten: 560,00 + 125,00 + 1.600,00 = {de(r.FIX15)} €. "
      f"Variable Kosten: (1.500 + 300) : 8.000 = {de(r.VARKM15, 3)} €/km. Kritische Entfernung = {de(r.FIX15)} : (0,49 − {de(r.VARKM15, 3)}) ≈ {de(r.KRIT15M, 0)} km im Monat."),
     ("Aufgabe 16", f"a) Durchschnitt: 3.000 km : 12 = 250 km im Monat; 250 km liegt unter 260 km: Empfehlung Fremdtransport. b) Auf Monatsbasis läge die Strecke im März (264), Juli (285), August (302), September (276) und Oktober (268) über 260 km, "
      "dort wäre das Eigenfahrzeug günstiger. Entscheidend ist aber, dass die Fixkosten des Eigenfahrzeugs in allen Monaten anfallen; deshalb ist die Jahresbetrachtung sinnvoll und die Entscheidung für den "
      "Fremdtransport ändert sich nicht. Nur wenn Fahrzeug und Fahrer in den schwachen Monaten anderweitig genutzt werden können, wäre eine Mischlösung denkbar."),
     ("Aufgabe 17", "a) Kriterien: Kosten, Schnelligkeit, Termintreue und Zuverlässigkeit, Flexibilität, Sendungsverfolgung, Haftung und Versicherung, Umweltwirkung, Kundenservice, Verfügbarkeit von Kapazität. "
      "b) Grenzen: Gewichtung und Punktvergabe sind subjektiv, das Ergebnis lässt sich durch die Gewichte beeinflussen, die Analyse wirkt genauer, als sie ist; Kosten sollten zusätzlich gerechnet werden, "
      "Kriterien müssen unabhängig voneinander sein, und Entscheidungen mit Risiko (Haftung, Ausfall) verlangen eine eigene Bewertung."),
     ("Aufgabe 18", "a variabel. b fix. c fix. d variabel (leistungsabhängig). e fix. f variabel. g fix. h variabel (nach Fahrleistung; zeitabhängige Teile fix). (Zuordnung mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 19", "a) Fahrerlose Transportsysteme: Unterfahrfahrzeuge, Routenzüge, Gabelstapler-FTS, autonome mobile Roboter (AMR), Regalbediengeräte. b) Aspekte: Investition und Amortisation, Platz und Layout, Anbindung an die Lagerverwaltung, "
      "Sicherheit bei gemeinsamem Arbeiten von Mensch und Maschine, Wartung und Ausfallkonzept, Schulung, Mitbestimmung. c) Vorteile: gleichbleibende Leistung, weniger körperliche Arbeit, Fehlerreduktion, rund um die Uhr; "
      "Nachteile: hohe Kosten, Abhängigkeit von Technik, geringere Flexibilität, Veränderung von Arbeitsplätzen."),
     ("Aufgabe 20", "Individuell (Transportmittel im Lager des Ausbildungsbetriebs vergleichen)."),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Basis: Info-Blatt und Arbeitsblatt", "Der Frachtbrief ist ein Warenbegleitpapier: Er beweist den Frachtvertrag und die Übernahme und begleitet das Gut. Er verbrieft keinen Anspruch auf Auslieferung und hat keine "
         "Traditionswirkung. Konnossement, Ladeschein und Lagerschein sind Warenwertpapiere. (Siehe überarbeitetes Info-Blatt.)"],
        ["Plus: Nutzwertanalyse", "Kriterien mit Gewichten (Summe 100 %), Punkte 1 bis 5 je Option, Nutzwert = Summe aus Gewicht mal Punkte; Sensitivitätsprüfung: Ändert sich die Rangfolge, wenn zum Beispiel "
         "die Kosten stärker gewichtet werden? Gute Lösungen nennen Grenzen und begründen die Empfehlung (kurze Strecke, Neukunde, hoher Wert)."],
        ["Kreativ: Erklärvideo", "Kriterien: Unterschiede richtig (Funktion, Rechtswirkung, Verkehrsträger), Beispiel, verständlich, höchstens drei Minuten."],
        ["BNE: CO2 beim Transport", "Methode: Fracht in Tonnenkilometern (0,72 t · 300 km = 216 tkm) mit Emissionsfaktoren je Verkehrsträger multiplizieren; Quelle angeben. Erwartung: Bahn und Binnenschiff "
         "verursachen je tkm deutlich weniger Emissionen als der Lkw, sind aber langsamer und weniger flexibel. Abwägung von Dauer, Kosten und Umwelt."],
    ], [4.0, 13.0])
    d.speichern(pfad)
