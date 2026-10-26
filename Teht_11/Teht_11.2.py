# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
# ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
# ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
# sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton
# (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran
# ja tulosta autojen matkamittarilukemat.

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

class Sahkoauto(Auto):
    def __init__(self, rekkari, huippu_nopeus, akku_kapasiteetti = 0.0):
        super().__init__(rekkari, huippu_nopeus)
        self.akku_kapasiteetti = akku_kapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippu_nopeus, bensa_tankin_koko = 0.0):
        super().__init__(rekkari, huippu_nopeus)
        self.bensa_tankin_koko = bensa_tankin_koko


auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

while True:
    auto1_nopeus = input("Valitse auton 1 nopeus (km/h): ")
    try:
        auto1_nopeus = float(auto1_nopeus)
        auto1.kiihdytä(auto1_nopeus - auto1.nyky_nopeus)
        break
    except ValueError:
        print("Virhe. Syötteen tulee olla numero.")
        continue
while True:
    auto2_nopeus = input("Valitse auton 2 nopeus (km/h): ")
    try:
        auto2_nopeus = float(auto2_nopeus)
        auto2.kiihdytä(auto2_nopeus - auto2.nyky_nopeus)
        break
    except ValueError:
        print("Virhe. Syötteen tulee olla numero.")
        continue

auto1.kulje(3)
auto2.kulje(3)
print("Kolme tuntia myöhemmin...")
print(f"Auto 1 on ajanut {auto1.matka:.2f} km.")
print(f"Auto 2 on ajanut {auto2.matka:.2f} km.")
