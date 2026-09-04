# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
# tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
# monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi
# siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi",
while True:
    kuukausi = input("Syötä kuukauden numero: ")
    try:
        kuukausi = int(kuukausi)
        testi_muuttuja = vuodenajat[kuukausi-1]
        break
    except ValueError:
        print("Virhe. Syötä kokonaisluku.")
    except IndexError:
        print("Virhe. Numeron täytyy olla välillä 1-12.")
print(f"Antamaasi kuukautta vastaava vuodenaika on {vuodenajat[kuukausi-1]}.")
