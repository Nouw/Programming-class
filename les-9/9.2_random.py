# Schrijf functie monopolyworp(), die een het gooien van twee dobbelstenen voor het spel Monopoly simuleert en afdrukt.
# Je mag nogmaals gooien als beide stenen dezelfde waarde hebben.
# Zorg dat de functie die worpen ook simuleert! Na driemaal dubbel moet de speler naar de gevangenis!

import random

def monopolyworp():
    running = True
    worp = 1
    while running:

        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        if worp == 3:
            print(str(dice1) + " + " + str(dice2) + " = (direct naar de gevangenis)")
            running = False
        else:
            if dice1 == dice2:
                print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2) + " (dubbel)")
                worp += 1
            else:
                print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2))
                running = False


monopolyworp()