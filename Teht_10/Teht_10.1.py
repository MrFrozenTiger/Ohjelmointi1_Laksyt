# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen
# numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi
# metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai
# kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja
# ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet
# pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen
# takaisin alimpaan kerrokseen.

class Hissi:

    # Luodaan hissi.
    def __init__(self, ylin_kerros, alin_kerros = 1):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.nyky_kerros = alin_kerros
        return

    # Siirrytään haluttuun kerrokseen.
    def siirry_kerrokseen(self, kohde_kerros):

        # Varmistetaan että kohde kerros on olemassa.
        if kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros
        elif kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros

        # Jatketaan kunnes oikea kerros löytyy.
        while self.nyky_kerros != kohde_kerros:
            if self.nyky_kerros < kohde_kerros:
                self.kerros_ylos()
            elif self.nyky_kerros > kohde_kerros:
                self.kerros_alas()
        return

    # Siirrytään kerros ylöspäin.
    def kerros_ylos(self):
        self.nyky_kerros += 1
        print('"Kerros ' + str(self.nyky_kerros) + '"')
        return

    # Siirrytään kerros alaspäin.
    def kerros_alas(self):
        self.nyky_kerros -= 1
        print('"Kerros ' + str(self.nyky_kerros) + '"')
        return

hissi1 = Hissi(7)

mihin = int(input("Mihin kerrokseen mennään?: "))
hissi1.siirry_kerrokseen(mihin)
hissi1.siirry_kerrokseen(1)
