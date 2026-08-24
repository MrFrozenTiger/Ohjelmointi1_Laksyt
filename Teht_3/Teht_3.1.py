# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta
# pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

print("Minkäs kokisen kuhan sait?")
pituus = float(input("Kerro kuhan pituus senttimetreissä: "))

if pituus < 37:
    erotus = 37 - pituus
    print(f"Heitä se takaisin järveen, se on {erotus:.2f}cm liian lyhyt.")
else:
    print("Onneksi olkoon, onpa vonkale!")
