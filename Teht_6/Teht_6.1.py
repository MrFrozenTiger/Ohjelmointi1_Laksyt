# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun
# väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def arpa ():
    luku = random.randint(1,6)
    return luku
luku = 0
heitot = 0
while luku != 6:
    luku = arpa()
    heitot += 1
    print(f"{heitot}. heiton silmäluku on {luku}")