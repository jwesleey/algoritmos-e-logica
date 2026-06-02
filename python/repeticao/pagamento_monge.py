"""
Um monge propôs a rainha um pagamento em grãos de trigo
dispostos sobre um tabuleiro de xadrez.

Na primeira casa deve ser colocado 1 grão e, em cada
casa seguinte, o dobro da quantidade da casa anterior.

Elaborar um algoritmo que calcule a quantidade total de
grãos que o monge espera receber ao final das 64 casas
do tabuleiro.

Utilizar estruturas de repetição para realizar os cálculos
e exibir o total de grãos acumulados.
"""
graos = 1
total = 0
for i in range(1, 65):
    print(f"Casa: {i} tem {graos}")
    total += graos
    graos *= 2

print(f"Soma de grãos: {total}")

