"""Block II, Teil A: Auftrag Handlungsprodukt 2, Orientierungen, Systematisierung, Fachgespräch, Reflexion."""
from docx_helfer import Dok
from block1_a import orientierung

KOPF = "LF 7 · Logistik- und Lagerprozesse · Industriekaufleute 2. Lehrjahr · Block II"


def auftrag_hp2(pfad):
    d = Dok(KOPF + " · Handlungsprodukt 2", "Handlungsprodukt 2: Nachhaltigkeits- und Entsorgungskonzept der Fly Bike Werke GmbH")
    d.h2("Die Situation")
    d.p("Nachhaltige Entwicklung ist in der Unternehmensstrategie der Fly Bike Werke GmbH verankert. Die Produktion ist schon "
        "deutlich nachhaltiger geworden, jetzt rückt die Logistik in den Mittelpunkt. Bei einem ersten Brainstorming wurden "
        "Ideen gesammelt, und die Abteilungsleitungen haben Abfälle aus der gesamten Wertschöpfung notiert.")
    d.p("Herr Thüne, Leiter Einkauf und Logistik, lädt zum nächsten Meeting ein: Bis dahin sollen aus den Ideen konkrete "
        "Handlungsstrategien und ein ganzheitliches Entsorgungskonzept werden, das auch die Mitarbeitenden einbindet.")
    d.h2("Euer Auftrag")
    d.p("Ihr arbeitet als Auszubildende in der Logistikabteilung und unterstützt Herrn Thüne und Jenny Liu (Teams mit 3 bis 4 "
        "Personen). Entwickelt ein Nachhaltigkeits- und Entsorgungskonzept für die Logistik und stellt es im Meeting vor.")
    d.tabelle(["Teil", "Das gehört hinein", "Ihr nutzt"], [
        ["A Nachhaltigkeitsmaßnahmen", "Ideen nach Ökologie, Soziales und Ökonomie; Hauptziele; priorisierte Maßnahmen (kurz-, mittel-, "
         "langfristig) mit Hürden; Sicherheitsmaßnahmen für Lager und Transport", "Lernsituation 70, Arbeitsblätter 70.1 bis 70.4"],
        ["B Entsorgungskonzept", "Präambel, gesetzliche Grundlagen, Abfallarten mit Maßnahmen zur Vermeidung und Verwertung, "
         "personalorientierte Maßnahmen, Monitoring", "Lernsituation 69, Arbeitsblatt 69.1"],
        ["C Wirkung und Nachhaltigkeitsziele", "Bezug zu den Nachhaltigkeitszielen der UN (SDG 6 Sauberes Wasser, SDG 11 "
         "Nachhaltige Städte und Gemeinden), mindestens eine Kennzahl zur Erfolgsmessung, Wirtschaftlichkeit und Risiken",
         "Lernatelier (BNE-Aufgaben), Strukturlegetechnik"],
    ], [3.8, 9.0, 4.2])
    d.h2("Das Meeting (Rollenspiel)")
    d.p("Ihr stellt euer Konzept in einem Meeting vor (ca. 10 Minuten je Team). Verteilt Rollen, zum Beispiel Geschäftsführung, "
        "Leitung Einkauf und Logistik, Produktion, Betriebsrat, Verwaltung und Kundenservice. Die Geschäftsführung fragt nach "
        "Kosten, die Produktion nach Machbarkeit, der Betriebsrat nach den Folgen für die Beschäftigten. Am Ende entscheidet das "
        "Meeting, welche Maßnahmen umgesetzt werden.")
    d.h2("Form und Umfang")
    d.punkte(["Konzeptdokument im OnlyOffice-Dokumenteneditor, ca. 4 bis 6 Seiten, mit Deckblatt und Quellen.",
              "Kurzpräsentation (5 bis 8 Folien) im OnlyOffice-Präsentationseditor für das Meeting.",
              "Teil A und B entstehen schrittweise in der Ko-kreativen Problemlösung, Teil C nach der Systematisierung.",
              "Handlungsprodukt 1 und 2 sind zusammen die Grundlage des Fachgesprächs."])
    d.speichern(pfad)


