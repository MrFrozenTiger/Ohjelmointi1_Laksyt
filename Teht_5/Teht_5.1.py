# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

summa = 0
#luvut = []#2
while True:
    noppia = input("Anna noppien määrä: ")
    try:
        noppia = int(noppia)
        break
    except ValueError:
        print("Virhe.")

for n in range(noppia):
#    luku = random.randint(1, 6)#2
#    luvut.append(luku)#2
    summa += random.randint(1, 6)#1
#    summa += luku#2
print(f"Silmälukujen summa: {summa}")#1
#luvut = sorted(luvut)#2.2
#print(luvut)#2
