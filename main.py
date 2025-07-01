# main.py
import time
import random
from logic.stats import MutagotchiStats
from logic.behavior import get_behavior
from utils.sound import play_random_sfx, play_background_music
from utils.save import save_creature, load_creature
from ui.terminal_ui import get_user_action

MOODS = ["hungry", "sleepy", "feral", "melancholy", "gassy", "glitchy", "ecstatic", "mysterious"]

def display_status(stats):
    mood = random.choice(MOODS)
    print(f"\n🧟 Mood: {mood.upper()}")
    print("📊 Stats:")
    for key, value in stats.status().items():
        print(f"   {key.capitalize()}: {value}")

    behaviors = get_behavior(stats)
    print("🧠 Behavior:")
    for b in behaviors:
        print(f"   - Your Mutagotchi {b}")

    play_random_sfx()

if __name__ == "__main__":
    print("Booting up your Mutagotchi...")

    play_background_music()

    saved_data = load_creature()
    if saved_data:
        print("🔁 Resurrecting your last Mutagotchi...")
        creature = MutagotchiStats.from_dict(saved_data)
    else:
        print("🌱 Hatching a new Mutagotchi...")
        creature = MutagotchiStats()

    while True:
        creature.tick()
        display_status(creature)

        action = get_user_action()

        if action == "1":
            creature.hunger = max(0, creature.hunger - 20)
            print("🍖 You tossed it a handful of questionable meat.")
        elif action == "2":
            creature.energy = min(100, creature.energy + 15)
            print("😴 You dimmed the lights. It shudders… then relaxes.")
        elif action == "3":
            creature.weirdness = min(100, creature.weirdness + 10)
            print("🔮 You performed a weird ritual. Something unseen is now aware of you.")
        elif action == "4":
            print("🕳️ You did nothing. It did not go unnoticed.")
        elif action == "q":
            print("🛑 Exiting and saving your Mutagotchi...")
            save_creature(creature)
            break
        else:
            print("❓ It stares at you, confused. Try again.")

        save_creature(creature)
        time.sleep(2)  # Optional cooldown; keep short for testing
