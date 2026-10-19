# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

auto = Auto("ABC-123", 142)

print("Auto on paikallaan.")
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
print(f"Autolla on ajettu {auto.matka} km.")

auto.nyky_nopeus = 60
auto.kulje(1.5)
print("Auto ajoi 1.5 tunnin ajan nopeudella 60 km/h.")
print(f"Auton nopeus on {auto.nyky_nopeus} km/h.")
print(f"Autolla on ajettu {auto.matka} km.")

while True:
    uusi_nopeus = input("Kuinka lujaa ajetaan?: ")
    try:
        uusi_nopeus = int(uusi_nopeus)
        break
    except ValueError:
        print("Virheellinen syöte.")

auto.nyky_nopeus = max(0, min(uusi_nopeus, auto.huippu_nopeus))

while True:
    uusi_ajoaika = input("Kuinka kauan ajetaan?: ")
    try:
        uusi_ajoaika = int(uusi_ajoaika)
        break
    except ValueError:
        print("Virheellinen syöte.")

auto.kulje(uusi_ajoaika)
print(f"Auto ajoi {uusi_ajoaika} tuntia nopeudella {auto.nyky_nopeus} km/h.")
print(f"Autolla on ajettu {auto.matka} km.")