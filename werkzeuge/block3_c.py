"""Block III, Teil C: Lernatelier und Lösungen Teil 2 für LS 66, 67, 68."""
from docx_helfer import Dok
from block1_b import STATUS
from block1_c import lernatelier
from block3_a import KOPF
import rechnen_block3 as r
de = r.de


def lernatelier_ls66(pfad):
    lernatelier(pfad, "LS 66", "Zwischen Eigen- und Fremdlager entscheiden", "Seiten 94 bis 97",
        ("5, 6, 7, 10", "Sie wollen Begriffe, Lagervertrag und Lagerschein sicher können."),
        ("1, 2, 3, 8", "Sie üben den Rechenweg zur kritischen Lagerfläche und die Entscheidung."),
        ("4, 9 und Zusatzaufgaben", "Sie übertragen den Rechenweg und prüfen Lagerscheine."),
        [("Plus", "Kostenvergleich in der Tabellenkalkulation",
          "Bauen Sie in OnlyOffice (Tabellenkalkulation) für Aufgabe 1 einen Kostenvergleich: Eingabefelder für Fixkosten, variable Kosten und Preis des "
          "Fremdlagers, Formel für die kritische Lagerfläche, Wertetabelle von 0 bis 8.000 m² und ein Liniendiagramm. Testen Sie, was passiert, wenn das "
          "Fremdlager 30 € je m² verlangt."),
         ("Kreativ", "Entscheidungsvorlage in einer Seite",
          "Schreiben Sie für die Geschäftsführung eine Entscheidungsvorlage (eine Seite) zu Aufgabe 3: Rechnung, Grafik, weitere Aspekte, Empfehlung."),
         ("BNE", "Nachhaltigkeit bei der Lagerwahl",
          "Welche ökologischen und sozialen Aspekte sollten bei der Entscheidung zwischen Eigen- und Fremdlager noch eine Rolle spielen "
          "(Energie, Fläche, Transportwege, Arbeitsbedingungen)? Ergänzen Sie Ihre Entscheidungsvorlage um einen Absatz.")])


def lernatelier_ls67(pfad):
    lernatelier(pfad, "LS 67", "Die Lagerhaltung mithilfe von Kennzahlen verbessern", "Seiten 102 bis 107",
        ("1, 3, 5, 6, 7, 13", "Sie wollen Lagerorganisation, Kostenarten und die Grundrechnungen sicher können."),
        ("8, 9, 10, 14, 15, 16, 19", "Sie vertiefen Kennzahlen und Lagerzinsen."),
        ("2, 4, 11, 12, 17, 18 und Zusatzaufgaben", "Sie deuten Kennzahlen und übertragen auf den Betrieb."),
        [("Plus", "Kennzahlen-Tabelle in der Tabellenkalkulation",
          "Bauen Sie für Aufgabe 9 eine Tabelle in OnlyOffice mit Formeln für den Ø Lagerbestand auf Monatsbasis, den Ø Lagerwert und die "
          "Umschlagshäufigkeit. Ergänzen Sie eine Bedingung, die Werkstoffe mit einer Umschlagshäufigkeit unter 3 farbig markiert."),
         ("Basis", "Fachartikel Kommissionierung (Festplatz- und Freiplatzsystem)",
          "Lesen Sie im Fachartikel „Erfolgsfaktor Kommissionierung“ (Ergänzendes Material) den Abschnitt zum Lagerhaltungssystem und beantworten Sie die "
          "Aufgaben 3 und 4 mit Argumenten aus dem Text."),
         ("Kreativ", "Kennzahlen im Betrieb",
          "Erfragen Sie in Ihrem Ausbildungsbetrieb (ohne vertrauliche Zahlen), welche Lagerkennzahlen genutzt werden, und erklären Sie sie an einem "
          "Beispiel für die Klasse."),
         ("BNE", "Lagerbestand und Ressourcen",
          "Überprüfen Sie, wie sich ein zu hoher Lagerbestand auf Ressourcen auswirkt (Energie, Fläche, Ausschuss, Entsorgung), und nennen Sie drei Maßnahmen, die "
          "Kennzahlen und Nachhaltigkeit verbinden.")])


