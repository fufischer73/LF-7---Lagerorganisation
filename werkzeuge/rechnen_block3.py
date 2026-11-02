"""Rechnungen für Block III (LS 66, 67, 68). Alle Zahlen in den Lösungen stammen aus diesem Modul und werden hier geprüft."""


def de(x, n=2):
    x = round(x + (1e-9 if x >= 0 else -1e-9), n)   # kaufmännisch runden (0,5 auf)
    s = f"{x:,.{n}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------- LS 66
# Aufgabe 1
AB1 = 2_450_000.0; FREMD1 = 36.65; VAR1 = 4.65; JAHRE1 = 14
ABSCHR1 = AB1 / JAHRE1
KRIT1 = ABSCHR1 / (FREMD1 - VAR1)
EIGEN_5000 = ABSCHR1 + VAR1 * 5000
FREMD_5000 = FREMD1 * 5000
ABSCHR15 = AB1 / 15
KRIT15 = ABSCHR15 / (FREMD1 - VAR1)
AMORT = AB1 / (FREMD_5000 - VAR1 * 5000)
assert round(ABSCHR1) == 175000 and round(KRIT1, 2) == 5468.75 and round(AMORT, 2) == 15.31
# Aufgabe 2
W0 = 1350.0; KRIT2 = 1500.0
W1, W2, W3 = W0 * 1.1, W0 * 1.1 ** 2, W0 * 1.1 ** 3
assert W1 < KRIT2 < W2
# Aufgabe 3
F3 = 5850.0; V3 = 4.95; M3 = 12.25; B3 = 750
KRIT3 = F3 / (M3 - V3)
EIGEN3 = F3 + V3 * B3; FREMD3 = M3 * B3
assert round(KRIT3, 2) == 801.37 and EIGEN3 > FREMD3
# Aufgabe 4
F4 = 3750.0; V4 = 4.30; B4 = 400
K4 = (F4 + V4 * B4) / B4
assert round(K4, 3) == 13.675
# Arbeitsblatt 66.1
FIX661 = 3750 + 2335 + 125 + 185
VAR661 = 4.20 + 6.30
FREMD661 = 28.50
KRIT661 = FIX661 / (FREMD661 - VAR661)
EIGEN500 = FIX661 + VAR661 * 500; FREMD500 = FREMD661 * 500
assert FIX661 == 6395 and round(KRIT661, 2) == 355.28 and round(EIGEN500) == 11645 and FREMD500 == 14250
# Aufgabe 9 (Lagerschein Bömke)
KARTONS = 600 // 25; WERT = 600 * 5.75; PRAEMIE = WERT * 0.02; GEWICHT = KARTONS * 18; KOSTEN = KARTONS * 1.75 * 3
assert KARTONS == 24 and WERT == 3450 and round(PRAEMIE, 2) == 69.0 and GEWICHT == 432 and KOSTEN == 126

# ---------------- LS 67
ARTIKEL = {  # AB, EB, Abgänge
    "701S": (32, 53, [280, 49]),
    "701M": (6, 7, [4, 7, 8]),
    "701L": (50, 31, [25, 14, 21, 17, 15, 22, 25]),
    "701XL": (50, 88, [40, 25, 10, 45]),
    "701XXL": (28, 27, [27, 12, 25, 5, 25, 27]),
}
VORJAHR = {"701S": 2, "701M": 4, "701L": 6, "701XL": 5, "701XXL": 4}
KENN = {}
for a, (ab, eb, abg) in ARTIKEL.items():
    absatz = sum(abg); avg = (ab + eb) / 2; uh = absatz / avg; dauer = 360 / uh
    KENN[a] = dict(absatz=absatz, avg=avg, uh=uh, dauer=dauer)
assert KENN["701S"]["absatz"] == 329 and KENN["701XL"]["absatz"] == 120 and KENN["701L"]["absatz"] == 139
# Aufgabe 7
def aufg7():
    a = dict(); uh = 58 / 40; a["a"] = (uh, 360 / uh)
    ab = 3850 * 4.20; a["b"] = (ab, 360 / 4.20)
    uh_c = 360 / 35; avg_c = 6300 / uh_c; a["c"] = (uh_c, avg_c)
    uh_d = 450 / 65; a["d"] = (uh_d, 360 / uh_d)
    ab_e = 420 * 5.75; a["e"] = (ab_e, 360 / 5.75)
    return a
