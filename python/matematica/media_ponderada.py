"""
Algoritmo que calcule a média ponderada entre cinco números quaisquer, senod que os pesos a serem aplicados
são 1, 2, 3 ,4 e 5 respectivamente.
Estrutura Sequencial.
"""

soma = 0
divisor = 0

for i in range(1, 6):
    numero = float(input("Digite um número: "))

    soma += numero * i
    divisor += i

media_ponderada = soma/divisor

print(f"Média ponderada: {media_ponderada:.2f}")