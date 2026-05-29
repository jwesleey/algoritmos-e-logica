"""
Elaborar um algoritmo que apresente uma tabela de conversão
de temperaturas em graus Fahrenheit para graus Celsius.

A tabela deve exibir os valores de 50°F até 150°F,
utilizando estrutura de repetição.

A conversão deve ser realizada utilizando a fórmula:

C = 5/9 * (F - 32)

Ao final, exibir cada temperatura Fahrenheit acompanhada
de seu valor correspondente em Celsius.
"""
for f in range(50, 151):
    c = 5 / 9 * (f - 32)
    print(f"{f}ºF -> {c:.1f}ºC")
