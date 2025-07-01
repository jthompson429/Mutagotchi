# logic/stats.py

import random
import json

class MutagotchiStats:
    def __init__(self, hunger=None, energy=None, weirdness=None, mutation=0, age=0):
        self.hunger = hunger if hunger is not None else random.randint(20, 60)
        self.energy = energy if energy is not None else random.randint(40, 80)
        self.weirdness = weirdness if weirdness is not None else random.randint(0, 100)
        self.mutation = mutation
        self.age = age

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

    def to_dict(self):
        return self.status()

    @classmethod
    def from_dict(cls, data):
        return cls(
            hunger=data.get("hunger"),
            energy=data.get("energy"),
            weirdness=data.get("weirdness"),
            mutation=data.get("mutation", 0),
            age=data.get("age", 0)
        )
