from art import *
import random
import time
import os
import locale
import pygame

locale.setlocale(locale.LC_ALL, '')
pygame.init()
os.system('cls||clear')
tprint("Good morning...")
time.sleep(2)

# Load sound effect
pygame.mixer.init()
sound_effect = pygame.mixer.Sound('rizz_sound.wav')  # Replace 'your_sound_file.wav' with the path to your sound file

fonts = [
        "univers", #maybe actual best one
        "varsity",
        "twisted", #illegible
        "tarty9", #good
        "tarty8", #best one?
        "tarty1", #top notch
        "sweet", #solid
        "swampland", #ok
        "starwars", #good
        "doom",
        "dotmatrix", #good
        "epic",
        "ghost",
        "merlin1",
        "modular",
        "nvscript",
        "poison",
        "standard",
        "swampland",
]

def random_walk(seed, scale):
    return seed+scale*random.uniform(-1, 1)

def main():
    font_choice = random.choice(fonts)
    tickprice_num = 99900
    scale = 500
    passed_threshold = False
    while True:
        try:
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_w]:
            #     font_choice = fonts[random.randint(0,len(fonts))]
            os.system('cls||clear')
            tickprice_num = random_walk(tickprice_num, random.randint(0, scale))
            #random.randint(42069, 111111)
            tickprice = locale.currency(tickprice_num, grouping=True)
            fill_spaces = 11-len(tickprice)
            tickprice = tickprice.replace("$", "$"+" "*fill_spaces)
            print(tickprice)
            tprint(tickprice, font=font_choice)
            print(font_choice)

            if tickprice_num >= 100000 and not passed_threshold:
                sound_effect.play()  # Rizz Rizz
                passed_threshold = True
            elif tickprice_num < 100000:
                passed_threshold = False

            time.sleep(2)
        except KeyboardInterrupt:
            try:
                os.system('cls||clear')
                tprint("...", font=font_choice)
                font_choice = fonts[random.randrange(0,len(fonts))]
                time.sleep(2)
            except KeyboardInterrupt:
                os.system('cls||clear')
                tprint("Exiting...", font=font_choice)
                print(font_choice)
                time.sleep(1)
                exit()

if __name__ == "__main__":
    main()
