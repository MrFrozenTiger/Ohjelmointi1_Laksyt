# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
# nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def arpa (min, max):
    luku = random.randint(min, max)
    return luku

luku = 0
heitot = 0
while True:
    noppa = input("Valitse nopan koko: ").lower().strip("d")
    try:
        noppa = int(noppa)
        break
    except ValueError:
        print("Virhe.")
while luku != noppa:
    luku = arpa(1, noppa)
    heitot += 1
    print(f"{heitot}. heiton silmäluku on {luku}")
