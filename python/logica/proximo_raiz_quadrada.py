"""
Algoritmo que calcule um número inteiro que mais se aproxime da raiz quadrada
de um número fornecido pelo usuário.
"""

raiz = int(input("Digite um número: "))
numero = 0

while numero * numero <= raiz:
    numero = numero + 1

numero -= 1

print(f"O número inteiro que mais se aproxima da raiz de {raiz} é {numero}")