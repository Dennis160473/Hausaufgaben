# Aufgabe 1


## Aufgabe 1.1

class Ingedient:
    def __init__(self, name, calories, preparation_time):
        selfIngredient.name = name
        self.calories = calories
        self.preparation_time = preparation_time

## Aufgabe 1.2

class Recipe:
    def __init__(self, name, description, ingredient_list):
        self.name = name
        self.description = description
        self.ingredient_list = {}

    def add_ingredient(self):
        self.ingredient_list = [Ingredient] = crowd

    def calories(self):
        calories counter = 0
        for Ingredient in self.ingredient_list:
            calories_counter += ingredient.calories
            print(f"The total calories are {calories_counter} kcal.")

    def cooking_time(self):
        cooking_time = 0
        for ingredient in self.ingredient_list:
            if ingredient > cooking_time:
                cooking_time = ingredient.time
        print(f"The cooking time is {self.time}.")

    def show recipe(self):
        print("Rezept: {self.name}")
        print("Ingredient: ")
        for recipe, crowd in self.ingredient_list.items():
            print("f - {recipe.name}: {crowd}")
        print("\nDescription of the recipe: {self.description}")

## Aufgabe 1.3

milk = ingredient(milk, 50, 5)
eggs = ingredient(eggs, 150, 0)
flour = ingredient(flour, 300, 10)
sugar = ingredient(sugar, 400, 5)

pancake = recipe("pancake, super delicious pancakes.")
pancake.add_ingredient(milk, "250ml")
pancake.add_ingredient(eggs, "2 piece")
pancake.add_ingredient(flour, "150g")
pancake.add_ingredient(sugar, "50g")







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
