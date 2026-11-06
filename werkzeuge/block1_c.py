"""Block I, Teil C: Lernatelier (Zusatzaufgaben) und Lösungen Teil 2 für LS 64 und LS 65."""
from docx_helfer import Dok
from block1_b import KOPF, STATUS

# --- Rechnungen werden hier geprüft, damit die Lösungen stimmen
KANBAN = 100 * 5 * (100 + 20) / (50 * 100)           # 600 Stück / 6 Tage; Lieferzeit 2 + 3 Tage; Puffer 20 %; 50 Stück je Behälter
assert abs(KANBAN - 12.0) < 1e-9
KOMM = 3 + 6 + 0.5 + 1                                 # Basis + Weg + Greif + Tot
assert KOMM == 10.5 and int(480 // KOMM) == 45
BRUTTO = 450 + 450 * 0.2 + 50
assert BRUTTO == 590


def lernatelier(pfad, ls, titel, buch_seiten, basis, plus, kreativ, zusatz):
    d = Dok(KOPF + f" · {ls}", f"Lernatelier {ls}: {titel}")
    d.p("Sie entscheiden selbst, was Sie üben. Wählen Sie die Aufgaben nach Ihrem Stand (Kann-Liste), nicht alle sind nötig. "
        "Die Lösungen finden Sie in „Lösungen Teil 2“. Ergänzend gibt es Aufgaben zu BNE und zum IHK-Prüfungskatalog.", kursiv=True)
    d.h2(f"Aufgaben aus dem Arbeitsheft ({buch_seiten})")
    d.tabelle(["Niveau", "Empfohlene Aufgaben", "Für wen?"], [
        ["Basis", basis[0], basis[1]], ["Plus", plus[0], plus[1]], ["Kreativ und Transfer", kreativ[0], kreativ[1]]], [3.2, 5.6, 8.2])
    d.p("Aufgaben mit „Recherchieren Sie in Ihrem Ausbildungsunternehmen …“ bearbeiten Sie im Betrieb oder mit Unterlagen aus "
        "dem Betrieb; achten Sie dabei auf Datenschutz und Betriebsgeheimnisse.", kursiv=True)
    d.h2("Zusatzaufgaben")
    for niv, t, aufg in zusatz:
        d.h3(f"{niv}: {t}")
        d.p(aufg)
    d.speichern(pfad)


def lernatelier_ls64(pfad):
    lernatelier(pfad, "LS 64", "Ein Logistikkonzept erstellen", "Seiten 77 bis 79",
        ("1, 2, 3, 6, 13", "Sie wollen Warenfluss, 7-R-Regel und Push/Pull sicher können."),
        ("4, 5, 7, 10, 12, 14", "Sie können die Grundlagen und wollen Zusammenhänge, Rechnungen (Kanban) und Rechtliches vertiefen."),
        ("8, 9, 11, 15 und Zusatzaufgaben", "Sie übertragen auf den Betrieb oder entwickeln eigene Lösungen."),
        [("Basis", "Info-Blatt 4.2: Just-in-Time und Just-in-Sequence (IHK-Katalog)",
          "Lesen Sie das Info-Blatt „Just-in-Time vs. Just-in-Sequence“ (Ergänzendes Material).\na) Erklären Sie beide Verfahren in eigenen Worten.\n"
          "b) Ordnen Sie zu, ob Just-in-Time oder Just-in-Sequence passt: Sitze für verschieden ausgestattete Autos, Schrauben, "
          "Außenspiegel in Wunschfarbe, einfache Standardteile. Nennen Sie je ein weiteres Beispiel aus Industrie oder Handel.\n"
          "c) Warum ist die Reihenfolge der Lieferung bei vielen Varianten so wichtig?"),
         ("Plus", "Passt Just-in-Time zur Fly Bike Werke GmbH?",
          "Die Fly Bike Werke GmbH erwägt, einzelne Teile per Just-in-Time zu beziehen. Prüfen Sie für drei Teile (zum Beispiel "
          "Flügelschrauben, Aluminiumrohre aus Deutschland, E-Bike-Batterien aus Asien), ob Just-in-Time oder ein Sicherheitsbestand "
          "besser passt. Beziehen Sie Lieferzeit, Verlässlichkeit des Lieferanten, Nachfrageschwankung und Kosten ein und geben Sie eine "
          "begründete Empfehlung ab. Prüfen Sie, ob Just-in-Sequence in der Endmontage sinnvoll wäre."),
         ("Kreativ", "Erklärbild oder Kurzvideo „JIT oder JIS?“",
          "Erstellen Sie in OnlyOffice (Präsentationseditor) eine Infografik oder ein kurzes Erklärvideo (höchstens 3 Minuten), das "
          "Mitschülern den Unterschied zwischen Just-in-Time und Just-in-Sequence an einem eigenen Beispiel erklärt."),
         ("BNE", "Lieferkette und Verantwortung",
          "Das Lieferkettensorgfaltspflichtengesetz verlangt von Unternehmen, auf Menschenrechte und Umweltstandards in der "
          "Lieferkette zu achten. Überlege, welche Auswirkungen das auf die Lieferantenauswahl der Fly Bike Werke GmbH hat. Welche "
          "Zielkonflikte entstehen (Preis, Liefersicherheit, Verantwortung)?")])


def lernatelier_ls65(pfad):
    lernatelier(pfad, "LS 65", "Die Lagerhaltung planen", "Seiten 84 bis 88",
        ("2, 4, 5, 6, 13, 16, 18, 20", "Sie wollen Lagerfunktionen, Wareneingang und Lagerformen sicher können."),
        ("7, 10, 11, 15, 17, 19, 23", "Sie vertiefen Kommissionierung, Flächenberechnung und Entscheidungen."),
        ("8, 9, 14, 21, 22, 24 und Zusatzaufgaben", "Sie übertragen auf den Betrieb oder entwickeln eigene Lösungen."),
        [("Basis", "Fachartikel „Erfolgsfaktor Kommissionierung“ (Ergänzendes Material)",
          "Lesen Sie den Fachartikel und beantworten Sie: a) Warum spielt die Kommissionierung für den Markterfolg eine Schlüsselrolle? "
          "b) Vergleichen Sie „Mann zur Ware“ und „Ware zum Mann“ nach Investitionen, Personalbedarf, Fehleranfälligkeit und Eignung. "
          "c) Erklären Sie Festplatzsystem und Freiplatzsystem und nennen Sie einen Vor- und einen Nachteil des Freiplatzsystems. "
          "d) Wie helfen „Ziffern statt Wörter“ und die GTIN-Codierung, Kommissionierfehler zu vermeiden?"),
         ("Plus", "Zentral, dezentral oder beides? Die drei Lager der Fly Bike Werke GmbH",
          "Die Fly Bike Werke GmbH hat Lager am Stammsitz, in Dresden und in München. Nutzen Sie Ihre Ergebnisse aus LS 64 (hohe "
          "Bestände, Nachfrageschwankung) und LS 65. Soll das neue Lager am Stammsitz die Lager in Dresden und München ersetzen, "
          "ergänzen oder bleiben diese bestehen? Vergleichen Sie Kosten, Lieferzeit zu den Händlern, Bestände und Sicherheit und geben Sie "
          "eine begründete Empfehlung ab."),
         ("Kreativ", "Lagerlayout digital und maßstabsgetreu",
          "Zeichnen Sie das Layout des neuen Lagers im OnlyOffice-Präsentationseditor mit Formen und Pfeilen. Markieren Sie Warenfluss, "
          "Gefahrstoffbereich, Kleinteilelager, Rampen und Fluchtwege. Präsentieren Sie Ihr Layout in drei Minuten."),
         ("BNE", "Nachhaltige Lagerplanung",
          "Wie kann die Lagerplanung ressourcenschonend sein (Energie, Flächenverbrauch, Verpackung, Mehrwegbehälter)? "
          "Schlagen Sie drei Maßnahmen für das neue Lager vor und bewerten Sie sie nach Kosten und Umweltwirkung.")])


def loesungen_ls64_teil2(pfad):
    d = Dok(KOPF + " · LS 64", "LS 64 Lösungen Teil 2: Aufgaben 1 bis 15 und Zusatzaufgaben", STATUS)
    d.p("Aufgaben, bei denen im Ausbildungsunternehmen recherchiert wird (1, 8, 9, 11, 15), haben keine Einheitslösung; "
        "Erwartungen stehen stichwortartig dabei.", kursiv=True)
    L = [
     ("Aufgabe 1", "Individuelle Skizze des Warenflusses vom Wareneingang bis zum Versand (Wareneingang, Lager, ggf. Produktion, "
      "Warenausgang, Kunde). b) Mögliche Maßnahmen: Lagerverwaltungssystem, kürzere Wege, Barcodescanner, feste Abläufe, "
      "Bestandskontrolle."),
     ("Aufgabe 2", "Jede Schnittstelle (zum Beispiel Einkauf zu Lager, Lager zu Versand) kann Zeit, Informationen und Qualität "
      "verlieren: Wartezeiten, Doppelerfassungen, Fehler, Mehrkosten, Verzögerungen für den Kunden. Wer Schnittstellen verkleinert "
      "oder abstimmt, verkürzt Durchlaufzeiten und senkt Kosten."),
     ("Aufgabe 3 a)", "Reihenfolge der Teilprozesse: Kunde bestellt, Ware wird beim Lieferanten bestellt, Ware wird geliefert, "
      "Wareneingangskontrolle, Wareneingang wird erfasst, Ware wird dem Lager entnommen, Warenentnahme wird erfasst, "
      "Warenausgangskontrolle, Ware wird an den Kunden versandt. Informationsfluss: Bestellung vom Kunden an die Papierkontor GmbH "
      "und von dort an die Lieferanten, Erfassung der Wareneingänge und -entnahmen. Warenfluss: von den Lieferanten über das "
      "Unternehmen zum Kunden."),
     ("Aufgabe 4", "a) Warenflüsse: Hersteller zum zentralen Lager, zentrales Lager zu den Verteilzentren, Verteilzentren zu den "
      "Einzelhändlern. Informationsflüsse: Bestellungen entgegengesetzt, Lieferavise, Bestandsmeldungen, Rechnungen. b) Eine "
      "effiziente Steuerung der Informationen schafft Transparenz über Bestände und Bedarfe und vermeidet Über- und Unterbestände "
      "sowie Verzögerungen. c) Einsatzgebiete für KI: Absatzprognose, Bestellvorschläge, Routenplanung, Erkennen von "
      "Auffälligkeiten (Lieferverzug), automatisches Lesen von Lieferscheinen, Chatbots für Statusanfragen, Lieferantenbewertung."),
     ("Aufgabe 5", "Beispielnetzwerk: Optimaler Warenfluss senkt Durchlaufzeit (−); kürzere Durchlaufzeit erhöht Kundenzufriedenheit (+); "
      "Kundenzufriedenheit erhöht Nachfrage (+) und Umsatz (+); hoher Umsatz bei gleichen Kosten erhöht Gewinn (+); Mitarbeitermotivation "
      "verbessert Qualität (+) und senkt Fehler (−). Bewertet wird, ob die Beziehungen sinnvoll und mit + oder − richtig "
      "gekennzeichnet sind."),
     ("Aufgabe 6", "7-R-Regel (Wortlaut bitte mit dem Buch abgleichen): 1 richtige Ware (Beispiel in der Aufgabe), 2 richtige Menge "
      "(zu wenig: Lieferverzug, zu viel: Kapitalbindung), 3 richtige Qualität bzw. richtiger Zustand (Reklamationen, Rücksendungen), "
      "4 richtiger Ort (Falschlieferung, Mehrkosten), 5 richtige Zeit (Verspätung, Produktionsstillstand, Vertragsstrafe), "
      "6 richtiger Kunde (Verwechslung, Datenschutz, Schadenersatz), 7 richtige Kosten (zu teure Logistik, nicht wettbewerbsfähig)."),
     ("Aufgabe 7", "a) Beschaffung: niedriger Einkaufspreis durch große Mengen gegen geringe Kapitalbindung und Lagerkosten; "
      "Liefersicherheit gegen Preis. b) Lagerhaltung: hohe Lieferbereitschaft (viel Bestand) gegen niedrige Lagerkosten. "
      "c) Distribution: schnelle Lieferung gegen niedrige Transportkosten, Servicequalität gegen Kosten."),
     ("Aufgabe 8", "Individuell: Beschreibung der Organisation (zentral oder dezentral, eigene oder externe Logistik, Systeme)."),
     ("Aufgabe 9", "Individuell: interne Kette (Wareneingang, Lager, Produktion, Versand) und externe Kette (Lieferanten, Spedition, Kunden)."),
     ("Aufgabe 10", "a) Vorteile Outsourcing: Fixkosten werden zu variablen Kosten, Konzentration auf das Kerngeschäft, Spezialwissen "
      "und größere Flexibilität des Dienstleisters, keine eigenen Investitionen. b) ba Transportlogistik im Absatzbereich: "
      "Abhängigkeit vom Dienstleister, weniger Kontrolle über Lieferzeit und Qualität, Verlust des direkten Kundenkontakts, "
      "Imagerisiko bei Fehlern. bb Lagerhaltung: Abhängigkeit, geringere Reaktionsgeschwindigkeit, Datenschutz und Sicherheit der "
      "Bestände, Know-how-Verlust, Kosten bei Vertragsende."),
     ("Aufgabe 11", "Individuell: ausgelagerte Bereiche im Betrieb (zum Beispiel Transport, Lagerung, Verpackung, IT)."),
     ("Aufgabe 12", "Hinweis: Rechtsstand zum Lieferkettensorgfaltspflichtengesetz vor dem Einsatz prüfen, weil es Änderungen und "
      "EU-Vorhaben gibt. a) Ziele: Menschenrechte (zum Beispiel kein Kinder- oder Zwangsarbeit) und Umweltschutz entlang der "
      "Lieferkette sichern, Risiken erkennen und mindern, Transparenz schaffen. b) Herausforderungen: viele Stufen und "
      "Lieferanten, geringe Einsicht in tiefere Stufen, Aufwand für Risikoanalyse und Dokumentation, Kosten, Konflikt mit "
      "Preis und Lieferzeit, Wettbewerbsnachteile."),
     ("Aufgabe 13", "a) „Asian Taste“ bereitet nach Bestellung zu und folgt dem Pull-Prinzip (Produktion auf Kundenbestellung). "
      "„TakeAway“ hält vorbereitete Speisen vor und folgt dem Push-Prinzip (Produktion auf Prognose). b) Pull: frische Ware, "
      "kaum Überschuss, aber Wartezeit und Spitzenbelastung. Push: sofort verfügbar, aber Gefahr von Überschuss und Verderb."),
     ("Aufgabe 14", f"a) Verbrauch je Tag: 600 Stück : 6 Tage = 100 Stück. Lieferzeit: 2 Tage Vorlauf der Herstellung plus 3 Tage "
      f"Belieferung = 5 Tage (Annahme: Wiederbeschaffungszeit). Behälter = 100 · 5 · (100 + 20) : (50 · 100) = {KANBAN:.0f}. "
      "Je Filiale sind 12 Kanban-Behälter nötig. (Zählt man nur die 3 Tage Belieferung, ergeben sich 100 · 3 · 1,2 : 50 = 7,2, also "
      "8 Behälter. Die Annahme mit 5 Tagen ist hier die plausiblere; mit dem Lösungsband abgleichen.) b) Zwei-Karten-System: "
      "Ist ein Behälter in der Filiale leer, geht die Nachschubkarte zum Lager. Dort wird eine Produktionskarte ausgelöst und "
      "die Produktion fertigt nach. Der volle Behälter wird mit der Karte zurückgeliefert. c) Verbesserungen: Sicherheitszuschlag "
      "überprüfen, Lieferzeit verkürzen, Behältergröße anpassen, saisonale Schwankungen berücksichtigen, digitale Kanban-Karten "
      "(E-Kanban)."),
     ("Aufgabe 15", "Individuell: Push- oder Pull-Anwendungen im Betrieb (zum Beispiel Kanban bei Kleinteilen); Vorteile: weniger "
      "Bestände, kürzere Durchlaufzeiten, bessere Auslastung."),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Basis: Info-Blatt JIT und JIS", "a) Nach dem Info-Blatt: Just-in-Time: Teile kommen zum benötigten Zeitpunkt, die Reihenfolge spielt "
         "keine Rolle, Lagerkosten sind minimal, ein Sortieraufwand kann nötig sein. Just-in-Sequence: Teile kommen zum exakten "
         "Zeitpunkt und in der benötigten Reihenfolge, kaum Zwischenlagerung und kein Sortieraufwand; Lieferanten und Hersteller "
         "stimmen sich eng ab. b) JiS: Sitze für unterschiedlich ausgestattete Autos, Außenspiegel in Wunschfarbe (viele Varianten). "
         "JiT: Schrauben, einfache Standardteile. Eigene Beispiele sind möglich (JiS zum Beispiel Cockpits oder Türverkleidungen, "
         "JiT zum Beispiel Verpackungsmaterial). c) Bei vielen Varianten muss jedes Teil genau zum richtigen Fahrzeug passen; sonst "
         "entstehen Sortierarbeit, Lager und Wartezeiten. Weitere Voraussetzungen und Risiken: zuverlässige Lieferanten, kurze Wege, "
         "Informationsverbindung; Störungen stoppen die Produktion."],
        ["Plus: JIT bei der Fly Bike Werke GmbH", "Erwartung: JIT eignet sich für Teile von regionalen, zuverlässigen Lieferanten und "
         "planbarer Nachfrage (zum Beispiel Flügelschrauben, Aluminiumrohre aus Deutschland). Für importierte Teile mit langen "
         "Lieferwegen und Risiken (zum Beispiel Batterien aus Asien) ist ein Sicherheitsbestand besser. JIS kann in der Endmontage bei "
         "variantenreichen Fahrrädern sinnvoll sein, verlangt aber sehr verlässliche Lieferanten. Gute Lösungen empfehlen eine "
         "Mischung und begründen sie mit Lieferzeit, Verlässlichkeit, Nachfrage und Kosten."],
        ["Kreativ: Erklärbild oder Video", "Kriterien: fachlich richtig, anschauliches Beispiel, Unterschied JIT und JIS klar, verständlich "
         "und höchstens 3 Minuten bzw. eine Seite."],
        ["BNE: Lieferkette und Verantwortung", "Erwartung: Das Gesetz verlangt Risikoanalysen und Maßnahmen bei Lieferanten, das kann Preise "
         "erhöhen und die Lieferantenauswahl einschränken; Zielkonflikte zwischen Preis, Liefersicherheit und Verantwortung werden "
         "benannt und gewichtet; Maßnahmen: Lieferantenfragebogen, Audits, Zertifikate, Vertragsklauseln."],
    ], [4.0, 13.0])
    d.speichern(pfad)


