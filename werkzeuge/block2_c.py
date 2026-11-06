"""Block II, Teil C: Lernatelier und Lösungen Teil 2 für LS 70 und LS 69."""
from docx_helfer import Dok
from block1_b import STATUS
from block1_c import lernatelier
from block2_a import KOPF

# Rechnungen LS 69, Aufgabe 5
LOG = [655.0, 682.4, 795.5, 762.5, 750.25, 752.8]
ENT = [245.5, 238.5, 220.9, 235.75, 199.75, 184.25]
ABF = [2650, 2725, 2585, 2430, 2200, 1950]
WV = [278, 276, 282, 295, 298, 287]
REL = [round(e / l * 100, 1) for e, l in zip(ENT, LOG)]
QUO = [round(w / a * 100, 1) for w, a in zip(WV, ABF)]
assert REL == [37.5, 35.0, 27.8, 30.9, 26.6, 24.5] and QUO == [10.5, 10.1, 10.9, 12.1, 13.5, 14.7]
assert abs(173.9 + 67.3 + 32.8 + 79.3 - 353.3) < 1e-6 and abs(506.5 + 179.1 + 175.9 + 152.6 - 1014.1) < 1e-6
P = ["Halbjahr 01/20X1", "02/20X1", "01/20X2", "02/20X2", "01/20X3", "02/20X3"]


def lernatelier_ls70(pfad):
    lernatelier(pfad, "LS 70", "Für Sicherheit und Nachhaltigkeit in der Logistik sorgen", "Seiten 132 bis 134",
        ("1, 2, 4, 6, 8", "Sie wollen Sicherheitszeichen, Gefahrensymbole, Ergonomie und die Unfallanzeige sicher können."),
        ("3, 5, 7, 9", "Sie vertiefen Gefahrguttransport, Unfallstatistik, Corporate Carbon Footprint und Datenschutz."),
        ("10 und Zusatzaufgaben", "Sie übertragen auf den Betrieb oder entwickeln eigene Lösungen."),
        [("Basis", "Sicherheitszeichen im Lager der Fly Bike Werke GmbH",
          "Ordnen Sie fünf Bereichen des neuen Lagers (Gefahrstofflager, Lithium-Batterien, Stapler-Verkehr, Laderampe, Büro) passende "
          "Sicherheitszeichen zu (Verbot, Gebot, Warnung, Brandschutz, Rettung) und begründen Sie jeweils kurz."),
         ("Plus", "Checkliste für eine Lagerbegehung (Kontrollieren, IHK-Katalog)",
          "Erstellen Sie für eine Lagerbegehung eine Checkliste mit mindestens zehn Prüfpunkten zu Lagervorschriften (zum Beispiel "
          "Fluchtwege, Kennzeichnung, Gefahrstofflagerung, Regalsicherheit, Ordnung, Löschmittel). Legen Sie fest, wer kontrolliert, "
          "wie oft und was bei einem Mangel passiert."),
         ("BNE: SDG 11", "Nachhaltige Stadtlogistik: die letzte Meile in Oldenburg",
          "Lesen Sie den Zeitungsartikel zur „letzten Meile“ in der Lernsituation. Entwickeln Sie ein Konzept für die Belieferung der Innenstadt "
          "(Packstationen, Elektrofahrzeuge, Lieferzonen, Bündelung). Beziehen Sie sich auf die Nachhaltigkeitsziele der UN "
          "(Ziel 11, besonders Verkehr und Umweltbelastung der Städte). Bewerten Sie das Konzept nach Ökologie, Sozialem und Ökonomie "
          "(Arbeitsblätter 70.1 bis 70.4) und nennen Sie Hürden."),
         ("Kreativ", "Die letzte Meile 2035",
          "Gestalten Sie ein Poster oder einen kurzen Pitch (3 Minuten): Wie sieht die Zustellung in Ihrer Stadt 2035 aus? "
          "Begründen Sie, welche Technik und welche Regeln dafür nötig sind.")])


