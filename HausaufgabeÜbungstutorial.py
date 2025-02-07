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


## Erstellen Sie ein Programm, das mit dem Benutzer das Spiel „Kühe und Bullen“ spielt.
## Das Spiel funktioniert folgendermaßen:
### Generieren Sie nach dem Zufallsprinzip eine 4-stellige Zahl. Bitten Sie den Benutzer, eine 4-stellige Zahl zu erraten.
### Für jede Ziffer, die der Benutzer an der richtigen Stelle richtig erraten hat , erhält er eine „Kuh“.
### Für jede Ziffer, die der Benutzer an der falschen Stelle richtig erraten hat , erhält er einen „Bullen“.
### Sagen Sie dem Benutzer bei jedem Raten, wie viele „Kühe“ und „Bullen“ er hat.
### Sobald der Benutzer die richtige Zahl errät, ist das Spiel vorbei.
### Notieren Sie die Anzahl der Vermutungen des Benutzers während des Spiels und teilen Sie sie dem Benutzer am Ende mit.

import random


def compare_numbers(number, user_guess):
    cowbull = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


if __name__ == "__main__":
    playing = True
    number = str(random.randint(0, 9999))
    guesses = 0

    print("Let's play a game of Cowbull!")
    print(
        "I will generate a number, and you have to guess the numbers one digit at a time."
    )
    print(
        "For every number in the wrong place, you get a cow. For every one in the right place, you get a bull."
    )
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number, user_guess)
        guesses += 1

        print(
            "You have "
            + str(cowbullcount[0])
            + " cows, and "
            + str(cowbullcount[1])
            + " bulls."
        )

        if cowbullcount[1] == 4:
            playing = False
            print(
                "You win the game after "
                + str(guesses)
                + "! The number was "
                + str(number)
            )
            break
        else:
            print("Your guess isn't quite right, try again.")


## Schreiben Sie eine Funktion, die eine geordnete Liste von Zahlen (eine Liste, deren Elemente in der Reihenfolge vom kleinsten zum größten sind) und eine andere Zahl annimmt.
## Die Funktion entscheidet, ob die angegebene Zahl in der Liste enthalten ist oder nicht, und gibt einen entsprechenden Booleschen Wert zurück (und druckt ihn dann aus).
## Zusatz: Verwenden Sie die binäre Suche.


import random


def binary_search(lst, num):
    lst.sort()
    if len(lst) == 0:
        return False
    else:
        found = ""
        midpt = len(lst) // 2
        midel = lst[midpt]
        if midel == num:
            found = 1
        elif midel > num:
            lst = lst[:midpt]
        elif midel < num:
            lst = lst[midpt + 1 :]
        result = True if found == 1 else binary_search(lst, num)
        return result


if __name__ == "__main__":
    a = [random.randint(0, 100) for i in range(100)]
    print(sorted(a))
    num = int(input("Find : "))
    print(binary_search(a, num))

## Gegeben seien zwei .txtDateien, die Zahlenlisten enthalten. Suchen Sie die Zahlen, die sich überschneiden.
## Eine .txtDatei enthält eine Liste aller Primzahlen unter 1000 und die andere .txtDatei eine Liste mit Glückszahlen bis 1000.

primeslist = []
with open("primenumbers.txt") as primesfile:
    line = primesfile.readline()
    while line:
        primeslist.append(int(line))
        line = primesfile.readline()

happieslist = []
with open("happynumbers.txt") as happiesfile:
    line = happiesfile.readline()
    while line:
        happieslist.append(int(line))
        line = happiesfile.readline()

overlaplist = []
for elem in primeslist:
    if elem in happieslist:
        overlaplist.append(elem)

print(overlaplist)


## Fragen Sie den Benutzer, welche Größe das Spielbrett haben soll, das er zeichnen möchte, und zeichnen Sie es mithilfe einer Python- printAnweisung für ihn auf den Bildschirm.

def horiz_line():
    print(" --- " * board_size)

def print_vert_line():
    print("|   " * (board_size + 1))

if __name__ == "__main__":
        board_size = int(input("What size of game board? "))

for index in range(board_size):
        print_horiz_line()
        print_vert_line()
        print horiz_line()


## Sie, der Benutzer, haben eine Zahl zwischen 0 und 100 im Kopf.
## Das Programm errät eine Zahl und Sie, der Benutzer, sagen, ob sie zu hoch, zu niedrig oder Ihre Zahl ist.
## Am Ende dieses Austauschs sollte Ihr Programm ausdrucken, wie viele Versuche nötig waren, um Ihre Nummer zu ermitteln.

import random

