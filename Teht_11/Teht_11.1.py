# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja
# Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen
# kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    julkaisut = []

    def __init__(self, nimi):
        self.nimi = nimi
        self.julkaisut.append(self)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}: {self.kirjoittaja}, {self.sivumaara} sivua.")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}: {self.paatoimittaja}")


Lehti("Aku Ankka", "Aki Hyyppä")
Kirja("Hytti n:o 6", "Rosa Liksom", 200)

for julkaisu in Julkaisu.julkaisut:
    julkaisu.tulosta_tiedot()