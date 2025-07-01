# main.py
import time
import random
from logic.stats import MutagotchiStats

MOODS = ["hungry", "sleepy", "feral", "melancholy", "gassy", "glitchy", "ecstatic", "mysterious"]

def display_status(stats):
    mood = random.choice(MOODS)
    print(f"\n🧟 Mood: {mood.upper()}")
    print("📊 Stats:")
    for key, value in stats.status().items():
        print(f"   {key.capitalize()}: {value}")

if __name__ == "__main__":
    print("Booting up your Mutagotchi...")
    creature = MutagotchiStats()

    while True:
        creature.tick()
        display_status(creature)
        time.sleep(60)  # You can set to 10 for testing
