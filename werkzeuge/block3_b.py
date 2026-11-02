"""Block III, Teil B: Lösungen Teil 1 (Arbeitsblätter) für LS 66, 67, 68."""
from docx_helfer import Dok
from block1_b import STATUS
from block3_a import KOPF
import rechnen_block3 as r
de = r.de


def ls66_teil1(pfad):
    d = Dok(KOPF + " · LS 66", "LS 66 Lösungen Teil 1: Zwischen Eigen- und Fremdlager entscheiden", STATUS)
    d.h2("Arbeitsblatt 66.1 Kostenvergleich zwischen Eigen- und Fremdlager")
    d.p("Annahmen: Alle Beträge sind Monatswerte. Die Kosten für Miete, Löhne, Versicherung und Sicherheitsdienst sind fix, die "
        "Nebenkosten (4,20 €/m²) und Verbrauchskosten (6,30 €/m²) sind variabel mit der Lagerfläche. Das Fremdlager kostet 28,50 €/m².")
    d.h3("a) Berechnung der kritischen Lagerfläche")
    d.tabelle(["Schritt", "Rechnung"], [
        ["Fixe Kosten Eigenlager", f"Miete 3.750,00 + Löhne 2.335,00 + Versicherung 125,00 + Sicherheitsdienst 185,00 = {de(r.FIX661)} €"],
        ["Variable Kosten Eigenlager je m²", "Nebenkosten 4,20 + Verbrauchskosten 6,30 = 10,50 €/m²"],
        ["Kosten Fremdlager je m²", "28,50 €/m² (keine fixen Kosten)"],
        ["Gleichsetzen", f"{de(r.FIX661)} + 10,50 · x = 28,50 · x"],
        ["Kritische Lagerfläche", f"x = {de(r.FIX661)} : (28,50 − 10,50) = {de(r.KRIT661)} m²"],
    ], [5.0, 12.0])
    d.h3("b) Grafische Darstellung")
    d.p(f"Zwei Geraden über der Fläche (m²): Eigenlager beginnt bei {de(r.FIX661)} € und steigt um 10,50 € je m². Das Fremdlager beginnt bei 0 € "
        f"und steigt um 28,50 € je m². Sie schneiden sich bei ca. {de(r.KRIT661, 0)} m² und etwa {de(28.5 * r.KRIT661, 0)} €. Links vom Schnittpunkt ist das "
        "Fremdlager günstiger, rechts davon das Eigenlager. Hinweis: Die Achse des Arbeitsblatts endet bei 22.000 €; die Gerade des Fremdlagers verlässt sie "
        "bei ca. 770 m².")
    d.h3("c) Entscheidung")
    d.p(f"Bei 500 m² kostet das Eigenlager {de(r.EIGEN500)} € im Monat, das Fremdlager {de(r.FREMD500)} €. Der Bedarf liegt über der kritischen Fläche. "
        f"Rechnerisch ist das Eigenlager um {de(r.FREMD500 - r.EIGEN500)} € im Monat günstiger.")
    d.p("Weitere Aspekte für die begründete Entscheidung:")
    d.punkte(["Flexibilität: Eigenlager Kündigungsfrist zwei Monate zum Quartalsende, Fremdlager vier Wochen zum Monatsende, Lagerfläche beim Fremdlager "
              "kurzfristig anpassbar.",
              "Wachstum: Das Eigenlager bietet nur 650 m² Lagerfläche; bei weiterem Wachstum reicht es nicht.",
              "Personal und Know-how: Beim Eigenlager muss Personal geführt werden, das Fremdlager bietet Ein- und Auslagerung und Lagerbuch im Preis.",
              "Risiko und Kapitalbindung: Fixkosten fallen auch bei geringer Auslastung an.",
              "Standort und Anbindung: Eigenlager mit Autobahn- und Bahnhofsnähe; Verfügbarkeit sofort (Eigenlager) bzw. nach einer Woche (Fremdlager).",
              "Sicherheit: Wer haftet, wie sind Versicherung und Zutritt geregelt?"])
    d.p("Eine gute Empfehlung nennt die Rechnung, gewichtet die Aspekte und trifft eine klare Entscheidung, zum Beispiel: Eigenlager, wenn der Bedarf von 500 m² "
        "dauerhaft bleibt; ein Fremdlager nur zur Abdeckung von Spitzen.")
    d.h2("Arbeitsblatt 66.2 Vertragsverhältnisse beim Fremdlager")
    d.tabelle(["Feld", "Erwartung"], [
        ["Pfeile zwischen Fly Bike Werke GmbH (Einlagerer) und Lagerhalter", "Lagervertrag (Einlagerer und Lagerhalter); Übergabe der Ware zur Einlagerung (Einlagerer an Lagerhalter); "
         "Ausstellung des Lagerscheins (Lagerhalter an Einlagerer)"],
        ["Funktionen des Lagerscheins", "Beweisfunktion (Einlagerung, Art und Menge des Gutes), Legitimationsfunktion (nur der Inhaber kann die Herausgabe verlangen), "
         "Traditionsfunktion (Übertragung der Rechte am Gut durch Übertragung des Papiers, beim Orderlagerschein mit Indossament, siehe Info-Blatt zu Warenwertpapieren)"],
        ["Lagerbereiche (Abbildung)", "Trennungslager: Das Gut des Einlagerers (zum Beispiel FBW) liegt getrennt von dem anderer Einlagerer (XY KG, XZ OHG). "
         "Der Einlagerer bleibt Eigentümer, der Lagerhalter hat ein Obhutsrecht und die Pflicht, es sicher aufzubewahren und zu versichern. "
         "Vorteil: Das Gut bleibt unvermischt zuordenbar. (Gegensatz: Sammellager, in dem gleichartige Waren vermischt werden.)"],
    ], [5.0, 12.0])
    d.speichern(pfad)


