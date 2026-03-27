"""
Algoritmo para ler 20 números inteiros e mostrar o maior e menor valor.
Utilizar Repetição e Decisão.
"""

numero = 0
maior = 0
menor = 0

for i in range(20):
    numero = int(input("Digite um número: "))

    if i == 0:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"O maior número digitado foi: {maior}.\nO menor número digitado foi: {menor}.")