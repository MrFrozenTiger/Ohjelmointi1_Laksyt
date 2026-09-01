# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallonat_litroiksi():
    litrat = gallonat * 3.785
    return litrat

while True:
    gallonat = input("Syötä gallonat: ")
    try:
        gallonat = float(gallonat)
        break
    except ValueError:
        print("Virheellinen syöte.")
litrat = gallonat_litroiksi()
print(f"{litrat:.3f}")

