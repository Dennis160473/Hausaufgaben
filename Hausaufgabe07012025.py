# Aufgabe 1


class Ingredient:
    def __init__(self, name, calories, time):
        self.name = name
        self.calories = calories
        self.time = time


class Recipe:
    def __init__(self, name, description, ingredient_list):
        self.name = name
        self.description = description
        self.ingredient_list = {Ingredient}

    def zutat_hinzufügen(self):
        print(f"You need {self.name} with {self.ingredient_list}")

    def kalorien(self):
        print(f"This includes {self.calories}kcal.")

    def kochzeit(self):
        print(f"The cooking time is {self.time}.")

    def rezept_anzeigen(self):
        print(f"The following recipe is available for you: ")


court = Recipe("{Ingredient}", {self.time}")


# Aufgabe 2

import requests


def information():
    user = user_input
    return


user_input = input("Please enter a location: ")

response = requests.get("https://wttr.in/berlin?format=j1")
daten = response.json()
temperature = dates["current_condition"][0]["temp_C"]
weather = dates["current_condition"][0]["weatherDesc"][0]["value"]
print(wetter)
print(f"The weather in Berlin is {weather} with {temperature}°C")
