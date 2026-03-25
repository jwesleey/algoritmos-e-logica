"""
Com base em um número fornecido pelo usuário realizar a soma harmônica.
"""
n = int(input("informe um número: "))

if n <= 0:
    print("Informe um número maior que 0.")
else:
    h = 0
    for i in range(1, n + 1):
        h = h + 1 / i

    print(f"Soma harmônica: {h}")