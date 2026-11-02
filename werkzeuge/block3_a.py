"""Block III, Teil A: Orientierungen, Systematisierung, Klassenarbeit, Reflexion."""
from docx_helfer import Dok
from block1_a import orientierung

KOPF = "LF 7 · Logistik- und Lagerprozesse · Industriekaufleute 2. Lehrjahr · Block III"


def orientierungen(ziel):
    orientierung(ziel + "LS66_Inhaltliche_Orientierung.docx", "LS 66", "Zwischen Eigen- und Fremdlager entscheiden", "Kapitel 2.4.3", 5,
        "Die Fly Bike Werke GmbH braucht zusätzliche Lagerfläche für E-Bikes. Du vergleichst die Kosten eines Eigenlagers mit "
        "denen eines Fremdlagers, ermittelst die kritische Lagerfläche und entscheidest mit weiteren Aspekten. Außerdem klärst "
        "du, welche rechtlichen Beziehungen beim Fremdlager bestehen (Lagervertrag, Lagerschein).",
        "Wer Lager plant, muss rechnen und entscheiden können. Die kritische Lagerfläche zeigt, ab welcher Menge sich ein Eigenlager "
        "lohnt. Aufgaben dazu kommen in der Klassenarbeit und in der IHK-Prüfung vor.",
        ["die Kosten für ein Eigen- und ein Fremdlager berechnen.", "die kritische Lagerfläche ermitteln.",
         "unter Berücksichtigung weiterer Aspekte zwischen Eigen- und Fremdlager entscheiden."],
        ["Eigenlager und Fremdlager", "fixe und variable Kosten", "kritische Lagerfläche", "Lagervertrag", "Lagerschein",
         "Inhaber-, Order- und Namenslagerschein", "Einlagerer und Lagerhalter", "Amortisation"],
        "LS 66 gehört zu Block III. Es gibt kein Handlungsprodukt, die Ergebnisse bereiten die Klassenarbeit vor.",
        "Seiten 89 bis 97", kopf=KOPF)
    orientierung(ziel + "LS67_Inhaltliche_Orientierung.docx", "LS 67", "Die Lagerhaltung mithilfe von Kennzahlen verbessern", "Kapitel 2.6", 8,
        "Der Absatz eines Fahrradshirts läuft schlechter als erhofft. Du wertest die Lagerdaten mit Kennzahlen aus (Ø Lagerbestand, "
        "Umschlagshäufigkeit, Ø Lagerdauer, Lagerzins), vergleichst sie mit Vorjahr und Branche und leitest Handlungsempfehlungen ab.",
        "Kennzahlen zeigen, ob zu viel oder zu wenig Ware im Lager liegt. Sie sind Schwerpunkt der Klassenarbeit und gehören zu den "
        "festen Prüfungsthemen (Handlungskomplex 06).",
        ["verschiedene Kennzahlen für die Lagerhaltung ermitteln.", "passende Handlungsempfehlungen aus den Lagerkennzahlen ableiten."],
        ["Ø Lagerbestand", "Ø Lagerwert", "Umschlagshäufigkeit", "Ø Lagerdauer", "Lagerzinssatz und Lagerzinsen", "Lagernutzungsgrad",
         "Festplatzsystem und chaotische Lagerhaltung", "FIFO, LIFO, HIFO", "Branchenvergleich"],
        "LS 67 ist Block III. Die Bestandserfassung und Inventur sind aus Lernfeld 5 bekannt und werden hier nicht neu behandelt.",
        "Seiten 98 bis 107", kopf=KOPF)
    orientierung(ziel + "LS68_Inhaltliche_Orientierung.docx", "LS 68", "Die geeignete Transportform auswählen", "Kapitel 3.2", 5,
        "Lukas macht ein Praktikum in der Versandabteilung der Fly Bike Werke GmbH. Du bereitest Frachtbrief und Rechtsbeziehungen für einen "
        "Auftrag vor und empfiehlst für einen zweiten Auftrag ein passendes Transportmittel. Dazu rechnest du Eigen- und "
        "Fremdtransport und unterscheidest Warenbegleit- und Warenwertpapiere.",
        "Transportentscheidungen kosten Geld und beeinflussen Lieferzeit und Umwelt. Frachtbrief, Konnossement und Co. werden oft "
        "verwechselt und kommen in Prüfungen vor.",
        ["das geeignete Transportmittel auftragsorientiert auswählen.", "die Kosten für die gewählte Transportform ermitteln.",
         "die für einen Transport notwendigen Dokumente erstellen."],
        ["Frachtführer und Spediteur", "Werkverkehr und Fremdtransport", "kritische Entfernung", "Nutzwertanalyse", "KEP-Dienst",
         "Frachtbrief", "Warenbegleitpapiere", "Warenwertpapiere (Konnossement, Ladeschein, Lagerschein)", "Vor-, Haupt- und Nachlauf",
         "multimodaler Verkehr"],
        "LS 68 schließt Block III ab. Das Info-Blatt zu Warenbegleit- und Warenwertpapieren ist ergänzendes Material.",
        "Seiten 108 bis 116", kopf=KOPF)