def lernatelier_ls69(pfad):
    lernatelier(pfad, "LS 69", "Ein Entsorgungskonzept erstellen", "Seiten 123 bis 125",
        ("1, 3, 4, 6, 7, 9", "Sie wollen Abfallarten, Vermeidung, Verwertung und die Abfallhierarchie sicher können."),
        ("2, 5, 8, 10", "Sie vertiefen Recycling, Kennzahlen (Aufgabe 5), Rechtsgrundlagen und Datenauswertung."),
        ("Zusatzaufgaben", "Sie übertragen auf den Betrieb oder entwickeln eigene Lösungen."),
        [("Basis", "Abfallarten ordnen",
          "Ordnen Sie die zwölf Haftnotizen der Lernsituation den Gruppen Produktionsabfall, Verpackung, Elektro- und Elektronikschrott, "
          "Gefahrstoff und Rücknahmeprodukt zu. Kennzeichnen Sie, welche Abfälle gefährlich sind und deshalb besondere Regeln brauchen."),
         ("BNE: SDG 6", "Sauberes Wasser: Lacke und Gewässerschutz",
          "In der Lackiererei der Fly Bike Werke GmbH werden überschüssige Lacke und Farben aufgefangen. a) Welche Stoffe in Lacken "
          "und Reinigern können Gewässer gefährden? b) Welche Regeln gelten für den Umgang mit wassergefährdenden Stoffen und "
          "Abwasser (zum Beispiel Wasserhaushaltsgesetz, Gefahrstoffrecht)? c) Entwickeln Sie Maßnahmen, damit nichts ins Abwasser "
          "gelangt (Auffangwannen, Annahme und Entsorgung, wasserbasierte Lacke, Schulung). Beziehen Sie sich auf das "
          "Nachhaltigkeitsziel 6 (Wasserqualität verbessern, Verschmutzung verringern) und ergänzen Sie die Ergebnisse in Ihrem "
          "Entsorgungskonzept."),
         ("Plus", "Kennzahlen-Cockpit für das Monitoring",
          "Entwickeln Sie für das Entsorgungskonzept ein Kennzahlen-Cockpit (OnlyOffice-Tabellenkalkulation) mit mindestens vier "
          "Kennzahlen (zum Beispiel Abfallmenge je Produkt, Wiederverwertungsquote, relative Entsorgungskosten, Anteil gefährlicher "
          "Abfälle). Tragen Sie Beispielwerte aus Aufgabe 5 ein und berechnen Sie die Kennzahlen mit Formeln. Legen Sie Zielwerte fest."),
         ("Kreativ", "Kampagne für die Belegschaft",
          "Gestalten Sie eine kurze Kampagne (Plakat, Kurztext oder Video), die Mitarbeitende zum Vermeiden und Trennen von Abfall "
          "motiviert. Benennen Sie Zielgruppe, Botschaft und einen Weg, den Erfolg zu messen.")])