# Awroken

MINIMUM = 0
MAXIMUM = 100
NUMBER = random.randint(MINIMUM, MAXIMUM)
TRY = 0
RUNNING = True
ANSWER = None

while RUNNING:
    print("Is it %s?" % str(NUMBER))
    ANSWER = raw_input()
    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
        NUMBER -= random.randint(1, 4)
    elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
        NUMBER += random.randint(1, 4)
    elif ANSWER.lower() == "no":
        print("Higher or lower?")
        ANSWER = raw_input()
        if ANSWER.lower() == "higher":
            NUMBER += random.randint(1, 4)
        elif ANSWER.lower() == "lower":
            NUMBER -= random.randint(1, 4)
    elif ANSWER.lower() == "yes":
        if TRY < 2:
            print("Yes! It only took me %s try!" % str(TRY))
        elif TRY < 2 and TRY < 10:
            print("Pretty well for a robot, %s tries." % str(TRY))
        else:
            print("That's so bad, %s tries." % str(TRY))
        RUNNING = False
    TRY += 1
    
print("Thanks for the game!")


## Für diese Übung werden wir die Geburtstage unserer Freunde notieren und diese Informationen anhand ihres Namens finden.
## Erstellen Sie ein Wörterbuch (in Ihrer Datei) mit Namen und Geburtstagen.
## Wenn Sie Ihr Programm ausführen, sollte es den Benutzer auffordern, einen Namen einzugeben, und ihm den Geburtstag dieser Person zurückgeben.

if __name__ == '__main__':
    birthdays = {
        'Anna': '03/14/1879',
        'Max': '01/17/1706',
        'Robert': '12/10/1815',
        'Unbekannt': '06/14/1946',
        'Ich': '01/6/1955'}

    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for key in birthday_dictionary:
        print(key)

while True:
    name = input("Who's birthday do you want to look up? ")
    if name in birthday_dictionary:
        print(birthday_dictionary[name])
else:
        print("Sorry, we don't have this person's birthday.")


## Ändern Sie in dieser Übung Ihr Programm so, dass das Geburtstagswörterbuch aus einer JSON-Datei auf der Festplatte geladen wird, anstatt das Wörterbuch im Programm zu definieren.
## Bonus : Bitten Sie den Benutzer um den Namen und das Geburtsdatum eines anderen, um diese dem Wörterbuch hinzuzufügen, und aktualisieren Sie die JSON-Datei auf Ihrer Festplatte mit dem Namen.
## Wenn Sie das Programm mehrmals ausführen und immer wieder neue Namen hinzufügen, sollte Ihre JSON-Datei immer größer werden.

import json

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

def add_entry():
    name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
    date = input('When is {} born?\n'.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print('{} was added to my birthday list\n'.format(name))

def find_date():
    name = input("who's birthday do you want to know?\n").title()
    try :
        if birthday[name]:
            print('{} is born on {}\n'.format(name, birthday[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))

def list_entries():
    print('The current entries in my birthday list are:\n============================================')
    for key in birthday:
        print(key.ljust(31), ':', birthday[key])
    print()

while True:
    what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
    if what_next == 'Quit':
        print('Good Bye')
        raise SystemExit(0)
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_date()
    elif what_next == 'List':
        list_entries()



## In dieser Übung laden Sie diese JSON-Datei von der Festplatte, extrahieren die Monate aller Geburtstage und zählen, wie viele in jedem Monat Geburtstag haben.

import json
from collections import Counter

with open("birthdays.json", "r") as f:
	birthdays = json.load(f)

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

months = []
for name, birthday_string in birthdays.items():
	month = int(birthday_string.split("/")[0])
	months.append(num_to_string[month])

print(Counter(months))


##  In dieser Übung verwenden Sie die Python-Bibliothek Bokeh , um mithilfe meiner JSON-Datei mit den Geburtstagen ein Histogramm zu erstellen, das die Monate zeigt, in denen die Eingetragenen Geburtstag haben.

from collections import Counter
import json
import math

from bokeh.plotting import figure, show, output_file


DATA_FILE = "scientist_birthdays.json"
output_file("plot.html")

with open(DATA_FILE, "r") as f:
    DATA = json.load(f)

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = []
for name, birthday_string in DATA.items():
    month = int(birthday_string.split("/")[0])
    months.append(num_to_string[month])
months = Counter(months)

months, counts = list(zip(*months.items()))

categories = list(num_to_string.values())
p = figure(x_range=categories, title="Scientists' Birthday Months")
p.xaxis.major_label_orientation = math.pi/4
p.vbar(x=months, top=counts)

show(p)


## 