def strukturlegen(pfad):
    d = Dok(KOPF + " · Systematisierung", "Systematisierung mit der Strukturlegetechnik: Kosten, Kennzahlen, Transport")
    d.hinweis("Diese Phase machen wir analog mit Karten, Stiften und Papier. Das Ergebnis hilft dir bei der Vorbereitung der Klassenarbeit.")
    d.h2("Ziel")
    d.p("Du ordnest die Inhalte aus LS 66, 67 und 68 so, dass du Rechenwege und Zusammenhänge auch in neuen Aufgaben anwenden kannst.")
    d.h2("So geht ihr vor")
    d.nummern(["Begriffe sammeln: Schreibe jeden wichtigen Begriff und jede Formel auf eine Karte (eine Karte, eine Idee).",
               "Gruppieren: Bilde Gruppen mit Oberbegriffen, zum Beispiel Kosten, Kennzahlen, Transport, Rechtliches, Entscheidung.",
               "Rechenwege verbinden: Lege Formeln in die Reihenfolge, in der du sie anwendest (zum Beispiel fixe Kosten, variable Kosten, "
               "kritische Menge, Entscheidung).",
               "Beziehungen legen: Verbinde die Gruppen mit Pfeilen und schreibe ein Verb darauf (zum Beispiel „bestimmt“, „senkt“).",
               "Vergleichen: Vergleicht eure Bilder im Team und erklärt euch an einem Zahlenbeispiel, wie ein Rechenweg funktioniert.",
               "Übertragen: Überlege, welche Aufgaben in der Klassenarbeit damit lösbar sind, und notiere offene Fragen."])
    d.h2("Begriffe als Startpunkt (ergänze eigene)")
    d.tabelle(["Kosten und Entscheidung", "Kennzahlen", "Transport", "Rechtliches und Dokumente"], [
        ["Eigen- und Fremdlager", "Ø Lagerbestand", "Eigen- und Fremdtransport", "Lagervertrag"],
        ["fixe und variable Kosten", "Umschlagshäufigkeit", "kritische Entfernung", "Lagerschein"],
        ["kritische Lagerfläche", "Ø Lagerdauer", "Nutzwertanalyse", "Frachtbrief"],
        ["Amortisation", "Lagerzinssatz", "Vor-, Haupt-, Nachlauf", "Konnossement, Ladeschein"],
        ["weitere Aspekte", "Lagernutzungsgrad", "Spediteur und Frachtführer", "Warenbegleit- und Warenwertpapiere"],
    ], [4.2, 4.2, 4.2, 4.2])
    d.h2("Leitfragen für die Pfeile")
    d.punkte(["Was ändert sich an der kritischen Menge, wenn sich der Preis des Fremdangebots ändert?",
              "Wie hängen Ø Lagerbestand, Umschlagshäufigkeit, Lagerdauer und Lagerzinssatz zusammen?",
              "Wann lohnt sich Werkverkehr, und welche Aspekte neben den Kosten zählen?",
              "Welches Papier gehört zu welchem Verkehrsträger, und was bewirkt es rechtlich?"])
    d.speichern(pfad)


