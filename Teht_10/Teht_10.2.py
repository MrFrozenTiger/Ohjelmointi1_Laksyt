# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon
# alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
# joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan
# lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:

    # Luodaan hissi.
    def __init__(self, ylin_kerros, alin_kerros=1):
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


class Talo():

    # Luodaan talo.
    def __init__(self, hissien_lukumaara, ylin_kerros, alin_kerros = 1):
        self.hissit = []

        # Lisätään hissit.
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(ylin_kerros, alin_kerros))

    # Does what it says.
    def aja_hissia(self, hissin_numero, kohde_kerros):
        hissin_numero.siirry_kerrokseen(kohde_kerros)
        return


# Luo talon: Hissien lukumäärä, ylin kerros, alin kerros.
talo = Talo(3, 7,)
loop_1 = True
while loop_1:
    loop_2 = True
    while True:
        valitse_hissi = input("Valitse hissi (1-3): ")
        try:
            valitse_hissi = int(valitse_hissi)
            if 1 <= valitse_hissi <= len(talo.hissit):
                break
            else:
                print(f"Virhe! Hissin pitää olla välillä 1-{len(talo.hissit)}.")
        except ValueError:
            print("Virhe! Syötteen pitää olla numero.")
    while True:
        valitse_kerros = input("Valitse kerros (1-7): ")
        try:
            valitse_kerros = int(valitse_kerros)
            break
        except ValueError:
            print("Virhe! Syötteen pitää olla numero.")

    valittu_hissi = talo.hissit[int(valitse_hissi)-1]
    print(f"Valitsit hissin {valitse_hissi}.")
    talo.aja_hissia(valittu_hissi, valitse_kerros)

    while loop_2:
        jatketaanko = input("Jatketaanko hissittelyä (k/e)?: ").lower()
        if jatketaanko in ["k","kyllä", "y", "yes"]:
            loop_2 = False
            continue
        elif jatketaanko in ["e", "ei", "n", "no"]:
            loop_1 = False
            loop_2 = False
        else:
            print("Virheellinen syöte.")
            continue