def loesungen_ls70_teil2(pfad):
    d = Dok(KOPF + " · LS 70", "LS 70 Lösungen Teil 2: Aufgaben 1 bis 10 und Zusatzaufgaben", STATUS)
    d.p("Aufgaben mit Recherche im Betrieb (1 b, 3, 5 d und e, 10) haben keine Einheitslösung.", kursiv=True)
    L = [
     ("Aufgabe 1", "a) Warnzeichen: Hinweis auf Gefahren (gelbes Dreieck, zum Beispiel Rutsch- oder Stolpergefahr). Gebotszeichen: "
      "Hinweis auf Schutz- oder Vorsichtsmaßnahmen (blauer Kreis, zum Beispiel Kopfschutz tragen). Gefahrensymbol (GHS): Warnung "
      "vor der Folge oder Wirkung eines Stoffes (rote Raute). Brandschutzzeichen: Handlungsempfehlungen zur Brandbekämpfung (rotes "
      "Zeichen, zum Beispiel Feuermelder). Verbotszeichen: Hinweis auf nicht erlaubte Handlungen (roter Kreis mit Strich, zum "
      "Beispiel Zutritt verboten). Rettungszeichen: Hinweis auf Fluchtwege und Notausgänge (grünes Zeichen). Die Symbole im Heft "
      "den Zeilen zuordnen. b) Individuell."),
     ("Aufgabe 2", "Symbole im Heft prüfen. Flamme: entzündbarer Stoff, von Zündquellen fernhalten, nicht rauchen, in "
      "Sicherheitsschrank lagern, Löschmittel bereithalten. Ätzwirkung: Haut- und Augenkontakt vermeiden, Schutzhandschuhe und "
      "-brille tragen, Augenspülung und Erste Hilfe bereithalten, in Auffangwanne lagern. Umwelt (toter Baum, Fisch): nicht in "
      "Gewässer oder Kanalisation gelangen lassen, Auffangwanne, Leckagen sofort aufnehmen, ordnungsgemäß entsorgen."),
     ("Aufgabe 3", "Individuell. Zu erwarten: Beförderung nach ADR, Gefahrgutbeauftragter, Kennzeichnung (orangefarbene Tafeln, "
      "Gefahrzettel, UN-Nummer), Beförderungspapier, Schulung des Fahrers, Ladungssicherung, Feuerlöscher."),
     ("Aufgabe 4", "a) Gesundheit (Rücken, Gelenke), weniger Ausfälle, höhere Produktivität und Qualität, gesetzliche Pflichten "
      "(Arbeitsschutz, Lastenhandhabung). b) Hubwagen und Hubtische, Rollwagen, Regalhöhen im Greifbereich (schwere Teile unten), "
      "richtige Hebetechnik, Wechsel der Tätigkeiten, ergonomische Arbeitshöhe. c) Weniger Krankheitstage, bessere Stimmung, "
      "geringere Fehlerquote und weniger Unfälle."),
     ("Aufgabe 5", "a) Menschliche Fehler (Zeitdruck, Routine, mangelnde Unterweisung) lösen Unfälle oft aus; die Ursachen liegen aber "
      "häufig in Organisation, Arbeitsplatzgestaltung und Schutzmitteln. b) Nach der Tabelle betreffen die Unfälle vor allem Paletten "
      "(12 237 von 35 533, 34,4 %) und verschiedene Verpackungen (14 224, 40,0 %), dazu Regalsysteme (2 057, 5,8 %). Als Hauptgründe "
      "kommen manuelles Handhaben, Heben, Stapeln, Umkippen und Verletzungen an beschädigten Paletten und Behältnissen in Betracht. "
      "c) Unterweisungen, Hilfsmittel, Prüfung der Paletten, Ordnung und Kennzeichnung, Schutzausrüstung. d) und e) Individuell."),
     ("Aufgabe 6", "a) Der Unternehmer bzw. die Unternehmerin. b) Bei Arbeits- und Wegeunfällen, wenn eine Person getötet oder so "
      "verletzt wird, dass sie mehr als drei Kalendertage arbeitsunfähig ist. c) An den zuständigen Unfallversicherungsträger "
      "(Berufsgenossenschaft oder Unfallkasse). d) Innerhalb von drei Tagen, nachdem man vom Unfall Kenntnis erlangt hat. "
      "Verfahren (zum Beispiel Online-Meldung) und Fristen vor dem Einsatz bei der Berufsgenossenschaft prüfen."),
     ("Aufgabe 7", "Der Corporate Carbon Footprint ist die Treibhausgasbilanz eines Unternehmens (in CO2-Äquivalenten). a) Er macht "
      "Emissionen sichtbar, zeigt Schwachstellen, erlaubt Ziele und Vergleiche. b) Nachteile: Aufwand und Kosten, schwierige "
      "Datenlage (Lieferkette), nur CO2 statt aller ökologischen und sozialen Wirkungen, Risiko schönender Darstellung. "
      "c) Elektrofahrzeuge, Routenoptimierung, Bündelung, Ökostrom, LED, Mehrwegverpackung, Bahn statt Lkw, Photovoltaik."),
     ("Aufgabe 8", "Mögliche Argumentation: a) Nicht grundsätzlich: Investitionen kosten zunächst, senken aber oft Energie- und "
      "Materialkosten, dazu Förderprogramme. b) Nicht immer: Kosten können durch Effizienz aufgefangen werden; teils bezahlt der Kunde "
      "mehr, teils nicht. c) Gewinnstreben und soziale Gerechtigkeit stehen im Konflikt, ergänzen sich aber auch: Gute Arbeits"
      "bedingungen steigern Motivation und Produktivität; Rahmenbedingungen und Regeln sind wichtig."),
     ("Aufgabe 9", "a) Datenschutz schützt personenbezogene Daten (DSGVO, BDSG); Verstöße können hohe Bußgelder und Vertrauensverlust "
      "bedeuten. b) Situation 1 (Lieferscheine): zulässig, soweit die Daten für die Vertragsabwicklung nötig sind; Datensparsamkeit "
      "und Löschfristen. Situation 2 (GPS-Tracking): nur mit berechtigtem Interesse, Transparenz, Verhältnismäßigkeit und "
      "Mitbestimmung des Betriebsrats; keine ständige Leistungskontrolle; Privatfahrten ausschließen. Situation 3 (Videoüberwachung "
      "im Lager): nur bei berechtigtem Interesse (zum Beispiel Diebstahlschutz), mit Hinweisschildern, begrenzter Speicherdauer, "
      "ohne Überwachung von Pausen- und Sozialräumen, mit Betriebsrat. Rechtliche Bewertung im Einzelfall."),
     ("Aufgabe 10", "Individuell."),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Basis: Sicherheitszeichen im Lager", "Gefahrstofflager: Warnzeichen entzündbar, Verbot offenes Feuer, Gebot Schutzbrille/Handschuhe. "
         "Lithium-Batterien: Warnzeichen Brandgefahr, Brandschutzzeichen, Verbot Wasser/Zündquellen je nach Lagerkonzept. Staplerverkehr: "
         "Warnzeichen Flurförderzeuge, Gebot Warnweste. Laderampe: Warnzeichen Absturzgefahr, Gebot Sicherheitsschuhe. Büro: Rettungszeichen, "
         "Feuerlöscher."],
        ["Plus: Checkliste Lagerbegehung", "Mindestens zehn sinnvolle Prüfpunkte (zum Beispiel Fluchtwege frei, Sicherheitszeichen "
         "sichtbar, Gefahrstoffe getrennt und gekennzeichnet, Auffangwannen vorhanden, Regalprüfung, Paletten unbeschädigt, Löschmittel "
         "geprüft, Ordnung, Beleuchtung), klare Zuständigkeit, Rhythmus und Maßnahmen bei Mängeln."],
        ["BNE: SDG 11, Stadtlogistik", "Konzept mit Packstationen, Mikro-Depots oder Übergabestationen, Elektro- oder Lastenrad-Zustellung, "
         "Lieferzonen mit festen Zeitfenstern, Bündelung. Bewertung nach Ökologie (Emissionen, Lärm), Soziales (Anwohner, Beschäftigte) "
         "und Ökonomie (Kosten, Auslastung). Hürden: Fläche, Kommune, Kosten, Akzeptanz. Bezug zu Ziel 11 (Verkehr, Umweltbelastung)."],
        ["Kreativ: Die letzte Meile 2035", "Kriterien: realistisch und begründet, Technik und Regeln benannt, verständlich präsentiert."],
    ], [4.0, 13.0])
    d.speichern(pfad)


