### Aufgabe 2.1: Einfache Mathematik

zahl1 = 4
zahl2 = 2
print("Zahl 1 + Zahl 2:", zahl1 + zahl2)
print("Zahl 1 - Zahl 2:", zahl1 - zahl2)
print("Zahl 1 * Zahl 2:", zahl1 * zahl2)
print("Zahl 1 / Zahl 2:", zahl1 / zahl2)


### Aufgabe 2.3 Kilometer in Meilen umrechnen: 1 Kilometer = 0.621371 Meilen


print("Meilen <-> Kilometer")
faktor = 0.621371

print("(1) Meilen -> Kilometer")
print("(2) Kilometer -> Meilen")
print("(3) Beenden")
auswahl = int(input("Deine Wahl: "))

if auswahl == 1:
    s = float(input("Strecke in Meilen: "))
    s = s / faktor
    print(f"Das sind {s}= Kilometer")
elif auswahl == 2:
    s = float(input("Strecke in Kilometern: "))
    s = s * faktor
    print(f"Das sind {s}= Meilen")
else:
    print("Diese Eingabe war nicht vorgesehen")

print("Ende des Programms")
