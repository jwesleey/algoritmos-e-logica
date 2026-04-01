"""
Algoritmo capaz de inverter um número de 3 digitos apresentado pelo usuário.
123 -> 321
"""

numero = int(input("Digite um número de 3 digitos: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100)

invertido = unidade * 100 + dezena * 10 + centena

print(f"Número digitado: {numero}\nNúmero invertido: {invertido}")