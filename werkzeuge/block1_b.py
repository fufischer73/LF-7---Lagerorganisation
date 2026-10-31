"""Block I, Teil B: Lösungen Teil 1 (Arbeitsblätter) für LS 64 und LS 65."""
from docx_helfer import Dok

KOPF = "LF 7 · Logistik- und Lagerprozesse · Industriekaufleute 2. Lehrjahr · Block I"
STATUS = ("Lösungsvorschlag (Entwurf). Bitte vor der Freigabe fachlich prüfen und mit dem Lösungsband des Verlags abgleichen. "
          "Bei offenen Aufgaben sind mehrere Lösungen möglich; die Beispiele sind Erwartungen, keine Musterlösung zum Abschreiben.")


def ls64_teil1(pfad):
    d = Dok(KOPF + " · LS 64", "LS 64 Lösungen Teil 1: Ein Logistikkonzept erstellen", STATUS)
    d.h2("Arbeitsblatt 64.1 Lieferbeziehungen der Fly Bike Werke GmbH")
    d.p("Verteilung der Lieferanten (Karte): In der Lernsituation stehen keine Orte. Zu erwarten ist eine begründete Annahme, "
        "zum Beispiel: Aluminium und Stahl aus Deutschland und Europa, Carbon und Elektronik (Dynamos, Beleuchtung, "
        "E-Bike-Batterien) aus Asien, Reifen und Bremsen von europäischen Zulieferern. Wichtig ist, dass zwischen regionalen und "
        "weit entfernten Lieferanten unterschieden wird und die Lieferwege erkennbar sind.")
    d.h3("Mögliche Problemfelder in der Zusammenarbeit mit den Lieferanten")
    d.punkte(["lange und schwankende Lieferzeiten, Lieferverzug (Seeweg, Zoll, Häfen)",
              "Transportrisiken: Schäden, Verlust, Verspätung",
              "Qualitätsschwankungen und Mengenabweichungen",
              "Abhängigkeit von einzelnen Lieferanten (Single Sourcing), Ausfall eines Lieferanten",
              "Preisschwankungen, Wechselkurse, steigende Frachtkosten",
              "Verständigung (Sprache, Zeitverschiebung), unterschiedliche Standards",
              "Nachhaltigkeit und Menschenrechte in der Lieferkette (Lieferkettensorgfaltspflichtengesetz)",
              "Peitscheneffekt: kleine Nachfrageschwankungen werden entlang der Kette immer größer"])
    d.h3("Mögliche Auswahlkriterien für Lieferanten")
    d.punkte(["Preis und Zahlungsbedingungen", "Qualität und Zertifizierungen", "Lieferzeit und Liefertreue (Verlässlichkeit)",
              "Flexibilität bei Menge und Termin", "Entfernung und Transportkosten", "Finanzielle Stabilität",
              "Nachhaltigkeit und Einhaltung von Sozial- und Umweltstandards",
              "Möglichkeit zu mehreren Lieferanten je Teil (Abhängigkeit vermeiden)"])
    d.h2("Arbeitsblatt 64.2 Maßnahmen für eine effizientere Lieferkette")
    d.tabelle(["Handlungsfeld", "Ziel", "Mögliche Maßnahmen"], [
        ["Lagerbestandsplanung", "Lieferfähig bleiben, ohne dass die Lager voll sind; Kapitalbindung und Lagerkosten senken",
         "Mindest-, Melde- und Sicherheitsbestände je Artikel festlegen; ABC-Analyse (teure und umsatzstarke Teile besonders "
         "eng steuern); Kanban oder Just-in-Time für Standardteile; Bestände der Lager Dresden und München abstimmen oder "
         "zusammenlegen; regelmäßige Bestandsüberwachung"],
        ["Prognose der Nachfrage", "Saisonale Schwankungen früh erkennen und Bestellungen darauf abstimmen",
         "Absatzdaten der Vorjahre und Saisonverläufe auswerten; Händler und Vertrieb in die Planung einbinden (Vorbestellungen, "
         "Händlermeldungen); Frühindikatoren (Wetter, Trends, Aktionen); statistische Prognoseverfahren und KI"],
        ["Einsatz von Technologie", "Transparenz und Geschwindigkeit in Warenfluss und Informationsfluss erhöhen",
         "IoT-Sensoren und RFID zur Verfolgung von Sendungen und Beständen; Lagerverwaltungssystem; elektronischer Datenaustausch "
         "mit Lieferanten (EDI, Lieferantenportal); KI für Prognose und Bestellvorschläge; Track-and-Trace"],
    ], [3.5, 5, 8.5])
    d.p("Die Pfeile zwischen den drei Feldern zeigen Wechselwirkungen. Erwartet wird, dass das begründet wird, zum Beispiel: "
        "Eine bessere Prognose erlaubt niedrigere Bestände; Technologie liefert die Daten für Prognose und Bestandsführung; "
        "geringere Bestände machen die Lieferkette empfindlicher gegen Lieferverzug und verlangen verlässlichere Lieferanten.")
    d.speichern(pfad)


