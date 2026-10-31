"""Block I, Teil A: Auftrag Handlungsprodukt 1, Orientierungen, Strukturlegetechnik, Zwischenreflexion."""
from docx_helfer import Dok

KOPF = "LF 7 · Logistik- und Lagerprozesse · Industriekaufleute 2. Lehrjahr · Block I"


def auftrag_hp1(pfad):
    d = Dok(KOPF + " · Handlungsprodukt 1", "Handlungsprodukt 1: Logistik- und Lagerkonzept der Fly Bike Werke GmbH")
    d.h2("Die Situation")
    d.p("Die Fly Bike Werke GmbH wächst. Die Nachfrage nach Fahrrädern und E-Bikes steigt, ist aber stark saisonal. "
        "Viele Lieferanten sitzen weit entfernt, die Lagerbestände an drei Standorten (Stammsitz, Dresden, München) sind hoch "
        "und am Stammsitz reicht die Lagerfläche nicht mehr aus.")
    d.p("Die Geschäftsführerin Ewa Nowak bittet die Logistikabteilung um Herrn Thüne, bis zur nächsten "
        "Gesellschafterversammlung ein Logistik- und Lagerkonzept vorzulegen. Wachstum, Lieferkette und Lagerplanung sollen "
        "gemeinsam betrachtet werden, bevor das Unternehmen in ein neues Lager investiert.")
    d.h2("Euer Auftrag")
    d.p("Ihr arbeitet als Auszubildende in der Logistikabteilung (Teams mit 3 bis 4 Personen). Erarbeitet ein Logistik- und "
        "Lagerkonzept als Entscheidungsvorlage für die Geschäftsführung.")
    d.tabelle(["Teil", "Das gehört hinein", "Ihr nutzt"], [
        ["A Lieferkette", "Lieferantenkarte, Problemfelder und Auswahlkriterien, drei Maßnahmenpakete (Lagerbestandsplanung, "
         "Nachfrageprognose, Einsatz von Technologie) mit je einem Ziel", "Lernsituation 64, Arbeitsblätter 64.1 und 64.2"],
        ["B Lagerplanung", "Bedarfsanalyse (Ware, Lagerart, Lagereinrichtung, Sicherheitshinweis), Skizze des neuen Lagers mit "
         "Lagerplätzen, Kommissionierkonzept für Beschaffung und Distribution", "Lernsituation 65, Arbeitsblätter 65.1 bis 65.3"],
        ["C Verknüpfung und Empfehlung", "Wie verändern die Maßnahmen aus Teil A den Flächenbedarf in Teil B? Begründete "
         "Empfehlung an die Geschäftsführung (eine Seite), Risiken und offene Fragen", "Eure Strukturlegearbeit (Systematisierung)"],
    ], [3.2, 9.3, 4.5])
    d.h2("Form und Umfang")
    d.punkte(["Entscheidungsvorlage als Dokument im OnlyOffice-Dokumenteneditor, ca. 4 bis 6 Seiten, mit Deckblatt und Quellen.",
              "Optional eine Kurzpräsentation (5 Minuten) im OnlyOffice-Präsentationseditor.",
              "Teil A und B entstehen schrittweise in der Ko-kreativen Problemlösung, Teil C nach der Systematisierung.",
              "Das Handlungsprodukt ist Grundlage des Fachgesprächs nach Block II. Dort kommen Handlungsprodukt 1 und 2 zusammen."])
    d.h2("Worauf wir achten (Kurzfassung des Rasters)")
    d.punkte(["Fachlich richtig und auf die Fly Bike Werke GmbH bezogen",
              "Zusammenhänge zwischen Lieferkette und Lager erkannt (Teil C)",
              "Empfehlung ist begründet und berücksichtigt Kosten, Sicherheit und Risiken",
              "Verständlich gegliedert und sauber dargestellt"])
    d.speichern(pfad)


