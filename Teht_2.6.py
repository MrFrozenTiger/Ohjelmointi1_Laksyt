# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
# Vihje: tutustu random.randint()-funktion käyttöön.

import random

koodi1_1 = random.randint(0,9)
koodi1_2 = random.randint(0,9)
koodi1_3 = random.randint(0,9)
koodi2_1 = random.randint(1,6)
koodi2_2 = random.randint(1,6)
koodi2_3 = random.randint(1,6)
koodi2_4 = random.randint(1,6)
print(f"{koodi1_1}{koodi1_2}{koodi1_3}")
print(f"{koodi2_1}{koodi2_2}{koodi2_3}{koodi2_4}")
