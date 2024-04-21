import random
import time
import os
import locale
import pygame
from art import tprint
from coinbase_websocket import BitcoinPriceFetcher, api_key, api_secret

locale.setlocale(locale.LC_ALL, '')
pygame.init()

SOUNDS = {'rizz_sound': 'rizz_sound.wav'}
FONTS = [
    "univers",
    "varsity",
    "tarty9",
    "tarty8",
    "tarty1",
    "sweet",
    "swampland",
    "starwars",
    "doom",
    "dotmatrix",
    "epic",
    "ghost",
    "merlin1",
    "modular",
    "nvscript",
    "poison",
    "standard",
    "swampland",
]

def load_sound(sound_name):
    return pygame.mixer.Sound(SOUNDS[sound_name])

def format_bitcoin_price(price):
    return locale.currency(float(price), grouping=True).replace("$", "$" + " " * (11 - len(price)))

def main():
    sound_effect = load_sound('rizz_sound')
    font_choice = random.choice(FONTS)
    fetcher = BitcoinPriceFetcher(api_key, api_secret)
    fetcher.start()

    passed_threshold = False
    while True:
        try:
            os.system('cls||clear')
            bitcoin_price = fetcher.get_bitcoin_price()
            if bitcoin_price is not None:
                tickprice = format_bitcoin_price(bitcoin_price)
                print(tickprice)
                tprint(tickprice, font=font_choice)
                print(font_choice)

                if float(bitcoin_price) >= 100000 and not passed_threshold:
                    sound_effect.play()
                    passed_threshold = True
                elif float(bitcoin_price) < 100000:
                    passed_threshold = False
            time.sleep(2)
        except KeyboardInterrupt:
            os.system('cls||clear')
            tprint("...", font=font_choice)
            font_choice = random.choice(FONTS)
            time.sleep(2)
            continue
        except Exception as e:
            print(f"Error: {e}")
            break

    os.system('cls||clear')
    tprint("Exiting...", font=font_choice)
    print(font_choice)
    time.sleep(1)

if __name__ == "__main__":
    main()