def orientierung(pfad, ls, titel, buch, std, worum, wichtig, kann, begriffe, verbindung, seiten):
    d = Dok(KOPF + f" · {ls}", f"Inhaltliche Orientierung {ls}: {titel}")
    d.p(f"Zeitrahmen: {std} Unterrichtsstunden · Buch: {buch} · Lernsituation und Aufgaben: {seiten}", kursiv=True)
    d.h2("Worum geht es?")
    d.p(worum)
    d.h2("Warum ist das wichtig?")
    d.p(wichtig)
    d.h2("Das kannst du am Ende (Kann-Liste)")
    d.punkte(["… " + k for k in kann])
    d.h2("Wichtige Begriffe")
    d.p(", ".join(begriffe))
    d.h2("So hängt es mit dem Handlungsprodukt zusammen")
    d.p(verbindung)
    d.h2("So arbeitest du")
    d.nummern(["Ihr plant im Team: Arbeitsplan, Rollen, Punktekonto (nicht in Moodle).",
               "Ko-kreative Problemlösung: Lest die Lernsituation und die Buchkapitel, löst die Arbeitsaufträge im Team und "
               "tragt eure Ergebnisse in die Arbeitsblätter ein.",
               "Subjektive Aneignung: Prüfe mit der Kann-Liste, was du schon kannst.",
               "Lernatelier: Übe gezielt, was dir noch fehlt. Wähle die Aufgaben nach Bedarf und Niveau.",
               "Individuelle Verarbeitung: Bearbeite die Alles-klar-Aufgaben und hake die Kann-Liste ab."])
    d.speichern(pfad)


def orientierungen(ziel):
    orientierung(ziel + "LS64_Inhaltliche_Orientierung.docx", "LS 64", "Ein Logistikkonzept erstellen",
        "Kapitel 1.1, 1.2 und 1.3.3", 5,
        "Die Fly Bike Werke GmbH bezieht Material von Lieferanten aus der Region und aus der ganzen Welt. Die Nachfrage schwankt "
        "mit den Jahreszeiten, die Lagerbestände sind hoch. Du untersuchst, wie die Lieferkette (Supply-Chain) aufgebaut ist, wo "
        "es Schwierigkeiten gibt und welche Maßnahmen sie effizienter machen.",
        "Eine Lieferkette ist nur so stark wie ihr schwächstes Glied. Lieferverzug, schwankende Nachfrage und hohe Bestände "
        "kosten Geld und gefährden die Liefertreue. Wer die Zusammenhänge versteht, kann im Betrieb Schwachstellen erkennen und "
        "Verbesserungen vorschlagen. Das wird auch in der IHK-Prüfung verlangt.",
        ["die Aufgaben der Logistik und ihre Bedeutung für das Unternehmen erläutern.",
         "Besonderheiten und Schwierigkeiten in der Supply-Chain erkennen.",
         "Maßnahmen im Rahmen des Supply-Chain-Managements vorschlagen."],
        ["Logistik", "Supply-Chain-Management", "Warenfluss und Informationsfluss", "Liefertreue", "Lieferfähigkeit",
         "Sicherheitsbestand", "Bedarfsprognose", "Push- und Pull-Prinzip", "Kanban", "Just-in-Time und Just-in-Sequence",
         "Outsourcing", "Lieferkettensorgfaltspflichtengesetz"],
        "Hier entsteht Teil A deines Handlungsprodukts: die Lieferkette mit Problemfeldern, Auswahlkriterien und drei "
        "Maßnahmenpaketen. Die Ergebnisse brauchst du in LS 65, denn Bestandsplanung und Prognose bestimmen, wie viel Lagerfläche "
        "das Unternehmen braucht.",
        "Seiten 74 bis 79")
    orientierung(ziel + "LS65_Inhaltliche_Orientierung.docx", "LS 65", "Die Lagerhaltung planen",
        "Kapitel 2.1 bis 2.4 und 2.3.4", 7,
        "Die Lagerflächen am Stammsitz reichen nicht mehr aus. Du planst ein neues Lager auf dem Firmengelände: Welche Waren "
        "brauchen welche Lagerart und Lagereinrichtung? Welche Sicherheitsanforderungen gibt es? Wie werden die Waren "
        "kommissioniert?",
        "Ein schlecht geplantes Lager kostet Zeit, Platz und Geld und kann Menschen gefährden, zum Beispiel bei Gefahrstoffen oder "
        "Lithium-Batterien. In der IHK-Prüfung werden Lagerarten, Lagersysteme und Kommissionierung häufig abgefragt.",
        ["bei der Planung von Lagerflächen Anforderungen an den Schutz der zu lagernden Waren feststellen.",
         "ein Lager anhand der gegebenen Anforderungen planen.",
         "die passende Form der Kommissionierung für ein Lager festlegen."],
        ["Lagerarten (offen, halboffen, geschlossen)", "Lagereinrichtung", "Lagerfunktionen", "Zentrales und dezentrales Lager",
         "Konsignationslager", "Wareneingang und Warenausgang", "Kommissionierung", "Person zur Ware, Ware zur Person",
         "Kommissionierzeit", "Verpackungsfunktionen", "Flächenbedarf"],
        "Hier entsteht Teil B deines Handlungsprodukts: Bedarfsanalyse, Lagerskizze und Kommissionierkonzept. In Teil C "
        "verbindest du es mit den Ergebnissen aus LS 64.",
        "Seiten 80 bis 88")