def orientierungen(ziel):
    orientierung(ziel + "LS70_Inhaltliche_Orientierung.docx", "LS 70", "Für Sicherheit und Nachhaltigkeit in der Logistik sorgen",
        "Kapitel 5.3", 5,
        "Die Fly Bike Werke GmbH will ihre Logistik nachhaltiger machen. In einem Brainstorming sammelst du Ideen für drei "
        "Dimensionen der Nachhaltigkeit (Ökologie, Soziales, Ökonomie), priorisierst sie nach Zeithorizont und bereitest ein "
        "Meeting vor. Im Lernatelier geht es außerdem um Sicherheit im Lager: Sicherheitszeichen, Gefahrstoffe, Ergonomie, "
        "Unfälle und Datenschutz.",
        "Nachhaltigkeit ist in der Logistik kein Zusatz mehr, sondern verlangt von Kunden, Gesetzgeber und Mitarbeitenden. "
        "Sicherheit im Lager schützt Menschen und Waren. Im IHK-Katalog stehen Sicherheitszeichen, Gefahrstoffe und die "
        "ökologische, soziale und ökonomische Beurteilung von Transport und Lager.",
        ["Handlungsempfehlungen für eine ökologische Ausrichtung der Logistik vorschlagen.",
         "Handlungsempfehlungen für eine soziale Ausrichtung der Logistik vorschlagen.",
         "wirtschaftliche Gesichtspunkte bei einer nachhaltigen Logistik ausreichend berücksichtigen."],
        ["Nachhaltigkeit: Ökologie, Soziales, Ökonomie", "Letzte Meile", "Corporate Carbon Footprint", "Sicherheitszeichen",
         "GHS-Gefahrensymbole", "Gefahrgut", "Ergonomie", "Unfallanzeige", "Datenschutz", "Nachhaltigkeitsziele der UN (SDG 11)"],
        "Hier entsteht Teil A deines Handlungsprodukts 2: die priorisierten Nachhaltigkeitsmaßnahmen mit Sicherheitsaspekten. "
        "Sie sind die Grundlage für das Entsorgungskonzept in LS 69.",
        "Seiten 126 bis 134", kopf=KOPF)
    orientierung(ziel + "LS69_Inhaltliche_Orientierung.docx", "LS 69", "Ein Entsorgungskonzept erstellen",
        "Kapitel 4.1 bis 4.3", 5,
        "In jedem Industrieunternehmen entstehen Abfälle: Metallreste, Lackreste, Verpackungen, Elektroschrott, Batterien. Du "
        "entwickelst ein ganzheitliches Entsorgungskonzept: Welche Abfallarten fallen an? Wie werden sie vermieden oder "
        "verwertet? Welche Gesetze gelten? Wie werden Mitarbeitende eingebunden und wie wird das Konzept überwacht?",
        "Entsorgung kostet Geld, ist gesetzlich geregelt und ein wichtiger Hebel für Nachhaltigkeit. Fehler beim Umgang mit "
        "gefährlichen Abfällen können Gewässer und Menschen gefährden (Nachhaltigkeitsziel 6, Sauberes Wasser).",
        ["feststellen, welche Abfallarten in einem Unternehmen anfallen.",
         "Maßnahmen zur Abfallvermeidung wie auch zur Abfallverwertung vorschlagen.",
         "Maßnahmen zur Überprüfung und Überwachung des Entsorgungskonzepts vorschlagen und anwenden."],
        ["Abfallhierarchie", "Kreislaufwirtschaftsgesetz", "Abfallvermeidung", "Abfallverwertung (stofflich, energetisch)",
         "Recycling", "Abfallbeseitigung", "gefährliche Abfälle", "Verpackungsgesetz", "Monitoring", "Wiederverwertungsquote"],
        "Hier entsteht Teil B deines Handlungsprodukts 2: das Entsorgungskonzept. In Teil C verbindest du es mit den "
        "Nachhaltigkeitsmaßnahmen aus LS 70.",
        "Seiten 117 bis 125", kopf=KOPF)


