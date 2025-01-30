def begruessung(name):
    # Der Parameter muss in einer einfachen () definiert werden.
    print("Hallo, " + name)


# Der Parameter heißt (name). Im print-Befehl wurde Parameter (Name) falsch hinterlegt.
# Der print-Befehl muss eingerückt werden, damit Er innerhalb der Definition ausgeführt wird.


def addiere_zahlen(a, b):
    # Bei Definition einer Funktion muss am Ende stets ein : gesetzt werden.
    ergebnis = a + b
    return ergebnis


# Die Ausgabe "ergebis" wurde falsch geschrieben. Korrekt ist "ergebnis".
# Es gibt keine Definition für ergebis.


def subtrahiere_zahlen(a, b):
    return a - b


# Es gibt noch keine Definition für Variable c.


def main():
    # Bei Definition einer Funktion muss am Ende stets ein : gesetzt werden.
    zahl1 = int(input("Gib eine Zahl ein: "))
    zahl2 = int(input("Gib eine weitere Zahl ein: "))

    summe = addiere_zahlen(zahl1, zahl2)
    print(f"Die Summe ist: {summe}")
    # Die Definition heißt main und nicht summe.
    differenz = subtrahiere_zahlen(zahl1, zahl2)
    print(f"Die Differenz ist: {differenz}")

    begruessung("Max")


if __name__ == "__main__":
    # In der Funktion müssen bei einem Vergleich stets 2 == gesetzt werden.
    main()


# Die Funktion muss innerhalb der Definition liegen. Daher eingerückt sein.
# Es muss ein break erfolgen. Sonst Endlosschleife.
