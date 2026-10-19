# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
# ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekkari, huippu_nopeus, nyky_nopeus= 0, matka= 0):
        self.rekkari = rekkari
        self.huippu_nopeus = huippu_nopeus
        self.nyky_nopeus = nyky_nopeus
        self.matka = matka

        return


auto = Auto("ABC-123", 142)

print(f"Auton rekisterinumero on {auto.rekkari} ja huippunopeus on {auto.huippu_nopeus} km/h!")
print("Auton tämän hetkinen nopeus on", str(auto.nyky_nopeus) + " km/h ja autolla on ajettu yhteensä", str(auto.matka), "km.")
