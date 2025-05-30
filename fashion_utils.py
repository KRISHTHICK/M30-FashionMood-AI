from PIL import Image
import numpy as np
import random

def get_dominant_color(img):
    img = img.resize((100, 100))
    pixels = np.array(img).reshape(-1, 3)
    mean_rgb = np.mean(pixels, axis=0)
    return tuple(int(val) for val in mean_rgb)

def map_color_to_mood(rgb):
    r, g, b = rgb
    if r > 180 and g < 100:
        return "Bold & Confident"
    elif g > 180:
        return "Fresh & Chill"
    elif b > 180:
        return "Cool & Mysterious"
    elif r > 150 and g > 120:
        return "Romantic & Warm"
    else:
        return "Minimal & Elegant"

def generate_caption(mood):
    captions = {
        "Bold & Confident": "Owning every step. 💥 #BoldFashion",
        "Fresh & Chill": "Stay cool, stay kind. 🍃",
        "Cool & Mysterious": "Vibes speak louder than words. 🌙",
        "Romantic & Warm": "Soft hues & soft hearts. 💖",
        "Minimal & Elegant": "Less is luxe. 🤍"
    }
    return captions.get(mood, "Stylish by nature.")

def generate_hashtags(mood):
    tags = {
        "Bold & Confident": "#BoldLook #FearlessFashion #StreetStyle",
        "Fresh & Chill": "#GreenOutfit #RelaxedStyle #CoolVibes",
        "Cool & Mysterious": "#DarkAesthetic #MoodyStyle #MidnightMood",
        "Romantic & Warm": "#LoveInStyle #PastelFashion #DateLook",
        "Minimal & Elegant": "#ElegantWear #MinimalStyle #ChicVibes"
    }
    return tags.get(mood, "#FashionMood")
