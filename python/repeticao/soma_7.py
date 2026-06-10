"""
Considere o lançamento simultâneo de dois dados de seis faces.

Elabore um algoritmo que apresente todas as combinações possíveis
dos valores obtidos nos dois dados cuja soma seja igual a 7.

Para cada combinação encontrada, exiba os valores obtidos em cada dado
e a soma correspondente.

Exemplo de saída:

Dado 1: 1 + Dado 2: 6 = 7
Dado 1: 2 + Dado 2: 5 = 7
...
"""
for i in range(1, 7):
    for j in range (1, 7):
        if i + j == 7:
            print(f"Dado 1: {i} + Dado 2: {j} = 7")