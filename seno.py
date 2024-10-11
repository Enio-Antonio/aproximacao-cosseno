from fatorial import fatorial
from math import sin, pi

teta = 60 * (pi / 180)
valor_esperado = sin(pi / 3)

soma = 0

for i in range(11):
    if i % 2 == 0:
        soma += (teta ** (2 * i + 1)) / fatorial(2 * i + 1)
    elif i % 2 != 0:
        soma -= (teta ** (2 * i + 1)) / fatorial(2 * i + 1)

print(valor_esperado)
print(soma)