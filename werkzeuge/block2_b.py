"""Block II, Teil B: Lösungen Teil 1 (Arbeitsblätter) für LS 70 und LS 69."""
from docx_helfer import Dok
from block1_b import STATUS
from block2_a import KOPF


def ls70_teil1(pfad):
    d = Dok(KOPF + " · LS 70", "LS 70 Lösungen Teil 1: Für Sicherheit und Nachhaltigkeit in der Logistik sorgen", STATUS)
    d.h2("Arbeitsblatt 70.1 Ideen zum ökologischen Aspekt der Nachhaltigkeit")
    d.tabelle(["", "Lager", "Transport", "Ressourceneinsatz"], [
        ["Hauptziel", "Energie- und Flächenverbrauch senken", "CO2-Emissionen je Transport senken",
         "Material und Verpackung reduzieren, Kreisläufe schließen"],
        ["Ideen", "LED-Beleuchtung mit Bewegungsmeldern; Photovoltaik auf dem Lagerdach; bessere Dämmung; kompaktes Layout und "
         "Mehrfachnutzung der Fläche; Gründach; Wärmerückgewinnung", "Elektrofahrzeuge für Zustellung in Städten; bessere Auslastung "
         "und Bündelung von Sendungen; Bahn statt Lkw auf langen Strecken; Routenoptimierung; Packstationen und Übergabestationen "
         "für die letzte Meile; Fahrertraining", "Mehrwegbehälter und Mehrwegverpackung; weniger und recyclingfähige Verpackung "
         "(Monomaterial); Rücknahme alter Räder und Batterien; Recyclingmaterial in der Produktion; Verschnitt vermeiden"],
    ], [2.4, 4.8, 4.9, 4.9])
    d.h2("Arbeitsblatt 70.2 Ideen zum sozialen Aspekt der Nachhaltigkeit")
    d.tabelle(["", "Mitarbeiter", "Arbeitsbedingungen", "Gesellschaft"], [
        ["Hauptziel", "Gesundheit, Qualifizierung und Beteiligung der Beschäftigten", "sichere, faire und gesunde Arbeit",
         "Verantwortung gegenüber Region und Lieferkette"],
        ["Ideen", "Ergonomische Arbeitsplätze und Hebehilfen; Schulungen und Weiterbildung; Mitsprache bei Verbesserungen; "
         "Gesundheitsangebote", "faire Entlohnung; planbare Schichten; Hitzeschutz und Pausenräume; Unterweisungen und Sicherheit; "
         "Entlastung durch Technik", "weniger Lärm und Verkehr für Anwohner; regionale Lieferanten; Einhaltung von Menschenrechten in "
         "der Lieferkette; Ausbildungsplätze; Kooperation mit Schulen"],
    ], [2.4, 4.8, 4.9, 4.9])
    d.h2("Arbeitsblatt 70.3 Ideen zum wirtschaftlichen Aspekt der Nachhaltigkeit")
    d.tabelle(["Kosten", "Wertschöpfung"], [
        ["Energie- und Materialkosten senken; weniger Abfall und Entsorgungskosten; Fördermittel nutzen; geringere Unfall- und "
         "Ausfallkosten; Investitionen mit Amortisationsrechnung", "Imagegewinn und Kundenbindung; neue Kunden mit Nachhaltigkeits"
         "anforderungen; Rücknahme und Wiederverkauf (Refurbish); höhere Attraktivität als Arbeitgeber; Lieferfähigkeit "
         "durch stabile Lieferketten"]], [8.5, 8.5])
    d.h2("Arbeitsblatt 70.4 Priorisierte Ideen und mögliche Herausforderungen")
    d.tabelle(["", "Ökologie", "Soziales", "Ökonomie"], [
        ["Kurzfristig", "LED und Bewegungsmelder im Lager", "Ergonomieschulung für das Lagerpersonal", "Energiekosten erfassen und überwachen"],
        ["Mittelfristig", "Zustellfahrzeuge schrittweise auf Elektro umstellen; Ladeinfrastruktur", "Gesundheits- und Qualifizierungsprogramm",
         "Wirtschaftlichkeitsrechnung und Fördermittel für Photovoltaik"],
        ["Langfristig", "Rücknahme- und Kreislaufkonzept für Räder und Batterien", "Verbindliche Sozialstandards in der Lieferkette",
         "Nachhaltigkeit als Verkaufsargument, neue Geschäftsfelder"],
        ["Hürden", "Investitionskosten, Platz und Strom für Ladeinfrastruktur, Rücknahmelogistik", "Akzeptanz, Zeit für Schulungen, Kontrolle bei Lieferanten",
         "Amortisationszeit, Preisdruck, Unsicherheit der Förderung"],
    ], [2.4, 4.8, 4.9, 4.9])
    d.p("Auswahl und Priorisierung sind individuell. Bewertet wird, ob Maßnahmen zum Zeithorizont passen und Hürden benannt werden. "
        "Rollenspiel (Auftrag 4): Gute Beiträge nennen Kosten, Machbarkeit und Folgen für Beschäftigte.")
    d.speichern(pfad)


