# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää
# tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin
# Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa
# järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()
nimi = input("Syötä nimi (tyhjä lopettaa): ")
while nimi != "":
    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi.")
    else:
        print("Aiemmin syötetty nimi.")
    nimi = input("Syötä nimi (tyhjä lopettaa): ")
for nimi in nimet:
    print(nimi)