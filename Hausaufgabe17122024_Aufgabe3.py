# Aufgabe 3: Programmierübungen vom Vormittag


# Aufgabe 3.1
def calc_area(width, height):
    return width * height


width = float(input("Please enter a number? "))
height = float(input("Please enter a number? "))

print(f"The result of the area is {alc_area(width * height)}.")


# Aufgabe 3.2 + 3.3
print("Meilen <-> Kilometer")
faktor = 1.60934

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


# Aufgabe 3.4

# Umrechnungsformeln
# von Fahrenheit in Celsius
# (F - 32) * 5/9:
# von Celsius nach Fahrenheit
# (C * 1,8 + 32):


# Umrechnung in Fahrenheit
def celsius_to_fahrenheit(result):
    return result


user = float(input("Please enter a number? "))
result = (user * 1.8) + 32

if celsius_to_fahrenheit(result):
    print(f"Ihr Ergebnis in Fahrenheit ist {result}. ")
else:
    print()


# Umrechnung in Celsius


def fahrenheit_to_celsius(result):
    return result


user = float(input("Please enter a number? "))
result = (user - 32) * (5 / 9)

if fahrenheit_to_celsius(result):
    print(f"Ihr Ergebnis in Celsius ist {result}. ")
else:
    print()
