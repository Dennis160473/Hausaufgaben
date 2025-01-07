# Aufgabe 1: Zähle, wie oft etwas passiert (40 Punkte)
## Schreibe ein Programm, das die Häufigkeit eines Buchstabens in einem Text zählt.
### 1. Der Benutzer gibt einen Text und einen Buchstaben ein.
### 2. Dein Programm zählt mit einer Schleife, wie oft dieser Buchstabe im Text vorkommt.
### Bonus (5 Punkte): Zeichne ein Flussdiagramm für den Code.


def count_letters(text, letter):
    text = text.lower()
    letter = letter.lower()

    frequency = text.count(letter)

    return frequency


text = "The task is not easy."
letter = "t"
frequency = count_letters(text, letter)

print(f"The letter '{letter}' appears {frequency} times in the text.")

# Alternative


# Aufgabe 2: Summen und Durchschnitt berechnen (40 Punkte)
## Schreibe ein Programm, das:
### 1. Den Benutzer auffordert, 5 Zahlen einzugeben.
### 2. Mit einer Schleife die Summe und den Durchschnitt der Zahlen berechnet.
### 3. Die Ergebnisse ausgibt.
### Bonus (5 Punkte): Zeichne ein Flussdiagramm für die Berechnung.


sum = 0

for i in range(5):
    number = float(input(f"Enter {i+1}. the number: "))
    sum += number
    average = sum / 5
    print(f"The sum of the numbers entered is: {sum}")
    print(f"The average of the numbers entered is: {average}")


# Aufgabe 3: Muster mit Schleifen erstellen (20 Punkte)
## Erstelle ein Muster mit einer verschachtelten Schleife.


lines = 5
split = 10

for i in range(lines):
    for _ in range(split):
        print("-", end=" ")
    print()
