# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan
# arvauskertojen välissä.

import random

koneen_luku = random.randint(1, 10)
pelaajan_luku = 0
while pelaajan_luku != koneen_luku:
    pelaajan_luku = int(input("Arvaa luku: "))
    if pelaajan_luku > koneen_luku:
        print("Liian suuri.")
    elif pelaajan_luku < koneen_luku:
        print("Liian pieni.")
    else:
        print("Oikein!")