def ls67_teil1(pfad):
    d = Dok(KOPF + " · LS 67", "LS 67 Lösungen Teil 1: Die Lagerhaltung mithilfe von Kennzahlen verbessern", STATUS)
    d.h2("Arbeitsblatt 67.1 Auswertung mithilfe von Lagerkennzahlen")
    d.p("Annahme: Ø Lagerbestand = (Anfangsbestand + Endbestand) : 2, Absatz = Summe der Abgänge im Jahr, Ø Lagerdauer = 360 Tage : Umschlagshäufigkeit. "
        "Wenn dein Heft den Ø Lagerbestand anders ermittelt (zum Beispiel aus Monatsendbeständen), weichen die Werte ab.")
    rows = [["Formel", "(AB + EB) : 2", "Absatz : Ø Lagerbestand", "360 : Umschlagshäufigkeit"]]
    for a, k in r.KENN.items():
        rows.append([f"Artikel {a}", f"{de(k['avg'], 1)} (Absatz {k['absatz']})", de(k["uh"]), f"{de(k['dauer'], 0)} Tage"])
    d.tabelle(["", "Ø Lagerbestand", "Umschlagshäufigkeit", "Ø Lagerdauer"], rows, [3.4, 4.6, 4.6, 4.4])
    d.h3("Vergleich mit Vorjahr und Branchenwert (Branchenwert 6)")
    rows = []
    for a, k in r.KENN.items():
        v = r.VORJAHR[a]
        rows.append([a, de(k["uh"]), str(v), de(k["uh"] - v), "6", de(k["uh"] - 6)])
    d.tabelle(["Artikel", "aktuell", "Vorjahr", "Differenz", "Branchenwert", "Differenz"], rows, [2.4, 2.8, 2.8, 3.0, 3.2, 2.8])
    d.p("Empfehlung (Beispiel): 701S liegt mit 7,74 über Vorjahr (2) und Branche (6); der Bestand ist knapp, die Lieferfähigkeit sollte geprüft werden. "
        "701M, 701L, 701XL und 701XXL liegen unter dem Branchenwert; am schwächsten ist 701XL (1,74, Ø Lagerdauer 207 Tage, Vorjahr 5). Hier sollten Bestellmengen "
        "gesenkt, Aktionen oder Sonderpreise geprüft und der Anteil dieser Größe im Sortiment überdacht werden. Auch 701M (2,92) und 701L (3,43) sind gesunken bzw. stagnieren "
        "unter dem Branchenwert.")
    d.p("Warum ist ein Branchenvergleich sinnvoll? Er zeigt, ob das Unternehmen im Vergleich zu ähnlichen Betrieben zu viel oder zu wenig Ware lagert; "
        "Vorjahreswerte zeigen nur die eigene Entwicklung. Grenzen: Branchenwerte sind Durchschnitte, Unternehmen und Sortimente unterscheiden sich.")
    d.h2("Arbeitsblatt 67.2 Zusammenhang zwischen Lagerkennzahlen")
    d.tabelle(["Feld", "Erwartung"], [
        ["Zu großer Lagerbestand führt zu", "hoher Kapitalbindung und hohen Zinsen, höheren Lagerkosten (Raum, Versicherung, Personal), Risiko von Verderb, Veralterung, Schwund"],
        ["Zu kleiner Lagerbestand führt zu", "Fehlmengen, Lieferverzug, Produktionsstillstand, entgangenem Umsatz und Kundenverlust, mehr Bestellungen (Bestellkosten)"],
        ["Hilfsmittel bei der Optimierung: Lagerkennzahlen", "Ø Lagerbestand, Ø Lagerwert, Umschlagshäufigkeit, Ø Lagerdauer, Lagerzinssatz und Lagerzinsen, Lagernutzungsgrad"],
        ["Ø Lagerbestand", "Formel: (Anfangsbestand + Endbestand) : 2 oder (Anfangsbestand + 12 Monatsendbestände) : 13. Je höher der Mindest- und/oder Höchstbestand, desto höher ist der Ø Lagerbestand."],
        ["Umschlagshäufigkeit", "Formel: Absatz : Ø Lagerbestand. Je höher der Ø Lagerbestand, desto niedriger die Umschlagshäufigkeit."],
        ["Ø Lagerdauer", "Formel: 360 Tage : Umschlagshäufigkeit. Je niedriger die Umschlagshäufigkeit, desto länger die Lagerdauer."],
        ["Lagerzinssatz", "Formel: Marktzinssatz · Ø Lagerdauer : 360. Je länger die Lagerdauer, desto höher der Lagerzinssatz und damit die Lagerzinsen."],
    ], [5.0, 12.0])
    d.speichern(pfad)


