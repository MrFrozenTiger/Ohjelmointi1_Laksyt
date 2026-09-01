# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu
# lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
# sen jälkeen sekä alkuperäisen että karsitun listan.

def parittomien_karsinta(lista1):
    lista2 = []
    for i in lista1:
        if i % 2 == 0:
            lista2.append(i)
    return lista2

lista1 = []
luku = input("Lisää luku (tyhjä lopettaa): ")
while luku != "":
    try:
        luku = int(luku)
        lista1.append(luku)
    except ValueError:
        print("Virheellinen syöte.")
    luku = input("Lisää luku (tyhjä lopettaa): ")
lista2 = parittomien_karsinta(lista1)
print(f"Alkuperäinen lista : {lista1}")
print("Uusi lista: ", lista2)
