from fatorial import fatorial
from math import cos, pi

teta = 30 * (pi / 180)
valor_esperado = cos(pi / 6)
soma = 0

for i in range(15):
    if i == 0:
        soma += 1
    elif i % 2 != 0:
        soma -= (teta**(i * 2)) / (fatorial(2 * i))
    elif i % 2 == 0:
        soma += (teta**(i * 2)) / (fatorial(2 * i))

print(valor_esperado)
print(soma)