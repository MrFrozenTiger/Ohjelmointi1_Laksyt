# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat
    #return gallonat * 3.785

gallonat = float(input("Syötä gallonat (negatiivinen lopettaa): "))
while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat} litraa.")
    gallonat = float(input("Syötä gallonat (negatiivinen lopettaa): "))
print("Ohjelma päättyy.")

#gallonat = 0
#litrat = 0
#while True:
#    gallonat = input("Syötä gallonat (negatiivinen lopettaa): ")
#    try:
#        gallonat = float(gallonat)
#        if gallonat < 0:
#            break
#        litrat = gallonat_litroiksi(gallonat)
#        print(f"{gallonat} gallonaa on {litrat:.3f} litraa.")
#    except ValueError:
#        print("Virheellinen syöte.")
#        gallonat = 0
#print("Ohjelma päättyy.")