def klassenarbeit(pfad):
    d = Dok(KOPF + " · Klassenarbeit 1", "Klassenarbeit 1: Überblick und Vorbereitung")
    d.hinweis("Termin, Dauer und erlaubte Hilfsmittel trägt die Lehrkraft ein: Termin ____________ · Dauer ______ Minuten · Hilfsmittel ____________")
    d.h2("Was kommt dran?")
    d.p("Die Klassenarbeit 1 bezieht sich auf LS 66, LS 67 und LS 68 (laut Kann-Liste). Du bekommst Rechenaufgaben und Aufgaben zum Erläutern "
        "und Begründen.")
    d.tabelle(["Thema", "Das solltest du können", "Übe mit"], [
        ["LS 66 Eigen- oder Fremdlager", "Kosten berechnen, kritische Lagerfläche ermitteln und grafisch darstellen, begründet entscheiden, "
         "Lagerschein und Lagervertrag erklären", "Arbeitsblatt 66.1 und 66.2, Aufgaben 1 bis 10"],
        ["LS 67 Lagerkennzahlen", "Ø Lagerbestand (drei Wege), Umschlagshäufigkeit, Ø Lagerdauer, Lagerzinssatz und -zinsen berechnen und "
         "deuten; Festplatzsystem und chaotische Lagerhaltung; FIFO, LIFO, HIFO", "Arbeitsblatt 67.1 und 67.2, Aufgaben 1 bis 19"],
        ["LS 68 Transportform", "Transportmittel auswählen, kritische Entfernung berechnen, Nutzwertanalyse, Werkverkehr oder Spedition, "
         "Frachtbrief, Warenbegleit- und Warenwertpapiere unterscheiden, Frachtführer und Spediteur", "Arbeitsblatt 68.1 und 68.2, Aufgaben 1 bis 20"],
    ], [4.0, 8.5, 4.5])
    d.h2("So bereitest du dich vor")
    d.nummern(["Kann-Liste: Hake ab, was du sicher kannst, und markiere, was fehlt.",
               "Lernatelier: Wähle die Aufgaben, die zu deinen Lücken passen (Aufgabenauswahl nach Niveau). Rechne mindestens eine Aufgabe je "
               "Rechenweg ohne Hilfe.",
               "Strukturbild: Erkläre dein Strukturbild aus der Systematisierung einer Mitschülerin oder einem Mitschüler.",
               "Formeln: Schreibe die wichtigsten Formeln auf eine Karte und erkläre jede an einem Zahlenbeispiel.",
               "Selbsttest: Löse eine Aufgabe aus dem Heft, die du noch nicht bearbeitet hast, unter Zeitvorgabe."])
    d.h2("Wichtige Formeln im Überblick")
    d.tabelle(["Bereich", "Formel"], [
        ["Kritische Menge (Lagerfläche oder Entfernung)", "fixe Kosten : (Preis je Einheit der Fremdleistung − variable Kosten je Einheit)"],
        ["Ø Lagerbestand", "(Anfangsbestand + Endbestand) : 2   oder   (Anfangsbestand + 12 Monatsendbestände) : 13"],
        ["Umschlagshäufigkeit", "Absatz (Jahresverbrauch) : Ø Lagerbestand"],
        ["Ø Lagerdauer", "360 Tage : Umschlagshäufigkeit"],
        ["Lagerzinssatz", "Marktzinssatz · Ø Lagerdauer : 360"],
        ["Lagerzinsen", "Ø Lagerwert · Lagerzinssatz"],
        ["Lagernutzungsgrad", "genutzte Fläche : verfügbare Fläche · 100 %"],
    ], [6.0, 11.0])
    d.p("Die Formeln stimmen mit den Lösungen im Lernatelier überein. Prüfe, ob dein Heft dieselbe Schreibweise verwendet.", kursiv=True)
    d.speichern(pfad)


def reflexion(pfad):
    d = Dok(KOPF + " · Reflexion", "Reflexion und Feedback Block III")
    d.p("Nimm dir nach der Klassenarbeit 15 Minuten. Die Antworten sind für dich bestimmt.", kursiv=True)
    d.h2("Leitfragen")
    d.nummern(["Was hat in der Vorbereitung gut funktioniert (Lernatelier, Strukturbild, Zusammenarbeit)?",
               "Welche Aufgaben in der Klassenarbeit fielen mir leicht, welche schwer? Woran lag das?",
               "Welche Rechenwege beherrsche ich sicher (kritische Menge, Kennzahlen, Lagerzinsen), welche muss ich noch üben?",
               "Wie hängen Lagerkosten, Kennzahlen und Transportentscheidungen zusammen? Erkläre es in zwei Sätzen.",
               "Was nehme ich aus dem gesamten Lernfeld 7 mit in den Betrieb und in die IHK-Prüfung?",
               "Wie ging es mir mit dem selbstorganisierten Lernen in den drei Blöcken? Was möchte ich beim nächsten Lernfeld anders machen?"])
    d.h2("Mein nächster Schritt")
    d.p("Ich werde als Nächstes …")
    d.speichern(pfad)
