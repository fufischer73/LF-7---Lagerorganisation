"""Block III: korrigiertes Info-Blatt und Anpassungen am Arbeitsblatt zu Warenbegleit- und Warenwertpapieren (LS 68).
Grundlage: planung/Pruefung_Warenbegleitpapiere.md (Branch pruefung-warenbegleitpapiere), Wortlaut aus dem Auszug der Lehrkraft."""
from docx_helfer import Dok

KOPF = "LF 7 · Logistik- und Lagerprozesse · Industriekaufleute 2. Lehrjahr · Block III · LS 68"
HINWEIS = ("Vorschlag zur Überarbeitung (Entwurf). Die Paragraphen stammen aus einem Auszug des HGB und sind noch nicht mit der amtlichen "
           "Fassung auf gesetze-im-internet.de abgeglichen. Bitte vor dem Einsatz im Unterricht die genannten Paragraphen nachlesen.")


def info_blatt(pfad):
    d = Dok(KOPF, "Warenbegleitpapiere und Warenwertpapiere (überarbeiteter Vorschlag)", HINWEIS)
    d.p("Datum: ______________        Name: ______________________________")
    d.h2("1 Grundlegende Unterscheidung")
    d.p("Warenbegleitpapiere begleiten die Lieferung und dokumentieren den Transport und die Ware, zum Beispiel Lieferschein, "
        "Packliste, Rechnung und Frachtbrief. Sie übertragen kein Recht am Gut: Wer sie besitzt, kann damit nicht über die Ware verfügen.")
    d.p("Warenwertpapiere (Traditionspapiere) verbriefen den Anspruch auf Ablieferung bzw. Auslieferung des Gutes. Die Übergabe oder "
        "Übertragung des Papiers hat beim Erwerb von Rechten am Gut dieselbe Wirkung wie die Übergabe des Gutes. Voraussetzung: "
        "Der Frachtführer, Lagerhalter oder Verfrachter hat das Gut im Besitz (§§ 448, 475g, 524 HGB).")
    d.h2("2 Der entscheidende Unterschied")
    d.punkte(["Warenwertpapiere: Wer das Papier rechtmäßig erwirbt, erwirbt Rechte am Gut so, als wäre ihm das Gut übergeben worden. "
              "Ob er auch Eigentümer wird, hängt zusätzlich von den Voraussetzungen des Eigentumserwerbs ab (BGB).",
              "Warenbegleitpapiere: Sie dokumentieren nur. Mit ihnen ist keine Verfügung über das Gut möglich."])
    d.h2("3 Die drei Traditionspapiere im HGB")
    d.p("Übertragbar durch Indossament, wenn sie „an Order“ lauten (§ 363 Abs. 2 HGB). Sie sind Warenwertpapiere und bestätigen "
        "zugleich die Übernahme des Gutes. Das Gut wird nur gegen Rückgabe des Papiers abgeliefert.")
    d.tabelle(["Papier", "Aussteller", "Ausstellung", "Traditionswirkung"], [
        ["Konnossement (Seefracht)", "Verfrachter", "§§ 513, 514 HGB", "§ 524 HGB"],
        ["Ladeschein", "Frachtführer", "§ 443 HGB", "§ 448 HGB"],
        ["Lagerschein (als Orderlagerschein)", "Lagerhalter", "§ 475c HGB", "§ 475g HGB"],
    ], [5.5, 3.5, 4.0, 4.0])
    d.h2("4 Der Frachtbrief: häufigste Verwechslung")
    d.punkte(["Der Frachtführer kann die Ausstellung verlangen (Kann-Papier). Der Frachtbrief wird in drei Originalen ausgestellt, "
              "eines begleitet das Gut (§ 408 HGB).",
              "Beweisfunktion: Ein von beiden Parteien unterzeichneter Frachtbrief beweist (bis zum Beweis des Gegenteils) Abschluss und "
              "Inhalt des Frachtvertrags und die Übernahme des Gutes. Er begründet die Vermutung, dass das Gut äußerlich in gutem Zustand "
              "war und Anzahl, Zeichen und Nummern der Frachtstücke stimmen (§ 409 HGB).",
              "Quittung: Ohne Vorbehalt des Frachtführers gilt das Gut bei der Übernahme als äußerlich in gutem Zustand („reiner“ Frachtbrief). "
              "Mit einem begründeten Vorbehalt („unreiner“ Frachtbrief) gilt diese Vermutung nicht.",
              "Sperrfunktion: Ist es im Frachtbrief vorgeschrieben, kann der Absender nachträgliche Weisungen nur gegen Vorlage der "
              "Absenderausfertigung erteilen (§ 418 Abs. 4 HGB).",
              "Der Frachtbrief ist kein Warenwertpapier und kein Traditionspapier. Mit ihm kann man nicht über das Gut verfügen."])
    d.h2("5 Übersicht")
    d.tabelle(["Dokument", "Warenbegleitpapier", "Warenwertpapier", "Rechte am Gut übertragbar?", "Rechtsgrundlage"], [
        ["Lieferschein", "ja", "nein", "nein", "–"],
        ["Packliste", "ja", "nein", "nein", "–"],
        ["Rechnung", "ja", "nein", "nein", "–"],
        ["Frachtbrief", "ja", "nein", "nein", "§§ 408, 409, 418 Abs. 4 HGB"],
        ["Konnossement", "nein", "ja", "ja, durch Übergabe oder Indossament", "§§ 513, 514, 524 HGB"],
        ["Ladeschein", "nein", "ja", "ja, durch Übergabe oder Indossament", "§§ 443, 448 HGB"],
        ["Lagerschein (Order)", "nein", "ja", "ja, durch Übergabe oder Indossament", "§§ 475c, 475g HGB"],
    ], [3.2, 2.6, 2.6, 4.2, 4.4], 9)
    d.hinweis("Merkhilfe: Nur wer das Traditionspapier (Konnossement, Ladeschein, Lagerschein an Order) rechtmäßig erwirbt, erwirbt "
              "Rechte am Gut. Der Frachtbrief macht dich nicht zum Berechtigten.", "E8F5E9")
    d.h2("6 Warum ist das wichtig?")
    d.punkte(["Banken nehmen Warenwertpapiere in der Praxis als Sicherheit, weil mit ihnen Rechte am Gut erworben werden können "
              "(zum Beispiel beim Dokumentenakkreditiv und Dokumenteninkasso).",
              "Der Frachtbrief dient als Nachweis des Transports, nicht als Sicherheit.",
              "Bei der Zuordnung entscheidet die Wirkung: Ist das Papier ein Anspruch auf Auslieferung des Gutes, oder dokumentiert es nur?"])
    d.h2("Quellen")
    d.punkte(["Handelsgesetzbuch (HGB): §§ 363, 408, 409, 418, 443, 444, 445, 448, 475c, 475g, 513, 514, 524 (Wortlaut: gesetze-im-internet.de, vor Einsatz prüfen)",
              "Ursprüngliches Info-Blatt der Lehrkraft und Prüfung vom 02.11.2026 (planung/Pruefung_Warenbegleitpapiere.md)"])
    d.speichern(pfad)


