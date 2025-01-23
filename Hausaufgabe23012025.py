# Nutzt den folgenden Link, um die Aufgaben zu bearbeiten, die eurem Level in Python entsprechen:
# https://www.practicepython.org/

## Übungen

### Erstellen Sie ein Programm, das den Benutzer auffordert, seinen Namen und sein Alter einzugeben. Drucken Sie eine an den Benutzer adressierte Nachricht aus, die ihm mitteilt, in welchem ​​Jahr er 100 Jahre alt wird.

name = input("What is your name: ")  # Aufforderung des Users, den Namen einzugeben.
age = int(input("How old are you: "))  # Aufforderung des Users, das Alter einzugeben.
year = 2014 - age + 100  # Berechnung des Ergebnisses
print(
    name + ", you will be 100 years old in the year " + str(year)
)  # Rückgabe des Ergebnisses an den User.

### Fragen Sie den Benutzer nach einer Nummer. Je nachdem, ob die Nummer gerade oder ungerade ist, drucken Sie dem Benutzer eine entsprechende Nachricht aus.

num = input("Enter a number: ")  # Aufforderung des Users, eine Zahl einzugeben.
mod = num % 2  # Variable, zur Berechnung, ob gerade oder ungerade Zahl
if (
    mod > 0
):  # Hier wird die Funktion durchgeführt mit einer Wenn/Sonst Programmanweisung
    print("You picked an odd number.")  # Rückgabe des Ergebnisses an den User.
else:
    print("You picked an even number.")  # Rückgabe des Ergebnisses an den User.

### Nehmen Sie eine Liste, sagen wir zum Beispiel diese:
### a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
### und schreiben Sie ein Programm, das alle Elemente der Liste ausgibt, die kleiner als 5 sind.
### Anstatt die Elemente einzeln auszudrucken, erstellen Sie eine neue Liste, die alle Elemente dieser Liste kleiner als 5 enthält, und drucken Sie diese neue Liste aus.
### Schreiben Sie dies in einer Zeile Python.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # Anlegen der Variable mit einer Liste

# basic problem:
for (
    x
) in (
    a
):  # Die Schleife geht die, oben angelegte, Liste von vorn durch. Das x ist der Platzhalter für jedes Element der Liste, welches abgefragt wird.
    if x < 5:
        print(
            x
        )  # Hier wird das Ergebnis ermittelt und ausgegeben. Jede Zahl wird untersucht, ob Sie kleiner als 5 ist.

# combine challenges 1 and 2:
print(
    [x for x in a if x < 5]
)  # Dies komprimiert alles in einer Zeile. Nach der Eingabe!!!

### Erstellen Sie ein Programm, das den Benutzer nach einer Zahl fragt und dann eine Liste aller Teiler dieser Zahl ausgibt. (Wenn Sie nicht wissen, was ein Teiler ist: Es handelt sich um eine Zahl, die sich ohne Rest in eine andere Zahl teilen lässt. Beispielsweise ist 13 ein Teiler von 26, da 26 / 13 keinen Rest hat.)

num = int(
    input("Please choose a number to divide: ")
)  # Aufforderung des Users, eine Zahl einzugeben.

listRange = list(
    range(1, num + 1)
)  # Hier wird die Variable gesetzt mit dem Durchlauf der Teiler der eingegeben Zahl.

divisorList = []  # Hier wird das Ergebnis aus der Liste abgefragt.

for (
    number
) in (
    listRange
):  # Dies ist die Funktion mittels einer Schleife, um die eingegebene Zahl als Vorgabe für die, zu durchlaufende, Liste zu setzen.
    if (
        num % number == 0
    ):  # Das Ergebnis wird nun mathematisch mit den Zahlen aus der Liste errechnet.
        divisorList.append(number)  # Hier wird der Teiler ermittelt.

print(divisorList)  # Rückgabe des Ergebnis an den User.

### Nehmen Sie zwei Listen, sagen wir zum Beispiel diese beiden:
### a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] und b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
### und schreiben Sie ein Programm, das eine Liste zurückgibt, die nur die Elemente enthält, die beiden Listen gemeinsam sind (ohne Duplikate). Stellen Sie sicher, dass Ihr Programm mit zwei Listen unterschiedlicher Größe funktioniert.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # Anlegen der 1. Liste.
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Anlegen der 2. Liste
c = []  # Platzhalter für ermittelte Liste

for number in a and b:  # Diese Schleife geht beide angelegte Listen durch.
    if (
        number in a and b
    ):  # Die Funktion ermittelt die gleichen Zahlen in beiden Listen.
        c.append(
            number
        )  # Hier wird dann dynamisch die Ergebnisliste mit den ermittelten Zahlen angelegt.

print(c)  # Rückgabe der Ergebnisliste.

### Fordern Sie vom Benutzer eine Zeichenfolge an und geben Sie aus, ob diese Zeichenfolge ein Palindrom ist oder nicht. (Ein Palindrom ist eine Zeichenfolge, die vorwärts und rückwärts gleich gelesen wird.)


def reverse(word):  # Anlegen einer Definition für die Variable.
    x = ""  # Platzhalter für das Ergebnis
    for i in range(len(word)):  # Eine Schleife zur Überprüfung des eingegebenen Wortes.
        x += word[len(word) - 1 - i]  # Platzhalter wird mit Ergebnis gefüllt.
    return x  # Ergebnis soll zurück gegeben werden.


