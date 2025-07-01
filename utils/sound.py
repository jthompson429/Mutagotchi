# utils/sound.py
import pygame
import random
import os

pygame.mixer.init()

SFX_DIR = os.path.join(os.path.dirname(__file__), "../assets/sounds")
MUSIC_DIR = os.path.join(SFX_DIR, "bg_music")

def play_random_sfx():
    sounds = [f for f in os.listdir(SFX_DIR) if f.endswith(".wav") and not f.startswith("bg_")]
    if not sounds:
        print("🔇 No sound effects found.")
        return
    file = os.path.join(SFX_DIR, random.choice(sounds))
    pygame.mixer.Sound(file).play()

def play_background_music():
    try:
        tracks = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".wav")]
        if not tracks:
            return
        bg_track = os.path.join(MUSIC_DIR, tracks[0])  # Just play the first one
        pygame.mixer.music.load(bg_track)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)  # Loop forever
        print("🎵 Background music started.")
    except Exception as e:
        print(f"🎵 Music error: {e}")
