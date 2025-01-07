# Eingabe des Datum durch den User
date = input("Please enter the date: ")

# Variablen der Feriendaten
is_winter = date <= "2025.12.24" and date <= "2025.01.01"
is_spring = date <= "2025.04.18" and date >= "2025.04.21"
is_summer = date <= "2025.08.11" and date >= "2025.08.19"
is_winter2 = date <= "2025.12.24" and date >= "2026.01.01"

# Abfrage der Ferien
if is_winter:
    print("Winterferien 2024. Jippiiiiie")
elif is_spring:
    print("Osterferien. Jippiiiiie")
elif is_summer:
    print("Sommerferien. Jippiiiiie")
elif is_winter2:
    print("Winterferien 2025. Jippiiiiie")
else:
    print("normale Kurswoche")


# Zusatzdaten

# Feiertage
# Eingabe des Datum durch den User
date = input("please enter the holiday date (yyyy.mm.dd): ")

# Feiertage 2025
if date == "2025.10.03":
    print("Tag der deutschen Einheit ist ein Feiertag")
if date == "2025.10.31":
    print("Reformationstag ist ein Feiertag")
if date == "2025.05.01":
    print("Tag der Arbeit ist ein Feiertag")
if date == "2025.05.29":
    print("Christi Himmelfahrt ist ein Feiertag")
if date == "2025.06.09":
    print("Pfingstmontag ist ein Feiertag")
else:
    print(X)
