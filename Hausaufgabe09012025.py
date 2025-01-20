# ● name (Name des Haustiers, z. B. "Bello")
# ● species (Tierart, z. B. "Hund", "Katze")
# ● age (Alter in Jahren)
# ● favorite_food (Lieblingsessen des Haustiers, z. B. "Knochen")


class Pet:
    def __init__(self, pet_name, pet_species, pet_age, favorite_food):
        self.energy_level = 100
        self.name = pet_name
        self.species = pet_species
        self.age = pet_age
        self.favorite_food = favorite_food

    def get_description(self):
        return f"{self.name} ist ein(e) {self.age} Jahre alter {self.species}."

    # kann aber nicht unter 0 fallen.
    # play(duration):
    # ○ Beispiel: Bei 10 Minuten Spielen sinkt die Energie um 10 * 5 = 50 Punkte.
    def play(self, duration):
        energy_lost = duration * 5
        if self.energy_level < energy_lost:
            self.energy_level = 0
        else:
            self.energy_level = self.energy_level - energy_lost

    # Wenn das Essen dem favorite_food entspricht, gewinnt das Haustier 30 Punkte Energie.
    # Anderes Essen bringt nur 10 Punkte.
    # Der Energielevel kann maximal 100 betragen.
    def feed(self, food):
        new_energy = self.energy_level
        # .lower() Fisch --> fisch
        if food.lower() == self.favorite_food.lower():
            new_energy = new_energy + 30
        else:
            new_energy = new_energy + 10
        if new_energy > 100:
            new_energy = 100
        self.energy_level = new_energy

    def reset(self):
        self.energy_level = 100

    def sleep(self, hours_slept):
        new_energy = self.energy_level + hours_slept * 20
        if new_energy > 100:
            self.reset()  # self.energy_level = 100
        else:
            self.energy_level = new_energy


# ● Name: "Mimi"
# ● Tierart: "Katze"
# ● Alter: 3 Jahre
# ● Lieblingsessen: "Fisch"
mimi = Pet("Mimi", "Katze", 3, "Fisch")
print(f"{mimi.get_description()}")
# 15 Minuten spielen.
mimi.play(15)
print(f"Mimis current energy_level: {mimi.energy_level}")
# Füttere  Lieblingsessen
mimi.feed("Fisch")
print(f"Mimis current energy_level: {mimi.energy_level}")
# mit einem anderen Essen.
mimi.feed("Salat")
print(f"Mimis current energy_level: {mimi.energy_level}")
# reset
mimi.reset()
print(f"Mimis current energy_level: {mimi.energy_level}")
