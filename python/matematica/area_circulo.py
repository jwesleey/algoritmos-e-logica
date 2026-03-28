"""
Algoritmo que calcule a área de um círculo qualquer de um raio fornecido.
"""

from math import pi

raio = float(input("Digite o raio do círculo: "))

if raio <= 0:
    print("Inválido.")
else:
    area = pi * (raio ** 2)
    print(f"Área do circulo: {area:.2f}cm²")