"""
Elaborar um algoritmo que calcule a soma dos 10 primeiros termos da série:

S = 2/500 - 5/450 + 2/400 - 5/350 + ...

Observações:
- Os numeradores alternam entre 2 e 5.
- Os sinais alternam entre positivo e negativo.
- Os denominadores iniciam em 500 e diminuem de 50 em 50.
- Ao final, exibir o valor da soma da série.
"""
soma = 0
denominador = 500

for i in range(1, 11):

    if i % 2 == 1:
        soma += 2 / denominador
        print(f"2/{denominador}")
    else:
        soma -= 5 / denominador
        print(f"5/{denominador}")

    denominador -= 50

print(soma)