def lernatelier_ls68(pfad):
    lernatelier(pfad, "LS 68", "Die geeignete Transportform auswählen", "Seiten 113 bis 116",
        ("1, 8, 9, 11, 18", "Sie wollen Transportdokumente, Akteure und Kostenarten sicher können."),
        ("6, 7, 10, 12, 14, 15, 16, 17", "Sie vertiefen Rechnungen (kritische Entfernung) und Entscheidungen."),
        ("2, 3, 4, 5, 13, 19, 20 und Zusatzaufgaben", "Sie recherchieren im Betrieb und übertragen."),
        [("Basis", "Info-Blatt und Arbeitsblatt zu Warenbegleit- und Warenwertpapieren",
          "Lesen Sie das Info-Blatt „Warenbegleitpapiere und Warenwertpapiere“ (Ergänzendes Material) und bearbeiten Sie das Arbeitsblatt „Warenbegleitpapiere "
          "unterscheiden“. Erklären Sie danach, warum der Frachtbrief kein Warenwertpapier ist."),
         ("Plus", "Nutzwertanalyse für den Auftrag der Go2Bike KG (IHK-Katalog)",
          "Vergleichen Sie für den zweiten Versandauftrag drei Möglichkeiten (KEP-Express, lokaler Kurier, Werkverkehr). Legen Sie Kriterien und Gewichte fest "
          "(zum Beispiel Kosten, Termintreue, Sendungsverfolgung, Haftung, Umwelt), vergeben Sie Punkte von 1 bis 5 und berechnen Sie den Nutzwert. Prüfen Sie, wie "
          "stark sich das Ergebnis ändert, wenn Sie die Gewichte verändern. Nutzen Sie Preise aus Ihrer Recherche."),
         ("Kreativ", "Erklärvideo „Frachtbrief oder Konnossement?“",
          "Erklären Sie in höchstens drei Minuten (Folien oder kurzes Video) den Unterschied zwischen Frachtbrief und Konnossement an einem Beispiel."),
         ("BNE", "CO2 beim Transport",
          "Berechnen Sie die Treibhausgasemissionen für die Beförderung von 720 kg Fahrrädern über 300 km mit Lkw, Bahn und Binnenschiff mit "
          "Emissionsfaktoren einer anerkannten Quelle (zum Beispiel Umweltbundesamt). Geben Sie die Quelle an und bewerten Sie die Ergebnisse (Dauer, Kosten, Umwelt).")])


