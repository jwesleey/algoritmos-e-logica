"""
Elaborar um algoritmo que leia um conjunto de números inteiros positivos
informados pelo usuário e determine o maior e o menor valor digitados.

A entrada de dados deve continuar até que o usuário informe o valor -1,
utilizado como sentinela para encerrar o conjunto.

Ao final, exibir o maior e o menor número do conjunto.
"""
n = int(input("Número: "))

if n < 0:
    print("Inválido, digite valores inteiros e positivos. E -1 para fechar o conjunto.")
else:
    maior, menor = n, n
    while n != -1:

        if n > maior:
            maior = n

        if n < menor:
            menor = n

        n = int(input("Número: "))

        while n < -1:
            n = int(input("Inválido, digite um valor inteiro positivo: "))

    print(f"Maior: {maior}\nMenor: {menor}")