def loesungen_ls65_teil2(pfad):
    d = Dok(KOPF + " · LS 65", "LS 65 Lösungen Teil 2: Aufgaben 1 bis 24 und Zusatzaufgaben", STATUS)
    d.p("Aufgaben mit Recherche im Betrieb (1, 3 b, 9 b, 14 b, 22, 23 c) haben keine Einheitslösung.", kursiv=True)
    L = [
     ("Aufgabe 1", "Fly Bike Werke GmbH: Rohstoffe: Aluminium, Carbon, Stahl, Leder. Hilfsstoffe: Lack, Sand zum Abstrahlen, "
      "Schrauben. Fremdbauteile: Gangschaltungen, Bremsen, Reifen, Dynamos, Sättel, Beleuchtung. Handelswaren: Zubehör (Körbe, "
      "Ständer), Bekleidung. Betriebsstoffe: Öl, Schmiermittel, Diesel, Strom. Ausbildungsunternehmen: individuell."),
     ("Aufgabe 2", "1 c Spekulationsfunktion (Preisvorteil durch Menge), 2 a Zeitüberbrückungsfunktion (Halbfertigerzeugnisse bis "
      "zur Endmontage), 3 d Entsorgungsfunktion (Recyclingmaterial wird gesammelt), 4 b Sicherungsfunktion (eiserner Bestand)."),
     ("Aufgabe 3", "a) Veredelungsfunktion: Das Lager verändert die Ware, zum Beispiel Reifelager für Bananen, Käse oder Wein, "
      "Trocknen von Holz, Aushärten von Lacken. b) Individuell."),
     ("Aufgabe 4", "b Entladen vom Transportfahrzeug, d Prüfung auf äußere Mängel und Dokumentation auf dem Lieferschein, "
      "a Erfassung des Warenzugangs, f Vorbereitung der Ware (Umpacken, Etikettieren), c Einlagerung nach Lagerplan, "
      "e Weitergabe der Warendokumente an die Finanzbuchhaltung. (Die Erfassung kann je nach Betrieb auch nach der Vorbereitung "
      "erfolgen; mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 5", "a) Annahme verweigern oder Ware nicht annehmen, Vermerk auf dem Frachtdokument, Spedition und Absender informieren. "
      "b) Durchgeweichte Kartons: Mangel auf dem Lieferschein vermerken, Fotos machen, Annahme unter Vorbehalt, Lieferant "
      "unverzüglich informieren (Mängelrüge). c) Mindermenge: Fehlmenge auf dem Lieferschein vermerken, Lieferant informieren, "
      "Nachlieferung oder Gutschrift verlangen. d) Glasbruch im Lager: Gefahrenstelle sichern und reinigen, Schaden dokumentieren, "
      "Bestand korrigieren, Schadensmeldung; bei Verletzung Erste Hilfe und Unfallanzeige."),
     ("Aufgabe 6", "a) Falsch: Die Wareneingangskontrolle muss unverzüglich erfolgen, weil Kaufleute ihre Waren unverzüglich "
      "untersuchen und Mängel rügen müssen (Untersuchungs- und Rügepflicht, § 377 HGB). b) Falsch: Volle Auslastung nimmt "
      "Flexibilität, behindert Wege und Zugriff und kann Sicherheitsvorschriften verletzen. c) Falsch: Der Lieferschein bleibt "
      "Nachweis für Art und Menge der gelieferten Ware, auch digital."),
     ("Aufgabe 7", "a) Person zur Ware: geringe Investition, flexibel, aber lange Wege, hohe Personalkosten, "
      "körperliche Belastung. Ware zur Person: hohe Investition, schnelle Zugriffe, ergonomisch (feste Greifhöhe), "
      "geringe Wegezeit, aber starre Abläufe und Tempodruck. b) Vor- und Nachteile aus den Kriterien Kosten, Effizienz und "
      "Gesundheit zusammenstellen."),
     ("Aufgabe 8", "a) Argumente: weniger Fehler, höhere Geschwindigkeit, Entlastung von schwerer Arbeit, rund um die Uhr nutzbar, "
      "gleichbleibende Qualität. b) Gefahren: Leistungsdruck (siehe Karikatur), Überwachung, monotone Arbeit, Unfälle bei "
      "Zusammenarbeit von Mensch und Roboter, Verlust von Arbeitsplätzen."),
     ("Aufgabe 9", "a) EAN (GTIN): Artikelnummer, die in der Datenbank nachgeschlagen wird. QR-Code: mehr Daten, zum Beispiel Text "
      "oder Link, auch bei Beschädigung lesbar. RFID: berührungslos, viele Etiketten gleichzeitig, wieder beschreibbar, "
      "Seriennummer und Historie. b) Individuell."),
     ("Aufgabe 10", f"a) Basiszeit: mobiles Datengerät aus dem Büro holen (3 Minuten). Wegzeit: Laufen zu den Waren (6 Minuten). "
      f"Greifzeit: Entnahme (0,5 Minuten). Totzeit: Kontrolle und Bestätigen am Endgerät (1 Minute). Die Pickliste wird digital "
      f"angezeigt; das Anzeigen ist hier Teil der Basiszeit. b) 3 + 6 + 0,5 + 1 = {KOMM:g} Minuten je Vorgang. c) 8 Stunden = 480 Minuten; "
      f"480 : {KOMM:g} = 45,7, also 45 vollständige Vorgänge. d) Maßnahmen: Datengerät am Arbeitsplatz bereithalten (Basiszeit "
      "sinkt), Wege verkürzen (häufig gepickte Artikel nah am Ausgang), mehrere Aufträge zusammen kommissionieren, Pick-by-Voice "
      "oder Pick-by-Light, Lagerplätze neu ordnen. e) Vorteile: Transparenz, Planbarkeit, Vergleich, Schwachstellen erkennen. "
      "Nachteile: Leistungsdruck, Überwachung (Datenschutz, Mitbestimmung des Betriebsrats)."),
     ("Aufgabe 11", "a) Parallele (zonenweise gleichzeitig), mehrstufige (zonenweise nacheinander) und Sammelkommissionierung "
      "(mehrere Aufträge auf einmal), auch mit Pick-by-Light oder Pick-by-Voice. b) Parallel und Sammelkommissionierung "
      "verkürzen die Wegzeit; mehrstufig braucht eine Zusammenführung. c) Empfehlung abhängig von Auftragsstruktur: viele "
      "kleine Aufträge: Sammelkommissionierung; große Aufträge: einstufig."),
     ("Aufgabe 12", "a) Falsch: Auch innerbetriebliche Entnahmen müssen kontrolliert werden, sonst stimmen Bestände und "
      "Kostenzuordnung nicht. b) Falsch: Auch bei EDV-geführtem Lager gibt es Fehlentnahmen oder Schwund; Kontrolle sichert "
      "Bestandsgenauigkeit."),
     ("Aufgabe 13", "Hinweis: Bilder im Heft prüfen. a) Luftpolsterfolie im Karton: Schutzfunktion (Transportschutz). "
      "b) Eierkarton: Schutzfunktion und Lagerung/Transport in Einheiten. c) Parfümverpackung: Werbe- und Verkaufsfunktion. "
      "d) Kartons: Transport- und Lagerfunktion (Stapelbarkeit, Handhabung)."),
     ("Aufgabe 14", "a) Zu überlegen: Rücknahmesystem und Pfand, Rücktransport, Reinigung, Lagerplatz für Leergut, Kosten, "
      "Hygiene, Haltbarkeit. b) Getränkehersteller: Pfandflaschen und -kästen. Schuhhersteller: Mehrwegversandkartons oder "
      "Mehrwegtaschen mit Rückversand. Ausbildungsunternehmen: individuell."),
     ("Aufgabe 15", f"a) Nettolagerfläche 450 m². Verkehrswege 20 % davon: 90 m². Dazu Sozialfläche 50 m². Bruttoflächenbedarf = 450 + 90 + "
      f"50 = {BRUTTO:.0f} m². Raumhöhe: 4 Ebenen · 2 m = 8 m. Nettoraumvolumen: 450 m² · 8 m = 3 600 m³ (Annahme: 450 m² sind die "
      "Grundfläche bei vier übereinanderliegenden Ebenen; mit dem Lösungsband abgleichen). b) Angebot 1: genug Fläche (600 m²), "
      "aber wegen der Stahlträger 2,5 m unter der Hallendecke nur ca. 7,5 m nutzbare Höhe; keine baulichen Unterteilungen, Büros und Sozialräume müssten erst abgetrennt werden. Angebot 2: Lagerfläche 540 m² "
      "und 9 m Höhe passen, aber die Verwaltungsfläche (40 m²) ist kleiner als der Bedarf von 50 m². Angebot 3: Bruttofläche "
      "625 m² ausreichend, 55 m² für Mitarbeiter, aber nur 7 m Höhe, also nur drei Ebenen. Begründete Entscheidung für Angebot 2 "
      "oder 3, je nach Gewichtung von Höhe und Sozialfläche. c) Eine große Höhe spart Fläche, verlangt aber mehr Heiz- und "
      "Beleuchtungskosten, stärkere Regale und Böden, Stapler oder Regalbediengeräte, aufwendigeren Brandschutz und Sicherheit; "
      "Zugriffszeiten steigen."),
     ("Aufgabe 16", "a Dezentral: Vorteil. b Dezentral: Nachteil. c Zentral: Vorteil. d Zentral: Vorteil. e Zentral: Nachteil. "
      "f Zentral: Vorteil. (Zuordnung von a und e bitte mit dem Lösungsband abgleichen.)"),
     ("Aufgabe 17", "Beispielhafte Begründungen: a Amazon: dezentral, viele Logistikzentren nah an den Kunden für schnelle Lieferung. "
      "b Schulbuchverlag: zentral, stark saisonaler Absatz, begrenztes Sortiment. c Kleidungshersteller: eher zentral mit "
      "Verteilung an die Filialen, bei vielen Filialen auch regional ergänzt. d Lebensmittelhersteller: dezentral wegen kurzer "
      "Haltbarkeit und Kühlkette. Gute Begründung zählt mehr als die Entscheidung."),
     ("Aufgabe 18", "a richtig, b falsch (auch im Handel gebräuchlich), c falsch (bezahlt wird bei Entnahme), d richtig, "
      "e richtig (Eigentum beim Lieferanten bis zur Entnahme)."),
     ("Aufgabe 19", "a) Vorteile: engere Kundenbindung, planbarer Absatz, schnelle Verfügbarkeit beim Kunden. Nachteile: "
      "Kapitalbindung und Lagerkosten beim Zulieferer, Risiko (Schwund, Veralten), Abhängigkeit vom Kunden. b) Abhängig von der "
      "Produktart: für Standardteile mit hohem Durchsatz geeignet, für teure oder seltene Spezialteile weniger. c) Alternativen: "
      "Regionallager oder Auslieferungslager, Lieferung Just-in-Time oder Just-in-Sequence, Logistikdienstleister."),
     ("Aufgabe 20", "a Textilien: geschlossenes Lager. b Holzstämme: offenes Lager. c Sand: offenes Lager (Schüttgut) oder Silo. "
      "d Kupferbleche: geschlossenes Lager (Wert, Diebstahl, Korrosion). e Getreide: Silo oder geschlossenes Lager (Feuchtigkeit, "
      "Schädlinge)."),
     ("Aufgabe 21", "a Flachlager: eingeschossig, Palettenware oder Stückgut. b Etagenlager: mehrere Geschosse, kleine Teile, "
      "wenig Platz am Standort. c Hochregallager: Paletten, oft automatisiert. d Bunkerlager: Schüttgut wie Kies oder Kohle. "
      "e Silolager: rieselfähiges Schüttgut wie Getreide oder Zement. f Tragluftlager: Halle aus Luftüberdruck, Schüttgüter oder "
      "Waren, die Platz brauchen."),
     ("Aufgabe 22", "Individuell (Erkundungstour)."),
     ("Aufgabe 23", "a) Bodenlagerung: günstig, flexibel, für schwere und sperrige Güter, aber hoher Flächenbedarf, begrenzte "
      "Stapelhöhe, Zugriff schwierig. Regallagerung: gute Raumnutzung, besserer Zugriff und Ordnung, aber Kosten und starre "
      "Struktur. b) ba Ziegelsteine: Bodenlagerung. bb Waschmaschinen: Regal oder Boden (Palettenregal). bc E-Autos: Bodenlagerung "
      "auf besonderen Stellplätzen, Brandschutz wegen Batterie. bd Holz: Kragarmregal (Langgut) oder Bodenlagerung. be Fahrräder: "
      "Regal. c) Individuell."),
     ("Aufgabe 24", "Zu überlegen: Wirtschaftlichkeit und Kosten, Prozessanalyse (welche Tätigkeiten), Platz und Layout, "
      "Anbindung an die Lagerverwaltung, Schulung und Einbindung der Mitarbeitenden, Mitbestimmung, Sicherheit bei Mensch-"
      "Roboter-Zusammenarbeit, Datenschutz, Wartung und Ausfallkonzept, spätere Erweiterbarkeit."),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Basis: Fachartikel Kommissionierung", "a) Eine schnelle Lieferung ist für viele Kunden kaufentscheidend; nur versandfertige Ware kann "
         "transportiert werden, deshalb ist die Kommissionierung der Schlüssel; Sorgfalt geht vor Schnelligkeit. b) Ware zum Mann: hohe "
         "Investitionen in Lager- und Fördertechnik und Software, wenig Personal, weitgehend automatisiert, weniger fehleranfällig, "
         "kürzere Kommissionierzeit, besonders sinnvoll bei Hochregallagern. Mann zur Ware: personalkostenintensiv, geringere "
         "Investitionen, flexibel, funktioniert bei Festplatz- und Freiplatzsystem. c) Festplatzsystem: Jeder Artikel hat einen festen "
         "Platz, schnell zu finden, schnelldrehende Artikel nahe am Kommissionierplatz; Freiplatzsystem (chaotische Lagerhaltung): "
         "Eingelagert wird, wo Platz frei ist, ein Lagerverwaltungssystem findet die Lagerorte. Vorteil: gute Flächennutzung. "
         "Nachteil: Software nötig, ein Artikel kann an mehreren Orten liegen und muss zusammengetragen werden. d) Ziffern sind "
         "sprachunabhängig und vermeiden Missverständnisse (Schraubenzieher/Schraubendreher); beim Scannen der GTIN vergleicht der "
         "Scanner Beleg und Produkt und meldet Abweichungen optisch oder akustisch; die Nummer ist weltweit eindeutig. Grenzen: "
         "unleserliche Codes, falsch gebuchter Lagerplatz."],
        ["Plus: Zentral, dezentral oder beides", "Vergleich nach Kosten (Fixkosten mehrerer Lager, Transportkosten), Lieferzeit zu den "
         "Händlern in Süd- und Ostdeutschland, Bestände (mehr Sicherheitsbestände bei mehreren Lagern), Sicherheit und Verwaltung. "
         "Gute Lösungen empfehlen begründet eine Variante, zum Beispiel zentrales Lager mit Regionallager für schnelle Lieferung."],
        ["Kreativ: Lagerlayout", "Kriterien: Materialfluss, Gefahrstoffbereich, Rampen, Fluchtwege, Maßstab, lesbare Legende, "
         "begründete Platzierung."],
        ["BNE: Nachhaltige Lagerplanung", "Erwartung: drei Maßnahmen, zum Beispiel energieeffiziente LED-Beleuchtung mit "
         "Bewegungsmelder, Photovoltaik auf dem Dach, Mehrwegbehälter, kompaktes Layout für weniger Fläche; Bewertung nach Kosten "
         "und Umweltwirkung."],
    ], [4.0, 13.0])
    d.speichern(pfad)
