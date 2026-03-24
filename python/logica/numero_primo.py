"""
Com baseno número fornecido pelo usuário, verifique se o número é primo.
"""

numero = int(input("Digite um número: "))
cont = 0

if numero <= 1:
    print("Números primos são positivos acima de 1.")
else:
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1

    if cont == 2:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
