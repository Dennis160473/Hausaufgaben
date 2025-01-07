# Namensaufforderung

name1 = input("Wie lautet Ihr Vorname: ")
name2 = input("Wie lautet Ihr Nachname: ")
print(f"Hallo, {name1 + " " + name2}")



# Addition von Zahlen

zahl1 = input("Bitte geben Sie die erste Zahl ein: ")
zahl2 = input("Bitte geben Sie die zweite Zahl ein: ")
zahl1 = int(zahl1)
zahl2 = int(zahl2)
print(f"Das Ergebnis ist: {zahl1+zahl2}")


# Zusatzaufgabe: Einfache If-Bedingung

Eingabe = input("Bitte Zahl eingeben: ")
if int(Eingabe) > 0:
    print("Ihre Zahl ist negativ.")
elif int(Eingabe) < 0:
    print("Ihre Zahl ist positiv.")
else: 
    print("Ihre Zahl ist 0")
print ("Ergebnis wurde angegeben!")



