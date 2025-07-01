# utils/save.py

import os
import json

SAVE_FILE = os.path.join(os.path.dirname(__file__), "../data/save.json")

def save_creature(stats):
    with open(SAVE_FILE, "w") as f:
        json.dump(stats.to_dict(), f)
    print("💾 Mutagotchi saved!")

def load_creature():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None
