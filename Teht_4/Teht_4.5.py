# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty
# viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä
# Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

tosi_tunnus = "python"
tosi_salaus = "rules"
toisto = 0
while toisto < 5:
    toisto += 1
    tunnus = input("Käyttäjätunnus: ")
    salaus = input("Salasana: ")
    if tosi_tunnus == tunnus and tosi_salaus == salaus:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty.")