LAGER = [  # Ware, Lagerart, Lagereinrichtung, Sicherheitshinweis
    ("Aluminium zur Rahmenherstellung", "geschlossen oder halboffen", "Kragarmregal (Langgut)", "Kippsicherung, Schnittschutz"),
    ("Carbon zur Herstellung der E-Bike-Rahmen", "geschlossen, trocken und temperiert", "Fachbodenregal oder Palettenregal",
     "Staubschutz bei Bearbeitung; Lagerbedingungen des Herstellers beachten"),
    ("Sand zum Abstrahlen der Rahmen", "halboffen oder geschlossen, trocken", "Big Bags auf Paletten, Bodenlagerung",
     "Feinstaub, Atemschutz; vor Feuchtigkeit schützen"),
    ("Schmiermittel", "geschlossen, Gefahrstofflager", "Gefahrstoffschrank mit Auffangwanne",
     "wassergefährdend, Auffangwanne, Kennzeichnung nach GHS"),
    ("Öl", "geschlossen, Gefahrstofflager", "Gefahrstoffschrank oder Fassregal mit Auffangwanne",
     "wassergefährdend, Brandschutz, Auffangwanne"),
    ("Lacke", "geschlossen, Gefahrstofflager", "Sicherheitsschrank für entzündbare Flüssigkeiten",
     "entzündbar, Brand- und Explosionsschutz, Lüftung, Zündquellen vermeiden, GHS-Kennzeichnung"),
    ("Gangschaltungen", "geschlossen", "Fachbodenregal", "Diebstahlschutz (hochwertig)"),
    ("Sättel", "geschlossen oder halboffen", "Fachbodenregal", "trocken lagern, Kratzschutz"),
    ("Softgriffe", "geschlossen", "Fachbodenregal oder Behälter", "vor Wärme und UV-Licht schützen"),
    ("Fahrradständer", "halboffen", "Palettenregal oder Bodenlagerung", "Stapelhöhe beachten"),
    ("Dynamos", "geschlossen, trocken", "Fachbodenregal", "vor Feuchtigkeit schützen"),
    ("Flügelschrauben", "geschlossen", "Kleinteilelager (Behälter, Schütten)", "Verwechslung vermeiden, getrennt nach Typen"),
    ("Fahrradkörbe", "halboffen", "Palettenregal oder Bodenlagerung", "sperrig, Beschädigungsschutz"),
    ("Reflektoren", "geschlossen", "Fachbodenregal", "Stoß- und Kratzschutz"),
    ("Rücklichter", "geschlossen", "Fachbodenregal", "Stoßschutz, Elektronik trocken lagern"),
    ("Fahrradglocken", "geschlossen", "Fachbodenregal oder Behälter", "Kleinteile, geordnet lagern"),
    ("Beleuchtung (Vorderlichter)", "geschlossen", "Fachbodenregal", "Stoßschutz, Elektronik trocken lagern"),
    ("Batterien für E-Bikes (Lithium-Ionen)", "geschlossen, eigener Brandabschnitt", "Spezialschrank oder Regal mit Brandschutz",
     "Gefahrgut (Klasse 9), Brandgefahr bei Beschädigung, Temperatur überwachen, geeignete Löschmittel, "
     "nicht vollgeladen lagern, schadhafte Batterien getrennt"),
    ("Treibstoffe für Maschinen (z. B. Diesel)", "offen mit Überdachung oder Gefahrstofflager", "doppelwandiger Tank oder Behälter",
     "wassergefährdend, Auffangwanne, Brandschutz, Zündquellen vermeiden"),
    ("Fahrradreifen von Zulieferern", "halboffen oder geschlossen", "Palettenregal, Reifenregal",
     "vor UV, Wärme und Ozon schützen; hohe Brandlast, Brandschutz beachten"),
    ("Fahrradketten und Getriebe", "geschlossen", "Fachbodenregal", "Korrosionsschutz, Ölreste: Rutschgefahr"),
    ("Kabel", "geschlossen", "Trommelregal oder Fachbodenregal", "Brandlast, Knickschutz"),
    ("Pedale", "geschlossen", "Fachbodenregal", "Kleinteile, geordnet"),
    ("Bremsen", "geschlossen", "Fachbodenregal", "Bremsflächen sauber und fettfrei halten"),
    ("Schutzbleche", "halboffen", "Palettenregal oder Bodenlagerung", "Kratzschutz, sperrig"),
]


