"""
Elaborar um algoritmo que leia dois números inteiros positivos
e determine o Máximo Divisor Comum (MDC) entre eles.
Ao final, exibir o MDC encontrado.
"""
n1 = int(input("Numero: "))
n2 = int(input("Numero: "))
i = min(n1, n2)

while n1 % i != 0 or n2 % i != 0:
    i -=1

print(f"MDC: {i}")
