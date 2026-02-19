"""
Problema: utilizar a seleção encadeada pra retornar ao usuário os tipos de triângulos.
Equilátero = todos os lados iguais.
Isósceles = dois lados iguais.
Escaleno = lados com medidas diferentes.
O que descaracteriza um triângulo: A medida de 1 lado deve ser estritamente menor do que a soma dos outros lados a < b + c.
"""
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a < b + c and b < a + c and c < b + a:
    if (a == b) and (b == c):
        print("Triângulo Equilátero.")
    elif a == b or b == c or c == a:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Não é um triângulo.")