def loesungen_ls66_teil2(pfad):
    d = Dok(KOPF + " · LS 66", "LS 66 Lösungen Teil 2: Aufgaben 1 bis 10 und Zusatzaufgaben", STATUS)
    L = [
     ("Aufgabe 1", f"Annahmen: Alle Werte in Euro pro Jahr; Abschreibung über {r.JAHRE1} Jahre. a) Fixkosten Eigenlager = Abschreibung = 2.450.000 : 14 = {de(r.ABSCHR1)} €/Jahr. "
      f"Kritische Lagerfläche: {de(r.ABSCHR1)} + 4,65 · x = 36,65 · x, also x = {de(r.ABSCHR1)} : 32,00 = {de(r.KRIT1)} m². Bei 5.000 m² (unter der kritischen Fläche): Eigenlager "
      f"{de(r.EIGEN_5000)} €, Fremdlager {de(r.FREMD_5000)} €. Das Fremdlager ist günstiger. b) Bei 15 Jahren Nutzung: Abschreibung {de(r.ABSCHR15)} €, kritische Fläche "
      f"{de(r.KRIT15)} m². 5.000 m² liegen weiter darunter, die Entscheidung für das Fremdlager bleibt. c) Ersparnis der laufenden Kosten bei 5.000 m²: "
      f"{de(r.FREMD_5000 - r.VAR1 * 5000)} € im Jahr; Amortisation: 2.450.000 : {de(r.FREMD_5000 - r.VAR1 * 5000)} ≈ {de(r.AMORT, 1)} Jahre (ohne Zinsen). Bei einer Nutzungsdauer von 14 oder 15 Jahren ist die Amortisation noch nicht erreicht; "
      "das Eigenlager lohnt sich bei 5.000 m² nicht."),
     ("Aufgabe 2", f"a) Bei 1.350 m² (unter der kritischen Fläche von 1.500 m²) ist das Fremdlager günstiger. b) Bei 10 % Wachstum pro Jahr: nach einem Jahr {de(r.W1)} m², nach "
      f"zwei Jahren {de(r.W2)} m² (über 1.500 m²), nach drei Jahren {de(r.W3)} m². Wenn das Wachstum zwei bis drei Jahre anhält, wird die kritische Fläche überschritten. "
      "Empfehlung: mittelfristig das Eigenlager planen; bis dahin Fremdlager mit kurzer Vertragsbindung nutzen."),
     ("Aufgabe 3", f"Annahmen: Alle Werte pro Monat. a) Kritische Fläche = 5.850 : (12,25 − 4,95) = {de(r.KRIT3)} m². Bei 750 m²: Eigenlager {de(r.EIGEN3)} €, Fremdlager {de(r.FREMD3)} €. "
      "Das Fremdlager ist günstiger; ab 802 m² würde sich die Sanierung lohnen. b) Grafik: Eigenlager beginnt bei 5.850 € und steigt um 4,95 € je m²; Fremdlager beginnt bei 0 € "
      "und steigt um 12,25 € je m²; Schnittpunkt bei ca. 801 m². c) Argumente für die Sanierung: Fläche für Wachstum, Kontrolle über das Lager, Unabhängigkeit von Vermieter und "
      "Mietpreisen, Möglichkeit zur Nutzung für weitere Zwecke, Bindung von Personal und Know-how, Identifikation. Argumente dagegen: Investitionsrisiko, "
      "Fixkosten bei geringerer Auslastung."),
     ("Aufgabe 4", f"a) Gesamtkosten Eigenlager bei 400 m²: 3.750 + 4,30 · 400 = 5.470 €. Damit die kritische Fläche 400 m² beträgt, muss der Preis des Fremdlagers je m² gleich 5.470 : 400 = {de(r.K4, 3)} € "
      "sein. b) ba Höherer Preis: Die kritische Fläche sinkt unter 400 m²; bei 400 m² ist das Eigenlager günstiger. bb Niedrigerer Preis: Die kritische Fläche steigt über 400 m²; "
      f"das Fremdlager ist günstiger. c) Es genügt, den Grenzpreis von {de(r.K4, 3)} €/m² zu kennen: Alle Anbieter mit höherem Preis sind teurer als das Eigenlager und können sofort "
      "aussortiert werden. Eine eigene Berechnung der kritischen Fläche je Anbieter ist nicht nötig."),
     ("Aufgabe 5", "a falsch (neben den Kosten zählen weitere Aspekte). b richtig. c richtig (liegen die variablen Kosten des Eigenlagers über dem Preis je m² des Fremdlagers, "
      "ist das Fremdlager wegen der zusätzlichen Fixkosten immer günstiger). d falsch (die kritische Fläche ist der Schnittpunkt der Gesamtkostenlinien beider Lager). "
      "e falsch (auch beim Fremdlager entstehen Kosten, nur nicht als Fixkosten)."),
     ("Aufgabe 6", "Beispiel „Zahlung der Vergütung“: Recht des Lagerhalters. a Einlagerung der Ware: Pflicht (das Gut muss angenommen und gelagert werden). "
      "b Aushändigung von Begleitdokumenten: Pflicht (zum Beispiel Lagerschein auf Verlangen des Einlagerers). c Haftung bei Verlust oder Beschädigung: Pflicht (Obhutshaftung des Lagerhalters). "
      "d Kündigung des Lagervertrags: Recht (beider Seiten, in vereinbarter Frist). e Herausgabe der Ware: Pflicht (Rückgabe auf Verlangen, bei Lagerschein gegen Rückgabe). "
      "Rechtsgrundlage: Lagergeschäft, §§ 467 ff. HGB (Wortlaut vor dem Einsatz prüfen)."),
     ("Aufgabe 7", "a) Der Lagerhalter liefert nur gegen Rückgabe des Lagerscheins aus, weil der Lagerschein den Anspruch auf Auslieferung verbrieft und nur der Inhaber legitimiert ist. "
      "b) Gibt er die Ware ohne den Lagerschein heraus, kann ein anderer rechtmäßiger Inhaber des Lagerscheins noch Ansprüche gegen ihn geltend machen; er riskiert doppelte Leistung und Schadenersatz."),
     ("Aufgabe 8", "a) Der Lagerschein nennt Lagerhalter, Ware (nur „mehrere Kisten“), Lagerdauer und Unterschrift. Es fehlen: Name des Einlagerers, Anzahl und Zeichen der Packstücke, "
      "Gewicht, Gefahrgutangabe, Lagerort, Lagerbuch- und Lagerscheinnummer, Versicherung, Auslieferungsklausel und Rechtsgrundlage. Er ist unvollständig. b) Ein einwandfreier "
      "Lagerschein ist Beweis für die Einlagerung (Art und Menge), legitimiert den Inhaber und kann als Warenwertpapier die Rechte am Gut übertragen; deshalb muss er genau sein."),
     ("Aufgabe 9", f"a) Der Lagerschein lautet „für … oder dessen legitimierten Rechtsnachfolger“ ohne Orderklausel, also ein Namenslagerschein (kein Orderpapier). b) Ausfüllen: Lagerbuch-Nr. 005/20XX, Lagerschein-Nr. 108/20XX, "
      f"Lagerhalter YourSpace GmbH, Neue Industriestraße 15, 90941 Nürnberg. Am 20.01.20XX lagerten wir für Karl Gustav Bömke, Münchner Straße 67, 90402 Nürnberg, in Nürnberg ein: "
      f"{r.KARTONS} Kartons (600 Stoffplüschtiere, davon je 200 Bären, Hasen, Elefanten, zu je 25 Stück), Bruttogewicht {r.GEWICHT} kg (24 · 18 kg), kein Gefahrgut, Trennungslager (getrennt von anderen Partien), "
      f"Lagerort Neue Industriestraße 15. Versicherung Elementarrisiken: Wert {de(r.WERT)} € (600 · 5,75), Prämie 2 % = {de(r.PRAEMIE)} €. Lagerkosten: {r.KARTONS} · 1,75 € · 3 Wochen = {de(r.KOSTEN)} €. "
      "c) Bei bestimmter Lagerzeit kann der Lagerhalter nicht ohne Weiteres vorzeitig herausgeben bzw. auf Vergütung verzichten; ob der Einlagerer das Gut vorzeitig zurückverlangen kann, ist in § 473 HGB geregelt "
      "(Wortlaut vor dem Einsatz prüfen). d) Der Lagerhalter hat ein Pfandrecht an dem Gut für seine Forderungen (Lagergeld) und darf die Herausgabe bis zur Zahlung verweigern (Rechtsgrundlage "
      "prüfen, zum Beispiel § 475b HGB)."),
     ("Aufgabe 10", "a Inhaberlagerschein: Übertragung durch Einigung und Übergabe (Zuordnung 2). b Orderlagerschein: Übergabe mit Indossament (Zuordnung 5). c Namenslagerschein: "
      "Abtretung der Rechte und Übergabe (Zuordnung 3). Zuordnung 1, 4: nicht passend (neuer Lagerschein, Korrektur der Namensangabe). Zuordnung mit dem Heft abgleichen."),
    ]
    d.tabelle(["Aufgabe", "Lösungsvorschlag"], [[a, b] for a, b in L], [2.6, 14.4])
    d.h2("Zusatzaufgaben")
    d.tabelle(["Aufgabe", "Erwartungen"], [
        ["Plus: Tabellenkalkulation", "Eingabefelder für Fixkosten, variable Kosten und Preis des Fremdlagers; Formel x = Fixkosten : (Preis Fremdlager − variable Kosten); Wertetabelle "
         "und Liniendiagramm mit zwei Geraden; Schnittpunkt bei 5.468,75 m². Bei 30 € je m² (günstigeres Fremdlager) steigt die kritische Fläche auf 175.000 : (30,00 − 4,65) = "
         "6.903,35 m², das Fremdlager bleibt also länger günstiger."],
        ["Kreativ: Entscheidungsvorlage", "Kriterien: Rechnung nachvollziehbar, Grafik beschriftet, mindestens vier weitere Aspekte gewichtet, klare Empfehlung."],
        ["BNE", "Zum Beispiel: Energieverbrauch und Fläche des Eigenlagers, Transportwege zum Fremdlager, Arbeitsbedingungen im Lager, Verantwortung des Lagerhalters."],
    ], [4.0, 13.0])
    d.speichern(pfad)
