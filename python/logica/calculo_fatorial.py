"""
Elaboração de algoritmo para o calculo de um número fatorial
com base no número inserido pelo usuário.
"""

n = int(input("Digite um número para calcular seu fatorial: "))

if n < 0:
    print("Fatorial é válido apenas para números positivos.")
else:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    print(f"Resultado: {resultado}")
