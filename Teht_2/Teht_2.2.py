#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#pii * r ^2
import math
sade = float(input("Syötä ympyrän säde: "))
p_ala = math.pi * sade ** 2
print(f"{p_ala:.3f}")
