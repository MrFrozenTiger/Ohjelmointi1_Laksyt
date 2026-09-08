# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="root",
         password="2511",
         autocommit=True
         )

def hae_sijainti(numero):
    lento_kentta = input(f"Syötä {numero} lentokentän ICAO-koodi: ").upper()
    sql = (f"select latitude_deg, longitude_deg "
           f"from airport where ident = '{lento_kentta}';")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return kursori.fetchall()

# Helsinki-Vantaa EFHK, Ivalo EFIV, n.930km
sijainti_1 = hae_sijainti("ensimmäinsen")
sijainti_2 = hae_sijainti("toisen")
etaisyys = distance.distance(sijainti_1, sijainti_2).km
print(f"Valitsemiesi kenttien välinen etäisyys on {etaisyys:.2f} km.")
