import math

"""
Problema: Calcular o volume de uma esfera a partir do raio.

Fórmula matemática:
V = 4/3 * π * r³
"""

raio = float(input("Digite o raio da esfera: "))

if raio <= 0:
    print("O raio não pode ser menor ou igual a 0")
else:
    volume = (4 / 3) * math.pi * raio ** 3
    print(f"Volume = {volume:.2f} unidades cúbicas.")