ABFALL = [
    ("Lederreste (Sattelherstellung)", "Zuschnitt optimieren (Verschnittplanung), Lederqualität prüfen", "Reste für Kleinteile (zum Beispiel Griffe, Taschen) oder Verwertung als Lederfaser"),
    ("Überschüssige Lacke und Farben", "Bedarfsgerecht mischen, weniger Farbwechsel, wasserbasierte Lacke statt Lösemittellacke",
     "Rückführung in den Prozess, Rest als gefährlicher Abfall über zugelassenen Entsorger"),
    ("Kartonagen, Folien, Füllmaterial (Beschaffung)", "Mehrwegtransportverpackung, Rücknahme durch Lieferanten", "Getrennt sammeln (Papier, Folie) und recyceln, Füllmaterial wiederverwenden"),
    ("Nicht mehr funktionsfähige E-Bike-Batterien", "Langlebige Batterien, Reparatur, Zweitnutzung", "Rücknahmesystem und Recycling durch zertifizierte Entsorger; Gefahrgutregeln beachten"),
    ("Papier in der Verwaltung", "Digitalisierung (E-Rechnung, digitale Akte), beidseitig drucken", "Altpapier recyceln, datenschutzgerechte Vernichtung"),
    ("Gebrauchte Fahrräder (Rücknahme)", "Reparatur und Wiederverkauf (Refurbish), Ersatzteile", "Demontage und getrennte Verwertung (Metalle, Reifen, Elektronik)"),
    ("Elektronik und Peripheriegeräte (Verwaltung)", "Nutzungsdauer verlängern, aufarbeiten", "Rückgabe nach Elektrogerätegesetz, Daten sicher löschen"),
    ("Metallreste aus Stahl und Aluminium", "Zuschnitt optimieren, Reststücke verwenden", "Sortenrein sammeln und dem Metallrecycling zuführen"),
    ("Umverpackungen und Füllmaterial im Versand", "Mehrwegkartons, passgenaue Verpackung", "Recycling, Rückführung von Mehrwegverpackung"),
    ("Elektroteile zurückgegebener Fahrräder (Lampen, Tacho)", "Reparatur und Wiederverwendung als Ersatzteil", "Rückgabe nach Elektrogerätegesetz, Materialrecycling"),
    ("Druckerpatronen und Tonerkartuschen", "Weniger drucken, Nachfüllsysteme", "Rückgabe an Hersteller (Rücknahmeprogramm) oder Recycling"),
    ("Kunststoffreste (Spritzguss)", "Optimierte Werkzeuge, Heißkanalsystem, weniger Anguss", "Mahlgut im Betrieb wiederverwenden oder sortenrein zurückführen"),
]


def ls69_teil1(pfad):
    d = Dok(KOPF + " · LS 69", "LS 69 Lösungen Teil 1: Ein Entsorgungskonzept erstellen", STATUS)
    d.h2("Arbeitsblatt 69.1 Entsorgungskonzept der Fly Bike Werke GmbH")
    d.h3("Gesetzliche Grundlagen (Erwartung; Rechtsstand vor dem Einsatz prüfen)")
    d.punkte(["Kreislaufwirtschaftsgesetz mit Abfallhierarchie: Vermeidung, Vorbereitung zur Wiederverwendung, Recycling, sonstige "
              "Verwertung (zum Beispiel energetisch), Beseitigung",
              "Verpackungsgesetz (Systembeteiligung für Verkaufsverpackungen)",
              "Gewerbeabfallverordnung (Getrennthaltung gewerblicher Abfälle)",
              "Elektro- und Elektronikgerätegesetz und Batterierecht (Rücknahme, Entsorgung)",
              "Gefahrstoffverordnung, Regeln zu gefährlichen Abfällen und Nachweisen",
              "Landesrecht und kommunale Satzungen"])
    d.h3("Abfallarten und Maßnahmen (Beispiele zu den zwölf Haftnotizen)")
    d.tabelle(["Abfallart", "Vermeidung oder Wiederverwendung", "Verwertung"], [list(z) for z in ABFALL], [4.4, 6.3, 6.3], 9)
    d.h3("Personalorientierte Maßnahmen")
    d.punkte(["Unterweisung und Schulung zu Mülltrennung und Gefahrstoffen", "Umweltteam oder Abfallbeauftragte benennen",
              "Ideenmanagement mit Prämien für Vermeidungsvorschläge", "gut sichtbare Trennsysteme und Kennzeichnung",
              "Information in Betriebsversammlungen, Rückmeldung zu Erfolgen"])
    d.h3("Monitoring des Entsorgungskonzepts")
    d.punkte(["Kennzahlen: Abfallmenge je Produkt, Wiederverwertungsquote, Entsorgungskosten, Anteil gefährlicher Abfälle",
              "Soll-Ist-Vergleich mit festen Zielen und jährlicher Abfallbilanz",
              "regelmäßige Begehungen und Audits, Prüfung der Entsorgungsnachweise",
              "Verantwortliche und Termine festlegen, Auswertung im Meeting, Konzept anpassen"])
    d.h3("Vorwort (Präambel), Beispiel")
    d.p("Die Fly Bike Werke GmbH übernimmt Verantwortung für Umwelt und Gesellschaft. Wir vermeiden Abfälle, wo es möglich ist, "
        "verwerten, was sich nicht vermeiden lässt, und beseitigen nur, was nicht anders zu behandeln ist. Dabei beziehen wir alle "
        "Bereiche und Mitarbeitenden ein und überprüfen regelmäßig, ob wir unsere Ziele erreichen.")
    d.speichern(pfad)