def loesungen_ls69_teil2(pfad):
    d = Dok(KOPF + " · LS 69", "LS 69 Lösungen Teil 2: Aufgaben 1 bis 10 und Zusatzaufgaben", STATUS)
    d.p("Aufgaben mit Recherche im Betrieb (1, 3, 8 b) haben keine Einheitslösung.", kursiv=True)
    tab = [[P[i], f"{LOG[i]:g}", f"{ENT[i]:g}", f"{REL[i]:.1f} %", f"{ABF[i]}", f"{WV[i]}", f"{QUO[i]:.1f} %".replace(".", ",")]
           for i in range(6)]
    tab = [[r[0], r[1].replace(".", ","), r[2].replace(".", ","), r[3].replace(".", ","), r[4], r[5], r[6]] for r in tab]
    L = [
     ("Aufgabe 1", "Individuell: Abfälle aus Produktion und Verwaltung des Ausbildungsbetriebs; Vermeidung und Verwertung nach Abfallhierarchie."),
     ("Aufgabe 2", "a) Ressourcen sind knapp, Gesetze verpflichten Unternehmen (Produktverantwortung), Entsorgung kostet, Kunden und "
      "Öffentlichkeit erwarten Verantwortung. b) Nach der Infografik nutzte Deutschland 2023 etwa 13,9 % recycelte Rohstoffe, "
      "+1,4 Prozentpunkte gegenüber 2022, über dem EU-Schnitt von 11,8 %; Spitzenreiter ist die Niederlande mit 30,6 %. Damit "
      "stammt der überwiegende Teil der Rohstoffe weiterhin aus Primärquellen. c) Gründe: Qualität und Reinheit von Sekundär"
      "rohstoffen, Sortierung bei Verbundstoffen, niedrige Preise von Neumaterial, fehlende Infrastruktur, nicht recycling"
      "gerechtes Produktdesign, Kosten. (Zahlen im Heft prüfen.)"),
     ("Aufgabe 3", "Beispiele Fly Bike Werke GmbH: Beschaffung: Kartonagen, Folien, Paletten. Produktion: Metall-, Leder-, "
      "Kunststoff- und Lackreste. Distribution: Umverpackungen, zurückgenommene Räder und Batterien. Ausbildungsunternehmen: individuell."),
     ("Aufgabe 4", "a) Mehrwegtransportverpackung (Paletten, Behälter), Rückgabe an den Lieferanten, Pfand, bessere Stapelbarkeit. "
      "b) Umverpackung: weniger Material, ein Werkstoff, recyclingfähig, passgenau, Mehrweg. c) Verkaufsverpackung: Verpackungsgesetz "
      "beachten (Systembeteiligung), Material reduzieren, recyclingfähig gestalten. Rechtsstand (zum Beispiel EU-Verpackungsregeln) prüfen."),
     ("Aufgabe 5", "a) Relative Entsorgungskosten (Entsorgungskosten : Logistikkosten): " + "; ".join(f"{P[i]}: {REL[i]:.1f} %".replace(".", ",") for i in range(6)) +
      ". b) Wiederverwertungsquote (wiederverwertet : Abfall): " + "; ".join(f"{P[i]}: {QUO[i]:.1f} %".replace(".", ",") for i in range(6)) +
      ". c) Die Abfallmenge sank von 2 650 kg auf 1 950 kg (−26,4 %), die Entsorgungskosten von 245,5 auf 184,25 TEUR (−24,9 %) und "
      "ihr Anteil an den Logistikkosten von 37,5 % auf 24,5 %, und das bei steigendem Absatz. Die Wiederverwertungsquote stieg von "
      "10,5 % auf 14,7 %, bleibt aber niedrig. Die Bemühungen wirken, sollten aber stärker auf Verwertung zielen."),
     ("Aufgabe 6", "a) Quantitativ: weniger Material einsetzen, Verschnitt vermeiden, Prozesse optimieren, Mehrweg. b) Qualitativ: "
      "Schadstoffe ersetzen oder verringern, gefährliche Stoffe durch unbedenklichere ersetzen, Produkte langlebig und reparierbar machen "
      "(zum Beispiel wasserbasierte statt lösemittelhaltiger Lacke)."),
     ("Aufgabe 7", "Stoffliche Verwertung: Der Abfall wird zu Rohstoff aufbereitet (Recycling), zum Beispiel Altglas oder Altmetall zu "
      "neuem Glas bzw. Metall. Energetische Verwertung: Der Abfall wird verbrannt, die Energie als Strom oder Wärme genutzt, zum "
      "Beispiel Restmüll oder Altholz."),
     ("Aufgabe 8", "a) Zum Beispiel Verpackungsgesetz, Gewerbeabfallverordnung, Elektrogerätegesetz, Batterierecht, Gefahrstoffverordnung, "
      "Nachweisverordnung, Landesabfallrecht und kommunale Satzungen. Rechtsstand prüfen. b) Individuell."),
     ("Aufgabe 9", "Geeignete Behälter und Kennzeichnung, Trennung der Abfallarten, Gefahrstoffe in Auffangwannen und Brandschutz, "
      "begrenzte Lagerdauer und Mengen, Zugangsschutz, Dokumentation der Entsorgungsnachweise, Platzbedarf und Hygiene, Kosten."),
     ("Aufgabe 10", "Nach der Grafik wurden 2019 von 353,3 Mio. t Plastikmüll nur 9,3 % recycelt (32,8 Mio. t), 49,2 % deponiert, "
      "19,0 % verbrannt und 22,4 % missgewirtschaftet. Bis 2060 wird mit 1 014,1 Mio. t (rund das 2,9-Fache) gerechnet; "
      "der Recyclinganteil steigt auf nur 17,3 %. Die Treibhausgase aus der Verbrennung (140 Mio. t, später 340 Mio. t CO2-"
      "Äquivalente) sind am größten, doch jeder Weg erzeugt Umweltwirkungen. Weil jede Behandlung Folgen hat, ist Vermeiden "
      "der wirksamste Hebel: Deshalb steht Vermeidung vor Verwertung und Beseitigung. (Werte im Heft prüfen.)"),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h3("Aufgabe 5: Tabelle der Ergebnisse")
    d.tabelle(["Halbjahr", "Logistik (TEUR)", "Entsorgung (TEUR)", "Entsorgung relativ", "Abfall (kg)", "Wiederverwertet (kg)", "Quote"], tab,
              [3.0, 2.2, 2.4, 2.4, 2.0, 2.6, 2.0], 9)
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Basis: Abfallarten ordnen", "Produktionsabfall: Lederreste, Metallreste, Kunststoffreste, Lackreste. Verpackung: Kartonagen, "
         "Folien, Umverpackungen, Füllmaterial. Elektro- und Elektronikschrott: Peripheriegeräte, Elektroteile, Druckerpatronen. Rücknahmeprodukte: "
         "Batterien, Fahrräder. Gefährlich: Lacke und Farben, Batterien, Druckerpatronen (Resttoner). Papier gehört in die Gruppe "
         "Verwaltung/Papier."],
        ["BNE: SDG 6, Lackabwasser", "a) Lösemittel, Schwermetalle in Pigmenten, Additive, Reiniger gefährden Gewässer. b) Wasserhaushaltsgesetz "
         "und Anlagenverordnung für den Umgang mit wassergefährdenden Stoffen, Abwasserrecht (Einleitung nur mit Genehmigung), "
         "Gefahrstoffrecht, Vorgaben zu gefährlichen Abfällen. c) Auffangwannen und dichte Böden, Lackschlamm als gefährlichen Abfall "
         "entsorgen, kein Ausspülen in die Kanalisation, wasserbasierte Lacke, Schulung, regelmäßige Kontrollen, Notfallplan. Bezug "
         "zu Ziel 6: Wasserqualität verbessern, Verschmutzung verringern."],
        ["Plus: Kennzahlen-Cockpit", "Vier Kennzahlen mit Formeln (zum Beispiel Wiederverwertungsquote = wiederverwertet : Abfall), "
         "Zielwerte, Ampelfarben oder Diagramm, Werte aus Aufgabe 5."],
        ["Kreativ: Kampagne", "Kriterien: klare Botschaft, passende Zielgruppe, einfache Handlungen, Messung des Erfolgs."],
    ], [4.0, 13.0])
    d.speichern(pfad)