def ls68_teil1(pfad):
    d = Dok(KOPF + " · LS 68", "LS 68 Lösungen Teil 1: Die geeignete Transportform auswählen", STATUS)
    d.h2("Arbeitsblatt 68.1 Rechtliche Beziehungen beim Warenausgang")
    d.tabelle(["Feld", "Erwartung (Pfeile im Heft zuordnen)"], [
        ["Fly Bike Werke GmbH", "Verkäufer und Absender"],
        ["Radbauer GmbH", "Käufer und Empfänger"],
        ["Schreiber Transporte GmbH", "Frachtführer (Spedition, die Transporte selbst durchführt)"],
        ["(1) zwischen Verkäufer und Käufer", "Kaufvertrag (Auftragsbestätigung)"],
        ["(2) Absender an Frachtführer", "Frachtvertrag"],
        ["(3) Absender an Frachtführer", "Frachtbrief (Original) und Packliste"],
        ["(4) Absender an Frachtführer", "Ware zur Beförderung (Übergabe der Güter)"],
        ["(5) Frachtführer an Empfänger", "Ablieferung der Ware"],
        ["(6) Empfänger an Frachtführer", "Empfangsbestätigung (Quittung auf dem Frachtbrief)"],
    ], [5.5, 11.5])
    d.p("Hinweis: Die Reihenfolge der Pfeile (3) bis (6) mit der Abbildung im Heft abgleichen.", kursiv=True)
    d.h3("Frachtbrief: Tabelle im Arbeitsblatt")
    d.tabelle(["Feld", "Erwartung"], [
        ["Aussteller", "Der Absender (hier: Fly Bike Werke GmbH) stellt den Frachtbrief aus bzw. füllt ihn aus; der Frachtführer unterschreibt bei Übernahme."],
        ["Ausstellungspflicht?", "Nein. Der Frachtführer kann die Ausstellung verlangen (Kann-Papier, § 408 HGB). Die Schreiber Transporte GmbH verlangt ihn immer."],
        ["Inhalte", "Absender, Empfänger, Frachtführer, Ort und Tag der Übernahme, Ablieferungsstelle, Beschreibung des Gutes (Anzahl, Zeichen, Nummern, Rohgewicht), "
         "vereinbarte Fracht und Kosten (Frankatur), Weisungen zum Beispiel für Zoll, beigefügte Dokumente."],
        ["Funktionen", "Beweis (Abschluss und Inhalt des Frachtvertrags, Übernahme des Gutes), Quittung (Übernahme, ggf. mit Vorbehalt), Begleitpapier (begleitet das Gut, "
         "dient der Ablieferung), Sperrpapier (Weisungen des Absenders nur gegen Vorlage seiner Ausfertigung, wenn vorgeschrieben), Abrechnungsgrundlage."],
    ], [4.0, 13.0])
    d.h2("Arbeitsblatt 68.2 Frachtbrief für die Radbauer GmbH (Beispielausfüllung)")
    pal = r.PAL
    d.tabelle(["Feld", "Eintrag"], [
        ["Absender", "Fly Bike Werke GmbH, Rostocker Str. 334, 26121 Oldenburg"],
        ["Empfänger", "Radbauer GmbH, Augsburger Straße 21, 80335 München"],
        ["Frachtführer", "Schreiber Transporte GmbH, Von-Bäumer-Straße 40, 26123 Oldenburg"],
        ["Übernahme des Gutes", "Oldenburg, Ausgangslager, Tor 2; Tag laut Auftragsbestätigung (Datum 20.02.20XX, Lieferung nach Absprache)"],
        ["Ablieferung des Gutes", "München, Radbauer GmbH, Augsburger Straße 21"],
        ["Beigefügte Dokumente", "Packliste in zweifacher Ausfertigung, Lieferschein"],
        ["Anzahl der Packstücke / Art", f"8 Kartons (je 5 Fahrräder) auf {pal} Europaletten (je 4 Kartons)"],
        ["Zeichen und Nummern", "FBW20XX99"],
        ["Bezeichnung des Gutes", "Fahrräder: 10 Mountain Dispo, 5 Mountain Constitution, 25 Mountain Unlimited (zusammen 40 Fahrräder)"],
        ["Bruttogewicht", "ca. 720 kg Fahrräder (40 · 18 kg) zuzüglich Verpackung und Paletten; ein Karton mit 5 Rädern ca. 90 kg"],
        ["Volumen", "ca. 2,9 m³ (je Palette 1,2 m · 0,8 m · 1,5 m = 1,44 m³, zwei Paletten) ohne Palettenhöhe"],
        ["Gefahrgut", "keines"],
        ["Frankatur", "Fracht trägt der Absender, die Versandkosten (1.500,00 €) stellt er dem Käufer in Rechnung (frei Haus, Kosten laut Auftragsbestätigung)"],
        ["Ausgefertigt in / am", "Oldenburg, 20.02.20XX; Unterschriften und Stempel von Absender und Frachtführer"],
    ], [4.5, 12.5])
    d.p("Rechnung: 40 Fahrräder : 5 je Karton = 8 Kartons; 8 : 4 je Palette = 2 Paletten. Maße und Gewicht mit dem Heft abgleichen; Palettenhöhe und Verpackungsgewicht "
        "sind nicht angegeben.", kursiv=True)
    d.h2("Auftrag 4: Transportmittel für den Auftrag der Go2Bike KG")
    d.p("Ausgangslage: Zwei Pakete, Neukunde in Oldenburg (gleiche Stadt), Lieferung per Express bis 23.02.20XX, versandkostenfrei frei Haus. Warenwert 6.440,00 € netto, "
        "also hochwertig.")
    d.tabelle(["Kriterium", "Überlegung"], [
        ["Entfernung", "innerstädtisch, sehr kurz: Fernverkehr (Bahn, Luft, Schiff) scheidet aus"],
        ["Termin", "Express, bis 23.02.20XX (3 Tage): Kurierdienst, KEP-Express oder eigener Lieferwagen sicher machbar"],
        ["Wert und Haftung", "hoher Wert: Sendungsverfolgung, Versicherung und Haftungshöhe prüfen (Haftung nach HGB begrenzt)"],
        ["Kosten", "Preise bei KEP-Diensten und lokalen Kurieren recherchieren und vergleichen; Werkverkehr mit eigenem Fahrzeug kostet ohnehin Fahrzeug und Fahrer"],
        ["Umwelt", "Lastenrad oder Elektrofahrzeug in der Stadt möglich"],
    ], [4.0, 13.0])
    d.p("Empfehlung (Beispiel): lokaler Kurier oder KEP-Express mit Sendungsverfolgung und Zustellung gegen Unterschrift, alternativ eigener Fahrer (Werkverkehr), weil "
        "die Entfernung kurz und der Neukunde wichtig ist. Die konkreten Preise werden recherchiert und hier eingetragen; sie sind nicht vorgegeben.")
    d.speichern(pfad)
