# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet
# ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

while True:
    vuosi = input("Syötä vuosi: ")
    try:
        vuosiluku = int(vuosi)
        break
    except ValueError:
        print("Virhe.")

if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
        print(f"Vuosi {vuosiluku} on karkausvuosi.")
    else:
        print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")
elif vuosiluku % 4 == 0:
    print(f"Vuosi {vuosiluku} on karkausvuosi.")
else:
    print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")
    