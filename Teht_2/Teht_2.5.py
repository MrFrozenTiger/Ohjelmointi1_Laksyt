# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
# leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi
# kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

le2g = float(leiviska*20*32*13.3)
na2g = float(naula*32*13.3)
lu2g = float(luoti*13.3)

massa = float(le2g+na2g+lu2g)

kilogrammat = massa//1000
grammat = massa%1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat:.0f} kilogrammaa ja {grammat:.2f} grammaa.")
