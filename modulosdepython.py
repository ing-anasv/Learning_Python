import math as m #se usa un alias para no escribir math
from math import sqrt

"""
print(sqrt(16)) #como se importa el sqrt ya no es necesario escribir math.
print(m.pi)
print(m.factorial(5))
print(m.cos(0))

"""

import random as r

for i in range(5):
    random= r.randint(1,100)
    print(f"Número aleatorio generado: {random}")