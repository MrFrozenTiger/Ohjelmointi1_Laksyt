#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

while True:
    sukupuoli = input("Oletko mies vai nainen: ")
    if sukupuoli == "mies" or sukupuoli == "m" or sukupuoli == "nainen" or sukupuoli == "n":
        break
    else:
        print("Virhe.")

while True:
    hemoglob = input("Syötä hemoglobiiniarvo (g/l): ")
    #Pääsin tähän asti ennen kuin hoksasin, ettei minulla ole harmainta aavistustakaan miten voin verrata onko syöte lukuarvo vai ei.
    try:
        testi = float(hemoglob)
        break
    except ValueError:
        print("Virhe.")
    # try / except löytyi googlaamalla, en ole moiseen aiemmin törmännyt.

if sukupuoli.lower() == "mies" or sukupuoli.lower() == "m":
    if testi >= 134 and testi <= 195:
        print("Hemoglobiini arvosi on normaali.")
    elif testi < 134:
        print("Hemoglobiini arvosi on alhainen.")
    elif testi > 195:
        print("Hemoglobiini arvosi on korkea.")
elif sukupuoli.lower() == "nainen" or sukupuoli.lower() == "n":
    if testi >= 117 and testi <= 175:
        print("Hemoglobiini arvosi on normaali.")
    elif testi < 117:
        print("Hemoglobiini arvosi on alhainen.")
    elif testi > 175:
        print("Hemoglobiini arvosi on korkea.")
