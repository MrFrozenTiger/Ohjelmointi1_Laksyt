# Autot lähtee viivalta tuskallisen hitaasti, olisi paljon mielenkiintoisempaa,
# jos edistymistä tarkastettaisiin useammin jne.
# Homma lähti vähän lapasesta, joten päätin tehdä lisämuutoksille ihan oman tiedoston.

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

# Luodaan kilpailijat
for entry in range(osallistuja_maara):
    rekisteritunnus = "ABC-" + str(entry + 1)
    huippunopeus = random.uniform(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    kilpailijat.append(auto)

reitti = 10000
edistys = 0
kilpailun_kesto = 0
aika_osa = 1/360# 10 sekuntia tunnista.
tasa_tunnit = 0
while edistys < reitti:
    # Lasketaan tasatunnit
    tasa_tunti = False
    if tasa_tunnit >= 1:
        tasa_tunti = True
        tasa_tunnit = 0
    for auto in kilpailijat:
        # Alku kiihdytys.
        if kilpailun_kesto < 1/60:
            kiihdytys = random.uniform(-10, 15)
            auto.kiihdytä(kiihdytys)
        # Uusi nopeus lasketaan tasatunnein.
        elif tasa_tunti:
            kiihdytys = random.uniform(-10, 15)
            auto.kiihdytä(kiihdytys)
        # Edistyminen lasketaan 10 sekunnin välein.
        auto.kulje(aika_osa)
        # Päivittää kilpailun edistymisen.
        if auto.matka > edistys:
            edistys = auto.matka
    kilpailun_kesto += aika_osa
    tasa_tunnit += aika_osa

# Tarkastetaan voittaja
voittaja = kilpailijat[0]
for auto in kilpailijat:
    if auto.matka > voittaja.matka:
        voittaja = auto

# Tulostetaan kilpailun kesto
kaikki_minuutit = round(kilpailun_kesto * 60)
tunnit = kaikki_minuutit // 60
minuutit = kaikki_minuutit % 60
print(f"Kilpailun kesto: {tunnit} h {minuutit} min")

# Tulostetaan kilpailu taulukko
print(f"{'Rekisteri':<12}{'Huippunopeus':<15}{'Nykynopeus':<15}{'Matka'}")
print("-" * 52)
for auto in kilpailijat:
    if auto == voittaja:
        merkinta = " *"
    else:
        merkinta = " "
    print(f"{auto.rekkari:<6}"
          f"{merkinta:<4}"
          f"{auto.huippu_nopeus:>7.1f} km/h"
          f"{auto.nyky_nopeus:>10.1f} km/h"
          f"{auto.matka:>12.1f} km")
