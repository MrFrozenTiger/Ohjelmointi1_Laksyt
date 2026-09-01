# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
# per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
# ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
# yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def price_by_square(koko, hinta):
    sade = koko/200
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala

while True:
    tieto = input("Syötä ensimmäisen pizzan halkaisija (cm): ")
    try:
        tieto = float(tieto)
        halkaisija1 = tieto
        break
    except ValueError:
        print("Virheellinen syöte.")
while True:
    tieto = input("Syötä ensimmäisen pizzan hinta (€): ")
    try:
        tieto = float(tieto)
        hinta1 = tieto
        break
    except ValueError:
        print("Virheellinen syöte.")
while True:
    tieto = input("Syötä toisen pizzan halkaisija (cm): ")
    try:
        tieto = float(tieto)
        halkaisija2 = tieto
        break
    except ValueError:
        print("Virheellinen syöte.")
while True:
    tieto = input("Syötä toisen pizzan hinta (€): ")
    try:
        tieto = float(tieto)
        hinta2 = tieto
        break
    except ValueError:
        print("Virheellinen syöte.")
vertailtava1 = price_by_square(halkaisija1, hinta1)
vertailtava2 = price_by_square(halkaisija2, hinta2)
if vertailtava1 < vertailtava2:
    print("Ensimmäinen pizza antaa enemmän vastinetta rahallesi.")
elif vertailtava1 > vertailtava2:
    print("Toinen pizza antaa enemmän vastinetta rahallesi.")
else:
    print("Pizzoilla on sama neliöhinta.")


#def kysy(numero):
#    while True:
#        halkaisija = input(f"Syötä {numero} pizzan halkaisija (cm): ")
#        try:
#            halkaisija = float(halkaisija)
#            break
#        except ValueError:
#            print("Virheellinen syöte.")

#    while True:
#        hinta = input(f"Syötä {numero} pizzan hinta (€): ")
#        try:
#            hinta = float(hinta)
#            break
#        except ValueError:
#            print("Virheellinen syöte.")

#    return halkaisija, hinta

#halkaisija1, hinta1 = kysy("ensimmäisen")
#halkaisija2, hinta2 = kysy("toisen")
#vertailtava1 = price_by_square(halkaisija1, hinta1)
#vertailtava2 = price_by_square(halkaisija2, hinta2)
#if vertailtava1 < vertailtava2:
#    print("Ensimmäinen pizza antaa enemmän vastinetta rahallesi.")
#elif vertailtava1 > vertailtava2:
#    print("Toinen pizza antaa enemmän vastinetta rahallesi.")
#else:
#    print("Pizzoilla on sama neliöhinta.")