def strukturlegen(pfad):
    d = Dok(KOPF + " · Systematisierung", "Systematisierung mit der Strukturlegetechnik: Nachhaltigkeit und Entsorgung")
    d.hinweis("Diese Phase machen wir analog: mit Karten, Stiften und Papier. Das Ergebnis fotografiert ihr oder überträgt es in "
              "Teil C eures Handlungsprodukts.")
    d.h2("Ziel")
    d.p("Du ordnest die Inhalte aus LS 70 und LS 69 so, dass du sie auf neue Situationen übertragen kannst: Wie hängen die drei "
        "Dimensionen der Nachhaltigkeit, Sicherheit, Abfallhierarchie und gesetzliche Vorgaben zusammen?")
    d.h2("So geht ihr vor")
    d.nummern(["Begriffe sammeln: Schreibe jeden wichtigen Begriff aus LS 70 und 69 auf eine Karte.",
               "Gruppieren: Bilde Gruppen mit Oberbegriffen, zum Beispiel Ökologie, Soziales, Ökonomie, Abfallhierarchie, Recht.",
               "Beziehungen legen: Verbinde die Gruppen mit Pfeilen und schreibe ein Verb darauf (zum Beispiel „verlangt“, "
               "„senkt“, „widerspricht“).",
               "Zielkonflikte markieren: Kennzeichne Stellen, an denen Ziele gegeneinander arbeiten (zum Beispiel Kosten gegen "
               "Umweltschutz), und überlege, wie man sie auflöst.",
               "Vergleichen und einigen: Vergleicht eure Bilder im Team und erklärt euch eure Zuordnungen.",
               "Übertragen: Ordnet die Nachhaltigkeitsziele 6 und 11 im Bild ein und haltet das Ergebnis für Teil C fest."])
    d.h2("Begriffe als Startpunkt (ergänze eigene)")
    d.tabelle(["Nachhaltigkeit", "Sicherheit", "Abfall", "Recht und Kennzahlen"], [
        ["Ökologie", "Sicherheitszeichen", "Vermeidung", "Kreislaufwirtschaftsgesetz"],
        ["Soziales", "Gefahrstoffe", "Verwertung (stofflich, energetisch)", "Verpackungsgesetz"],
        ["Ökonomie", "Ergonomie", "Beseitigung", "Wiederverwertungsquote"],
        ["Letzte Meile", "Unfallanzeige", "Recycling", "Monitoring"],
        ["SDG 11", "Datenschutz", "Gefährlicher Abfall, SDG 6", "Corporate Carbon Footprint"],
    ], [4.2, 4.2, 4.2, 4.2])
    d.h2("Mögliche Leitfragen für die Pfeile")
    d.punkte(["Welche Maßnahme aus LS 70 wirkt sich auf welche Abfallart in LS 69 aus?",
              "Wo stehen Kosten und Umweltschutz im Konflikt, und wo gehen sie zusammen?",
              "Was ändert sich für die Mitarbeitenden, und wie binden wir sie ein?",
              "Woran würden wir merken, dass die Maßnahmen wirken (Kennzahlen)?"])
    d.speichern(pfad)