def ls65_teil1(pfad):
    d = Dok(KOPF + " · LS 65", "LS 65 Lösungen Teil 1: Die Lagerhaltung planen", STATUS)
    d.h2("Arbeitsblatt 65.1 Bedarfsanalyse zur Erweiterung der Lagerflächen")
    d.p("Beispiel in der Vorlage: Stahl, offenes Lager, Bodenlagerung. Die Zuordnung ist begründbar unterschiedlich möglich. "
        "Entscheidend ist, dass der Schutzbedarf der Ware (Witterung, Brand, Umwelt, Diebstahl, Gesundheit) die Lagerart und "
        "Einrichtung bestimmt.")
    d.tabelle(["Ware", "Lagerart", "Lagereinrichtung", "Sicherheitshinweis"], [list(z) for z in LAGER], [4.2, 3.6, 4.2, 5.0], 9)
    d.h2("Arbeitsblatt 65.2 Planungsentwurf für die neuen Lagerflächen")
    d.p("Eine Musterskizze gibt es nicht, weil sich das Lager auf dem Grundstück unterschiedlich planen lässt. Ein Entwurf ist "
        "gut, wenn er diese Kriterien erfüllt (zugleich Bewertungshilfe):")
    d.punkte(["Der Materialfluss ist logisch: Wareneingang, Beschaffungslager, Fertigung I, Fertigung II und Endmontage, Absatzlager, "
              "Warenausgang, ohne lange Wege und ohne Kreuzungen.",
              "Wareneingang und Warenausgang haben jeweils eine eigene Zufahrt oder Rampe; die LKW-Zufahrt von der Straße ist "
              "sichergestellt.",
              "Gefahrstoffe (Lacke, Öle, Treibstoffe) und Lithium-Batterien liegen getrennt in eigenen Brandabschnitten, mit "
              "Abstand zu Verwaltungsgebäude und Mitarbeiterbereichen.",
              "Die Lagerplätze der Waren aus Arbeitsblatt 65.1 sind eingezeichnet und zu sinnvollen Gruppen zusammengefasst "
              "(zum Beispiel Gefahrstoffe, Kleinteile, sperrige Teile, Rahmenmaterial).",
              "Die Lagergröße ist begründet, Reserve für Wachstum ist bedacht.",
              "Fluchtwege, Verkehrswege für Stapler und Fußgänger und Feuerwehrzufahrt sind berücksichtigt."])
    d.h2("Arbeitsblatt 65.3 Vorschläge zur Kommissionierung")
    d.tabelle(["", "Beschaffungslogistik (Material für die Produktion)", "Distributionslogistik (Verkauf)"], [
        ["Materialien und Waren", "Rahmenmaterial, Kleinteile, Fremdbauteile (Schaltungen, Bremsen, Reifen), Lacke",
         "Eigene Erzeugnisse: Fahrräder und E-Bikes. Handelswaren: Zubehör, Bekleidung (zum Beispiel Shirts)"],
        ["Form der Kommissionierung", "auftragsbezogene Bereitstellung für die Montage (Materialsets je Fertigungsauftrag); "
         "Kleinteile über Kanban-Behälter; Person zur Ware bei vielen verschiedenen Teilen",
         "Eigene Erzeugnisse: einstufig, auftragsbezogen (wenige, große Positionen). Handelswaren: Person zur Ware, bei vielen "
         "Kleinaufträgen mehrstufig oder Sammelkommissionierung nach Zonen"],
        ["Hilfsmittel", "Pickliste oder mobiles Datengerät, Kommissionierwagen, Stapler, Barcode oder RFID zur Kontrolle",
         "Mobiles Datengerät oder Pick-by-Voice, Barcode-Scanner, Versandkartons und Verpackungsmaterial, Rollwagen"],
    ], [3.2, 6.9, 6.9])
    d.p("Auch andere Begründungen sind richtig, wenn sie zur Warenart, Auftragsstruktur und Artikelzahl passen.")
    d.speichern(pfad)
