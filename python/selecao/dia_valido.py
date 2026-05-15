"""
Algoritmo que lê uma data fornecida pelo usuário
e verifica se ela é válida, considerando:
- meses com 30 e 31 dias
- ano bissexto
- quantidade correta de dias em fevereiro

Ao final, exibe a data formatada caso seja válida.
"""
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

valido = False

if mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31:
    valido = True
elif mes in [4, 6, 9, 11] and 1 <= dia <= 30:
    valido = True
elif mes == 2:
    if (bissexto and 1 <= dia <= 29) or (not bissexto and 1 <= dia <= 28):
        valido = True

if valido:
    print(f"Válido.\n{dia:02d}/{mes:02d}/{ano:04d}")
else:
    print(f"Data informada inválida:\n{dia:02d}/{mes:02d}/{ano:04d}")
