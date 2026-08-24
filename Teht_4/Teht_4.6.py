import random

N = 10000
n = 0
toistot = 0

while toistot < N:
    x = random.randint
    y = random.randint
    if x ** 2 + y ** 2 < 1:
        n += 1
        toistot += 1
pii = 4*n/N
print(pii)