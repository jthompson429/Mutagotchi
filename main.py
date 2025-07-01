# main.py
import time
import random
from logic.stats import MutagotchiStats
from utils.sound import play_random_sfx, play_background_music

MOODS = ["hungry", "sleepy", "feral", "melancholy", "gassy", "glitchy", "ecstatic", "mysterious"]

def display_status(stats):
    mood = random.choice(MOODS)
    print(f"\n🧟 Mood: {mood.upper()}")
    print("📊 Stats:")
    for key, value in stats.status().items():
        print(f"   {key.capitalize()}: {value}")
    play_random_sfx()  # Play sound after displaying mood and stats

if __name__ == "__main__":
    print("Booting up your Mutagotchi...")

    play_background_music()  # Start looping background music

    creature = MutagotchiStats()

    while True:
        creature.tick()
        display_status(creature)
        time.sleep(60)  # Reduce to 10 for faster testing if needed
