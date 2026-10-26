# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla
# on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan
# ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
# tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin
# autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi
# taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut
# vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä “Suuri romuralli”.
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa
# tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa
# tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
# onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla
# kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.


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

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.kesto = 0
        self.osallistujat = osallistujat
        return

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)
        self.kesto += 1
        return

    def tulosta_tilanne(self):

        voittaja = self.osallistujat[0]

        for auto in self.osallistujat:
            if auto.matka > voittaja.matka:
                voittaja = auto

        # Tulostetaan kilpailun kesto
        kaikki_minuutit = self.kesto * 60
        tunnit = kaikki_minuutit // 60
        minuutit = kaikki_minuutit % 60
        print(f"\nKilpailun kesto: {tunnit} h {minuutit} min")

        # Tulostetaan kilpailu taulukko
        print(f"{'Rekisteri':<12}{'Huippunopeus':<15}{'Nykynopeus':<15}{'Matka'}")
        print("-" * 52)
        for auto in self.osallistujat:
            if auto == voittaja and kilpailu_jatkuu == False:
                merkinta = " *"
            else:
                merkinta = " "
            print(f"{auto.rekkari:<6}"
                  f"{merkinta:<4}"
                  f"{auto.huippu_nopeus:>7.1f} km/h"
                  f"{auto.nyky_nopeus:>10.1f} km/h"
                  f"{auto.matka:>12.1f} km")

    def kilpailu_ohi(self):
        # Tarkistetaan, onko kilpailu ohi.
        for auto in self.osallistujat:
            if auto.matka >= self.pituus:
                return True
        return False


import random

osallistujat = []
osallistuja_maara = 10

# Luodaan kilpailijat
for entry in range(osallistuja_maara):
    rekisteritunnus = "ABC-" + str(entry + 1)
    huippunopeus = random.uniform(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    osallistujat.append(auto)

# Luodaan kilpailu.
kilpailu1 = Kilpailu("Suuri romuralli", 8000, osallistujat)

# Kilpailua jatketaan kunnes voittaja löytyy.
kilpailu_jatkuu = True
while kilpailu_jatkuu:
    kilpailu1.tunti_kuluu()
    if kilpailu1.kilpailu_ohi():
        kilpailu_jatkuu = False
        kilpailu1.tulosta_tilanne()
    else:
        if kilpailu1.kesto % 10 == 0:
            kilpailu1.tulosta_tilanne()
