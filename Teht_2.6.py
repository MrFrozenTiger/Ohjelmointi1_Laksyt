# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
# Vihje: tutustu random.randint()-funktion käyttöön.

import random

koodi11 = random.randint(0,9)
koodi12 = random.randint(0,9)
koodi13 = random.randint(0,9)
koodi21 = random.randint(1,6)
koodi22 = random.randint(1,6)
koodi23 = random.randint(1,6)
koodi24 = random.randint(1,6)
print(f"{koodi11}{koodi12}{koodi13}")
print(f"{koodi21}{koodi22}{koodi23}{koodi24}")
