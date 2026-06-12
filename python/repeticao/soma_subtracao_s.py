"""
Elaborar um algoritmo que calcule o valor da série S:

S = -1/1 + 2/4 - 3/9 + 4/16 - 5/25 + ... + 10/100

O programa deve somar todos os termos da série,
alternando os sinais entre negativo e positivo,
e exibir o resultado final de S.
"""
s = 0

for numerador in range(1, 11):
    denominador = numerador * numerador

    if numerador % 2 == 1:
        s -= numerador / denominador
    else:
        s += numerador / denominador

print(f"Resultado S = {s}")