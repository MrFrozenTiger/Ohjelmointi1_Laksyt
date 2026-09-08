# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
# kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
# airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="root",
         password="2511",
         autocommit=True
         )


koodi = input("Syötä lentoaseman ICAO-koodi: ").upper()# Helsinki-Vantaan ICAO on EFHK
sql = f"select name, municipality from airport where ident = '{koodi}';"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
if tulos != []:
    print(tulos)
else:
    print("Hakemaasi lentokenttää ei löytynyt.")
