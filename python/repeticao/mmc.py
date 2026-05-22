"""
Elaborar um algoritmo que leia dois números inteiros positivos
e determine o Mínimo Múltiplo Comum (MMC) entre eles.
Ao final, exibir o MMC encontrado.
"""
n1 = int(input("Numero: "))
n2 = int(input("Numero: "))
i = max(n1, n2)

while i % n1 != 0 or i % n2 != 0:
    i += 1

print(f"MMC: {i}")