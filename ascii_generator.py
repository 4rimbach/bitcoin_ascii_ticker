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
    font_choice = fonts[random.randrange(0,len(fonts))]
    font_choice = "tarty8"
    tickprice_num = 129521
    scale = 500
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
            time.sleep(2)
        except KeyboardInterrupt:
            try:
                os.system('cls||clear')
                tprint("...", font=font_choice)
                font_choice = fonts[random.randrange(0,len(fonts))]
                time.sleep(2)
            except:
                os.system('cls||clear')
                tprint("Exiting...", font=font_choice)
                print(font_choice)
                time.sleep(1)
                exit()

if __name__ == "__main__":
    main()