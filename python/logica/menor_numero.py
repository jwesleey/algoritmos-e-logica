"""
Encontrar o menor número de uma lista
"""

lista = [7, 9, 14, 6, 3]
menor = lista[0]

for numero in lista:
    if numero < menor:
        menor = numero

print(menor)
