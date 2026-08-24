# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.
# 1 tuuma = 2,54 cm

syote = float(input("Anna tuumat: "))
while syote > 0:
    print(f"{syote*2.54} cm")
    syote = float(input("Anna tuumat: "))