def arbeitsblatt_anpassungen(pfad):
    d = Dok(KOPF, "Arbeitsblatt „Warenbegleitpapiere unterscheiden“: Änderungsvorschläge", HINWEIS)
    d.p("Die Tabelle zeigt, welche Frage oder Antwortoption im Arbeitsblatt geändert werden sollte, warum und mit welcher "
        "Formulierung. Die Zuordnungsübung (Dokument und Beschreibung) bleibt bis auf einen Hinweis unverändert.")
    d.h2("Fragen im Arbeitsblatt")
    d.tabelle(["Stelle", "Bisher", "Problem", "Vorschlag"], [
        ["Frage 1: Funktion für die Überprüfung des Vertrags", "Antworten: Abrechnungsgrundlage, Quittungsfunktion, Sperrfunktion, Beweisfunktion",
         "Mehrdeutig: Auch die Frachtangaben dienen der Abrechnung.",
         "Frage ergänzen: „… zum Nachweis von Abschluss und Inhalt des Frachtvertrags“. Richtig bleibt die Beweisfunktion (§ 409 HGB)."],
        ["Frage 2: „reine Quittung“", "„Die Güter sind in einwandfreiem Zustand angekommen.“",
         "Der Frachtbrief bezieht sich auf die Übernahme durch den Frachtführer, nicht auf die Ankunft. „Einwandfrei“ ist zu stark: Es geht um den äußerlich guten Zustand.",
         "„Der Frachtführer hat das Gut bei der Übernahme ohne Vorbehalt in äußerlich gutem Zustand erhalten.“ Falsche Optionen: beschädigt angekommen, nicht unterschrieben, Transport abgebrochen."],
        ["Frage 3: Sperrfunktion", "„Der Absender kann keine nachträglichen Weisungen erteilen, nachdem der Frachtbrief aus der Hand gegeben wurde.“",
         "Falsch. Der Absender hat das Verfügungsrecht grundsätzlich. Ist es vorgeschrieben, kann er es nur gegen Vorlage der Absenderausfertigung ausüben (§ 418 Abs. 4 HGB).",
         "Richtige Option: „Der Absender kann nachträgliche Weisungen nur gegen Vorlage seiner Ausfertigung des Frachtbriefs erteilen, wenn das im Frachtbrief vorgeschrieben ist.“ Falsche Optionen wie bisher."],
        ["Frage 4: schnelle Zuordnung und Zahlung", "Abrechnungsgrundlage",
         "Die Funktion „Abrechnungsgrundlage“ steht im Auszug nicht als eigene Regel; sie ergibt sich aus den Frachtangaben im Frachtbrief (§ 408).",
         "Frage als Anwendungsfrage lassen (Frachtangaben im Frachtbrief), Antwort „Abrechnungsgrundlage“ beibehalten."],
        ["Frage 5: „unreine Quittung“", "„Die Güter weisen bei Übernahme oder Ablieferung Mängel auf.“",
         "Der Vorbehalt bezieht sich auf die Übernahme (§ 409 Abs. 2 HGB). Zur Ablieferung enthält der Auszug keine Regel.",
         "„Der Frachtführer hat bei der Übernahme einen begründeten Vorbehalt in den Frachtbrief eingetragen, zum Beispiel wegen beschädigter Verpackung.“"],
        ["Option „Kann-Papier“", "„Der Frachtbrief ist als ‚Kann-Papier‘ optional.“ (als falsche Option bei den Fragen 3 und 5)",
         "Richtig ist: Der Frachtführer kann die Ausstellung verlangen (§ 408 Abs. 1). Als falsche Antwort zu den Funktionsfragen ist die Option trotzdem ungeeignet, weil sie zu etwas anderem gehört.",
         "Eigene Frage: „Warum nennt man den Frachtbrief ein Kann-Papier?“ Antwort: Der Frachtführer kann die Ausstellung verlangen, sie ist nicht zwingend."],
        ["Offene Frage: Sperrpapier", "„Erkläre, was ein Sperrpapier ist …“",
         "Ohne Vorgabe sind sehr unterschiedliche Antworten möglich.",
         "Erwartung: Der Absender kann nachträglich Weisungen nur gegen Vorlage seiner Ausfertigung erteilen; der Frachtführer führt Weisungen ohne die Ausfertigung nicht aus."],
        ["Offene Frage: Wertpapier", "„Beschreibe, was ein Wertpapier im Kontext der Logistik ist …“",
         "Begriff ist weit. Gemeint ist das Warenwertpapier.",
         "Frage umformulieren: „… was ein Warenwertpapier (Traditionspapier) ist …“. Erwartung: Verbrieft den Anspruch auf Auslieferung; die Übergabe wirkt beim Erwerb von Rechten wie die Übergabe des Gutes; Auslieferung gegen Rückgabe."],
        ["Offene Frage: Vergleich Sperrpapier und Wertpapier", "„Vergleiche …“",
         "Beides sind keine gleichartigen Kategorien: Sperrpapier ist eine Funktion des Frachtbriefs, Warenwertpapier eine Art von Papier.",
         "Frage ändern: „Vergleiche Frachtbrief und Konnossement.“ Erwartung: Frachtbrief als Begleitpapier mit Beweis- und Sperrfunktion, Konnossement als Warenwertpapier mit Traditionswirkung."],
    ], [3.0, 3.6, 5.0, 5.4], 8.5)
    d.h2("Zuordnungstabelle (Abkürzungen)")
    d.punkte(["Die Zuordnungen sind in sich stimmig (CMR = Internationaler LKW-Frachtbrief, B/L = Handelbares Wertpapier in der Seefracht, "
              "FCR = Spediteur-Übernahmebescheinigung, FCT = Spediteur-Transportbescheinigung, FBL = FIATA Multimodal Transport Bill of Lading, "
              "AWB = Frachtbrief für die Luftfracht, CIM = Internationaler Bahntransport-Frachtbrief, SWR = FIATA Warehouse Receipt).",
              "Ergänzungsvorschlag bei B/L: „Konnossement, als Orderpapier durch Indossament übertragbar“.",
              "Diese Abkürzungen und die internationalen Übereinkommen (CMR, CIM) stehen nicht im HGB-Auszug und sind hier nicht geprüft."])
    d.h2("Buch Aufgabe 8 und 9 (LS 68)")
    d.tabelle(["Aufgabe", "Hinweis"], [
        ["Aufgabe 8: Zuordnung", "Konnossement, Ladeschein und Lagerschein = Warenwertpapier (2). Frachtbrief = Warenbegleitpapier (1). Die Einordnung von "
         "Ursprungszeugnis, Zollfaktura und Packliste als Begleitpapiere ist im HGB-Auszug nicht geregelt."],
        ["Aufgabe 9 a: „mehrfach ausgestellt … lediglich Informationen“", "Die Begründung ist nicht allgemein richtig, denn auch das Konnossement gibt es in mehreren Originalen. "
         "Zuordnung zu (1) bleibt plausibel."],
        ["Aufgabe 9 b: „verkörpert das Eigentum“", "Juristisch genauer: „verkörpert den Anspruch auf Auslieferung, die Übergabe wirkt wie die Übergabe der Ware“."],
        ["Aufgabe 9 d: „Verfügung nur bei Vorlage des Originals“", "Auch beim Frachtbrief kann die Vorlage der Absenderausfertigung nötig sein (Sperrfunktion). Als Zusatz für (2) merken: "
         "„und die Ware wird nur gegen Rückgabe des Papiers abgeliefert“."],
        ["Aufgabe 9 e: „für einen Kredit verpfändet“", "Die Verpfändung ist im HGB-Auszug nicht geregelt; sie gilt als Praxis der Banken."],
    ], [5.0, 12.0])
    d.speichern(pfad)


if __name__ == "__main__":
    from pathlib import Path
    Z = Path(__file__).resolve().parents[1] / "nextcloud" / "Block-III"
    Z.mkdir(parents=True, exist_ok=True)
    info_blatt(str(Z / "LS68_Info-Blatt_Warenbegleitpapiere_und_Warenwertpapiere_ueberarbeitet.docx"))
    arbeitsblatt_anpassungen(str(Z / "LS68_Arbeitsblatt_Warenbegleitpapiere_Aenderungsvorschlaege.docx"))
    print("ok")