A7 = aufg7()
assert abs(A7["b"][0] - 16170) < 1e-6 and abs(A7["c"][1] - 612.5) < 1e-6 and abs(A7["e"][0] - 2415) < 1e-6
# Aufgabe 8
END8 = [28, 21, 15, 10, 5, 23, 16, 10, 4, 23, 16, 11]
AB8, BEST8, MIN8, EP8 = 34, 25, 6, 85.25
AVG8_J = (AB8 + END8[-1]) / 2; AVG8_M = (AB8 + sum(END8)) / 13; AVG8_B = MIN8 + BEST8 / 2
assert sum(END8) == 182 and AVG8_J == 22.5 and AVG8_B == 18.5
# Aufgabe 9
def werkstoff(ab, monate, preis):
    bestand, ends, verbrauch = ab, [], 0
    for m in monate:
        for z in m:
            bestand += z
            if z < 0:
                verbrauch += -z
        ends.append(bestand)
    avg = (ab + sum(ends)) / 13
    return dict(ends=ends, verbrauch=verbrauch, avg=avg, wert=avg * preis, uh=verbrauch / avg)
W1_ = werkstoff(25, [[-3], [-13], [-7, 30], [-4], [-8], [-9], [-11, 30], [-3], [-15], [-7], [-3, 30], [-9]], 16.50)
W2_ = werkstoff(58, [[-3], [-9], [-7], [-6], [-9], [-2], [-5], [-2], [-6], [-5, 25], [-4], [-5]], 52.50)
W3_ = werkstoff(10, [[-2], [-2], [-2, 36], [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-2]], 26.00)
assert W1_["verbrauch"] == 92 and W1_["ends"][-1] == 23 and W2_["verbrauch"] == 63 and W2_["ends"][-1] == 20 and W3_["verbrauch"] == 24
# Aufgabe 10
ABG10 = [("04.07.", -5), ("07.07.", -3), ("15.07.", -2), ("29.07.", -11), ("01.08.", 25), ("06.08.", -6), ("14.08.", -5),
         ("26.08.", -4), ("31.08.", -5), ("01.09.", 25), ("05.09.", -4), ("11.09.", -7), ("20.09.", -4), ("28.09.", -6), ("30.09.", -1)]
b = 22; BEST10 = []
for d, z in ABG10:
    b += z; BEST10.append((d, z, b))
ABSATZ10 = -sum(z for _, z in ABG10 if z < 0)
EB_JUL = BEST10[3][2]; EB_AUG = BEST10[8][2]; EB_SEP = BEST10[-1][2]
AVG10_M = (22 + EB_JUL + EB_AUG + EB_SEP) / 4
UH10 = ABSATZ10 / AVG10_M; DAUER10 = 90 / UH10; AVG10_J = (22 + EB_SEP) / 2
assert ABSATZ10 == 63 and EB_JUL == 1 and EB_AUG == 6 and EB_SEP == 9
# Aufgabe 11
UH11_Q1, UH11_Q2 = 378 / 72, 239 / 72; UH11_J = (378 + 239) * 2 / 72
# Aufgabe 12
SPIEL = {"Bauklötze": (18.50, 56, 28), "Ballspiel": (10.75, 23, 39), "Puzzle": (12.50, 64, 239),
         "Holzspielfiguren": (22.00, 18, 72), "Autorennbahn": (48.50, 31, 108)}
SP = {}
for n, (vp, avg, ab) in SPIEL.items():
    uh = round(ab / avg, 1); SP[n] = (uh, ab / avg, 90 / (ab / avg), vp * ab)
# Aufgabe 14
UH14 = 2.55; DAUER14 = 360 / UH14; ZS14 = 0.085 * DAUER14 / 360; ZINS14 = 87 * 378 * ZS14
# Aufgabe 15
ZS15 = 750 / 46500; DAUER15 = ZS15 * 360 / 0.0925; ZINS15_100 = 46500 * 0.0925 * 100 / 360
# Aufgabe 16
ZINS16 = 6925 * 0.045 / 12; GES16 = 2540 + ZINS16; STK16 = 6925 / 138.50; JE16 = GES16 / STK16
assert STK16 == 50
# Aufgabe 17
FL17 = 625 + 285 + 230; AUS17 = 455 + 148 + 182; NG17 = AUS17 / FL17

# ---------------- LS 68
FIX14 = 3550 * 12 + 28552.5; SP14 = 4.75; VAR14 = 2.10
KRIT14 = FIX14 / (SP14 - VAR14)
EIGEN14 = FIX14 + VAR14 * 14350; FREMD14 = SP14 * 14350
assert round(KRIT14) == 26850 and EIGEN14 > FREMD14
MON15 = 560 + 1500 / 12 + 18000 / 12 + 3600 / 12 + 1600
FREMD15 = 8000 * 0.49
FIX15 = 560 + 1500 / 12 + 1600; VARKM15 = (18000 / 12 + 3600 / 12) / 8000
KRIT15M = FIX15 / (0.49 - VARKM15)
assert round(MON15, 2) == 4085.0 and round(FREMD15, 2) == 3920.0
KM16 = [250, 230, 264, 210, 218, 220, 285, 302, 276, 268, 255, 222]
assert sum(KM16) == 3000
PAL = 40 // 5 // 4  # Paletten
assert PAL == 2
