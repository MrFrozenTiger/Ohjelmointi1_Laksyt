# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy
# käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman
# tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma
# kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
# ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä
# haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten
# monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan
# lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lento_asemat = {}
valinta = ""
while valinta != "3":
    valinta = input("Haluatko syöttää uuden lentoaseman (1), hakea lentoaseman tiedot (2) vai lopettaa (3): ")
    if valinta == "1":
        ICAO = input("Syötä lentoaseman ICAO-koodi: ")
        lentoaseman_nimi = input("Syötä lentoaseman nimi: ")
        lento_asemat[ICAO] = lentoaseman_nimi
    elif valinta == "2":
        icao_haku = input("Syötä lentoaseman ICAO-koodi: ")
        if icao_haku in lento_asemat:
            print(f"{icao_haku}: {lento_asemat[icao_haku]}")
        else:
            print("Etsimääsi lentoasemaa ei löytynyt.")
    elif valinta == "3":
        print("Ohjelman suoritus lopetetaan.")
    else:
        print("Virhe.")
