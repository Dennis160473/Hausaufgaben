class Pet:
    def __init__(self, name, species, age, favorite_food, energy_level):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy_level = energy_level

    def get_description(self):
        return self.name + self.species + self.age

    # def play(self, duration):

    # def feed(self, food):


my_pet1 = Pet("Bello", "Hund", 5, "Knochen", 100)
my_pet2 = Pet("Mimi", "Katze", 3, "Fisch", 100)
print(f" Mein {self.species} {self.name} ist {self.age} Jahre alt.")
