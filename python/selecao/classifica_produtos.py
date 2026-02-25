"""
Algoritmo que lê um número do usuário e determina a classificação do produto.
"""

n = int(input("Digite o número para verificar a classificação: "))

match n:
    case 1:
        print("Alimento não perecível.")
    case 2 | 3 | 4:
        print("Alimento perecível.")
    case 5 | 6:
        print("Vestuário.")
    case 7:
        print("Higiene Pessoal.")
    case _ if 8 <= n <= 15: # significa: n é MAIOR OU IGUAL a 8 E MENOR OU IGUAL a 15 (mesma coisa que n >= 8 and n <= 15)
        print("Limpeza e utensílios domésticos.")
    case _:
        print("Inválido")
