# logic/stats.py

import random

class MutagotchiStats:
    def __init__(self):
        self.hunger = random.randint(20, 60)
        self.energy = random.randint(40, 80)
        self.weirdness = random.randint(0, 100)
        self.mutation = 0
        self.age = 0

    def tick(self):
        self.age += 1
        self.hunger = min(100, self.hunger + random.randint(1, 5))
        self.energy = max(0, self.energy - random.randint(1, 3))
        self.weirdness = min(100, self.weirdness + random.randint(-2, 4))
        if self.hunger > 80:
            self.mutation += 1

    def status(self):
        return {
            "age": self.age,
            "hunger": self.hunger,
            "energy": self.energy,
            "weirdness": self.weirdness,
            "mutation": self.mutation
        }