def strukturlegen(pfad):
    d = Dok(KOPF + " · Systematisierung", "Systematisierung mit der Strukturlegetechnik: Von der Lieferkette zum Lager")
    d.hinweis("Diese Phase machen wir bewusst analog: mit Karten, Stiften und Papier. Das Ordnen von Hand hilft beim Verstehen "
              "und Behalten. Danach fotografiert ihr das Ergebnis oder übertragt es in euer Handlungsprodukt (Teil C).")
    d.h2("Ziel")
    d.p("Du ordnest die Inhalte aus LS 64 und LS 65 so, dass du sie auch auf neue Situationen übertragen kannst, zum Beispiel "
        "auf den Betrieb oder die Prüfung. Das Ergebnis ist ein Strukturbild, das zeigt, wie Lieferkette, Bestand, Prognose, "
        "Technologie und Lager zusammenhängen.")
    d.h2("So geht ihr vor (Einzelarbeit, dann Team, ca. 2 Std. zusammen mit Teil C)")
    d.nummern(["Begriffe sammeln: Schreibe jeden wichtigen Begriff aus LS 64 und 65 auf eine eigene Karte. Nutze deine "
               "Ergebnisse und das Buch. Beispiele findest du unten.",
               "Gruppieren: Lege Karten zusammen, die inhaltlich zusammengehören, und gib jeder Gruppe einen Oberbegriff.",
               "Beziehungen legen: Verbinde die Gruppen mit Pfeilen. Schreibe auf jeden Pfeil ein Verb oder eine kurze Aussage "
               "(zum Beispiel „bestimmt“, „verringert“, „macht möglich“).",
               "Vergleichen: Vergleicht eure Strukturbilder im Team. Wo habt ihr unterschiedlich geordnet? Warum? Einigt euch auf "
               "ein gemeinsames Bild.",
               "Prüfen: Erklärt euch gegenseitig an einem Beispiel aus der Fly Bike Werke GmbH, wie ein Problem in der Lieferkette "
               "bis ins Lager wirkt.",
               "Übertragen: Haltet das Ergebnis fest und nutzt es für Teil C eures Handlungsprodukts."])
    d.h2("Begriffe als Startpunkt (ergänze eigene)")
    d.tabelle(["Lieferkette", "Bestand und Planung", "Lager", "Kommissionierung"], [
        ["Lieferant", "Sicherheitsbestand", "Lagerart", "Person zur Ware"],
        ["Lieferzeit", "Prognose", "Lagereinrichtung", "Ware zur Person"],
        ["Warenfluss", "Kanban", "Sicherheitsanforderung", "Kommissionierzeit"],
        ["Informationsfluss", "Push und Pull", "Zentral, dezentral", "Pickliste, Scanner"],
        ["Peitscheneffekt", "Just-in-Time", "Flächenbedarf", "Automatisierung"],
    ], [4.2, 4.2, 4.2, 4.2])
    d.h2("Mögliche Leitfragen für die Pfeile")
    d.punkte(["Wie beeinflusst eine schlechte Prognose den Bestand?",
              "Wie beeinflusst der Bestand den Flächenbedarf im Lager?",
              "Was ändert sich im Lager, wenn Lieferanten zuverlässiger liefern?",
              "Wie verändert Technologie (IoT, KI) die Kommissionierung?"])
    d.speichern(pfad)


def reflexion(pfad):
    d = Dok(KOPF + " · Zwischenreflexion", "Zwischenreflexion Block I")
    d.p("Nimm dir 10 Minuten. Schreibe stichwortartig auf; die Antworten sind nur für dich und dienen der Rückmeldung an dich "
        "selbst. Gespräche über eure Antworten sind im Team willkommen.", kursiv=True)
    d.h2("Leitfragen")
    d.nummern(["Was hat gut geklappt, und woran hat das gelegen (Arbeitsweise, Zusammenarbeit im Team, Aufgaben)?",
               "Was war schwierig oder ist noch unklar? Welche Aufgaben im Lernatelier helfen dir, die Lücke zu schließen?",
               "Welche Kann-Aussagen aus LS 64 und LS 65 kannst du jetzt sicher? Bei welchen musst du noch üben?",
               "Wie hat dein Team gearbeitet? Was wollt ihr in Block II beibehalten, was ändern?"])
    d.h2("Mein nächster Schritt")
    d.p("Ich werde als Nächstes …")
    d.speichern(pfad)