def fachgespraech_schueler(pfad):
    d = Dok(KOPF + " · Zertifizierung", "Zertifizierung: Fachgespräch zu Handlungsprodukt 1 und 2")
    d.h2("Worum geht es?")
    d.p("Im Fachgespräch zeigt ihr, was ihr in Block I und II verstanden habt. Es ist ein Gespräch, kein Vortrag: Ihr erklärt "
        "eure Handlungsprodukte, begründet Entscheidungen und beantwortet Rückfragen. Danach wisst ihr, was ihr schon gut könnt "
        "und woran ihr noch arbeiten könnt.")
    d.h2("Ablauf (ca. 15 bis 20 Minuten, Gruppe von 3 bis 4 Personen)")
    d.tabelle(["Phase", "Inhalt", "Zeit"], [
        ["1 Einstieg", "Jede Gruppe stellt in einem Satz je Handlungsprodukt die zentrale Empfehlung vor", "ca. 3 Min."],
        ["2 Fragen zu HP 1", "Lieferkette, Lager, Verknüpfung und Empfehlung", "ca. 5 Min."],
        ["3 Fragen zu HP 2", "Nachhaltigkeit, Entsorgung, SDG, Kennzahlen", "ca. 5 Min."],
        ["4 Verknüpfung und Transfer", "Wie hängen beide Handlungsprodukte zusammen? Wie lässt es sich auf den Betrieb übertragen?", "ca. 4 Min."],
        ["5 Rückmeldung", "Rückmeldung zu Stärken und nächsten Schritten", "ca. 3 Min."],
    ], [3.8, 10.2, 3.0])
    d.h2("Anmeldung")
    d.p("Tragt euch auf dem Board in Moodle ein, sobald ihr Block II bearbeitet habt. Sobald ein Termin mit 3 bis 4 Schülerinnen "
        "und Schülern belegt ist, beginnt das Fachgespräch.")
    d.h2("Wonach wird bewertet?")
    d.punkte(["Fachlichkeit und Genauigkeit eurer Aussagen (HP 1 und HP 2)",
              "Verknüpfung von Lieferkette, Lager, Nachhaltigkeit und Entsorgung",
              "Begründung eurer Empfehlungen, auch bei Rückfragen",
              "Bezug zu Nachhaltigkeitszielen und Kennzahlen",
              "Fachsprache, Zusammenarbeit und Beitrag jeder Person"])
    d.p("Das genaue Raster bekommt ihr vor dem Gespräch von eurer Lehrkraft.", kursiv=True)
    d.speichern(pfad)


def fachgespraech_lehrkraft(pfad):
    d = Dok(KOPF + " · Zertifizierung · Lehrkraft", "Fachgespräch: Fragenkatalog und Bewertungsraster (Lehrkraft)")
    d.hinweis("Entwurf für die Lehrkraft. Punkte und Gewichtung können angepasst werden; der Notenschlüssel liegt bei der Lehrkraft "
              "und ist hier bewusst nicht festgelegt.", "FFF3CD")
    d.h2("Fragenpool (Auswahl, je Gespräch 5 bis 8 Fragen)")
    d.h3("Handlungsprodukt 1 (Lieferkette und Lager)")
    d.punkte(["Welches Problem in der Lieferkette der Fly Bike Werke GmbH ist aus eurer Sicht das größte, und warum?",
              "Welche Auswahlkriterien für Lieferanten gewichtet ihr am stärksten? Wie wirkt sich das auf die Abhängigkeit aus?",
              "Wie verändert eine bessere Prognose den Flächenbedarf im neuen Lager?",
              "Warum liegen Lacke und Lithium-Batterien nicht im selben Lagerbereich? Was gilt für die Lagerung?",
              "Welche Kommissionierform empfehlt ihr für Handelswaren, welche für die Produktion, und warum?",
              "Wann wäre Just-in-Time bei der Fly Bike Werke GmbH sinnvoll, wann nicht?",
              "Welches Risiko bleibt bei eurer Empfehlung, und wie geht ihr damit um?"])
    d.h3("Handlungsprodukt 2 (Nachhaltigkeit und Entsorgung)")
    d.punkte(["Welche eurer Maßnahmen ist kurzfristig, welche langfristig umsetzbar? Welche Hürden seht ihr?",
              "Wo stehen Kosten und Umweltschutz im Konflikt, und wie löst ihr das?",
              "Welche Abfallart bereitet die größten Risiken, und warum (Gefahrstoffe, Gewässerschutz)?",
              "Wie ordnet ihr die Abfallhierarchie auf ein konkretes Beispiel der Fly Bike Werke GmbH ein?",
              "Wie bindet ihr die Mitarbeitenden ein, und woran merkt ihr, ob es wirkt (Kennzahl)?",
              "Welchen Beitrag leistet euer Konzept zu SDG 6 und SDG 11?"])
    d.h3("Verknüpfung und Transfer")
    d.punkte(["Wie hängen Lieferkette, Lager und Entsorgung zusammen? Nennt ein Beispiel, wo eine Entscheidung in einem Bereich "
              "den anderen beeinflusst.",
              "Was würdet ihr in eurem Ausbildungsbetrieb als Erstes prüfen?",
              "Was hätte sich geändert, wenn die Nachfrage sinkt statt wächst?"])
    d.h2("Bewertungsraster (Entwurf)")
    d.p("Pro Kriterium 0 bis 4 Punkte (Zwischenwerte 1 und 3 sind möglich), gesamt höchstens 36. Teil „Gespräch“ bewertet die Gruppe und die einzelne Person.", kursiv=True)
    kopf = ["Kriterium", "4 Punkte", "2 Punkte", "0 Punkte"]
    d.tabelle(kopf, [
        ["HP 1 Fachlichkeit und Bezug zur Fly Bike Werke GmbH", "Aussagen fachlich richtig, auf die Firma bezogen, Fachbegriffe sicher",
         "überwiegend richtig, einzelne Lücken, teils allgemein", "viele Fehler oder kein Bezug"],
        ["HP 1 Verknüpfung Lieferkette und Lager", "Zusammenhänge erkannt und an Beispielen erklärt (Bestand, Fläche, Prognose)",
         "Zusammenhänge benannt, wenig erklärt", "keine Verknüpfung"],
        ["HP 1 Empfehlung und Begründung", "begründet, wägt Kosten, Sicherheit und Risiken ab", "Empfehlung vorhanden, Begründung knapp",
         "ohne Begründung"],
        ["HP 2 Nachhaltigkeitsmaßnahmen", "alle drei Dimensionen, priorisiert, Hürden benannt", "Dimensionen unvollständig oder Priorisierung "
         "ohne Begründung", "Ideen ohne Ordnung"],
        ["HP 2 Entsorgungskonzept", "Abfallarten, Vermeidung und Verwertung, Recht, Mitarbeitende und Monitoring stimmig",
         "Teile fehlen oder sind ungenau", "unvollständig oder falsch"],
        ["HP 2 SDG-Bezug und Kennzahl", "SDG 6 und 11 sinnvoll genutzt, Kennzahl passend und erklärt", "ein Ziel oder Kennzahl nur angedeutet",
         "kein Bezug"],
        ["Gespräch: Verknüpfung HP 1 und HP 2", "erkennt Querverbindungen und wendet sie an", "einzelne Verbindungen", "keine Verbindung"],
        ["Gespräch: Argumentation und Fachsprache", "klar, genau, antwortet sicher auf Rückfragen", "teilweise unsicher oder ungenau",
         "kaum Antworten"],
        ["Gespräch: Zusammenarbeit und eigener Beitrag", "jede Person trägt erkennbar bei, Gruppe ergänzt sich", "ungleiche Beteiligung",
         "kaum Beitrag"],
    ], [4.8, 4.8, 4.0, 3.4], 9)
    d.h2("Rückmeldung an die Gruppe (Vorlage)")
    d.punkte(["Das kann das Team schon gut: …", "Daran sollte das Team noch arbeiten: …", "Empfohlene Lernatelier-Aufgaben: …"])
    d.speichern(pfad)


