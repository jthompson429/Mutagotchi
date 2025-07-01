# utils/sound.py
import pygame
import random
import os

# Init mixer (should be done once at start)
pygame.mixer.init()

# Path to your sound effects
SOUND_DIR = os.path.join(os.path.dirname(__file__), "../assets/sounds")

def play_random_sound():
    sounds = [f for f in os.listdir(SOUND_DIR) if f.endswith((".wav", ".mp3", ".ogg"))]
    if not sounds:
        print("🔇 No sounds found.")
        return
    sound_file = os.path.join(SOUND_DIR, random.choice(sounds))
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
