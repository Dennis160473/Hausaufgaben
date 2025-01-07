# Aufgabe 2

# 2.1 - Aktuelles Datum und Uhrzeit ausgeben im Format TT.MM.JJJJ HH:MM:SS
from datetime import datetime


def aktuelles_datum_und_uhrzeit():
    Ausgabe = datetime.now()
    print(Ausgabe.strftime("Heute ist der %d.%m.%Y und es ist %H:%M:%S"))


aktuelles_datum_und_uhrzeit()


# 2.2 - Differenz bis zum Jahresende berechnen
from datetime import timedelta

today = datetime.now()


def tage_bis_jahresende(keydate):
    year = keydate.year
    end_of_year = datetime(year, 12, 31)
    return (end_of_year - keydate).days


difference_in_days = tage_bis_jahresende(today)
print(f"2. Days left until end of year: {difference.days}")


# 2.3 - Benutzerdefiniertes Datum
def tage_bis_datum(keydate):
    return (keydate - today).days


user_date_str = input("Enter a date (DD.MM.YYYY): ")

user_date = datetime.strptime(user_date_str, "%d.%m.%Y")

remaining = tage_bis_datum(user_date)
print(f"Remainig days from now until user input:{remaining_days} days")


# 2.4 - Wochentag berechnen
def wochentag_berechnen(input_date):
    return input_date_strftime("%A")


user_date_str = input("Enter a date (DD.MM.YYYY): ")

user_date = datetime.strptime(user_date_str, "%d.%m.%Y")
result_weekday = wochentag_berechnen(user_date)
print(f"The weekday of the input date is {result_weekday}")
