# Flussdiagramm für einen Algorithmus
## Entwickle ein Flussdiagramm für einen Algorithmus, der prüft, ob eine Zahl eine Primzahl ist.
### Schritte:
### 1. Nimm eine Zahl als Eingabe.
### 2. Überprüfe, ob die Zahl kleiner oder gleich 1 ist (nicht prim).
### 3. Überprüfe für alle Zahlen von 2 bis √n, ob es einen Teiler gibt.
### 4. Gib „Primzahl“ oder „Keine Primzahl“ aus.


# Pseudocode


# Umsetzung
while True:
    try:
        lower = int(input("Bei welcher ganzen Zahl soll die Aufzählung beginnen? "))
        upper = int(input("Bei welcher ganzen Zahl soll die Aufzählung enden? "))
    except ValueError:
        print("Das ist keine ganze Zahl gewesen!\n")
        continue
    if lower <= upper:
        break
    else:
        print("Die untere Grenze ist größer als die obere Grenze!\n")


if lower % 2 == 0:
    even = list(range(lower, upper + 1, 2))
    uneven = list(range(lower + 1, upper + 1, 2))
else:
    even = list(range(lower + 1, upper + 1, 2))
    uneven = list(range(lower, upper + 1, 2))


print("Gerade Zahlen:", even)
print("Ungerade Zahlen:", uneven)

# ODER

for x in range(2, 6):
    print(x)
