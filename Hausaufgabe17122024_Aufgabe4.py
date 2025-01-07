# Aufgabe 4: Schere Stein Papier
## Aufgabenstellung:
# ○ Schreibe eine Datei, die beim Ausführen mit dem Benutzer “Schere Stein Papier” spielt.
# ○ Der User soll nach einer Auswahl gefragt werden.
# ○ Fangt falsche Werte ab.
# ○ Der Computer wählt per Zufall eine Option.
# ○ Die Wahl des Computers sowie der Gewinner sollen auf dem Terminal ausgegeben werden.
# ○ Tipp: Nutze das random Paket und die Funktion random.choice([“Schere”, “Stein”, “Papier”]) um den Computer aus einer Liste von Möglichkeiten auswählen zu lassen.


user = input("Please choose: Schere, Stein, Papier - ")
import random

Computer = ["Schere", "Stein", "Papier"]


def selectRandom(Computer):
    return random.choice(Computer)


print("The name selected is: ", selectRandom(Computer))
print(f"Player: {user}, Opponent: {selectRandom(Computer)}")

if user == selectRandom(Computer):
    print(f"Same choice {user}. Draw")
elif user == "Schere" and selectRandom(Computer) == "Stein":
    print("Rock beats scissors. Point for computer")
elif user == "Schere" and selectRandom(Computer) == "Papier":
    print("Scissors beats paper. Point for player")
elif user == "Stein" and selectRandom(Computer) == "Papier":
    print("Rock loses to paper. Point for computer")
elif user == "Stein" and selectRandom(Computer) == "Schere":
    print("Rock beats scissors. Point for player")
elif user == "Papier" and selectRandom(Computer) == "Schere":
    print("Paper loses to scissors. Point for computer")
elif user == "Papier" and selectRandom(Computer) == "Stein":
    print("Paper beats rock. Point for player")

play_again = input("Want to play another round? Y/N ")
if play_again.lower != "Y":
    print("New game")
else:
    print("End of Game")
