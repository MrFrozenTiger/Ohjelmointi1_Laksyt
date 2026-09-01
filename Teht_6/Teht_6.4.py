# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen palauttaman summan.

def lukujen_summa(lista):
    summa = 0
    for i in lista:
        summa += int(i)
    return summa

lista = []
luku = input("Lisää luku (tyhjä lopettaa): ")
while luku != "":
    try:
        luku = int(luku)
        lista.append(luku)
    except ValueError:
        print("Virheellinen syöte.")
    luku = input("Lisää luku (tyhjä lopettaa): ")
summa = lukujen_summa(lista)
print("Lukujen summa on ", summa)
