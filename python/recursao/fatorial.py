"""
Algoritmo que lê um número do usuário e apresenta o resultado
do fatorial utilizando recursão.
"""

def fatorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * fatorial(n - 1)

n = int(input("Digite um número para calcular seu fatorial: "))

resultado = fatorial(n)

if resultado is None:
    print("Número inválido. O fatorial não é definido para números negativos.")
else:
    print(f"Resultado = {resultado}")