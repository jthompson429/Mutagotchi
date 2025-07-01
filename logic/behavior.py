# logic/behavior.py

def get_behavior(stats):
    behaviors = []

    if stats.hunger > 80:
        behaviors.append("is gnawing on its own limbs. 🍖")
    elif stats.hunger > 60:
        behaviors.append("keeps eyeing your fingers... 🍗")

    if stats.energy < 20:
        behaviors.append("is twitching with exhaustion. 💤")
    elif stats.energy < 40:
        behaviors.append("just let out a long, wet sigh. 😩")

    if stats.weirdness > 90:
        behaviors.append("is communicating with unseen forces. 👁️")
    elif stats.weirdness > 70:
        behaviors.append("is humming a song that doesn’t exist. 🎵")

    if stats.mutation >= 3:
        behaviors.append("has grown a suspicious lump. 🧬")
    elif stats.mutation >= 1:
        behaviors.append("has developed an extra eyelid. 👀")

    if not behaviors:
        behaviors.append("is quietly vibrating. 🌀")

    return behaviors
