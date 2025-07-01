# main.py
import time
import random

MOODS = ["hungry", "sleepy", "feral", "melancholy", "gassy", "glitchy", "ecstatic", "mysterious"]

def display_random_mood():
    mood = random.choice(MOODS)
    print(f"🧟 Your Mutagotchi feels {mood.upper()}.")

if __name__ == "__main__":
    print("Booting up your Mutagotchi...")
    while True:
        display_random_mood()
        time.sleep(60)  # wait 60 seconds
