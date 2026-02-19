"""
Problema: receber do usuário 3 valores inteiros diferentes e exibi-los de forma descrescente.
Utilizar o método de seleção encadeada.
"""
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))

if a == b or b == c or c == a:
    print(f"Os valores devem ser diferentes.")
else:
    if a > b and a > c:
        if b > c:
            print(f"{a, b, c}")
        else:
            print(f"{a, c, b}")
    elif b > a and b > c:
        if a > c:
            print(f"{b, a, c}")
        else:
            print(f"{b, c, a}")
    else:
        if a > b:
            print(f"{c, a, b}")
        else:
            print(f"{c, b, a}")
