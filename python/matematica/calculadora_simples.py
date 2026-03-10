"""
Elaborar um algoritmo que leia 2 números inteiros e a operação aritmética desejada e calcular a resposta adequada.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = str(input("Informe a operação ( + - * / ) "))

match operacao:
    case "+":
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    case "/":
        if num2 == 0:
            print("Erro: divisão por zero")
        else:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
    case _:
        print("Operação Inválida.")
