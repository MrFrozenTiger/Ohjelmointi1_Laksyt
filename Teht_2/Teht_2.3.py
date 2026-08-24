# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Syötä suorakulmion kanta: "))
korkeus = float(input("Syötä suorakulmion korkeus: "))

print(f"Suorakulmion piiri on {2*kanta + 2*korkeus}")
print(f"Suorakulmion pinta-ala on {kanta*korkeus}")
