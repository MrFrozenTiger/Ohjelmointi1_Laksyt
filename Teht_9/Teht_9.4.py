# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti
# nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella
# luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h
# väliltä. Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu
# alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä
# -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla
# kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

class Auto:
    def __init__(self, rekkari, huippu_nopeus, nyky_nopeus= 0, matka= 0):
        self.rekkari = rekkari
        self.huippu_nopeus = huippu_nopeus
        self.nyky_nopeus = nyky_nopeus
        self.matka = matka

    def kiihdytä(self, nopeuden_muutos):
        self.nyky_nopeus += nopeuden_muutos
        self.nyky_nopeus = max(0, min(self.nyky_nopeus, self.huippu_nopeus))
        return

    def kulje(self, ajo_aika):
        self.matka += self.nyky_nopeus * ajo_aika
        return

import random

kilpailijat = []
osallistuja_maara = 10


for entry in range(osallistuja_maara):
    rekisteritunnus = "ABC-" + str(entry + 1)
    huippunopeus = random.uniform(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    kilpailijat.append(auto)


reitti = 10000
edistys = 0
kesto = 0
while edistys < reitti:
    kesto += 1
    for auto in kilpailijat:
        kiihdytys = random.uniform(-10, 15)
        auto.kiihdytä(kiihdytys)
        auto.kulje(1)
        if auto.matka > edistys:
            edistys = auto.matka


print(f"Kilpailun kesto: {kesto}h")

print(f"{'Rekisteri':<12}{'Huippunopeus':<15}{'Nykynopeus':<15}{'Matka'}")
print("-" * 52)

for auto in kilpailijat:
    print(f"{auto.rekkari:<12}"
          f"{auto.huippu_nopeus:>8.1f} km/h"
          f"{auto.nyky_nopeus:>9.1f} km/h"
          f"{auto.matka:>12.1f} km")

