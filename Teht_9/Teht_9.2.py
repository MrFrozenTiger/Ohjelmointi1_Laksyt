# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
# nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa
# huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
# että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden
# muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

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

auto = Auto("ABC-123", 142)

print("Auto on paikallaan.")
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
print("Auto kiihdyttää.")
auto.kiihdytä(+30)
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
print("Auto kiihdyttää..")
auto.kiihdytä(+70)
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
print("Auto kiihdyttää...")
auto.kiihdytä(+50)
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
print("Hätäjarrutus!!!")
auto.kiihdytä(-200)
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
