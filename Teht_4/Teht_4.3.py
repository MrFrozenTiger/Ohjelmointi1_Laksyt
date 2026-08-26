# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

suurin = ""
pienin = ""
while True:
    luku = input("Syötä luku (tyhjä lopettaa): ")
    if luku == "":
        break
    try:
        luku = int(luku)
        if suurin == "" or pienin == "":
            suurin = luku
            pienin = luku
        elif int(luku) > suurin:
            suurin = int(luku)
        elif int(luku) < pienin:
            pienin = int(luku)
    except ValueError:
        print("Virhe. Antamasi syöte ei ole luku.")

print(f"Suurin luku: {suurin}, pienin luku: {pienin}")