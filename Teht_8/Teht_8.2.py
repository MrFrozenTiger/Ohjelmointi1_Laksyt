# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
# kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä
# on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="root",
         password="2511",
         autocommit=True
         )

koodi = input("Syötä maa koodi: ").upper()
sql = f"select type, count(*) from airport where iso_country = '{koodi}' group by type;"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
if tulos != []:
    print(tulos)
else:
    print("Virheellinen syöte.")
