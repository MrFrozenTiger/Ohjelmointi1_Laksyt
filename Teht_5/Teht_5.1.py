# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

summa = 0
#luvut = []
while True:
    noppia = input("Anna noppien määrä: ")
    try:
        noppia = int(noppia)
        break
    except ValueError:
        print("Virhe.")

for n in range(noppia):
#    luku = random.randint(1, 6)
#    luvut.append(luku)
    summa += random.randint(1, 6)
#    summa += luku
print(summa)
#luvut = sorted(luvut)
#print(luvut)