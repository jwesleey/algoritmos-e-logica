"""
Elaborar um algoritmo que leia uma base e um expoente inteiros
e calcule o valor da potência correspondente.

O cálculo deve ser realizado utilizando estruturas de repetição
e multiplicações sucessivas, sem utilizar o operador de potência (**).

Ao final, exibir o resultado da potenciação.
"""
base = int(input("Base: "))
expoente = int(input("Expoente: "))
resultado = 1

for _ in range(1, expoente + 1):
    resultado *= base

print(resultado)