word = input("give me a word:\n")  # Aufforderung des Users, ein Palindrom einzugeben.
x = reverse(word)  # Abfrage der Ermittlung aus der Definition.
if (
    x == word
):  # Wenn/Funktion, ob eingegebenes Wort das selbige, wie aus der Definition ermittelte Wort ist.
    print("This is a Palindrome")  # Rückgabe an den User, ob es ein Palindrom ist.
else:
    print("This is NOT a Palindrome")  # Rückgabe an den User, ob es kein Palindrom ist.

### Nehmen wir an, ich gebe Ihnen eine in einer Variablen gespeicherte Liste: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Schreiben Sie eine Zeile Python, die aus dieser Liste aeine neue Liste erstellt, die nur die geraden Elemente dieser Liste enthält.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Anlegen der Liste
b = [
    element for element in a if element % 2 == 0
]  # Erstellung einer neuen Liste mit Funktion und Ergebnis.
print(b)  # Rückgabe der neu ermittelten Liste.

### Übung 8 = Hausaufgabe17122024_Aufgabe4.py
### Generieren Sie eine Zufallszahl zwischen 1 und 9 (einschließlich 1 und 9). Bitten Sie den Benutzer, die Zahl zu erraten, und teilen Sie ihm dann mit, ob er zu niedrig, zu hoch oder genau richtig geraten hat.
### Das Spiel wird fortgesetzt, bis der Benutzer „exit“ eingibt.
### Notieren Sie, wie viele Vermutungen der Benutzer angestellt hat, und drucken Sie diese nach Spielende aus.

import random  # Aufrufen und nutzen eines integrierten Datenpaketes.

rd = random.randint(
    1, 9
)  # # Automatisch generierte Zahl aus dem Datenpaket mit den notwendigen Inhalten.
guess = 0  # User tätigt Eingabe 0.
c = 0  # Es darf keine 0 eingegeben worden sein.
while (
    guess != rd and guess != "exit"
):  # Funktion wird angelegt, wenn der User "exit" eingibt.
    guess = input(
        "Enter a guess between 1 to 9"
    )  # Aufforderung des Users, eine Zahl zwischen 1 und 9 einzugeben.

    if guess == "exit":
        break  # # Programm wird beendet, wenn der User "exit" eingibt.

    guess = int(guess)  # Eingabe des Users wird als Zahl geprüft.
    c += 1  # Prüfung, ob eingegebene Zahl zwischen 1 und 9 ist.

    if (
        guess < rd
    ):  # Wenn/Funktion zur Überprüfung der eingegebenen Zahl mit der generierten Zahl.
        print("Too low")  # Rückgabe, wenn die eingegebene Zahl zu niedrig ist.
    elif (
        guess > rd
    ):  # Wenn/Funktion zur Überprüfung der eingegebenen Zahl mit der generierten Zahl.
        print("Too high")  # Rückgabe, wenn die eingegebene Zahl zu hoch ist.
    else:
        print("Right!")  # Rückgabe, wenn die eingegebene Zahl richtig geraten wurde.
        print("You took only", c, "tries!")  # Rückfrage, ob es weiter geht.
input()  # Das Programm wartet auf eine erneute Eingabe.

### Schreiben Sie ein Programm, das aus einer Liste von Zahlen (z. B. a = [5, 10, 15, 20, 25]) eine neue Liste mit nur den ersten und letzten Elementen der gegebenen Liste erstellt. Schreiben Sie diesen Code zur Übung in eine Funktion.

a = [5, 10, 15, 20, 25]


def list_ends(a_list):  # Hier wird der Aufruf und Nutzung der Liste definiert.
    return [
        a_list[0],
        a_list[len(a_list) - 1],
    ]  # Das Ergebnis der ausgeführten Funktion wird ausgegeben.


### Schreiben Sie einen Passwortgenerator in Python. Seien Sie kreativ bei der Generierung von Passwörtern – sichere Passwörter bestehen aus einer Mischung aus Kleinbuchstaben, Großbuchstaben, Zahlen und Sonderzeichen. Die Passwörter sollten zufällig sein und jedes Mal, wenn der Benutzer nach einem neuen Passwort fragt, ein neues Passwort generieren. Fügen Sie Ihren Code in eine Hauptmethode ein.
### Fragen Sie den Benutzer, wie stark sein Passwort sein soll. Wählen Sie für schwache Passwörter ein oder zwei Wörter aus einer Liste aus.

import random

accepted_chars = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
]


def password_generator():
    x = int(input("How many characters do you want in your new password? "))
    collection = []


for i in range(x):
    collection.append(accepted_chars[random.randint(0, len(accepted_chars) - 1)])
    new_pass = "".join(collection)
    print(new_pass)

pass_gen()

### Oder

import random

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
password = []
strength = input("You want your password to be 'STRONG' or 'WEAK' : ").lower()
if strength == "strong":
    while len(password) < 8:
        password.append(random.choice(alphabet))
        password.append((random.choice(alphabet)).upper())
        password.append(random.choice(symbols))
        password.append(random.choice(numbers))
elif strength == "weak":
    while len(password) < 8:
        password.append(random.choice(alphabet))
        password.append((random.choice(alphabet)).upper())

password = "".join(password)
print(password)
