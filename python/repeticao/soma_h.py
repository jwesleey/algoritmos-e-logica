"""
Elaborar um algoritmo que calcule o valor da série H:

H = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

O programa deve somar todos os termos da série e exibir o valor final de H.

Observação:
- O numerador deve seguir a sequência dos números ímpares.
- O denominador deve variar de 1 até 50.
"""
h = 0
numerador = 1
denominador = 1

for denominador in range(1, 51):
    print(f"{numerador}/{denominador}")
    h += numerador / denominador
    numerador += 2


print(f"Resultado H = {h}")