def reflexion(pfad):
    d = Dok(KOPF + " · Reflexion", "Reflexion und Feedback Block II")
    d.p("Nimm dir nach dem Fachgespräch 15 Minuten. Deine Antworten sind für dich bestimmt und helfen dir, dein Lernen zu "
        "steuern.", kursiv=True)
    d.h2("Leitfragen")
    d.nummern(["Was hat im Fachgespräch gut geklappt? Wo war ich unsicher?",
               "Welche Kann-Aussagen aus LS 70 und LS 69 beherrsche ich sicher? Welche muss ich noch üben, und welche Aufgaben im "
               "Lernatelier helfen mir dabei?",
               "Wie hängen Lieferkette, Lager, Nachhaltigkeit und Entsorgung zusammen? Erkläre es in zwei Sätzen.",
               "Welchen Beitrag leistet die Logistik zu den Nachhaltigkeitszielen 6 (Sauberes Wasser) und 11 (Nachhaltige Städte)?",
               "Wie hat unser Team gearbeitet (Planung, Aufgabenverteilung, Umgang mit Konflikten)? Was nehmen wir für Block III mit?",
               "Welche Rückmeldung zu meinem Lernen war für mich besonders hilfreich?"])
    d.h2("Mein nächster Schritt")
    d.p("Ich werde als Nächstes …")
    d.speichern(pfad)
